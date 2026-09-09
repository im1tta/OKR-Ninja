---
description: Run the OKR-Ninja eval harness — smoke (1 run per slice), baseline (5 runs per slice at a git ref), or decision (5 runs per slice per arm, old skill vs new)
---

# /okr-eval — run the eval harness

**Usage:** `/okr-eval smoke [slice,slice]` · `/okr-eval baseline [--ref <git-ref>]` · `/okr-eval decision --baseline <git-ref> [--runs N] [slice,slice]` · add `--batch <id>` to resume an existing batch.

Arguments: `$ARGUMENTS`

You are the orchestrating session. Model runs execute as subagents on this session's model and subscription; grading is deterministic and spends no tokens. Slices: `fixture1-portfolio`, `fixture2-portfolio`, `fixture1-platform-single-team` (default: all). For a smoke run inside the verify gate, pass the slices whose keys cover the category the change touched — each fixture's "Modes deliberately not covered" section says which modes are the other fixture's territory; a procedure-wide change runs all three, and any change touching mode selection or single-team behaviour includes the Platform slice.

## 1. Plan

```bash
python3 evals/grader/harness.py check
python3 evals/grader/harness.py plan --tier <smoke|baseline|decision> [--slices a,b] [--runs N] [--baseline-ref <ref>] [--batch <id>] --json
```

`check` must exit 0 first — never run on stale keys. Parse the plan JSON: `batch_dir`, and `pending` entries each with `run_dir`, `prompt`, `report`. Re-planning an existing batch lists only the runs that still lack a report.

## 2. Execute the pending runs

For every pending run, read its `prompt.md` and spawn one **general-purpose** Agent whose task is that prompt **verbatim**; do not summarise it, add instructions, or change paths. Launch them in the background, at most **five** at a time, and wait for each to finish. Never edit prompts, inputs, or reports yourself.

When an Agent returns, record its provenance immediately, taking the token count and duration from the Agent result's usage line and the model id from this session's own identity:

```bash
python3 evals/grader/harness.py record <run_dir> --model <model-id> --tokens <subagent_tokens> --seconds <duration_ms / 1000>
```

If an Agent errors or leaves no `report.md`, do not retry inside the same batch: the run counts as *not produced* in the scorecard. Resume later with `--batch <id>`.

## 3. Grade, aggregate, compare

Before grading, move any working files a runner left at its run-directory root (extraction YAML, drafts) into `<run_dir>/scratch/`, which is gitignored, so that only `prompt.md`, `report.md`, `run.json` and `grade.json` are committed per run.

```bash
python3 evals/grader/harness.py aggregate <batch_dir>        # grades any run without grade.json, writes scorecard.json, prints the table
python3 evals/grader/harness.py compare <batch_dir>          # decision batches only: applies the regression rule, writes comparison.json
```

## 4. Report to the user

Show the scorecard table as printed, then per slice: runs passing the key criterion, structure failures, warnings (mixed or unknown models, unverified supporting quotes), and the recurring extras/duplicates table with counts. Smoke passes only when **every** run passes its key criterion — quote each failing run's `failures` list verbatim. For decision batches, state the comparison verdict and every triggered rule.

Never edit keys, fixtures, or triage entries to turn a batch green. For an extra or duplicate that recurs in three or more runs, propose a triage entry (finding, anchor, bucket, decision, rationale) and leave the decision to the user; only a confirmed entry with a rationale may become `known-red`, and a `skill-error` entry never can.

## Notes

- Runs write only inside their run directory. `<batch>/<arm>/<slice>/input/` and `<batch>/skill/` are regenerable and gitignored; what gets committed per batch is `prompt.md`, `report.md`, `run.json` and `grade.json` per run plus `scorecard.json` and `comparison.json`.
- The baseline arm is exported from git (`git archive <ref> SKILL.md references`), the candidate arm from the working tree; every grade records the arm's SHA, a dirty flag, the model, the prompt-template hash and the key hash.
- `python3 evals/grader/harness.py selftest` checks the grader itself; run it after any change to the harness.
