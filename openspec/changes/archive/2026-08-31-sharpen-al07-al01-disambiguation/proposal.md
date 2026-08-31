## Why

A fixture eval against `examples/sample-portfolio.md` found 13/14 planted defects; the miss was A5 (AL-07 Resource contention). The evaluator detected the underlying facts — Payments and Data both booking Platform capacity that Platform's OKRs declare "fully committed" — but reported the Payments↔Platform edge as AL-01 Unacknowledged dependency, applying the "one finding, one failure mode" rule (Part 3 §5 of `references/alignment-taxonomy.md`) in the wrong direction. The taxonomy currently gives no precedence rule between per-edge AL-01 and aggregate AL-07, so an evaluator that processes edges individually never assembles the contention finding.

## What Changes

- Extend AL-07's detection heuristic in `references/alignment-taxonomy.md` with an explicit aggregation/precedence rule: when two or more claimant edges land on one resource owner whose pages state a capacity constraint, the contention aggregates into a single AL-07 finding — never per-edge AL-01 findings standing in for it (AL-01 cross-referenced as secondary per the one-finding-one-failure-mode rule). A pure capacity/provisioning ask folds into the aggregate entirely; an edge naming a distinct deliverable absent from the producer's plans still earns its own AL-01 (this keeps answer-key row A2 reportable — first-draft phrasing that suppressed all per-edge AL-01s traded A2 for A5 in eval).
- Add a matching example in AL-07 illustrating the misclassification and the correct aggregated finding (CLAUDE.md requires every taxonomy change to carry an example in the same file).
- No IDs added, renumbered, or renamed; no changes to SKILL.md, report-format.md, or the fixture.

Planted defect newly caught: **A5** (AL-07 · Resource contention, Payments + Data ↔ Platform). No other answer-key rows are affected; the intentional non-defects list must remain unreported.

## Capabilities

### New Capabilities

- `alignment-detection`: Cross-team alignment failure-mode detection behavior owned by `references/alignment-taxonomy.md` — specifically the AL-01/AL-07 classification and aggregation requirement introduced here.

### Modified Capabilities

(none — no specs exist yet under `openspec/specs/`)

## Impact

- `references/alignment-taxonomy.md` only (AL-07 heuristic + example; possibly a one-line pointer in AL-01's heuristic).
- Eval behavior: the alignment-category fixture eval must catch A5 while still catching A-row defects previously found and not exceeding the finding budget.

## Non-goals

- No changes to the goodness rubric, report format, severity scale, SKILL.md procedure, or the fixture/answer key.
- No new AL-XX failure mode; this refines detection guidance for existing IDs.
- No general rework of the "one finding, one failure mode" rule beyond this specific AL-01/AL-07 precedence.
