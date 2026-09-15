# OKR-Ninja Portfolio Review — Brightledger, Q3 2026

## 1. Executive summary

**Verdict: At risk. The Q3 2026 plan cannot be carried out as written.**
4 teams reviewed (Payments, Growth, Platform, Data), in portfolio mode, with the Company Q3 2026 priorities as the strategy source. Findings: 6 Critical, 7 Major, 1 Minor.
The biggest alignment risk is AL-07 Resource contention. Payments and Data both expect Platform to do infra work in Q3, but Platform is holding all non-critical infra requests until Q4. Payments' dependent API v2 GA also gates Growth's upgrade launch, which is dated six weeks before that GA (AL-06 Timeline mismatch).
Company priority C4 (the Brightledger Capital pilot) has no contributing objective or KR on any team (AL-10 Strategy coverage gap).
Growth and Data both target new-user activation from the same 31% baseline, but set different targets and don't mention each other (AL-03 Duplicated / overlapping objectives).
The most common quality problem is AP-04 KR Without Baseline: 4 KRs across Growth, Platform and Data. Two more KRs (Platform, Data) are Critical AP-09 Metric Nobody Can Measure.
Recommended first action: this week, the CEO names an owner for C4, and Platform meets with Payments and Data to re-plan Q3 infra capacity.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Data | 2 | 3 | 3 | 1 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.32) · Growth C (2.68) · Payments B (2.77).
- Platform: K1/K3/K5/K6/K7=2 — sandbagged uptime target, unmeasurable dev-satisfaction KR, binary SOC 2 KR.
- Data: O4=1 — objective D1 traces to no company priority (AL-04 Orphan objective).
- Growth: O2=2 — both objectives rest on vague abstractions (magical, machine).
- Payments: K1/K3/K5=2 — API v2 KR is a dated deliverable; no metric sources named.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Evidence: "Keep the lights on, cheaper" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: The file never names a survey, instrument or system for a "developer satisfaction score". I searched the company priorities, all four team pages and the Q2 appendix; the only named instrument is Datadog, for uptime. With no source and no current value, the 8/10 can't be scored honestly or judged for ambition. Developer satisfaction also has no short causal link to an objective about uptime and cost, so hitting it would not show the objective happened.
- Scores affected: K1=1, K5=1, K3=2, K7=2
- Suggested rewrite: "KR: Sev-1/Sev-2 production incidents per month `<baseline>` → `<target>` (source: `<incident tracker report>`)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: The committed target is below the Q2 trailing actual in the same file. The team can meet it without doing anything new, and even while uptime gets worse.
- Scores affected: K3=1
- Suggested rewrite: "KR: Raise API uptime (trailing 90 days, Datadog SLO monitor) from 99.95% to `<target>`%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: This is a completion task, with no metric, no starting point and nothing measured outside the team. Mid-quarter it can only read 0% or 100%, so it gives no steering signal about whether enterprise trust is being earned.
- Scores affected: K1=0, K2=1, K6=2
- Suggested rewrite: "KR: SOC 2 Type II controls with auditor-accepted evidence `<0/N>` → `<N/N>` by `<date>`, final audit report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Also: AP-04 KR Without Baseline
- Why it's a problem: "Data quality" is not defined as a metric, and no test, check or dashboard is named for it. "Significantly" gives no size of change, and I found no current value on the Data page or in the Q2 appendix. The one instrument on the page, the reconciliation check in KR D1.1, measures cross-source discrepancies, not core-table quality. As written, this KR can never be scored honestly.
- Scores affected: K1=0, K5=0, K3=2
- Suggested rewrite: "KR: Share of core tables failing automated data-quality tests (nulls, uniqueness, freshness) `<baseline>`% → `<target>`%, measured daily by `<data-quality test suite>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Evidence: "Turn our funnel into a machine" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 43)
- Also: AP-04 KR Without Baseline
- Why it's a problem: Pageviews rise with exposure and spend, and don't show that the funnel converts efficiently. No current pageview figure appears anywhere in the file (Growth page or Q2 appendix), so 50,000 can't be judged as a stretch.
- Scores affected: K2=2, K1=2, K3=2
- Suggested rewrite: "KR (aspirational): Qualified signups sourced from the blog `<baseline>`/mo → `<target>`/mo." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: The KR gives no starting value. I searched the Growth page and the Q2 appendix, which reports only uptime, chargeback, step-up and qualified-signup figures. With no trial-to-paid figure anywhere, 22% can't be judged as a stretch or a sandbag, and progress can't be read.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR: Trial-to-paid conversion (monthly trial cohorts, `<billing analytics report>`) from `<Q2 actual>`% to 22%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient · AP-14 Date as Target
- Why it's a problem: Shipping is an output, and the only way to fail is to be late. The KR is done/not-done and succeeds even if no checkout traffic or upgrade flow ever uses the API, so it says nothing about whether customers stop thinking about checkout.
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR: Share of card checkout sessions served by checkout & billing API v2 0% → `<target>`% by Sep 26, with authorization error rate ≤ `<threshold>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company evidence: "C4 — Launch Brightledger Capital:" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Company evidence: "invoice-financing pilot live with 3 design partners by Sep 30." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (closest match found): "first invoice sent within 7 days" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Conflict: A committed, dated company priority has zero contributing objectives or KRs across all four teams, so nobody is on the hook for the pilot by its date.
- Detection check that fired: Top-down strategy trace (AL-10 heuristic). I checked each company priority for contributing objectives or KRs. C1 has contributors by metric linkage (Growth), C2 has Platform's SOC 2 and uptime work, C3 has Payments P2, and C4 has none.
- Disconfirming checks run: Zero hits ≠ coverage gap. I searched all four team pages (lines 17–82) for "Capital", "financing", "lending", "pilot", "design partner", "credit", "C4" and "invoice". The only hit is Growth's activation definition, which is about invoicing activity, not invoice financing, so it doesn't count as coverage. The company page assigns C4 to no named function outside the four teams; the only owner shown is the page owner. Result: the gap stands.
- Inference labels: none — all load-bearing text quoted
- Verdict: CONFIRMED
- Recommended resolution owner: Dana W. (CEO, owner of the priorities page) should, within 1 week, either name an owning team for C4 and add a pilot KR to that team's Q3 OKRs, or formally drop C4 for the quarter.

### [Critical] AL-07 Resource contention: Payments ↔ Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Two teams' committed Q3 plans need Platform's Q3 infra capacity: Payments' PCI-scoped infra in July, and Data's streaming pipeline. Platform says Q3 is fully committed and holds non-critical infra requests until Q4. Committed demand exceeds the declared supply and nobody has reconciled it. The default severity is Major; I raised it to Critical because this capacity sits on the critical path of the AL-06 and AL-01 findings below.
- Detection check that fired: Resource-node fan-in (AL-07 heuristic). Grouping resource mentions by owner put two Q3 claimants on Platform, and Platform's own page states a capacity constraint.
- Disconfirming checks run:
  - Plural demand ≠ contention: I searched Platform's page (lines 52–65) for any allocation to PCI, provisioning, payments, pipeline, streaming, schema or events. There were zero hits, and no capacity or allocation table is linked. No Jira was available (no Atlassian connection), so an off-page allocation could not be checked.
  - Same quarter: yes. Payments says "in July", and Data's schema v2 work sits inside its Q3 KR.
  - Same resource: yes. Platform is the only infra-owning team in the file.
  - Non-critical carve-out: neither ask is classified as critical anywhere on Platform's page.
  - Result: the finding stands.
- Inference labels: Resolving Data's "handled at the infra level" to Platform is analyst inference; Payments names Platform explicitly. Secondary cross-reference: AL-01 Unacknowledged dependency. Payments' provisioning ask is a pure capacity ask and folds into this finding; Data's missing pipeline deliverable is reported separately below.
- Verdict: CONFIRMED
- Recommended resolution owner: Elena R. (Platform lead) meets with Priya N. (Payments) and Jonas K. (Data) before `<date in July>`. They decide whether the PCI-scoped infra and the streaming pipeline are Q3-critical, then re-plan either Platform's Q3 KRs or the dependent Payments and Data KRs.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's committed upgrade launch on Aug 15 depends on the billing API that Payments commits to GA only on Sep 26. The consumer ships about six weeks before its dependency exists, which is a hard inversion on two committed KRs.
- Detection check that fired: Edge date comparison on the dependency map (AL-06 heuristic). The consumer's need-by date (Aug 15) comes before the producer's delivery date (Sep 26).
- Disconfirming checks run:
  - Late date ≠ inversion: I looked for a beta or early-access API v2 milestone that could serve Growth's integration before GA. None exists; the only API v2 date on Payments' page is the GA on Sep 26.
  - Commitment levels: both KRs are committed under each page's convention, "Commitment: KRs are committed unless marked (aspirational)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Payments team — Q3 2026 › line 19; /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Growth team — Q3 2026 › line 36).
  - Awareness plus a resolution plan: Growth's "should be fine" is an assurance with no date or plan, so it does not downgrade the finding.
  - Result: the finding stands.
- Inference labels: Matching Growth's "the new billing API" to Payments' "checkout & billing API v2" is analyst inference. It is supported by the note's reference to Priya, the Payments page owner, and by Payments' API being the only billing API in the file.
- Verdict: CONFIRMED
- Recommended resolution owner: Marcus T. (Growth) and Priya N. (Payments) should, within 1 week, agree either an early-access API v2 milestone before Aug 15 or a G1.3 launch date after GA with a re-sized upgrade target, and write the agreed date into both KRs.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Data's committed KR D1.1 needs a streaming pipeline migration, which is a distinct build that Data expects someone at the infra level to deliver. That migration appears nowhere in Platform's plans, and Platform has explicitly deferred non-critical infra work to Q4. The combined capacity arithmetic is reported once, under AL-07 above.
- Detection check that fired: Dependency extraction and producer-side search (AL-01 heuristic). "Rides on the streaming pipeline migration" resolves to an infra owner, and the owner's inventory has no matching deliverable.
- Disconfirming checks run: Missing mention ≠ unacknowledged. I searched Platform's page (lines 52–65) for "pipeline", "streaming", "migration", "schema", "event" and "data": zero hits. The closest items are PL1.2 (cloud spend) and PL2.2 (SOC 2 audit), and neither covers a pipeline migration. No Jira backlog was available to check for an unscheduled epic. Result: the finding stands. It is Critical because D1.1 is committed and Platform has explicitly deprioritized non-critical infra.
- Inference labels: Resolving "handled at the infra level" to Platform is analyst inference (Platform is the only infra-owning team in the file). Cross-reference: AL-07 Resource contention.
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data) with Elena R. (Platform) should, by `<date in July>`, decide who owns the streaming pipeline migration in Q3 and add it as a KR to that team's page, or re-scope D1.1 so it does not depend on schema v2 this quarter.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Data evidence: "Own onboarding personalization end-to-end" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 78)
- Conflict: Both teams target the same new-user activation metric from the same 31% baseline, with inconsistent targets (40% vs 35%). Data claims onboarding "end-to-end" while Growth's first-week objective covers the same surface, so it's unclear who is accountable for activation and which target counts.
- Detection check that fired: Clustering by target metric plus target population and surface (AL-03 heuristic; blocking key: same canonical metric + new-user onboarding population).
- Disconfirming checks run: Similar objectives ≠ duplication. I searched Growth's page (lines 34–48) and Data's page (lines 69–82) for any mention of the other team, a shared epic, a joint owner or a lane split. There were zero hits: Growth's notes mention only the billing API sync with Priya, and Data's notes mention only the pipeline. Population and surface split: both KRs say "new-user", with no segment, surface or geography division. Result: the finding stands.
- Inference labels: Data's KR doesn't define activation. Treating it as the same measurement as Growth's definition is analyst inference, supported by the identical metric name and identical 31% baseline. Secondary cross-reference: AL-08 Terminology collision (definition absent on Data's side).
- Verdict: CONFIRMED
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) should, within 2 weeks, agree one owner for the activation KR, one definition, one target, and a written lane split (for example, who owns onboarding checklists vs. first-week lifecycle).

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: Step-up verification is a friction control on transactions. Raising its coverage from 35% to 90% adds challenge steps to checkouts that include self-serve signups' payments, which works against Growth's committed ten-point checkout conversion lift. Neither team mentions the other or a guardrail.
- Detection check that fired: Surface-lever key (AL-02 key 2). Both KRs sit on the checkout/transaction surface; Payments' stated lever is a verification (friction) control, and Growth targets that surface's conversion. The metric-identity key (key 1) found no opposing same-metric pair. It generated Payments' "Raise checkout success rate from 91.2% to 95% for card transactions." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 22) against Growth's checkout conversion. I killed that pair as lookalike metrics with different definitions and populations (card transactions vs. self-serve signups), both pushed in the same direction with no control lever. That kill is per-candidate and does not suppress this pair.
- Disconfirming checks run:
  - Shared or parent OKR covering both: none found.
  - Documented lever split or guardrail: none on either page (lines 17–30, 34–48).
  - Directionality: coverage going up adds friction while conversion is pushed up, so they are opposed by mechanism.
  - Commitment: both are committed under their pages' conventions, so no Minor downgrade applies.
  - Payments' objective wording "Cut fraud losses without drama" hints at concern for side effects but names no conversion guardrail, so it does not kill the finding.
  - Result: the finding stands at Major.
- Inference labels: The friction→conversion mechanism is analyst inference (no team document states the tradeoff). That step-up verification applies on the self-serve checkout surface is also analyst inference, from "of transactions".
- Verdict: CONFIRMED
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) should, within 2 weeks, agree a shared guardrail pair (step-up coverage rollout capped where self-serve checkout conversion falls below `<conversion floor>`%, and chargeback rate ≤ `<fraud ceiling>`%) [proposal — placeholder target] and reference it in both KRs.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73)
- Company evidence: "C1 — Grow self-serve revenue:" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 10); "C2 — Become enterprise-ready:" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 11); "C3 — Cut fraud losses:" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 12); "C4 — Launch Brightledger Capital:" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Conflict: Data's first objective claims no company parent, and none of its KRs moves a company-level metric. The team's committed data work serves nothing the strategy names.
- Detection check that fired: Three-way strategy-trace check (AL-04 heuristic), 0 of 3.
  - (a) Explicit parent link: none on Data's page (lines 69–82); it never mentions "priority" or C1–C4.
  - (b) Metric linkage: D1's KRs measure exec-dashboard discrepancies, dashboard latency and data quality. None is a company metric (self-serve ARR, SOC 2 or reliability, chargeback rate, Capital pilot) or a stated driver of one.
  - (c) Strategy-page mention: the company priorities page mentions no data, dashboards, events or schema.
- Disconfirming checks run: No parent link ≠ orphan. The three-way check ran and gave 0 of 3. Data's page contains no justification of its own and no exploratory charter to quote. Capacity: "we've sized our part at 3 engineer-months" is an effort estimate, not a stated fraction of team capacity, so the finding stays Minor.
- Inference labels: none — all load-bearing text quoted
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data lead) should, before mid-quarter, either state which company priority D1 serves and add a KR on that priority's metric, or move D1 to a health or enablement section outside the Q3 OKRs.

## 5. Prioritized action list

1. Name an owning team and a pilot KR for C4 Brightledger Capital, or formally drop C4 for Q3 — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Meet with Payments and Data to decide whether the PCI-scoped infra and the streaming pipeline are Q3-critical, and re-plan Platform's capacity or the dependent KRs — owner: Elena R. (Platform lead) (resolves §4 AL-07 Resource contention).
3. Re-sequence Growth's Aug 15 self-serve upgrade launch against API v2's Sep 26 GA, either through an early-access milestone or a later launch date — owner: Marcus T. (Growth lead) with Priya N. (Payments lead) (resolves §4 AL-06 Timeline mismatch).
4. Assign Q3 ownership of the streaming pipeline migration as a KR, or re-scope D1.1 away from schema v2 — owner: Jonas K. (Data lead) (resolves §4 AL-01 Unacknowledged dependency).
5. Replace Platform's developer-satisfaction KR with an instrumented reliability KR that has a baseline — owner: Elena R. (Platform lead) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
6. Replace Data's "data quality" KR with a test-backed metric that has a baseline and target — owner: Jonas K. (Data lead) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
7. Merge the two activation KRs into one owner, one definition and one target, with a written lane split — owner: Marcus T. (Growth lead) with Jonas K. (Data lead) (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Agree a joint step-up-coverage / checkout-conversion guardrail pair and reference it in both KRs — owner: Priya N. (Payments lead) with Marcus T. (Growth lead) (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
9. Rewrite Platform's uptime KR against the quoted 99.95% baseline and its SOC 2 KR as graded control progress — owner: Elena R. (Platform lead) (resolves §3 AP-06 Sandbagged Target and AP-01 Task Masquerading as KR — Platform).
10. Rewrite Growth's trial-to-paid and blog-pageview KRs with stated baselines and a signup-outcome metric, and Payments' API v2 KR as an adoption measure — owners: Marcus T. (Growth lead) and Priya N. (Payments lead) (resolves §3 AP-04 KR Without Baseline and AP-03 Vanity Metric — Growth; AP-01 Task Masquerading as KR — Payments).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.15), above the needs-rework threshold; Critical findings: AP-09 Metric Nobody Can Measure, and resource owner in AL-07 Resource contention and AL-01 Unacknowledged dependency): re-run in single-team mode — `Review the Platform team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md, section "Platform team — Q3 2026" (lines 52–65; Q2 actuals in the Appendix, lines 86–91); strategy doc: "Company Q3 2026 priorities" in the same file (lines 7–13).`
- **Data** (roll-up C (2.32), above the needs-rework threshold; Critical findings: AP-09 Metric Nobody Can Measure and AL-01 Unacknowledged dependency, plus claimant in AL-07 Resource contention): re-run in single-team mode — `Review the Data team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md, section "Data team — Q3 2026" (lines 69–82); strategy doc: "Company Q3 2026 priorities" in the same file (lines 7–13).`
- **Payments** (roll-up B (2.77), above the needs-rework threshold; Critical findings: claimant in AL-07 Resource contention, producer in AL-06 Timeline mismatch): re-run in single-team mode — `Review the Payments team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md, section "Payments team — Q3 2026" (lines 17–30; Q2 actuals in the Appendix, lines 86–91); strategy doc: "Company Q3 2026 priorities" in the same file (lines 7–13).`
- **Growth** (roll-up C (2.68), above the needs-rework threshold; Critical finding: consumer in AL-06 Timeline mismatch): re-run in single-team mode — `Review the Growth team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md, section "Growth team — Q3 2026" (lines 34–48; Q2 actuals in the Appendix, lines 86–91); strategy doc: "Company Q3 2026 priorities" in the same file (lines 7–13).`
