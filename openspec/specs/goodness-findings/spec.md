# goodness-findings Specification

## Purpose
Defines how the goodness review reports an objective or key result that exhibits more than one anti-pattern: one finding per instance under a root-cause ID, with every other applicable anti-pattern carried as a secondary ID inside that finding.

## Requirements

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

### Requirement: AP-10 is decided on the objective's own statement

`references/goodness-rubric.md`'s AP-10 · BAU Dressed as OKR detect rule SHALL be decidable from the objective statement alone. AP-10 fires when the objective asserts continuation of the team's standing job **and** either (a) it names no change at all — no direction, reduction, improvement, or other end-state differing from today — or (b) it names such a change and **no** key result realizes it with a baseline→target pair. AP-10 SHALL NOT fire when the objective names a change and at least one key result realizes it with such a pair, however operational the rest of the objective's wording sounds.

The rule SHALL NOT be stated as a property of the key-result set. Whether the KRs beneath an objective carry deltas is not the test: a standing-duty objective whose KRs happen to carry deltas is still AP-10, because the objective — the thing the anti-pattern is about — still commits the team to no change.

#### Scenario: BAU-sounding objective that names a change

- **WHEN** an objective reads "Keep the lights on, cheaper" and one of its KRs states a cost reduction with a baseline→target pair ("Reduce cloud spend per 1,000 transactions from $4.10 to $3.20")
- **THEN** AP-10 does not fire on that objective, and the report contains no AP-10 finding for it — the objective names a change ("cheaper") and a KR realizes it
- **AND** other anti-patterns on that objective's KRs are unaffected and still reported on their own instances

#### Scenario: Standing-duty objective whose KRs carry deltas

- **WHEN** an objective reads "Continue running the platform smoothly for every team" and its KRs state real deltas ("Sev-1 incidents per quarter 9 → ≤ 4", "Cloud cost per completed delivery $0.42 → $0.30")
- **THEN** AP-10 still fires on that objective — the objective statement names no change, and the deltas in its KRs do not rescue it

#### Scenario: A named change that no KR realizes

- **WHEN** an objective asserts continuation and names a change, but no key result realizes that change with a baseline→target pair
- **THEN** AP-10 fires on that objective — naming a change does not rescue it unless a KR pays for the change
- **AND** the finding quotes the objective's named change and the key result offered as the unpaid-for change, or enumerates the objective's key results as the search the rubric's absence-claim rule requires; the key-result half of the test is never asserted narratively

#### Scenario: AP-10 is never carried on a key result's secondary-ID line

- **WHEN** a reviewer notices an objective's operational framing while writing a finding about one of its key results
- **THEN** AP-10 is not appended to that key result's `Also:` line — its instance is the objective statement, so it heads or joins the objective's own block, where the objective statement is quoted

#### Scenario: Two readers, one verdict

- **WHEN** two independent reviewers apply the AP-10 detect rule to the same BAU-worded objective
- **THEN** the rule's text is sufficient for both to reach the same verdict without appeal to taste, because the test names what must be present in the objective statement and what must be present in one KR

#### Scenario: Worked example beside the rule

- **WHEN** a reader opens the AP-10 entry after this change
- **THEN** they find a before/after example in the same file showing an objective that fires and the concretely rewritten form that does not — actual replacement text, fictional content, every invented number tagged as a proposal placeholder

### Requirement: AP-01 rescue clause for delivery-verb key results

`references/goodness-rubric.md`'s AP-01 · Task Masquerading as KR entry SHALL state what rescues a KR that matches its delivery-verb trigger. The KR is not AP-01 when it carries **either**:

1. a **result measure someone outside the delivering team moves** — an adoption count, a usage or error rate, a quality measure — whether or not it states a baseline; or
2. a **baseline→target pair**, including a coverage figure that moves from a stated starting point over a countable denominator, which is progress-measurable across the period.

A delivery-verb KR SHALL fire only when it carries **neither**: a bare completion target with no starting point and no outside-moved measure restates the delivery instead of measuring a result.

The clause SHALL be an exclusion only. AP-01's trigger — the delivery-verb list — SHALL be unchanged, so no key result that the rule leaves silent today begins firing.

A missing baseline on a KR rescued by (1) SHALL NOT bear on AP-01; it is AP-04 · KR Without Baseline, filed under the precedence rule already in Part 5.

A finding filed under AP-01 SHALL quote the key result in full as extracted, not the delivery clause alone: the exclusion turns on the remainder of the sentence, so a clipped quote can satisfy every evidence check while making a rescued key result look like a firing one.

#### Scenario: Bare completion target fires

- **WHEN** a KR reads "Ship personalized onboarding checklists to 100% of new signups" — a completion percentage with no starting point and no measure anyone outside the team moves
- **THEN** AP-01 fires: "100%" measures the rollout, which the team completes by shipping

#### Scenario: Coverage with a stated starting point does not fire

- **WHEN** a KR reads "Billing-system migration covering 38% → 100% of the 6,400 self-serve accounts (migration tracker)" or "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14)"
- **THEN** AP-01 does not fire: the KR is progress-measurable all quarter, which is what the trigger's "no baseline→target pair" clause asks about
- **AND** the rule SHALL NOT be stated as "a coverage percentage of the team's own delivery never rescues" — that phrasing contradicts the eval corpus, which records the first of these as an intentional non-defect

#### Scenario: An outside-moved measure rescues without a baseline

- **WHEN** a KR names a delivery and also states a measure someone outside the team moves — a count of customers who upgraded through a newly launched flow — and states no baseline for it
- **THEN** AP-01 does not fire, and the missing baseline is reported as AP-04 · KR Without Baseline under the existing precedence rule

#### Scenario: The trigger list is unchanged

- **WHEN** a KR uses a completion verb outside AP-01's stated trigger list — for example "Close 100% of pen-test findings rated High or above (currently 7 open)"
- **THEN** the rescue clause does not cause AP-01 to fire on it; the clause narrows AP-01 and never widens it

#### Scenario: Checked against both fixtures' non-defects

- **WHEN** the rescue clause is written or revised
- **THEN** it is checked against the intentional non-defects of **every** fixture, not only the one whose extras motivated it — a clause that resolves one fixture's ambiguity while contradicting another fixture's recorded non-defect is a regression, and the eval measures it as one

#### Scenario: Worked example beside the rule

- **WHEN** a reader opens the AP-01 entry after this change
- **THEN** they find a before/after example in the same file contrasting a bare completion target that fires with its concretely rewritten outcome form, and naming the progress-measurable coverage form that does not fire — actual replacement text, fictional content, placeholder-tagged numbers
