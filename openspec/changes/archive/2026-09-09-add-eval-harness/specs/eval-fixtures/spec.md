## MODIFIED Requirements

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

## ADDED Requirements

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
