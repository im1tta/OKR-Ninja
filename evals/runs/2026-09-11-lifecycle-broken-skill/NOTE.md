# Negative proof — the lifecycle eval goes red when the contract is violated

An eval that only ever passes proves nothing. This batch is the counter-test for
`evals/runs/2026-09-11-lifecycle-6115de2` (five scenarios, all green): the **same** `update`
scenario, the **same** seeded registry and seam store, run against a **deliberately broken skill**.

## How it was produced

1. `lifecycle-plan --scenarios update --batch 2026-09-11-lifecycle-broken-skill` — this batch's own
   snapshot of the skill was taken as usual (`<batch>/skill/candidate/`, regenerable and gitignored).
2. That snapshot — and only that snapshot — was then mutated:
   - `SKILL.md` Step 7 rewritten to "publish each report deliverable as a **fresh artifact** … Do not
     look for, read, or write any registry file, and never try to update an existing artifact".
   - `references/report-format.md`'s "Artifact lifecycle" section replaced with "**Publish fresh every
     run.** There is no registry and no update path."
3. One fresh subagent ran that broken skill against the scratch corpus with the prompt verbatim.

The repository's real `SKILL.md` and `references/report-format.md` were never touched. Re-planning this
batch regenerates a **clean** snapshot from the working tree, so re-running it will not reproduce the
failure unless the mutation is applied again.

## What the run did, and what the grader said

The broken skill created a second artifact for each of the two registered keys and never opened the
registry: the seam ledger holds two `publish` operations and no `update`, the seam ends with four
artifacts (two seeded, two forked), and `work/artifacts.json` still carries the June entries.

`lifecycle-grade` failed the run and exited 1, naming every violation (see `update/grade.json`):

```
FAIL | update | creates 2 updates 0
  portfolio-dashboard — cycle_date_current: cycle_date is '2026-06-15', expected '2026-09-14'
  portfolio-dashboard — registered_url_verified: acted on portfolio-dashboard without verifying https://artifacts.test/a/7c1f9a20 through the seam first
  portfolio-dashboard — no_fork: created 1 artifact(s) for a key that had a registry entry: https://artifacts.test/a/dda52846
  portfolio-dashboard — updated_in_place: no update recorded for this key
  portfolio-dashboard — timestamp_advanced: last_published '2026-06-15T10:04:00Z' does not advance on '2026-06-15T10:04:00Z'
  team-report/ledger — cycle_date_current: cycle_date is '2026-06-15', expected '2026-09-14'
  team-report/ledger — registered_url_verified: acted on team-report/ledger without verifying https://artifacts.test/a/b4e2d118 through the seam first
  team-report/ledger — no_fork: created 1 artifact(s) for a key that had a registry entry: https://artifacts.test/a/37746ceb
  team-report/ledger — updated_in_place: no update recorded for this key
  team-report/ledger — timestamp_advanced: last_published '2026-06-15T10:06:00Z' does not advance on '2026-06-15T10:06:00Z'
  create_over_entry_reported: a create happened while a registry entry existed (portfolio-dashboard@https://artifacts.test/a/dda52846, team-report/ledger@https://artifacts.test/a/37746ceb); the run summary never says a re-create happened
```

Every failure above is a check the grader would also raise on its own: the run forked both keys **and** never
consulted the registry, so it fails wide. The tight counterfactual — a fork behind an otherwise correct registry —
is pinned in the self-test corpus.

Per-violation coverage is pinned deterministically in the grader's self-test corpus
(`evals/grader/selftest/cases/lifecycle-*`), including a fork hidden behind a tidy registry.
