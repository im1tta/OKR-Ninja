# eval-fixtures

## Purpose

Defines what the repo's eval fixture set must provide: full-catalog planted-defect coverage across fixtures, per-fixture answer keys and false-positive controls, and fictional-universe independence so evals measure detection rather than recall.

## Requirements

### Requirement: Full-catalog defect coverage across the fixture set

Every anti-pattern (AP-XX) in `references/goodness-rubric.md` and every failure mode (AL-XX) in `references/alignment-taxonomy.md` SHALL have at least one planted defect in at least one fixture under `examples/`, so that no detection path is without eval coverage.

#### Scenario: Coverage after this change

- **WHEN** the planted-defect rows of all fixtures' answer keys are united
- **THEN** every ID AP-01–AP-15 and AL-01–AL-12 appears in at least one row (fixture 1 covers AP-01/02/03/04/06/09 + AP-14 as an accepted alternate and AL-01/02/03/04/06/07/10; fixture 2 covers AP-05/07/08/10/11/12/13/15 and AL-05/08/09/11/12)

#### Scenario: A catalog mode loses coverage

- **WHEN** a fixture edit removes the only planted defect for some catalog ID
- **THEN** the verify gate's structural checks fail the change, because the fixture set no longer satisfies full-catalog coverage

### Requirement: Per-fixture answer key and eval criterion

Each fixture SHALL have a canonical machine-readable answer key at `evals/keys/<fixture-basename>.json` that lists every planted defect with its accepted canonical IDs (primary ID first, spelled as the owning reference file spells them), its location expressed as grader-checkable evidence anchors (an item marker such as `KR PL1.2` or `Objective D1` that appears on exactly one fixture line, or a section heading prefix; anchors MAY be marked optional), and what is wrong; an intentional non-defects list of deliberate near-misses, each with the IDs it forbids and its location; a modes-deliberately-not-covered list naming every catalog ID the fixture does not plant; the extra-findings budget; the eval criterion; any eval slices with their input sections, expected rows, budget and mode-specific expectations; and any triage entries. The fixture file SHALL end with an `## Answer key` section that is generated from that JSON key, and the harness's zero-token checks SHALL fail when that section differs from the generator's output or when any evidence anchor fails to resolve to a fixture line or heading. The eval criterion SHALL require all planted defects found by canonical ID with verbatim quotes and source refs, zero fabricated quotes, and no more than the stated budget of findings beyond the key (2 for both fixtures), where findings covered by an active known-red triage entry are excluded from that count.

#### Scenario: Grading a review run against fixture 2

- **WHEN** a portfolio review of `examples/sample-portfolio-2.md` is graded against its answer key
- **THEN** the run passes only if all 13 planted defects are cited by canonical ID with quotes that exist character-for-character in the fixture, and at most 2 findings fall outside the key (reported intentional non-defects count against that budget)

#### Scenario: Off-key mode cited

- **WHEN** a graded review reports a finding citing an ID from the fixture's modes-deliberately-not-covered list
- **THEN** that finding counts against the fixture's extra-findings budget

#### Scenario: Generated key section is stale

- **WHEN** the JSON key changes and the fixture's `## Answer key` section is not regenerated
- **THEN** the harness's zero-token checks fail naming the fixture

#### Scenario: Evidence anchor does not resolve

- **WHEN** a key row names an item marker that appears on no line of the fixture, or on more than one
- **THEN** the harness's zero-token checks fail naming the row and the marker

### Requirement: Fixture 2 plants the thirteen previously uncovered modes

`examples/sample-portfolio-2.md` SHALL plant exactly one defect for each of AP-05, AP-07, AP-08, AP-10, AP-11, AP-12, AP-13, AP-15, AL-05, AL-08, AL-09, AL-11, AL-12, in a portfolio of at least three teams (the minimum for a multi-edge AL-11 dependency cycle), structured like fixture 1: company priorities, per-team OKR pages with source lines and notes, and an appendix of supporting extracts sufficient for every cross-source defect to be quotable from both sides.

#### Scenario: AL-11 cycle is quotable edge by edge

- **WHEN** the AL-11 Circular dependency defect is audited
- **THEN** each edge of the cycle is supported by a verbatim quotable blocking statement in a different team's page, and the cycle spans at least three teams

#### Scenario: Cross-source defects quotable from both sides

- **WHEN** a planted defect requires two-sided evidence (e.g. AL-09 Baseline disagreement, AL-12 Commitment asymmetry)
- **THEN** both sides' triggering text exists verbatim in the fixture, each attributable to its own source ref

### Requirement: Fictional-universe independence

Each fixture SHALL use an invented company, teams, and people that are clearly fictional and distinct from every other fixture's universe and from the worked-example universes used in `references/` (e.g. the taxonomy's Meridian/Atlas/Bluefin), so that an eval run cannot pattern-match scenarios already present in reference material or in another fixture.

#### Scenario: New fixture universe

- **WHEN** `examples/sample-portfolio-2.md` is authored
- **THEN** its company and team names appear nowhere in `references/` or in `examples/sample-portfolio.md`, and no real company or person is named

### Requirement: Fixture selection scoped to the touched category

The verify gate's fixture eval SHALL run against the fixture(s) whose answer keys cover the category touched by the change under review; a change touching modes covered only by fixture 2 must be evaluated against fixture 2.

#### Scenario: Change touches an AL mode only fixture 2 covers

- **WHEN** a change edits the detection heuristic of AL-11 Circular dependency
- **THEN** the verify gate's fixture eval runs against `examples/sample-portfolio-2.md` (the fixture whose key contains AL-11), not only against fixture 1

### Requirement: Fixture 1 defines a single-team-mode eval slice

`examples/sample-portfolio.md`'s answer key SHALL define a **single-team eval slice** giving single-team mode eval coverage without a new fixture file. The slice SHALL specify: the scoped team (**Platform**), the run's input scope (the "Platform team — Q3 2026" section plus the "Appendix — Q2 2026 business review (extracts)" section, no strategy/priorities page provided), the expected defects (**G4 · AP-02, G5 · AP-06, G7 · AP-04**, each cited by canonical ID with verbatim quotes and source refs — G5 quoting both the KR and the appendix per the cross-source rule), the requirement of **zero AL-XX findings** and **zero fabricated quotes**, the expectation that **O4 is scored N/A** per the rubric's no-strategy-source rule with its gap note recorded in the score section (not a findings-section entry, not counted against the budget), and an extra-findings budget of **1**. Content from other teams' sections is out of the slice's scope; a finding grounded in it counts against the budget.

#### Scenario: Grading a compliant single-team run

- **WHEN** single-team mode reviews Platform per the slice's input scope and the output is graded against the slice
- **THEN** the run passes only if it cites G4, G5, and G7 by canonical ID with quotes that exist character-for-character in the fixture, reports zero AL-XX findings, fabricates no quotes, scores O4 N/A with the rubric's gap note in the score section, and raises at most 1 finding beyond the three expected

#### Scenario: Cross-source defect must still be caught alone

- **WHEN** the graded run reports the Platform uptime KR without quoting the Q2 appendix's trailing actual (or vice versa)
- **THEN** G5 counts as missed, because AP-06's cross-source evidence rule applies in single-team mode unchanged

#### Scenario: Alignment finding in the slice

- **WHEN** the graded run reports any AL-XX finding (e.g. resource contention built on Platform's "fully committed" note)
- **THEN** the run fails the slice, because single-team mode must not produce cross-team alignment findings

### Requirement: Triage entries for recurring extras

A key SHALL be able to record triage entries for findings that recur beyond the key. Each entry SHALL name the finding's ID and evidence anchor, a bucket — `fixture-ambiguous`, `rubric-gap`, or `skill-error` — a decision, a rationale, and a status of `known-red` or `fixed`. A `known-red` entry SHALL exclude matching findings from the budget count while the grade and scorecard still report them with the entry's bucket; a `fixed` entry SHALL have no effect on counting. An entry without a rationale is invalid, and a `skill-error` entry SHALL NOT carry `known-red` status. The generated `## Answer key` section SHALL render triage entries beside the intentional non-defects.

#### Scenario: Known-red rubric gap tolerated until fixed

- **WHEN** the key holds a `known-red` entry with bucket `rubric-gap` for duplicate findings on Platform KR PL1.3 and a run reports PL1.3 under three IDs
- **THEN** the duplicates are reported in the grade with bucket `rubric-gap` and do not count toward the budget

#### Scenario: Skill error cannot be tolerated

- **WHEN** a triage entry with bucket `skill-error` is given `known-red` status
- **THEN** the key validation fails naming the entry

#### Scenario: Triage entry visible in the fixture

- **WHEN** the answer-key section is regenerated
- **THEN** every triage entry appears in it with its bucket, decision, rationale and status

### Requirement: Fixture-reference overlap caveat

A key row whose planted scenario also appears in a worked example under `references/` SHALL carry a reference-overlap flag with a pointer to the example, and the scorecard SHALL surface that flag as a caveat on the row's hit rate. While any such flag exists, `examples/sample-portfolio-2.md` SHALL be the primary fixture for headline quality claims; the regression rule applies to both fixtures unchanged.

#### Scenario: Fixture 1 rows overlapping report-format examples

- **WHEN** fixture 1's key is validated
- **THEN** every row whose defect text matches a `references/report-format.md` worked example (at least the Payments checkout API milestone, the Platform uptime sandbag, and the Payments-versus-Growth checkout conflict) carries the reference-overlap flag

#### Scenario: Caveat shown on the scorecard

- **WHEN** a scorecard is rendered for a fixture-1 slice
- **THEN** each flagged row shows the caveat next to its hit rate

### Requirement: A fixture plants no defect its key does not declare

Every objective and key result in a fixture SHALL be accounted for by that fixture's key: either it is evidence for a planted-defect row, or it is listed as an intentional non-defect, or the catalog does not fire on it. An instance the catalog genuinely fires on that appears in neither list is a **fixture defect**, not an evaluator error: it taxes the extras budget on every run that catches it, and it punishes the correct behavior the rubric asks for.

An unplanted true defect SHALL be resolved by changing the fixture text so the instance is clean, or by adding the key row it deserves — never by raising a budget, and never by adding an intentional non-defect that forbids a finding the rubric would correctly produce.

Where the same instance is caught in only some runs, planting it as a key row SHALL be rejected in favor of correcting the fixture text: a row the skill finds intermittently converts a precision failure into a recall failure without improving the skill.

#### Scenario: Unplanted true defect found in some runs

- **WHEN** a fixture KR states a target with no baseline, the key lists it neither as a planted defect nor as an intentional non-defect, and reports flag it in some but not all runs
- **THEN** the fixture text is corrected so the KR states its baseline, and the key gains a triage entry recording the disposition — the budget is not raised and no non-defect row is added to suppress the finding

#### Scenario: Fixture edit preserves dependent rows

- **WHEN** a fixture line is reworded and another answer-key row cites that line as evidence
- **THEN** the rewording preserves what that row depends on, the row's own note is updated wherever it quoted the replaced wording, and every evidence anchor still resolves under `harness.py check`

### Requirement: An intentional non-defect demonstrates the property its rationale claims

Each intentional non-defect in a key SHALL be a near-miss a correct reviewer genuinely should not flag: the fixture text it points at must exhibit the property the rationale asserts. A non-defect whose rationale claims a property the text does not have is a **key defect** — it marks correct detections as violations and drives the measured false-positive rate away from the truth.

When reports repeatedly violate a non-defect with sound reasoning, the disposition SHALL be to establish which of the two is wrong before any fix lands: if the rationale is unsupported by the text, the fixture text or the rationale is corrected; only if the reports are wrong does the fix belong in the rubric.

#### Scenario: Non-defect whose text does not support its rationale

- **WHEN** a non-defect claims a KR states an adoption measure, but the KR's measure is a rollout percentage the delivering team satisfies by shipping, and reports flag it with that reasoning
- **THEN** the non-defect is treated as the defect: the fixture KR is reworded so its measure is one the delivering team does not satisfy by shipping, the non-defect's rationale is rewritten against the new text, and the near-miss character — a delivery verb still present in the KR — is preserved so the row keeps measuring false positives

#### Scenario: A confirmed false positive becomes a non-defect

- **WHEN** triage establishes that a recurring extra is a false positive the rubric should never have produced, and the rubric anchor is corrected
- **THEN** the key gains an intentional non-defect forbidding that finding at that instance, so a regression in the anchor is caught as a violation rather than absorbed by the budget

#### Scenario: Each disposition is recorded

- **WHEN** a recurring extra is resolved by any of these routes
- **THEN** the key carries a triage entry naming its bucket, the decision taken, the rationale, and a status — and an entry whose fix has landed is recorded as such rather than left tolerated
