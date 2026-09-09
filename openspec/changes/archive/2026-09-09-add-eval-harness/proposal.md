## Why

The repo's only quality signal today is the verify gate's fresh-subagent fixture eval, graded by eye against a markdown answer key. Nine scratch runs on this branch (three per slice, produced by an earlier session whose grader prototype was lost) show what that misses: every planted defect is found in every run, yet 6 of 9 runs exceed the extras budget, and the extras are the same four or five findings each time — a systematic-precision problem that a single pass/fail verdict cannot name. There is also no way to say whether a future rubric or taxonomy edit made the skill better or worse, because nothing records per-defect behaviour across runs or versions. The content fixes for those recurring extras are queued as a separate change, so the harness must land first to measure them.

## What Changes

- **New `evals/` harness**, Python 3 standard library only, zero model tokens on the grading side:
  - `evals/keys/<fixture>.json` — machine-readable answer keys (accepted-ID lists, evidence anchors, optional anchors, non-defect forbids, not-covered lists, budgets, slices, triage entries). These become the canonical keys; each fixture's `## Answer key` section is **generated** from its JSON key, and a zero-token check fails when the generated section is stale.
  - A slicer that produces run inputs (answer key stripped, single-team slice cut) so source-ref line numbers are checked against what the run actually read.
  - A deterministic grader: parses the mandated finding headings, matches key rows by accepted ID plus evidence anchors, classifies every quote (verbatim / near-miss / fabricated / out-of-scope / mention) after Unicode and whitespace normalisation, deduplicates a second finding on an already-matched anchor, counts extras and non-defect violations against the budget, and checks structural conformance per mode. Ships with self-tests (mini reports with known grades, corrupted keys).
  - An aggregator producing a **scorecard** per batch — per-defect hit rate (any accepted ID, and ID-exact), extras frequency by ID and anchor, non-defect violations, quote classes, structure, tokens and wall time — and a comparator that applies the regression rule to two arms.
- **Triage entries** in the key: a recurring extra is classified once as fixture-ambiguous, rubric-gap, or skill-error, with rationale and status. Entries marked known-red are excluded from the budget count until their fix lands, while still being reported; the fixtures' eval criteria are otherwise untouched.
- **`/okr-eval` command** (`.claude/commands/okr-eval.md`): runs slices via Agent subagents on the session's model, production-faithful (fan-out allowed, cost recorded). Two tiers: **smoke** (1 run per touched slice) and **decision** (5 runs per slice per arm, old skill snapshot and candidate in the same batch). Every run records model ID, skill git SHA, prompt-template hash, tokens and time.
- **Verify gate wiring**: the fixture-eval bullet in `.claude/skills/openspec-loop/phases/verify-gate.md` invokes the smoke tier and reads pass/fail from the grader instead of an ungraded subagent judgement. Decision batches remain a manual pre-release step.
- **Baseline batch**: 15 production-faithful runs of the unchanged skill at `main` (5 per slice, single arm), committed under `evals/runs/` with their scorecard, as the "before" arm for the content-fix change and as the harness's own acceptance test.
- **Fixture 1 leakage caveat**: the scorecard flags fixture 1 rows whose scenarios also appear in the `references/report-format.md` worked examples, and treats fixture 2 as the primary regression fixture; the example rewrite itself is a later content change.
- **Docs**: `CLAUDE.md` gains an `evals/` file-map row and a testing step pointing at `/okr-eval`; `README.md`'s roadmap line for the CI eval harness is updated.

`SKILL.md` and `references/` are **not** modified. Detection behaviour is unchanged, so this change newly catches **no** planted defect in `examples/sample-portfolio.md` or `examples/sample-portfolio-2.md`; the harness measures detection, it does not alter it.

## Capabilities

### New Capabilities
- `eval-harness`: deterministic grading of skill runs against machine-readable answer keys; batch orchestration tiers (smoke, decision) via subagents on the subscription; scorecard contents; the paired-arm comparison and regression rule; per-run provenance (model, SHA, prompt hash, cost); committed run artefacts; the verify gate's use of the smoke tier.

### Modified Capabilities
- `eval-fixtures`: answer-key ownership moves to a canonical JSON key per fixture with the fixture's markdown key section generated from it; keys gain grader-checkable evidence anchors and triage entries; the eval criterion's extras budget excludes triaged known-red entries until fixed; fixture 1's overlap with reference worked examples is recorded as a caveat.

## Impact

- **New files**: `evals/keys/*.json`, `evals/prompts/*`, `evals/grader/` (scripts plus `selftest/`), `evals/runs/<batch>/…` (reports, grades, scorecard), `.claude/commands/okr-eval.md`.
- **Modified files**: `examples/sample-portfolio.md` and `examples/sample-portfolio-2.md` (answer-key sections regenerated from JSON, content-preserving), `.claude/skills/openspec-loop/phases/verify-gate.md` (fixture-eval bullet), `CLAUDE.md`, `README.md`, `.gitignore` (ignore regenerated sliced inputs under `evals/runs/`; `scratch/` stays ignored).
- **Untouched**: `SKILL.md`, `references/*.md`, `openspec/config.yaml`.
- **Subscription quota**: the baseline batch costs 15 production-faithful runs; each later skill-content change costs one smoke run per touched slice; a paired decision batch costs 30 runs.
- **Existing scratch runs**: the nine reports under `evals/scratch/` (gitignored) are reused only as grader self-test inputs; they are not a baseline.
- **Dependencies**: `python3` on the developer's machine; no packages, no build.

## Non-goals

- Any edit to `SKILL.md` or `references/`: the goodness-side one-finding-per-instance rule, a G7 accepted-alternate ID, and the fixes for triaged recurring extras belong to the follow-up content change, which must show a paired before/after scorecard from this harness.
- Rewriting the `references/report-format.md` worked examples into a third fictional universe (a later content change).
- Routing/trigger tests for the skill description (not observable from subagent output; would need headless transcripts or `claude plugin eval`).
- A zero-defect control fixture, per-mode mini fixtures, or any new fixture content.
- A headless `claude -p` driver, GitHub CI execution, or `claude plugin eval` packaging (the scripts are written so a headless wrapper can be added later).
- An LLM-judge grading tier, rewrite-quality scoring, or severity calibration.
- Model comparisons (model matrix per batch); the model is inherited from the session and recorded.
- Compatibility with skill-creator's `benchmark.json` viewer schema.
