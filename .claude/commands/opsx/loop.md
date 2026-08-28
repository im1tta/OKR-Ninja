---
name: "OPSX: Loop"
description: Run the full OpenSpec loop — explore → refine → propose → apply → verify → archive — with one approval gate after refine
category: Workflow
tags: [workflow, loop, orchestration, experimental]
---

Drive the whole OpenSpec lifecycle in one run, so you steer **once** (at refinement) and the chaining, gating, and failure-repair happen automatically.

**Follow the [`openspec-loop`](../../skills/openspec-loop/SKILL.md) skill** — it is the source of truth. It orchestrates the existing `/opsx:*` skills as sub-steps and adds the gates, the repair loop, and resumability. Its phase subskills live in `.claude/skills/openspec-loop/phases/`.

```
 explore* ─▶ refine ─┤APPROVAL├─▶ propose ─▶ apply ─▶ verify ─┐ green?
                                                              │
                            repair ◀── back to apply ◀──── red ┘ → archive
```

**Input**: the argument after `/opsx:loop` is the starting idea (or empty to be asked).

**Entry & resume**
- Raw idea → start at **Explore**; already-clear idea → start at **Refine**.
- If an in-progress change matches, the skill offers to **resume** at its current phase instead of restarting.

**The one gate**: after Refine, the loop stops for your explicit approval before creating the change. Everything after auto-advances on success, repairs on failure (bounded), and **never archives on red**. The loop ends at archive — it does not commit, push, or open a PR. Say "pause after each phase" if you want checkpoints between every step.
