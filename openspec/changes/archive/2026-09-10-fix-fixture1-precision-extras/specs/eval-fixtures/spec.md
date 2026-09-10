# eval-fixtures (delta)

## ADDED Requirements

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
