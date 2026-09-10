# goodness-findings (delta)

## ADDED Requirements

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
