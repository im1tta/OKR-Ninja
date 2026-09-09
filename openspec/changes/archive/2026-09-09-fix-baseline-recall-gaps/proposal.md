## Why

The harness's first baseline batch (15 production-faithful runs of the unchanged skill, `evals/runs/2026-09-08-baseline-02f27be`) and the final smoke batch (`evals/runs/2026-09-09-smoke-02f27be`) measured two recall gaps and one reporting habit that together keep fixture 1 red on most runs, so the verify gate's smoke tier would block unrelated changes:

- **A1 (AL-02, Payments step-up verification vs Growth checkout conversion) is found in 2 of 5 runs.** The taxonomy's only AL-02 candidate stream blocks on metric identity; those KRs share no metric name, so most runs never compare them. The archived change `2026-09-01-strengthen-al02-mechanism-pair-generation` on the `claude/okr-ninja-improvements-1f147e` branch already fixed this with a second, surface-lever blocking key and was verified green on both fixtures, but it was never merged into `main`.
- **G7 (AP-04 on Platform KR PL1.3) was folded into an AP-12 block** in the smoke run, with the missing baseline noted as "co-occurring" inside the block. That is the one-finding-per-KR practice the harness Q&A asked for, but neither the rubric nor the finding template defines it, and the grader credits heading IDs only, so the fold reads as a miss. The same habit produced the recurring duplicate now excluded as triage entry T1.

Change 1 (`add-eval-harness`) left its final-verification task open on exactly these two causes; this change closes them and is the first content change the harness proves with a paired before/after scorecard.

## What Changes

- **Goodness rubric, Part 5:** a new evidence-discipline rule, *one finding per objective or KR instance* — file under the root-cause AP-ID chosen by a stated precedence (measurability, then structure, then calibration and hygiene), list every other applicable anti-pattern as a secondary ID in the finding's `Also:` line, and never open a second block for the same instance — with a matching before/after example in the same file.
- **Report format, §3:** the goodness finding template gains an optional `Also:` line (required whenever a second anti-pattern applies to the same instance) carrying secondary AP-IDs with canonical names; the evidence invariant, severity scale and AL template are unchanged.
- **Alignment taxonomy, AL-02:** port the archived surface-lever change verbatim — candidate generation as two named, always-run keys (metric identity and surface lever), per-candidate kills stated in the AL-02 entry and Step 4, Step 3's blocking-key list naming both keys, and the in-file Meridian example.
- **Harness:** the grader credits secondary IDs parsed from a finding's `Also:` line when matching key rows (the row's evidence anchors still have to be satisfied; `id_exact` stays true only for the primary ID); new self-test cases cover folded findings.
- **Keys:** fixture 1 row G7 accepts AP-09 Metric Nobody Can Measure as an alternate ID (either ID, counted once), because the KR names no instrument and the baseline runs split on the reading; triage entry T1 moves to `fixed` once the rule lands, so a repeated block on one KR counts again.
- **Verification:** a smoke batch on all three slices, then a decision batch against the 2026-09-08 baseline per the design's batch decision, with `compare` reporting no regression; change 1's open task 5.4 is closed by that green result.

**Detection behaviour changes.** Planted defects in `examples/sample-portfolio.md` this change should newly catch: **A1** (AL-02, expected to move from 2 of 5 toward 5 of 5 through surface-lever generation) and **G7** (AP-04, credited whenever it is folded under AP-12 or AP-09 with the baseline noted as secondary, instead of counting as missed). No other row's expected behaviour changes; intentional non-defect 4 (checkout success rate vs checkout conversion) must stay unreported, as the ported change's per-candidate-kill rule requires.

## Capabilities

### New Capabilities
- `goodness-findings`: one finding per objective or KR instance — root-cause precedence, the secondary-ID (`Also:`) field of the goodness finding template, and the rule that a folded anti-pattern is reported inside the primary block rather than as a second block.

### Modified Capabilities
- `alignment-detection`: AL-02 candidate generation runs a surface-lever key beside metric identity, generation is distinct from disconfirmation with per-candidate kills, and the entry carries an in-file example (ported requirements from the archived change).
- `eval-harness`: row matching credits secondary IDs from a finding's `Also:` line; the capability's main spec is created when `add-eval-harness` archives, so this delta adds requirements rather than modifying existing ones.

## Impact

- **Modified files:** `references/goodness-rubric.md` (Part 5 rule with example), `references/report-format.md` (§3 template and example), `references/alignment-taxonomy.md` (AL-02 entry, Part 2 Step 3 and Step 4), `evals/grader/harness.py` and `evals/grader/selftest/` (secondary-ID crediting, cases, frozen key snapshot), `evals/keys/sample-portfolio.json` and the regenerated answer-key section of `examples/sample-portfolio.md` (G7 alternate, T1 status).
- **Untouched:** `SKILL.md` (Step 3 already defers to the rubric's rules; stays under ~150 lines), AP-XX and AL-XX IDs and names, severities, `examples/sample-portfolio-2.md`.
- **Subscription quota:** 3 smoke runs plus the decision batch (15 or 30 runs per the design decision), each portfolio run about 200k tokens.
- **Downstream:** `add-eval-harness` task 5.4 closes on this change's green smoke; triage entry T1 is retired.

## Non-goals

- Rewriting the `references/report-format.md` worked examples into a third fictional universe (the fixture 1 leakage caveat stays a later change).
- A "known-missed" triage status for rows (the alternative to fixing the recall gaps, not chosen).
- Any other AL-XX blocking key, severity mapping, or evidence rule; any new anti-pattern or failure mode.
- Fixing extras that recur below the three-run threshold (AP-10 on Platform Objective PL1 appeared in 1 of 5 baseline runs).
- Routing tests, control or mini fixtures, a headless driver, or changes to the report's non-finding sections.
