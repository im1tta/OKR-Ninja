# Platform team — Q3 2026 OKR review (single-team mode)

Scope confirmed at intake: **Platform team only** (exactly one team → single-team mode), period **Q3 2026** as stated on the source page, source **`input.md`** (Platform OKR page + Q2 2026 business-review appendix). No Atlassian connection available; no other source consulted.

## 1. Verdict summary

**Verdict: Needs rework before the quarter can be trusted.** Roll-up grade **C (2.15)** for the team, but Objective PL1 lands at **D (1.9)** on its own.
2 objectives and 5 KRs reviewed exhaustively; **1 Critical, 6 Major, 0 Minor** findings.
The worst finding is **AP-09 Metric Nobody Can Measure**: "Improve internal developer satisfaction score to 8/10." names a score that no instrument in the corpus produces, so the KR can never be honestly scored.
The most consequential quality pattern is measurement discipline — two of five KRs (PL1.3, PL2.2) carry no usable baseline→target pair at all, and the one cross-checkable target (PL1.1) sits *below* the baseline quoted in the same file.
Objective PL2 "Earn enterprise trust" is the strongest objective in the set (O1=4); its KRs, not its framing, are what drag it to C.
**Company-level strategy tracing was out of scope** for this run: no company/org strategy document was provided and none exists in the corpus (searched the whole corpus for "strategy", "priorit*", "pillar", "bet" — 0 substantive hits). Per `references/goodness-rubric.md`, O4 Strategic Anchoring is therefore scored **N/A** and excluded from the roll-up, with the mandated gap note in §2 — it is not scored as a low O4 and not reported as a finding.
**Recommended first action:** Elena R. rebases KR PL1.1 on the quoted 99.95% trailing baseline and replaces KR PL1.3 with a metric that has a named instrument, before the quarter is scored.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

**O4 = N/A — gap note (rubric-mandated):** no strategy source exists in the corpus. Search trail: the entire corpus for this run is the single file above; it contains a Platform OKR page and a Q2 2026 business-review appendix, and no company/org strategy artifact, priority list, or pillar set. Neither objective states a parent link — the only parent-like text on the page is "*Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05*" (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 4`), which names a page, not a strategic priority. O4 is excluded from the roll-up rather than guessed. **This is a real traceability gap:** neither objective can be shown to serve a company priority, and the team cap for "0 OKRs traceable to strategy" could not be evaluated because no strategy corpus is present.

**Roll-up grades (per `references/goodness-rubric.md` Roll-Up):** Platform **C (2.15)** — Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**.

- Platform: K1=2 — two of five KRs state no measurable baseline→target pair (AP-04, AP-02).

### Per-instance breakdown

Objective dimensions:

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 2 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

- **PL1 O1=2** — "Keep the lights on, cheaper" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): the "cheaper" clause names a changed end-state, but "Keep the lights on" names the team's standing condition, satisfiable with no change. Half the objective is not a change in the world.
- **PL1 O2=3 / PL2 O2=3** — "Keep the lights on, cheaper" (line 7) and "Earn enterprise trust" (`… › Objective PL2: Earn enterprise trust › line 12`) are both short, plain and memorable with no metric pasted in, but neither carries a specific noun subject: "the lights" is a metaphor whose scope (uptime? incidents? support load?) is fixed only by the KRs, and "trust" leaves the evidence-of-trust unnamed.
- **O3=3 (both)** — neither objective restates a period; both inherit it unambiguously from "## Platform team — Q3 2026" (`… › Platform team — Q3 2026 › line 3`), and both are failable within it.
- **O4=N/A (both)** — see gap note above.

KR dimensions:

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 Maintain API uptime | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 Reduce cloud spend | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 Developer satisfaction | 1 | 3 | 2 | 3 | 1 | 2.0 |
| PL2.1 Close pen-test findings | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 Complete SOC 2 audit | 0 | 1 | 2 | 3 | 2 | 1.6 → **1.0** (K1=0 cap) |

- **PL1.1 K1=3** — "Maintain API uptime at or above 99.9%." (`… › Objective PL1: Keep the lights on, cheaper › line 8`): metric, target and unit present; baseline absent from the KR but retrievable from the corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`… › Appendix — Q2 2026 business review (extracts) › line 21`). Window unstated in the KR.
- **PL1.1 K3=1** — sandbag; see §3 AP-06. **K5=3** — "API uptime" has one obvious system of record found elsewhere in the corpus ("Datadog SLO monitor", line 21), but the KR itself names no source.
- **PL1.2 K1=3 / K5=2** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`… › Objective PL1: Keep the lights on, cheaper › line 9`) is the strongest KR in the set: named metric, numeric baseline, numeric target, explicit denominator. It loses a point on K1 for an unstated measurement window and on K5 because no cost system of record is named anywhere in the corpus (searched: no "dashboard", "Looker", "FinOps" or billing source present), so cloud-console, finance-ledger and internal readings could differ. **K3=3** — a properly-labeled committed KR at a modest, unjustified stretch (~22%).
- **PL1.3 K1=1 / K5=1 / K3=2** — "Improve internal developer satisfaction score to 8/10." (`… › Objective PL1: Keep the lights on, cheaper › line 10`) is a qualitative state dressed as a metric with no defined score (K1=1) and requires data collection that does not exist yet, with no KR or task to build it (K5=1; corpus search for "survey", "eNPS", "Culture Amp", "dashboard" returned nothing). No baseline or trend for it exists anywhere in the corpus, so K3 takes the rubric's unverifiable cap of 2 — calibration cannot be judged. **K2=3** — internal developers sit outside the Platform team, but self-reported sentiment is a proxy and no causal link to an outcome is stated.
- **PL2.1 K1=3 / K3=3 / K5=2** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`… › Objective PL2: Earn enterprise trust › line 13`): the population is explicitly bounded ("rated High or above", "currently 7 open"), so the percentage has a defined denominator and a stated baseline — no ambiguous-denominator defect here. Window unstated (K1=3); no security tracker or vendor report named in the corpus (K5=2). **K2=3** — a proxy output whose link to the stated objective is credible.
- **PL2.2 K1=0 / K2=1** — "Complete the SOC 2 Type II audit." (`… › Objective PL2: Earn enterprise trust › line 14`): nothing countable, a pure done/not-done milestone (see §3 AP-02, AP-01). K1=0 caps this KR's score at 1.0. **K3=2** — no baseline, target magnitude or prior actual exists for it anywhere; unverifiable cap applied.
- **K4=3 for all five KRs** — no KR names an accountable individual, but the owning team is named and an individual is derivable from the same source: "*Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05*" (`… › Platform team — Q3 2026 › line 4`). No KR is ownerless.
- **K6=2 (both sets)** — PL1's three KRs are all end-of-quarter truths (uptime, quarterly cost, a satisfaction score) with no leading indicator that predicts any of them; PL2's two KRs are both compliance proxies ("Close 100% of pen-test findings rated High or above (currently 7 open)." line 13; "Complete the SOC 2 Type II audit." line 14) with no lagging outcome KR that they predict.
- **K7=2 (both sets)** — PL1: both objective clauses are covered (PL1.1 for "lights on", PL1.2 for "cheaper"), but PL1.3 is an orphan serving a different goal (see §3 AP-12). PL2: multiple gaps — nothing in the set measures whether enterprises actually extend trust (deals unblocked, security reviews passed, enterprise renewals), and nothing commits the availability or support assurances enterprises buy; both KRs measure audit readiness only.
- **Commitment labelling is present and does not need flagging:** "*Commitment: KRs are committed unless marked (aspirational).*" (`… › Platform team — Q3 2026 › line 5`) supplies the convention the rubric looks for, so committed-vs-aspirational is not an open defect.

**Roll-up arithmetic.** PL1: 0.35 × mean(O1..O3) 2.67 + 0.45 × mean per-KR 2.60 + 0.20 × mean(K6,K7) 2.00 = 2.50, then capped to **1.9 (D)** by the confirmed Critical AP-09. PL2: 0.35 × 3.33 + 0.45 × 1.90 + 0.20 × 2.00 = 2.42, then capped to **2.4 (C)** by two Major anti-patterns on one OKR (AP-02, AP-01). Team = mean(1.9, 2.4) = **2.15 (C)**. Team caps checked: K1 ≤ 1 on 2 of 5 KRs (not more than half, no cap); the strategy-traceability cap is not evaluable with no strategy corpus present.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the KR quantifies an internal state and names no instrument, and no survey, dashboard or tool that could report an "internal developer satisfaction score" appears anywhere in the corpus (searched the whole file for "survey", "eNPS", "Culture Amp", "dashboard"; the only instrument named is the "Datadog SLO monitor" at line 21, which measures uptime). The number can never be honestly scored, so the KR can be claimed at any value at quarter end.
- Scores affected: K5=1, K1=1, K3=2 (unverifiable cap); drives PL1's per-OKR cap to 1.9 (D).
- Suggested rewrite: "KR PL1.3 (committed): Platform Experience pulse survey — new quarterly instrument, run in `<survey tool>`, n ≥ `<respondents>` of the engineering org, same population both runs: overall platform satisfaction `<month-1 baseline>`/10 → `<target>`/10. The survey instrument ships in month 1 so a baseline exists before scoring." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 8`), against the baseline quoted in the same file: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`…/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the target (99.9%) sits *below* the team's own trailing-90-day actual (99.95%) recorded in the corpus, so the KR is already met on the day it is written and could be hit while reliability degrades by roughly a factor of two. "Maintain" is the rubric's exact sandbag trigger.
- Scores affected: K3=1; contributes to K6=2 (no leading signal) and to PL1's D grade.
- Suggested rewrite: "KR PL1.1 (committed): API uptime, trailing 90 days: 99.95% → 99.97%, measured on the same Datadog SLO monitor; error-budget burn reported monthly." [proposal — placeholder target] (99.95% is quoted from line 21; 99.97% is a proposed target.)

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 7`), operationalised by "Maintain API uptime at or above 99.9%." (`… › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: "Keep the lights on" is the team's standing job stated with no delta — it is achieved by default staffing and its KR asks only that today's uptime not get worse. Presenting it as half of one of the team's two objectives consumes goal space that a real change should occupy; the page itself records the displacement: "Holding all non-critical infra requests until Q4." (`… › Objective PL2: Earn enterprise trust › line 16`).
- Scores affected: O1=2, K3=1 (PL1.1), K6=2; PL1 roll-up D (1.9).
- Suggested rewrite: "O PL1: Serving a transaction costs less every month, and customers never notice the difference. — KR PL1.1 (committed): cloud spend per 1,000 transactions $4.10 → $3.20. KR PL1.2 (committed): customer-visible incidents `<baseline>` → `<target>` per quarter (Datadog SLO monitor)." [proposal — placeholder target] Move the standing "Maintain API uptime at or above 99.9%." duty to a health-metric/SLO section outside the OKRs, where it belongs. ($4.10 and $3.20 are quoted from line 9.)

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the target ("to 8/10") is stated with no starting point and no "from", and none is retrievable in the corpus — the Q2 2026 business review carries only uptime, chargeback and signup figures ("API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." line 21), nothing on developer satisfaction. Ambition and mid-quarter progress are both unjudgeable: 8/10 could be a stretch or already true.
- Scores affected: K1=1, K3=2 (unverifiable cap).
- Suggested rewrite: "KR PL1.3 (committed): internal developer satisfaction `<month-1 baseline>`/10 → 8/10, same instrument and same population on both runs, reported at mid-quarter and quarter end." [proposal — placeholder target] (8/10 is quoted from line 10.)

### [Major] AP-12 Orphan KR — Platform
- Evidence: objective "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 7`) paired with its third KR, "Improve internal developer satisfaction score to 8/10." (`… › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the objective's two stated end-states are availability and unit cost; moving a developer satisfaction score to 8/10 would not move either one. The plausible causal chain runs the other way (reliability improves, so developers are happier), and the cost clause pushes against it, so the KR's *success* does not advance the objective it sits under — the rubric's orphan test.
- Scores affected: K7=2 (PL1 set), contributes to K6=2.
- Suggested rewrite: keep the developer-experience measure but move it under its own objective, and replace it here with a KR that moves this objective: "KR PL1.3 (committed): unplanned platform toil hours per on-call week `<baseline>` → `<target>` (source: `<on-call report>`), so cost reduction is not paid for in operator time." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input.md › Objective PL2: Earn enterprise trust › line 14`)
- Why it's a problem: the KR is a single done/not-done event with no numeric scale, so mid-cycle scoring can only read 0% or 100% — the team gets no signal about whether it is on track until the quarter is over, even though the page states the work is a load-bearing commitment: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`… › Objective PL2: Earn enterprise trust › line 16`).
- Scores affected: K1=0 (caps this KR at 1.0), K2=1, K6=2, K7=2; PL2 roll-up C (2.4).
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence controls closed 0/`<N total controls>` → `<N>`/`<N>`, tracked weekly, with the auditor's Type II report received by `<date>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input.md › Objective PL2: Earn enterprise trust › line 14`)
- Why it's a problem: the KR opens with a delivery verb ("Complete") and states a deliverable with no metric and no baseline→target pair; it succeeds when a document is produced, whether or not a single enterprise customer's trust changes — which is what the objective "Earn enterprise trust" (`… › Objective PL2: Earn enterprise trust › line 12`) claims.
- Scores affected: K2=1, K1=0, K7=2; second Major on PL2, triggering the 2.4 cap.
- Suggested rewrite: "KR PL2.2 (committed): enterprise security reviews cleared without a compensating-control exception `<baseline>` → `<target>` per quarter, with the SOC 2 Type II report received by `<date>` as the enabling evidence." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`input.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** The sentence records a cross-team dependency: other teams' infra requests on Platform are deferred out of the quarter. Its stated cause is quoted in the same line: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`… › Objective PL2: Earn enterprise trust › line 16`). No other team's OKRs were in scope, so whether any team has committed to work that this deferral blocks cannot be checked here, and no severity is assigned.

No other cross-team dependency mention appears in the Platform material: neither objective nor any of the five KRs names another team, a shared system, or a "depends on" / "blocked by" relationship. (The Payments and Growth lines in the appendix are other teams' Q2 results, not Platform dependencies, and were not treated as Platform's material.)

## 5. Prioritized action list

1. Rebase KR PL1.1 on the quoted 99.95% trailing-90-day actual and set a target above it — owner: Elena R., Platform lead (resolves §3 AP-06 Sandbagged Target).
2. Replace KR PL1.3 with a metric backed by a named instrument, and ship that instrument in month 1 so a baseline exists before scoring — owner: Elena R., Platform lead (resolves §3 AP-09 Metric Nobody Can Measure and §3 AP-04 KR Without Baseline).
3. Convert KR PL2.2 from a binary audit milestone into a countable evidence-closure metric with a weekly reading — owner: Platform SOC 2 evidence lead (resolves §3 AP-02 Binary KR with No Gradient and §3 AP-01 Task Masquerading as KR).
4. Rewrite Objective PL1 so it states a change rather than the standing job, and move "Maintain API uptime at or above 99.9%." to a health-metric section outside the OKRs — owner: Elena R., Platform lead (resolves §3 AP-10 BAU Dressed as OKR).
5. Move the developer-experience measure under its own objective and give PL1 a third KR that actually moves availability or unit cost — owner: Elena R., Platform lead (resolves §3 AP-12 Orphan KR).
6. Add one leading indicator to each KR set — an error-budget-burn reading for PL1 and a weekly evidence-closure reading for PL2 — so both objectives are steerable mid-quarter — owner: Elena R., Platform lead (resolves §2 K6=2).
7. Add a customer-side KR to Objective PL2 that measures whether enterprises extend trust, not only whether the team is audit-ready — owner: Elena R. with the enterprise account owner (resolves §2 K7=2 for PL2).
8. Name the system of record for cloud spend per 1,000 transactions and for pen-test findings on the OKR page — owner: Elena R., Platform lead (resolves §2 K5=2 on PL1.2 and PL2.1).
9. Obtain the company Q3 2026 priority list and record each objective's parent link on the page, then re-score O4 — owner: Elena R. with her manager (resolves §2's O4 = N/A gap note).
10. Take the deferral "Holding all non-critical infra requests until Q4." to the teams that filed those requests before mid-quarter — owner: Elena R., Platform lead (resolves §4's unverified outbound dependency note).
