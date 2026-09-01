# eval-fixtures Specification (delta)

## ADDED Requirements

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
