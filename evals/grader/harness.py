#!/usr/bin/env python3
"""OKR-Ninja evaluation harness (Python 3 standard library only).

Subcommands
  check        validate the JSON keys: schema, anchors, catalog partition and coverage,
               generated answer-key freshness, reference-overlap pointers, triage rules
  render-key   regenerate a fixture's "## Answer key" section from its JSON key
  plan         create or resume a batch: sliced inputs, skill snapshots, prompts,
               batch.json; print the pending runs
  record       write a run's provenance (model, tokens, wall time) next to its report
  grade        grade one run directory (or an explicit report/input/key triple)
  aggregate    build scorecard.json for a batch and print the scorecard table
  compare      apply the regression rule between the two arms of a batch
  selftest     grade the bundled self-test cases and diff against expected results

Design: openspec/changes/add-eval-harness/design.md
Contract: openspec/changes/add-eval-harness/specs/eval-harness/spec.md
"""
from __future__ import annotations

import argparse
import bisect
import datetime as _dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HARNESS_VERSION = 2
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
KEYS_DIR = ROOT / "evals" / "keys"
PROMPTS_DIR = ROOT / "evals" / "prompts"
RUNS_DIR = ROOT / "evals" / "runs"
SELFTEST_DIR = HERE / "selftest"
RUBRIC = ROOT / "references" / "goodness-rubric.md"
TAXONOMY = ROOT / "references" / "alignment-taxonomy.md"
ANSWER_KEY_HEADING = "## Answer key (planted defects)"
DIMENSIONS = ["O1", "O2", "O3", "O4", "K1", "K2", "K3", "K4", "K5", "K6", "K7"]
MODES = ("portfolio", "single-team")
BUCKETS = ("fixture-ambiguous", "rubric-gap", "skill-error")
TRIAGE_STATUS = ("known-red", "fixed")


class Fail(Exception):
    """A user-facing failure; the message is printed and the command exits 1."""


# ----------------------------------------------------------------- utilities

def now_iso():
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_text(p):
    return Path(p).read_text(encoding="utf-8")


def write_text(p, s):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def load_json(p):
    return json.loads(read_text(p))


def dump_json(p, obj):
    write_text(p, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=str(cwd or ROOT), capture_output=True, text=True)
    if r.returncode != 0:
        raise Fail("git %s failed: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout.strip()


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


def row_family(row_id):
    return "AP" if row_id.startswith("G") else "AL"


def anchor_label(a):
    return a.get("item") or ("section " + a.get("section", "?"))


# ------------------------------------------------------------------- catalog

AP_HEAD = re.compile(r"^### (AP-\d{2}) · (.+?) — \*\*(Critical|Major|Minor)\*\*\s*$")
AL_HEAD = re.compile(r"^### (AL-\d{2}) — (.+?)\s*$")


def load_catalog():
    """ID -> {name, severity} from the two owning reference files."""
    cat = {}
    for line in read_text(RUBRIC).splitlines():
        m = AP_HEAD.match(line)
        if m:
            cat[m.group(1)] = {"name": m.group(2).strip(), "severity": m.group(3)}
    for line in read_text(TAXONOMY).splitlines():
        m = AL_HEAD.match(line)
        if m:
            cat[m.group(1)] = {"name": m.group(2).strip(), "severity": None}
    if not cat:
        raise Fail("no catalog headings found in references/")
    return cat


# ------------------------------------------------------------- normalisation

_TYPO = {
    "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
    "‘": "'", "’": "'", "‚": "'",
    "—": "-", "–": "-", "‑": "-", "−": "-",
    "…": "...",
    "↔": "<->", "→": "->", "←": "<-",
    " ": " ",
}
_TYPO_RE = re.compile("|".join(re.escape(k) for k in _TYPO))
_OUTER = "\"'*_` \t"
QCHARS = "\"“”„«»"
QSPLIT = re.compile("[%s]" % QCHARS)


def typo(s):
    """Level-1 normalisation: typographic variants to ASCII, whitespace collapsed."""
    s = _TYPO_RE.sub(lambda m: _TYPO[m.group(0)], s)
    return re.sub(r"\s+", " ", s).strip()


def norm1(span):
    """A quoted span as compared for a verbatim hit: typo() plus its own outer quotes/emphasis stripped."""
    return typo(typo(span).strip(_OUTER))


def strip_marks(s):
    return s.replace("*", "").replace("`", "").replace('"', "")


def norm2(s):
    """Level-2 normalisation for near-miss: emphasis, backticks and quote characters removed,
    leading/trailing punctuation dropped."""
    s = strip_marks(typo(s))
    s = re.sub(r"[\s.;,:!?]+$", "", s)
    s = re.sub(r"^[\s.;,:]+", "", s)
    return re.sub(r"\s+", " ", s).strip()


# ------------------------------------------------------------------ documents

ITEM_KR = re.compile(r"^\s*-\s*\*\*(KR [A-Z]+\d+(?:\.\d+)?):\*\*")
ITEM_OBJ = re.compile(r"^###\s+(Objective [A-Z]+\d+)\b")
H2 = re.compile(r"^##\s+(.*\S)\s*$")
H1 = re.compile(r"^#\s+")


class Doc:
    """A markdown document (fixture body or sliced input) with line-level indexes."""

    def __init__(self, lines):
        self.lines = list(lines)
        self.items = {}      # marker -> [line index]
        self.item_at = {}    # line index -> marker
        self.h2 = []         # [(line index, heading text)]
        for i, ln in enumerate(self.lines):
            m = ITEM_KR.match(ln) or ITEM_OBJ.match(ln)
            if m:
                self.items.setdefault(m.group(1), []).append(i)
                self.item_at[i] = m.group(1)
            m2 = H2.match(ln)
            if m2:
                self.h2.append((i, m2.group(1)))
        self.section_at = []
        cur = None
        starts = {i: t for i, t in self.h2}
        for i in range(len(self.lines)):
            if i in starts:
                cur = starts[i]
            self.section_at.append(cur)
        self.text1, self.off1 = self._join(typo)
        self.text2, self.off2 = self._join(lambda s: strip_marks(typo(s)))

    def _join(self, fn):
        parts, offs, pos = [], [], 0
        for ln in self.lines:
            t = fn(ln)
            offs.append(pos)
            parts.append(t)
            pos += len(t) + 1
        return " ".join(parts), offs

    @staticmethod
    def _line_of(offs, pos):
        return bisect.bisect_right(offs, pos) - 1

    def find1(self, needle):
        p = self.text1.find(needle)
        return None if p < 0 else self._line_of(self.off1, p)

    def find2(self, needle):
        p = self.text2.find(needle)
        return None if p < 0 else self._line_of(self.off2, p)

    @staticmethod
    def _all(text, needle):
        out, p = [], text.find(needle)
        while p >= 0:
            out.append(p)
            p = text.find(needle, p + 1)
        return out

    def lines1(self, needle):
        return sorted({self._line_of(self.off1, p) for p in self._all(self.text1, needle)})

    def lines2(self, needle):
        return sorted({self._line_of(self.off2, p) for p in self._all(self.text2, needle)})

    def find_ellipsis(self, needle2):
        pieces = [p.strip() for p in needle2.split("...") if len(p.strip()) >= 3]
        if len(pieces) < 2:
            return None
        pos, first = 0, None
        for pc in pieces:
            q = self.text2.find(pc, pos)
            if q < 0:
                return None
            if first is None:
                first = q
            pos = q + len(pc)
        return self._line_of(self.off2, first)

    def section_index(self, prefix):
        return [i for (i, t) in self.h2 if t.startswith(prefix)]

    def section_range(self, h2_line):
        idx = [i for (i, _) in self.h2]
        k = idx.index(h2_line)
        end = idx[k + 1] if k + 1 < len(idx) else len(self.lines)
        return range(h2_line, end)

    @staticmethod
    def section_short(text):
        if text is None:
            return None
        if text.startswith("Company"):
            return "Company"
        if text.startswith("Appendix"):
            return "Appendix"
        return re.split(r" — | \(", text)[0].strip()


class Fixture:
    """A fixture file split into body (source of truth for quotes) and the generated key section."""

    def __init__(self, path):
        self.path = Path(path)
        self.text = read_text(self.path)
        self.lines = self.text.split("\n")
        try:
            self.key_line = next(i for i, ln in enumerate(self.lines) if ln.strip() == ANSWER_KEY_HEADING)
        except StopIteration:
            raise Fail("%s: missing '%s' heading" % (rel(path), ANSWER_KEY_HEADING))
        body = self.lines[: self.key_line]
        while body and body[-1].strip() in ("", "---"):
            body.pop()
        self.body_lines = body
        self.body = Doc(body)
        self.head_text = "\n".join(self.lines[: self.key_line])
        self.key_text = "\n".join(self.lines[self.key_line:])

    def write_key_section(self, rendered):
        write_text(self.path, self.head_text + "\n" + rendered)


KEY_CLAUSE = re.compile(r",?\s*and deliberately contains planted defects\s*—\s*see the answer key at the bottom\.?.*$")


def scrub_intro(lines):
    """Drop the fixture intro's pointer to the answer key so the input never invites a runner to look for it."""
    out = []
    for ln in lines:
        if ln.startswith("> **Fictional test fixture") and KEY_CLAUSE.search(ln):
            ln = KEY_CLAUSE.sub("", ln).rstrip()
            if not ln.endswith("."):
                ln += "."
        out.append(ln)
    return out


def build_input_lines(fx, slice_spec=None):
    """The sliced input a run reads: fixture body without the key (and without the intro's pointer to it),
    cut to a slice's sections."""
    if not slice_spec:
        return scrub_intro(fx.body_lines)
    out = []
    h1 = next((ln for ln in fx.body_lines if H1.match(ln)), None)
    body = scrub_intro(fx.body_lines)
    if h1:
        out.append(h1)
    for prefix in slice_spec["input_sections"]:
        hits = fx.body.section_index(prefix)
        if len(hits) != 1:
            raise Fail("slice section prefix %r resolves to %d headings in %s" % (prefix, len(hits), rel(fx.path)))
        seg = [body[i] for i in fx.body.section_range(hits[0])]
        while seg and seg[-1].strip() in ("", "---"):
            seg.pop()
        if out:
            out.append("")
        out.extend(seg)
    return out


# ----------------------------------------------------------------------- keys

def key_files():
    return sorted(KEYS_DIR.glob("*.json"))


def load_keys():
    keys = []
    for p in key_files():
        k = load_json(p)
        k["_path"] = str(p)
        keys.append(k)
    return keys


def key_hash(k):
    return sha256_file(k["_path"])


def slice_registry(keys):
    """slice id -> {key, slice (spec or None), mode, team}."""
    reg = {}
    for k in keys:
        reg["%s-portfolio" % k["id"]] = {"key": k, "slice": None, "mode": k.get("mode", "portfolio"), "team": None}
        for name, sp in (k.get("slices") or {}).items():
            reg["%s-%s" % (k["id"], name)] = {"key": k, "slice": sp, "mode": sp["mode"], "team": sp.get("team")}
    return reg


def resolve_anchor(anchor, doc):
    """-> (kind, set of line indexes or None when unresolvable, raw hits)."""
    if "item" in anchor:
        hits = doc.items.get(anchor["item"], [])
        return "item", (set(hits) if len(hits) == 1 else None), hits
    if "section" in anchor:
        hits = doc.section_index(anchor["section"])
        return "section", (set(doc.section_range(hits[0])) if len(hits) == 1 else None), hits
    raise Fail("anchor must carry 'item' or 'section': %r" % (anchor,))


def validate_key(k, path, catalog):
    errs = []
    where = rel(path)

    def err(msg):
        errs.append("%s: %s" % (where, msg))

    for field in ("id", "fixture", "universe", "budget", "criterion", "defects", "non_defects", "not_covered"):
        if field not in k:
            err("missing field %r" % field)
    if errs:
        return errs
    if not isinstance(k["budget"], int):
        err("budget must be an integer")
    fixture_path = ROOT / k["fixture"]
    if not fixture_path.exists():
        err("fixture %s does not exist" % k["fixture"])
        return errs
    fx = Fixture(fixture_path)
    seen = set()
    accepted_all = set()
    for d in k["defects"]:
        rid = d.get("id", "?")
        if rid in seen:
            err("duplicate defect id %s" % rid)
        seen.add(rid)
        if not re.match(r"^[GA]\d+$", rid):
            err("defect id %r must look like G1 or A1" % rid)
        acc = d.get("accepted") or []
        if not acc:
            err("%s: accepted list is empty" % rid)
        for i in acc:
            if i not in catalog:
                err("%s: accepted id %s is not in the catalog" % (rid, i))
            elif i[:2] != row_family(rid):
                err("%s: accepted id %s does not match row family" % (rid, i))
        accepted_all |= set(acc)
        for field in ("location", "note"):
            if not isinstance(d.get(field), str) or not d[field].strip():
                err("%s: %s must be a non-empty string" % (rid, field))
        if not d.get("evidence"):
            err("%s: evidence anchors are empty" % rid)
        for a in d.get("evidence", []):
            kind, lineset, hits = resolve_anchor(a, fx.body)
            if lineset is None:
                err("%s: %s anchor %r resolves to %d lines (need exactly 1)" % (rid, kind, anchor_label(a), len(hits)))
        ro = d.get("reference_overlap")
        if ro:
            f = ROOT / ro.get("file", "")
            if not f.exists():
                err("%s: reference_overlap file %s does not exist" % (rid, ro.get("file")))
            elif ro.get("quote", "") not in read_text(f):
                err("%s: reference_overlap quote %r not found in %s" % (rid, ro.get("quote"), ro.get("file")))
    for nd in k["non_defects"]:
        nid = nd.get("id", "?")
        for i in nd.get("forbid", []):
            if i not in catalog:
                err("%s: forbid id %s is not in the catalog" % (nid, i))
        if not nd.get("forbid"):
            err("%s: forbid list is empty" % nid)
        if not isinstance(nd.get("text"), str) or not nd["text"].strip():
            err("%s: text must be a non-empty string" % nid)
        for a in nd.get("at", []):
            kind, lineset, hits = resolve_anchor(a, fx.body)
            if lineset is None:
                err("%s: %s anchor %r resolves to %d lines" % (nid, kind, anchor_label(a), len(hits)))
    nc = set(k["not_covered"])
    for i in nc:
        if i not in catalog:
            err("not_covered id %s is not in the catalog" % i)
    overlap = nc & accepted_all
    if overlap:
        err("not_covered overlaps accepted ids: %s" % ", ".join(sorted(overlap)))
    gap = set(catalog) - nc - accepted_all
    if gap:
        err("catalog ids neither planted nor listed as not covered: %s" % ", ".join(sorted(gap)))
    for name, sp in (k.get("slices") or {}).items():
        if sp.get("mode") not in MODES:
            err("slice %s: mode must be one of %s" % (name, MODES))
        for prefix in sp.get("input_sections", []):
            if len(fx.body.section_index(prefix)) != 1:
                err("slice %s: input section prefix %r does not resolve to exactly one heading" % (name, prefix))
        for rid in sp.get("expected", []):
            if rid not in seen:
                err("slice %s: expected row %s is not a defect id" % (name, rid))
        if not isinstance(sp.get("budget"), int):
            err("slice %s: budget must be an integer" % name)
        r = sp.get("render") or {}
        for field in ("title", "intro", "run", "must"):
            if field not in r:
                err("slice %s: render.%s missing" % (name, field))
    tseen = set()
    for t in k.get("triage", []):
        tid = t.get("id", "?")
        if tid in tseen:
            err("duplicate triage id %s" % tid)
        tseen.add(tid)
        for field in ("finding", "anchor", "bucket", "decision", "rationale", "status"):
            if field not in t:
                err("triage %s: missing %s" % (tid, field))
        if t.get("finding") not in catalog:
            err("triage %s: finding %s is not in the catalog" % (tid, t.get("finding")))
        if t.get("bucket") not in BUCKETS:
            err("triage %s: bucket must be one of %s" % (tid, BUCKETS))
        if t.get("status") not in TRIAGE_STATUS:
            err("triage %s: status must be one of %s" % (tid, TRIAGE_STATUS))
        if not str(t.get("rationale", "")).strip():
            err("triage %s: rationale is required" % tid)
        if t.get("bucket") == "skill-error" and t.get("status") == "known-red":
            err("triage %s: a skill-error entry cannot be known-red" % tid)
        if isinstance(t.get("anchor"), dict):
            kind, lineset, hits = resolve_anchor(t["anchor"], fx.body)
            if lineset is None:
                err("triage %s: anchor %r resolves to %d lines" % (tid, anchor_label(t["anchor"]), len(hits)))
    return errs


# -------------------------------------------------------------- key rendering

NUM_WORDS = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 21: "Twenty-one", 22: "Twenty-two",
    23: "Twenty-three", 24: "Twenty-four", 25: "Twenty-five", 26: "Twenty-six", 27: "Twenty-seven",
    28: "Twenty-eight", 29: "Twenty-nine", 30: "Thirty",
}


def oxford(items):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    if len(items) == 2:
        return "%s or %s" % tuple(items)
    return ", ".join(items[:-1]) + ", or " + items[-1]


def id_cell(d, catalog):
    primary = d["accepted"][0]
    cell = "%s · %s" % (primary, catalog[primary]["name"])
    if d.get("alternate_note"):
        cell += " *(%s)*" % d["alternate_note"]
    return cell


def render_key_section(k, catalog):
    g = [d for d in k["defects"] if d["id"].startswith("G")]
    a = [d for d in k["defects"] if d["id"].startswith("A")]
    n = len(k["defects"])
    out = [ANSWER_KEY_HEADING, ""]
    out.append(
        "**%s planted defects: G1–G%d (goodness) and A1–A%d (alignment).** Every row cites its canonical ID "
        "and name from `references/goodness-rubric.md` (AP-XX) or `references/alignment-taxonomy.md` (AL-XX). "
        "Locations reference the sections above; a compliant report quotes the exact objective/KR text with a "
        "source ref (format in `references/report-format.md`)." % (NUM_WORDS[n], len(g), len(a)))
    out += ["", "### Goodness defects", "", "| # | ID · Anti-pattern | Location | What's wrong |", "|---|---|---|---|"]
    for d in g:
        out.append("| %s | %s | %s | %s |" % (d["id"], id_cell(d, catalog), d["location"], d["note"]))
    out += ["", "### Alignment defects", "", "| # | ID · Failure mode | Location(s) | What's wrong |", "|---|---|---|---|"]
    for d in a:
        out.append("| %s | %s | %s | %s |" % (d["id"], id_cell(d, catalog), d["location"], d["note"]))
    out += ["", "### Intentional non-defects (do not report)", "",
            "Near-misses planted to measure false-positive discipline. Reporting one of these counts against the "
            "extra-findings budget in the eval criterion.", ""]
    for i, nd in enumerate(k["non_defects"], 1):
        out.append("%d. %s" % (i, nd["text"]))
    triage = k.get("triage") or []
    if triage:
        out += ["", "### Triage entries", "",
                "Recurring findings beyond the key, each classified once so the same debate is not re-had. "
                "A **known-red** entry is reported by the grader but excluded from the extra-findings budget until "
                "its fix lands; a **fixed** entry no longer affects counting.", ""]
        for i, t in enumerate(triage, 1):
            out.append("%d. **%s · %s on %s** — bucket: %s · status: %s · decision: %s · rationale: %s" % (
                i, t["id"], t["finding"], anchor_label(t["anchor"]), t["bucket"], t["status"], t["decision"],
                t["rationale"]))
    al = [x for x in k["not_covered"] if x.startswith("AL")]
    ap = [x for x in k["not_covered"] if x.startswith("AP")]
    out += ["", "### Modes deliberately not covered", "",
            "The fixture plants no instance of **%s** (nor of anti-patterns %s)%s. A finding citing any of them is "
            "off-key and counts against the extra-findings budget." % (oxford(al), ", ".join(ap), k.get("not_covered_note", ""))]
    alt = (" (where a row accepts either of two IDs, either passes — counted once)"
           if any(len(d["accepted"]) > 1 for d in k["defects"]) else "")
    kr = (" — except findings covered by an active known-red triage entry (see Triage entries), which are reported "
          "but not counted" if any(t.get("status") == "known-red" for t in triage) else "")
    out += ["", "### Eval criterion", "", "A passing portfolio review must:", "",
            "1. surface **all %d planted defects, cited by canonical ID**%s, each with correct verbatim quotes and "
            "source refs;" % (n, alt),
            "2. contain **zero fabricated quotes** — every quoted span must exist character-for-character in this file;",
            "3. raise **no more than %d findings beyond this key** (the stated budget), with any reported item from "
            "the Intentional non-defects list counting against that budget%s." % (k["budget"], kr)]
    for name, sp in (k.get("slices") or {}).items():
        r = sp["render"]
        out += ["", "### %s" % r["title"], "", r["intro"], "", "**Run:** %s" % r["run"], "",
                "A passing single-team review must:", ""]
        for i, m in enumerate(r["must"], 1):
            out.append("%d. %s" % (i, m))
    return "\n".join(out) + "\n"


# --------------------------------------------------------------- report parse

HEADING = re.compile(r"^(#{2,4})\s*\[(Critical|Major|Minor)\]\s*((?:AP|AL)-\d{2})\b\s*(.*)$")
ANY_HEADING = re.compile(r"^#{1,6}\s")
REF_GROUP = re.compile(r"\((?:[^()]|\([^()]*\))*\)")
REF_LINE = re.compile(r"\bline\s+(\d+)")


def is_ref(group):
    return ("›" in group) or bool(REF_LINE.search(group))


def quoted_spans(segment):
    """Quoted spans in a text segment. Sequential quote pairs by default; when the quote
    characters are unbalanced or a pair is empty (nested quotes), the outermost span wins."""
    pieces = QSPLIT.split(segment)
    nq = len(pieces) - 1
    if nq == 0:
        return []
    inner = pieces[1::2]
    if nq % 2 == 1 or any(not p.strip() for p in inner):
        idxs = [m.start() for m in QSPLIT.finditer(segment)]
        return [segment[idxs[0] + 1: idxs[-1]]] if len(idxs) >= 2 else []
    return [p for p in inner if re.search(r"[A-Za-z0-9]", p)]


def extract_spans(line):
    """-> (evidence [(text, ref, ref_line)], mentions [text]) for one report line."""
    ev, pos = [], 0
    for m in REF_GROUP.finditer(line):
        g = m.group(0)
        if not is_ref(g):
            continue
        seg = line[pos:m.start()]
        rl = REF_LINE.search(g)
        for s in quoted_spans(seg):
            ev.append((s, g[1:-1], int(rl.group(1)) if rl else None))
        pos = m.end()
    return ev, quoted_spans(line[pos:])


LABEL_RE = re.compile(r"^\s*[-*]\s*\**([^:]{1,80}?)\**\s*:")


def line_label(line):
    m = LABEL_RE.match(line)
    return m.group(1).strip() if m else ""


def is_evidence_label(label, names):
    """Evidence lines: the template's 'Evidence:' / '<Side> evidence:' lines, or a line labelled with a
    team or section name. Every other labelled line (Why, Conflict, Detection check, Disconfirming checks,
    Suggested rewrite, ...) carries supporting spans."""
    if not label:
        return False
    if re.search(r"evidence|quote", label, re.I):
        return True
    base = re.split(r"\s*[\(\[—–-]", label)[0].strip()
    return base in names


def parse_report(text, names=()):
    names = set(names)
    lines = text.split("\n")
    findings, i = [], 0
    while i < len(lines):
        m = HEADING.match(lines[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not ANY_HEADING.match(lines[j]):
            j += 1
        block = lines[i + 1: j]
        f = {"heading": lines[i].strip(), "line": i + 1, "severity": m.group(2), "id": m.group(3),
             "title": m.group(4).strip(), "evidence": [], "mentions": [], "secondary": []}
        for k, bl in enumerate(block):
            label = line_label(bl)
            if label.lower() == "also":
                for sid in re.findall(r"\b(?:AP|AL)-\d{2}\b", bl):
                    if sid != f["id"] and sid not in f["secondary"]:
                        f["secondary"].append(sid)
                continue
            ev, men = extract_spans(bl)
            role = "evidence" if is_evidence_label(label, names) else "supporting"
            for (s, ref, rl) in ev:
                f["evidence"].append({"text": s.strip(), "ref": ref, "ref_line": rl, "report_line": i + 2 + k,
                                      "role": role})
            f["mentions"].extend(x.strip() for x in men)
        findings.append(f)
        i = j
    return lines, findings


def is_short(s1):
    """A quoted span of fewer than three words is a term (a label or search word), not a quote of source text.

    The word count is the whole rule, per the eval-harness spec: a character-length escape hatch would
    exempt short 3+-word spans — exactly the shape of an invented numeric target — from the fabrication
    check, and the fabrication invariant is the one this repo cannot weaken."""
    return len(s1.split()) < 3


def pick_line(lines, ref_line):
    """One occurrence -> that line; several -> the line the source ref names, else unlocated (ambiguous)."""
    if not lines:
        return None, False
    if len(lines) == 1:
        return lines[0], False
    if ref_line and (ref_line - 1) in lines:
        return ref_line - 1, False
    return None, True


def classify_span(text, doc, body_doc, key_text2, ref_line=None):
    """-> (class, located line index or None, ambiguous). Classes: verbatim, near_miss, term, out_of_scope,
    key_leak, fabricated."""
    s1 = norm1(text)
    s2 = norm2(s1)
    if s1:
        lines = doc.lines1(s1)
        if lines:
            ln, amb = pick_line(lines, ref_line)
            return "verbatim", ln, amb
    if s2:
        lines = doc.lines2(s2)
        if lines:
            ln, amb = pick_line(lines, ref_line)
            return "near_miss", ln, amb
        ln = doc.find_ellipsis(s2)
        if ln is not None:
            return "near_miss", ln, False
    if is_short(s1):
        return "term", None, False
    if body_doc is not None and body_doc is not doc:
        if (s1 and body_doc.find1(s1) is not None) or (
                s2 and (body_doc.find2(s2) is not None or body_doc.find_ellipsis(s2) is not None)):
            return "out_of_scope", None, False
    if key_text2 and s2 and s2 in key_text2:
        return "key_leak", None, False
    return "fabricated", None, False


# ------------------------------------------------------------------ structure

def find_tables(lines, start=0, end=None):
    """-> [(header cells, first data row cells)] for pipe tables between start and end."""
    end = len(lines) if end is None else end
    tables, i = [], start
    while i < end - 1:
        if lines[i].lstrip().startswith("|") and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            data = None
            j = i + 2
            while j < end and lines[j].lstrip().startswith("|"):
                data = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                break
            tables.append((header, data))
            i = j + 1
        else:
            i += 1
    return tables


def clean_cell(c):
    return re.sub(r"[*`_]", "", c).strip()


def check_dimension_table(header, label):
    dims = [clean_cell(c) for c in header[1:]]
    if dims != DIMENSIONS:
        extra = [d for d in dims if d not in DIMENSIONS]
        missing = [d for d in DIMENSIONS if d not in dims]
        parts = []
        if extra:
            parts.append("extra column(s) %s" % ", ".join(extra))
        if missing:
            parts.append("missing column(s) %s" % ", ".join(missing))
        if not parts:
            parts.append("columns out of order: %s" % ", ".join(dims))
        return "%s columns are not exactly O1-O4, K1-K7: %s" % (label, "; ".join(parts))
    return None


def check_structure(lines, findings, mode, slice_spec, text):
    fails, warns = [], []
    if not findings:
        fails.append("no findings parsed (no heading in the mandated '### [Severity] AP-XX ...' form)")
    for f in findings:
        if not f["evidence"]:
            fails.append("finding without evidence: %s" % f["heading"])
        for e in f["evidence"]:
            if e.get("ref_line_ok") is False:
                warns.append("ref says line %s but quote is on input line %s: %s" % (
                    e["ref_line"], e["input_line"], f["heading"]))
            if e.get("class") == "unverified":
                warns.append("unverified supporting quote %r: %s" % (e["text"][:60], f["heading"]))
            if e.get("ambiguous"):
                warns.append("quote occurs on several input lines and the ref names none of them, not anchored: %r (%s)" % (
                    e["text"][:60], f["heading"]))
    numbered = []
    for ln in lines:
        m = re.match(r"^##\s+(\d+)\.\s*(.*)$", ln)
        if m:
            numbered.append((int(m.group(1)), m.group(2)))
    if mode == "portfolio":
        nums = [n for n, _ in numbered]
        if nums != [1, 2, 3, 4, 5, 6]:
            fails.append("portfolio sections numbered %s, expected 1-6 in order" % nums)
        s2 = next((i for i, ln in enumerate(lines) if re.match(r"^##\s+2\.", ln)), None)
        s3 = next((i for i, ln in enumerate(lines) if re.match(r"^##\s+3\.", ln)), None)
        tables = find_tables(lines, s2, s3) if s2 is not None else []
        if not tables:
            fails.append("no heatmap table found in section 2")
        else:
            msg = check_dimension_table(tables[0][0], "heatmap")
            if msg:
                fails.append(msg)
        for f in findings:
            if f["id"].startswith("AL"):
                secs = {e["section"] for e in f["evidence"] if e.get("input_line")}
                if len(secs) < 2:
                    fails.append("one-sided alignment evidence (%d section): %s" % (len(secs), f["heading"]))
    else:
        for f in findings:
            if f["id"].startswith("AL"):
                fails.append("AL block in single-team report: %s" % f["heading"])
        if any(re.search(r"re-?run", t, re.I) for _, t in numbered):
            fails.append("re-run section present in single-team report")
        tables = find_tables(lines)
        if not tables:
            fails.append("no score table found")
        else:
            header, data = tables[0]
            msg = check_dimension_table(header, "score table")
            if msg:
                fails.append(msg)
            elif slice_spec and slice_spec.get("o4") == "N/A":
                cell = clean_cell(data[1 + DIMENSIONS.index("O4")]) if data and len(data) > 4 else ""
                if cell.upper() != "N/A":
                    fails.append("O4 must be N/A in this slice, score table shows %r" % cell)
        if not (re.search(r"outbound dependency", text, re.I) or "No outbound dependency mentions found." in text):
            fails.append("no outbound dependency notes section")
        if slice_spec and not slice_spec.get("strategy_provided", True):
            if not re.search(r"strateg[a-z]*[^.\n]*out of scope|out of scope[^.\n]*strateg", text, re.I):
                fails.append("missing statement that company-level strategy tracing was out of scope")
    return {"pass": not fails, "failures": fails, "warnings": warns}


# --------------------------------------------------------------------- grade

def anchor_of(f, doc):
    if f["items_ordered"]:
        return f["items_ordered"][0]
    for ln in f["located_lines"]:
        sec = doc.section_short(doc.section_at[ln])
        if sec:
            return sec + (" notes" if doc.lines[ln].lstrip().startswith("*Notes") else "")
    return "unlocated"


def grade_report(report_text, key, slice_spec, input_lines, fixture, provenance):
    doc = Doc(input_lines)
    body_doc = fixture.body if fixture else None
    key_text2 = strip_marks(typo(fixture.key_text)) if fixture else ""
    mode = slice_spec["mode"] if slice_spec else key.get("mode", "portfolio")
    budget = slice_spec["budget"] if slice_spec else key["budget"]
    expected = slice_spec["expected"] if slice_spec else [d["id"] for d in key["defects"]]
    rows = {d["id"]: d for d in key["defects"] if d["id"] in expected}
    names = {doc.section_short(t) for _, t in doc.h2} | {"Company", "Appendix"}
    lines, findings = parse_report(report_text, names)

    for f in findings:
        f["items_ordered"], f["sections"], f["located_lines"] = [], set(), []
        for e in f["evidence"]:
            cls, ln, amb = classify_span(e["text"], doc, body_doc, key_text2, e.get("ref_line"))
            e["ambiguous"] = amb
            e["key_leak"] = cls == "key_leak"
            if cls == "key_leak":
                cls = "fabricated"
            if e["role"] == "supporting" and cls == "fabricated":
                cls = "unverified"
            e["class"] = cls
            e["input_line"] = None if ln is None else ln + 1
            e["section"] = doc.section_short(doc.section_at[ln]) if ln is not None else None
            e["ref_line_ok"] = (e["ref_line"] == ln + 1) if (ln is not None and e["ref_line"]) else None
            if ln is not None:
                f["located_lines"].append(ln)
                if ln in doc.item_at and doc.item_at[ln] not in f["items_ordered"]:
                    f["items_ordered"].append(doc.item_at[ln])
                if doc.section_at[ln]:
                    f["sections"].add(doc.section_at[ln])
        f["items"] = set(f["items_ordered"])
        f["anchor"] = anchor_of(f, doc)

    row_anchors = {}
    for rid, d in rows.items():
        req = []
        for a in d["evidence"]:
            if a.get("optional"):
                continue
            kind, lineset, hits = resolve_anchor(a, doc)
            req.append((a, lineset))
        row_anchors[rid] = req

    def missing_anchors(f, rid):
        loc = set(f["located_lines"])
        return [a for a, lineset in row_anchors[rid] if lineset is None or not (loc & lineset)]

    claimed = {}
    for idx, f in enumerate(findings):
        f["match"], f["partial"] = None, []
        for cand in [f["id"]] + f["secondary"]:
            for rid, d in rows.items():
                if cand not in d["accepted"] or rid in claimed:
                    continue
                miss = missing_anchors(f, rid)
                if not miss:
                    f["match"] = {"row": rid, "matched_id": cand,
                                  "id_exact": cand == f["id"] and f["id"] == d["accepted"][0],
                                  "via_secondary": cand != f["id"]}
                    claimed[rid] = idx
                    break
                f["partial"].append({"row": rid, "id": cand, "missing": [anchor_label(a) for a in miss]})
            if f["match"]:
                break
    for f in findings:
        f["duplicate_of"] = None
        if f["match"]:
            continue
        primary = f["items_ordered"][0] if f["items_ordered"] else None
        for rid in claimed:
            d = rows[rid]
            items = {a["item"] for a in d["evidence"] if "item" in a and not a.get("optional")}
            if items and items <= f["items"] and primary in items and f["id"][:2] == row_family(rid):
                f["duplicate_of"] = rid
                break

    nd_resolved = []
    for nd in key.get("non_defects", []):
        if not nd.get("at"):
            nd_resolved.append((nd, None))
            continue
        ls = set()
        for a in nd["at"]:
            kind, lineset, hits = resolve_anchor(a, doc)
            if lineset:
                ls |= lineset
        nd_resolved.append((nd, ls))
    known_red = [t for t in key.get("triage", []) if t.get("status") == "known-red"]

    def triage_hit(f):
        for t in known_red:
            if t["finding"] != f["id"]:
                continue
            a = t["anchor"]
            if "item" in a and a["item"] in f["items"]:
                return t
            if "section" in a and any(s.startswith(a["section"]) for s in f["sections"]):
                return t
        return None

    for f in findings:
        f["flags"], f["excluded"], f["triage"], f["bucket"] = [], False, None, None
        f["kind"] = "match" if f["match"] else ("duplicate" if f["duplicate_of"] else "extra")
        loc = set(f["located_lines"])
        if f["kind"] != "match":
            for nd, ls in nd_resolved:
                if f["id"] in nd["forbid"] and (ls is None or (loc & ls)):
                    f["flags"].append("non_defect:%s" % nd["id"])
            if f["id"] in key.get("not_covered", []):
                f["flags"].append("off_key")
            t = triage_hit(f)
            if t:
                f["excluded"], f["triage"], f["bucket"] = True, t["id"], t["bucket"]
        if any(e["class"] == "out_of_scope" for e in f["evidence"]):
            f["flags"].append("out_of_scope")
        if any(e["class"] == "fabricated" for e in f["evidence"]):
            f["flags"].append("fabricated")
        if any(e["class"] == "unverified" for e in f["evidence"]):
            f["flags"].append("unverified")
        if not f["evidence"]:
            f["flags"].append("no_evidence")

    counted = [f for f in findings if f["kind"] in ("duplicate", "extra") and not f["excluded"]]
    counted += [f for f in findings if f["kind"] == "match" and "out_of_scope" in f["flags"]]
    excluded = [f for f in findings if f["excluded"]]

    rows_out = {}
    for rid in expected:
        if rid in claimed:
            f = findings[claimed[rid]]
            rows_out[rid] = {"status": "found", "matched_id": f["match"]["matched_id"], "id_exact": f["match"]["id_exact"],
                             "via_secondary": f["match"].get("via_secondary", False), "finding_line": f["line"]}
        else:
            partials = [{"finding_line": f["line"], "missing": p["missing"]}
                        for f in findings for p in f["partial"] if p["row"] == rid]
            rows_out[rid] = {"status": "partial" if partials else "missed", "matched_id": None,
                             "id_exact": False, "partials": partials}

    quotes = {"total": 0, "evidence": 0, "supporting": 0, "verbatim": 0, "near_miss": 0, "out_of_scope": 0,
              "fabricated": 0, "unverified": 0, "term": 0, "ambiguous": 0, "key_leak": 0,
              "mentions": sum(len(f["mentions"]) for f in findings), "fabricated_spans": [], "unverified_spans": []}
    for f in findings:
        for e in f["evidence"]:
            quotes["total"] += 1
            quotes[e["role"]] += 1
            quotes[e["class"]] += 1
            if e.get("ambiguous"):
                quotes["ambiguous"] += 1
            if e["key_leak"]:
                quotes["key_leak"] += 1
            if e["class"] == "fabricated":
                quotes["fabricated_spans"].append({"text": e["text"], "finding": f["heading"], "key_leak": e["key_leak"]})
            elif e["class"] == "unverified":
                quotes["unverified_spans"].append({"text": e["text"], "finding": f["heading"], "key_leak": e["key_leak"]})

    structure = check_structure(lines, findings, mode, slice_spec, report_text)
    failures = ["missed row %s (%s)" % (rid, "/".join(rows[rid]["accepted"]))
                for rid in expected if rows_out[rid]["status"] != "found"]
    if quotes["fabricated"]:
        failures.append("fabricated quotes: %d" % quotes["fabricated"])
    if len(counted) > budget:
        failures.append("budget exceeded: %d counted findings > %d" % (len(counted), budget))
    failures += [x for x in structure["failures"] if x.startswith("AL block in single-team")]

    def finding_out(f):
        return {"heading": f["heading"], "report_line": f["line"], "severity": f["severity"], "id": f["id"],
                "secondary": f["secondary"], "kind": f["kind"], "anchor": f["anchor"], "key": "%s@%s" % (f["id"], f["anchor"]),
                "match": f["match"], "duplicate_of": f["duplicate_of"], "partial": f["partial"],
                "flags": f["flags"], "excluded": f["excluded"], "triage": f["triage"], "bucket": f["bucket"],
                "evidence": [{k: e[k] for k in ("text", "role", "class", "input_line", "section", "ref_line", "ref_line_ok", "key_leak", "ambiguous")}
                             for e in f["evidence"]],
                "mentions": f["mentions"]}

    return {
        "harness_version": HARNESS_VERSION,
        "graded_at": now_iso(),
        "mode": mode,
        "provenance": provenance,
        "findings_parsed": len(findings),
        "produced": True,
        "rows": rows_out,
        "findings": [finding_out(f) for f in findings],
        "extras": [finding_out(f)["key"] for f in findings if f["kind"] == "extra" and not f["excluded"]],
        "duplicates": [finding_out(f)["key"] for f in findings if f["kind"] == "duplicate" and not f["excluded"]],
        "excluded": [finding_out(f)["key"] for f in excluded],
        "violations": {"non_defect": sum(1 for f in findings if any(x.startswith("non_defect") for x in f["flags"])),
                       "off_key": sum(1 for f in findings if "off_key" in f["flags"])},
        "budget": {"limit": budget, "counted": len(counted), "excluded": len(excluded)},
        "quotes": quotes,
        "structure": structure,
        "failures": failures,
        "pass": not failures,
    }


def not_produced_grade(provenance, mode):
    return {"harness_version": HARNESS_VERSION, "graded_at": now_iso(), "mode": mode, "provenance": provenance,
            "findings_parsed": 0, "produced": False, "rows": {}, "findings": [], "extras": [], "duplicates": [],
            "excluded": [], "violations": {"non_defect": 0, "off_key": 0}, "budget": {"limit": None, "counted": 0,
            "excluded": 0}, "quotes": {"total": 0, "evidence": 0, "supporting": 0, "verbatim": 0, "near_miss": 0, "out_of_scope": 0,
            "fabricated": 0, "unverified": 0, "term": 0, "ambiguous": 0, "key_leak": 0, "mentions": 0,
            "fabricated_spans": [], "unverified_spans": []}, "structure": {"pass": False,
            "failures": ["report not produced"], "warnings": []}, "failures": ["report not produced"], "pass": False}


def summarize_grade(g):
    rows = " ".join("%s:%s" % (r, v["status"][0].upper() + ("" if v.get("id_exact", True) else "~"))
                    for r, v in g["rows"].items())
    return "%s | rows %s | counted %s/%s (excluded %d) | quotes v%d n%d o%d f%d u%d | structure %s | %s" % (
        "PASS" if g["pass"] else "FAIL", rows, g["budget"]["counted"], g["budget"]["limit"], g["budget"]["excluded"],
        g["quotes"]["verbatim"], g["quotes"]["near_miss"], g["quotes"]["out_of_scope"], g["quotes"]["fabricated"],
        g["quotes"]["unverified"],
        "ok" if g["structure"]["pass"] else "FAIL", "; ".join(g["failures"]) or "-")


# ---------------------------------------------------------------------- plan

def snapshot_from_git(ref, dest):
    sha = git("rev-parse", ref)
    dest.mkdir(parents=True, exist_ok=True)
    archive = subprocess.run(["git", "archive", ref, "SKILL.md", "references"], cwd=str(ROOT), capture_output=True)
    if archive.returncode != 0:
        raise Fail("git archive %s failed: %s" % (ref, archive.stderr.decode(errors="replace").strip()))
    subprocess.run(["tar", "-x", "-C", str(dest)], input=archive.stdout, check=True)
    return {"ref": ref, "skill_sha": sha, "dirty": False, "snapshot": rel(dest)}


def snapshot_from_worktree(dest):
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "SKILL.md", dest / "SKILL.md")
    if (dest / "references").exists():
        shutil.rmtree(dest / "references")
    shutil.copytree(ROOT / "references", dest / "references")
    sha = git("rev-parse", "HEAD")
    dirty = bool(git("status", "--porcelain", "--", "SKILL.md", "references"))
    return {"ref": "worktree", "skill_sha": sha, "dirty": dirty, "snapshot": rel(dest)}


def render_prompt(mode, ctx):
    tpl_path = PROMPTS_DIR / ("%s.md" % mode)
    if not tpl_path.exists():
        raise Fail("prompt template missing: %s" % rel(tpl_path))
    tpl = read_text(tpl_path)
    for k, v in ctx.items():
        tpl = tpl.replace("{{%s}}" % k, str(v))
    left = re.findall(r"{{\w+}}", tpl)
    if left:
        raise Fail("unresolved placeholders in %s: %s" % (rel(tpl_path), ", ".join(left)))
    return tpl


def cmd_plan(args):
    keys = load_keys()
    reg = slice_registry(keys)
    slices = args.slices.split(",") if args.slices else list(reg)
    for s in slices:
        if s not in reg:
            raise Fail("unknown slice %r; known: %s" % (s, ", ".join(reg)))
    runs = args.runs or (1 if args.tier == "smoke" else 5)
    head = git("rev-parse", "HEAD")
    batch = args.batch or "%s-%s-%s" % (_dt.date.today().isoformat(), args.tier, head[:7])
    bdir = RUNS_DIR / batch
    bjson = bdir / "batch.json"
    if bjson.exists():
        meta = load_json(bjson)
    else:
        arms = {}
        if args.tier in ("baseline", "decision"):
            arms["baseline"] = snapshot_from_git(args.baseline_ref or "main", bdir / "skill" / "baseline")
        if args.tier in ("smoke", "candidate", "decision"):
            arms["candidate"] = snapshot_from_worktree(bdir / "skill" / "candidate")
        meta = {"harness_version": HARNESS_VERSION, "batch": batch, "tier": args.tier, "created": now_iso(),
                "runs_per_slice": runs, "slices": slices, "arms": arms,
                "prompt_hashes": {m: sha256_file(PROMPTS_DIR / ("%s.md" % m)) for m in MODES
                                  if (PROMPTS_DIR / ("%s.md" % m)).exists()},
                "key_hashes": {k["id"]: key_hash(k) for k in keys}, "runs": []}
    index = {(r["arm"], r["slice"], r["n"]): r for r in meta["runs"]}
    pending = []
    for arm, ainfo in meta["arms"].items():
        snap = ROOT / ainfo["snapshot"]
        if not (snap / "SKILL.md").exists():
            if arm == "baseline":
                snapshot_from_git(ainfo["ref"], snap)
            else:
                snapshot_from_worktree(snap)
        for s in slices:
            spec = reg[s]
            fx = Fixture(ROOT / spec["key"]["fixture"])
            inp = bdir / arm / s / "input" / Path(spec["key"]["fixture"]).name
            if not inp.exists():
                write_text(inp, "\n".join(build_input_lines(fx, spec["slice"])) + "\n")
            for n in range(1, runs + 1):
                rdir = bdir / arm / s / ("run-%d" % n)
                prompt, report = rdir / "prompt.md", rdir / "report.md"
                if not prompt.exists():
                    write_text(prompt, render_prompt(spec["mode"], {
                        "skill_md": snap / "SKILL.md", "references_dir": snap / "references",
                        "input_path": inp, "report_path": report, "run_dir": rdir,
                        "team": spec.get("team") or "", "fixture_name": Path(spec["key"]["fixture"]).name}))
                entry = index.get((arm, s, n)) or {"arm": arm, "slice": s, "n": n}
                entry.update({"dir": rel(rdir), "prompt": rel(prompt), "report": rel(report), "input": rel(inp),
                              "mode": spec["mode"], "status": "done" if report.exists() else "pending"})
                if (arm, s, n) not in index:
                    meta["runs"].append(entry)
                    index[(arm, s, n)] = entry
                if entry["status"] == "pending":
                    pending.append({"arm": arm, "slice": s, "n": n, "run_dir": str(rdir), "prompt": str(prompt),
                                    "report": str(report)})
    dump_json(bjson, meta)
    if args.json:
        print(json.dumps({"batch": batch, "batch_dir": str(bdir), "pending": pending}, indent=2))
    else:
        print("batch %s (%s): %d run(s) planned, %d pending" % (batch, args.tier, len(meta["runs"]), len(pending)))
        for p in pending:
            print("  pending %s/%s/run-%d -> %s" % (p["arm"], p["slice"], p["n"], p["prompt"]))
        print("batch dir: %s" % bdir)


def cmd_record(args):
    rdir = Path(args.run_dir).resolve()
    if not rdir.exists():
        raise Fail("run dir does not exist: %s" % rdir)
    rec = load_json(rdir / "run.json") if (rdir / "run.json").exists() else {}
    if args.model:
        rec["model"] = args.model
    if args.tokens is not None:
        rec["tokens"] = args.tokens
    if args.seconds is not None:
        rec["wall_seconds"] = args.seconds
    rec["started_at"] = args.started or rec.get("started_at") or now_iso()
    rec["recorded_at"] = now_iso()
    dump_json(rdir / "run.json", rec)
    print("recorded %s" % rel(rdir / "run.json"))


# --------------------------------------------------------------------- grade

def find_batch(rdir):
    for p in [rdir, *rdir.parents]:
        if (p / "batch.json").exists():
            return p, load_json(p / "batch.json")
    raise Fail("no batch.json above %s" % rdir)


def grade_run_dir(rdir, keys=None, write=True):
    rdir = Path(rdir).resolve()
    bdir, meta = find_batch(rdir)
    entry = next((r for r in meta["runs"] if (ROOT / r["dir"]).resolve() == rdir), None)
    if entry is None:
        raise Fail("%s is not a run of batch %s" % (rdir, meta["batch"]))
    keys = keys or load_keys()
    reg = slice_registry(keys)
    spec = reg[entry["slice"]]
    arm = meta["arms"][entry["arm"]]
    run_json = load_json(rdir / "run.json") if (rdir / "run.json").exists() else {}
    prov = {"batch": meta["batch"], "tier": meta["tier"], "arm": entry["arm"], "slice": entry["slice"],
            "run": entry["n"], "skill_sha": arm["skill_sha"], "dirty": arm["dirty"], "skill_ref": arm["ref"],
            "model": run_json.get("model"), "prompt_hash": meta["prompt_hashes"].get(spec["mode"]),
            "key_hash": key_hash(spec["key"]), "key_hash_at_plan": meta["key_hashes"].get(spec["key"]["id"]),
            "started_at": run_json.get("started_at"),
            "wall_seconds": run_json.get("wall_seconds"), "tokens": run_json.get("tokens")}
    report = rdir / "report.md"
    if not report.exists():
        g = not_produced_grade(prov, spec["mode"])
    else:
        fx = Fixture(ROOT / spec["key"]["fixture"])
        input_lines = read_text(ROOT / entry["input"]).split("\n")
        g = grade_report(read_text(report), spec["key"], spec["slice"], input_lines, fx, prov)
    if write:
        dump_json(rdir / "grade.json", g)
    return g


def cmd_grade(args):
    if args.run_dir:
        keys = load_keys()
        for rd in args.run_dir:
            g = grade_run_dir(rd, keys)
            print("%s: %s" % (rel(rd), summarize_grade(g)))
        return
    if not (args.report and args.key):
        raise Fail("grade needs run directories, or --report with --key (and optionally --slice, --input, --out)")
    key = load_json(args.key)
    key["_path"] = args.key
    spec = None
    if args.slice:
        spec = (key.get("slices") or {}).get(args.slice)
        if spec is None:
            raise Fail("slice %r not in key" % args.slice)
    fx = Fixture(ROOT / key["fixture"])
    input_lines = read_text(args.input).split("\n") if args.input else build_input_lines(fx, spec)
    prov = {"batch": None, "tier": None, "arm": None, "slice": args.slice, "run": None, "skill_sha": None,
            "dirty": None, "skill_ref": None, "model": None, "prompt_hash": None, "key_hash": key_hash(key),
            "started_at": None, "wall_seconds": None, "tokens": None}
    g = grade_report(read_text(args.report), key, spec, input_lines, fx, prov)
    if args.out:
        dump_json(args.out, g)
    print(summarize_grade(g))
    if args.verbose:
        print(json.dumps(g, indent=2, ensure_ascii=False))


# ----------------------------------------------------------------- aggregate

def mean(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return round(sum(xs) / len(xs), 1) if xs else None


def cmd_aggregate(args):
    bdir = Path(args.batch_dir).resolve()
    meta = load_json(bdir / "batch.json")
    keys = load_keys()
    reg = slice_registry(keys)
    sc = {"harness_version": HARNESS_VERSION, "batch": meta["batch"], "tier": meta["tier"], "created": now_iso(),
          "runs_per_slice": meta["runs_per_slice"], "prompt_hashes": meta["prompt_hashes"],
          "key_hashes": {k["id"]: key_hash(k) for k in keys}, "key_hashes_at_plan": meta["key_hashes"],
          "warnings": [], "arms": {}}
    for arm, ainfo in meta["arms"].items():
        arm_out = {"skill_sha": ainfo["skill_sha"], "dirty": ainfo["dirty"], "ref": ainfo["ref"], "models": [],
                   "slices": {}}
        models = set()
        for slice_id in sorted({r["slice"] for r in meta["runs"] if r["arm"] == arm}):
            runs = [r for r in meta["runs"] if r["arm"] == arm and r["slice"] == slice_id]
            grades = []
            for r in runs:
                gp = ROOT / r["dir"] / "grade.json"
                if not gp.exists():
                    grade_run_dir(ROOT / r["dir"], keys)
                grades.append(load_json(gp))
            spec = reg[slice_id]
            expected = spec["slice"]["expected"] if spec["slice"] else [d["id"] for d in spec["key"]["defects"]]
            rows = {}
            for rid in expected:
                d = next(x for x in spec["key"]["defects"] if x["id"] == rid)
                ro = d.get("reference_overlap")
                rows[rid] = {"found": sum(1 for g in grades if g["rows"].get(rid, {}).get("status") == "found"),
                             "id_exact": sum(1 for g in grades if g["rows"].get(rid, {}).get("id_exact")),
                             "accepted": d["accepted"],
                             "caveat": ("overlaps a worked example in %s (%r)" % (ro["file"], ro["quote"])) if ro else None}
            freq = {}
            for g in grades:
                for f in g["findings"]:
                    if f["kind"] == "match" and "out_of_scope" not in f["flags"]:
                        continue
                    e = freq.setdefault(f["key"], {"key": f["key"], "runs": 0, "kind": f["kind"], "flags": set(),
                                                   "excluded": f["excluded"], "bucket": f["bucket"], "triage": f["triage"]})
                    e["runs"] += 1
                    e["flags"] |= set(f["flags"])
            extras = sorted(({**e, "flags": sorted(e["flags"])} for e in freq.values()),
                            key=lambda e: (-e["runs"], e["key"]))
            q = {k: sum(g["quotes"][k] for g in grades) for k in
                 ("total", "evidence", "supporting", "verbatim", "near_miss", "out_of_scope", "fabricated",
                  "unverified", "term", "ambiguous", "key_leak", "mentions")}
            tokens = [g["provenance"].get("tokens") for g in grades]
            secs = [g["provenance"].get("wall_seconds") for g in grades]
            slice_models = {g["provenance"].get("model") for g in grades}
            models |= slice_models
            arm_out["slices"][slice_id] = {
                "runs": len(runs), "produced": sum(1 for g in grades if g["produced"]),
                "pass": sum(1 for g in grades if g["pass"]), "structure_pass": sum(1 for g in grades if g["structure"]["pass"]),
                "rows": rows, "extras": extras,
                "violations": {"non_defect": sum(g["violations"]["non_defect"] for g in grades),
                               "off_key": sum(g["violations"]["off_key"] for g in grades)},
                "budget_counted": [g["budget"]["counted"] for g in grades],
                "quotes": q,
                "structure_failures": sorted({x for g in grades for x in g["structure"]["failures"]}),
                "cost": {"tokens_mean": mean(tokens), "tokens_max": max([t for t in tokens if isinstance(t, (int, float))] or [None]) if any(isinstance(t, (int, float)) for t in tokens) else None,
                         "seconds_mean": mean(secs), "seconds_max": max([s for s in secs if isinstance(s, (int, float))] or [None]) if any(isinstance(s, (int, float)) for s in secs) else None},
                "models": sorted(m for m in slice_models if m),
            }
            if len(slice_models) > 1:
                sc["warnings"].append("%s/%s: runs on mixed models %s" % (arm, slice_id, sorted(str(m) for m in slice_models)))
            if None in slice_models:
                sc["warnings"].append("%s/%s: model unknown for %d run(s)" % (arm, slice_id, sum(1 for g in grades if not g["provenance"].get("model"))))
        arm_out["models"] = sorted(m for m in models if m)
        sc["arms"][arm] = arm_out
    dump_json(bdir / "scorecard.json", sc)
    print(render_scorecard(sc))


def render_scorecard(sc):
    out = ["## Scorecard %s (%s)" % (sc["batch"], sc["tier"]), ""]
    for arm, a in sc["arms"].items():
        out.append("### arm %s — skill %s%s · model %s" % (arm, a["skill_sha"][:7], "+dirty" if a["dirty"] else "",
                                                          ", ".join(a["models"]) or "unknown"))
        out += ["", "| slice | runs | pass | structure | fabricated | near-miss | out-of-scope | counted extras/run | tokens mean | s mean |",
                "|---|---|---|---|---|---|---|---|---|---|"]
        for sid, s in a["slices"].items():
            out.append("| %s | %d (%d produced) | %d | %d | %d | %d | %d | %s | %s | %s |" % (
                sid, s["runs"], s["produced"], s["pass"], s["structure_pass"], s["quotes"]["fabricated"],
                s["quotes"]["near_miss"], s["quotes"]["out_of_scope"], "/".join(str(x) for x in s["budget_counted"]) or "-",
                s["cost"]["tokens_mean"] if s["cost"]["tokens_mean"] is not None else "n/a",
                s["cost"]["seconds_mean"] if s["cost"]["seconds_mean"] is not None else "n/a"))
        for sid, s in a["slices"].items():
            out.append("")
            out.append("**%s rows** (found/id-exact of %d): " % (sid, s["runs"]) + " · ".join(
                "%s %d/%d%s" % (rid, r["found"], r["id_exact"], " [caveat]" if r["caveat"] else "") for rid, r in s["rows"].items()))
            if s["extras"]:
                out.append("**%s extras/duplicates:** " % sid + " · ".join(
                    "%s ×%d [%s%s%s]" % (e["key"], e["runs"], e["kind"], ("; " + ", ".join(e["flags"])) if e["flags"] else "",
                                         "; excluded:" + str(e["triage"]) if e["excluded"] else "") for e in s["extras"]))
            if s["structure_failures"]:
                out.append("**%s structure failures:** " % sid + " · ".join(s["structure_failures"]))
            caveats = [(rid, r["caveat"]) for rid, r in s["rows"].items() if r["caveat"]]
            if caveats:
                out.append("**%s caveats:** " % sid + " · ".join("%s %s" % c for c in caveats))
        out.append("")
    if sc["warnings"]:
        out.append("**Warnings:** " + " · ".join(sc["warnings"]))
    return "\n".join(out)


# ------------------------------------------------------------------- compare

def cmd_compare(args):
    bdir = Path(args.batch_dir).resolve()
    scp = bdir / "scorecard.json"
    if not scp.exists() or args.refresh:
        ns = argparse.Namespace(batch_dir=str(bdir))
        cmd_aggregate(ns)
    sc = load_json(scp)
    arms = sc["arms"]
    warnings = []
    paired, baseline_batch = True, None
    if args.baseline_batch:
        obdir = Path(args.baseline_batch).resolve()
        if not (obdir / "scorecard.json").exists():
            cmd_aggregate(argparse.Namespace(batch_dir=str(obdir)))
        other = load_json(obdir / "scorecard.json")
        oarms = other["arms"]
        base = oarms.get("baseline") or (list(oarms.values())[0] if len(oarms) == 1 else None)
        if base is None:
            raise Fail("baseline batch %s must hold a baseline arm or exactly one arm" % other["batch"])
        if "candidate" not in arms:
            raise Fail("compare --baseline-batch needs a candidate arm in %s" % sc["batch"])
        cand = arms["candidate"]
        paired, baseline_batch = False, {"batch": other["batch"], "created": other["created"]}
        warnings.append("unpaired: baseline arm taken from batch %s (created %s), candidate from %s (created %s)" % (
            other["batch"], other["created"], sc["batch"], sc["created"]))
    else:
        if "baseline" not in arms or "candidate" not in arms:
            raise Fail("compare needs both a baseline and a candidate arm; batch has %s" % ", ".join(arms))
        base, cand = arms["baseline"], arms["candidate"]
    if base["models"] and cand["models"] and set(base["models"]) != set(cand["models"]):
        print("error: arms ran on different models: baseline %s vs candidate %s" % (base["models"], cand["models"]))
        sys.exit(2)
    if not base["models"] or not cand["models"]:
        warnings.append("model unknown for at least one arm; comparison proceeds unverified")
    regressions, improvements = [], []
    for sid in sorted(set(base["slices"]) & set(cand["slices"])):
        b, c = base["slices"][sid], cand["slices"][sid]
        if b["runs"] != c["runs"]:
            warnings.append("%s: unequal run counts (baseline %d, candidate %d)" % (sid, b["runs"], c["runs"]))
        for rid in b["rows"]:
            if rid not in c["rows"]:
                continue
            drop = b["rows"][rid]["found"] - c["rows"][rid]["found"]
            rec = {"rule": "hit_drop", "slice": sid, "row": rid, "baseline": b["rows"][rid]["found"],
                   "candidate": c["rows"][rid]["found"]}
            if drop >= 2:
                regressions.append(rec)
            elif drop <= -2:
                improvements.append({**rec, "rule": "hit_gain"})
        bk = {e["key"]: e["runs"] for e in b["extras"] if not e["excluded"]}
        ck = {e["key"]: e["runs"] for e in c["extras"] if not e["excluded"]}
        for k, n in ck.items():
            if n >= 3 and bk.get(k, 0) < 3:
                regressions.append({"rule": "new_stable_extra", "slice": sid, "key": k, "baseline": bk.get(k, 0), "candidate": n})
        for k, n in bk.items():
            if n >= 3 and ck.get(k, 0) < 3:
                improvements.append({"rule": "extra_resolved", "slice": sid, "key": k, "baseline": n, "candidate": ck.get(k, 0)})
        if c["quotes"]["fabricated"] > 0:
            regressions.append({"rule": "fabricated", "slice": sid, "candidate": c["quotes"]["fabricated"]})
    comparison = {"harness_version": HARNESS_VERSION, "batch": sc["batch"], "created": now_iso(), "paired": paired,
                  "baseline_batch": baseline_batch,
                  "baseline": {"skill_sha": base["skill_sha"], "models": base["models"]},
                  "candidate": {"skill_sha": cand["skill_sha"], "models": cand["models"]},
                  "regressions": regressions, "improvements": improvements, "warnings": warnings,
                  "verdict": "REGRESSION" if regressions else "OK"}
    dump_json(bdir / "comparison.json", comparison)
    print("## Comparison %s: %s%s" % (sc["batch"], comparison["verdict"], "" if paired else " (unpaired)"))
    for r in regressions:
        print("  REGRESSION %s" % json.dumps(r))
    for r in improvements:
        print("  improvement %s" % json.dumps(r))
    for w in warnings:
        print("  warning: %s" % w)
    sys.exit(1 if regressions else 0)


# --------------------------------------------------------------------- check

def cmd_render_key(args):
    catalog = load_catalog()
    keys = load_keys()
    targets = keys if args.all else [k for k in keys if args.target in (k["id"], k["fixture"], Path(k["_path"]).name, Path(k["_path"]).stem)]
    if not targets:
        raise Fail("no key matches %r (use an id like fixture1, a key file name, or --all)" % args.target)
    for k in targets:
        errs = validate_key(k, k["_path"], catalog)
        if errs:
            raise Fail("refusing to render an invalid key:\n  " + "\n  ".join(errs))
        fx = Fixture(ROOT / k["fixture"])
        rendered = render_key_section(k, catalog)
        if args.check:
            print("%s: %s" % (k["fixture"], "fresh" if fx.key_text == rendered else "STALE"))
            continue
        if fx.key_text == rendered:
            print("%s: already fresh" % k["fixture"])
        else:
            fx.write_key_section(rendered)
            print("%s: answer-key section regenerated" % k["fixture"])


def cmd_check(args):
    catalog = load_catalog()
    errors = []
    if args.key:
        paths = [Path(args.key)]
    else:
        paths = key_files()
        if not paths:
            errors.append("no keys under %s" % rel(KEYS_DIR))
    keys = []
    for p in paths:
        try:
            k = load_json(p)
        except Exception as e:  # noqa: BLE001
            errors.append("%s: invalid JSON: %s" % (rel(p), e))
            continue
        k["_path"] = str(p)
        errs = validate_key(k, p, catalog)
        errors += errs
        if not errs:
            keys.append(k)
    if not args.key and keys:
        covered = set()
        for k in keys:
            covered |= {i for d in k["defects"] for i in d["accepted"]}
        missing = sorted(set(catalog) - covered)
        if missing:
            errors.append("catalog ids without a planted defect in any key: %s" % ", ".join(missing))
    for k in keys:
        fx = Fixture(ROOT / k["fixture"])
        if fx.key_text != render_key_section(k, catalog):
            errors.append("%s: generated '## Answer key' section is stale — run: python3 evals/grader/harness.py render-key %s" % (k["fixture"], k["id"]))
    if errors:
        print("check: %d problem(s)" % len(errors))
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("check: ok (%d key(s), %d catalog ids, answer-key sections fresh)" % (len(keys), len(catalog)))


# ------------------------------------------------------------------ selftest

def flatten(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, prefix + k + "."))
    else:
        out[prefix[:-1]] = obj
    return out


def expect_ok(actual, expected):
    if isinstance(expected, dict) and "contains" in expected:
        hay = json.dumps(actual, ensure_ascii=False)
        return all(sub in hay for sub in expected["contains"])
    if isinstance(expected, list) and isinstance(actual, list):
        return sorted(map(str, expected)) == sorted(map(str, actual))
    return actual == expected


def cmd_selftest(args):
    catalog = load_catalog()
    cases = sorted((SELFTEST_DIR / "cases").glob("*/case.json"))
    if not cases:
        raise Fail("no self-test cases under %s" % rel(SELFTEST_DIR / "cases"))
    failures, total = [], 0
    for cp in cases:
        case = load_json(cp)
        cdir = cp.parent
        name = cdir.name
        if args.only and args.only not in name:
            continue
        total += 1
        if case.get("type") == "check":
            kp = cdir / case["key"]
            try:
                k = load_json(kp)
                errs = validate_key(k, kp, catalog)
            except Fail as e:
                errs = [str(e)]
            text = "\n".join(errs)
            if not errs:
                failures.append("%s: expected check to fail, it passed" % name)
            for sub in case.get("expect_mentions", []):
                if sub not in text:
                    failures.append("%s: check output lacks %r" % (name, sub))
            continue
        kp = next(p for p in (cdir / case["key"], SELFTEST_DIR / "keys" / case["key"], KEYS_DIR / case["key"]) if p.exists())
        key = load_json(kp)
        key["_path"] = str(kp)
        spec = (key.get("slices") or {}).get(case["slice"]) if case.get("slice") else None
        fx = Fixture(ROOT / key["fixture"])
        input_lines = read_text(cdir / case["input"]).split("\n") if case.get("input") else build_input_lines(fx, spec)
        prov = {"batch": None, "tier": None, "arm": None, "slice": case.get("slice"), "run": None, "skill_sha": None,
                "dirty": None, "skill_ref": None, "model": None, "prompt_hash": None, "key_hash": key_hash(key),
                "started_at": None, "wall_seconds": None, "tokens": None}
        g = grade_report(read_text(cdir / case["report"]), key, spec, input_lines, fx, prov)
        flat = flatten({k: v for k, v in g.items() if k != "findings"})
        flat["extras"] = g["extras"]
        flat["duplicates"] = g["duplicates"]
        flat["excluded"] = g["excluded"]
        flat["failures"] = g["failures"]
        flat["structure.failures"] = g["structure"]["failures"]
        flat["structure.warnings"] = g["structure"]["warnings"]
        flat["quotes.fabricated_spans"] = g["quotes"]["fabricated_spans"]
        for path, exp in case["expected"].items():
            act = flat.get(path, "<absent>")
            if not expect_ok(act, exp):
                failures.append("%s: %s expected %s, got %s" % (name, path, json.dumps(exp, ensure_ascii=False),
                                                                json.dumps(act, ensure_ascii=False)))
        if args.verbose:
            print("%s: %s" % (name, summarize_grade(g)))
    if failures:
        print("selftest: %d case(s), %d failure(s)" % (total, len(failures)))
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("selftest: ok (%d case(s))" % total)


# ---------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(prog="harness.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="validate keys, anchors, coverage, freshness")
    p.add_argument("--key", help="check one key file instead of every key under evals/keys")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("render-key", help="regenerate a fixture's answer-key section from its JSON key")
    p.add_argument("target", nargs="?", help="key id (fixture1), key file name, or fixture path")
    p.add_argument("--all", action="store_true")
    p.add_argument("--check", action="store_true", help="report fresh/stale without writing")
    p.set_defaults(fn=cmd_render_key)

    p = sub.add_parser("plan", help="create or resume a batch and list pending runs")
    p.add_argument("--tier", choices=("smoke", "candidate", "baseline", "decision"), required=True)
    p.add_argument("--slices", help="comma-separated slice ids (default: all)")
    p.add_argument("--runs", type=int, help="runs per slice per arm (default 1 for smoke, 5 otherwise; candidate = candidate arm only)")
    p.add_argument("--baseline-ref", help="git ref for the baseline arm (default main)")
    p.add_argument("--batch", help="batch id (default <date>-<tier>-<sha7>)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_plan)

    p = sub.add_parser("record", help="write run.json provenance for a run directory")
    p.add_argument("run_dir")
    p.add_argument("--model")
    p.add_argument("--tokens", type=int)
    p.add_argument("--seconds", type=float)
    p.add_argument("--started")
    p.set_defaults(fn=cmd_record)

    p = sub.add_parser("grade", help="grade run directories, or an explicit report")
    p.add_argument("run_dir", nargs="*")
    p.add_argument("--report")
    p.add_argument("--key")
    p.add_argument("--slice")
    p.add_argument("--input")
    p.add_argument("--out")
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(fn=cmd_grade)

    p = sub.add_parser("aggregate", help="build scorecard.json for a batch")
    p.add_argument("batch_dir")
    p.set_defaults(fn=cmd_aggregate)

    p = sub.add_parser("compare", help="apply the regression rule between the arms of a batch")
    p.add_argument("batch_dir")
    p.add_argument("--refresh", action="store_true", help="re-aggregate before comparing")
    p.add_argument("--baseline-batch", help="take the baseline arm from another batch (unpaired comparison)")
    p.set_defaults(fn=cmd_compare)

    p = sub.add_parser("selftest", help="grade the bundled self-test cases")
    p.add_argument("--only")
    p.add_argument("--verbose", action="store_true")
    p.set_defaults(fn=cmd_selftest)

    args = ap.parse_args(argv)
    try:
        args.fn(args)
    except Fail as e:
        print("error: %s" % e)
        sys.exit(1)


if __name__ == "__main__":
    main()
