# Run summary — Tidewell Q3 2026 portfolio review (cycle date 2026-09-14)

Mode: **portfolio** (2 teams in confirmed scope: Ledger, Onboarding). Corpus: `evals/corpora/tidewell-q3.md` (the only source read for OKR content). Strategy source: that file's "Company Q3 2026 priorities" section. No Atlassian connection was available; the publish seam stood in for the artifact surface, and the registry is `adopt/work/artifacts.json`.

## What was published

| Key | File published | URL | Registry action |
|---|---|---|---|
| `portfolio-dashboard` | `adopt/work/2026-09-14-portfolio-review.md` | https://artifacts.test/a/9f3b77c4 | **Adopted** the user-supplied URL (overwrote the prior entry), then **updated in place** |
| `team-report/ledger` | `adopt/work/2026-09-14-ledger-report.md` | https://artifacts.test/a/b4e2d118 | **Updated in place** at the registered URL |

**No artifact was created this run.** Both deliverables landed on existing artifacts via update, so there was nothing to report under the "create while an entry existed" rule, and no key forked.

## Registry actions, in the order the decision procedure ran

**`portfolio-dashboard`**

1. **Adopt.** The user supplied https://artifacts.test/a/9f3b77c4 for this key and asked that it be kept. Per step 1 of the publish decision procedure, that URL was recorded under the key, overwriting the prior entry — which pointed at a *different* artifact, https://artifacts.test/a/51aa9c6e ("Tidewell OKR Portfolio Review", last published 2026-06-15). The user-supplied URL takes precedence over the registry's stored URL; the registry is the source of truth for update-vs-create, not for overriding an explicit instruction.
2. **Read.** Key present; registered URL after adopt = 9f3b77c4.
3. **Verify.** `read --url https://artifacts.test/a/9f3b77c4` → exit 0, alive, title "Tidewell OKR Dashboard (shared with leads)", favicon 🧭.
4. **Act.** Entry valid → **update in place**. Title and favicon were deliberately **not** passed, so the adopted artifact keeps its own name and emoji — the deliverable moved to the user's artifact, the user's artifact was not renamed to the deliverable. Result: versions 1 → 2.
5. **Refresh.** Entry rewritten with the adopted URL, its live title/favicon (so the registry matches reality), `last_published` 2026-09-15T08:47:37Z, `cycle_date` 2026-09-14.

**`team-report/ledger`**

1. **Adopt.** Not applicable — the user supplied no URL for this key.
2. **Read.** Key present → https://artifacts.test/a/b4e2d118.
3. **Verify.** `read --url https://artifacts.test/a/b4e2d118` → exit 0, alive, title "Ledger Team OKR Report", favicon 📒.
4. **Act.** Entry valid → **update in place**, title and favicon unchanged. Result: versions 1 → 2.
5. **Refresh.** `last_published` 2026-09-15T08:47:37Z, `cycle_date` 2026-09-14.

### What happened to the superseded artifact

https://artifacts.test/a/51aa9c6e — the previous `portfolio-dashboard` URL — was **left untouched**: it was read once for context (alive, still at version 1) and never published to. It is no longer referenced by the registry. Nothing was deleted; if a bookmark or the CEO page still points at it, that artifact now holds only the Q2 cycle's content, which is worth flagging to the user since the two dashboards have similar names.

### Seam calls made (in order)

`read` 9f3b77c4 (alive) · `read` b4e2d118 (alive) · `read` 51aa9c6e (alive, context only) · `update` portfolio-dashboard → 9f3b77c4 · `update` team-report/ledger → b4e2d118. No `publish` call was made.

## Review outcome (detail in the published report)

Verdict **At risk** — 1 Critical, 6 Major, 1 Minor. The Critical is AL-06 Timeline mismatch: Ledger's committed KR L1.2 assumes the bank-link connector lands "in July" while Onboarding's only quoted date for it is Aug 29. Most common goodness anti-pattern: AP-01 Task Masquerading as KR (one per team). Roll-ups: Onboarding C (2.40), Ledger B (2.76); neither is at or below the needs-rework threshold, so both §6 re-run recommendations rest on criterion (b) — each team is a named party to the Critical finding.

Two judgment calls worth recording, both made on the evidence-discipline rules rather than on impression:

- **AP-06 Sandbagged Target was not filed** against Ledger's "Hold billing run success rate at or above 99.7% through Q3." No baseline for that metric exists anywhere in the corpus, and a sandbag claim requires quotes from both ends; the deficiency is recorded as AP-04 KR Without Baseline with K3 taking the rubric's unverifiable-calibration cap.
- **AP-13 Ambiguous Denominator (Critical) was considered and dropped** on two percentage KRs (Ledger's "85% of transactions", Onboarding's "share of clinics reaching first paid visit within 14 days"). Both name a population and both state a current value, which is evidence a measurement already exists — so "any number can be claimed" does not follow from the quotes. They are reflected in K1/K5 scores instead.

## Files written (all inside `adopt/`)

- `adopt/work/2026-09-14-portfolio-review.md` — full six-section portfolio report (new dated cycle file)
- `adopt/work/2026-09-14-ledger-report.md` — Ledger slice of the same run (new dated cycle file)
- `adopt/work/artifacts.json` — registry, refreshed
- `adopt/summary.md` — this file

The prior cycle's `adopt/work/2026-06-15-portfolio-review.md` was not modified, per the append-only history rule. The corpus was not modified. Nothing outside `adopt/` was written except the seam store named in the prompt.
