## Context

See `proposal.md` — Why. Three constraints shape everything below:

1. **The contract is a decision procedure, not a rendering.** What `references/report-format.md`'s "Artifact lifecycle" section specifies is which of adopt / update / re-create / create fires, driven by a registry lookup and a URL verification — plus what gets written back and what must be said out loud.
2. **The grader is stdlib-only, deterministic, token-free.** Everything under `evals/grader/` grades from files on disk; nothing calls a model. The lifecycle eval must fit that, or it will not be run.
3. **The fixture exemption is load-bearing and was the subject of its own change** (`openspec/changes/archive/2026-09-10-generalize-fixture-publish-exemption/`). Its fixture arm must survive this change untouched.

## Goals / Non-Goals

**Goals:**
- Execute the contract's decision procedure end-to-end for the first time, with a real skill run making each decision.
- Fail loudly and specifically on each way the contract can be violated — above all a silent fork.
- Keep grading reproducible offline, with no external side effects and no cleanup.

**Non-Goals (design-level, beyond the proposal's):**
- No change to how OKR reports are graded; lifecycle grading is a separate command producing its own `grade.json` shape.
- No shared state between scenarios: each is independently seeded and independently runnable.
- No attempt to verify the real Artifact tool's semantics.

## Decisions

### D1 — Publish through a local seam, not the real artifact surface

The run prompt supplies `evals/lifecycle/publish_seam.py` as the publish target. The runner verifies with `read --url`, creates with `publish --key --title --favicon --file`, updates with `update --url --file`; the seam keeps a per-run JSON store with an append-only ledger.

*Why:* the seam preserves every decision point the contract specifies — the registry is still the source of truth, verification still gates update-vs-create, the never-fork rule still binds — while grading stays a file read. Real publishing would add: non-determinism (network, real URLs), external side effects on the user's account, cleanup of live artifacts after every batch, and a hard dependency on the runner having artifact tooling at all. The eval would then be un-runnable offline and un-rerunnable in CI, which is how deferred work stays deferred.

*What it does not cover, stated plainly:* the real Artifact tool's own semantics — that redeploying the same file path truly keeps the URL, that title and favicon truly persist across versions. Those are the tool's contract, not the skill's, and remain covered only by the tool. **The seam tests the decision, not the publish surface.**

*Alternative considered — real publishing behind a cleanup harness:* rejected on determinism and side effects. Revisit only if the update-in-place semantics themselves come into doubt.

### D2 — Narrow the exemption by naming the real artifact surface, not by dropping its eval arm

`references/report-format.md`'s "Fixture/eval exemption" today reads "any of this skill's own fixtures … and any eval run". The eval arm is restated as: no eval run touches the **real artifact surface** or writes a registry outside its own run directory; an eval run given a seam and a working folder executes the procedure against that seam.

*Why this is not a weakening:* the fixture arm is unchanged, word for word in scope — a fixture run publishes nothing even when a seam is supplied (spec scenario "A fixture run is exempt even when a seam is supplied"). The property the earlier change made load-bearing — an eval never reaches the user's artifacts — is unchanged. What changes is only that a *sandboxed* publish becomes expressible, which is what makes the contract testable at all.

*Alternative considered — leave the contract alone and frame the lifecycle runs as "not eval runs":* rejected as dishonest. They are eval runs; the prompts live in `evals/prompts/` and the harness plans them. A contract that only holds when you avoid saying the word "eval" is not a contract.

### D3 — Independently seeded scenarios, not a chained run-1-feeds-run-2

Each scenario's registry, seam store and prior-cycle output are seeded by `lifecycle-plan` from fixed values in `evals/lifecycle/scenarios.json`.

*Why:* the expected post-state is then exactly known (the seeded URL is a literal in the scenario file), scenarios can run in parallel and be re-run individually, and one flaky run cannot cascade. Chaining would test "run 2 sees run 1's registry", but the registry file is the interface either way — seeding it is the same interface with a known value.

### D4 — Grade the registry, the ledger, the summary and the working folder jointly

A scenario passes only when all four agree. `artifacts.json` alone cannot see a fork (a run could fork and still write a tidy registry); the ledger alone cannot see a stale registry; neither can see an unreported re-create.

To attribute ledger operations to deliverables, `publish`/`update` take `--key`. The seam is a test double, so recording the runner's stated key is fair game and makes the never-fork assertion exact rather than title-matched.

Grading also checks **what** was published, not merely that something was: each key's published content must hash-match that key's own declared file for this cycle. Without it a run could publish last cycle's file, or one file under both keys, and pass — the two cheapest ways to look correct while the living artifacts are wrong.

### D5 — The seam exposes no listing operation

The contract forbids deciding by artifact listing or title matching. Giving the seam a `list` command would hand the runner exactly the shortcut the contract bans. Verification is by URL only; a URL the store does not hold is dead.

### D6 — Seeded URLs use a reserved, non-routable host

Seeded and generated URLs are `https://artifacts.test/a/<id>` (`.test` is reserved by RFC 2606). A runner tempted to verify by fetching the URL cannot accidentally reach anything real, and the seam stays the only verification path.

### D7 — The re-create summary is graded on data-driven markers, not hardcoded English

The contract requires the run summary to state that a re-create happened **and why**. The scenario file supplies the accepted marker sets (one for "a re-create happened", one for the reason); grading is a normalised substring check against the run's `summary.md`. This keeps the check deterministic and keeps the wording requirement in data, where it can be widened without touching the grader.

### D8 — Two new subcommands, not an extension of the batch/scorecard machinery

`lifecycle-plan` and `lifecycle-grade` reuse the harness's utilities but produce their own grade shape and exit non-zero on failure. Folding lifecycle runs into `plan`/`aggregate`/`compare` would force a row/extra/quote model onto runs that have no findings to grade, and would drag the regression rule into a place it does not apply.

### D9 — Negative proof by breaking the skill, not by doctoring the output

To prove the eval fails on violation, the update scenario is re-run against a **mutated skill snapshot** — the batch's own regenerable, gitignored copy of `SKILL.md`, with Step 7 rewritten to publish a fresh artifact every run. That exercises the whole path (a real runner, really forking) rather than a hand-edited ledger. Deterministic per-violation coverage lives alongside it in the selftest corpus.

### D10 — A fixture-exempt counter-scenario, with a prompt that gives nothing away

The fixture arm of the exemption is the load-bearing guarantee, and it was in the same position this change exists to fix: asserted in prose, never executed. A fifth scenario supplies the identical seam and working folder but points at `examples/sample-portfolio.md`; a passing run publishes nothing, writes no registry anywhere, and says why.

Its prompt must not leak the answer, so every sentence that presupposes publishing is rendered from the scenario: the exemption note, the task tail, the `examples/` reading rule, the "publish that exact file" clause and the summary ask. The four publishing scenarios render byte-identically to what they always did, so their recorded evidence is unaffected.

## Risks / Trade-offs

- **A runner reads the seam's store instead of the registry** → the store lives in `<run_dir>/seam/`, outside the working folder; the seam exposes no listing; grading requires the registry to be correct independently.
- **A runner writes no summary** → the prompt names `summary.md` explicitly and the grader fails a scenario whose summary is missing, not just one whose wording is wrong.
- **The eval passes for the wrong reason (runner publishes nothing at all)** → every scenario asserts a positive: the expected ledger operation per key must be present, not merely the forbidden one absent.
- **Agent variance** (asks a clarifying question, writes outside the run dir, skips Step 7 because it reads "eval run" and stops) → the prompt states there is no user, confines writes to the run directory, and states that this run is seam-backed and therefore not publish-exempt. Residual variance shows up as a failing run, which is the correct signal, not a flake to paper over.
- **Seam realism drift** — if the real artifact surface ever gains a semantic the seam lacks, the eval could stay green while reality breaks. Mitigated only by D1's stated scope: this eval covers the decision, and the gate keeps the structural checks that cover the contract's presence.
- **Cost** — five subagent runs per lifecycle batch. Mitigated by the conditional gate tier (publish-path changes only) and a deliberately small two-team corpus.

## Migration Plan

Additive. New files under `evals/corpora/`, `evals/lifecycle/`, `evals/prompts/`; new subcommands; edits to the exemption paragraph in `references/report-format.md`, `SKILL.md` Step 7, `verify-gate.md`, `.claude/commands/okr-eval.md`, `CLAUDE.md` and `README.md`. `.gitignore` needs no new entry: a lifecycle run's working folder and seam store are graded evidence and are committed (as `report.md` is for a report run), and the only regenerable artefact — the skill snapshot — is already covered by `evals/runs/**/skill/`. No existing batch, fixture, key or report format changes, so every committed batch under `evals/runs/` stays valid and `check`'s existing output is unchanged. Rollback is deleting the new files and reverting the exemption paragraph.
