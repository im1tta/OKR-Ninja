# Phase 5 — Verify gate + repair loop

Decide whether the change is **green** (ready to archive) and, if not, fix it automatically before bothering the user.

## What "green" means

Green requires **both**:

1. **Spec coherence — independent and refute-mode.** Run `opsx:verify` as a *non-author* check (the agent that implemented the change does not sign off its own work): hunt for one requirement the docs violate, not confirmation that it "looks done." Brief it with the design **rationale** — the `design.md` decisions and any deliberate-divergence notes in the skill docs — so an intentional divergence is reported as intentional, not a manufactured bug.
2. **Quality gate** — the skill is markdown only (`install.py` packages it, but nothing is compiled), so the gate is:
   - **Structural checks** — SKILL.md frontmatter parses and stays under ~150 lines; every `references/` and `phases/` path mentioned in any doc resolves to a real file; no rubric/taxonomy/report-format detail duplicated across files (each topic has exactly one owning file per CLAUDE.md); `references/report-format.md` contains the "Artifact lifecycle" contract section (registry schema + publish decision procedure); SKILL.md's publish step references that "Artifact lifecycle" section rather than restating it; `python3 install.py check` exits 0 (the frontmatter passes the skill-upload rules, including the 1,024-character description limit); `python3 evals/grader/harness.py check` exits 0 (the JSON answer keys under `evals/keys/` validate, every evidence anchor resolves, the catalog stays fully covered across keys, and each fixture's generated `## Answer key` section is fresh), plus `python3 evals/grader/harness.py selftest` whenever the harness itself changed.
   - **Lifecycle eval** — **only** when the change touches the publish path: `SKILL.md`'s Step 7, the "Artifact lifecycle" section of `references/report-format.md`, the publish seam (`evals/lifecycle/publish_seam.py`), the scratch corpus under `evals/corpora/`, or the scenario file (`evals/lifecycle/scenarios.json`). Run `/okr-eval lifecycle` (defined in `.claude/commands/okr-eval.md`): it plans the five scenarios — create, update, re-create, adopt, and fixture-exempt (a fixture corpus with the same seam, which must publish nothing) — runs each as a *fresh* subagent against the scratch corpus with its registry and seam store pre-seeded, and grades them with `python3 evals/grader/harness.py lifecycle-grade --batch-dir <batch>`. The gate's result is that grader's verdict, never a subagent's judgement, and it is green **iff** every scenario passes: each deliverable key reaches the outcome its scenario declares, no artifact is created for a key that already had a registry entry except a single re-create stated with its reason and its deliverable in the run summary, every registered URL was verified through the seam before the run acted on it, the registry agrees with the artifact it points at, timestamps advance, no prior cycle's local output is modified, and the fixture-exempt run publishes nothing and writes no registry at all. Skip it — and say so — for a change that cannot reach the publish path.
   - **Fixture eval** — **only** when the change touches SKILL.md's procedure, the rubric, the taxonomy, the report format, or a fixture's planted content: run the harness's smoke tier, `/okr-eval smoke <slices>` (defined in `.claude/commands/okr-eval.md`), for the slices whose keys cover the touched category — `fixture1-portfolio`, `fixture2-portfolio`, `fixture1-platform-single-team`; each key's "Modes deliberately not covered" section says which modes are the other fixture's territory; when in doubt, or for procedure-wide changes, run all three, and include the Platform slice whenever mode selection or single-team behaviour is touched. The runs execute as *fresh* subagents (never the author) and the fixture eval is green **iff** the harness reports every run passing its key criterion — planted defects found by canonical ID, zero fabricated quotes, budget respected net of confirmed known-red triage entries — with structure failures and warnings reported alongside the verdict. Skip it for docs-only changes (README, CLAUDE.md) for speed (say which you chose and why).

Green = `opsx:verify` reports complete & coherent **AND** the structural checks (and the fixture eval / lifecycle eval when run) all pass.

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
- **Don't loosen the gate to pass** — no skipping the fixture or lifecycle eval, editing the answer key or a lifecycle scenario to match a miss, adding a known-red triage entry the user has not confirmed, deleting checks, or lowering thresholds to force green. Fix the cause.
- Report honestly: if you skipped the fixture eval, say so; if a fixture result is borderline (a defect arguably found under a different name), surface it rather than silently counting it green.
