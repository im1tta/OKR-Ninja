# Phase 5 — Verify gate + repair loop

Decide whether the change is **green** (ready to archive) and, if not, fix it automatically before bothering the user.

## What "green" means

Green requires **both**:

1. **Spec coherence — independent and refute-mode.** Run `opsx:verify` as a *non-author* check (the agent that implemented the change does not sign off its own work): hunt for one requirement the docs violate, not confirmation that it "looks done." Brief it with the design **rationale** — the `design.md` decisions and any deliberate-divergence notes in the skill docs — so an intentional divergence is reported as intentional, not a manufactured bug.
2. **Quality gate** — this is a markdown skill repo (no build), so the gate is:
   - **Structural checks** — SKILL.md frontmatter parses and stays under ~150 lines; every `references/` and `phases/` path mentioned in any doc resolves to a real file; no rubric/taxonomy/report-format detail duplicated across files (each topic has exactly one owning file per CLAUDE.md).
   - **Fixture eval** — **only** when the change touches SKILL.md's procedure, the rubric, the taxonomy, the report format, or a fixture's planted content: have a *fresh* subagent (not the author) run the okr-ninja skill against the fixture(s) under `examples/` whose answer keys cover the touched category (each key's "Modes deliberately not covered" section says which modes are the other fixture's territory; when in doubt, or for procedure-wide changes, run both) and compare its findings to that fixture's `## Answer key` — planted defects in the touched category must be found, every reported quote must appear verbatim in the fixture, and no finding may cite text that isn't there. Skip it for docs-only changes (README, CLAUDE.md) for speed (say which you chose and why).

Green = `opsx:verify` reports complete & coherent **AND** the structural checks (and fixture eval when run) all pass.

## Red → bounded repair loop

On any failure, do **not** dump it on the user yet:

1. **Diagnose precisely** — name the failing check and the specific cause (which missed defect, which broken reference, which spec/task gap).
2. **Fix at the right altitude:**
   - A spec/design gap → update the relevant openspec artifact **first**, then continue tasks (don't let the docs and spec diverge).
   - A defect in the skill docs themselves (rubric anchor too vague to converge, missing detection heuristic, broken cross-reference) → fix the owning file.
3. **Re-apply** — invoke `opsx:apply` to make the fix, then **re-run this whole gate**.
4. **Bound it** — default **2** auto-repair cycles. If still red after that, **stop** and hand back to the user with: the phase reached, the exact failures, what you tried, and the resume command (`/opsx:apply <name>`).

## Hard rules

- **Never advance to Archive on red.** A failing verify or a single failing test blocks archive.
- **Refute-dominant, not majority vote.** For deterministic spec conformance, one cited, reproducible violation blocks archive even if other checks pass — don't average it away. Reserve odd-number voting for genuinely stochastic near-threshold claims (e.g. whether a rubric anchor converges across independent scorers) only.
- **For changes touching the scoring anchors or evidence-discipline rules**, add independent reviewers with separate lenses — a scoring-convergence lens (would two independent scorers land on the same 0–4 level from these anchors?) and an evidence-discipline lens (can any finding be produced without a verbatim quote?) — each with only its own rubric; don't share stress tests across lenses (that manufactures false consensus).
- **Don't loosen the gate to pass** — no skipping the fixture eval, editing the answer key to match a miss, deleting checks, or lowering thresholds to force green. Fix the cause.
- Report honestly: if you skipped the fixture eval, say so; if a fixture result is borderline (a defect arguably found under a different name), surface it rather than silently counting it green.
