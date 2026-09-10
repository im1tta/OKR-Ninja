# Coppervale — Q1 2027 OKR portfolio review

**Scope (confirmed at intake):** 5 teams — Dispatch, Courier (driver app), Core Systems, Insights, Accounts (billing & customer success). Period: Q1 2027. Mode: **portfolio** (2+ teams). Sources: `sample-portfolio-2.md` (Confluence export of the company priorities page, five team OKR pages, and a Q4 2026 business-review extract). Strategy source in scope: "Company Q1 2027 priorities" (Confluence page 91050). No Atlassian connection was available; the local export is the only corpus.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 10 Major, 2 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — a three-team cycle with no valid execution order, and every edge is a hard "once/after" gate that the teams' own notes restate.
The most common quality issue is AP-12 Orphan KR (2 of 5 teams park a KR under an objective its success would not move).
A second cross-team fault line runs through delivery reporting: Dispatch and Accounts both carry an "On-time delivery rate" KR with different numerators, denominators, cadences and systems of record (AL-08 Terminology collision), and both feed the same company priority C2.
Dispatch is the only team below B — its KR DS2.4 states a percentage whose population is never defined (AP-13 Ambiguous Denominator, Critical).
Recommended first action: Core Systems convenes Courier and Insights this week to cut one edge of the telemetry cycle before any of the three teams' Q1 commitments can be planned.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 4 | 2 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.54) · Core Systems B (3.07) · Courier B (3.25) · Insights B (3.39) · Accounts B (3.48).
- Dispatch: K3=2 — DS2.4's undefined failure-rate population makes its 6%→3% ambition unjudgeable.
- Core Systems: O1=2 — CS1's objective commits to continuing the standing job, naming no change.
- Courier: K3=2 — referral installs 3,000→45,000 is a 15x jump with no stated mechanism.
- Insights: K7=2 — an App Store rating KR sits under an exec-dashboards objective it cannot move.
- Accounts: K3=2 — AC2.2's stated CSAT baseline contradicts the only Q4 2026 actual in the corpus.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Evidence (contrast, same objective): "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Why it's a problem: "the failure rate" never says failure of what population — dispatched jobs, completed jobs, route-plan builds, or deliveries all read plausibly and would give different numbers, so any of them can be claimed as 3%; the sibling KR quoted above shows the team can state a denominator when it chooses to, and "ops weekly report" names no query of record that would settle it.
- Scores affected: K1=1, K3=2, K5=2
- Suggested rewrite: "KR DS2.4: Job failure rate — jobs ending in a failed state as a share of all jobs dispatched in the week, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target; the 6% and 3% figures are quoted from the source, the population and system of record are proposed]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing enterprise dispatchers versus prospective DE/FR customers — and the KRs split cleanly along that seam, one per clause, so each half of the objective rests on a single measure; "Delight" is additionally an abstraction two readers would gloss differently.
- Scores affected: O1=3, O2=2, K6=2, K7=3
- Suggested rewrite: split into two ranked objectives — "O DS1 (ranked first): Enterprise dispatchers would be upset if Coppervale disappeared tomorrow" (keeping "Enterprise dispatcher NPS 24 → 40" plus a usage-depth KR) and "O DS1b: Coppervale runs live routes for paying customers in DE and FR" (keeping "Signed pilot customers in DE and FR: 0 → 6"). [proposal]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter" (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target with no named lever, intermediate milestone, or resourcing signal anywhere on the page — the notes line quoted above asserts importance, not a mechanism — and it is the objective's only KR, so nothing steers it mid-quarter; unlabeled, it also corrupts the team's expected-attainment arithmetic.
- Scores affected: K3=1, K6=0, K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral bonus (App Store + Play attributed installs); KR CR2.2 (committed, leading): drivers sending at least one referral invite `<baseline>` → `<target>` per month." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36)
- Evidence (the convention the other four pages carry): "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Evidence (targets that vary wildly in stretch, same page): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) and "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: Courier's page states no commitment convention while its targets range from a 0.4-point reliability improvement to a 15x referral jump, so no reader can tell must-hit from bet — the search covered the whole Courier section (lines 35–49) for "committed", "stretch" and "aspirational" and returned nothing, while the Dispatch, Core Systems, Insights and Accounts pages each state the convention (lines 19, 55, 76, 93).
- Scores affected: K3=2 (Courier team dimension — attainment expectations unjudgeable across the set)
- Suggested rewrite: add to the Courier page header "Commitment: KRs are committed unless marked (stretch)." and mark KR CR2.1 "(stretch)". [proposal]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence: "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 58)
- Why it's a problem: the objective commits the team to continuing its standing duty and names no change — no direction, reduction, or improvement — and per AP-10 the real deltas in its KRs do not rescue it, because the objective is the thing the anti-pattern is about; "smoothly" is also an abstraction two readers would gloss differently, and the cost KR under it serves a different end than "running smoothly".
- Scores affected: O1=2, O2=2, O3=2, K7=2
- Suggested rewrite: "O CS1: Product teams stop losing days to platform incidents — KR: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." and move "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." under its own objective, "O: Every completed delivery costs less to serve than it did last quarter". [proposal]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its stated objective): "Objective IN1: Execs run Monday mornings from our dashboards" (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: there is no causal chain in two steps from a public app-store rating to leadership running Monday mornings from Insights' dashboards, and the KR shares no nouns or audience with the objective — it measures the driver app, which is Courier's domain ("Drivers finish every shift without fighting the app"), so Insights can hit it while the objective goes nowhere.
- Scores affected: K7=2 (IN1 set)
- Suggested rewrite: replace with a KR that moves the stated objective — "KR IN1.3: Leadership questions answered from the exec suite without an analyst request `<baseline>` → `<target>` per month (Looker usage stats)." [proposal — placeholder target] — and, if the rating is worth carrying, move it to Courier's Objective CR1 where the driver app's quality is the outcome.

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own convention): "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page promises an owner per KR and every other Insights KR names one (Halima D., Vik M.), but this one names nobody — and it is the KR that most depends on people outside Insights, since nine product squads have to act; with no accountable individual, the 9/9 target has no one to chase it.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights), with a named counterpart per squad." [proposal]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four objectives and eight KRs carry a uniform top-priority label and the team's own note says the trade-off was declined, so the set encodes no decision — when the quarter tightens, nothing in the OKRs tells Accounts what to drop, and the portal KR the team already flags as conditional sits at the same nominal priority as onboarding time-to-value.
- Scores affected: set-level — no O or K dimension scores prioritization, so this defect is reported here rather than in the §2 heatmap.
- Suggested rewrite: "P0: AC1 (onboarding time-to-value, the named C2 driver). P1: AC2 (escalation backlog). P2: AC4 (billing migration, the named C1 driver). Backlog / explicitly conditional: AC3.2 partner portal." [proposal]

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Evidence (its stated objective): "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence (where the team itself ties the portal): "Portal timing depends on how fast the billing migration goes (see AC3.2)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: a portal rollout count has no stated causal chain in two steps to customers trusting the delivery promises Coppervale reports, and shares no nouns with that objective; the team's own note ties the portal to the billing migration, and Dispatch treats it as a growth lever — so the KR sits under an objective it cannot move while AC3's real subject rests on one metric.
- Scores affected: K6=2, K7=2 (AC3 set)
- Suggested rewrite: move the portal under AC4 and measure use rather than rollout — "KR AC4.3: Partner accounts completing at least one billing action in the portal 0 → `<target>` (Partner CRM)" — and give AC3 a second measure of the stated outcome — "KR AC3.2: Customer-raised delivery-promise disputes `<baseline>` → `<target>` per month (Zendesk)." [proposal — placeholder target]

## 4. Alignment findings

Blocking keys used for the pairwise checks: metric-identity and surface-lever (conflicting metrics), metric plus target-population cluster (duplication), metric name and normalized definition diff (terminology), canonical-metric baselines (baseline disagreement). Graph-structural checks ran over the dependency map built from every "once/after/assumes/depends on/owns" mention (edge acknowledgment, dates, cycle detection, commitment labels, resource fan-in), and the strategy trace ran top-down and bottom-up over "Company Q1 2027 priorities". Candidates generated and then killed by the disconfirming checks: the three telemetry objectives (Courier CR3, Core Systems CS3, Insights IN2) as duplication — killed because each page explicitly references the others' work, which is a stated division of labor; Courier's instrumentation push against Core Systems' unit-cost target as a mechanism-level conflict — killed because both objectives cite C4, whose text names pipeline consolidation as the cost lever; and a strategy hole — killed because each of C1–C4 has at least one contributing objective, with C2's three named drivers all claimed (onboarding time-to-value, escalation backlog, delivery promises) and no team objective left without a stated parent.

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema-v3 validation, and Insights waits on Courier's instrumentation — a closed three-team cycle in which no team can start, so as written none of the three KRs can be completed and C4's telemetry consolidation stalls with them.
- Detection check that fired: AL-11 structural cycle detection on the dependency graph — edges Courier→Core Systems ("once Core Systems GAs the SDK"), Core Systems→Insights ("after Insights validates event schema v3 in production"), Insights→Courier ("after Courier instruments the new driver-app event stream") close a cycle.
- Disconfirming checks run: hard blocking vs. soft preference — all three edges use hard sequencing ("once", "after", "after") and each team's own notes restate the gate rather than softening it: "SDK timing per Core Systems' plan." (line 49), "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70), "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (line 87) — no soft edge found. Staged-milestone interleaving — checked all three pages for an earlier milestone (beta, pre-GA build, partial flow set) that would let one edge start before its predecessor finishes; none is named, so no valid interleaving is quotable. Awareness plus resolution plan — each team's notes state its own gate and none proposes a sequencing fix, so no downgrade applies.
- Inference labels: none — all load-bearing text quoted, including all three edges and all three restating notes.
- Verdict: CONFIRMED (every quote re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) in week 1 to cut one edge — the quotable candidate is Courier instrumenting a subset of the 14 flows against the code-complete pre-GA SDK so Insights can validate schema v3, with GA following validation; whichever edge is cut, all three KRs need restating before the quarter is planned. Note: Core Systems and Insights label their KRs committed by page convention (lines 55, 76) and Courier's page states no convention at all (§3 AP-08 Committed vs Aspirational Not Labeled), so no edge here is marked soft.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two measurements — different numerator event (completed within the window vs. scanned at the destination), different denominator (all completed jobs vs. all scheduled deliveries including cancellations), different cadence (weekly vs. monthly) and different system of record (Ops Console vs. Billing warehouse) — which is why the two baselines sit 13 points apart; both objectives report into the same company priority, "keeping the delivery promises we report to customers" (sample-portfolio-2.md › Company Q1 2027 priorities › line 11), so an exec rollup of "on-time delivery" has two defensible numbers.
- Detection check that fired: AL-08 form (a) — metric-name blocking across teams, then diffing each team's stated definition (formula, window, population, data source).
- Disconfirming checks run: normalize before diffing — normalized, the two definitions still differ on numerator event, denominator population, cadence and source, so this is not verbally-different-but-equal wording. Superseded glossary — searched the company priorities page, both team pages and the Q4 review extract for a shared definition; none exists, and the nearest text ("keeping the delivery promises we report to customers", line 11) names no formula. Baseline-disagreement pre-check — the 91% vs. 78% gap is explained by the definition split, so per the taxonomy this is reported as AL-08 rather than as a baseline disagreement.
- Inference labels: none — all load-bearing text quoted; both definitions are stated in the KRs themselves.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Accounts lead (Georg B.) and Dispatch lead (Mei L.) to publish one company definition of on-time delivery — naming the reported numerator, denominator, cadence and system of record — and to restate whichever KR does not match it, before the first C2 report of the quarter; if two measures are genuinely needed, rename one (e.g. "dispatch window adherence") so no rollup can merge them.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), with "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31) and the page convention "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" marked "(stretch — only if the billing migration lands early)" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), with "Portal timing depends on how fast the billing migration goes (see AC3.2)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: Dispatch's KR is committed by its page's own convention and rests entirely on a deliverable Accounts marks stretch and conditional on another project landing early; worse, the arithmetic assumes more than Accounts' full stretch — 600 trial starts sourced from a portal Accounts commits only to "the first 40 partner accounts" — so Dispatch's number fails even in the world where Accounts hits its stretch exactly.
- Detection check that fired: AL-12 commitment-label comparison on an acknowledged dependency edge (Accounts does carry the portal KR, so this is not an unacknowledged dependency), plus the target-arithmetic coupling check — 0 → 600 on the consumer side against 0 → 40 on the producer side.
- Disconfirming checks run: missing label ≠ mismatch — both pages state their labeling scheme (Dispatch line 19; Accounts line 93 plus the explicit "(stretch — only if the billing migration lands early)" marker), so the asymmetry is real rather than a vocabulary difference. Consumer hedging — searched Dispatch's KR text and team notes for a discount, contingency or partial-credit clause; the only text found assumes the launch ("DS2.2 assumes the partner portal launch"), it does not discount it, so no downgrade applies.
- Inference labels: none — all load-bearing text quoted, including both commitment labels and both targets.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.), by week 3: either promote the portal to a committed KR at a scope that can carry 600 trial starts, or Dispatch re-cuts DS2.2 to a portal-independent trial-start path and files the portal-sourced portion as a stretch add-on.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, the same named instrument and the same stated period carry two different current values, eight points apart; if the business review is right, Accounts' committed P0 KR is a twelve-point ask presented as a four-point one, and its expected attainment, its ambition and any exec rollup of CSAT are all calibrated against the wrong starting point.
- Detection check that fired: AL-09 metric-catalog baseline collection — the canonical metric "Customer CSAT" carries two stated Q4 2026 baselines that differ beyond rounding.
- Disconfirming checks run: different as-of dates — both texts name Q4 2026 explicitly, so the dates do not explain the gap. Different populations (terminology pre-check) — both name the "quarterly relationship survey"; the review adds only a sample size ("n = 412") and no alternative population, and no other CSAT definition exists anywhere in the corpus (searched the company priorities page, all five team pages and the appendix). Neither check weakens the finding.
- Inference labels: none — all load-bearing text quoted; no baseline was computed or recalled.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Accounts lead (Georg B.) to reconcile with the Q4 review owner within one week and restate AC2.2 against the agreed number — if 78 stands, the KR reads "Customer CSAT 78 (Q4 2026 actual, quarterly relationship survey, n = 412) → `<target>`" [proposal — placeholder target].

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "Ship with confidence *(supports C2 — enterprise churn)*" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), with its three KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64) (sample-portfolio-2.md › Objective CS2: Ship with confidence)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the claimed parent names its three drivers, and none of CS2's KRs measures churn or any of those drivers — all three are internal delivery-pipeline metrics, so the objective could be fully achieved in a quarter where enterprise logo churn worsens, which makes the stated link decorative rather than causal.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's page names as needed? All three answers are no.
- Disconfirming checks run: mechanism documented elsewhere — searched the company priorities page (C2's own driver list), the Core Systems notes ("SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.", line 70) and the other four team pages for any statement linking deploy cadence, change-failure rate or CI time to enterprise churn; none found. Named-contributor check — C2's three drivers are claimed elsewhere in the portfolio (Accounts AC1, AC2, AC3 and Dispatch's on-time delivery KR), and C2 does not name Core Systems as a contributor, so the parent is not relying on this child by name.
- Inference labels: the claim that the three pipeline metrics have no causal path to enterprise logo churn is analyst inference — no Coppervale document states either such a link or its absence; every quoted text is verbatim.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Core Systems lead (Adaeze O.) with the priorities-page owner (Noor E., CEO): either re-anchor CS2 to C4, where its cost and pipeline work already lives, or add one KR that measures a named C2 driver — e.g. "KR: Enterprise escalations caused by a production change `<baseline>` → `<target>` per quarter (incident review tags)" [proposal — placeholder target]. Severity note: AL-05 defaults to Minor here because C2 does not name Core Systems as a contributor; it is escalated one level because all three CS2 KRs are explicitly committed under the page's stated convention (line 55).

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to cut one edge of the telemetry cycle and restate all three KRs — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with a named population and system of record before the quarter's first ops review — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Publish one company definition of on-time delivery and restate the KR that does not match it — owners: Accounts lead (Georg B.) and Dispatch lead (Mei L.) (resolves §4 AL-08 Terminology collision).
4. Reconcile the partner-portal commitment level and scope against Dispatch's 600-trial-start number — owners: Accounts lead (Georg B.) and Dispatch lead (Mei L.) (resolves §4 AL-12 Commitment asymmetry).
5. Settle the Q4 2026 CSAT baseline with the business-review owner and restate AC2.2 — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring a named C2 driver — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-05 Cascade drift).
7. Rank Accounts' four objectives P0/P1/P2 and name what drops if the quarter tightens — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Split the referral moonshot into a labeled aspirational target plus a committed leading KR — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot).
9. Move the two orphan KRs to objectives they can move and name an owner for IN2.2 — owners: Insights lead (Halima D.) and Accounts lead (Georg B.) (resolves §3 AP-12 Orphan KR ×2, AP-15 Ownerless KR).
10. Restate CS1 as a named change, add Courier's commitment convention, and split Dispatch's DS1 objective — owners: Core Systems, Courier and Dispatch leads (resolves §3 AP-10 BAU Dressed as OKR, AP-08 Committed vs Aspirational Not Labeled, AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.54); Critical §3 AP-13 Ambiguous Denominator, plus inbound §4 AL-08 Terminology collision and §4 AL-12 Commitment asymmetry): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.25); qualifies on the Critical §4 AL-11 Circular dependency, plus §3 AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.07); qualifies on the Critical §4 AL-11 Circular dependency, plus §3 AP-10 BAU Dressed as OKR and §4 AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.39); qualifies on the Critical §4 AL-11 Circular dependency, plus §3 AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.48), above the needs-rework threshold, and no Critical finding — its four Major findings are actionable from §5 without a deeper pass.
