#!/usr/bin/env python3
"""OKR-Ninja evaluation harness (Python 3 standard library only).

Subcommands
  check        validate the JSON keys: schema, anchors, catalog partition and coverage,
               generated answer-key freshness, reference-overlap pointers, triage rules
  render-key   regenerate a fixture's "## Answer key" section from its JSON key
  plan         create or resume a batch: sliced inputs, skill snapshots, prompts,
               batch.json; print the pending runs
  capture      extract a run's report byte-exact from the runner's JSONL transcript (the final
               message's marker block), write report.md and run.json, or record why not
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
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HARNESS_VERSION = 3
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
REPORT_BEGIN = "=====BEGIN OKR-NINJA REPORT====="
REPORT_END = "=====END OKR-NINJA REPORT====="
# Why a run has no report.md: transport failures first, runner-format failures second.
NOT_PRODUCED = ("agent-error", "transcript-unreadable", "no-final-text", "markers-missing", "multiple-blocks",
                "empty-report", "model-mismatch")


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


def not_produced_grade(provenance, mode, reason=None):
    """The grade of a run without report.md. `reason` is a NOT_PRODUCED name from run.json (capture wrote it);
    runs recorded before capture existed carry none and keep the bare legacy failure string."""
    msg = "report not produced" + (": %s" % reason if reason else "")
    return {"harness_version": HARNESS_VERSION, "graded_at": now_iso(), "mode": mode, "provenance": provenance,
            "findings_parsed": 0, "produced": False, "not_produced": reason, "rows": {}, "findings": [], "extras": [],
            "duplicates": [], "excluded": [], "violations": {"non_defect": 0, "off_key": 0}, "budget": {"limit": None,
            "counted": 0, "excluded": 0}, "quotes": {"total": 0, "evidence": 0, "supporting": 0, "verbatim": 0,
            "near_miss": 0, "out_of_scope": 0, "fabricated": 0, "unverified": 0, "term": 0, "ambiguous": 0,
            "key_leak": 0, "mentions": 0, "fabricated_spans": [], "unverified_spans": []},
            "structure": {"pass": False, "failures": [msg], "warnings": []}, "failures": [msg], "pass": False}


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


# ------------------------------------------------------------------- capture

class Unreadable(Exception):
    """The transcript cannot be parsed; the message says why."""


def read_transcript(path):
    """Parse a Claude Code subagent JSONL transcript into API messages.

    One API message is spread over several JSONL lines that share `message.id` (thinking, tool_use and text
    items arrive one per line). Assistant lines are grouped by unique id in first-appearance order — not by
    runs of consecutive lines, so interleaved ids still form one message each; a line without an id is a
    message of its own. -> {messages: [{id, model, usage, texts, timestamp, last_line}] (assistant only),
    first_ts, last_ts, lines}. Only message.role/content/model/id/usage and the line timestamp are relied on;
    attachment lines, tool results and anything else are ignored. Raises Unreadable for a file that cannot be
    read, a non-JSON line, or a line whose relied-on fields have an unexpected shape."""
    p = Path(path)
    if not p.is_file():
        raise Unreadable("transcript does not exist or is not a regular file: %s" % p)
    try:
        data = p.read_bytes()
    except OSError as e:
        raise Unreadable("transcript cannot be read: %s" % e)
    messages, by_id, first_ts, last_ts, n = [], {}, None, None, 0
    for i, raw in enumerate(data.split(b"\n"), 1):
        if not raw.strip():
            continue
        n += 1
        try:
            obj = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as e:
            raise Unreadable("line %d of %s is not JSON: %s" % (i, p, e))
        if not isinstance(obj, dict):
            raise Unreadable("line %d of %s is not a JSON object" % (i, p))
        ts = obj.get("timestamp")
        if ts is not None and not isinstance(ts, str):
            raise Unreadable("line %d of %s: timestamp is not a string" % (i, p))
        if ts:
            first_ts = first_ts or ts
            last_ts = ts
        msg = obj.get("message")
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        mid, model, usage, content = msg.get("id"), msg.get("model"), msg.get("usage"), msg.get("content")
        if mid is not None and not isinstance(mid, str):
            raise Unreadable("line %d of %s: message.id is not a string" % (i, p))
        if model is not None and not isinstance(model, str):
            raise Unreadable("line %d of %s: message.model is not a string" % (i, p))
        if usage is not None and not isinstance(usage, dict):
            raise Unreadable("line %d of %s: message.usage is not an object" % (i, p))
        if not isinstance(content, list):
            raise Unreadable("line %d of %s: message.content is not a list" % (i, p))
        texts = []
        for c in content:
            if not isinstance(c, dict) or not isinstance(c.get("type"), str):
                raise Unreadable("line %d of %s: a content item is not an object with a type" % (i, p))
            if c["type"] == "text":
                if not isinstance(c.get("text"), str):
                    raise Unreadable("line %d of %s: a text item's text is not a string" % (i, p))
                texts.append(c["text"])
        m = by_id.get(mid) if mid is not None else None
        if m is None:
            m = {"id": mid, "model": model, "usage": usage or {}, "texts": [], "timestamp": ts, "last_line": i}
            messages.append(m)
            if mid is not None:
                by_id[mid] = m
        m["texts"] += texts
        m["usage"] = usage or m["usage"]      # the last line per id carries the message's final running usage
        m["model"] = model or m["model"]
        m["last_line"] = i
    return {"messages": messages, "first_ts": first_ts, "last_ts": last_ts, "lines": n}


def final_message(messages):
    """The runner's final reply: among messages carrying a text item, the one whose last transcript line is latest."""
    cands = [m for m in messages if m["texts"]]
    return max(cands, key=lambda m: m["last_line"]) if cands else None


def final_text(messages):
    """The final message's text items concatenated in order with nothing inserted (only bytes the runner emitted)."""
    m = final_message(messages)
    return "".join(m["texts"]) if m else None


def transcript_usage(messages):
    """Token usage summed over unique messages (each carries its final running usage)."""
    out = {"messages": len(messages), "input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0,
           "cache_read_input_tokens": 0}
    for m in messages:
        for k in list(out)[1:]:
            v = m["usage"].get(k)
            if isinstance(v, (int, float)):
                out[k] += int(v)
    return out


def iso_seconds(a, b):
    try:
        ta = _dt.datetime.fromisoformat(a.replace("Z", "+00:00"))
        tb = _dt.datetime.fromisoformat(b.replace("Z", "+00:00"))
        return round((tb - ta).total_seconds(), 3)
    except (AttributeError, ValueError, TypeError):
        return None


def is_marker(line, marker):
    """Exact-line match; only a trailing carriage return (CRLF transport) is tolerated."""
    return line == marker or line == marker + "\r"


def extract_report(text):
    """-> (report, reason). Exactly one REPORT_BEGIN line and one REPORT_END line, begin before end; the report is
    the text strictly between them, kept as emitted, with a final newline added only when the body lacks one.
    An empty body (nothing, or only whitespace — spaces, tabs, CR, LF — between the markers) is `empty-report`;
    a non-empty body is never stripped."""
    lines = text.split("\n")
    begins = [i for i, ln in enumerate(lines) if is_marker(ln, REPORT_BEGIN)]
    ends = [i for i, ln in enumerate(lines) if is_marker(ln, REPORT_END)]
    if len(begins) > 1 or len(ends) > 1:
        return None, "multiple-blocks"
    if not begins or not ends or ends[0] < begins[0]:
        return None, "markers-missing"
    body = "\n".join(lines[begins[0] + 1: ends[0]])
    if not body.strip(" \t\r\n"):
        return None, "empty-report"
    return body if body.endswith("\n") else body + "\n", None


def fresh_provenance(args, tr):
    """The provenance capture records for a run, built from the transcript and the command line only — never
    from an earlier run.json (design D6: nothing survives a re-capture)."""
    msgs = tr["messages"]
    models = []
    for m in msgs:
        if m["model"] and m["model"] not in models:
            models.append(m["model"])
    usage = transcript_usage(msgs) if msgs else None
    fm = final_message(msgs)
    return {
        # the final message's model (D2's final-message rule); without a text-carrying message, the latest model seen
        "model": (fm["model"] if fm else None) or next((m["model"] for m in reversed(msgs) if m["model"]), None),
        "models_seen": models,
        "transcript_usage": usage,
        "tokens": args.tokens if args.tokens is not None else (
            sum(v for k, v in usage.items() if k != "messages") if usage else None),
        "wall_seconds": args.seconds if args.seconds is not None else (
            iso_seconds(tr["first_ts"], tr["last_ts"]) if tr["first_ts"] else None),
        "started_at": tr["first_ts"] or now_iso(),
    }


EMPTY_TRANSCRIPT = {"messages": [], "first_ts": None, "last_ts": None, "lines": 0}


def decide_capture(args):
    """Everything capture decides, with no side effects: -> (provenance, reason, detail, body bytes or None)."""
    reason, detail, body = None, None, None
    try:
        tr = read_transcript(args.transcript)
    except Unreadable as e:
        tr, reason, detail = EMPTY_TRANSCRIPT, "transcript-unreadable", str(e)
    if args.agent_error:
        reason, detail = "agent-error", args.agent_error + ("" if detail is None else " (also: %s)" % detail)
    prov = fresh_provenance(args, tr)
    msgs = tr["messages"]
    if reason is None and not msgs:
        reason, detail = "agent-error", "transcript holds no assistant turn"
    if reason is None and args.model and args.model != prov["model"]:
        reason, detail = "model-mismatch", "--model %s but the transcript records %s" % (
            args.model, prov["model"] or "no model")
    if reason is None:
        text = final_text(msgs)
        if text is None:
            reason, detail = "no-final-text", "no assistant message carries a text item"
        else:
            body, reason = extract_report(text)
            if reason == "empty-report":
                detail = "the marker block holds no report text"
            elif reason:
                detail = "final message has %d begin and %d end marker line(s)" % (
                    sum(1 for ln in text.split("\n") if is_marker(ln, REPORT_BEGIN)),
                    sum(1 for ln in text.split("\n") if is_marker(ln, REPORT_END)))
    if reason is None:
        try:
            body = body.encode("utf-8")
        except UnicodeEncodeError as e:
            reason, detail, body = "transcript-unreadable", "report text is not encodable as UTF-8: %s" % e, None
    return prov, reason, detail, body


RUN_JSON_KEYS = ("transcript", "previous_run_json_replaced", "stale_report_removed", "stale_grade_removed", "model",
                 "models_seen", "transcript_usage", "tokens", "wall_seconds", "started_at", "not_produced",
                 "not_produced_detail", "recorded_at")


def ascii_safe(v):
    """A string that json.dumps(ensure_ascii=True) and UTF-8 can always represent: non-ASCII and lone surrogates
    become backslash escapes."""
    return str(v).encode("ascii", "backslashreplace").decode("ascii")


def serialize_record(rec):
    """The exact bytes run.json will hold. Raises when any value cannot be represented."""
    return (json.dumps(rec, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def fallback_record(args, flags, failure):
    """A run.json that cannot fail to serialize, for when the real record could not be represented (design D3):
    reason transcript-unreadable — or agent-error when --agent-error was given — with an ASCII-safe detail."""
    def cli_num(v):
        try:
            json.dumps(v).encode("ascii")
            return v
        except (TypeError, ValueError, UnicodeEncodeError, OverflowError):
            return None
    detail = "run record could not be serialized: %s" % ascii_safe(failure)
    reason = "transcript-unreadable"
    if args.agent_error:
        reason, detail = "agent-error", "%s (also: %s)" % (ascii_safe(args.agent_error), detail)
    rec = {"transcript": ascii_safe(args.transcript), **flags, "model": None, "models_seen": [], "transcript_usage": None,
           "tokens": cli_num(args.tokens), "wall_seconds": cli_num(args.seconds), "started_at": now_iso(),
           "not_produced": reason, "not_produced_detail": detail, "recorded_at": now_iso()}
    return rec, (json.dumps(rec, indent=2, ensure_ascii=True) + "\n").encode("ascii")


def cmd_capture(args):
    """Capture a run's report from its transcript. Structure (design D6): decide everything and serialize the exact
    bytes in memory first; only then touch the run directory — stage the new files, remove the stale ones, and
    move the staged files into place — so no path ends with stale files removed and no valid run.json."""
    rdir = Path(args.run_dir).resolve()
    if not rdir.exists():
        raise Fail("run dir does not exist: %s" % rdir)
    try:
        report, grade, run_json = rdir / "report.md", rdir / "grade.json", rdir / "run.json"
        flags = {"previous_run_json_replaced": run_json.exists(), "stale_report_removed": report.exists(),
                 "stale_grade_removed": grade.exists()}
        # 1. decide, never crashing: an error the parser did not anticipate is a named reason with fresh provenance
        try:
            prov, reason, detail, body = decide_capture(args)
        except Exception as e:  # noqa: BLE001
            prov, body = fresh_provenance(args, EMPTY_TRANSCRIPT), None
            reason, detail = "transcript-unreadable", "unexpected error while reading the transcript: %r" % (e,)
            if args.agent_error:
                reason, detail = "agent-error", "%s (also: %s)" % (args.agent_error, detail)
        rec = {"transcript": str(args.transcript), **flags, **prov, "not_produced": reason, "not_produced_detail": detail,
               "recorded_at": now_iso()}
        # 2. serialize the exact bytes; a record that cannot be represented becomes the fallback (no report)
        try:
            rec_bytes = serialize_record(rec)
        except Exception as e:  # noqa: BLE001 — lone surrogates, NaN, unrepresentable values
            rec, rec_bytes = fallback_record(args, flags, "%s: %s" % (type(e).__name__, e))
            reason, detail, body = rec["not_produced"], rec["not_produced_detail"], None
        # 3. stage the new files, then remove stale ones, then move staged files into place (`*.tmp` is gitignored,
        #    never graded, and never counted as a report by `plan`). On a failure the message says exactly what
        #    changed: nothing before the first removal; after it, which stale files went and whether run.json was
        #    replaced, so the operator re-runs capture rather than trusting a directory in a half-way state.
        staged_run, staged_report = rdir / "run.json.tmp", rdir / "report.md.tmp"
        removed, written = [], []
        try:
            staged_run.write_bytes(rec_bytes)
            if body is not None:
                staged_report.write_bytes(body)
            for stale in (report, grade):
                if stale.exists():
                    stale.unlink()
                    removed.append(stale.name)
            os.replace(staged_run, run_json)
            written.append(run_json.name)
            if body is not None:
                os.replace(staged_report, report)
                written.append(report.name)
        except OSError as e:
            for t in (staged_run, staged_report):
                try:
                    if t.exists():
                        t.unlink()
                except OSError:
                    pass
            if not removed and not written:
                state = "the run directory was left as it was"
            else:
                state = "%s; %s; re-run capture" % (
                    ("stale %s removed" % " and ".join(removed)) if removed else "no stale file removed",
                    ("%s written" % " and ".join(written)) if written else "run.json not replaced")
            print("error: capture could not write into %s (%s); %s" % (rdir, e, state), file=sys.stderr)
            sys.exit(1)
        if reason:
            print("not produced (%s): %s — recorded in %s, no report.md written" % (reason, ascii_safe(detail), rel(run_json)))
            sys.exit(1)
        print("captured %s (%d bytes, model %s) from %s" % (rel(report), len(body), ascii_safe(rec["model"]), ascii_safe(args.transcript)))
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001 — last line of defence: never a traceback
        print("error: capture failed unexpectedly (%s); nothing was changed unless the messages above say otherwise" % ascii_safe(repr(e)),
              file=sys.stderr)
        sys.exit(1)


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
            "wall_seconds": run_json.get("wall_seconds"), "tokens": run_json.get("tokens"),
            "not_produced": run_json.get("not_produced")}
    report = rdir / "report.md"
    if not report.exists():
        g = not_produced_grade(prov, spec["mode"], run_json.get("not_produced"))
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
            "started_at": None, "wall_seconds": None, "tokens": None, "not_produced": None}
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
            not_produced = {}
            for g in grades:
                if not g["produced"]:
                    r = g.get("not_produced") or "unknown"
                    not_produced[r] = not_produced.get(r, 0) + 1
            arm_out["slices"][slice_id] = {
                "runs": len(runs), "produced": sum(1 for g in grades if g["produced"]),
                "not_produced": not_produced,
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
            if s.get("not_produced"):
                out.append("**%s not produced:** " % sid + " · ".join(
                    "%s ×%d" % (r, n) for r, n in sorted(s["not_produced"].items())))
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
    base_hashes = cand_hashes = sc.get("prompt_hashes") or {}
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
        base_hashes = other.get("prompt_hashes") or {}
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
    # The prompt template is transport, not skill content: a mismatch is warned about, never refused (design D7).
    differing = sorted(m for m in set(base_hashes) | set(cand_hashes) if base_hashes.get(m) != cand_hashes.get(m))
    if differing:
        warnings.append("prompt-template hash differs between arms for mode(s) %s; the arms ran on different "
                        "prompts, so transport effects may be mixed into the verdict" % ", ".join(differing))
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
                  "baseline": {"skill_sha": base["skill_sha"], "models": base["models"], "prompt_hashes": base_hashes},
                  "candidate": {"skill_sha": cand["skill_sha"], "models": cand["models"], "prompt_hashes": cand_hashes},
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
    scenarios = 0
    if not args.key:
        try:
            sc = load_scenarios(args.scenarios_file)
            errors += validate_scenarios(sc, keys)
            scenarios = len(sc.get("scenarios", []))
        except Fail as e:
            errors.append(str(e))
    if errors:
        print("check: %d problem(s)" % len(errors))
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("check: ok (%d key(s), %d catalog ids, answer-key sections fresh, %d lifecycle scenario(s))" % (
        len(keys), len(catalog), scenarios))


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


def selftest_capture(name, cdir, case):
    """Run capture on a synthetic transcript into a temporary run directory and check the outcome.
    case: {type: capture, transcript, args: {model, tokens, seconds, agent_error}, expected: {produced,
    not_produced, model, tokens, report: <file whose bytes report.md must equal>}}. A case with
    `preexisting_dirs` and `expected: {error: true, removed, kept, stderr_contains}` exercises a write failure
    (design D6): capture must exit 1, leave no staged file, and describe the directory's state truthfully."""
    import tempfile
    fails = []
    tmp = Path(tempfile.mkdtemp(prefix="okr-capture-"))
    try:
        a = case.get("args") or {}
        for fn in case.get("preexisting", []):
            (tmp / fn).write_text("stale\n", encoding="utf-8")
        for fn in case.get("preexisting_dirs", []):
            (tmp / fn).mkdir()
        if case.get("preexisting_run_json") is not None:
            (tmp / "run.json").write_text(case["preexisting_run_json"], encoding="utf-8")
        transcript = cdir / case["transcript"]
        if case.get("chmod0"):
            import os
            transcript = tmp / "unreadable.jsonl"
            transcript.write_text("{}\n", encoding="utf-8")
            os.chmod(transcript, 0)
            if os.access(transcript, os.R_OK):
                return []      # running as a user chmod cannot restrict (root): nothing to test here
        ns = argparse.Namespace(run_dir=str(tmp), transcript=str(transcript), model=a.get("model"),
                                tokens=a.get("tokens"), seconds=a.get("seconds"), agent_error=a.get("agent_error"))
        import io
        import contextlib
        exit_code, err = 0, io.StringIO()
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            try:
                cmd_capture(ns)
            except SystemExit as e:
                exit_code = e.code
            except Exception as e:  # noqa: BLE001
                return ["%s: capture raised %r instead of recording a reason" % (name, e)]
        if case["expected"].get("error"):
            exp = case["expected"]
            if exit_code != 1:
                fails.append("%s: a write failure must exit 1, got %s" % (name, exit_code))
            for t in ("run.json.tmp", "report.md.tmp"):
                if (tmp / t).exists():
                    fails.append("%s: staged file %s left behind" % (name, t))
            for fn in exp.get("removed", []):
                if (tmp / fn).exists():
                    fails.append("%s: %s should have been removed before the failure" % (name, fn))
            for fn in exp.get("kept", []):
                if not (tmp / fn).exists():
                    fails.append("%s: %s should have survived the failure" % (name, fn))
            if exp.get("stderr_contains") and exp["stderr_contains"] not in err.getvalue():
                fails.append("%s: stderr %r lacks %r" % (name, err.getvalue().strip(), exp["stderr_contains"]))
            return fails
        if not (tmp / "run.json").exists():
            return ["%s: capture wrote no run.json (exit %s)" % (name, exit_code)]
        try:
            rec = load_json(tmp / "run.json")
        except ValueError as e:
            return ["%s: run.json is not valid JSON (%s)" % (name, e)]
        if set(rec) != set(RUN_JSON_KEYS):
            fails.append("%s: run.json keys %s != expected %s" % (name, sorted(set(rec) ^ set(RUN_JSON_KEYS)), "RUN_JSON_KEYS"))
        for t in ("run.json.tmp", "report.md.tmp"):
            if (tmp / t).exists():
                fails.append("%s: staged file %s left behind" % (name, t))
        exp = case["expected"]
        produced = (tmp / "report.md").exists()
        for fn in case.get("preexisting", []):
            if fn == "report.md" and produced and (tmp / fn).read_text(encoding="utf-8") != "stale\n":
                continue
            if (tmp / fn).exists():
                fails.append("%s: pre-existing %s survived capture" % (name, fn))
        if produced != exp.get("produced", True):
            fails.append("%s: produced expected %s, got %s" % (name, exp.get("produced", True), produced))
        if (exit_code != 0) != (not exp.get("produced", True)):
            fails.append("%s: exit code %s does not match produced=%s" % (name, exit_code, produced))
        for field in ("not_produced", "model", "tokens", "wall_seconds", "models_seen", "transcript_usage",
                      "stale_report_removed", "stale_grade_removed", "previous_run_json_replaced"):
            if field in exp and rec.get(field) != exp[field]:
                fails.append("%s: run.json %s expected %s, got %s" % (name, field, json.dumps(exp[field]), json.dumps(rec.get(field))))
        for field, old in (exp.get("not_equal") or {}).items():
            if rec.get(field) == old:
                fails.append("%s: run.json %s still carries the old value %s" % (name, field, json.dumps(old)))
        if "detail_contains" in exp and exp["detail_contains"] not in str(rec.get("not_produced_detail")):
            fails.append("%s: not_produced_detail %r lacks %r" % (name, rec.get("not_produced_detail"), exp["detail_contains"]))
        if exp.get("report"):
            want = (cdir / exp["report"]).read_bytes()
            got = (tmp / "report.md").read_bytes() if produced else b""
            if want != got:
                fails.append("%s: report.md differs from %s (%d vs %d bytes)" % (name, exp["report"], len(got), len(want)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return fails


SUBST = re.compile(r"{{(created|seeded|supplied):([^}]+)}}")


def _subst(value, resolve):
    if isinstance(value, str):
        return SUBST.sub(lambda m: resolve(m.group(1), m.group(2)), value)
    if isinstance(value, list):
        return [_subst(v, resolve) for v in value]
    if isinstance(value, dict):
        return {k: _subst(v, resolve) for k, v in value.items()}
    return value


def lifecycle_selftest_case(name, case, cdir):
    """Materialise a lifecycle run directory from the case, drive the real seam, grade it, diff."""
    out = []
    sc = load_scenarios(cdir / case["scenarios_file"]) if case.get("scenarios_file") else load_scenarios()
    scen = scenario_of(sc, case["scenario"])
    run = case.get("run") or {}
    seeded = {k: e["url"] for k, e in ((scen.get("seed") or {}).get("registry") or {}).items()}
    supplied = dict(scen.get("supplied_urls") or {})
    created = {}

    def resolve(kind, key):
        src = {"created": created, "seeded": seeded, "supplied": supplied}[kind]
        if key not in src:
            out.append("%s: no %s URL for %r" % (name, kind, key))
            return "<unresolved>"
        return src[key]

    with tempfile.TemporaryDirectory() as tmp:
        rdir = Path(tmp) / "run"
        seed_run(rdir, scen)
        for fname, content in (run.get("work_files") or {}).items():
            write_text(rdir / "work" / fname, content)
        for fname, content in (run.get("tamper") or {}).items():
            write_text(rdir / "work" / fname, content)
        for fname in (run.get("delete") or []):
            p = rdir / "work" / fname
            if p.exists():
                p.unlink()
        for op in run.get("ops", []):
            argv = [sys.executable, str(ROOT / sc["seam"]), op["op"], "--store", str(rdir / "seam" / "store.json")]
            for flag in ("key", "url", "title", "favicon"):
                if op.get(flag):
                    argv += ["--" + flag, _subst(op[flag], resolve)]
            if op.get("file"):
                argv += ["--file", str(rdir / "work" / op["file"])]
            r = subprocess.run(argv, capture_output=True, text=True)
            if r.returncode != op.get("exit", 0):
                out.append("%s: seam %s exited %d, expected %d: %s" % (
                    name, op["op"], r.returncode, op.get("exit", 0), (r.stdout or r.stderr).strip()))
            if op["op"] == "publish" and r.returncode == 0:
                created[op["key"]] = json.loads(r.stdout)["url"]
        for fname, content in (run.get("post_tamper") or {}).items():
            write_text(rdir / "work" / fname, content)
        if run.get("delete_store") and (rdir / "seam" / "store.json").exists():
            (rdir / "seam" / "store.json").unlink()
        if "registry_raw" in run:
            write_text(rdir / "work" / "artifacts.json", run["registry_raw"])
        elif "registry" in run:
            rp = rdir / "work" / "artifacts.json"
            if run["registry"] is None:
                if rp.exists():
                    rp.unlink()
            else:
                dump_json(rp, _subst(run["registry"], resolve))
        if run.get("summary") is not None:
            write_text(rdir / "summary.md", run["summary"])
        prov = {"batch": None, "tier": "lifecycle", "scenario": scen["id"], "skill_sha": None, "dirty": None,
                "skill_ref": None, "model": None, "prompt_hash": None, "scenarios_hash": sha256_file(sc["_path"]),
                "scenarios_hash_now": sha256_file(sc["_path"]), "corpus_hash": None, "started_at": None,
                "wall_seconds": None, "tokens": None}
        g = grade_lifecycle(rdir, sc, scen, prov)

    flat = {"pass": g["pass"], "produced": g["produced"], "failed_checks": g["failed_checks"],
            "failures": g["failures"], "warnings": g["warnings"],
            "ledger.created": g["ledger"]["created"], "ledger.updated": g["ledger"].get("updated", 0),
            "ledger.artifacts_total": g["ledger"]["artifacts_total"]}
    for path, exp in case["expected"].items():
        act = flat.get(path, "<absent>")
        if not expect_ok(act, exp):
            out.append("%s: %s expected %s, got %s" % (name, path, json.dumps(exp, ensure_ascii=False),
                                                       json.dumps(act, ensure_ascii=False)))
    return out


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
        if case.get("type") == "lifecycle":
            failures += lifecycle_selftest_case(name, case, cdir)
            continue
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
        if case.get("type") == "capture":
            failures += selftest_capture(name, cdir, case)
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


# ------------------------------------------------------------------ lifecycle
#
# The behavioural eval for the artifact-lifecycle contract (references/report-format.md,
# "Artifact lifecycle"). A lifecycle run reviews the scratch corpus and publishes its
# deliverables through the publish seam; grading reads the registry it wrote, the seam's
# ledger, the run summary and the working folder — deterministically, with no model calls.

LIFECYCLE_DIR = ROOT / "evals" / "lifecycle"
SCENARIOS_FILE = LIFECYCLE_DIR / "scenarios.json"
REGISTRY_FIELDS = ("url", "title", "favicon", "last_published", "cycle_date")
OUTCOMES = ("create_and_register", "update_in_place", "recreate", "adopt_and_update", "no_publish")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_scenarios(path=None):
    p = Path(path) if path else SCENARIOS_FILE
    if not p.exists():
        raise Fail("scenario file missing: %s" % rel(p))
    sc = load_json(p)
    sc["_path"] = str(p)
    return sc


def deliverables_of(sc, scen):
    """The deliverable map for one scenario: the shared map, with the scenario's own overrides on top.

    A scenario that reviews a different corpus names different teams, so the copy that reaches the
    runner has to follow the corpus rather than the other way round."""
    return {**sc.get("deliverables", {}), **(scen.get("deliverables") or {})}


def scenario_of(sc, sid):
    for s in sc["scenarios"]:
        if s["id"] == sid:
            return s
    raise Fail("unknown scenario %r; known: %s" % (sid, ", ".join(s["id"] for s in sc["scenarios"])))


def parse_ts(s):
    """An ISO-8601 instant with a UTC designator, or None."""
    if not isinstance(s, str) or not s.strip():
        return None
    try:
        d = _dt.datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else None


def validate_scenarios(sc, keys=None):
    """-> [error strings]. Structure, corpus-is-not-a-fixture, and per-outcome seed consistency."""
    errs = []
    where = rel(sc.get("_path", SCENARIOS_FILE))

    def err(msg):
        errs.append("%s: %s" % (where, msg))

    for field in ("version", "corpus", "seam", "prompt_template", "deliverables", "summary_markers", "scenarios"):
        if field not in sc:
            err("missing field %r" % field)
    if errs:
        return errs
    corpus = ROOT / sc["corpus"]
    if not corpus.exists():
        err("corpus %s does not exist" % sc["corpus"])
    elif Path(sc["corpus"]).parts[0] == "examples" or "/examples/" in sc["corpus"]:
        err("corpus %s is under examples/ — a fixture is publish-exempt and cannot exercise this contract" % sc["corpus"])
    else:
        fixtures = {k["fixture"] for k in (keys if keys is not None else load_keys())}
        if sc["corpus"] in fixtures:
            err("corpus %s is a fixture named by an answer key — it is publish-exempt" % sc["corpus"])
        if ANSWER_KEY_HEADING in read_text(corpus):
            err("corpus %s carries an answer-key section — it is a fixture, not a scratch corpus" % sc["corpus"])
    for f in ("seam", "prompt_template"):
        if not (ROOT / sc[f]).exists():
            err("%s %s does not exist" % (f, sc[f]))
    if not sc["deliverables"]:
        err("deliverables is empty")
    for dk, d in sc["deliverables"].items():
        if not re.match(r"^[a-z0-9][a-z0-9\-]*(?:/[a-z0-9][a-z0-9\-]*)?$", dk):
            err("deliverable key %r is not a slug like 'portfolio-dashboard' or 'team-report/<team>'" % dk)
        for field in ("label", "ask", "file"):
            if not str(d.get(field, "")).strip():
                err("deliverable %s: %s must be a non-empty string" % (dk, field))
    required_markers = ["recreate", "reason"]
    if any(v == "no_publish" for s in sc["scenarios"] for v in (s.get("expect") or {}).values()):
        required_markers.append("exempt")
    for m in required_markers:
        if not sc["summary_markers"].get(m):
            err("summary_markers.%s is empty" % m)
    seen = set()
    for s in sc["scenarios"]:
        sid = s.get("id", "?")
        if sid in seen:
            err("duplicate scenario id %s" % sid)
        seen.add(sid)
        if not str(s.get("title", "")).strip():
            err("%s: title must be a non-empty string" % sid)
        if not DATE_RE.match(str(s.get("cycle_date", ""))):
            err("%s: cycle_date must look like 2026-09-14" % sid)
        seed = s.get("seed") or {}
        reg = seed.get("registry") or {}
        arts = {a["url"]: a for a in seed.get("seam_artifacts", []) if isinstance(a, dict) and "url" in a}
        if len(arts) != len(seed.get("seam_artifacts", [])):
            err("%s: seam_artifacts need unique 'url' fields" % sid)
        for a in seed.get("seam_artifacts", []):
            for field in ("url", "title", "favicon"):
                if not str(a.get(field, "")).strip():
                    err("%s: seeded artifact %r missing %s" % (sid, a.get("url"), field))
        for name, content in (seed.get("work_files") or {}).items():
            if "/" in name or not name.strip():
                err("%s: seeded work file %r must be a plain file name" % (sid, name))
            if not str(content).strip():
                err("%s: seeded work file %s has empty content" % (sid, name))
        dels = deliverables_of(sc, s)
        for dk, d in (s.get("deliverables") or {}).items():
            for field in ("label", "ask", "file"):
                if not str(d.get(field, "")).strip():
                    err("%s: deliverable override %s: %s must be a non-empty string" % (sid, dk, field))
        for k, e in reg.items():
            if k not in dels:
                err("%s: seeded registry key %s is not a declared deliverable" % (sid, k))
            for field in REGISTRY_FIELDS:
                if not str(e.get(field, "")).strip():
                    err("%s: seeded entry %s missing %s" % (sid, k, field))
            if not parse_ts(e.get("last_published")):
                err("%s: seeded entry %s has an unparseable last_published" % (sid, k))
        exp = s.get("expect") or {}
        if not exp:
            err("%s: expect is empty" % sid)
        exempt = any(v == "no_publish" for v in exp.values())
        if exempt and not all(v == "no_publish" for v in exp.values()):
            err("%s: a no_publish scenario cannot mix outcomes — a fixture run publishes nothing at all" % sid)
        scorpus = s.get("corpus")
        if scorpus is not None:
            sp = ROOT / scorpus
            if not sp.exists():
                err("%s: corpus %s does not exist" % (sid, scorpus))
            is_fixture = scorpus in {k["fixture"] for k in (keys if keys is not None else load_keys())}
            if exempt and not is_fixture:
                err("%s: a no_publish scenario must name one of the skill's own fixtures as its corpus" % sid)
            if not exempt and is_fixture:
                err("%s: corpus %s is a fixture — a publishing scenario cannot use one" % (sid, scorpus))
        elif exempt:
            err("%s: a no_publish scenario must name a fixture corpus of its own" % sid)
        if exempt and (reg or arts):
            err("%s: a no_publish scenario seeds no registry and no artifacts" % sid)
        for k, outcome in exp.items():
            if k not in dels:
                err("%s: expected key %s is not a declared deliverable" % (sid, k))
            if outcome not in OUTCOMES:
                err("%s: %s outcome %r must be one of %s" % (sid, k, outcome, ", ".join(OUTCOMES)))
                continue
            entry = reg.get(k)
            if outcome == "no_publish":
                continue
            if outcome == "create_and_register" and entry:
                err("%s: %s expects a create but the registry seeds an entry" % (sid, k))
            if outcome in ("update_in_place", "recreate") and not entry:
                err("%s: %s expects %s but no registry entry is seeded" % (sid, k, outcome))
            if outcome == "update_in_place" and entry and entry["url"] not in arts:
                err("%s: %s expects an update but its seeded URL is not a live seam artifact" % (sid, k))
            if outcome == "recreate" and entry and entry["url"] in arts:
                err("%s: %s expects a re-create but its seeded URL is live in the seam" % (sid, k))
            if outcome == "adopt_and_update":
                supplied = (s.get("supplied_urls") or {}).get(k)
                if not supplied:
                    err("%s: %s expects an adopt but no supplied_urls entry exists" % (sid, k))
                elif supplied not in arts:
                    err("%s: %s supplied URL is not a live seam artifact" % (sid, k))
                elif entry and entry["url"] == supplied:
                    err("%s: %s supplied URL equals the seeded entry — the adopt would be unobservable" % (sid, k))
        for k in (s.get("supplied_urls") or {}):
            if exp.get(k) != "adopt_and_update":
                err("%s: supplied_urls names %s, whose expected outcome is not adopt_and_update" % (sid, k))
    return errs


def scenario_decl_hash(sc, scen):
    """A hash of what this scenario asks — the fields grading consumes, not the prose around them."""
    decl = {"cycle_date": scen["cycle_date"], "corpus": scen.get("corpus") or sc["corpus"],
            "expect": scen["expect"], "seed": scen.get("seed") or {},
            "supplied_urls": scen.get("supplied_urls") or {},
            "files": {k: (deliverables_of(sc, scen)[k].get("file")) for k in scen["expect"]},
            "markers": {m: sc["summary_markers"].get(m) for m in
                        (["recreate", "reason"] if any(v != "no_publish" for v in scen["expect"].values())
                         else ["exempt"])}}
    return hashlib.sha256(json.dumps(decl, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def seed_run(rdir, scen):
    """Seed a run directory's working folder and seam store from the scenario declaration."""
    rdir = Path(rdir)
    work = rdir / "work"
    work.mkdir(parents=True, exist_ok=True)
    seed = scen.get("seed") or {}
    if seed.get("registry"):
        dump_json(work / "artifacts.json", seed["registry"])
    for name, content in (seed.get("work_files") or {}).items():
        write_text(work / name, content)
    store = {"artifacts": {}, "ledger": [], "seq": 0}
    for a in seed.get("seam_artifacts", []):
        store["artifacts"][a["url"]] = {"url": a["url"], "title": a["title"], "favicon": a["favicon"],
                                        "created_at": a.get("created_at", "2026-06-15T10:00:00Z"),
                                        "updated_at": a.get("created_at", "2026-06-15T10:00:00Z"),
                                        "versions": 1, "content_sha": None, "bytes": 0, "seeded": True}
    dump_json(rdir / "seam" / "store.json", store)
    return work


def lifecycle_prompt_ctx(sc, scen, rdir, snap):
    """The placeholder values the frozen lifecycle template is rendered with."""
    rdir = Path(rdir)
    keys = list(scen["expect"])
    dels = deliverables_of(sc, scen)
    lines = []
    for k in keys:
        d = dels[k]
        lines.append("  - `%s` — %s. Write it to `%s`." % (
            k, d["ask"], rdir / "work" / d["file"].replace("{{cycle_date}}", scen["cycle_date"])))
    supplied = scen.get("supplied_urls") or {}
    sup = ""
    if supplied:
        parts = ["- The user has an artifact already and wants it kept: %s." % "; ".join(
            "for `%s`, use %s" % (k, u) for k, u in supplied.items())]
        sup = "\n".join(parts) + "\n"
    exempt = any(v == "no_publish" for v in scen["expect"].values())
    note = ("- **This run supplies a publish seam and a review working folder.** Whether the skill's publish step "
            "runs at all is for the skill's own rules to decide — read them, apply them to this corpus, and if the "
            "step is skipped say so and why in the run summary."
            if exempt else
            "- **This run is not publish-exempt.** It supplies a publish seam and a review working folder, so the "
            "skill's publish step runs in full — work the decision procedure it points to exactly as written, and "
            "do not skip it.")
    # For a fixture corpus the prompt must not assert the run's exemption status either way, and must not
    # forbid opening the very file it names — deciding that is the skill's job, and the point of the test.
    tail = ("take the skill's publish step on its deliverables." if exempt else "publish its deliverables.")
    scope = ("do not open any other file under `examples/` or anything under `evals/keys/`," if exempt
             else "do not open anything under `examples/` or `evals/keys/`,")
    cnote = "" if exempt else " This corpus is **not** one of the skill's own fixtures."
    publish_clause = ("" if exempt else ", publish that exact file")
    summary_ask = ("what the skill's publish step did with each deliverable and why — every artifact and registry "
                   "action you took, or the reason you took none."
                   if exempt else
                   "what you published under each key, to which URL, and every registry action you took — including, "
                   "if one happened, what you had to create rather than update and why.")
    return {"skill_md": snap / "SKILL.md", "references_dir": snap / "references", "exemption_note": note,
            "task_tail": tail, "corpus_scope_note": scope, "corpus_note": cnote,
            "publish_clause": publish_clause, "summary_ask": summary_ask,
            "deliverables_header": ("- Deliverables, one per key:" if exempt
                                    else "- Deliverables, each published under its own key:"),
            "corpus_path": ROOT / (scen.get("corpus") or sc["corpus"]), "run_dir": rdir, "work_dir": rdir / "work",
            "seam": ROOT / sc["seam"], "store": rdir / "seam" / "store.json",
            "summary_path": rdir / "summary.md", "cycle_date": scen["cycle_date"],
            "deliverables_block": "\n".join(lines), "supplied_block": sup}


def render_lifecycle_prompt(sc, scen, rdir, snap):
    tpl = read_text(ROOT / sc["prompt_template"])
    for k, v in lifecycle_prompt_ctx(sc, scen, rdir, snap).items():
        tpl = tpl.replace("{{%s}}" % k, str(v))
    left = re.findall(r"{{\w+}}", tpl)
    if left:
        raise Fail("unresolved placeholders in %s: %s" % (sc["prompt_template"], ", ".join(left)))
    return tpl


def cmd_lifecycle_plan(args):
    sc = load_scenarios(args.scenarios_file)
    errs = validate_scenarios(sc)
    if errs:
        raise Fail("refusing to plan on an invalid scenario file:\n  " + "\n  ".join(errs))
    ids = args.scenarios.split(",") if args.scenarios else [s["id"] for s in sc["scenarios"]]
    scens = [scenario_of(sc, i) for i in ids]
    head = git("rev-parse", "HEAD")
    batch = args.batch or "%s-lifecycle-%s" % (_dt.date.today().isoformat(), head[:7])
    bdir = RUNS_DIR / batch
    bjson = bdir / "batch.json"
    if bjson.exists():
        meta = load_json(bjson)
    else:
        meta = {"harness_version": HARNESS_VERSION, "batch": batch, "tier": "lifecycle", "created": now_iso(),
                "scenarios": ids, "arms": {"candidate": snapshot_from_worktree(bdir / "skill" / "candidate")},
                "prompt_hash": sha256_file(ROOT / sc["prompt_template"]),
                "scenarios_hash": sha256_file(sc["_path"]), "corpus_hash": sha256_file(ROOT / sc["corpus"]),
                "decl_hashes": {}, "corpus_hashes": {}, "runs": []}
    meta.setdefault("decl_hashes", {})
    meta.setdefault("corpus_hashes", {})
    snap = ROOT / meta["arms"]["candidate"]["snapshot"]
    if not (snap / "SKILL.md").exists():
        snapshot_from_worktree(snap)
    index = {r["scenario"]: r for r in meta["runs"]}
    pending = []
    for scen in scens:
        rdir = bdir / scen["id"]
        summary, prompt = rdir / "summary.md", rdir / "prompt.md"
        seeded = (rdir / "seam" / "store.json").exists()
        if seeded and args.reseed and (args.force or not summary.exists()):
            # A run that died mid-flight may have left a half-written ledger or working folder;
            # grading that would judge wreckage rather than behaviour. Reset it to its seeded state.
            for sub in ("work", "seam"):
                if (rdir / sub).exists():
                    shutil.rmtree(rdir / sub)
            meta["decl_hashes"][scen["id"]] = scenario_decl_hash(sc, scen)
            meta["corpus_hashes"][scen["id"]] = sha256_file(ROOT / (scen.get("corpus") or sc["corpus"]))
            if args.force:
                # The scenario's own declaration changed: the recorded run answers a question that is
                # no longer being asked, so it is redone rather than re-interpreted.
                for f in ("summary.md", "grade.json", "run.json", "prompt.md"):
                    if (rdir / f).exists():
                        (rdir / f).unlink()
            seeded = False
        if not seeded:
            seed_run(rdir, scen)
        if not prompt.exists():
            write_text(prompt, render_lifecycle_prompt(sc, scen, rdir, snap))
        meta["decl_hashes"].setdefault(scen["id"], scenario_decl_hash(sc, scen))
        meta["corpus_hashes"].setdefault(scen["id"], sha256_file(ROOT / (scen.get("corpus") or sc["corpus"])))
        entry = index.get(scen["id"]) or {"scenario": scen["id"]}
        entry.update({"dir": rel(rdir), "prompt": rel(prompt), "summary": rel(summary),
                      "title": scen["title"], "status": "done" if summary.exists() else "pending"})
        if scen["id"] not in index:
            meta["runs"].append(entry)
            index[scen["id"]] = entry
        if entry["status"] == "pending":
            pending.append({"scenario": scen["id"], "run_dir": str(rdir), "prompt": str(prompt),
                            "summary": str(summary)})
    dump_json(bjson, meta)
    if args.json:
        print(json.dumps({"batch": batch, "batch_dir": str(bdir), "pending": pending}, indent=2))
    else:
        print("batch %s (lifecycle): %d run(s) planned, %d pending" % (batch, len(meta["runs"]), len(pending)))
        for p in pending:
            print("  pending %s -> %s" % (p["scenario"], p["prompt"]))
        print("batch dir: %s" % bdir)


# ------------------------------------------------------------- lifecycle grade

def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def work_shas(work):
    out = {}
    for p in sorted(work.rglob("*")):
        if p.is_file() and p.name != "artifacts.json":
            out[sha_bytes(p.read_bytes())] = rel(p)
    return out


def grade_lifecycle(rdir, sc, scen, provenance):
    rdir = Path(rdir)
    work, store_p, summary_p = rdir / "work", rdir / "seam" / "store.json", rdir / "summary.md"
    keys = list(scen["expect"])
    seed = scen.get("seed") or {}
    seeded_reg = seed.get("registry") or {}
    supplied = scen.get("supplied_urls") or {}
    failures, warnings = [], []
    gchecks, kchecks = [], {}

    def chk(bucket, name, ok, detail="", key=None):
        bucket.append({"check": name, "pass": bool(ok), "detail": detail})
        if not ok:
            failures.append("%s%s: %s" % (("%s — " % key) if key else "", name, detail))
        return bool(ok)

    if not summary_p.exists():
        return {"harness_version": HARNESS_VERSION, "graded_at": now_iso(), "scenario": scen["id"],
                "scenario_title": scen["title"], "produced": False, "provenance": provenance, "keys": {},
                "global": [{"check": "summary_written", "pass": False, "detail": "no summary.md in the run directory"}],
                "ledger": {"ops": [], "artifacts_total": 0, "seeded": len(seed.get("seam_artifacts", [])), "created": 0},
                "failures": ["run not produced: no summary.md"], "warnings": [], "failed_checks": ["summary_written"],
                "pass": False}

    summary = read_text(summary_p)
    summary2 = re.sub(r"\s+", " ", typo(summary)).lower()
    chk(gchecks, "summary_written", bool(summary.strip()), "summary.md is empty")

    store_present = store_p.exists()
    store = load_json(store_p) if store_present else {"artifacts": {}, "ledger": [], "seq": 0}
    ledger = store.get("ledger", [])
    chk(gchecks, "seam_store_present", store_present,
        "the seam store this run was seeded with is gone — nothing can be graded from its ledger")
    ops = [{k: e.get(k) for k in ("n", "op", "key", "url", "title", "favicon", "content_sha", "result", "reason")}
           for e in ledger]
    creates = [e for e in ledger if e.get("op") == "publish"]
    updates = [e for e in ledger if e.get("op") == "update"]

    dels = deliverables_of(sc, scen)
    exempt = bool(keys) and all(scen["expect"][k] == "no_publish" for k in keys)
    registry, reg_ok = {}, False
    rp = work / "artifacts.json"
    if exempt:
        # A fixture run publishes nothing and writes no registry — anywhere, seam or not.
        found = [rel(p) for p in rdir.rglob("artifacts.json")]
        chk(gchecks, "no_registry_written", not found,
            "a registry file was written: %s" % ", ".join(found))
        chk(gchecks, "nothing_published", not creates and not updates and not store.get("artifacts"),
            "published through the seam: %d create(s), %d update(s), %d artifact(s)" % (
                len(creates), len(updates), len(store.get("artifacts", {}))))
        chk(gchecks, "exempt_skip_explained",
            any(m in summary2 for m in sc["summary_markers"].get("exempt", [])),
            "the run summary never says publishing was skipped or why")
        if rp.exists():
            registry = load_json(rp) if rp.stat().st_size else {}
    elif not rp.exists():
        chk(gchecks, "registry_at_working_folder", False, "no artifacts.json in the review working folder")
    else:
        try:
            loaded = load_json(rp)
            reg_ok = isinstance(loaded, dict)
            registry = loaded if reg_ok else {}
        except Exception as e:  # noqa: BLE001
            chk(gchecks, "registry_at_working_folder", False, "artifacts.json is not valid JSON: %s" % e)
        else:
            stray = [rel(p) for p in rdir.rglob("artifacts.json") if p.resolve() != rp.resolve()]
            chk(gchecks, "registry_at_working_folder", reg_ok and not stray,
                "registry is not a JSON object" if not reg_ok else "extra registry file(s): %s" % ", ".join(stray))

    for key in keys:
        outcome = scen["expect"][key]
        entry = registry.get(key) if isinstance(registry.get(key), dict) else None
        seeded = seeded_reg.get(key)
        ck = kchecks.setdefault(key, {"outcome": outcome, "checks": [], "ops": {}})
        ic, iu = [e for e in creates if e.get("key") == key], [e for e in updates if e.get("key") == key]
        ck["ops"] = {"creates": [e["url"] for e in ic], "updates": [e["url"] for e in iu],
                     "failed_updates": sum(1 for e in ledger if e.get("op") == "update_failed" and e.get("key") == key),
                     "reads": sum(1 for e in ledger if e.get("op") == "read")}
        c = ck["checks"]
        if outcome == "no_publish":
            chk(c, "not_published", not ic and not iu,
                "published for an exempt corpus: %d create(s), %d update(s)" % (len(ic), len(iu)), key)
            chk(c, "not_registered", entry is None, "a registry entry was written for an exempt corpus", key)
            continue
        if not chk(c, "registry_entry_written", entry is not None, "no registry entry for this key", key):
            continue
        missing = [f for f in REGISTRY_FIELDS if not str(entry.get(f, "")).strip()]
        chk(c, "registry_fields_present", not missing, "entry missing %s" % ", ".join(missing), key)
        ts = parse_ts(entry.get("last_published"))
        chk(c, "last_published_valid", ts is not None,
            "last_published %r is not an ISO-8601 UTC instant" % entry.get("last_published"), key)
        chk(c, "cycle_date_current", entry.get("cycle_date") == scen["cycle_date"],
            "cycle_date is %r, expected %r" % (entry.get("cycle_date"), scen["cycle_date"]), key)

        acts = sorted(ic + iu, key=lambda e: e.get("n", 0))
        must_verify = (seeded or {}).get("url") if outcome in ("update_in_place", "recreate") else (
            supplied.get(key) if outcome == "adopt_and_update" else None)
        if must_verify and acts:
            reads = [e for e in ledger if e.get("op") in ("read", "update_failed")
                     and e.get("url") == must_verify and e.get("n", 0) < acts[0].get("n", 0)]
            chk(c, "registered_url_verified", bool(reads),
                "acted on %s without verifying %s through the seam first" % (key, must_verify), key)

        if outcome == "create_and_register":
            chk(c, "created_once", len(ic) == 1, "expected exactly 1 create, found %d" % len(ic), key)
            if len(ic) == 1:
                chk(c, "registry_url_is_created_url", entry.get("url") == ic[0]["url"],
                    "registry url %r but the artifact was created at %r" % (entry.get("url"), ic[0]["url"]), key)
                chk(c, "registry_matches_artifact", entry.get("title") == ic[0].get("title") and
                    entry.get("favicon") == ic[0].get("favicon"),
                    "registry title/favicon %r/%r differ from the published %r/%r" % (
                        entry.get("title"), entry.get("favicon"), ic[0].get("title"), ic[0].get("favicon")), key)
            chk(c, "updates_target_registered_url", all(e["url"] == entry.get("url") for e in iu),
                "update(s) at %s, registry names %s" % ([e["url"] for e in iu], entry.get("url")), key)
        elif outcome == "update_in_place":
            chk(c, "no_fork", not ic, "created %d artifact(s) for a key that had a registry entry: %s" % (
                len(ic), ", ".join(e["url"] for e in ic)), key)
            chk(c, "updated_in_place", len(iu) >= 1, "no update recorded for this key", key)
            chk(c, "updates_target_registered_url", all(e["url"] == seeded["url"] for e in iu),
                "update(s) at %s, registered URL is %s" % ([e["url"] for e in iu], seeded["url"]), key)
            chk(c, "registry_url_unchanged", entry.get("url") == seeded["url"],
                "registry url changed from %s to %r" % (seeded["url"], entry.get("url")), key)
            chk(c, "title_favicon_unchanged", entry.get("title") == seeded["title"] and
                entry.get("favicon") == seeded["favicon"],
                "title/favicon changed from %r/%r to %r/%r" % (seeded["title"], seeded["favicon"],
                                                               entry.get("title"), entry.get("favicon")), key)
            seed_ts = parse_ts(seeded["last_published"])
            chk(c, "timestamp_advanced", bool(ts and seed_ts and ts > seed_ts),
                "last_published %r does not advance on %r" % (entry.get("last_published"), seeded["last_published"]), key)
        elif outcome == "recreate":
            chk(c, "recreated_once", len(ic) == 1, "expected exactly 1 replacement create, found %d" % len(ic), key)
            chk(c, "no_successful_update", not iu, "updated %s although the registered URL was dead" % (
                [e["url"] for e in iu]), key)
            if len(ic) == 1:
                chk(c, "registry_overwritten", entry.get("url") == ic[0]["url"] and entry.get("url") != seeded["url"],
                    "registry url %r, replacement published at %r, dead URL was %r" % (
                        entry.get("url"), ic[0]["url"], seeded["url"]), key)
                chk(c, "registry_matches_artifact", entry.get("title") == ic[0].get("title") and
                    entry.get("favicon") == ic[0].get("favicon"),
                    "registry title/favicon %r/%r differ from the published %r/%r" % (
                        entry.get("title"), entry.get("favicon"), ic[0].get("title"), ic[0].get("favicon")), key)
            # A re-create is a publish, so Refresh applies: the dead entry's timestamp is exactly the
            # value that must not survive it.
            seed_ts = parse_ts(seeded["last_published"])
            chk(c, "timestamp_advanced", bool(ts and seed_ts and ts > seed_ts),
                "last_published %r does not advance on the replaced entry's %r" % (
                    entry.get("last_published"), seeded["last_published"]), key)
        elif outcome == "adopt_and_update":
            url = supplied[key]
            chk(c, "no_fork", not ic, "created %d artifact(s) although a URL was supplied: %s" % (
                len(ic), ", ".join(e["url"] for e in ic)), key)
            chk(c, "adopted_url_recorded", entry.get("url") == url,
                "registry url %r, supplied URL was %s" % (entry.get("url"), url), key)
            chk(c, "updated_in_place", len(iu) >= 1, "no update recorded for this key", key)
            chk(c, "updates_target_adopted_url", all(e["url"] == url for e in iu),
                "update(s) at %s, supplied URL is %s" % ([e["url"] for e in iu], url), key)
            art = store.get("artifacts", {}).get(url, {})
            chk(c, "registry_matches_artifact", entry.get("title") == art.get("title") and
                entry.get("favicon") == art.get("favicon"),
                "registry title/favicon %r/%r differ from the adopted artifact's %r/%r" % (
                    entry.get("title"), entry.get("favicon"), art.get("title"), art.get("favicon")), key)
            # The adopted artifact keeps its own identity: comparing the registry against the post-rename
            # store would agree with itself, so the seeded artifact is the reference.
            was = next((a for a in seed.get("seam_artifacts", []) if a["url"] == url), None)
            if was:
                chk(c, "adopted_artifact_unchanged",
                    art.get("title") == was["title"] and art.get("favicon") == was["favicon"],
                    "the adopted artifact was renamed from %r/%r to %r/%r" % (
                        was["title"], was["favicon"], art.get("title"), art.get("favicon")), key)
            if seeded:
                seed_ts = parse_ts(seeded["last_published"])
                chk(c, "timestamp_advanced", bool(ts and seed_ts and ts > seed_ts),
                    "last_published %r does not advance on %r" % (entry.get("last_published"),
                                                                  seeded["last_published"]), key)

    # The registry must describe the artifact it points at: a run that renames the living artifact
    # through the seam, or registers a URL the seam does not hold, leaves the two out of step.
    for key in keys:
        entry = registry.get(key) if isinstance(registry.get(key), dict) else None
        if not entry or scen["expect"][key] == "no_publish":
            continue
        c = kchecks[key]["checks"]
        art = store.get("artifacts", {}).get(entry.get("url"))
        if not chk(c, "registry_points_at_live_artifact", art is not None,
                   "registry names %r, which the seam does not hold" % entry.get("url"), key):
            continue
        chk(c, "registry_matches_live_artifact",
            entry.get("title") == art.get("title") and entry.get("favicon") == art.get("favicon"),
            "registry says %r/%r but the artifact now carries %r/%r" % (
                entry.get("title"), entry.get("favicon"), art.get("title"), art.get("favicon")), key)

    # What was published, not merely that something was. Set membership over the working folder let a run
    # publish last cycle's file, or one file under both keys, and still pass.
    shas_by_name = {}
    if work.exists():
        for p in sorted(work.rglob("*")):
            if p.is_file() and p.name != "artifacts.json":
                shas_by_name[p.name] = sha_bytes(p.read_bytes())
    for key in keys:
        d = dels.get(key) or {}
        want_name = str(d.get("file", "")).replace("{{cycle_date}}", scen["cycle_date"])
        acts = [e for e in creates + updates if e.get("key") == key]
        if not want_name:
            continue
        want_sha = shas_by_name.get(want_name)
        c = kchecks[key]["checks"]
        # Skipping the publish step is not licence to skip the review: the deliverable is still produced.
        if not chk(c, "deliverable_file_written", want_sha is not None,
                   "no %s in the working folder" % want_name, key):
            continue
        if not acts:
            continue
        wrong = [e for e in acts if e.get("content_sha") and e["content_sha"] != want_sha]
        chk(c, "published_own_deliverable", not wrong,
            "published content that is not %s (%s)" % (want_name, ", ".join(
                "%s@%s" % (e.get("op"), e.get("url")) for e in wrong)), key)

    extra_keys = [k for k in registry if k not in keys]
    chk(gchecks, "no_unexpected_registry_keys", not extra_keys,
        "registry holds key(s) no deliverable declares: %s" % ", ".join(extra_keys))
    off_key = [e for e in creates if e.get("key") not in keys]
    chk(gchecks, "no_stray_creates", not off_key,
        "artifact(s) created under no declared deliverable key: %s" % ", ".join(
            "%s@%s" % (e.get("key"), e.get("url")) for e in off_key))
    seeded_urls = {a["url"] for a in seed.get("seam_artifacts", [])}
    expected_total = len(seeded_urls) + len(creates)
    chk(gchecks, "no_stray_artifacts", len(store.get("artifacts", {})) == expected_total,
        "seam holds %d artifact(s); %d seeded plus %d created is %d" % (
            len(store.get("artifacts", {})), len(seeded_urls), len(creates), expected_total))

    forks = [e for e in creates if e.get("key") in seeded_reg]
    if forks:
        hit_re = any(m in summary2 for m in sc["summary_markers"]["recreate"])
        hit_why = any(m in summary2 for m in sc["summary_markers"]["reason"])
        chk(gchecks, "create_over_entry_reported", hit_re and hit_why,
            "a create happened while a registry entry existed (%s); the run summary %s" % (
                ", ".join("%s@%s" % (e.get("key"), e.get("url")) for e in forks),
                "never says a re-create happened" if not hit_re else "gives no reason for it"))
        unnamed = [e["key"] for e in forks
                   if e.get("key") not in summary2 and dels[e["key"]]["label"].lower() not in summary2]
        chk(gchecks, "create_over_entry_names_deliverable", not unnamed,
            "the run summary never names the re-created deliverable(s): %s" % ", ".join(unnamed))

    shas = work_shas(work)
    unlocal = [e for e in creates + updates if e.get("content_sha") and e["content_sha"] not in shas]
    chk(gchecks, "published_content_local", not unlocal,
        "published content is not a file in the working folder: %s" % ", ".join(
            "%s@%s" % (e.get("op"), e.get("key")) for e in unlocal))
    dated = [p.name for p in work.glob("%s*" % scen["cycle_date"])] if work.exists() else []
    chk(gchecks, "dated_output_written", bool(dated),
        "no file named for this cycle (%s*) in the working folder" % scen["cycle_date"])
    tampered = []
    for name, content in (seed.get("work_files") or {}).items():
        p = work / name
        if not p.exists():
            tampered.append("%s (deleted)" % name)
        elif sha_bytes(p.read_bytes()) != sha_bytes(content.encode("utf-8")):
            tampered.append("%s (modified)" % name)
    chk(gchecks, "prior_outputs_unmodified", not tampered,
        "a prior cycle's local output was changed: %s" % ", ".join(tampered))

    failed = [c["check"] for c in gchecks if not c["pass"]] + \
             [c["check"] for k in kchecks for c in kchecks[k]["checks"] if not c["pass"]]
    return {"harness_version": HARNESS_VERSION, "graded_at": now_iso(), "scenario": scen["id"],
            "scenario_title": scen["title"], "produced": True, "provenance": provenance,
            "keys": kchecks, "global": gchecks,
            "ledger": {"ops": ops, "artifacts_total": len(store.get("artifacts", {})),
                       "seeded": len(seeded_urls), "created": len(creates), "updated": len(updates)},
            "failures": failures, "warnings": warnings, "failed_checks": failed, "pass": not failures}


def summarize_lifecycle(g):
    return "%s | %s | creates %d updates %d | %s" % (
        "PASS" if g["pass"] else "FAIL", g["scenario"], g["ledger"]["created"], g["ledger"].get("updated", 0),
        "; ".join(g["failures"]) or "-")


def refresh_batch_status(bdir, meta, scenario, verdict):
    entry = next((r for r in meta["runs"] if r["scenario"] == scenario), None)
    if entry is None:
        return
    want = {"status": "done" if (ROOT / entry["summary"]).exists() else "pending", "pass": verdict}
    if {k: entry.get(k) for k in want} != want:
        entry.update(want)
        dump_json(bdir / "batch.json", meta)


def grade_lifecycle_dir(rdir, sc=None, write=True):
    rdir = Path(rdir).resolve()
    bdir, meta = find_batch(rdir)
    entry = next((r for r in meta["runs"] if (ROOT / r["dir"]).resolve() == rdir), None)
    if entry is None:
        raise Fail("%s is not a run of batch %s" % (rdir, meta["batch"]))
    sc = sc or load_scenarios()
    scen = scenario_of(sc, entry["scenario"])
    arm = meta["arms"]["candidate"]
    run_json = load_json(rdir / "run.json") if (rdir / "run.json").exists() else {}
    prov = {"batch": meta["batch"], "tier": meta["tier"], "scenario": entry["scenario"],
            "skill_sha": arm["skill_sha"], "dirty": arm["dirty"], "skill_ref": arm["ref"],
            "model": run_json.get("model"), "prompt_hash": meta["prompt_hash"],
            "scenarios_hash": meta["scenarios_hash"], "scenarios_hash_now": sha256_file(sc["_path"]),
            "corpus_hash": meta["corpus_hash"], "started_at": run_json.get("started_at"),
            "wall_seconds": run_json.get("wall_seconds"), "tokens": run_json.get("tokens")}
    prov["prompt_hash_now"] = sha256_file(ROOT / sc["prompt_template"])
    prov["corpus_hash"] = (meta.get("corpus_hashes") or {}).get(entry["scenario"]) or meta.get("corpus_hash")
    prov["corpus_hash_now"] = sha256_file(ROOT / (scen.get("corpus") or sc["corpus"]))
    # What matters is whether THIS run's prompt would differ today, not whether the shared template was
    # edited: a template change that leaves this scenario's rendering identical changes nothing about the run.
    prompt_p = rdir / "prompt.md"
    prompt_now = prompt_then = None
    if prompt_p.exists():
        try:
            prompt_now = hashlib.sha256(render_lifecycle_prompt(
                sc, scen, rdir, ROOT / arm["snapshot"]).encode("utf-8")).hexdigest()
        except Fail:
            prompt_now = None
        prompt_then = sha256_file(prompt_p)
    prov["prompt_rendered_hash"] = prompt_then
    prov["prompt_rendered_hash_now"] = prompt_now
    g = grade_lifecycle(rdir, sc, scen, prov)
    prov["decl_hash"] = (meta.get("decl_hashes") or {}).get(entry["scenario"])
    prov["decl_hash_now"] = scenario_decl_hash(sc, scen)
    for label, then, now in (("scenario's own declaration", prov["decl_hash"], prov["decl_hash_now"]),
                             ("prompt this run was given", prompt_then, prompt_now)):
        if then and now and then != now:
            g["warnings"].append("the %s changed since this run was planned — the run answered an "
                                 "earlier question; re-plan with --reseed --force to re-ask it" % label)
    if prov["corpus_hash"] and prov["corpus_hash_now"] and prov["corpus_hash"] != prov["corpus_hash_now"]:
        g["warnings"].append("the corpus has changed since this run reviewed it — provenance only, as grading "
                             "reads the run directory and never the corpus; re-run it if the change was material")
    if write:
        dump_json(rdir / "grade.json", g)
        refresh_batch_status(bdir, meta, entry["scenario"], g["pass"])
    return g


def cmd_lifecycle_grade(args):
    sc = load_scenarios(args.scenarios_file)
    dirs = [Path(d) for d in args.run_dir]
    if args.batch_dir:
        meta = load_json(Path(args.batch_dir) / "batch.json")
        dirs += [ROOT / r["dir"] for r in meta["runs"]]
    if not dirs:
        raise Fail("lifecycle-grade needs run directories or --batch-dir")
    bad = 0
    for d in dirs:
        g = grade_lifecycle_dir(d, sc, write=not args.no_write)
        print("%s: %s" % (rel(d), summarize_lifecycle(g)))
        for w in g["warnings"]:
            print("    warning: %s" % w)
        bad += 0 if g["pass"] else 1
    print("lifecycle: %d run(s), %d failing" % (len(dirs), bad))
    if bad:
        sys.exit(1)


# ---------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(prog="harness.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="validate keys, anchors, coverage, freshness, lifecycle scenarios")
    p.add_argument("--key", help="check one key file instead of every key under evals/keys")
    p.add_argument("--scenarios-file", dest="scenarios_file", help="check this lifecycle scenario file instead of evals/lifecycle/scenarios.json")
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

    p = sub.add_parser("capture", help="write a run's report.md byte-exact from its subagent transcript, plus run.json")
    p.add_argument("run_dir")
    p.add_argument("--transcript", required=True, help="the Agent launch result's output_file (JSONL)")
    p.add_argument("--tokens", type=int, help="from the Agent usage line; default: the transcript's summed usage")
    p.add_argument("--seconds", type=float, help="from the Agent usage line; default: first-to-last transcript timestamp")
    p.add_argument("--model", help="cross-check only: the model is taken from the transcript, a disagreement fails")
    p.add_argument("--agent-error", help="record the run as not produced (agent-error) with this text")
    p.set_defaults(fn=cmd_capture)

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

    p = sub.add_parser("lifecycle-plan", help="create or resume a lifecycle batch and list pending runs")
    p.add_argument("--scenarios", help="comma-separated scenario ids (default: all)")
    p.add_argument("--scenarios-file", dest="scenarios_file", help="use this scenario file instead of evals/lifecycle/scenarios.json")
    p.add_argument("--batch", help="batch id (default <date>-lifecycle-<sha7>)")
    p.add_argument("--force", action="store_true",
                   help="with --reseed, also reset a run that already has a summary — for a scenario whose declaration changed")
    p.add_argument("--reseed", action="store_true",
                   help="reset a pending run's working folder and seam store to the seeded state (for a run that died mid-flight); never touches a run that has a summary")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_lifecycle_plan)

    p = sub.add_parser("lifecycle-grade", help="grade lifecycle runs against their scenario declarations")
    p.add_argument("run_dir", nargs="*")
    p.add_argument("--batch-dir", dest="batch_dir", help="grade every run of this lifecycle batch")
    p.add_argument("--scenarios-file", dest="scenarios_file")
    p.add_argument("--no-write", action="store_true", help="do not write grade.json")
    p.set_defaults(fn=cmd_lifecycle_grade)

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
