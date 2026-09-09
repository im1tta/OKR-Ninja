## Purpose

Defines how the goodness review reports an objective or key result that exhibits more than one anti-pattern: one finding per instance under a root-cause ID, with every other applicable anti-pattern carried as a secondary ID inside that finding.

## ADDED Requirements

### Requirement: One finding per objective or KR instance

`references/goodness-rubric.md` Part 5 SHALL state that a goodness report files at most one finding block per objective or key-result instance. When more than one anti-pattern applies to the same instance, the finding SHALL be filed under the root-cause AP-ID chosen by the rubric's precedence rule and SHALL list every other applicable anti-pattern as a secondary ID in the block; a second block for the same instance is a reporting defect. The rule applies per instance only — two different KRs each get their own block. A **set-level** anti-pattern (one scoped to an objective set or team page rather than a single objective or KR — AP-05 Everything Is a P0 and AP-08 Committed vs Aspirational Not Labeled) SHALL be treated as its own instance: it gets its own finding block and SHALL NOT be folded into, or listed on the `Also:` line of, any member objective's or KR's block.

#### Scenario: KR with a missing baseline and no causal link to its objective

- **WHEN** a KR both states a target with no baseline (AP-04 KR Without Baseline) and would not move its stated objective (AP-12 Orphan KR)
- **THEN** the report contains one block for that KR, headed by the ID the precedence rule selects, whose `Also:` line names the other ID with its canonical name, and no second block for the KR

#### Scenario: Set-level defect beside a member KR's defect

- **WHEN** a team page states no commitment convention (AP-08 Committed vs Aspirational Not Labeled, a set-level defect) and one of its KRs is also an unmoored moonshot (AP-07)
- **THEN** the report contains two blocks — one for the set, quoting the set-level evidence, and one for the KR — and the KR's `Also:` line does not name AP-08

#### Scenario: Two distinct instances

- **WHEN** two different KRs each exhibit an anti-pattern
- **THEN** each KR has its own finding block; the rule never merges findings across instances

### Requirement: Root-cause precedence

The rubric SHALL define the precedence that selects the primary ID when several anti-patterns apply to one instance: measurability defects first (AP-09 Metric Nobody Can Measure, AP-13 Ambiguous Denominator), then structural defects (AP-01 Task Masquerading as KR, AP-02 Binary KR with No Gradient, AP-10 BAU Dressed as OKR, AP-11 Objective as Kitchen Sink, AP-12 Orphan KR, AP-14 Date as Target), then calibration and hygiene defects (AP-03 Vanity Metric, AP-04 KR Without Baseline, AP-05 Everything Is a P0, AP-06 Sandbagged Target, AP-07 Unmoored Moonshot, AP-08 Committed vs Aspirational Not Labeled, AP-15 Ownerless KR); within a tier, the lower-numbered ID leads.

#### Scenario: Measurability outranks calibration

- **WHEN** a KR names no measurable metric (AP-09) and also lacks a baseline (AP-04)
- **THEN** the block is headed AP-09 Metric Nobody Can Measure and lists AP-04 KR Without Baseline as secondary

### Requirement: The secondary-ID field of the goodness finding template

`references/report-format.md` §3 SHALL define an `Also:` line in the goodness finding template, placed after the evidence lines: omitted when no other anti-pattern applies to the instance, required otherwise, listing each secondary ID as "AP-XX <canonical name>" exactly as the rubric spells it, separated by " · ". The line carries no evidence of its own — the block's evidence lines already quote the instance — and the alignment finding template is unchanged.

#### Scenario: Folded finding

- **WHEN** a finding block folds AP-04 under AP-12 for one KR
- **THEN** its `Also:` line reads `AP-04 KR Without Baseline`, the block quotes the KR once with its source ref, and the "Why it's a problem" and "Suggested rewrite" lines address both anti-patterns

### Requirement: Worked example beside the rule

Per the repository's editing rule for rubric changes, the rubric SHALL carry a before/after example of the consolidation rule in the same file: a "before" showing two blocks on one KR and an "after" showing the single consolidated block with its `Also:` line, using fictional content only and placeholder-tagged numbers per the report-format convention.

#### Scenario: Example present

- **WHEN** a reader opens Part 5 after this change
- **THEN** they find the before/after example next to the rule, with no real company data and every invented number tagged as a proposal placeholder
