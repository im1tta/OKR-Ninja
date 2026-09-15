---
description: Run the OKR-Ninja eval harness — smoke (1 run per slice), baseline (5 runs per slice at a git ref), decision (5 runs per slice per arm, old skill vs new), or lifecycle (the artifact-lifecycle contract eval)
---

# /okr-eval — run the eval harness

**Usage:** `/okr-eval smoke [slice,slice]` · `/okr-eval baseline [--ref <git-ref>]` · `/okr-eval candidate [--runs N] [slice,slice]` · `/okr-eval decision --baseline <git-ref> [--runs N] [slice,slice]` · `/okr-eval lifecycle [scenario,scenario]` · add `--batch <id>` to resume an existing batch.

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
python3 evals/grader/harness.py compare <batch_dir>          # decision batches: applies the regression rule, writes comparison.json
python3 evals/grader/harness.py compare <batch_dir> --baseline-batch <other_batch_dir>   # candidate-only batch vs an earlier baseline batch: same rule, marked unpaired
```

## 4. Report to the user

Show the scorecard table as printed, then per slice: runs passing the key criterion, structure failures, warnings (mixed or unknown models, unverified supporting quotes), and the recurring extras/duplicates table with counts. Smoke passes only when **every** run passes its key criterion — quote each failing run's `failures` list verbatim. For decision batches, state the comparison verdict and every triggered rule.

Never edit keys, fixtures, or triage entries to turn a batch green. For an extra or duplicate that recurs in three or more runs, propose a triage entry (finding, anchor, bucket, decision, rationale) and leave the decision to the user; only a confirmed entry with a rationale may become `known-red`, and a `skill-error` entry never can.

## 5. The `lifecycle` tier — the artifact-lifecycle behavioural eval

`/okr-eval lifecycle [scenario,...]` grades the **publish contract**, not report content: scenarios `create`, `update`, `recreate`, `adopt` and `fixture-exempt` (default: all), declared in `evals/lifecycle/scenarios.json`. The last is the counter-case: same seam, same working folder, but one of the skill's own fixtures as the corpus — a passing run publishes nothing and writes no registry.

```bash
python3 evals/grader/harness.py check
python3 evals/grader/harness.py lifecycle-plan [--scenarios a,b] [--batch <id>] --json
```

Planning seeds each run's working folder (`work/`, with the registry the scenario declares) and its seam store (`seam/store.json`), then renders the prompt. Give every pending run one **general-purpose** Agent whose task is its `prompt.md` **verbatim** — the same rule as the tiers above: never summarise it, never add instructions, and never publish or edit a registry yourself. The runs are independent; launch them together. Each reviews the scratch corpus, publishes through the seam, writes its registry, and ends with a `summary.md`; record provenance with `record <run_dir> --model … --tokens … --seconds …` exactly as for report runs.

```bash
python3 evals/grader/harness.py lifecycle-grade --batch-dir evals/runs/<batch>   # exits non-zero if any scenario fails
```

If a run dies mid-flight (a stalled agent, an interrupted session), re-plan it with `lifecycle-plan --batch <id> --reseed` before relaunching: that resets a *pending* run's working folder and seam store to their seeded state, so grading judges behaviour rather than wreckage. It never touches a run that already has a `summary.md` — to redo one of those, because the scenario's own declaration changed, add `--force`. Grading refreshes each run's status in `batch.json`, and warns when the scenario file, prompt template or corpus has changed since the run was planned.

Grading is deterministic and token-free — the registry the run wrote, the seam ledger, the run summary and the working folder, checked against the scenario's declared outcomes. Report per scenario: pass/fail, every failed check verbatim, and any warnings. A failing scenario is a finding about the skill: never fix it by editing a run's registry or store, or by relaxing the scenario file.

## Notes

- Runs write only inside their run directory. `<batch>/<arm>/<slice>/input/` and `<batch>/skill/` are regenerable and gitignored; what gets committed per batch is `prompt.md`, `report.md`, `run.json` and `grade.json` per run plus `scorecard.json` and `comparison.json`.
- The `candidate` tier runs only the working-tree arm (default 5 runs per slice) for a cheaper, **unpaired** comparison against a committed baseline batch on the same model; a paired `decision` batch remains the release-grade check.
- The baseline arm is exported from git (`git archive <ref> SKILL.md references`), the candidate arm from the working tree; every grade records the arm's SHA, a dirty flag, the model, the prompt-template hash and the key hash.
- `python3 evals/grader/harness.py selftest` checks the grader itself — report grading and lifecycle grading alike; run it after any change to the harness.
- Lifecycle batches commit, per run, `prompt.md`, `summary.md`, `work/` (the registry and the cycle's outputs), `seam/store.json` (the ledger) and `grade.json`; the skill snapshot under `<batch>/skill/` stays regenerable and gitignored.
