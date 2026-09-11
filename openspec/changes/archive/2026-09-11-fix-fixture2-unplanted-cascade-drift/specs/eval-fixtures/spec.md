# eval-fixtures (delta)

## MODIFIED Requirements

### Requirement: A fixture plants no defect its key does not declare

Every objective and key result in a fixture SHALL be accounted for by that fixture's key: either it is evidence for a planted-defect row, or it is listed as an intentional non-defect, or the catalog does not fire on it. An instance the catalog genuinely fires on that appears in neither list is a **fixture defect**, not an evaluator error: it taxes the extras budget on every run that catches it, and it punishes the correct behavior the rubric asks for.

An unplanted true defect SHALL be resolved by changing the fixture text so the instance is clean, or by adding the key row it deserves — never by raising a budget, and never by adding an intentional non-defect that forbids a finding the rubric would correctly produce.

Where the same instance is caught in only some runs, planting it as a key row SHALL be rejected in favor of correcting the fixture text: a row the skill finds intermittently converts a precision failure into a recall failure without improving the skill.

Where the unplanted instance arises from a **link between two fixture pages** — a child objective's declared parent and the parent's own text — the fixture text to correct SHALL be chosen by which side is free, not by which side the finding names. When the child's page is load-bearing evidence for a different key row, the repair SHALL land on the parent's page instead, and the child's page SHALL be left unchanged. Removing an unplanted defect at the cost of a planted one is not a resolution, and neither is declaring the instance unfixable while an unexamined side of the link remains: each rejected lever SHALL be recorded with the row it would have cost.

Where a fixture correction makes a previously defensible finding wrong while the instance remains a plausible near-miss, the key SHALL gain an intentional non-defect forbidding that finding at that instance, so that a later edit undoing the correction surfaces as a named violation rather than as an anonymous extra.

#### Scenario: Unplanted true defect found in some runs

- **WHEN** a fixture KR states a target with no baseline, the key lists it neither as a planted defect nor as an intentional non-defect, and reports flag it in some but not all runs
- **THEN** the fixture text is corrected so the KR states its baseline, and the key gains a triage entry recording the disposition — the budget is not raised and no non-defect row is added to suppress the finding

#### Scenario: Fixture edit preserves dependent rows

- **WHEN** a fixture line is reworded and another answer-key row cites that line as evidence
- **THEN** the rewording preserves what that row depends on, the row's own note is updated wherever it quoted the replaced wording, and every evidence anchor still resolves under `harness.py check`

#### Scenario: Unplanted cross-page defect whose child page is load-bearing

- **WHEN** a child objective declares a parent link, its only KR measures something the parent's page names as no driver of the parent's metric, and that child page is load-bearing evidence for a different planted row that requires the page to state no mechanism
- **THEN** the repair lands on the parent's page — which gains the missing driver as a named contributing workstream, so the detection's own mechanism check passes on the documented-driver branch — and the child's page is left unedited, preserving the row that depends on it

#### Scenario: A lever is rejected without examining both sides of the link

- **WHEN** an unplanted cross-page defect is triaged and every rejected lever edits the child's side
- **THEN** the triage is incomplete: the parent's side is examined before the instance may be recorded as tolerated, and the disposition names which row each rejected lever would have cost

#### Scenario: Corrected fixture text gains a guard non-defect

- **WHEN** a fixture correction makes a finding that was previously defensible wrong, and the instance still reads as a near-miss a careless reviewer would flag
- **THEN** the key gains an intentional non-defect forbidding that finding at that instance — valid only because the corrected text now exhibits the property the rationale claims — alongside the triage entry recording the correction
