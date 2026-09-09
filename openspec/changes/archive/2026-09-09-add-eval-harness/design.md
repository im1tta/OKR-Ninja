## Context

See `proposal.md` — Why. Current state that shapes the approach:

- Markdown-only repo; the answer keys are markdown tables at the bottom of `examples/sample-portfolio.md` and `examples/sample-portfolio-2.md`; the verify gate asks a fresh subagent to run the skill and eyeball the result.
- Nine ungraded scratch reports exist under `evals/scratch/` (gitignored) from an earlier session, together with that session's grader *outputs* (`out.json`, a corrupted key, mini reports). The grader script itself survives nowhere; its key shape — `defects[].accepted`, evidence anchors `{"item": "KR P1.2"}` / `{"section": "Platform team"}`, `non_defects[].forbid`, `not_covered`, `slices` — is the seed for this design.
- Hand-grading those runs: recall 14/14, 13/13 and 3/3 in every run; the extras budget fails in 6 of 9 runs; the extras recur (AP-10 on Platform PL1, AP-01 on Data D2.1, AP-12 on Accounts AC3.2, AL-05 Courier↔C3, PL1.3 under three IDs). This is what the scorecard must make visible.
- Runs must execute on the subscription: Agent subagents inside a Claude Code session are available everywhere the repo is developed; the standalone `claude` CLI is not on this machine's PATH. `python3` is.
- Constraints from the Q&A: deterministic stdlib-only grading, JSON key canonical with the fixture section generated, production-faithful runs, paired arms, 1/5 run tiers, known-red allowlist sourced from triage entries, no edits to `SKILL.md` or `references/`.

## Goals / Non-Goals

**Goals (design-level)**
- One CLI entry point with subcommands; no state outside `evals/`; every step re-runnable and idempotent.
- The session does the parallelism (Agent calls); Python never spawns model runs, so a headless driver can be added later without touching grading.
- Parsing tolerant of typographic drift (dash and arrow variants, curly quotes) but strict about the evidence invariant.
- Anchors, not line numbers, locate defects — slicing changes line numbers, markers do not move.

**Non-Goals (design-level)**
- Parallel or remote execution inside Python; HTML viewers; any dependency beyond the standard library.
- Grading anything not expressible from the report text plus the sliced input (rewrite quality, severity calibration).

## Decisions

### D1. Layout

```
evals/
  keys/        sample-portfolio.json, sample-portfolio-2.json         (canonical keys)
  prompts/     portfolio.md, single-team.md                           (frozen templates)
  grader/      harness.py                                             (single stdlib CLI)
               selftest/  mini reports, corrupted keys, expected grades, the 9 scratch reports
  runs/        <batch>/batch.json
               <batch>/<arm>/<slice>/run-N/{prompt.md, report.md, run.json, grade.json}
               <batch>/scorecard.json, comparison.json                (committed)
               <batch>/<arm>/<slice>/input/ and <batch>/skill/<arm>/  (gitignored, regenerable)
               <batch>/<arm>/<slice>/run-N/scratch/                    (the runner's working files; gitignored via scratch/)
  scratch/     existing, stays gitignored
.claude/commands/okr-eval.md
```

Batch id: `<YYYY-MM-DD>-<tier>-<candidate-sha7>`; arms are `baseline` and `candidate` (a baseline batch has only `baseline`). *Alternative:* a sibling `okr-ninja-workspace/` as skill-creator prescribes — rejected, the repo's one-owner rule and the verify gate both want the harness inside the repo.

### D2. One CLI, seven subcommands

`python3 evals/grader/harness.py <cmd>`: `check` (key validation, anchor resolution, generated-section freshness, full-catalog coverage across keys), `render-key <fixture>` (regenerate the fixture's `## Answer key` section), `plan` (create the batch dir, slice inputs, export skill snapshots, write prompts and `batch.json`; skips runs whose report exists), `grade <run-dir>`, `aggregate <batch>`, `compare <batch>`, `selftest`. Exit codes 0/1 so the verify gate and a future headless wrapper can chain them. *Alternative:* one script per step — rejected for discoverability and shared parsing code.

### D3. Key schema

Extends the lost prototype's shape. Top level: `fixture`, `universe`, `budget`, `criterion`, `defects[]`, `non_defects[]`, `not_covered[]`, `slices{}`, `triage[]`.
- `defects[]`: `id` (G1…/A1…), `accepted[]` (primary first), `team` or `teams[]`, `evidence[]` of `{item}` or `{section}` with optional `optional: true`, `note`, optional `reference_overlap: {file, example}`.
- `non_defects[]`: `id` (N1…), `forbid[]`, `at[]` anchors (empty = anywhere), `note`.
- `slices{name}`: `team`, `mode`, `input_sections[]` (H2 heading prefixes kept), `expected[]` row ids, `budget`, `forbid_al`, `o4`, `note`.
- `triage[]`: `id` (T1…), `finding` (`AP-XX`/`AL-XX`), `anchor` (`{item}` or `{section}`), `bucket` ∈ {fixture-ambiguous, rubric-gap, skill-error}, `decision`, `rationale`, `status` ∈ {known-red, fixed}; `check` rejects skill-error + known-red and any entry without rationale.
Content on first authoring is transcribed from the current markdown keys; nothing is added or removed except the machine fields. *Alternative:* YAML — rejected, no stdlib parser.

### D4. Generated answer-key section

`render-key` rewrites everything from the `## Answer key (planted defects)` heading to end of file from the JSON: the defect tables, intentional non-defects, triage entries (new subsection beside non-defects), modes not covered, eval criterion, and slices. `check` fails when the file tail differs from the render. The first render must preserve today's wording row for row; a one-time formatting normalisation is acceptable and is reviewed in that diff. Hand edits below the heading are therefore impossible to keep — the JSON is where edits go, which is the point.

### D5. Slicing and anchors

`plan` writes the sliced input: fixture minus the answer-key section (and minus the intro's "see the answer key at the bottom" clause, as the previous session's inputs did); for a slice, only the H1 line plus the listed H2 sections. Anchors resolve against the *sliced input*: an item anchor's marker (`KR PL1.3`, `Objective D1`) must occur on exactly one line; a section anchor is a `## ` heading prefix. An evidence span's location is the input line where its normalised text occurs. Because keys carry markers, not line numbers, the same key grades full-fixture and sliced runs unchanged. Source-ref `line N` values are cross-checked against the located line and reported as a warning when they disagree (see Open Questions).

### D6. Parsing and quote classes

Findings split at `^### \[(Critical|Major|Minor)\] (AP|AL)-\d{2}` after normalising dashes (`—`, `–`, `-`) and arrows (`↔`, `<->`); a block runs to the next `##`/`###` heading. A quoted span (`"…"` or `“…”`) followed on the same line by a parenthesised source ref is an evidence span on evidence-labelled lines (`Evidence:`, `<Side> evidence:`, or a team/section name as label) and a supporting span elsewhere (why, conflict, detection and disconfirming checks, rewrite); any quoted span without a ref is a mention. Supporting spans satisfy anchors when located but are reported as unverified rather than fabricated when not — the scratch reports quote search terms and check names on those lines, and failing runs for them would punish documented disconfirming checks. Normalisation for matching: Unicode quotes/dashes → ASCII, whitespace collapsed, outer quotes and `*`/`_` emphasis stripped. Classes: verbatim, near-miss (trailing `.`/`…`/emphasis only), out-of-scope (in the original fixture, not in the sliced input), fabricated. Spans of fewer than three words that cannot be located are `term` (label and search words such as "aspirational" or "and" — never fabricated, never anchoring); a span occurring on several lines is located by the ref's line number and otherwise left unlocated and reported as ambiguous, so a repeated commitment line or a two-word phrase cannot anchor a finding to the wrong team. A span that matches the *answer-key section* of the original fixture is additionally flagged `key-leak` — a cheap tripwire for a run that read `examples/` despite the prompt.

### D7. Matching order

For each finding compute its anchor set (lines and sections hit by its evidence spans). Walk key rows in order: match when the finding's ID is accepted and every required anchor is satisfied; a row is claimed once. A finding whose anchors coincide with an already-claimed row is a duplicate of that row. Unmatched findings are extras, then flagged non-defect violation (forbidden ID at the non-defect's anchors, or anywhere when `at` is empty) or off-key (`not_covered`). Finally, triage entries with `status: known-red` mark matching extras/duplicates as excluded from the budget count. Partial matches (ID accepted, an anchor missing) are recorded with the missing anchor so a cross-source miss like G5 is diagnosable.

### D8. Orchestration through `/okr-eval`

The command file instructs the orchestrating session: parse `smoke [slice…]`, `baseline`, or `decision --baseline <git-ref> [--runs N]`; run `plan`; spawn one general-purpose Agent per pending run with the run's `prompt.md` as the task, at most five concurrent; after each Agent returns, write `run.json` (model, start, wall time, tokens from the usage line or null); then `grade` every run, `aggregate`, `compare` when two arms exist, and print the scorecard table plus any regression. The runner subagent follows `SKILL.md` unchanged, including fan-out; the prompt confines writes to the run directory. *Alternative:* a `claude -p` driver — deferred; `plan`/`grade`/`aggregate` are already shell-callable, so the wrapper is additive.

### D9. Arm snapshots

`plan` exports the baseline skill with `git archive <ref> SKILL.md references/ | tar -x -C runs/<batch>/skill/baseline/`; the candidate arm copies the working tree's `SKILL.md` and `references/` into `skill/candidate/` and records the HEAD SHA plus a dirty flag. Prompts point at the arm's snapshot, never at the repo root, so both arms are frozen for the batch's duration. *Alternative:* git worktrees — heavier, and the shared stash caveats apply.

### D10. Prompt templates

Derived from the scratch prompts, with placeholders for skill root, input path, report path and the mode's scope sentence. Kept verbatim: "the skill applies — do not decide whether it applies", "there is no user to ask", "the input file is the only source", "never publish or write a registry", "write nothing else", the local-file source-ref form, "reply with only the report path". The template hash (before placeholder substitution) is the `prompt_hash` in every grade and scorecard.

### D11. Scorecard and comparison

```json
{"harness_version": 2, "batch": "…", "tier": "decision", "prompt_hash": "…", "key_hashes": {"sample-portfolio": "…"},
 "arms": {"baseline": {"skill_sha": "…", "dirty": false, "model": "…",
   "slices": {"fixture1-portfolio": {"runs": 5, "pass": 1,
     "rows": {"G7": {"found": 5, "id_exact": 1, "caveat": null}},
     "extras": [{"key": "AP-10@Objective PL1", "runs": 5, "kind": "extra", "excluded": true, "bucket": "fixture-ambiguous"}],
     "violations": {"non_defect": 5, "off_key": 5}, "quotes": {"verbatim": 0, "near_miss": 0, "out_of_scope": 0, "fabricated": 0},
     "structure_pass": 5, "cost": {"tokens_mean": null, "tokens_max": null, "seconds_mean": 0}}}}},
 "comparison": {"regressions": [], "improvements": []}}
```
`compare` implements the regression rule from the spec (hit drop ≥ 2, new key in ≥ 3 candidate and < 3 baseline runs, any fabricated span) and refuses arms with different model IDs; improvements (mirror conditions) are listed for the record but gate nothing.

### D12. Verify-gate wiring

Replace the gate's fixture-eval bullet body with: run `/okr-eval smoke <slices>` for the slices whose keys cover the touched category (both fixtures for procedure-wide changes, the Platform slice when mode selection or single-team behaviour is touched); the fixture eval is green iff the harness reports pass. Keep the fixture-selection language, the docs-only skip, and the honesty rules ("report a borderline result rather than counting it green") untouched.

### D13. Self-tests

`selftest/` holds: the mini reports and corrupted key from the previous session's `evalcheck/` (recovered from that session's scratchpad), new minis for each quote class and for duplicates and known-red exclusion, and the nine scratch reports with their source-ref paths rewritten to the selftest input copies, each with an `expected.json` (row statuses, extras keys, quote-class counts, pass). `selftest` grades them all and diffs. Cases grade against frozen key snapshots under `selftest/keys/` (the live keys minus triage entries, plus a `_frozen` note), so a triage decision on the live key can never move a self-test expectation; the case that exercises known-red exclusion carries its own key copy with the entry.

### D14. Reference-overlap flags

Rows flagged in fixture 1's key: G1 (report-format §3 example "Ship checkout API v2 to GA"), G5 (§2 example's 99.95% trailing baseline), A1 (§4 example, step-up 90% vs conversion 58→68). A2 and A5 (the §1 and §6 examples mention Platform's implicit commitments and an inbound AL-01) are checked at apply time and flagged if the example text quotes or closely paraphrases the fixture's defect. *Decided at apply time:* A5 is flagged (the §1 example's "implicitly committed to work by two other teams" paraphrases the planted contention); A2 is not (the §6 example only names an inbound AL-01, with no defect text). The harness also gained a small `record` subcommand for writing `run.json`, so D2's count is eight subcommands.

## Risks / Trade-offs

- [Report-format drift breaks the parser] → dash/arrow/quote normalisation; "no findings parsed" is a structural failure, never a silent pass; parser cases in `selftest`.
- [A runner writes the report elsewhere or not at all] → `plan` marks a run without a report as *not produced*; it counts as a failed run in the scorecard, and the batch is resumable.
- [Quota runs out mid-batch] → resumable batches; smoke on gate, decision by hand.
- [The session model changes between arms or mid-batch] → model recorded per run; `aggregate` warns on mixed models within an arm; `compare` refuses mismatched arms.
- [Someone edits the fixture's key section by hand] → `check` fails on freshness; the CLAUDE.md file map states the JSON owns the key.
- [A runner subagent reads `examples/` and sees the key] → prompt forbids it, sliced inputs live outside `examples/`, and the `key-leak` quote flag catches quoted key text.
- [Near-miss tolerance hides sloppy quoting] → near-miss totals are on the scorecard, so a rise is visible even though it does not fail.
- [Token usage unavailable from the Agent usage line] → `null`, never a fabricated number; wall time is always recorded.
- [Committed reports bloat the repo] → about 6,000 lines per 30-run batch, accepted; sliced inputs and snapshots are not committed.
- [A folded secondary ID is invisible to the grader] → seen in the final smoke batch: the skill reported KR PL1.3 once, under AP-12, with "AP-04 confirmed as co-occurring" inside the block; the grader credits heading IDs only, so with T1 excluding the AP-12 finding, row G7 counts as missed. The content-fix change must define the secondary-ID field in the finding template and let the grader credit a secondary ID whose anchor matches — until then, T1 can convert a duplicate into a miss on runs that pick AP-12 as the primary.
- [A one-run smoke is red on a stochastic recall gap regardless of the change under test] → the baseline finds A1 (AL-02, step-up verification vs checkout conversion) in 2 of 5 fixture 1 runs because the taxonomy's metric-name blocking never pairs those KRs; a single smoke run therefore fails fixture 1 most of the time even for an unrelated edit. Options for the user, not decided here: fix the AL-02 candidate generation first (the unmerged surface-lever commit on the improvements branch targets it), add a symmetrical known-missed triage status for rows, or run the gate's smoke tier at three runs with a majority rule for rows.

## Migration Plan

1. Author `evals/keys/*.json` by transcribing the current markdown keys; run `check` (anchors resolve, catalog coverage holds).
2. `render-key` both fixtures; review the diff (formatting only); commit.
3. Build `harness.py` with `selftest` first, seeded from the recovered minis and the nine scratch reports; make it green.
4. Write the prompt templates and `/okr-eval`; run one smoke batch end to end.
5. Run the baseline batch (15 runs, single arm, at `main`), commit `evals/runs/<batch>/` with reports, grades and scorecard.
6. Seed triage entries for the recurring extras as **proposals** (bucket, rationale) for the user to confirm one by one; only confirmed entries get `known-red`.
7. Wire the verify gate, update `CLAUDE.md`, `README.md`, `.gitignore`.

Rollback: delete `evals/`, `.claude/commands/okr-eval.md`, and revert the gate bullet; the regenerated fixture sections remain valid markdown keys and need no revert.

## Open Questions

- Should a source-ref `line N` that disagrees with the located line become a failure later, once the baseline shows how often it happens? (Warning-only in this change.)
- Should near-miss quotes start counting against the budget after the content-fix change lands? (Reported-only in this change.)
- Whether A2 and A5 join the reference-overlap flags (decided at apply time by reading the examples, see D14).
- Concurrency cap of five: raise if the session tolerates it, lower if batches destabilise.
- Whether the verify gate's smoke tier should tolerate documented recall gaps (see the two risks above) until the content-fix change lands, or stay strictly red — a gate-policy decision for the user before archiving.
