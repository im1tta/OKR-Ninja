# OKR Portfolio Review — Brightledger, Q3 2026

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed (Payments, Growth, Platform, Data), period Q3 2026, portfolio mode; 5 Critical, 8 Major, 1 Minor findings.
The worst alignment risk is AL-10 Strategy coverage gap: company priority "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." — has zero coverage in any of the four teams' OKRs.
The most common goodness anti-pattern is AP-04 KR Without Baseline: three KRs across Growth and Platform state a target with no starting point.
Two committed KRs are sequenced impossibly: Growth launches self-serve upgrades on the new billing API "by Aug 15" while Payments commits that API to GA "by Sep 26" (AL-06 Timeline mismatch).
Payments and Data both bank on Platform capacity in a quarter Platform declares "fully committed" (AL-07 Resource contention), and Data's pipeline dependency appears nowhere in Platform's plan (AL-01 Unacknowledged dependency).
Platform and Data each carry a KR that no system in the corpus can score (AP-09 Metric Nobody Can Measure), and Growth and Data both commit to the same activation metric with different targets (AL-03 Duplicated / overlapping objectives).
Recommended first action: name an owner for C4 and re-sequence the Growth/Payments billing-API dates before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Data | 3 | 2 | 3 | 1 | 3 | 3 | 2 | 3 | 2 | 2 | 3 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.2) · Data C (2.3) · Growth C (2.6) · Payments B (3.1).

- Platform: K1/K5=2 — "Improve internal developer satisfaction score to 8/10." names no instrument and no baseline.
- Data: O4=1 — "One trustworthy source of truth" traces to no company priority (see AL-04).
- Growth: K1/K3=2 — "Increase trial-to-paid conversion to 22%." states no baseline, so ambition is unjudgeable.
- Payments: K1=2 — "Ship checkout & billing API v2 to GA by Sep 26." counts nothing measurable.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no instrument for a "developer satisfaction score" exists anywhere in the corpus — the whole export (company priorities page, all four team pages, Q2 business-review appendix) was searched for `satisfaction`, `survey`, `score` and `sentiment`, and line 59 is the only hit — so the number can never be honestly scored; the KR also states no current value, so 8/10 cannot be read as ambition or as progress.
- Scores affected: K5=0, K1=1, K3=2 (calibration unverifiable), K7=2 for the PL1 set
- Suggested rewrite: "KR PL1.3: Internal developer satisfaction, quarterly engineering survey (instrument: `<named survey tool>`, n ≥ `<sample size>`): `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing-90-day actual quoted in the same export, so the KR is achieved by changing nothing and would still score green if reliability degraded — it encodes a regression allowance, not an improvement.
- Scores affected: K3=1, K1=3 (baseline retrievable from the appendix but not stated in the KR)
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.98%, measured monthly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable — it begins with "Complete" and carries no metric and no baseline→target pair — so it can only ever score 0% or 100% and gives the team no mid-quarter steering signal on the work the company names as priority C2.
- Scores affected: K1=0, K2=1, K6=3 for the PL2 set
- Suggested rewrite: "KR PL2.2: SOC 2 Type II auditor evidence requests closed `<baseline>`/`<total>` → 100%, auditor's report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" is never defined and no check, dashboard, or system of record for it appears anywhere in the corpus — the whole export was searched for `data quality`, `quality`, `freshness`, `accuracy` and `completeness`, and line 76 is the only hit — so nobody can say at quarter end whether the KR was hit; "Significantly" states a direction with no magnitude.
- Scores affected: K5=0, K1=1, K3=2 (calibration unverifiable)
- Suggested rewrite: "KR D1.3: Core-table quality — rows failing the nightly `<test suite>` across the `<N>` core tables: `<baseline>`% → 0.5%, reported weekly." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no current trial-to-paid value is stated in the KR or retrievable anywhere in the corpus — all four team pages, the company priorities page and the Q2 business-review appendix were searched, and the appendix reports only uptime, chargeback rate, step-up coverage and qualified signups — so 22% could be a stretch or could already be true today.
- Scores affected: K1=2, K3=2 (calibration unverifiable)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<funnel dashboard>`) → 22%, monthly signup cohorts." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid distribution without indicating that the funnel converts anything, which is exactly what the objective claims; and with no starting value stated or retrievable in the corpus, 50,000 cannot be read as ambition or progress.
- Scores affected: K2=2, K1=2, K3=2, K7=2 for the G2 set
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → 250/mo (attribution: `<analytics source>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR begins with "Ship" and states no metric and no baseline→target pair, so it is satisfied the moment the team declares GA even if no merchant traffic ever moves onto v2; its only failure mode is lateness, not a worse checkout.
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR P1.2: Card transactions served by checkout & billing API v2: 0% → `<target>`% of production volume by Sep 26, with v2 error rate no higher than v1's `<baseline>`%." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company Q3 2026 priorities ↔ Payments · Growth · Platform · Data
- Company evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss across all four teams): "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23) — a payments-API delivery, which finances nothing and names no design partners.
- Conflict: a dated, committed company priority has no contributing objective or KR in any of the four teams in scope; with 12 weeks to Sep 30 and no team carrying the pilot, C4 fails by default rather than by decision.
- Detection check that fired: AL-10 top-down strategy trace — company objective with zero contributing children after sweeping all four team pages (Payments, Growth, Platform, Data).
- Disconfirming checks run: re-searched the whole export under synonyms and program names (`capital`, `financ`, `invoice-financing`, `design partner`, `lending`, `loan`, `pilot`) — line 13 itself is the only hit, so no coverage hides under a different name; checked C4's own line and the priorities page for an owner outside the swept team set — none is named beyond the page owner "Dana W. (CEO)" (line 8), so this is a portfolio hole, not an ownership note.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Dana W. (CEO) to name an owning team for C4 or to move it out of Q3 — decision within 2 weeks, while a Sep 30 pilot is still reachable.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41), with the dependency stated as "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's launch date precedes the producer's delivery date by six weeks — Growth ships on the new billing API on Aug 15, Payments commits that API to GA on Sep 26 — and both KRs are committed under each page's stated convention "Commitment: KRs are committed unless marked (aspirational)." (line 19, line 36). A hard inversion on committed KRs is Critical by the AL-06 severity rule.
- Detection check that fired: AL-06 edge date comparison on the dependency map — consumer need-by (Aug 15) earlier than producer delivery (Sep 26), leaving negative integration margin.
- Disconfirming checks run: `late date ≠ inversion` — searched Payments' page for an earlier milestone (beta, early access, private preview) that Growth's integration could ride instead; the Sep 26 GA is the only dated API milestone in the corpus. Checked Growth's note for a hedge or fallback path — it records only "should be fine", no alternative. Both dates are quoted, neither inferred.
- Inference labels: none — all load-bearing text quoted. (The June sync is quoted, but it records no date agreement.)
- Verdict: CONFIRMED
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree either an Aug 15 pre-GA cut of billing API v2 or a revised G1.3 launch date — within 1 week, while Growth's Aug 15 commitment is still recoverable.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and taking its coverage from 35% to 90% of transactions puts a challenge step in front of far more checkouts in the very quarter Growth commits to a ten-point conversion lift on that same surface; neither page mentions the other team. Severity: a mechanism-level conflict is Major by default, escalated one level because both KRs are committed under their pages' stated convention (line 19, line 36).
- Detection check that fired: AL-02 surface-lever blocking key — both KRs sit on the checkout surface, Payments' stated lever is a verification/friction control there, and Growth targets that surface's conversion metric. The metric-identity key generated nothing: the two KRs share no canonical metric name.
- Disconfirming checks run: shared or parent OKR covering both — none found (the priorities page carries C1 and C3 as separate items with no joint guardrail); documented split of levers — none found in either team's notes; directionality — confirmed opposed (more challenges vs. more completions). Separately, the lookalike candidate "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) × Growth's checkout conversion was generated and killed: different populations (card transactions vs self-serve signups), same direction, no control lever on either side — that kill is per-candidate and does not touch this pair.
- Inference labels: the verification→conversion mechanism is analyst inference — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against the export)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree a guardrail pair — a chargeback ceiling plus a checkout-conversion floor, reviewed monthly — before step-up coverage ramps; escalate to Dana W. (CEO) if unresolved in 2 weeks.

### [Major] AL-07 Resource contention: Payments · Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (declared supply): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' Q3 plans draw on Platform capacity while Platform's own page declares the quarter fully committed to SOC 2 and cost work and defers non-critical infra requests to Q4; nobody has done the arithmetic, and Platform's five KRs fund neither ask. Both claimants' KRs (Payments' API v2 GA, Data's schema v2 rollout) are committed and both assume the capacity silently.
- Detection check that fired: AL-07 resource-node fan-in — grouping every shared-resource mention by owner puts two Q3 claimants on the Platform node; checking that owner's page for declared supply yields an explicit fully-committed statement. Classification was made at the node, not edge-by-edge.
- Disconfirming checks run: `plural demand ≠ contention` — no Jira, backlog, or capacity/allocation table exists in this corpus (local export only, no Atlassian connection available), and Platform's page contains no allocation for either claimant; confirmed both claims fall in the same period (Q3 2026) and name the same owner (Platform explicitly, "the infra level" resolved to Platform), not similarly-named groups. Per the taxonomy's AL-07/AL-01 aggregation rule, Payments' ask is a pure provisioning/capacity claim and folds into this finding entirely, while Data's named deliverable additionally earns the AL-01 below; the capacity arithmetic is reported once, here.
- Inference labels: Data's "the infra level" resolved to the Platform team — analyst inference (Platform is the only infrastructure-owning team in scope).
- Verdict: CONFIRMED
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 allocation covering the PCI-scoped infra and the streaming pipeline migration, or to state explicitly that neither lands this quarter so Payments and Data can re-plan — within 1 week.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82), carrying the KR "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (closest partial match, and why it does not cover the need): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65) — a generic deferral, not an acknowledgment: neither Platform objective nor any of its five KRs names a pipeline, a migration, or event streaming.
- Conflict: Data's committed KR D1.1 depends on a streaming pipeline migration that Data explicitly assigns to someone else while sizing only its own 3 engineer-months; the deliverable — a project Platform would have to plan and staff, not merely capacity to allocate — appears nowhere in Platform's OKRs. Cross-reference: the combined-demand arithmetic for this edge and the Payments edge is reported once, under AL-07 above.
- Detection check that fired: AL-01 edge acknowledgment on the dependency map — dependency phrases extracted from Data's notes ("rides on", "expect the pipeline itself to be handled at the infra level"), resolved to Platform, then searched on the producer's side with no hit. Per the AL-07 aggregation rule this edge names a distinct deliverable, so it earns its own AL-01 alongside the aggregate.
- Disconfirming checks run: `missing mention ≠ unacknowledged` — the producer's Jira epics and backlog cannot be searched (no Atlassian connection; the local export is the entire corpus), so the search scope was the whole export: the terms `pipeline`, `streaming`, `migrat`, `schema` and `warehouse` return only Data's own lines 74 and 82, and nothing on the Platform page. The nearest Platform text is quoted above. The Critical escalation (producer has explicitly deprioritized the area) was considered and declined: Platform's deferral quote names "non-critical infra requests" generically and never names this migration.
- Inference labels: "the infra level" resolved to the Platform team — analyst inference (Platform is the only infrastructure-owning team in scope).
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data) to get the streaming pipeline migration named, sized and scheduled on Platform's Q3 plan with Elena R. (Platform), or to re-scope D1.1 to what Data can deliver alone — within 2 weeks.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to moving the same metric from the same baseline to two different targets in the same quarter with no cross-reference, shared owner, or division of labor; if activation lands at 36% both teams can declare success and nobody is accountable for the missing four points. Inconsistent targets on one metric make this Major rather than plain duplication.
- Detection check that fired: AL-03 clustering by target metric plus population — "new-user activation rate", identical 31% baseline, identical new-user population, two teams.
- Disconfirming checks run: `similar objectives ≠ duplication` — searched both pages for a mutual reference, shared epic, joint owner, or explicit lane split: Growth's notes name only Payments ("Marcus synced with Priya in June"), Data's notes name only the infra dependency, and neither page mentions the other team. Checked for different populations, surfaces or segments that would make this legitimate division of labor — Data's KR states no population or definition at all, so no split is quotable. Checked AL-09 first: the two baselines agree at "31%", so this is duplication, not baseline disagreement.
- Inference labels: none — all load-bearing text quoted. Cross-reference: AL-08 Terminology collision is secondary here — Growth defines activation as "first invoice sent within 7 days" and Data states no definition, so the two targets may not even measure the same thing.
- Verdict: CONFIRMED
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to agree a single owner, a single target and one written definition for new-user activation — before mid-quarter.

### [Minor] AL-04 Orphan objective: Data ↔ Company Q3 2026 priorities
- Data evidence: "One trustworthy source of truth" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73)
- Company evidence: "C1 — Grow self-serve revenue" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 10); the remaining priorities are "C2 — Become enterprise-ready" (line 11), "C3 — Cut fraud losses" (line 12) and "C4 — Launch Brightledger Capital" (line 13) — none names data, reporting, or analytics.
- Conflict: D1 claims no parent, and its KR metrics (reconciliation discrepancies, critical-dashboard latency) are neither company-level metrics nor documented drivers of one, so a quarter of Data's capacity serves nothing stated above it.
- Detection check that fired: AL-04 three-way check — (a) no explicit parent link anywhere on the Data page, (b) no KR metric that is a company metric or a stated driver of one, (c) no mention of data, reporting or analytics on the company priorities page. Zero of three.
- Disconfirming checks run: `no parent link ≠ orphan` — searched the Data page for its own justification or charter text that could downgrade or kill the finding; the only justification-shaped text is "we've sized our part at 3 engineer-months" (line 82), an absolute size rather than a stated fraction of team capacity, so the finding stays Minor instead of escalating to Major. Re-read the priorities page for an implicit parent (a measurement dependency under C1–C4) — none is stated.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to attach D1 to a stated Q3 priority or to record it explicitly as platform-health investment outside the company OKR tree — at the next portfolio review.

## 5. Prioritized action list

1. Name an owning team for company priority C4 or move it out of Q3 — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Re-sequence Growth's Aug 15 upgrade launch against Payments' Sep 26 billing API v2 GA, or cut an earlier usable API milestone — owner: Priya N. (Payments) with Marcus T. (Growth) (resolves §4 AL-06 Timeline mismatch).
3. Agree a checkout guardrail pair (chargeback ceiling plus conversion floor) before step-up coverage ramps — owner: Priya N. (Payments) with Marcus T. (Growth) (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Replace Platform's developer-satisfaction KR with a named-instrument survey measure and a stated baseline — owner: Elena R. (Platform) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
5. Replace Data's "Significantly improve data quality across core tables." with a defined, testable quality measure — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
6. Publish a Q3 Platform allocation for the PCI-scoped infra and the streaming pipeline migration, or declare that neither lands — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
7. Get the streaming pipeline migration onto Platform's plan or re-scope D1.1 to Data-only work — owner: Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
8. Assign a single owner, target and definition for new-user activation — owner: Marcus T. (Growth) with Jonas K. (Data) (resolves §4 AL-03 Duplicated / overlapping objectives).
9. Rebaseline Platform's uptime KR against the quoted 99.95% trailing actual — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target).
10. Add a baseline to Growth's trial-to-paid KR and replace the blog-pageview KR with a signup-attributed measure — owner: Marcus T. (Growth) (resolves §3 AP-04 KR Without Baseline, AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.2); Critical §3 AP-09 Metric Nobody Can Measure, plus inbound §4 AL-07 Resource contention and AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3) of the Brightledger Q3 2026 portfolio export at /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md; strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Data** (roll-up C (2.3); Critical §3 AP-09 Metric Nobody Can Measure, plus §4 AL-01 Unacknowledged dependency and AL-04 Orphan objective): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3) of the Brightledger Q3 2026 portfolio export at /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md; strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Growth** (roll-up C (2.6); Critical §4 AL-06 Timeline mismatch and AL-02 Conflicting metrics / adversarial incentives): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3) of the Brightledger Q3 2026 portfolio export at /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md; strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Payments** (roll-up B (3.1), above the needs-rework threshold, but qualifies on Critical §4 AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3) of the Brightledger Q3 2026 portfolio export at /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture1-portfolio/input/sample-portfolio.md; strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
