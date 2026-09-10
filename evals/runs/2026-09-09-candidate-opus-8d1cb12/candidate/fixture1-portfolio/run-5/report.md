# Brightledger — Q3 2026 OKR portfolio review

*Mode: portfolio (4 teams in scope: Payments, Growth, Platform, Data). Period: Q3 2026, as stated by the source file. Source: `sample-portfolio.md` (local export; no Atlassian connection available). Strategy source: the file's "Company Q3 2026 priorities" section (C1–C4). All source refs below use the local-file form `<file path> › <nearest heading> › line N` against that file.*

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 6 Critical, 8 Major, 1 Minor findings.

The portfolio's biggest threat is **AL-02 Conflicting metrics / adversarial incentives**: Payments is taking step-up verification from 35% to 90% of transactions while Growth commits to a 10-point lift in checkout conversion on the same surface — neither team's page mentions the other, and no guardrail pairs the two numbers.

Three of the four Critical alignment findings converge on delivery sequencing: Growth's committed Aug 15 launch depends on a Payments API that reaches GA on Sep 26 (**AL-06 Timeline mismatch**), and Data's committed schema-v2 migration assumes infra work that appears nowhere in Platform's OKRs (**AL-01 Unacknowledged dependency**) — while Platform's own page declares Q3 fully committed and defers non-critical infra requests to Q4 (**AL-07 Resource contention**).

Company priority C4 (Brightledger Capital) has zero coverage across all four teams (**AL-10 Strategy coverage gap**).

The most common goodness issue is **AP-04 KR Without Baseline** — five KRs across Growth, Platform and Data state a target with no starting point. Two KRs (Platform's developer-satisfaction score, Data's "data quality") cannot be measured at all (**AP-09 Metric Nobody Can Measure**).

Recommended first action: a joint Payments/Growth session on the checkout funnel, and a Platform capacity conversation with Payments and Data, both before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 2 | 2 | 3 | 1 | 1 | 3 | 2 | 3 | 1 | 2 | 3 |
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.14) · Platform C (2.15) · Growth C (2.64) · Payments B (2.77).

- Data: K1=1, K5=1 — "Significantly improve data quality across core tables" names no metric and no instrument.
- Platform: K3=2 — the uptime target sits below the 99.95% trailing baseline quoted in the same corpus.
- Growth: O2=2 — "magical" is an abstraction two readers would gloss differently; two KRs lack baselines.
- Payments: K1=2 — the API v2 KR is a ship date carrying no metric or baseline.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76`)
- Why it's a problem: "data quality" names no defined score, no threshold and no system of record, so the KR can never be honestly scored — searched all four team sections, the company priorities section and the Q2 business-review appendix, and no data-quality dashboard, tool or metric appears anywhere in the corpus.
- Scores affected: K1=0, K5=0, K3=2 (calibration unverifiable), K6=1
- Suggested rewrite: "KR D1.3: Rows failing the `<data-quality test suite>` nightly checks across the `<N>` core tables: `<baseline>`% → `<target>`%, reported weekly from `<data-quality dashboard>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Data
- Evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80`)
- Evidence (cross-source baseline search): "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40`) — the only stated value for this metric anywhere in the corpus, and it sits on Growth's page under a definition Data does not repeat.
- Why it's a problem: Data's own text states no current activation value and no definition, so 35% can be read neither as ambition nor as progress; the only baseline in the corpus belongs to another team, whose target for the same named metric is 40%.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR D2.2: New-user activation rate (first invoice sent within 7 days, the definition stated on Growth's page) `<baseline>`% → `<target>`%, measured weekly from `<analytics dashboard>`; target reconciled with Growth's 40% and a single accountable team named." [proposal — placeholder target] (See §4 AL-03.)

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59`)
- Evidence (objective this KR sits under): "Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56`)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: no survey, instrument or dashboard for a "developer satisfaction score" exists anywhere in the corpus (searched all four team sections, the company priorities section and the Q2 business-review appendix), so the 8/10 can neither be produced nor contested; the KR also states no current score, and internal developer sentiment would not move either half of its objective — uptime or cost.
- Scores affected: K1=2, K5=1, K3=2, K7=2
- Suggested rewrite: "KR PL1.3: Quarterly internal platform survey (n ≥ `<N>` engineers, `<survey tool>`), 'Platform unblocks my work' top-two-box `<baseline>`% → `<target>`%, fielded in month 1 and month 3." [proposal — placeholder target] — and move it under a developer-experience objective, not under "Keep the lights on, cheaper".

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57`)
- Evidence (prior actual, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89`)
- Also: AP-10 BAU Dressed as OKR · AP-04 KR Without Baseline
- Why it's a problem: the quarter's target sits below the trailing-90-day actual quoted in the same corpus, so the KR is achieved by changing nothing; "Maintain" states the team's standing duty rather than a delta, and the KR states no baseline of its own.
- Scores affected: K3=1, K1=2
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → `<target ≥ 99.97>`%, measured monthly on the Datadog SLO monitor, with error-budget burn reviewed weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63`)
- Evidence (company priority it serves): "complete SOC 2 Type II and hold enterprise-grade reliability." (`sample-portfolio.md › Company Q3 2026 priorities › line 11`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: "Complete" names a deliverable with no metric and no baseline→target pair, so the KR can only ever score 0% or 100% and offers no mid-quarter steering signal on the company priority it carries.
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR PL2.2: SOC 2 Type II auditor evidence requests closed `<0>`/`<N>` → `<N>`/`<N>`, fieldwork complete by `<date>`, audit report received by `<date>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39`)
- Why it's a problem: no current trial-to-paid value exists anywhere in the corpus — searched the Growth section, the other three team sections, the company priorities section and the Q2 business-review appendix, which states values for uptime, chargeback rate, step-up coverage and qualified signups but nothing for trial-to-paid — so 22% cannot be judged as ambition or tracked as progress.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<analytics dashboard>`) → 22%, measured on trials started in the quarter." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46`)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid distribution without indicating anything about the funnel the objective claims to build, and no current pageview figure appears anywhere in the corpus, so 50,000 is neither an outcome nor a judgeable target. The KR is labelled "*(aspirational)*", which sets expected attainment but does not turn an exposure count into a result.
- Scores affected: K2=2, K1=2, K3=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed in `<analytics dashboard>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR measures a shipping event rather than a result — it scores 100% whether or not a single merchant or internal consumer moves onto v2, and until Sep 26 it can only read 0%. It is also the deliverable two other teams' plans hang on (§4 AL-06, AL-07), so a binary KR hides the slip risk that matters most to the portfolio.
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing API calls served by v2 by Sep 26 (0% today), v2 error rate ≤ `<threshold>`%, and Growth's self-serve upgrade flow migrated by `<date>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28`)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44`)
- Conflict: step-up verification is a friction control on the checkout surface; taking it from 35% to 90% of transactions inserts an extra authentication step into roughly nine of every ten checkouts in the same quarter that Growth commits to a 10-point conversion lift on that surface. Neither KR references the other team, and no shared guardrail pairs the two numbers.
- Detection check that fired: AL-02 surface-lever blocking key (2) — both KRs sit on the checkout surface, Payments' stated lever (step-up verification coverage) is a friction control there, and Growth targets that surface's conversion metric. Metric-identity key (1) generated nothing: the two KRs share no canonical metric.
- Disconfirming checks run: shared or parent OKR covering both — searched both team sections and the company priorities section, none found; documented split of levers — none found (Payments' note cites only "(company priority C3)", Growth's note concerns the billing API); directionality — confirmed opposed at the mechanism level. Separately generated and killed: the lookalike pair Payments "Raise checkout success rate from 91.2% to 95% for card transactions." (`sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 22`) ↔ the same Growth KR — different definitions and populations (card-transaction success vs self-serve signup funnel conversion), same direction, no control lever on either side. That kill is per-candidate and does not touch this finding.
- Inference labels: the verification-friction → checkout-conversion mechanism is analyst inference; no Brightledger document states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product convenes Priya N. (Payments) and Marcus T. (Growth) to agree a guardrail pair — a chargeback ceiling and a checkout-conversion floor — plus risk-based targeting so step-up applies to `<share>`% of transactions rather than a blanket 90%, before mid-quarter. [proposal — placeholder target]

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41`); the dependency is stated as "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48`)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23`)
- Conflict: Growth's need-by date for the billing API is Aug 15; the producer's only stated delivery date is Sep 26 — a six-week hard inversion with no integration margin, on two KRs that are both committed. Growth's note treats the dependency as settled by a June conversation rather than by a date.
- Detection check that fired: AL-06 edge date comparison on the dependency map — consumer need-by (Aug 15) precedes producer delivery (Sep 26).
- Disconfirming checks run: "late date ≠ inversion" — searched both team sections for an earlier milestone of the billing API (beta, EA, preview, staged rollout); the corpus states only the Sep 26 GA date and Growth names no milestone short of the API itself, so no tighter reading rescues the sequence. Commitment levels checked on both sides: neither KR carries an "(aspirational)" mark, and both pages state "KRs are committed unless marked (aspirational)." (`sample-portfolio.md › Growth team — Q3 2026 › line 36`).
- Inference labels: none — all load-bearing text quoted; the need-by date is Growth's own stated launch date, not inferred.
- Verdict: CONFIRMED (all three quotes re-verified against lines 41, 48 and 23)
- Recommended resolution owner: Marcus T. (Growth) and Priya N. (Payments) to agree in writing within one week either a dated partial-availability milestone for the billing endpoints G1.3 needs before Aug 15, or a re-dated G1.3 launch; whichever is chosen, the date belongs in both KRs.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82`), supporting the committed KR "Migrate 100% of product events to unified event schema v2." (`sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74`)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65`)
- Conflict: Data's committed 100% schema-v2 migration rests on a streaming pipeline migration it expects someone else to run, and no objective, KR or note on the Platform page contains that work — Platform instead states that the quarter is fully committed elsewhere and that non-critical infra requests are deferred to Q4. Data has sized only "our part"; the pipeline itself is unowned.
- Detection check that fired: AL-01 dependency-edge acknowledgment — the phrase "rides on" plus a named external deliverable ("the streaming pipeline migration"), resolved to an owning team and then searched for on the producer's side with no hit.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched the whole Platform section (lines 52–66) for pipeline, stream, schema, event, data, migration and warehouse: zero hits. No Jira or backlog source exists in this corpus (local export only, no Atlassian connection), so the absence claim is bounded to the OKR export and cannot be downgraded by a scheduled-epic finding. Closest near-miss quoted and distinguished: "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 58`) — infra work, but a spend target that commits Platform to no pipeline delivery.
- Inference labels: Data's phrase "at the infra level" is resolved to the Platform team by **analyst inference** — Data's page names no team, and Platform is the only infrastructure-owning team in the confirmed scope. Severity rests on Platform's explicit deprioritization ("Holding all non-critical infra requests until Q4."), which is quoted, and on Data's KR being committed by its page's stated default.
- Verdict: PLAUSIBLE (every quote re-verified character-for-character, but the producer-side resolution of "the infra level" to Platform is inferred rather than quoted)
- Recommended resolution owner: Jonas K. (Data) to take the streaming pipeline migration to Elena R. (Platform) within two weeks for an explicit accept or decline; if declined, D1.1's 100% target must be re-scoped in the same conversation. Cross-reference: §4 AL-07 Resource contention — this is one of two claimants on Platform, and the capacity arithmetic is reported once, there.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ all four teams
- Company evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (`sample-portfolio.md › Company Q3 2026 priorities › line 13`)
- Teams evidence (closest near-miss across the swept portfolio): "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23`) — the only KR in any team's set that touches new payments surface area, and it commits to an API version, not to a financing product, design partners or a pilot.
- Conflict: a dated company priority with a hard Sep 30 deadline and a named deliverable — a pilot live with 3 design partners — has no objective, KR or note anywhere in the four teams' Q3 sets. Nothing in the portfolio is arranged to deliver it, and no team's capacity is reserved for it.
- Detection check that fired: AL-10 top-down strategy trace — for each company priority, searched all four teams' objectives and KRs for coverage; C1 is served by Growth's funnel KRs, C2 by Platform's PL2, C3 explicitly by Payments' P2, and C4 by nothing.
- Disconfirming checks run: "zero hits ≠ coverage gap" — re-searched the whole file under synonyms and program names (capital, financ*, invoice-financing, design partner, lending, factoring): the single hit in the entire corpus is line 13 itself. Checked the company priorities page for a named owner outside the swept team set — it states only "Owner: Dana W. (CEO)" (`sample-portfolio.md › Company Q3 2026 priorities › line 8`) for the page as a whole and assigns C4 to no team or function, so this is a portfolio hole rather than an ownership note.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (company objective and near-miss re-verified against lines 13 and 23)
- Recommended resolution owner: Dana W. (CEO) to name an owning team and an in-quarter objective for C4 within one week, or to move the priority out of Q3; a Sep 30 pilot with no staffed workstream cannot be assumed to land.

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30`)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82`)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65`)
- Conflict: two teams book Platform capacity in the same quarter — one for PCI-scoped infra provisioning in July, one for a streaming pipeline migration — against a page that declares the quarter fully committed to two other workstreams and defers non-critical infra requests to Q4. Combined demand exceeds declared supply, both claims rest on an informal conversation ("as discussed in standup") or on expectation rather than a Platform commitment, and nobody in the portfolio has done this arithmetic.
- Detection check that fired: AL-07 resource-node fan-in — grouping every external-resource mention by owner puts two claimants on Platform in Q3 2026; checking the owner's own page for declared supply returns the fully-committed statement. Classified at the resource node rather than edge by edge: Payments' ask is a pure provisioning/capacity claim and folds into this finding entirely, while Data's names a distinct deliverable and additionally earns its own AL-01 Unacknowledged dependency above; the capacity arithmetic is reported only here.
- Disconfirming checks run: "plural demand ≠ contention" — searched Platform's objectives, KRs and notes for an allocation, a capacity table or a partner-engagement commitment covering either claimant: none found, and the only capacity statement present is the fully-committed one quoted above. No Jira or allocation source exists in this corpus (local export only), so the check is bounded to the export. Confirmed both claims fall in the same period (both pages are headed Q3 2026) and land on the same team rather than on similarly-named groups.
- Inference labels: Data's phrase "at the infra level" is resolved to the Platform team by **analyst inference** (Data's page names no team; Platform is the only infrastructure-owning team in scope). Payments' edge names Platform explicitly and needs no inference.
- Verdict: PLAUSIBLE (all three quotes re-verified character-for-character; the second claimant's edge depends on the labelled inference above)
- Recommended resolution owner: Elena R. (Platform) convenes Priya N. (Payments) and Jonas K. (Data) within one week to state Platform's actual Q3 supply and allocate it explicitly; whatever is not funded gets written back into the consuming team's KRs as a re-scope rather than left as an assumption.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40`), under the objective "Make the first week with Brightledger magical" (`sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 38`)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80`), under the objective "Own onboarding personalization end-to-end" (`sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 78`)
- Conflict: two teams commit to moving the same named metric for the same population in the same quarter to two different numbers — 40% and 35% — with no cross-reference, shared owner or division of labour, while Data's objective claims the onboarding surface "end-to-end" and Growth's owns the first week. A quarter that ends at 35% is simultaneously a Data success and a Growth failure, and nobody can say who was accountable for the gap.
- Detection check that fired: AL-03 clustering on target metric plus population — both KRs name "new-user activation rate" for new signups on the onboarding surface; the pair is also generated by the AL-08 metric-name key (one metric name used by two teams).
- Disconfirming checks run: "similar objectives ≠ duplication" — searched the Growth section (lines 34–49) for any mention of the Data team, Jonas K., personalization or checklists, and the Data section (lines 69–83) for any mention of Growth, Marcus T., trials or the funnel: zero hits in both directions. No shared epic, joint owner or explicit lane split appears anywhere in the corpus, and no parent objective assigns lanes — the company priorities section contains no mention of activation or onboarding at all. Different-population check: both KRs target new signups on the same surface, so the legitimate-division-of-labour reading does not hold.
- Inference labels: none — all load-bearing text quoted. Secondary failure mode cross-referenced rather than double-counted: **AL-08 Terminology collision**, form (a) — Growth defines activation as "first invoice sent within 7 days" and Data's KR states no definition, so the 40% and the 35% may not even be the same measurement; per the taxonomy's one-finding-one-failure-mode rule it is reported here under the root-cause category.
- Verdict: CONFIRMED (both KRs and both objectives re-verified against lines 38, 40, 78 and 80)
- Recommended resolution owner: Head of Product convenes Marcus T. (Growth) and Jonas K. (Data) within two weeks to assign one accountable team for new-user activation, one target and one written definition; the other team's KR becomes a named contributing lever with its own distinct metric.

### [Minor] AL-04 Orphan objective: Data ↔ company strategy
- Data evidence: "One trustworthy source of truth" (`sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73`), whose KRs are "Migrate 100% of product events to unified event schema v2." (`sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74`) and "Cut critical-dashboard data latency from 6h to 1h." (`sample-portfolio.md › Objective D1: One trustworthy source of truth › line 75`)
- Company evidence: the full priority list — "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." / "complete SOC 2 Type II and hold enterprise-grade reliability." / "bring chargeback rate under 0.5% after the Q2 incident." / "invoice-financing pilot live with 3 design partners by Sep 30." (`sample-portfolio.md › Company Q3 2026 priorities › lines 10–13`)
- Conflict: D1 claims no parent, moves no company-level metric and is named nowhere in the strategy source, yet it consumes one of Data's two objectives for the quarter on work whose contribution to C1–C4 is never argued in writing.
- Detection check that fired: AL-04 three-way check on the strategy trace (explicit parent link / metric linkage / strategy-page mention) — all three negative.
- Disconfirming checks run: "no parent link ≠ orphan" — (a) explicit link: the Data section states none, while Payments is the only team in the portfolio that cites a priority, with "(company priority C3)" (`sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30`), showing the convention exists and Data did not use it; (b) metric linkage: none of D1's metrics — event-schema migration percentage, dashboard latency, data quality — is one of the four company metrics or a documented driver of one; (c) strategy-page mention: searched the company priorities section (lines 7–13) for data, schema, dashboard, latency, warehouse and analytics: zero hits. Exploratory-charter check: the Data section contains no charter for enabling or exploratory work that would kill the finding.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (objective, both KRs and all four company priorities re-verified against lines 73–75 and 10–13)
- Recommended resolution owner: Jonas K. (Data) to state D1's parent priority and the driver relationship in one line on the Data page before mid-quarter, or to re-frame D1 around the company metric it serves. Severity is Minor: the page's only capacity claim, "we've sized our part at 3 engineer-months", is scoped to the schema-v2 workstream and states no large fraction of team capacity, so AL-04's escalation condition is not met.

## 5. Prioritized action list

1. Convene Payments and Growth to set a joint checkout guardrail pair (chargeback ceiling plus conversion floor) and risk-based step-up targeting before mid-quarter — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
2. Fix the billing-API sequencing in writing — either a dated partial-availability milestone before Aug 15 or a re-dated G1.3 launch — within one week — owner: Marcus T. (Growth) with Priya N. (Payments) (resolves §4 AL-06 Timeline mismatch).
3. Get an explicit accept or decline from Platform on the streaming pipeline migration, and re-scope D1.1 in the same conversation if it is declined — owner: Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
4. Name an owning team and an in-quarter objective for company priority C4, or move it out of Q3, within one week — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
5. Replace Platform's developer-satisfaction KR with an instrumented survey measure and move it off the "Keep the lights on, cheaper" objective — owner: Elena R. (Platform) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
6. Replace Data's "data quality" KR with a defined, dashboard-backed freshness and completeness measure — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
7. State Platform's real Q3 supply and allocate it explicitly across the Payments and Data asks, writing any unfunded ask back into the consuming team's KRs — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
8. Assign one accountable team, one target and one written definition for new-user activation — owner: Head of Product with Marcus T. (Growth) and Jonas K. (Data) (resolves §4 AL-03 Duplicated / overlapping objectives, cross-referencing AL-08 Terminology collision, and §3 AP-04 KR Without Baseline — Data).
9. Rewrite the uptime KR against the quoted 99.95% trailing baseline so the target is a delta rather than a floor already cleared — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target).
10. Convert the remaining deliverable, unbaselined and vanity KRs into measured outcomes with quoted baselines — owner: each team's OKR owner, Priya N., Marcus T. and Elena R. (resolves §3 AP-01 Task Masquerading as KR for Payments and Platform, AP-04 KR Without Baseline for Growth, and AP-03 Vanity Metric for Growth).

## 6. Suggested single-team re-runs

All four teams qualify — none on the roll-up grade (no team is at or below the rubric's D needs-rework threshold), but each carries at least one Critical finding, which is the second qualifying criterion.

- **Data** (roll-up C (2.14); Critical AP-09 Metric Nobody Can Measure and Critical AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: the 'Data team — Q3 2026' section of `sample-portfolio.md` (Confluence page 88225, DATA-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Local export only — no Atlassian connection available."
- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: the 'Platform team — Q3 2026' section of `sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Local export only — no Atlassian connection available."
- **Growth** (roll-up C (2.64); Critical AL-02 Conflicting metrics / adversarial incentives and Critical AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: the 'Growth team — Q3 2026' section of `sample-portfolio.md` (Confluence page 88217, GRW-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Local export only — no Atlassian connection available."
- **Payments** (roll-up B (2.77); Critical AL-02 Conflicting metrics / adversarial incentives and Critical AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: the 'Payments team — Q3 2026' section of `sample-portfolio.md` (Confluence page 88213, PAY-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Local export only — no Atlassian connection available."
