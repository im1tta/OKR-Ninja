## Why

Claude Code now refuses every subagent `Write` of a report file (`Subagents should return findings as text, not write report files`), and the subagent system prompt tells runners to return findings as text. The eval prompts still tell runners to write `report.md`, so on `claude-sonnet-5` (18 of 18 runs in `2026-09-14-candidate-sonnet-6115de2`) and `claude-opus-5` (a probe) every run either gives up and returns the report as text — graded "report not produced", an environment failure counted as a model failure — or re-types the report into a Bash heredoc, which alters characters (90 em-dashes became `--`, `$` became `\$`) and turned one fabricated quote into six. The verify gate's smoke tier cannot be trusted until the transport is fixed.

## What Changes

- **Prompt templates** (`evals/prompts/portfolio.md`, `evals/prompts/single-team.md`): the runner no longer writes the report to a file. It replies with the complete report as its final message, between two exact marker lines, with nothing it needs graded outside them. Scratch files inside `{{run_dir}}` remain allowed. Every other rule keeps its meaning. The prompt hashes change, which is expected and recorded per batch as today.
- **Harness `capture` subcommand** (`evals/grader/harness.py`, stdlib only): `capture <run_dir> --transcript <path> [--tokens N] [--seconds S] [--model ID] [--agent-error TEXT]` reads the subagent's JSONL transcript, takes the last assistant message that carries text, validates exactly one marker block, writes the block's content byte-exact to `<run_dir>/report.md`, and writes `run.json` provenance with the model read from the transcript (a disagreeing `--model` fails loudly). On any failure it writes no `report.md` and records a named not-produced reason in `run.json`.
- **Not-produced reasons flow through grades and the scorecard**, so a capture or transport failure is never reported as a runner that failed to finish: grades carry the reason, the scorecard counts runs per reason and prints them.
- **`compare` surfaces prompt-hash mismatches** between compared arms as a printed warning recorded in `comparison.json` (it keeps refusing mismatched models).
- **`/okr-eval` orchestration** (`.claude/commands/okr-eval.md`): the orchestrator runs `capture` on each finished runner's transcript (`output_file`), never copies report text from a completion notification (which HTML-escapes it), never retries inside a batch, and never writes a report itself.
- **Self-tests** for capture: clean capture; `<`, `&` and em-dashes preserved exactly; preamble and trailing chatter outside the markers; missing markers; two marker blocks; no assistant text; a model cross-check mismatch.
- `HARNESS_VERSION` moves from 2 to 3: grades and scorecards gain not-produced fields and runs are transported differently, so a batch's version now says which transport produced it.
- Not breaking for committed batches: grading and aggregating every batch under `evals/runs/` still works and changes no committed pass/fail figure.

This change touches no detection behavior — no skill content, rubric, taxonomy, report format, fixture or key — so it newly catches no planted defect in either fixture.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `eval-harness`: the "Batch tiers and execution" requirement changes from runs writing their report inside their run directory to runs returning the report as their final message, captured byte-exact from the transcript, with named not-produced reasons and the model recorded per run from the transcript (batches stay single-model; a per-batch model override is allowed). "Run provenance" gains the not-produced reason and the transcript-derived model. "Scorecard per batch" distinguishes not-produced reasons. "Regression rule between arms" gains the prompt-hash mismatch warning (it governs both paired and `--baseline-batch` comparisons; the "Cross-batch comparison" requirement is unchanged).

## Impact

- `evals/prompts/portfolio.md`, `evals/prompts/single-team.md` — the output rule and the closing line.
- `evals/grader/harness.py` — new `capture` subcommand, transcript parsing, reason plumbing in `grade_run_dir`/`not_produced_grade`, scorecard fields, `compare` warning, self-test case type `capture`, `HARNESS_VERSION` 3.
- `evals/grader/selftest/cases/capture-*` — synthetic JSONL transcripts (seven at first proposal; 36 at archive, after four repair cycles and a final independent verify) mirroring the real transcript shape (no real transcript content is copied into the repo).
- `.claude/commands/okr-eval.md` — step 2 (execute), step 3 (working files) and Notes.
- `openspec/specs/eval-harness/spec.md` — via the delta at archive time.
- `CLAUDE.md` — the `evals/` file-map row lists the harness subcommands; `capture` is added. `README.md` is unchanged: its harness description ("runs the skill against each fixture as subagents ... and grades every report") stays true. `.claude/skills/openspec-loop/phases/verify-gate.md` is unchanged: it names the smoke tier and `/okr-eval`, not the transport.
- Committed batches under `evals/runs/` are untouched.

## Non-goals

- Not evading the guard: no renaming the output file, no telling runners to write the report via Bash.
- Not building a headless `claude -p` driver (option C); that is a separate later change.
- Not changing any grading rule: findings-must-quote-evidence and the quote classes are untouched; this is transport only.
- Not retrying failed runs inside a batch, and not backfilling the `2026-09-14` Sonnet batch, which lives on another branch.
- Not making batches multi-model: a batch still runs on one model; `capture` records what the transcript says and the scorecard keeps warning on mixed models.
