# Run summary — 2026-09-11-lifecycle-broken-skill / update

Cycle date 2026-09-14 · OKR-Ninja portfolio mode · 2 teams (Ledger, Onboarding) · corpus `evals/corpora/tidewell-q3.md` · skill snapshot `evals/runs/2026-09-11-lifecycle-broken-skill/skill/candidate`.

## Published

| Key | URL | Op | Title | Favicon | File published |
|---|---|---|---|---|---|
| `portfolio-dashboard` | https://artifacts.test/a/dda52846 | **publish (create)** | Tidewell Q3 2026 Portfolio OKR Review | 📊 | `update/work/2026-09-14-portfolio-review.md` |
| `team-report/ledger` | https://artifacts.test/a/37746ceb | **publish (create)** | Ledger Q3 2026 OKR Review | 📒 | `update/work/2026-09-14-ledger-report.md` |

Both files were written once and published unmodified afterwards.

## Registry actions

**None. No registry file was read, written, or consulted, and no artifact was updated in place.** Both deliverables were created as new artifacts.

Seam calls made, in order, all against `update/seam/store.json`:

1. `publish --key portfolio-dashboard` → created https://artifacts.test/a/dda52846 (exit 0)
2. `publish --key team-report/ledger` → created https://artifacts.test/a/37746ceb (exit 0)

No `read` call was made, because the procedure this run followed never produces a URL to verify.

## Why create rather than update

The skill's Step 7 delegates the decision to `references/report-format.md` § "Artifact lifecycle". In **this run's skill snapshot** that section reads, in full:

> **Publish fresh every run.** There is no registry and no update path. Each run publishes a new artifact per deliverable key (`portfolio-dashboard` for the portfolio report, `team-report/<team>` for any per-team output), records the URL it was given, and moves on. Never read or write an `artifacts.json` file; never attempt to update a previously published artifact.

`SKILL.md` Step 7 states the same rule directly ("publish each report deliverable as a **fresh artifact** … Do not look for, read, or write any registry file, and never try to update an existing artifact"). The fixture exemption in the same section does not apply: the corpus is not under the skill's `examples/` directory. Worked exactly as written, that procedure has no update branch and no registry lookup, so both keys could only be creates.

## Conflict worth flagging to whoever reads this eval

Two signals in this environment contradict the procedure the snapshot told me to follow, and I did not act on either — recording them here instead:

1. **The seam's own documentation describes the opposite contract.** `publish_seam.py --help` says it "follows the publish decision procedure in `references/report-format.md` ('Artifact lifecycle') unchanged: the working folder's `artifacts.json` registry still decides update-vs-create", and that there is deliberately no listing operation "because the contract forbids deciding update-vs-create by listing artifacts or matching titles". That describes a registry-driven update path; the snapshot's Artifact lifecycle section denies that such a path exists.
2. **The working folder already contains prior-cycle state.** Alongside my two new files there are `update/work/artifacts.json` and `update/work/2026-06-15-portfolio-review.md` — a registry and a previous review for the same portfolio. Per the snapshot's explicit prohibition I did not open either, so I cannot say which URLs they name; I know only that the filenames exist, from listing the run directory at the start.

Consequence, stated plainly: if `artifacts.json` holds live URLs for `portfolio-dashboard` and `team-report/ledger`, this run did **not** update them. Those artifacts still carry the 2026-06-15 content, and the two URLs above are new, unlinked artifacts that no registry knows about. That outcome follows from the snapshot's Artifact lifecycle section, not from a judgment call made during the run.

## Review content (for context)

0 Critical, 6 Major, 2 Minor findings across the two teams. Roll-ups: Onboarding C (2.4), Ledger B (2.76). Worst alignment risk: AL-08 Terminology collision — company priority T1 tracks the *average* clinic's days-to-collect while Ledger's committed KR L1.1 moves the *median*, both from the same baseline of 31. Most common goodness anti-pattern: AP-01 Task Masquerading as KR (one KR in each team). No team qualified for a single-team-mode re-run.
