import json, shutil, sys
from pathlib import Path
ROOT = Path(".").resolve()
CASES = ROOT / "evals/grader/selftest/cases"
CASES.mkdir(parents=True, exist_ok=True)

def case(name, report, expected, key="sample-portfolio.json", slice=None, extra_files=None):
    d = CASES / name; d.mkdir(exist_ok=True)
    (d / "report.md").write_text(report, encoding="utf-8")
    c = {"key": key, "slice": slice, "report": "report.md", "expected": expected}
    for fn, content in (extra_files or {}).items():
        (d / fn).write_text(content, encoding="utf-8")
        if fn.endswith(".json"): c["key"] = fn
    (d / "case.json").write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

P = "sample-portfolio.md"
def ap(sev, aid, name, team, ev_lines, why="x", rewrite="\"<placeholder>\"", also=None):
    lines = list(ev_lines) + (["- Also: " + also] if also else [])
    return "### [{}] {} {} — {}\n{}\n- Why it's a problem: {}\n- Scores affected: K1=1\n- Suggested rewrite: {}\n".format(sev, aid, name, team, "\n".join(lines), why, rewrite)
def E(q, heading, line, label="Evidence", path=P):
    return "- {}: \"{}\" ({} › {} › line {})".format(label, q, path, heading, line)

G11 = ("Increase trial-to-paid conversion to 22%.", "Objective G1: Make the first week with Brightledger magical", 39)
PL13 = ("Improve internal developer satisfaction score to 8/10.", "Objective PL1: Keep the lights on, cheaper", 59)
PL11 = ("Maintain API uptime at or above 99.9%.", "Objective PL1: Keep the lights on, cheaper", 57)
APX = ("API uptime, trailing 90 days: 99.95% (Datadog SLO monitor).", "Appendix — Q2 2026 business review (extracts)", 89)
P12 = ("Ship checkout & billing API v2 to GA by Sep 26.", "Objective P1: Make checkout something customers never think about", 23)
D21 = ("Ship personalized onboarding checklists to 100% of new signups.", "Objective D2: Own onboarding personalization end-to-end", 79)
PL1 = ("Keep the lights on, cheaper", "Objective PL1: Keep the lights on, cheaper", 56)
port_head = "# Report\n\n## 3. Per-team goodness findings\n\n"

case("quote-verbatim", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth", [E(*G11)]),
     {"rows.G2.status": "found", "rows.G2.id_exact": True, "quotes.verbatim": 1, "quotes.fabricated": 0, "quotes.near_miss": 0, "extras": []})
case("quote-near-miss-curly-period", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth",
     [E("Make the first week with Brightledger magical.", "Objective G1", 38).replace('"', "“", 1).replace('"', "”", 1),
      E("Increase **trial-to-paid** conversion to 22%.", "Objective G1", 39)]),
     {"rows.G2.status": "found", "quotes.near_miss": 2, "quotes.verbatim": 0, "quotes.fabricated": 0, "failures": {"contains": ["missed row G1"]}})
case("quote-fabricated-paraphrase", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth",
     [E("Trial conversion should reach 22 percent.", "Objective G1", 39)]),
     {"quotes.fabricated": 1, "pass": False, "failures": {"contains": ["fabricated quotes: 1"]}, "rows.G2.status": "partial"})
case("quote-out-of-scope", "# Platform review\n\n## 3. Findings\n\n" + ap("Major", "AP-04", "KR Without Baseline", "Platform", [E(*G11)]),
     {"quotes.out_of_scope": 1, "quotes.fabricated": 0, "budget.counted": 1, "extras": ["AP-04@unlocated"]}, slice="platform-single-team")
case("quote-key-leak", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth",
     [E("states a target with no current value, and none is retrievable anywhere in this corpus", "Objective G1", 39)]),
     {"quotes.fabricated": 1, "quotes.key_leak": 1, "pass": False})
case("supporting-unverified-search-terms", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth", [E(*G11)],
     why="searched every page for \"a stated starting value for the metric\" and \"any trailing ninety-day actual\" ({} › Growth team › line 34) and found nothing".format(P)),
     {"quotes.unverified": 2, "quotes.fabricated": 0, "quotes.supporting": 2, "quotes.evidence": 1, "rows.G2.status": "found",
      "structure.warnings": {"contains": ["unverified supporting quote"]}})
case("supporting-term-search-words", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth", [E(*G11)],
     why="searched every page for \"baseline\" and \"current value\" ({} › Growth team › line 34) and found nothing".format(P)),
     {"quotes.term": 2, "quotes.unverified": 0, "quotes.fabricated": 0, "rows.G2.status": "found"})
case("match-accepted-alternate", port_head + ap("Major", "AP-14", "Date as Target", "Payments", [E(*P12)]),
     {"rows.G1.status": "found", "rows.G1.matched_id": "AP-14", "rows.G1.id_exact": False, "extras": []})
case("match-same-id-two-locations", port_head + ap("Major", "AP-04", "KR Without Baseline", "Growth", [E(*G11)]) + "\n" + ap("Major", "AP-04", "KR Without Baseline", "Platform", [E(*PL13)]),
     {"rows.G2.status": "found", "rows.G7.status": "found", "extras": [], "duplicates": []})
case("match-cross-source-partial", port_head + ap("Major", "AP-06", "Sandbagged Target", "Platform", [E(*PL11)]),
     {"rows.G5.status": "partial", "rows.G5.partials": {"contains": ["section Appendix"]}, "extras": ["AP-06@KR PL1.1"]})
case("match-cross-source-found", port_head + ap("Major", "AP-06", "Sandbagged Target", "Platform", [E(*PL11), E(*APX, label="Evidence (trailing actual)")]),
     {"rows.G5.status": "found", "extras": []})
case("non-defect-violation", port_head + ap("Major", "AP-01", "Task Masquerading as KR", "Data", [E(*D21)]),
     {"violations.non_defect": 1, "extras": ["AP-01@KR D2.1"], "budget.counted": 1})
case("off-key", port_head + ap("Major", "AP-10", "BAU Dressed as OKR", "Platform", [E(*PL1)]),
     {"violations.off_key": 1, "extras": ["AP-10@Objective PL1"]})

case("quote-term-absent-label", port_head + ap("Minor", "AP-08", "Committed vs Aspirational Not Labeled", "Growth",
     ["- Evidence: the page never uses \"stretch\" or \"must-hit\" ({} › Growth team › line 34)".format(P)]),
     {"quotes.term": 2, "quotes.fabricated": 0, "quotes.key_leak": 0, "failures": {"contains": ["missed row G1"]}})
case("quote-repeated-line-located-by-ref", port_head + ap("Major", "AP-08", "Committed vs Aspirational Not Labeled", "Platform",
     [E("Commitment: KRs are committed unless marked (aspirational).", "Platform team — Q3 2026", 54)]),
     {"quotes.verbatim": 1, "quotes.ambiguous": 0, "extras": ["AP-08@Platform team"], "violations.non_defect": 1})
case("quote-repeated-line-no-ref-match", port_head + ap("Major", "AP-08", "Committed vs Aspirational Not Labeled", "Platform",
     [E("Commitment: KRs are committed unless marked (aspirational).", "Platform team — Q3 2026", 999)]),
     {"quotes.verbatim": 1, "quotes.ambiguous": 1, "extras": ["AP-08@unlocated"], "structure.warnings": {"contains": ["not anchored"]}})

case("secondary-folded-g7-credited", port_head + ap("Major", "AP-12", "Orphan KR", "Platform", [E(*PL13)], also="AP-04 KR Without Baseline"),
     {"rows.G7.status": "found", "rows.G7.matched_id": "AP-04", "rows.G7.id_exact": False, "duplicates": [], "extras": []})
case("secondary-without-anchor", port_head + ap("Major", "AP-12", "Orphan KR", "Platform", [E(*PL1)], also="AP-04 KR Without Baseline"),
     {"rows.G7.status": "partial", "extras": ["AP-12@Objective PL1"]})
case("secondary-prose-mention-no-credit", port_head + ap("Major", "AP-12", "Orphan KR", "Platform", [E(*PL13)], why="the KR also lacks a baseline, so AP-04 applies as well"),
     {"rows.G7.status": "missed", "extras": ["AP-12@KR PL1.3"]})
case("no-findings", "# Report\n\n## 1. Executive summary\n\nNothing found.\n",
     {"findings_parsed": 0, "pass": False, "structure.failures": {"contains": ["no findings parsed"]}})

def st_report(findings_md, al_block=""):
    return ("# Platform — Q3 2026 single-team OKR review\n\n## 1. Verdict summary\n**Verdict: Needs rework.** Roll-up C (2.4); 0 Critical, 3 Major, 0 Minor. "
            "Company-level strategy tracing was out of scope: no strategy document was provided.\n\n## 2. Score table\n"
            "| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
            "| Platform | 2 | 2 | 3 | N/A | 2 | 2 | 1 | 3 | 2 | 2 | 2 |\n\nO4 N/A — no strategy source in scope (rubric gap note).\n\n## 3. Findings\n\n"
            + findings_md + al_block + "\n## 4. Outbound dependency notes\n- \"Holding all non-critical infra requests until Q4.\" (input.md › Objective PL2: Earn enterprise trust › line 16) — unverified — counterparty not in scope\n\n## 5. Prioritized action list\n1. Rewrite PL1.1 against the trailing actual — owner: Platform lead (resolves §3 AP-06 Sandbagged Target).\n")
def SE(q, heading, line, label="Evidence"):
    return E(q, heading, line, label=label, path="input.md")
sPL22 = ("Complete the SOC 2 Type II audit.", "Objective PL2: Earn enterprise trust", 14)
sPL11 = ("Maintain API uptime at or above 99.9%.", "Objective PL1: Keep the lights on, cheaper", 8)
sAPX = ("API uptime, trailing 90 days: 99.95% (Datadog SLO monitor).", "Appendix — Q2 2026 business review (extracts)", 21)
sPL13 = ("Improve internal developer satisfaction score to 8/10.", "Objective PL1: Keep the lights on, cheaper", 10)
sPL1 = ("Keep the lights on, cheaper", "Objective PL1: Keep the lights on, cheaper", 7)
three = (ap("Major", "AP-02", "Binary KR with No Gradient", "Platform", [SE(*sPL22)]) + "\n" +
         ap("Major", "AP-06", "Sandbagged Target", "Platform", [SE(*sPL11), SE(*sAPX, label="Evidence (trailing actual)")]) + "\n" +
         ap("Major", "AP-04", "KR Without Baseline", "Platform", [SE(*sPL13)]) + "\n")
case("single-team-compliant", st_report(three),
     {"pass": True, "structure.pass": True, "rows.G4.status": "found", "rows.G5.status": "found", "rows.G7.status": "found", "budget.counted": 0, "extras": [], "duplicates": []}, slice="platform-single-team")
case("dup-three-ids-one-kr", st_report(three + ap("Critical", "AP-09", "Metric Nobody Can Measure", "Platform", [SE(*sPL13)]) + "\n" + ap("Major", "AP-12", "Orphan KR", "Platform", [SE(*sPL13)]) + "\n"),
     {"rows.G7.status": "found", "rows.G7.matched_id": "AP-04", "duplicates": ["AP-09@KR PL1.3", "AP-12@KR PL1.3"], "extras": [], "budget.counted": 2, "pass": False, "failures": {"contains": ["budget exceeded: 2 counted findings > 1"]}}, slice="platform-single-team")
case("budget-exceeded", st_report(three + ap("Major", "AP-10", "BAU Dressed as OKR", "Platform", [SE(*sPL1)]) + "\n" + ap("Major", "AP-01", "Task Masquerading as KR", "Platform", [SE(*sPL22)]) + "\n"),
     {"budget.counted": 2, "budget.limit": 1, "pass": False, "failures": {"contains": ["budget exceeded"]}}, slice="platform-single-team")
case("structure-single-team-al-block", st_report(three, al_block="### [Critical] AL-07 Resource contention: Payments ↔ Platform\n- Platform evidence: \"Q3 is fully committed between SOC 2 evidence collection and the cost work.\" (input.md › Objective PL2 › line 16)\n- Payments evidence: \"assuming Platform provisions this in July\" (input.md › Payments › line 1)\n- Verdict: PLAUSIBLE\n"),
     {"pass": False, "structure.pass": False, "structure.failures": {"contains": ["AL block in single-team report"]}, "failures": {"contains": ["AL block in single-team"]}}, slice="platform-single-team")
k = json.loads((ROOT / "evals/grader/selftest/keys/sample-portfolio.json").read_text(encoding="utf-8"))
k["triage"] = [{"id": "T1", "finding": "AP-10", "anchor": {"item": "Objective PL1"}, "bucket": "fixture-ambiguous", "decision": "tolerate until the objective wording is disambiguated", "rationale": "self-test entry", "status": "known-red"}]
case("known-red-exclusion", st_report(three + ap("Major", "AP-10", "BAU Dressed as OKR", "Platform", [SE(*sPL1)]) + "\n"),
     {"excluded": ["AP-10@Objective PL1"], "extras": [], "budget.counted": 0, "budget.excluded": 1, "pass": True}, slice="platform-single-team",
     extra_files={"key-with-triage.json": json.dumps(k, indent=1, ensure_ascii=False)})
heat = ("# Portfolio review\n\n## 1. Executive summary\nVerdict: At risk.\n\n## 2. Portfolio heatmap\n"
        "| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| Growth | 2 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | 2 | 2 | 3 | 1 |\n\n"
        "## 3. Per-team goodness findings\n\n" + ap("Major", "AP-04", "KR Without Baseline", "Growth", [E(*G11)]) +
        "\n## 4. Alignment findings\n\nNone.\n\n## 5. Prioritized action list\n1. x\n\n## 6. Suggested single-team re-runs\nNone qualifies.\n")
case("structure-heatmap-12-columns", heat, {"structure.pass": False, "structure.failures": {"contains": ["extra column(s) K8"]}, "rows.G2.status": "found"})
kc = json.loads((ROOT / "evals/grader/selftest/keys/sample-portfolio.json").read_text(encoding="utf-8"))
kc["defects"][0]["evidence"] = [{"item": "KR NONEXISTENT.99"}]
d = CASES / "check-corrupted-key"; d.mkdir(exist_ok=True)
(d / "corrupted-key.json").write_text(json.dumps(kc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
(d / "case.json").write_text(json.dumps({"type": "check", "key": "corrupted-key.json", "expect_mentions": ["G1", "KR NONEXISTENT.99"]}, indent=2) + "\n", encoding="utf-8")
S = Path("/private/tmp/claude-502/-Users-difan-Archive-A-02-Cursor-OKR-Reviewer--claude-worktrees-loving-hypatia-0d8d0c/7e150d6b-7f47-4a2d-a191-156c5f91b4aa/scratchpad/evalcheck")
case("recovered-mini1", (S / "mini1.md").read_text(encoding="utf-8"), {"rows.G2.status": "found", "rows.G7.status": "found", "extras": ["AP-07@KR P2.1"], "violations.non_defect": 1, "budget.counted": 1})
case("recovered-mini2", (ROOT / "evals/scratch/manual-check/mini2.md").read_text(encoding="utf-8"), {"rows.G1.status": "found", "rows.G1.matched_id": "AP-14", "duplicates": ["AP-01@KR P1.2"], "extras": [], "budget.counted": 1})
sys.path.insert(0, str(ROOT / "evals/grader")); import harness as h
scratch = [("fixture1-portfolio", "sample-portfolio.json", None, "sample-portfolio.md"), ("fixture2-portfolio", "sample-portfolio-2.json", None, "sample-portfolio-2.md"), ("fixture1-platform-single-team", "sample-portfolio.json", "platform-single-team", "sample-portfolio.md")]
for dname, kf, sl, inp in scratch:
    for r in (1, 2, 3):
        name = "scratch-%s-run-%d" % (dname.replace("fixture1-platform-single-team", "platform"), r)
        d = CASES / name; d.mkdir(exist_ok=True)
        rep = (ROOT / "evals/scratch" / dname / ("run-%d" % r) / "report.md").read_text(encoding="utf-8")
        rep = rep.replace(str(ROOT / "evals/scratch" / dname / "input" / inp), "input.md").replace("evals/scratch/%s/input/%s" % (dname, inp), "input.md").replace("`%s`" % inp, "`input.md`")
        (d / "report.md").write_text(rep, encoding="utf-8")
        shutil.copy(ROOT / "evals/scratch" / dname / "input" / inp, d / "input.md")
        key = json.loads((ROOT / "evals/grader/selftest/keys" / kf).read_text(encoding="utf-8")); key["_path"] = str(ROOT / "evals/grader/selftest/keys" / kf)
        spec = key["slices"][sl] if sl else None
        fx = h.Fixture(ROOT / key["fixture"])
        g = h.grade_report(rep, key, spec, (d / "input.md").read_text(encoding="utf-8").split("\n"), fx, {})
        exp = {"pass": g["pass"], "budget.counted": g["budget"]["counted"], "quotes.fabricated": 0, "structure.pass": g["structure"]["pass"], "extras": g["extras"], "duplicates": g["duplicates"]}
        for rid, v in g["rows"].items(): exp["rows.%s.status" % rid] = v["status"]
        (d / "case.json").write_text(json.dumps({"key": kf, "slice": sl, "report": "report.md", "input": "input.md", "expected": exp}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("%-28s pass=%-5s counted=%d extras=%s dups=%s missed=%s" % (name, g["pass"], g["budget"]["counted"], g["extras"], g["duplicates"], [k2 for k2, v in g["rows"].items() if v["status"] != "found"]))
print("cases:", len(list(CASES.glob("*/case.json"))))
