# Proposal — strengthen-al02-mechanism-pair-generation

## Why

The absorb-single-team-mode verify gate (2026-09-01) ran two independent fresh portfolio evals against `examples/sample-portfolio.md`; each found 13/14 planted defects, both missing exactly **A1** — the AL-02 Conflicting metrics / adversarial incentives pair between Payments KR P2.2 ("Increase step-up verification coverage to 90% of transactions") and Growth KR G2.1 (checkout conversion 58% → 68%), where the verification-friction mechanism suppresses conversion. Both runs' method notes show the same root cause: AL-02 candidate generation ran only on the heuristic's clause (1) (same canonical metric, opposing direction); the mechanism-pair clause (2) never generated candidates, because Part 2 Step 3 lists only "same canonical metric" as AL-02's blocking key, so clause (2) exists as a definition with no generation step that produces its pairs. An aggravating factor compounds the miss: correctly disconfirming the lookalike-metric pair P1.1 ↔ G2.1 (the fixture's intentional non-defect #4 — different metrics and populations) reads to eval runs as license to dismiss checkout-metric pairs wholesale, suppressing the true mechanism-level pair on the same surface.

## What Changes

- Rewrite the **AL-02 Detection heuristic** in `references/alignment-taxonomy.md` to define **two independent, always-run blocking keys** for candidate generation — (1) the existing metric-identity key, and (2) an explicit **surface-lever key**: two KRs share a funnel stage / surface / population and one KR's stated lever is a friction, quality, risk, or cost control on that surface while the other targets that surface's throughput/conversion/volume metric — and to state that candidate generation is a mechanical step distinct from disconfirmation (generate first from both keys; judge each candidate individually afterward).
- Make explicit that **disconfirmation kills candidates one at a time, never a surface**: killing a metric-identity or lookalike-metric candidate on a surface does not suppress surface-lever candidates on that same surface.
- Add a **matching in-file example** (fictional Meridian universe, per CLAUDE.md's taxonomy-change rule) — a scenario narrative of a mechanism-level pair that metric-identity blocking would miss, plus the heuristic reading that catches it, including the near-miss trap (a lookalike-metric pair correctly killed without taking the mechanism pair down with it).
- Update **Part 2 Step 3's blocking-key list** so AL-02 blocks on both keys (AL-09 remains metric-identity-only) — the procedure step and the entry must name the same keys, or runs will keep following the narrower one.
- Update **Part 2 Step 4's AL-02 disconfirming check** ("Shared metric ≠ conflict") to carry the per-candidate-kill rule.

## Capabilities

### New Capabilities

(none)

### Modified Capabilities

- `alignment-detection`: adds requirements that AL-02 candidate generation runs the surface-lever blocking key in addition to metric identity, that generation is separate from (and never suppressed by) disconfirmation, and that the AL-02 entry carries a matching in-file example of a mechanism-level pair invisible to metric-identity blocking.

## Impact

- **Files:** `references/alignment-taxonomy.md` only (AL-02 entry + Part 2 Steps 3 and 4). It is the sole owning file for AL-XX failure modes and detection heuristics, so no other file needs edits.
- **Not touched:** `SKILL.md` (its Step 4 already defers to "the taxonomy's blocking keys" generically), `references/report-format.md`, `references/goodness-rubric.md`, both fixtures (defect A1 is already planted and on fixture 1's answer key; no key rows, counts, budgets, or non-defect lists change).
- **Planted defects this change should newly catch:** **A1** (AL-02 · Payments KR P2.2 ↔ Growth KR G2.1) in `examples/sample-portfolio.md`. It must do so without regressing the other 13 planted defects and without causing intentional non-defect #4 (P1.1 ↔ G2.1) to be reported.

## Non-goals

- No new AL-XX failure modes and no renumbering/renaming — IDs and canonical names are frozen; this amends AL-02's detection procedure only.
- No changes to severity definitions (they live in `references/report-format.md` and are referenced by name only), to the evidence-discipline rules in Part 3, or to the report templates.
- No changes to AL-03/AL-08/AL-09 blocking keys or to any other failure mode's heuristic.
- No fixture or answer-key edits, and no SKILL.md edits.
