---
name: openspec-loop
description: Drive the full OpenSpec coding loop end-to-end — explore → refine (guided one-question-at-a-time A/B/C Q&A) → propose → apply → verify → archive — with a single human approval gate after refinement, automatic gated progression through the rest, and a bounded repair loop that fixes failures before escalating. Use when the user wants to run "the loop", take an idea from start to archived change, or chain the opsx workflow.
license: MIT
compatibility: Requires the openspec CLI and the project quality gate (structural checks + fixture eval, scoped as phases/verify-gate.md defines - it names which fixture(s) under examples/ cover a touched category). Orchestrates the existing opsx:* skills; reuses, never re-implements them.
metadata:
  author: relay
  version: "1.0"
---

# OpenSpec loop

Take an idea through the whole OpenSpec lifecycle in one run, so the user steers **once** (at refinement) and the mechanical chaining, gating, and failure-repair happen automatically.

```
 explore* ─▶ refine ─┤APPROVAL├─▶ propose ─▶ apply ─▶ verify ─┐
 (think,     A/B/C Q&A            opsx:      opsx:   opsx:verify│ green?
  no code)   phases/refine.md     propose    apply   + qual gate│
                                                                 │
                            ▲                  repair ◀──────── red┘  (bounded)
                            └── one human gate                   │
                                                        green ─▶ archive
                                                                opsx:archive
```

This skill is an **orchestrator**: at each phase it invokes the existing `/opsx:*` skill (Cursor: `/opsx-*`) rather than re-doing its work. The only net-new logic lives here — the gates, the repair loop, resumability — and in `phases/`.

## When to use

- "Run the opsx loop", "take this idea through opsx", "idea → archived change", "do the full loop".
- The user hands you an idea and wants it shepherded to a finished, verified, archived change.

## Start: orient and pick the entry phase

1. Run `openspec list --json`. If an **in-progress change** matches what the user is doing, offer to **resume** at its current phase (check `openspec status --change "<name>" --json`) instead of starting fresh. Don't restart a change that's mid-apply.
2. Otherwise choose the entry phase from the user's input:
   - Raw idea, not yet thought through → start at **Explore**.
   - Idea is already clear (or they've explored) → start at **Refine**.
   - They explicitly say "just propose/apply this" → honor it, but still run the **Verify** gate before archive.
3. Announce each transition on its own line: `▶ Phase: <phase> · change: <name|—>`.

## Phases

| # | Phase | Runs | Advance when |
|---|-------|------|--------------|
| 1 | Explore* | `/opsx:explore` (thinking only, no code) | user is ready to formalize |
| 2 | **Refine** | `phases/refine.md` (A/B/C Q&A) | **explicit user approval (hard gate)** |
| 3 | Propose | `/opsx:propose` | artifacts apply-ready |
| 4 | Apply | `/opsx:apply` | tasks implemented |
| 5 | Verify | `phases/verify-gate.md` (`/opsx:verify` + quality gate) | **green** (verify ok AND gate passes) |
| 6 | Archive | `/opsx:archive` (sync deltas + archive) | done |

\* Optional — skip if the idea is already clear.

### 1. Explore (optional)

If the idea is raw, invoke the `opsx:explore` skill — a thinking stance, **never write application code**. Skip when the user already explored or the idea is well-formed. Exit when the shape is clear enough to refine.

### 2. Refine — the one human gate

**Load and follow [`phases/refine.md`](phases/refine.md).** It runs the one-question-at-a-time A/B/C elicitation, converges to an **Agreed requirements** summary, and ends by asking for explicit approval.

**Hard rule: do not advance past Refine — do not create a change, write code, or call `/opsx:propose` — until the user explicitly approves.** This is the only mandatory checkpoint in the loop.

### 3. Propose

On approval, invoke the `opsx:propose` skill, passing the refined idea. Feed it the Agreed-requirements summary as the source description so the proposal/design/tasks reflect the decisions made in Refine.

**Propose stops at its own planning boundary — that is expected, not a failure.** Since OpenSpec 1.11.0, `opsx:propose` ends by requiring a new user request before implementation begins. In this loop the **Refine approval _is_ that request** — it authorized the run end-to-end, Apply included. So when Propose returns, close the Propose step, announce `▶ Phase: Apply · change: <name>`, and start Apply as a new step. Do not ask the user to approve a second time, and do not let Propose's boundary rule absorb Apply into the Propose step.

Advance when every artifact in the required set — `applyRequires` plus everything reachable through its `requires` edges — reads `done` or `skipped`.

### 4. Apply

Invoke the `opsx:apply` skill to implement the change's tasks. If implementation reveals a design gap, **update the relevant openspec artifact first** (per the project conventions), then continue tasks — don't silently diverge from the spec. Auto-advance when tasks are complete.

### 5. Verify — the green gate

**Load and follow [`phases/verify-gate.md`](phases/verify-gate.md).** It runs `opsx:verify` plus the project quality gate (the same `make` targets CI runs), defines "green," and runs the **bounded repair loop** back to Apply on failure. Advance to Archive **only on green**.

### 6. Archive

When green, invoke the `opsx:archive` skill (it syncs delta specs into `openspec/specs/` and archives the change). The loop **ends here** — it does not commit, push, or open a PR.

## Cross-cutting rules

- **One gate by default.** Only Refine pauses for the user; phases 3–6 auto-advance on success and stop on failure. If the user wants checkpoints, they can say "pause after each phase" and you add a confirm between every phase.
- **Repair, don't dump.** A failed Verify triggers the bounded repair loop (default **2** cycles) before you hand the failure back to the user. See `phases/verify-gate.md`.
- **Never archive on red.** Verify failure or any failing test blocks Archive.
- **Respect project conventions.** Don't commit, push, or create empty commits — the loop stops at Archive. Minimize scope (defer anything not needed now). Prefer updating openspec artifacts over diverging from them.
- **Stay legible.** Always show the current phase and change name. On any stop (gate, unrecoverable failure, user interruption), state the phase reached and the exact command to resume (`/opsx:apply <name>`, etc.).
- **Configurable defaults** (state them if relevant; flip on request): auto-archive on green = ON; auto-repair cycles = 2; run the fixture eval only when the change touches the skill procedure, rubric, taxonomy, or report format (skip for docs-only changes).

## Hard rules

- Never skip the Refine approval gate or auto-proceed to Propose.
- Never write application code during Explore or Refine.
- Never archive when Verify is red.
- Never commit or push as part of the loop.
