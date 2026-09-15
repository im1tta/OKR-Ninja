# Run summary — Tidewell Q3 2026 portfolio review (cycle date 2026-09-14)

Mode: **portfolio** (2 teams in confirmed scope: Ledger, Onboarding). Corpus: `evals/corpora/tidewell-q3.md` (not a skill fixture, so the run is not publish-exempt). A publish seam and a working folder were supplied, so the "Artifact lifecycle" decision procedure ran in full, with `work/artifacts.json` as the registry.

## Published deliverables

| Key | File published | URL | Registry action |
|---|---|---|---|
| `portfolio-dashboard` | `work/2026-09-14-portfolio-review.md` | https://artifacts.test/a/fbac94f1 (**new**) | **Re-create** — registered URL was dead; entry overwritten with the new URL |
| `team-report/ledger` | `work/2026-09-14-ledger-report.md` | https://artifacts.test/a/b4e2d118 (unchanged) | **Update in place** — entry valid; title and favicon left exactly as registered |

## Registry actions, in order

1. **Adopt** — no artifact URL was supplied for either deliverable, so nothing was adopted.
2. **Read** — `work/artifacts.json` already held both keys: `portfolio-dashboard` → `https://artifacts.test/a/0dead0dd` (title "Tidewell OKR Portfolio Review", favicon 🧭, last published 2026-06-15) and `team-report/ledger` → `https://artifacts.test/a/b4e2d118` (title "Ledger Team OKR Report", favicon 📒, last published 2026-06-15).
3. **Verify** — `read --url https://artifacts.test/a/0dead0dd` returned exit 3, `{"ok": false, "reason": "no such artifact"}`. `read --url https://artifacts.test/a/b4e2d118` returned exit 0: reachable, title "Ledger Team OKR Report".
4. **Act — `portfolio-dashboard`: a create was performed while an entry existed, and this is why.** The registered URL failed verification (dead artifact), which is the decision procedure's "entry dead or un-updatable → re-create" branch: `publish --key portfolio-dashboard --title "Tidewell OKR Portfolio Review"` returned the new URL `https://artifacts.test/a/fbac94f1`. The dead entry was overwritten with that URL rather than a second entry being added — no fork. Title and favicon were carried over from the dead entry so the deliverable keeps its identity across the re-create.
5. **Act — `team-report/ledger`:** entry valid → `update --key team-report/ledger --url https://artifacts.test/a/b4e2d118`, which kept the URL (artifact now at version 2). `--title`/`--favicon` were deliberately not passed, so both stay exactly as registered.
6. **Refresh** — both entries rewritten with `last_published` and `cycle_date` for this cycle (2026-09-14); `portfolio-dashboard` also carries its new `url`.

No artifact was created for a key that already had a live entry, no second artifact exists for any key, and nothing outside this run directory and the named seam store was written. The prior cycle's `work/2026-06-15-portfolio-review.md` was left untouched (history is append-only); this run's outputs are new dated files beside it.

## Review result (for context)

0 Critical, 5 Major, 1 Minor. Worst alignment risk: AL-06 Timeline mismatch (Ledger assumes the bank-link connector "lands from Onboarding in July", Onboarding commits "by Aug 29"); most common goodness anti-pattern: AP-01 Task Masquerading as KR (both teams). Roll-ups: Ledger B (2.86), Onboarding B (3.09) — no team qualified for a single-team-mode re-run.
