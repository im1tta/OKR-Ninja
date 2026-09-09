# Brightledger — Q3 2026 OKR portfolio review

Scope: 4 teams (Payments, Growth, Platform, Data), period Q3 2026, portfolio mode. Strategy source: the company priorities section of the same export. Source of record for every quote: `input/sample-portfolio.md` (no Atlassian connection available; Jira/backlog evidence could not be consulted).

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings.
The worst alignment risk is AL-06 Timeline mismatch: Growth commits to launching self-serve plan upgrades by Aug 15 on a billing API that Payments does not reach GA until Sep 26 — both KRs committed, six weeks apart.
Its root sits one edge upstream: Platform declares Q3 fully committed and is holding infra requests until Q4 while two teams' committed KRs assume Platform capacity (AL-07 Resource contention), with Data's pipeline dependency unacknowledged entirely (AL-01 Unacknowledged dependency).
Company priority C4 (Brightledger Capital) has no owner anywhere in the four teams' OKRs (AL-10 Strategy coverage gap).
The most common goodness issue is AP-04 KR Without Baseline (3 KRs across Growth and Platform state a target with no starting point); two further KRs — one on Platform, one on Data — cannot be measured at all (AP-09 Metric Nobody Can Measure).
Recommended first action: Growth and Payments reconcile the Aug 15 / Sep 26 dependency date this week, before Platform's capacity decision makes both dates moot.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 3 |
| Platform | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.1) · Platform C (2.2) · Growth C (2.6) · Payments B (3.1). Per-objective: D1 D (1.9) · D2 C (2.4) · PL1 D (1.9) · PL2 C (2.6) · G1 B (2.9) · G2 C (2.4) · P1 B (2.9) · P2 B (3.3).

- Data: K1/K5=1 — one KR states no metric at all; three more state targets without baselines.
- Platform: K3=2 — the uptime KR targets less than the trailing actual quoted in the same export.
- Growth: O2=2 — "magical" and "machine" are abstractions two readers would gloss differently.
- Payments: K1=2 — the API v2 KR is a ship date carrying no metric or baseline.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" names no metric, no scale and no system that could report it — searching the whole export for the terms `quality`, `score`, `dashboard`, `Datadog`, `Looker` and `analytics` returns only this KR and the unrelated dashboard-latency KR at line 75 — so the KR can never be honestly scored; "Significantly" adds a direction with no magnitude.
- Scores affected: K1=0, K5=0, K3=2
- Suggested rewrite: "KR D1.3: Core-table defect rate (null, duplicate or out-of-range rows across the `<N>` core tables, nightly `<data-quality monitor>` job): `<baseline>`% → `<target>`%, reported weekly." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no survey, tool or instrument that could produce a developer-satisfaction score appears anywhere in the corpus — all four team pages, the priorities page and the Q2 review extracts were searched for the terms `satisfaction`, `survey` and `score`, and only this line returns — so the 8/10 can never be scored honestly; and with no current value stated, the target cannot be read as ambition or as progress.
- Scores affected: K1=1, K5=1, K3=2
- Suggested rewrite: "KR PL1.3: Engineering experience survey (`<named survey tool>`, n ≥ `<N>`, same question wording each quarter): developer satisfaction `<baseline>`/10 → 8/10 by Sep 30." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (prior actual): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing-90-day actual quoted in the same export, so the KR is achieved by changing nothing and would still be met if unavailability doubled from 0.05% to 0.1%.
- Scores affected: K3=1, K1=3, K6=2
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.97% for Q3, measured monthly on the same monitor, error-budget burn reviewed weekly." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Why it's a problem: the KR is done/not-done with no scale and no date, so mid-quarter it can only be scored 0% or 100% and slippage stays invisible until the quarter closes — despite C2 making the audit a company commitment.
- Scores affected: K1=0, K2=1, K6=2
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence requests closed 0/`<N>` → `<N>`/`<N>`, observation window closed by `<date>`, auditor's report received by Sep 30." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no current trial-to-paid value exists anywhere in the corpus — all four team pages and the Q2 review extracts were searched for the terms `trial` and `conversion`, and the only conversion baselines given are checkout conversion at 58% (line 44) and activation at 31% (line 40) — so 22% may be a stretch or already achieved, and progress cannot be tracked.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<funnel dashboard>`) → 22%, measured per signup cohort 30 days after trial start." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume or paid promotion without indicating anything about the funnel the objective is about, so the KR can be hit while qualified signups and conversion stand still; and no current pageview figure appears on the Growth page or in the Q2 review extracts, so the 50,000 cannot be judged as ambition.
- Scores affected: K2=2, K1=2, K3=2, K7=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, first-touch attribution in `<analytics tool>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: reaching GA is a delivery event, not a result — the KR is fully satisfied if no traffic ever moves to v2 and checkout gets no better, and its only failure mode is lateness. It is also the KR two alignment findings hang on (§4 AL-06, §4 AL-07), so its all-or-nothing shape hides the partial progress other teams need to see.
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing API calls served by v2 (0% → `<target>`%) by Sep 26, with v2 error rate ≤ `<threshold>`% and p95 latency no worse than v1." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41); the dependency itself, from the team's notes: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's committed launch date precedes the producer's only stated delivery date by six weeks, leaving negative integration margin; Growth's note treats the dependency as settled by a June conversation rather than by a date.
- Detection check that fired: AL-06 date comparison on the Growth → Payments dependency edge — need-by Aug 15 earlier than producer delivery Sep 26.
- Disconfirming checks run: the late date ≠ inversion control — searched the Payments section (lines 17–30) for an earlier milestone that could satisfy Growth (beta, EA, preview, partial or phased availability): none exists, Sep 26 GA is the only date Payments states. Commitment check: both pages carry "Commitment: KRs are committed unless marked (aspirational)." (lines 19 and 36) and neither KR is marked aspirational, so this is not AL-12 Commitment asymmetry. Hedge check: neither note states a fallback if the API is late.
- Inference labels: none — all load-bearing text quoted; the six-week gap is arithmetic on the two quoted dates.
- Verdict: CONFIRMED
- Recommended resolution owner: Marcus T. (Growth) and Priya N. (Payments) to decide this week either a pre-GA interface Growth can launch on by Aug 15 or a revised G1.3 date, and to write the agreed date onto both OKR pages.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82), supporting the committed KR "Migrate 100% of product events to unified event schema v2." (`input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Data's committed KR rests on a streaming pipeline migration Data explicitly does not own; nothing in Platform's objectives or KRs commits to that migration, and Platform's own note defers non-critical infra work to Q4.
- Detection check that fired: AL-01 dependency extraction — "rides on" and "handled at the infra level" resolve to Platform, the only infrastructure-owning team in scope; searching Platform's whole section (lines 52–65, two objectives and five KRs) and then the entire export for the terms `streaming`, `pipeline`, `schema`, `event`, `ingest` and `warehouse` returns hits only on Data's own page (lines 74 and 82). Per AL-07's disambiguation rule this edge names a distinct deliverable Platform would have to plan as its own project, so it earns this AL-01 in addition to the AL-07 below, which carries the capacity arithmetic.
- Disconfirming checks run: the missing mention ≠ unacknowledged control — the producer's backlog could not be searched (no Atlassian connection in this run; the export is the entire corpus), so the absence is established across the OKR export only and is recorded as such rather than claimed for Jira. Near-miss check: Platform's closest infrastructure KR is "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 58), which commits to cutting infrastructure cost and covers no migration.
- Inference labels: resolving "the infra level" to the Platform team is analyst inference — Data's note names no team; Platform is the only infra owner among the four teams in scope.
- Verdict: CONFIRMED
- Recommended resolution owner: Elena R. (Platform) with Jonas K. (Data) to decide by week 2 whether the streaming pipeline migration enters Platform's Q3 scope; if it does not, D1.1 must be rescoped to what Data can deliver alone or moved to Q4.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company evidence: "Launch Brightledger Capital:" … "invoice-financing pilot live with 3 design partners by Sep 30." (`input/sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest misses, neither of which is coverage): "Make checkout something customers never think about" (`input/sample-portfolio.md` › Payments team — Q3 2026 › line 21) and "Turn our funnel into a machine" (`input/sample-portfolio.md` › Growth team — Q3 2026 › line 43) — the two revenue-facing objectives in scope; neither they nor any of their KRs mention financing, lending or design partners.
- Conflict: a dated, committed company priority has zero contributing objectives or KRs across all four teams — there is nobody to ask about the Sep 30 pilot.
- Detection check that fired: AL-10 top-down strategy trace — all four team sections (Payments 17–30, Growth 34–48, Platform 52–65, Data 69–82), covering 8 objectives and 13 KRs, searched for the terms `capital`, `financ`, `invoice-financing`, `lend`, `design partner` and `pilot`; the only hit in the entire file is the priority itself at line 13.
- Disconfirming checks run: the zero hits ≠ coverage gap control — re-searched under synonyms and program names (capital, financing, lending, pilot, design partner) with the same single hit; checked the priorities page for a named owner outside the swept team set — it states only "Owner: Dana W. (CEO)" (line 8) for the page as a whole, with no per-priority owner, so nothing shows C4 assigned to a function outside this portfolio.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Dana W. (CEO) to assign C4 to a named team before mid-quarter or drop it from Q3 explicitly; the receiving team needs an objective with dated KRs against the Sep 30 pilot.

### [Major] AL-07 Resource contention: Platform ↔ Payments, Data
- Payments (claimant) evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data (claimant) evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform (resource owner) evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs assume Platform capacity in the same quarter Platform declares fully committed elsewhere and closed to non-critical infra requests; nobody has done the combined-demand arithmetic, and Payments' assumption rests on a standup conversation that never reached Platform's page.
- Detection check that fired: AL-07 resource-node fan-in — grouping all dependency mentions by resource put two Q3 claimants on Platform; checking the owner's page for declared supply produced the fully-committed statement. Payments' edge is a pure provisioning/capacity ask, so per the taxonomy's AL-01/AL-07 disambiguation it folds into this finding entirely rather than being filed as its own AL-01; Data's edge additionally names a distinct deliverable and is filed above as AL-01, cross-referencing this finding. The capacity arithmetic is reported only here.
- Disconfirming checks run: the plural demand ≠ contention control — no Jira allocation or capacity table is available in this run, so scheduled-capacity evidence could not falsify the finding; both claims fall in Q3 2026 and name the same team, not similarly-named pods; Platform's five KRs (lines 57–59 and 62–63) were searched for PCI, provisioning or pipeline work and contain none, so there is no partial allocation to downgrade the finding.
- Inference labels: resolving "the infra level" (Data) to Platform is analyst inference; Payments names Platform explicitly.
- Verdict: CONFIRMED
- Recommended resolution owner: Elena R. (Platform) to publish Q3 capacity against both inbound asks in week 1 and take the trade-off to Dana W. (CEO) if it cannot be absorbed; Payments and Data to re-date or re-scope whichever ask is not funded.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 80), under the objective "Own onboarding personalization end-to-end" (`input/sample-portfolio.md` › Data team — Q3 2026 › line 78)
- Conflict: both teams commit to raising the same named metric for the same population in the same quarter at two different targets — 40% and 35% — with no division of labour and no mention of each other, while Data additionally claims end-to-end ownership of the onboarding surface Growth's G1 is built on. Nobody can say who is accountable, and the two numbers cannot both be the goal.
- Detection check that fired: AL-03 clustering by target metric plus population — "new-user activation rate" for new users put the two KRs in one cluster, and the cluster contains no mutual reference, shared owner or stated lane split.
- Disconfirming checks run: the similar objectives ≠ duplication control — searched both pages for a cross-reference, shared epic or explicit split (terms: activation, onboarding, personaliz, each team's name and owner name); Growth's notes reference only Payments (line 48), Data's notes only the pipeline (line 82), and no population, surface or segment split appears anywhere. AL-09 Baseline disagreement checked and rejected: Growth states a 31% baseline and Data states none, which is a missing baseline rather than two conflicting ones. Secondary AL-08 Terminology collision cross-referenced rather than filed separately: Growth defines the metric inside its KR ("first invoice sent within 7 days") and Data states no definition, so the two targets may not even measure the same population.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to name one accountable team and one activation target this week, with the other team's KR restated as a supporting leading indicator carrying the same definition.

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the same checkout surface whose conversion Growth must lift by ten points; taking challenge coverage from 35% to 90% of transactions works against that target, and neither page acknowledges the other team.
- Detection check that fired: AL-02 surface-lever blocking key — both KRs sit on the checkout surface, the Payments KR states a verification/friction control there, and the Growth KR targets that surface's conversion metric. The metric-identity key generated nothing for this pair, since the two metric names differ.
- Disconfirming checks run: shared or parent OKR covering both — none; the priorities page separates the goals into "Cut fraud losses:" (C3, line 12) and "Grow self-serve revenue:" (C1, line 10) with no shared guardrail. Documented split of levers — none in either team's notes. Directionality — confirmed coupled: one KR raises a control on the surface whose throughput the other must raise. Per-candidate kill recorded on the same surface: Payments' "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) paired with the same Growth KR is a lookalike pair — different definitions and populations, same direction, no control lever on either side — and is not reported.
- Inference labels: the verification-friction → conversion mechanism is analyst inference; no Brightledger document states the trade-off.
- Verdict: CONFIRMED
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree a guardrail pair — a chargeback ceiling plus a checkout-conversion floor of `<conversion floor>`% — before step-up coverage passes `<coverage threshold>`%, escalating to Dana W. (CEO) if they cannot agree [proposal — placeholder target].

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (`input/sample-portfolio.md` › Data team — Q3 2026 › line 73), with KRs "Migrate 100% of product events to unified event schema v2." (line 74) and "Cut critical-dashboard data latency from 6h to 1h." (line 75)
- Company evidence: "Grow self-serve revenue:" (line 10), "Become enterprise-ready:" (line 11), "Cut fraud losses:" (line 12) and "Launch Brightledger Capital:" (line 13) (`input/sample-portfolio.md` › Company Q3 2026 priorities)
- Conflict: half of Data's quarter serves an objective with no parent in company strategy — no priority names data, analytics or event infrastructure, and none of D1's metrics is a company metric or a stated driver of one. Severity stays Minor because no capacity fraction is stated, though the team does size part of the work at three engineer-months.
- Detection check that fired: AL-04 three-way check — (a) explicit parent link: none on the Data page, and Payments is the only team that cites a priority at all, "(company priority C3)" (line 30); (b) metric linkage: event-schema coverage, dashboard latency and data quality appear in none of C1–C4; (c) strategy-page mention: the priorities page never mentions data or analytics work. Zero of three.
- Disconfirming checks run: the no parent link ≠ orphan control — the full three-way check above was run before flagging, and inferred parents were counted against the finding, not for it; the Data page was searched for its own justification and the only rationale it offers is a sizing statement, "we've sized our part at 3 engineer-months" (line 82), not a strategic parent.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data) to state D1's parent priority (or its explicit internal-enabler case) on the OKR page before mid-quarter and have Dana W. (CEO) confirm it at the next review.

## 5. Prioritized action list

1. Agree a single date for the billing-API dependency — a pre-GA interface by Aug 15 or a revised G1.3 launch — owner: Marcus T. with Priya N. (resolves §4 AL-06 Timeline mismatch).
2. Decide whether the streaming pipeline migration is in Platform's Q3 scope, and rescope D1.1 if it is not — owner: Elena R. with Jonas K. (resolves §4 AL-01 Unacknowledged dependency).
3. Assign company priority C4 (Brightledger Capital) to a named team with dated KRs, or drop it from Q3 explicitly — owner: Dana W. (resolves §4 AL-10 Strategy coverage gap).
4. Publish Platform's Q3 capacity against both inbound asks and arbitrate the shortfall — owner: Elena R. (resolves §4 AL-07 Resource contention).
5. Name one accountable team and one target for new-user activation, with a shared definition — owner: Marcus T. with Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
6. Set a fraud/conversion guardrail pair before step-up coverage rises — owner: Priya N. with Marcus T. (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
7. Replace the developer-satisfaction KR with a named survey instrument and a stated baseline — owner: Elena R. (resolves §3 AP-09 Metric Nobody Can Measure, Platform).
8. Define a countable data-quality metric with a system of record, or drop D1.3 — owner: Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure, Data).
9. Reset the uptime KR above the quoted 99.95% trailing actual and give the SOC 2 KR a countable gradient — owner: Elena R. (resolves §3 AP-06 Sandbagged Target and §3 AP-02 Binary KR with No Gradient).
10. Add baselines and outcome measures to the remaining defective KRs — P1.2, G1.1, G2.3 — owner: Priya N. and Marcus T. (resolves §3 AP-01 Task Masquerading as KR, §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Data** (roll-up C (2.1); Critical findings §3 AP-09 Metric Nobody Can Measure and §4 AL-01 Unacknowledged dependency — criterion (b)): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `input/sample-portfolio.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Platform** (roll-up C (2.2); Critical finding §3 AP-09 Metric Nobody Can Measure, plus inbound §4 AL-01 and §4 AL-07 — criterion (b)): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `input/sample-portfolio.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Growth** (roll-up C (2.6); Critical finding §4 AL-06 Timeline mismatch — criterion (b)): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `input/sample-portfolio.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Payments** (roll-up B (3.1), above the needs-rework threshold, but a party to the Critical §4 AL-06 Timeline mismatch — criterion (b)): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `input/sample-portfolio.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."

No team qualifies under criterion (a): every roll-up grade is C or better, above the rubric's D needs-rework threshold. All four qualify under criterion (b).
