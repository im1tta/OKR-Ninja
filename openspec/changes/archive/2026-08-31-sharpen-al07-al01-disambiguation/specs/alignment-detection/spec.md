## Purpose

Defines the classification behavior the alignment taxonomy (`references/alignment-taxonomy.md`) must produce when cross-team defects match multiple AL-XX failure modes — starting with the AL-01/AL-07 boundary.

## ADDED Requirements

### Requirement: Multiple claimants on a stated-capacity constraint aggregate into AL-07
When two or more teams' KRs claim work, capacity, or roadmap slots from the same resource-owning team, and that owner's own pages state a capacity constraint (including a statement that capacity is fully committed elsewhere), the taxonomy SHALL direct the reviewer to report a single AL-07 Resource contention finding aggregating all claimant edges against the owner's capacity statement — never per-edge AL-01 Unacknowledged dependency findings standing in for the contention (the "one finding, one failure mode" rule resolves the contention's root cause to AL-07, with AL-01 cross-referenced as secondary). The aggregate SHALL NOT swallow distinct missing-deliverable defects: an edge whose ask is the owner's capacity itself folds into the aggregate entirely, while an edge naming a distinct deliverable absent from the producer's plans still earns its own AL-01 finding for that absence, cross-referencing the AL-07; the capacity arithmetic itself is reported exactly once, under AL-07.

#### Scenario: Fixture defects A5 and A2 are both caught
- **WHEN** the skill audits `examples/sample-portfolio.md`, where Payments assumes Platform provisions PCI-scoped infra in July, Data assumes Platform runs the streaming pipeline migration, and Platform's notes state Q3 is "fully committed"
- **THEN** the alignment report contains one AL-07 Resource contention finding aggregating both claimants against Platform's capacity statement (answer-key row A5), no standalone AL-01 finding for the Payments↔Platform provisioning ask, and a separate AL-01 finding for Data's unacknowledged streaming pipeline migration (answer-key row A2)

#### Scenario: Single claimant remains AL-01
- **WHEN** exactly one team's KR depends on unacknowledged work from a resource owner and no other team claims that owner's capacity in the period
- **THEN** the edge is reported under AL-01 (or another matching mode) and the aggregation rule does not apply

### Requirement: The AL-07 aggregation rule carries a matching in-file example
The AL-07 entry in `references/alignment-taxonomy.md` SHALL include an example in the same file illustrating the aggregation/precedence rule — a scenario narrative in which per-edge AL-01 classification would miss the contention, plus the detection heuristic reading that catches it — using only the file's fictional Meridian teams.

#### Scenario: Example present and fictional
- **WHEN** a reader opens the AL-07 entry after this change
- **THEN** they find a worked example of multiple claimants on one owner's stated capacity being aggregated into AL-07 instead of per-edge AL-01, phrased with fictional Meridian teams and no real company data
