# Proposal: add-second-eval-fixture

## Why

Only 7 of 15 goodness anti-patterns and 5 of 12 alignment failure modes have a planted defect in `examples/sample-portfolio.md` — the fixture's own "Modes deliberately not covered" section lists 13 catalog modes with no eval anywhere (AP-05, AP-07, AP-08, AP-10, AP-11, AP-12, AP-13, AP-15; AL-05, AL-08, AL-09, AL-11, AL-12). A regression in any of those detection paths would merge silently, because both the OPSX verify gate and the manual pre-merge test grade only against fixture 1.

## What Changes

- **New fixture `examples/sample-portfolio-2.md`**: a fresh fictional company (distinct from fixture 1's Brightledger and from Meridian, the taxonomy's worked-example universe, to prevent answer leakage), ~5–6 teams (at least 3 required for an AL-11 dependency cycle), planting **all 13 currently-uncovered catalog modes, one defect each**. Mirrors fixture 1's structure exactly: company priorities + team OKR pages + appendix extracts, then `## Answer key (planted defects)`, `### Intentional non-defects`, `### Modes deliberately not covered`, and `### Eval criterion` with an extra-findings budget of 2.
- **Doc updates naming both fixtures**:
  - `CLAUDE.md` — file map row for `examples/` and the "Testing changes" steps reference both fixtures (grade against the fixture(s) covering the touched modes).
  - `README.md` — repository layout includes the new file; roadmap's "More fixtures" item updated to reflect partial delivery (coverage closed; larger 8–12-team portfolios remain future work).
  - `.claude/skills/openspec-loop/phases/verify-gate.md` — fixture-eval wording generalizes from "the fixture" to running the fixture(s) whose answer keys cover the touched category.
- No changes to fixture 1, its answer key, or its budget.

### Newly evaluated defects

This change does not alter detection behavior; it adds eval coverage. After it lands, these modes gain their first planted defect (in fixture 2): AP-05 Everything Is a P0, AP-07 Unmoored Moonshot, AP-08 Committed vs Aspirational Not Labeled, AP-10 BAU Dressed as OKR, AP-11 Objective as Kitchen Sink, AP-12 Orphan KR, AP-13 Ambiguous Denominator, AP-15 Ownerless KR, AL-05 Cascade drift, AL-08 Terminology collision, AL-09 Baseline disagreement, AL-11 Circular dependency, AL-12 Commitment asymmetry.

## Capabilities

### New Capabilities

- `eval-fixtures`: what the repo's eval fixture set must provide — full-catalog defect coverage across fixtures, per-fixture answer keys with canonical IDs, deliberate near-miss non-defects, a stated extra-findings budget, and fictional-universe independence (no leakage from reference-file examples).

### Modified Capabilities

<!-- none — no existing specs in openspec/specs/ -->

## Non-goals

- No CI eval harness (running the fixtures stays manual / verify-gate-driven).
- No historical drift tracking, no JSON/machine-readable report output.
- No edits to `references/` (rubric, taxonomy, report format), `SKILL.md`, or the skill `description` — no new AP/AL IDs, no routing impact.
- No changes to `examples/sample-portfolio.md` (fixture 1 stays byte-identical).
- No 8–12-team scale fixture (remains on the README roadmap).

## Impact

- **New file:** `examples/sample-portfolio-2.md`.
- **Edited docs:** `CLAUDE.md`, `README.md`, `.claude/skills/openspec-loop/phases/verify-gate.md`.
- **Untouched:** `SKILL.md`, all of `references/`, `examples/sample-portfolio.md`.
- **Risk:** dense planting can accidentally create unplanned defects that burn the eval budget — each team page must be authored against the *full* catalog, with near-misses made deliberate and listed under Intentional non-defects.
