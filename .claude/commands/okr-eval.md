---
description: Run the OKR-Ninja eval harness — smoke (1 run per slice), baseline (5 runs per slice at a git ref), or decision (5 runs per slice per arm, old skill vs new)
---

# /okr-eval — run the eval harness

**Usage:** `/okr-eval smoke [slice,slice]` · `/okr-eval baseline [--ref <git-ref>]` · `/okr-eval candidate [--runs N] [slice,slice]` · `/okr-eval decision --baseline <git-ref> [--runs N] [slice,slice]` · add `--batch <id>` to resume an existing batch.

Arguments: `$ARGUMENTS`

You are the orchestrating session. Model runs execute as subagents on this session's subscription — on this session's model unless you launch them with a model override, one model per batch — and each run's report is captured from the subagent's transcript; grading is deterministic and spends no tokens. Slices: `fixture1-portfolio`, `fixture2-portfolio`, `fixture1-platform-single-team` (default: all). For a smoke run inside the verify gate, pass the slices whose keys cover the category the change touched — each fixture's "Modes deliberately not covered" section says which modes are the other fixture's territory; a procedure-wide change runs all three, and any change touching mode selection or single-team behaviour includes the Platform slice.

## 1. Plan

```bash
python3 evals/grader/harness.py check
python3 evals/grader/harness.py plan --tier <smoke|baseline|decision> [--slices a,b] [--runs N] [--baseline-ref <ref>] [--batch <id>] --json
```

`check` must exit 0 first — never run on stale keys. Parse the plan JSON: `batch_dir`, and `pending` entries each with `run_dir`, `prompt`, `report`. Re-planning an existing batch lists only the runs that still lack a report.

## 2. Execute the pending runs

For every pending run, read its `prompt.md` and spawn one **general-purpose** Agent whose task is that prompt **verbatim**; do not summarise it, add instructions, or change paths. Launch them in the background, at most **five** at a time, and note each launch result's `output_file` (the subagent's JSONL transcript) against its `run_dir`. Wait for each to finish. Never edit prompts, inputs, or reports yourself.

The runner does not write `report.md`: the environment refuses subagent report writes, so the prompt tells it to return the complete report as its final message between two marker lines. When an Agent finishes, capture that report **from the transcript file**, taking the token count and duration from the Agent result's usage line:

```bash
python3 evals/grader/harness.py capture <run_dir> --transcript <output_file> --tokens <subagent_tokens> --seconds <duration_ms / 1000>
```

`capture` extracts the final message byte-exact, validates exactly one marker block, writes `<run_dir>/report.md` itself, and writes `run.json` with the model id read from the transcript (pass `--model <id>` only as a cross-check; a disagreement fails). Never copy report text out of the completion notification — it HTML-escapes `<` and `&` — and never write, edit, or "fix up" a `report.md` yourself. If the Agent errored, run `capture` with `--agent-error "<message>"` so the reason is recorded.

If `capture` exits non-zero (`agent-error`, `transcript-unreadable`, `no-final-text`, `markers-missing`, `multiple-blocks`, `empty-report`, `model-mismatch`), do not retry inside the same batch: the run counts as *not produced* in the scorecard under that reason. Resume later with `--batch <id>`. A run with no reason recorded — `capture` never ran, or exited on a usage error before writing `run.json` — is counted as `unknown`. Two failures are not runner results and are fixed by re-running the same `capture` command: a write failure whose message names removed files (re-run it before grading), and `transcript-unreadable` with `Operation not permitted`, which means the Bash sandbox is denying the transcript's real location (`output_file` is a symlink into the Claude Code projects directory) — re-run that one command outside the sandbox or allow the path with `/sandbox`, never copy the transcript's text by another route.

## 3. Grade, aggregate, compare

Before grading, move any working files a runner left at its run-directory root (extraction YAML, drafts) into `<run_dir>/scratch/`, which is gitignored, so that only `prompt.md`, the captured `report.md`, `run.json` and `grade.json` are committed per run. A `report.md` a runner wrote despite the prompt is not a working file to keep: `capture` replaces it from the transcript, and also removes any earlier `grade.json` so a resumed batch is re-graded from the captured report (`stale_report_removed` / `stale_grade_removed` in `run.json`).

```bash
python3 evals/grader/harness.py aggregate <batch_dir>        # grades any run without grade.json, writes scorecard.json, prints the table
python3 evals/grader/harness.py compare <batch_dir>          # decision batches: applies the regression rule, writes comparison.json
python3 evals/grader/harness.py compare <batch_dir> --baseline-batch <other_batch_dir>   # candidate-only batch vs an earlier baseline batch: same rule, marked unpaired
```

## 4. Report to the user

Show the scorecard table as printed, then per slice: runs passing the key criterion, runs not produced with their reasons (a transport reason — `agent-error`, `transcript-unreadable` — is a harness or environment failure, not a runner result), structure failures, warnings (mixed or unknown models, unverified supporting quotes), and the recurring extras/duplicates table with counts. Smoke passes only when **every** run passes its key criterion — quote each failing run's `failures` list verbatim. For decision batches, state the comparison verdict and every triggered rule.

Never edit keys, fixtures, or triage entries to turn a batch green. For an extra or duplicate that recurs in three or more runs, propose a triage entry (finding, anchor, bucket, decision, rationale) and leave the decision to the user; only a confirmed entry with a rationale may become `known-red`, and a `skill-error` entry never can.

## Notes

- Runners return the report as their final message and write nothing outside their run directory (scratch files inside it are fine); the harness writes `report.md` from the transcript. The transcript itself (`output_file`, under the session's tasks directory) is not copied into the batch — it holds system prompts and environment details. `<batch>/<arm>/<slice>/input/` and `<batch>/skill/` are regenerable and gitignored; what gets committed per batch is `prompt.md`, `report.md`, `run.json` and `grade.json` per run plus `scorecard.json` and `comparison.json`.
- A batch runs on one model — this session's, or whatever model the Agents are launched with — and every run's model is recorded from its transcript; the scorecard warns when a slice mixes models, and `compare` refuses arms on different models. `compare` warns (in the output and in `comparison.json`) when the arms ran on different prompt-template hashes, which happens when comparing across a prompt change.
- The `candidate` tier runs only the working-tree arm (default 5 runs per slice) for a cheaper, **unpaired** comparison against a committed baseline batch on the same model; a paired `decision` batch remains the release-grade check.
- The baseline arm is exported from git (`git archive <ref> SKILL.md references`), the candidate arm from the working tree; every grade records the arm's SHA, a dirty flag, the model, the prompt-template hash and the key hash.
- `python3 evals/grader/harness.py selftest` checks the grader itself; run it after any change to the harness.
