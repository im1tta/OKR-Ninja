## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed (Payments, Growth, Platform, Data; Q3 2026; portfolio mode; strategy source: the Company Q3 2026 priorities section); 14 findings: 3 Critical, 10 Major, 1 Minor.
The single worst alignment risk is AL-10 Strategy coverage gap: company priority C4, the Brightledger Capital invoice-financing pilot due Sep 30, has no team work in any of the four OKR sets.
Behind it sits a dependency chain: Growth launches its self-serve upgrade flow by Aug 15 on the billing API that Payments ships to GA by Sep 26 (AL-06 Timeline mismatch), and that GA waits on PCI-scoped infra from Platform, which, like Data's streaming pipeline migration, lands in a quarter Platform declares fully committed (AL-07 Resource contention; AL-01 Unacknowledged dependency).
Growth and Data both commit new-user activation from 31%, to 40% and to 35% (AL-03 Duplicated / overlapping objectives), and Payments' step-up verification push can undercut Growth's checkout-conversion target (AL-02 Conflicting metrics / adversarial incentives).
The most common goodness anti-pattern is AP-04 KR Without Baseline (3 KRs across Growth and Platform); the one Critical goodness finding is Data's unmeasurable data-quality KR (AP-09 Metric Nobody Can Measure).
Roll-ups: Payments B (2.86), Growth C (2.69), Platform C (2.40), Data C (2.25); none is at the needs-rework threshold, but Critical findings route Data, Growth and Payments to single-team re-runs (§6).
Recommended first action: the priorities owner (Dana W., CEO) assigns C4 to a named team while Platform, Payments and Growth settle Platform's Q3 infra allocation and the API v2 dates before July.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |
| Platform | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.25) · Platform C (2.40) · Growth C (2.69) · Payments B (2.86).
- Data: O4=1 — objective D1 traces to no company priority (AL-04 Orphan objective).
- Platform: K3=2 — uptime target below the Q2 review's 99.95% (AP-06 Sandbagged Target).
- Growth: K1=2 — trial-to-paid and blog KRs lack baselines (AP-04 KR Without Baseline).
- Payments: K1=2 — API v2 KR is a dated milestone (AP-01 Task Masquerading as KR).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "improve" gives a direction and "Significantly" an unquantified degree, but the KR names no data-quality metric, baseline, target number or system of record, and none appears anywhere in the file. The only named check on Data's page belongs to KR D1.1 (line 74), counts cross-source metric discrepancies, and is not referenced by D1.3. So the KR can never be honestly scored.
- Scores affected: K1=1, K5=0, K3=2 (KR score capped at 1.0; objective D1 capped at 1.9 by the Critical cap)
- Suggested rewrite: "KR D1.3: Share of core-table rows passing the `<named data-quality test suite>` checks, weekly: `<baseline>`% → `<target>`% (source: `<data-quality monitor>`)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target is below the only uptime actual in the document. PL1.1 can therefore be met with uptime below the 99.95% trailing-90-day figure that the Q2 business review already reports. A maintain target set under the prior actual asks for nothing new, while company priority C2 (line 11) asks to hold enterprise-grade reliability. PL1.1 names no window or source, so this reading assumes the same Datadog SLO measure.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime (Datadog SLO monitor, trailing 90 days) at or above 99.95% in every month of Q3, rising to `<target>`% by quarter end." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Evidence: "Keep the lights on, cheaper" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56)
- Also: AP-04 KR Without Baseline
- Why it's a problem: PL1 is about keeping systems running at lower cost; its other KRs are API uptime and cloud spend per 1,000 transactions (lines 57–58). Developer satisfaction shares no noun with it and the page states no causal link, so nothing on the page supports reading 8/10 as progress on the objective. The KR also states no starting value. No developer-satisfaction figure appears in Platform's section (lines 52–65) or the Q2 review (lines 86–91), so 8/10 cannot be judged as either a stretch or a sandbag.
- Scores affected: K1=2, K3=2, K5=2; PL1 set K7=2
- Suggested rewrite: "KR PL1.3: Sev-1 incident minutes per month `<baseline>` → `<target>` (source: `<incident tracker>`)." [proposal — placeholder target], and move the survey KR under a developer-experience objective as "KR: Internal developer satisfaction, `<named quarterly survey>` (n ≥ `<n>`): `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable with no metric, no baseline→target pair and no result measure, so mid-quarter it can only read done or not done. Company priority C2 names the same deliverable (line 11), so the portfolio has no progress signal on that part of C2 until the audit ends.
- Scores affected: K1=0, K2=1 (KR score capped at 1.0; PL2 capped at 2.4 by two Major anti-patterns)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II controls with auditor-accepted evidence `<baseline>`/`<total>` → `<total>`/`<total>`, final audit report received by `<date>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the KR states no starting value, and no trial-to-paid figure appears anywhere in the file. Searched: Growth's section (lines 34–48), the company priorities (lines 7–13) and the Q2 review (lines 86–91), whose Growth line reports only qualified signups. So 22% cannot be judged as a stretch or a sandbag, and the quarter's movement cannot be tracked.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion (trials started in the quarter, paid within `<n>` days): `<Q2 actual>`% → 22% (source: `<billing analytics report>`)." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Evidence: "Turn our funnel into a machine" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 43)
- Also: AP-04 KR Without Baseline
- Why it's a problem: G2 is about a funnel that converts; its other KRs are checkout conversion and qualified signups (lines 44–45). Nothing on Growth's page links blog pageviews to signups or conversion, so 50,000 pageviews can be reached while the funnel stands still. The KR also states no starting value and none is found (lines 34–48 and 86–91), so the target is uncalibrated. The "(aspirational)" label changes neither problem.
- Scores affected: K2=2, K1=2, K3=2
- Suggested rewrite: "KR G2.3 (aspirational): Qualified signups attributed to blog content `<baseline>`/mo → `<target>`/mo (source: `<attribution report>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR measures a delivery, with no metric, no baseline→target pair and no outcome measure such as adoption or usage of v2. Mid-quarter it can only read done or not done. Other plans depend on it: Growth's note says its self-serve upgrades (G1.3) "will use the new billing API" (line 48). The note does not name v2. Reading it as this API rests on the note naming Priya, who owns the Payments page (line 18), and on v2 being the only billing API in the file.
- Scores affected: K1=0, K2=1 (KR score capped at 1.0; P1 capped at 2.4 by two Major anti-patterns)
- Suggested rewrite: "KR P1.2: Checkout & billing API v2 GA by Sep 26 and carrying `<target>`% of billing API calls, including Growth's self-serve upgrade flow, by quarter end, with error rate ≤ `<threshold>` (source: `<API gateway dashboard>`)." [proposal — placeholder target]

## 4. Alignment findings

Blocking keys used:
- the dependency map (Growth → Payments, Payments → Platform, Data → "the infra level"), with Platform as a shared-resource node;
- the strategy trace of all 8 objectives against C1–C4;
- metric identity (new-user activation rate; chargeback rate vs C3);
- surface-lever on checkout / payment transactions (step-up verification vs checkout conversion; transaction cost vs latency and conversion);
- same metric + population (activation / new users; checkout);
- metric names shared across teams;
- metrics with two or more stated baselines (activation, chargeback rate, step-up coverage, qualified signups, API uptime).

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's committed launch (Aug 15) falls six weeks before the committed GA of the API that the launch will use. Payments commits only to GA "by Sep 26"; if GA lands on that deadline, a launch at GA leaves only Sep 26–30 of the quarter for the 300 upgrades. Neither KR is marked aspirational, so both are committed under their pages' stated default (lines 19 and 36).
- Detection check that fired: AL-06 edge date comparison on the dependency map. The consumer's need-by (Aug 15) comes before the producer's delivery (GA by Sep 26), a hard inversion. The quarter-boundary comparison leaves at most Sep 26–30 for the volume target.
- Disconfirming checks run:
  - Late date ≠ inversion: searched Payments' page (lines 17–30) for beta, preview, pilot, early access, alpha and Aug. No earlier milestone exists; GA is the only quotable v2 milestone → the inversion stands.
  - Soft-date check: both dates are firm → not weakened.
  - Hedging: Growth's "should be fine" gives no date or pre-GA access. Payments' page was last updated 2026-07-02, after the June sync, and still dates GA Sep 26 without mentioning Growth or upgrades → not weakened.
  - Jira due dates: no Jira in scope; both dates come from OKR text.
- Inference labels:
  - analyst inference — "the new billing API" (line 48) is the "checkout & billing API v2" (line 23), because v2 is the only billing API in the file and Priya N. owns the Payments page (line 18);
  - analyst inference — Q3 ends Sep 30 (calendar quarter, consistent with C4's "by Sep 30", line 13).
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Growth (Marcus T.) convenes Payments (Priya N.) before Aug 15. They either add a dated pre-GA billing-API milestone for the upgrade flow to Payments' page, or move G1.3's launch after GA and re-set its 300-upgrade target. Decide this together with Platform's allocation (AL-07 Resource contention, below), because v2 GA itself waits on Platform.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company priorities evidence: "C4 — Launch Brightledger Capital" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Company priorities evidence: "invoice-financing pilot live with 3 design partners by Sep 30." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Conflict: this dated company priority has no team work in the portfolio stated as contributing to it. No objective, KR or note of the four teams (lines 17–82) mentions Brightledger Capital, financing, lending, credit, a pilot or design partners, and C4 names no owning team. The line-40 Growth KR is the closest near-miss, but it concerns invoicing activation, not invoice financing.
- Detection check that fired: AL-10 top-down strategy trace. C4 has zero contributing children, while C1 ← Growth (by inference), C2 ← Platform (by inference) and C3 ← Payments (explicit).
- Disconfirming checks run:
  - Zero hits ≠ coverage gap: re-searched every team section and the Q2 review under synonyms and program names (Capital, financing, invoice financing, lending, loan, credit, underwriting, receivables, pilot, design partner, Sep 30). The only hits are the line-40 near-miss and Payments' billing API (line 23), which states no financing scope → the gap stands.
  - Named owner outside the swept teams: C4's line names none, and the page owner (line 8) owns the whole priorities page rather than C4 → not an ownership note.
  - Aspirational label: C4 is not marked aspirational → no downgrade.
  - Linked epics: no Jira in scope.
- Inference labels:
  - analyst inference — C4 is read as committed: the priorities page uses no commitment labels, and C4 is dated and not marked aspirational. It sits on the CEO-owned priorities page, so it is exec-visible either way;
  - analyst inference — the export holds four teams; if a team outside it owns C4, this becomes an ownership note. Nothing in the file names such a team.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Dana W. (CEO, owner of the priorities page), with the four team owners at the first Q3 check-in. Options: assign C4 to a named team with Q3 KRs for the pilot and its 3 design partners, add the owning team's OKRs to this review, or formally re-date C4.

### [Major] AL-07 Resource contention: Payments, Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two committed Q3 KRs assume Platform infrastructure work this quarter: Payments' P1.2 (API v2 GA) and Data's D1.1 (schema v2 target). Platform's own page declares Q3 fully committed to SOC 2 and cost work, holds non-critical infra requests until Q4, and allocates nothing to either ask. The source does not say whether either request would count as critical.
- Detection check that fired: AL-07 resource-node fan-in. Grouping dependency mentions by resource puts two Q3 claimants on Platform, whose page states a capacity constraint (fully committed). The contention is therefore one aggregate candidate quoting both claimants and the owner's capacity statement.
- Disconfirming checks run:
  - Plural demand ≠ contention: searched Platform's section (lines 52–65) for PCI, provisioning, API v2, payments, checkout, stream, pipeline, migration, schema, event and data. There is no allocation or item for either claimant, and no Jira or capacity table in scope → not falsified.
  - Same quarter: both claimant KRs are Q3 KRs, and Payments' need-by is July → passes.
  - Same resource: Payments names Platform, and Data's "the infra level" resolves to Platform by inference → passes, with a labeled inference.
  - AL-01 disambiguation: Payments' ask is provisioning, a pure capacity ask, so it folds into this finding with AL-01 Unacknowledged dependency as secondary. Data's migration is a distinct deliverable and also gets its own AL-01 finding below.
- Inference labels:
  - analyst inference — Data's "the infra level" means Platform. Platform's page is the only one that handles "infra requests" (line 65), and Payments also looks to Platform for infra (line 30);
  - analyst inference — both needs fall in Q3. Data states no need-by date (D1.1 is a Q3 KR), and Payments' "in July" is read as Q3 on a calendar-quarter basis.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Platform (Elena R.) convenes Payments (Priya N.) and Data (Jonas K.) before July to decide whether PCI-scoped infra and the streaming pipeline migration are funded in Q3 alongside SOC 2 and the cost work. For anything deferred, Payments re-dates P1.2 (and with it Growth's G1.3, per AL-06 Timeline mismatch) and Data re-scopes D1.1. Escalate to the priorities owner (Dana W., CEO) if there is no agreement.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: D1.1's committed 14 → 0 target depends on a streaming pipeline migration. Data keeps the migration out of its own sizing and expects "the pipeline itself to be handled at the infra level". No other team's section mentions a streaming pipeline, a migration, schema or event work, so no team has committed to it. The closest near-miss is Platform's only reference to other teams' infra requests, the Q4 hold on non-critical ones, which does not say whether the migration would count as critical.
- Detection check that fired: AL-01 dependency extraction. The phrases "rides on" and "handled at the infra level" name external work, and searching the resolved owner's page found no matching item. Under the AL-07 disambiguation rule this edge names a distinct deliverable, a migration the producer would have to plan as its own project. It therefore earns its own AL-01 as well as counting as an AL-07 claimant.
- Disconfirming checks run:
  - Missing mention ≠ unacknowledged: searched Platform (lines 52–65), Payments (lines 17–30) and Growth (lines 34–48) for stream, pipeline, migration, schema and event. No hits, and no Jira or backlog in scope → not killed.
  - Data's own work: Data's note keeps the pipeline itself out of its 3 engineer-months → not Data's.
  - Capacity-ask fold-in: a migration is a project, not a provisioning or review-bandwidth ask → stands as its own finding.
- Inference labels: analyst inference — the producer is Platform, on the same basis as the AL-07 Resource contention finding above. The absence holds for every team in the file, whoever "the infra level" is.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Data (Jonas K.) with Platform (Elena R.), inside the AL-07 allocation decision before July. Either put the streaming pipeline migration on a named owner's page as a dated Q3 item, or re-scope D1.1's schema v2 path and its 14 → 0 target. The capacity arithmetic stays with AL-07 Resource contention.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Growth evidence: "Make the first week with Brightledger magical" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 38)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Data evidence: "Own onboarding personalization end-to-end" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 78)
- Conflict: two teams each commit a Q3 target for the same metric on the same population, from the same 31% baseline: 40% vs 35%. Neither page mentions the other team or a split of the work, so it is unclear who is accountable for new-user activation and which committed number counts. Data claims onboarding "end-to-end" while Growth owns the first-week outcome.
- Detection check that fired: AL-03 clustering by target metric + population. "new-user activation rate" on the new-user / first-week population appears in both teams' KRs, with no cross-reference, shared epic, joint owner or split inside the cluster.
- Disconfirming checks run:
  - Similar objectives ≠ duplication: neither KR states a different population or segment; Data's "via onboarding experiments" names a lever, not a sub-population → not disconfirmed.
  - Cross-references: searched Growth (lines 34–48) for Data, Jonas, onboarding and personalization, and Data (lines 69–82) for Growth, Marcus, first invoice and first week. No hits.
  - Parent that assigns lanes: the company priorities (lines 7–13) mention neither activation nor onboarding.
  - Shared epics: no Jira in scope.
  - Shared metric ≠ conflict: same direction and nested targets, so the pair is duplication rather than an adversarial conflict. The two baselines agree (31% on both).
- Inference labels: analyst inference — Data's undefined "new-user activation rate" is the same measure as Growth's defined one (same name, same 31% baseline).
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Growth (Marcus T.) convenes Data (Jonas K.) before the first Q3 check-in to:
  - agree one accountable owner and one committed Q3 activation target (40% or 35%);
  - write any split on both pages, for example Data's personalized onboarding as a named contribution;
  - have D2.2 adopt Growth's definition, "first invoice sent within 7 days".

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: Payments' stated lever is a verification step applied to far more transactions (35% → 90%), while Growth commits to lifting checkout conversion for self-serve signups. If self-serve checkout payments fall inside P2.2's scope, the added verification friction would likely cost some conversions, so pushing P2.2 can work against G2.1. Neither page mentions the trade-off, an exemption or a shared guardrail.
- Detection check that fired: AL-02 surface-lever key. Both KRs sit on the checkout / payment surface, P2.2's stated lever there is a verification step (a friction control), and G2.1 targets that surface's conversion metric. The metric-identity key generates nothing for this pair, since the KRs share no metric.
- Disconfirming checks run:
  - Shared metric ≠ conflict, directionality: different metrics with a mechanism-level opposition → survives at Major rather than Critical.
  - Explicit shared or parent OKR covering both: none (P2 cites C3 at line 30; G2 cites no parent) → survives.
  - Documented split of levers, exemption or guardrail: searched both pages (lines 17–48) for exempt, guardrail, friction, trade-off and step-up; the only hit is line 28 itself → none.
  - Aspirational clause: neither KR is marked aspirational → no downgrade.
- Inference labels:
  - analyst inference — the mechanism (added verification friction lowers checkout conversion); no text in the file states it;
  - analyst inference — self-serve signup checkout payments are among the "transactions" P2.2 covers. P2.2 states no carve-out. Payments frames checkout in terms of card transactions (line 22) and ships the checkout & billing API v2 (line 23), and Growth's self-serve upgrades (G1.3) "will use the new billing API" (line 48). No line says whether signup checkout (G2.1) is subject to step-up verification.
- Verdict: CONFIRMED (both KR quotes re-verified character-for-character; mechanism and shared surface carried as labeled inferences)
- Recommended resolution owner: Payments (Priya N.) convenes Growth (Marcus T.) before step-up coverage is pushed past its Q2 level of 35% (line 90). First confirm whether self-serve signup checkout is inside P2.2's 90% scope. If it is, agree either a risk-based step-up rule for that path or a guardrail pair: a `<conversion floor>` on P2.2 and a `<chargeback-rate ceiling>` on G2.1 [proposal — placeholder target]. Escalate to the priorities owner (Dana W., CEO) if C3 and C1 trade off.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73)
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Data evidence: "Cut critical-dashboard data latency from 6h to 1h." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 75)
- Company priorities evidence: "C1 — Grow self-serve revenue" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 10)
- Company priorities evidence: "C2 — Become enterprise-ready" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 11)
- Company priorities evidence: "C3 — Cut fraud losses" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 12)
- Company priorities evidence: "C4 — Launch Brightledger Capital" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Conflict: D1 states no link to any company priority. None of its KR metrics (cross-source metric discrepancies, dashboard data latency, data quality) is a company-level metric or a stated driver of one, and the priorities page names no data, dashboard or metric-quality work. Yet Data's own part of the schema v2 rollout is sized at "3 engineer-months" (line 82).
- Detection check that fired: AL-04 three-way check on the strategy trace: (a) explicit parent link: none; (b) KR metric that is a company-level metric or a documented driver of one: none; (c) mention on the strategy page: none → 0 of 3.
- Disconfirming checks run:
  - No parent link ≠ orphan: searched Data's section (lines 69–82) for priority, C1–C4, strategy, leadership and parent. None found.
  - Reasonable metric linkage: tested each priority (C1 self-serve ARR; C2 SOC 2 and reliability, which the Q2 review measures as API uptime, line 89; C3 chargeback rate; C4 the Capital pilot). None found. The general argument that trustworthy executive data helps every priority was rejected as not a metric linkage.
  - Team's own justification (could downgrade): none on the page.
  - Exploratory charter (could kill): none.
  - Capacity (the Major trigger): 3 engineer-months is stated but team size is not, so no fraction of capacity is stated → Minor.
- Inference labels: analyst inference — that no D1 metric drives a C1–C4 metric is a judgment from the absence of any stated mechanism.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the file)
- Recommended resolution owner: Data (Jonas K.) with the priorities owner (Dana W., CEO), before the schema v2 engineer-months are spent. Options: name the C1–C4 metric D1 moves and how, record D1 as accepted non-priority work, or re-scope it.

## 5. Prioritized action list

1. Assign company priority C4 (the Brightledger Capital pilot due Sep 30) to a named team with Q3 KRs, or add its owning team's OKRs to this review — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Re-sequence Growth's Aug 15 upgrade-flow launch against Payments' Sep 26 API v2 GA, either with a dated pre-GA milestone on Payments' page or by moving G1.3 and re-setting its 300-upgrade target — owner: Growth lead Marcus T. with Payments lead Priya N. (resolves §4 AL-06 Timeline mismatch).
3. Replace KR D1.3 with a defined data-quality metric, baseline, target and named monitor, and state which company priority objective D1 serves — owner: Data lead Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure and §4 AL-04 Orphan objective).
4. Decide before July whether Platform funds Payments' PCI-scoped infra and Data's streaming pipeline migration in Q3 alongside the SOC 2 and cost work, and re-date the dependent KRs for anything deferred — owner: Platform lead Elena R. (resolves §4 AL-07 Resource contention).
5. Get the streaming pipeline migration onto a named owner's page as a dated Q3 item, or re-scope D1.1's schema v2 path and its 14 → 0 target — owner: Data lead Jonas K. (resolves §4 AL-01 Unacknowledged dependency).
6. Agree one accountable owner and one committed Q3 new-user activation target (40% or 35%), and write the split on both pages — owner: Growth lead Marcus T. with Data lead Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
7. Confirm whether self-serve signup checkout sits inside the 90% step-up scope and, if it does, pair P2.2 and G2.1 with a conversion floor and a chargeback-rate ceiling — owner: Payments lead Priya N. with Growth lead Marcus T. (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
8. Rebase PL1.1 on the quoted 99.95% trailing uptime, restate PL2.2 as graded SOC 2 control-evidence progress, and move PL1.3 to a developer-experience objective with a baseline — owner: Platform lead Elena R. (resolves §3 AP-06 Sandbagged Target, §3 AP-01 Task Masquerading as KR and §3 AP-12 Orphan KR).
9. Add baselines to G1.1 and G2.3 and replace blog pageviews with a conversion-linked measure — owner: Growth lead Marcus T. (resolves §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).
10. Restate P1.2 with an adoption measure for API v2 alongside its Sep 26 GA date — owner: Payments lead Priya N. (resolves §3 AP-01 Task Masquerading as KR).

## 6. Suggested single-team re-runs

- **Data** (roll-up C (2.25), above the needs-rework threshold; Critical finding §3 AP-09 Metric Nobody Can Measure): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Data team — Q3 2026' (lines 69–82; Confluence page 88225, DATA-OKR-Q3), with Q2 baselines from the section 'Appendix — Q2 2026 business review (extracts)' of the same file (lines 86–91; Confluence page 88104, Q2-REVIEW). Strategy doc: the section 'Company Q3 2026 priorities' of the same file (lines 7–13; Confluence page 88101, CO-PRIO-Q3)."
- **Growth** (roll-up C (2.69), above the needs-rework threshold; Critical finding §4 AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Growth team — Q3 2026' (lines 34–48; Confluence page 88217, GRW-OKR-Q3), with Q2 baselines from the section 'Appendix — Q2 2026 business review (extracts)' of the same file (lines 86–91; Confluence page 88104, Q2-REVIEW). Strategy doc: the section 'Company Q3 2026 priorities' of the same file (lines 7–13; Confluence page 88101, CO-PRIO-Q3)."
- **Payments** (roll-up B (2.86), above the needs-rework threshold; Critical finding §4 AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Payments team — Q3 2026' (lines 17–30; Confluence page 88213, PAY-OKR-Q3), with Q2 baselines from the section 'Appendix — Q2 2026 business review (extracts)' of the same file (lines 86–91; Confluence page 88104, Q2-REVIEW). Strategy doc: the section 'Company Q3 2026 priorities' of the same file (lines 7–13; Confluence page 88101, CO-PRIO-Q3)."
- **Platform**: no re-run. Roll-up C (2.40) is above the needs-rework threshold. Its only Critical-rated involvement is as one of the four teams swept for §4 AL-10 Strategy coverage gap, a company-level gap that no single-team review can close.
