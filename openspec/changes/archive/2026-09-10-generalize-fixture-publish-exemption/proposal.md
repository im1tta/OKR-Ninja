## Why

The artifact publish exemption names one fixture. `SKILL.md` Step 7 and `references/report-format.md` both exempt "runs against `examples/sample-portfolio.md` or any eval", and `openspec/specs/artifact-lifecycle/spec.md` says the same thing as "a run against the test fixture (`examples/sample-portfolio.md`) or any eval run" — all written when `examples/sample-portfolio.md` was the only fixture. `examples/sample-portfolio-2.md` has existed since `434c4e8` and is named in none of them.

The trailing "or any eval" saves harness-driven runs, and `evals/prompts/*.md` independently instruct "never publish artifacts and never create or modify any registry file," so `/okr-eval` was never exposed. The gap is the **hand-typed** fixture run — demoing the skill, or spot-checking a change without the harness — where a user types something like "review the OKRs in `examples/sample-portfolio-2.md`" and never says "eval." Against fixture 2 that run matches no enumerated exemption, and an enumerated list invites the reading that the fixture it omits is not covered. A hermetic-run guarantee should not depend on the prompt remembering to restate it.

## What Changes

- The exemption covers **any of this skill's own fixtures**, plus any eval run, instead of one named file — in the spec requirement and its scenarios, `SKILL.md` Step 7, and `references/report-format.md`'s "Fixture/eval exemption" line.
- The scope phrase is identical across the three so the one-owner rule holds: the spec states the requirement, `references/report-format.md` owns the contract text, `SKILL.md` points at it.
- The test is the corpus, not its path: a fixture is exempt whether read from an installed skill, a symlink or a working checkout, and a user's own OKR exports are never exempt — including when they sit in a folder the user happens to call `examples/`.
- No behavior changes for any run that was already exempt. Not breaking.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `artifact-lifecycle`: the "Fixture and eval runs never publish" requirement changes scope from the single named fixture to any of the skill's own fixtures, tested by corpus rather than by path.

## Impact

- `openspec/specs/artifact-lifecycle/spec.md` — requirement text, its existing scenario reworded, and three added scenarios (hand-typed run against a checkout fixture, fixture added later, user's own exports in a folder named `examples/`). Synced from the delta at archive time.
- `SKILL.md` — Step 7 (publish), one sentence. Stays well under the ~150-line cap.
- `references/report-format.md` — the "Fixture/eval exemption" line in the Artifact lifecycle section.
- No change to the registry schema, the publish decision procedure, the recovery paths, or `evals/`. The harness's `check` and `selftest` are unaffected; no answer key, planted defect, or budget moves.

Detection behavior is untouched, so the change should newly catch no planted defect in either fixture — the proposal rule's disclosure requirement is satisfied vacuously, and the fixture eval exists here to prove nothing regressed rather than to demonstrate a new catch.

## Non-goals

- Not implementing the deferred artifact-lifecycle behavioral eval (pre-seeded `artifacts.json`, second run must update in place) — it stays future work in `verify-gate.md`.
- Not changing the registry schema, deliverable keys, or the adopt/read/verify/act/refresh procedure.
- Not touching the fixture-1 references that are legitimately specific: the `alignment-detection` spec's Brightledger AL-07 scenario, and `eval-fixtures`' Platform single-team slice and name-collision check.
- Not restating the exemption anywhere new, and not adding a fixture allowlist that a third fixture would strand again.
