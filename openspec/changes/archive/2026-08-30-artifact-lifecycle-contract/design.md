# Design — artifact-lifecycle-contract

## Context

See proposal.md — Why. This is a markdown-only skill repo; the "implementation" is contract prose in the owning files, following CLAUDE.md's ownership rules: templates/output contracts live only in `references/report-format.md`, procedure steps only in `SKILL.md` (which must stay under ~150 lines), gate logic only in `.claude/skills/openspec-loop/phases/verify-gate.md`.

## Goals / Non-Goals

**Goals:**
- One unambiguous home for the contract, reachable from the procedure in one hop.
- Keep SKILL.md's addition minimal (a short step pointing at the contract), preserving the line budget.
- Registry schema concrete enough that two independent agents produce identical decisions.

**Non-Goals:**
- No scripts or tooling to manage the registry — the contract is followed by the agent, not enforced by code.
- No changes to report sections 1–6 or their templates.

## Decisions

1. **Contract placement: a new top-level section in `references/report-format.md`, after §6.** Rationale: report-format.md is the output contract file; publishing is part of the output contract. Alternative — a new `references/artifact-lifecycle.md` file — rejected: adds a file for ~40 lines and weakens the "one output-contract home" rule.
2. **SKILL.md gets a "Step 7 — Publish" of a few lines** that (a) says fixture/eval runs skip it entirely, and (b) defers everything else to report-format.md's contract section by name. Rationale: keeps the 150-line budget and the no-duplication rule.
3. **Registry schema shown as a concrete JSON example** in the contract (keys `portfolio-dashboard`, `team-report/<team>`; fields `url`, `title`, `favicon`, `last_published`, `cycle_date`). A concrete example prevents field-name drift better than prose.
4. **Self-healing expressed as an ordered decision procedure** (adopt user URL → read registry → verify URL → update / re-create+report / create+register), so the update-vs-create decision is a lookup, not a judgment call.
5. **Verify-gate change is two added bullets** in the structural-checks list of `phases/verify-gate.md` (contract section exists; SKILL.md publish step references it). The deferred behavioral eval is recorded there as an explicit "future work" note so it isn't silently forgotten.

## Risks / Trade-offs

- [Registry file deleted or hand-edited by user] → self-healing rules treat a missing/invalid entry as "create and register", always reported in the run summary.
- [Two concurrent runs on the same portfolio] → out of scope; contract assumes one run at a time per working folder (noted in the contract text).
- [SKILL.md creeping past 150 lines] → publish step budgeted at ≤8 lines; verify gate already checks the line cap.

## Migration Plan

Doc-only change; no rollout. The predecessor MDPI project is untouched. First real run against a portfolio with a pre-existing artifact: user supplies the URL, which the adopt rule folds into the registry.
