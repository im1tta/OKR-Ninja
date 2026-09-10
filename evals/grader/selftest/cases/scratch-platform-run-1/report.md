# Platform team — Q3 2026 OKR review (single-team mode)

*Scope confirmed at intake: Platform only (exactly one team → single-team mode) · Period: Q3 2026, as stated by the source page · Source (only corpus in scope): `input.md` = `input.md` (the Platform OKR page, lines 3–16, plus the Q2 2026 business-review appendix, lines 18–23) · No Atlassian connection available; no company strategy document in scope.*

## 1. Verdict summary

**Verdict: Objective PL1 needs rework before the quarter can be trusted; Objective PL2 is aimed at the right outcome but under-measured.**
Roll-up grade: **C (2.3)** for the team — Objective PL1 **D (1.9)**, Objective PL2 **C (2.6)**.
Findings: **1 Critical, 5 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." has no instrument, survey or dashboard anywhere in the corpus, so it can never be honestly scored.
Company-level strategy tracing was **out of scope**: no company/portfolio strategy document was provided or found in the corpus, so O4 Strategic Anchoring is scored **N/A** for both objectives (rubric gap note in §2) instead of guessed, and O4 is excluded from the roll-up.
Two KRs are sound as written and are deliberately not flagged: "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (baseline → target, defined denominator) and "Close 100% of pen-test findings rated High or above (currently 7 open)." (stated population and baseline).
AP-08 Committed vs Aspirational Not Labeled does **not** fire: the page states "Commitment: KRs are committed unless marked (aspirational)."
Recommended first action: replace KR PL1.3 with a KR whose measuring instrument actually exists (§5 item 1), then reset the uptime target against the quoted 99.95% trailing baseline (§5 item 2).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 2 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.3)** — Objective PL1 D (1.9, capped by a confirmed Critical anti-pattern), Objective PL2 C (2.6). No per-team cap applied: 2 of 5 KRs carry K1 ≤ 1 (not more than half), and the strategy cap is inapplicable with no strategy corpus.
- Platform: K1=2 — a done/not-done SOC 2 KR and an "8/10" score with no baseline.

**O4 = N/A — gap note (mandated by `references/goodness-rubric.md` O4, "If no strategy source exists in the corpus"):** no strategy source exists in the corpus, so O4 is scored N/A for both objectives and excluded from every mean; no strategic anchoring is inferred. Search trail: the only material in scope is `input.md` (23 lines, path above); it contains no company priority, pillar, bet, mission or strategy statement, and neither objective states a parent goal — the appendix (lines 18–23) holds Q2 metric extracts only. Obtaining the company Q3 priorities page and re-running the O4 trace is §5 item 9.

**Per-instance breakdown** (single-team mode scores exhaustively; each score ≤ 3 lists the quoted span that drove it):

**Objective PL1** — "Objective PL1: Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- O1 = 2 — "Keep the lights on, cheaper": one outcome word ("cheaper") bolted onto a standing-duty clause; delete it and no changed end-state remains. Sits between anchors 3 and 2 → lower taken.
- O2 = 2 — "Keep the lights on": a metaphor two readers would gloss differently (availability only, or all infra support?).
- O3 = 2 — the period is inherited unambiguously from "## Platform team — Q3 2026" (`sample-portfolio.md › Platform team — Q3 2026 › line 3`), but "Keep the lights on" is an open-ended standing duty crammed into a cycle → lower anchor taken.
- O4 = N/A (see gap note).

**KR PL1.1** — "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- K1 = 3 — metric, target and unit present; no baseline stated in the KR (retrievable from the corpus: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." `sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`) and no measurement window.
- K2 = 4 — "Maintain API uptime at or above 99.9%." measures a result customers experience directly.
- K3 = 1 — sandbag: "at or above 99.9%" sits below the quoted 99.95% trailing actual (see §3 AP-06).
- K4 = 3 — no owner on the KR; an individual is derivable from the same page: "Owner: Elena R." (`sample-portfolio.md › Platform team — Q3 2026 › line 4`).
- K5 = 3 — no source named in the KR, but the corpus names one obvious system of record: "(Datadog SLO monitor)" (line 21).

**KR PL1.2** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`)
- K1 = 3 — metric, baseline "$4.10", target "$3.20", unit and denominator "per 1,000 transactions" all present; measurement window unstated.
- K2 = 4 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." is a unit-economics result, not an activity.
- K3 = 3 — a clear ~22% reduction stretch off the quoted "$4.10"; justification and trend absent.
- K4 = 3 — page-level owner only: "Owner: Elena R." (line 4).
- K5 = 2 — no system of record named for cloud spend and none appears in the corpus (the only named source is the Datadog SLO monitor, for uptime); billing-console and finance views would give different numbers.

**KR PL1.3** — "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- K1 = 1 — qualitative dressed as a metric: "developer satisfaction score" defines no scale of record and states no "from" value.
- K2 = 3 — a perception proxy for the internal-developer customer, with no stated causal link to the objective it sits under.
- K3 = 2 — capped as unverifiable: no baseline or prior actual for this metric exists anywhere in the corpus (whole file searched), so calibration cannot be judged.
- K4 = 3 — page-level owner only: "Owner: Elena R." (line 4).
- K5 = 1 — requires data collection that does not exist yet: no survey, instrument or dashboard for developer satisfaction appears anywhere in the corpus, and no KR or task in the set builds one (see §3 AP-09).

**Objective PL2** — "Objective PL2: Earn enterprise trust" (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`)
- O1 = 4 — "Earn enterprise trust" states a changed end-state with no delivery verb; it survives dropping SOC 2 as the route.
- O2 = 4 — "Earn enterprise trust": three words, plain language, named audience, no metric inside.
- O3 = 3 — period inherited unambiguously from "## Platform team — Q3 2026" (line 3), not restated in the objective.
- O4 = N/A (see gap note).

**KR PL2.1** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`)
- K1 = 3 — population, baseline "(currently 7 open)" and the "100%" target are all stated; measurement window not stated.
- K2 = 3 — remediation output with a credible link to the stated objective, "Earn enterprise trust".
- K3 = 3 — closing all 7 quoted High-or-above findings is a genuine stretch; no justification stated.
- K4 = 3 — page-level owner only: "Owner: Elena R." (line 4).
- K5 = 2 — the pen-test report or tracker of record is not named in the KR and appears nowhere in the corpus.

**KR PL2.2** — "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- K1 = 0 — "Complete the SOC 2 Type II audit." is a pure done/not-done milestone with nothing countable (caps this KR's score at 1.0 per the rubric).
- K2 = 1 — the measure is a delivery milestone.
- K3 = 2 — capped as unverifiable: no baseline or numeric target exists for it anywhere in the corpus.
- K4 = 3 — page-level owner only: "Owner: Elena R." (line 4).
- K5 = 2 — no auditor, report or tracker of record is named, and none appears in the corpus.

**KR sets**
- PL1 K6 = 2 — all lagging: "Maintain API uptime at or above 99.9%.", "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." and "Improve internal developer satisfaction score to 8/10." are all end-state truths; no leading indicator predicts any of them, so the set gives no mid-cycle steering signal.
- PL1 K7 = 2 — one orphan KR: "Improve internal developer satisfaction score to 8/10." serves a different goal than "Keep the lights on, cheaper" (see §3 AP-12), while PL1.1 and PL1.2 already cover both halves of the objective.
- PL2 K6 = 2 — both KRs are compliance proxies ("Close 100% of pen-test findings rated High or above (currently 7 open)." and "Complete the SOC 2 Type II audit.") with nothing in the set that they predict; no lagging trust outcome is measured.
- PL2 K7 = 3 — one coverage gap: nothing in the set measures anything an enterprise customer does or decides, so "Earn enterprise trust" is evidenced only by internal compliance posture. No orphan KR.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the KR quantifies an internal state with no instrument — the entire corpus in scope (the 23-line `input.md`: the Platform OKR page and the Q2 2026 business-review appendix) contains no survey, tool or dashboard for developer satisfaction, and no KR or task in the set stands one up; the only named system of record anywhere is "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`). The KR therefore cannot be honestly scored at quarter end, and "score to 8/10" names no scale of record.
- Scores affected: K5=1, K1=1, K3=2 (unverifiable cap); as a confirmed Critical anti-pattern it caps Objective PL1's roll-up at 1.9 (max D).
- Suggested rewrite: "KR PL1.3 (committed): stand up the internal developer-experience survey in `<survey tool>` by `<date>`, run it to n ≥ `<respondents>` of the internal engineering org, and move platform satisfaction from `<measured baseline>`/10 to `<target>`/10 as reported on `<survey dashboard>` — that dashboard is the sole system of record." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, other end of the cross-source claim): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target sits below the trailing actual quoted in the same document, so the KR is already achieved on day one and the team can hit it by changing nothing — it encodes no ambition and, worse, licenses a reliability regression from 99.95% to 99.9%.
- Scores affected: K3=1; contributes to the team K3=2 aggregate.
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% trailing 90 days (Q2 actual, Datadog SLO monitor) → 99.98% monthly across Q3, measured on the same monitor, with the monthly error budget capped at `<minutes>`." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Objective PL1: Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: "Keep the lights on" plus "Maintain" describes the team's standing operational job with no delta — it is achieved by default staffing and displaces a real goal, and only the "cheaper" clause proposes any change in the world. An open-ended duty also cannot be failed inside a quarter.
- Scores affected: O1=2, O2=2, O3=2.
- Suggested rewrite: "Objective PL1: Serving a transaction gets cheaper every month without customers feeling a difference." Move the standing duty out of the OKRs into a health-metric guardrail that is tracked but not scored: "Guardrail: API uptime stays at or above 99.95% (Datadog SLO monitor)." [proposal — guardrail figure quoted from line 21]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Why it's a problem: the KR can only be scored 0% or 100%, so it gives no mid-cycle progress signal on the largest commitment in the quarter ("Q3 is fully committed between SOC 2 evidence collection and the cost work.", `sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`). The same span also satisfies AP-01 Task Masquerading as KR's detect — it opens with "Complete", names no metric and states no baseline → target pair.
- Scores affected: K1=0 (caps this KR's score at 1.0), K2=1, K3=2 (unverifiable cap), K5=2; drives PL2 K6=2.
- Suggested rewrite: "KR PL2.2 (committed): close 100% of the `<N>` control gaps listed in the SOC 2 readiness assessment (0/`<N>` closed today, tracked in `<compliance tracker>`) and receive the Type II report with zero exceptions by `<date>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the target is stated with no starting point and none is retrievable — the whole corpus was searched (the Platform OKR page, lines 3–16, and the Q2 2026 business-review appendix, lines 18–23, whose only Platform row is the uptime figure), and no prior or current satisfaction number appears. Both the ambition and mid-quarter progress are unjudgeable: 8/10 may be a stretch or may already be true.
- Scores affected: K1=1, K3=2 (unverifiable cap).
- Suggested rewrite: "KR PL1.3 (committed): internal developer satisfaction `<measured baseline>`/10 (first measurement taken in week 1 of Q3, same instrument and population) → `<target>`/10 by quarter end." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence (objective it sits under): "Objective PL1: Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Why it's a problem: there is no causal chain in two steps or fewer from a satisfaction score to either availability or unit cost, and the KR shares no noun or domain with the objective; the objective's two halves are already covered by PL1.1 and PL1.2, so hitting this KR would not move "Keep the lights on, cheaper" at all.
- Scores affected: K7=2 (PL1 set), K2=3.
- Suggested rewrite: "KR PL1.3 (committed): idle or unattached cloud resources fall from `<baseline>`% to `<target>`% of monthly cloud spend (source: `<cloud billing export>`)." Move developer satisfaction to a developer-experience objective where it is the outcome being pursued rather than a bystander. [proposal — placeholder target]

## 4. Outbound dependency notes

Single-team mode produces no AL-XX findings — with one team in scope the taxonomy's both-sides quote rule cannot be met — so the cross-team mentions in Platform's material are recorded here as notes only, with no severity.

- "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** Platform declares its quarter full and defers other teams' infra requests to Q4, but names no requesting team and no specific request, so whether another team's Q3 plan depends on that deferred work cannot be checked from the material in scope.

No other cross-team dependency mention appears in Platform's OKRs: no team name, "depends on", "blocked by" or shared-system reference occurs in lines 3–16. (The appendix's Payments and Growth rows, lines 22–23, are Q2 metric extracts for other teams, not Platform dependency statements, and are not treated as such.)

## 5. Prioritized action list

1. Replace KR PL1.3 with a KR whose measuring instrument exists and is named, standing the survey up in the first weeks of Q3 — owner: Elena R., Platform (resolves §3 AP-09 Metric Nobody Can Measure).
2. Reset KR PL1.1 above the quoted 99.95% trailing baseline before the quarter is locked — owner: Elena R., Platform (resolves §3 AP-06 Sandbagged Target).
3. Rewrite Objective PL1 as a cost-reduction outcome and demote standing availability to a tracked guardrail — owner: Elena R., Platform (resolves §3 AP-10 BAU Dressed as OKR).
4. Convert KR PL2.2 into a graded control-closure count with a dated report milestone — owner: Platform compliance/security lead (resolves §3 AP-02 Binary KR with No Gradient).
5. Take and publish a measured baseline before committing any developer-satisfaction target — owner: Elena R., Platform (resolves §3 AP-04 KR Without Baseline).
6. Move developer satisfaction out of Objective PL1 and put a cost or reliability KR in its place — owner: Elena R., Platform (resolves §3 AP-12 Orphan KR).
7. Name the system of record for cloud spend per 1,000 transactions and for pen-test findings, as the uptime KR already implies via Datadog — owner: Elena R., Platform (raises K5=2 on PL1.2 and PL2.1, §2).
8. Add one leading indicator to each KR set so both objectives can be steered mid-quarter — owner: Elena R., Platform (raises K6=2 on both sets, §2).
9. Obtain the company Q3 2026 priorities page and re-run the O4 strategic-anchoring trace for both objectives — owner: Elena R., Platform (resolves the §2 O4 = N/A gap note).
