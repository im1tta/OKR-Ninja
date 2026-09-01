# Design

## Context

See proposal.md — Why. The taxonomy's graph-structural checks (Part 2, Step 3) run AL-01 per edge and AL-07 per resource node; nothing tells an evaluator which wins when the same edges feed both. Part 3 §5 ("one finding, one failure mode") says to report the root-cause category, but neither AL-01 nor AL-07 says which is root cause here — so an edge-by-edge pass emits AL-01 twice and never assembles the AL-07 aggregate (the fixture A5 miss).

## Goals / Non-Goals

- Goal: make the AL-07-wins rule explicit at the point where an evaluator classifies, i.e., inside the AL-01 and AL-07 entries themselves, not only in Part 3.
- Non-goal: restructuring Part 2/Part 3, adding IDs, or touching other files (report-format.md and goodness-rubric.md own other topics; CLAUDE.md forbids duplication).

## Decisions

1. **Put the aggregation/precedence rule in AL-07's detection heuristic** (the mode that must fire), with a one-sentence redirect in AL-01's detection heuristic (the mode that must yield). Rationale: evaluators read the entry they're about to apply; a rule living only in Part 3 §5 demonstrably failed. Alternative considered: a standalone "disambiguation" subsection — rejected as it adds structure for a single pair and risks becoming a second home for classification rules.
2. **Phrase the AL-01 side as a redirect, not a duplicate definition**: "two or more claimants on one producer with a stated capacity constraint → escalate to AL-07 (aggregate), cross-reference AL-01" — referencing AL-07 by canonical name only, per the no-duplication rule. *Deliberate divergence (verify repair cycle 1):* the redirect carries one qualifier — distinct deliverable → separate AL-01, pure capacity/provisioning ask → folds into AL-07 — because a bare redirect left the AL-01 reading path contradicting AL-07's fold-in rule (a reviewer reading only AL-01 would still file the provisioning edge standalone). The qualifier mirrors AL-07's criterion without restating its definition; AL-07's rule also states the tie-break explicitly (capacity-ask clause wins when both fit).
3. **Example placement**: extend AL-07 with a scenario narrative + heuristic reading (permitted stand-in for an after-state under CLAUDE.md's example rule), using Meridian teams (Bluefin/Ember claiming Atlas capacity) to mirror the fixture's Payments/Data/Platform shape without copying it.

## Risks / Trade-offs

- [Over-aggregation: evaluators fold genuine single-edge AL-01s into AL-07] → the rule triggers only at ≥2 claimants on the same resource **and** a stated capacity constraint (or countable supply) on the owner's side; single-claimant edges stay AL-01. Confirmed by eval: a first-draft rule suppressing *all* per-edge AL-01s made the evaluator merge the fixture's A2 (Data's unacknowledged pipeline migration) into the A5 aggregate — the shipped rule therefore distinguishes pure capacity asks (fold in) from named-deliverable absences (separate AL-01, cross-referenced).
- [Fixture eval regression elsewhere (extra findings blowing the budget)] → verify step re-runs the alignment-category eval against the full answer key and non-defects list, not just A5.

## Migration Plan

Docs-only; single commit through OPSX apply → verify → archive. Rollback = revert the taxonomy edit.
