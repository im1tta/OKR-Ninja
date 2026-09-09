# Platform team — Q3 2026 OKR review (single-team mode)

- **Team in scope:** Platform (confirmed; exactly one team → single-team mode, full-depth goodness review, no cross-team analysis)
- **Period:** Q3 2026, as stated by the source page ("Platform team — Q3 2026")
- **Source:** `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md` — local export of "Source: Confluence page 88221 (PLAT-OKR-Q3)" ("Last updated 2026-07-05") plus a Q2 2026 business-review appendix. No Atlassian connection; no other file consulted for OKR content.
- **Strategy doc:** none provided — company-level strategy tracing was out of scope; O4 is scored N/A per the rubric (see §2).
- **Run note:** eval run — the publish step (Step 7) was skipped; no artifact or registry was created or modified.

## 1. Verdict summary

**Verdict: At risk.** Platform's Q3 2026 OKRs roll up to **C (2.5)** — above the rubric's needs-rework threshold (D), but 3 of the 5 KRs carry a Major anti-pattern and one committed KR cannot be scored mid-quarter at all.
Findings: **0 Critical · 4 Major · 0 Minor** (2 objectives and 5 KRs scored exhaustively).
Worst finding: **AP-02 Binary KR with No Gradient** — "Complete the SOC 2 Type II audit." is done/not-done, yet the page says the quarter's capacity is committed to it, so the team's largest bet has no progress signal.
Runner-up: **AP-06 Sandbagged Target** — the committed uptime target (≥ 99.9%) sits below the 99.95% trailing actual quoted in the Q2 review; the KR is met on day one.
KR PL1.3 (developer satisfaction) carries two findings: no baseline anywhere in the corpus (**AP-04 KR Without Baseline**) and no causal link to "Keep the lights on, cheaper" (**AP-12 Orphan KR**).
Company-level strategy tracing was out of scope: no strategy document was provided, so O4 Strategic Anchoring is N/A for both objectives and excluded from the roll-up (gap recorded in §2).
Single-team mode: no AL-XX analysis was run; one outbound dependency note is recorded in §4.
Recommended first action: rewrite PL2.2 as a graded KR over the SOC 2 evidence backlog with a report date — owner: Elena R. (page owner) (§3 AP-02 Binary KR with No Gradient).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.5)** — PL1 C (2.4, capped: ≥ 2 Major anti-patterns on one OKR) · PL2 C (2.5).
- Platform: K1=2 / K3=2 / K5=2 — a binary KR (K1=0), a sandbagged uptime target (K3=1), and no metric source named on four of five KRs.

**O4 = N/A — gap note (rubric O4 rule, no strategy source in corpus):** no company/portfolio strategy document was provided, and none exists inside the source file (search trail: the entire file, lines 1–23; the only headings are "Brightledger — Q3 2026 OKRs (portfolio export)" line 1, "Platform team — Q3 2026" line 3, the two objective headings lines 7 and 12, and "Appendix — Q2 2026 business review (extracts)" line 18; no line contains strategy, priority, pillar, bet, or company-goal text). Neither objective states a parent link in its own text — "Objective PL1: Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`) and "Objective PL2: Earn enterprise trust" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`); parent recorded as null for both. O4 is excluded from every mean; the strategy-based team cap does not apply. Company-level strategy tracing was out of scope for this run and should be re-done once a strategy page is supplied.

### Per-instance breakdown

Source refs below use the form `<file> › <heading> › line N`; `<file>` is `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md` in every ref.

**Objectives**

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

- PL1 O1=3 — "Keep the lights on, cheaper" (`<file> › Objective PL1: Keep the lights on, cheaper › line 7`): outcome-framed with no delivery verb and no named solution, but the first clause "Keep the lights on" describes a maintained state, not a changed end-state.
- PL1 O2=3 — "Keep the lights on, cheaper" (`<file> › Objective PL1: Keep the lights on, cheaper › line 7`): short, plain, metric-free; the subject is the idiom "the lights" — which systems it covers is unstated.
- PL2 O1=4 — "Earn enterprise trust" (`<file> › Objective PL2: Earn enterprise trust › line 12`).
- PL2 O2=3 — "Earn enterprise trust" (`<file> › Objective PL2: Earn enterprise trust › line 12`): short and plain; what enterprises would observably do differently is unspecified in the objective text.
- PL1 and PL2 O3=3 — period inherited unambiguously from "Platform team — Q3 2026" (`<file> › Platform team — Q3 2026 › line 3`), not restated in either objective.
- O4 — N/A for both (gap note above).

**Key results** (K1–K5 per KR; per-KR score = mean)

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." | 2 | 4 | 2 | 3 | 2 | 2.6 |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 "Complete the SOC 2 Type II audit." | 0 | 1 | 2 | 3 | 2 | 1.6 → **1.0** (K1=0 cap) |

- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (`<file> › Objective PL1: Keep the lights on, cheaper › line 8`): no baseline on the OKR page; retrievable from "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`<file> › Appendix — Q2 2026 business review (extracts) › line 21`); measurement window unstated on the KR.
- PL1.1 K3=1 — same two quotes: target (≥ 99.9%) is below the quoted trailing actual (99.95%) → sandbag (§3 AP-06 Sandbagged Target).
- PL1.1 K5=3 — the KR names no source, but the corpus names the system of record for this metric: "Datadog SLO monitor" (`<file> › Appendix — Q2 2026 business review (extracts) › line 21`).
- PL1.2 K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`<file> › Objective PL1: Keep the lights on, cheaper › line 9`): metric, numeric baseline, numeric target and unit present; measurement window (monthly average, quarter-end run rate, or other) unstated.
- PL1.2 K3=3 — same quote, committed by the page convention "KRs are committed unless marked (aspirational)." (`<file> › Platform team — Q3 2026 › line 5`): a modest, properly-labeled committed stretch; no trend exists in the corpus to justify or test it.
- PL1.2 K5=2 — same quote: no billing or transaction system of record is named, and the only system named anywhere in the corpus is "Datadog SLO monitor" (`<file> › Appendix — Q2 2026 business review (extracts) › line 21`), which does not report spend.
- PL1.3 K1=2 — "Improve internal developer satisfaction score to 8/10." (`<file> › Objective PL1: Keep the lights on, cheaper › line 10`): target without baseline, none retrievable (§3 AP-04 KR Without Baseline).
- PL1.3 K3=2 — rubric cap: no baseline or trend anywhere in the corpus (search trail in §3 AP-04) — calibration unverifiable.
- PL1.3 K5=2 — same quote: the survey/instrument behind the "score" is unnamed; different instruments would give different numbers.
- PL2.1 K1=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`<file> › Objective PL2: Earn enterprise trust › line 13`): metric, numeric baseline (7 open), numeric target and unit present; measurement window unstated.
- PL2.1 K2=3 — same quote: closed findings is a proxy output; its outcome link is stated only through the objective "Earn enterprise trust" (`<file> › Objective PL2: Earn enterprise trust › line 12`).
- PL2.1 K3=3 — same quote plus "KRs are committed unless marked (aspirational)." (`<file> › Platform team — Q3 2026 › line 5`): committed KR at modest stretch (7 → 0 open); no trend in the corpus.
- PL2.1 K5=2 — same quote: no pen-test report or tracker named as the system of record.
- PL2.2 K1=0 — "Complete the SOC 2 Type II audit." (`<file> › Objective PL2: Earn enterprise trust › line 14`): pure done/not-done milestone (§3 AP-02 Binary KR with No Gradient).
- PL2.2 K2=1 — same quote: a delivery milestone, not a measured result.
- PL2.2 K3=2 — rubric cap: no baseline, scale, or trend — calibration unverifiable.
- PL2.2 K5=2 — same quote: no source named; the auditor's report would be the obvious record but nothing in the corpus names it.
- K4=3 on all five KRs — the team is named by "Platform team — Q3 2026" (`<file> › Platform team — Q3 2026 › line 3`) and an individual is derivable from the page-level "Owner: Elena R." (`<file> › Platform team — Q3 2026 › line 4`), but no KR names its own accountable individual.
- K2=4 on PL1.1, PL1.2 and PL1.3 — the quoted KR texts measure results experienced outside the team (availability, unit cost, internal developers' satisfaction).

**KR sets** (K6, K7 once per set)

| Set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1, PL1.2, PL1.3) | 2 | 2 |
| PL2 (PL2.1, PL2.2) | 2 | 3 |

- PL1 K6=2 — all three KRs are lagging end-of-period truths — "Maintain API uptime at or above 99.9%." (line 8), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9), "Improve internal developer satisfaction score to 8/10." (line 10; all `<file> › Objective PL1: Keep the lights on, cheaper`) — none is a leading indicator that predicts another.
- PL1 K7=2 — one orphan KR: "Improve internal developer satisfaction score to 8/10." (`<file> › Objective PL1: Keep the lights on, cheaper › line 10`) serves a different goal than "Keep the lights on, cheaper" (`<file> › Objective PL1: Keep the lights on, cheaper › line 7`) (§3 AP-12 Orphan KR); the other two KRs cover the objective's two facets.
- PL2 K6=2 — both KRs are leading proxies of trust — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) and "Complete the SOC 2 Type II audit." (line 14; both `<file> › Objective PL2: Earn enterprise trust`) — with no lagging KR measuring trust as enterprises experience it.
- PL2 K7=3 — one coverage gap: nothing in the set observes "Earn enterprise trust" (`<file> › Objective PL2: Earn enterprise trust › line 12`) from the enterprise side (deals, security-review outcomes, renewals).

**Roll-up arithmetic** (rubric Part 3; O4 excluded as N/A)

- PL1 = 0.35 × mean(O1..O3 = 3.00) + 0.45 × mean(2.8, 3.0, 2.6 = 2.80) + 0.20 × mean(K6=2, K7=2 = 2.00) = 1.05 + 1.26 + 0.40 = **2.71** → cap 3 (≥ 2 Major anti-patterns on one OKR: AP-06, AP-04, AP-12) → **2.4 → C**.
- PL2 = 0.35 × mean(O1..O3 = 3.33) + 0.45 × mean(2.8, 1.0 = 1.90) + 0.20 × mean(K6=2, K7=3 = 2.50) = 1.17 + 0.86 + 0.50 = **2.52 → C**. (One confirmed Major, AP-02; the co-triggered AP-01 on the same span, if counted as a second Major, would cap PL2 at 2.4 — still C.)
- Team = mean(2.4, 2.52) = **2.46 → C (2.5)**. Team caps: K1 ≤ 1 on 1 of 5 KRs (not more than half) — not triggered; strategy-traceability cap — N/A (no strategy corpus). Needs-rework threshold (D or below) — not reached; no Critical finding.
- Team dimension integers (mean of scored instances, rounded down): O1 3.5→3 · O2 3 · O3 3 · O4 N/A · K1 2.2→2 · K2 3.2→3 · K3 2.2→2 · K4 3 · K5 2.2→2 · K6 2 · K7 2.5→2.

## 3. Findings

Ordered by severity (all Major; worst impact first). Every rewrite is OKR-Ninja's proposal; numbers not quoted from the corpus appear as `<placeholder>` or carry the tag [proposal — placeholder target].

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
- Why it's a problem: done/not-done phrasing with no numeric scale — mid-quarter the KR can only score 0% or 100%, so the work the page says absorbs most of Q3's capacity carries no progress signal and no partial credit. The leading verb "Complete" with no metric and no baseline→target pair also fires AP-01 Task Masquerading as KR on the same span (co-occurring, same root cause; not counted as a separate finding).
- Scores affected: K1=0 (per-KR score capped at 1.0), K2=1, K3=2 (calibration unverifiable — no scale); PL2 roll-up 2.52.
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence requests closed `<current count>`/`<N>` → `<N>`/`<N>` (baseline recorded at the page's last update), auditor fieldwork complete and the Type II report received by `<date>` — source: `<audit-evidence tracker>`." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
- Why it's a problem: the committed target (at or above 99.9%) sits below the trailing-90-day actual (99.95%) quoted in the Q2 review, so the KR is already met and encodes no delta — the definition of AP-06 Sandbagged Target. The "Maintain" phrasing describing the team's standing duty, with the page allotting no Q3 work to it, also fires AP-10 BAU Dressed as OKR on the same span (co-occurring, same root cause; not counted as a separate finding).
- Scores affected: K3=1; K1=3 (baseline retrievable only from the appendix; window unstated); contributes to the PL1 roll-up cap at 2.4.
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% (trailing 90 days, per the Q2 review) → ≥ `<target above 99.95>`% over the Q3 trailing-90-day window, per Datadog SLO monitor." [proposal — placeholder target] If the team does not intend to raise availability this quarter, instead move uptime out of the OKRs into a health-metric floor ("API uptime floor 99.9%, Datadog SLO monitor") and use the KR slot for a reliability delta the team will actually work.

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: a target ("to 8/10") with no starting point and none retrievable anywhere in the corpus — the search covered the whole input file (lines 1–23: every numeric figure is on lines 8, 9, 10, 13, 21, 22 and 23, and the only Platform figure in the Q2 review appendix is the uptime line), so neither ambition nor progress can be judged. The score's instrument (which survey, sample, cadence) is also unnamed, so two readers could report different numbers.
- Scores affected: K1=2, K3=2 (rubric cap — calibration unverifiable), K5=2; contributes to the PL1 roll-up cap at 2.4.
- Suggested rewrite: "KR PL1.3: Internal developer satisfaction score `<current value>`/10 (last survey, `<instrument>`, n = `<n>`) → 8/10 on the same instrument, end-of-Q3 survey." [proposal — placeholder target] (8/10 is reused from the source; if the KR is relocated per AP-12 below, carry this form with it.)

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence: "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Why it's a problem: hitting the KR would not move the objective — "developer satisfaction" shares no noun or domain with "lights on" (availability) or "cheaper" (cost), and no causal chain from a higher satisfaction score to either outcome is stated on the page or reachable in ≤ 2 steps; the KR serves a different, unstated developer-experience goal, which is the definition of AP-12 Orphan KR.
- Scores affected: K7=2 for the PL1 set (one orphan KR); contributes to the PL1 roll-up cap at 2.4.
- Suggested rewrite: replace PL1.3 with a KR that predicts PL1's own outcomes — "KR PL1.3: `<API incident count or change-failure rate>` `<baseline>` → `<target>` per Datadog SLO monitor" [proposal — placeholder target] — which also gives the set a leading indicator (K6). If the team wants to keep developer satisfaction, move it, in the AP-04 form above, under an objective about developer experience; none exists on the page today.

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** No team is named; the sentence implies other teams' infrastructure requests to Platform are deferred for the quarter. Whether any dependent team's Q3 plan assumes Platform delivery cannot be checked with one team in scope.

The appendix's Payments (line 22) and Growth (line 23) lines are Q2 business-review extracts about other teams, not dependency statements in Platform's material, so no note is recorded for them.

## 5. Prioritized action list

1. Rewrite PL2.2 as a graded KR over the SOC 2 evidence backlog with a count baseline and a report date — owner: Elena R. (page owner) (resolves §3 AP-02 Binary KR with No Gradient).
2. Re-baseline PL1.1 against the quoted 99.95% trailing actual — raise the target above it or move uptime to a health-metric floor outside the OKRs — owner: Elena R. (page owner) (resolves §3 AP-06 Sandbagged Target).
3. Add the current score, the instrument and the sample size to PL1.3 — owner: Platform lead (resolves §3 AP-04 KR Without Baseline).
4. Relocate or replace PL1.3 so that PL1's KR set measures only reliability and cost — owner: Platform lead (resolves §3 AP-12 Orphan KR; raises §2 K7).
5. State a measurement window and a system of record on PL1.2 and PL2.1 — owner: Platform lead (raises §2 K1 and K5; no finding block).
6. Add one leading indicator to each KR set (a mid-quarter reliability or cost signal for PL1; an evidence-closure or findings-burndown rate for PL2) — owner: Platform lead (raises §2 K6 for both sets).
7. Name an accountable individual on each KR rather than relying on the page-level owner — owner: Elena R. (page owner) (raises §2 K4).
8. Record each objective's company-priority link once a strategy page is supplied, then re-run this review to score O4 — owner: Elena R. (page owner) (closes the §2 O4 gap note).
9. Confirm with the teams whose infra requests are being held until Q4 that their own Q3 plans do not assume Platform delivery — owner: Elena R. (page owner) (follows up §4 dependency note; not a finding).
