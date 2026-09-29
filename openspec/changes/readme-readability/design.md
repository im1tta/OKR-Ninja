## Context

See proposal.md — Why. Three things constrain the rewrite:

- The `distribution` spec fixes what README's install documentation must contain. This change's delta splits that content across a Quick start section and an Installation reference section.
- `review-modes` requires README to describe the two-mode routing: a single-team prompt and a portfolio prompt both trigger the skill.
- CLAUDE.md makes README the only home of the product context and of human install instructions, and `openspec/config.yaml` quotes that section by its current heading.

## Goals / Non-Goals

**Goals:**
- A reader can install and try the skill from the first ~60 lines without scrolling past strategy or repo internals.
- Every product decision and every install route present today survives, with commands byte-identical.

**Non-Goals:**
- Revising any product decision. Condensing tightens and rephrases each product-context item, but never drops or revises a decision or its rationale.
- Adding badges, screenshots or new docs files.

## Decisions

**D1 — Section order and names.** The README reads top to bottom as follows:

`# OKR-Ninja` → pitch → `## Quick start` → `## Usage` → `## What you get` → `## Data sources` → `---` divider with a one-line "Reference" lead-in → `## Installation reference` → `## Product context` → `## Development` → `## Roadmap` → `## License`.

The divider marks where casual readers can stop. `## Installation reference` names the spec's second section exactly, which avoids ambiguity at verify. Rejected alternative: a `<details>` collapsible for the reference material, because GitHub renders it but many markdown viewers and agents don't.

**D2 — The Quick start holds exactly what a first install needs.** It carries:
- the macOS/Linux one-liner and the Windows one-liner;
- a sentence each for "run it again to update" and "start a new session and check the skill is listed";
- the claude.ai/Cowork `build` command, the upload step, and the note that you rebuild and re-upload to update.

Everything else goes to the Installation reference: the explanation of `-I`, the platform table, the options, the pinned form, the inspect-first form, the `.plugin`, and the clone and checkout commands.

**D3 — Product context is condensed per item, not summarised as a whole.** Each current paragraph maps to one tighter paragraph or bullet that keeps its decision:
- personas per mode and the §6 hand-off;
- the drift-tracking target vs. the pre-commit review built today, with the mid-quarter guardrail note;
- the four jobs with their build status and the tie-break rule (brevity wins in portfolio mode, depth in single-team mode);
- the distribution intent: demo piece, eval over detection features, fixed doctrine with the AP-06/K3 example, no per-org configuration, and fictional fixtures.

The heading becomes `## Product context`, and `openspec/config.yaml` is updated to cite it.

**D4 — Development replaces the landed roadmap items.** It has four parts:
- a trimmed tree listing the top-level entries only, one line each;
- a short paragraph on the eval harness naming the `/okr-eval` tiers and the three pass criteria;
- one line saying changes go through OPSX;
- a pointer to CLAUDE.md for agents.

The Roadmap keeps only the open items: single-team depth parity, drift tracking, the calibration set, a headless CI driver and routing tests, and larger fixtures.

**D5 — The modes table is trimmed to four rows.** They are core question, goodness depth, alignment, and follow-up. The "Report" row folds into a sentence below the table.

## Risks / Trade-offs

- [Condensing drops a product nuance] → The verify step checks the old README's product-context claims one by one against the new text.
- [A command is accidentally altered when moved] → The verify step diffs every fenced command block, old vs. new, to confirm they are byte-identical.
- [The spec delta drifts from what README actually does] → The verify step runs each scenario of the modified requirement against the final README.

## Migration Plan

Docs only. There is no version bump or release, and the new README is live on merge. Rollback is a revert.
