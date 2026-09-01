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

Each fixture SHALL end with an answer key that lists every planted defect with its canonical ID and name (as spelled by the owning reference file), its location, and what is wrong; an intentional non-defects list of deliberate near-misses that must not be reported; a modes-deliberately-not-covered list naming every catalog ID the fixture does not plant; and an eval criterion requiring all planted defects found by canonical ID with verbatim quotes and source refs, zero fabricated quotes, and no more than a stated budget of findings beyond the key (2 for both fixtures).

#### Scenario: Grading a review run against fixture 2

- **WHEN** a portfolio review of `examples/sample-portfolio-2.md` is graded against its answer key
- **THEN** the run passes only if all 13 planted defects are cited by canonical ID with quotes that exist character-for-character in the fixture, and at most 2 findings fall outside the key (reported intentional non-defects count against that budget)

#### Scenario: Off-key mode cited

- **WHEN** a graded review reports a finding citing an ID from the fixture's modes-deliberately-not-covered list
- **THEN** that finding counts against the fixture's extra-findings budget

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
