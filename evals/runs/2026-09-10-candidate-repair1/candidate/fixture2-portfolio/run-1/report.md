# Coppervale — Q1 2027 portfolio OKR review

Mode: **portfolio** (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027, per the source file's title. Strategy source: the "Company Q1 2027 priorities" section (C1–C4). Sole corpus: `input/sample-portfolio-2.md`.

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 11 Major, 3 Minor findings.
The worst alignment risk is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' schema validation, and Insights' validation waits on Courier's instrumentation — three committed telemetry KRs with no valid execution order as written.
The most common goodness anti-pattern is **AP-12 Orphan KR** (2 instances, in Insights and Accounts); no other anti-pattern appears more than once.
The one Critical quality defect is Dispatch's DS2.4, which names no population for "the failure rate" and so cannot be honestly scored (**AP-13 Ambiguous Denominator**).
Dispatch's committed 600 enterprise trial starts ride on a partner portal that Accounts lists as stretch, conditional on its billing migration (**AL-12 Commitment asymmetry**).
Dispatch and Accounts both report a metric called "on-time delivery rate" under incompatible definitions, baselines and systems, and both feed company priority C2 (**AL-08 Terminology collision**).
Company priority C1's ARR target is dated inside this quarter and measured by no team (**AL-10 Strategy coverage gap**).
Recommended first action: Core Systems convenes Courier and Insights in week 1 to break the telemetry cycle before any of the three teams plans against it.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 2 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.5) · Core Systems B (3.1) · Courier B (3.2) · Insights B (3.4) · Accounts B (3.4).

- Dispatch: K7=2 — DS2's four KRs leave "whole day" usage unmeasured while trial starts chase acquisition.
- Core Systems: O1=2, O3=2 — "Continue running the platform smoothly" states standing duty, names no change.
- Courier: K3=2 — the referral-install target is a 15x jump with no stated mechanism.
- Insights: K7=2 — an App Store rating KR sits under an exec-dashboard objective it cannot move.
- Accounts: K6=2 — AC3 pairs an outcome metric with an unrelated portal rollout, no steering signal.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Evidence (contrast, same objective): "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Why it's a problem: "the failure rate" never says failures of what — dispatched jobs, route plans, deliveries, or API calls — so several different numbers could all be reported as 3%; the sibling KR on the same page defines its population explicitly, which shows the omission is not a house style.
- Scores affected: K1=1, K5=2
- Suggested rewrite: "KR DS2.4: Job failure rate — dispatched jobs ending in a failure state as a share of all dispatched jobs, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (`input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (`input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing enterprise dispatchers versus two new markets — and the KRs split one-to-one into those unrelated groups, so a trade-off between satisfaction work and expansion work cannot be made against this objective; separately, "Delight" is the kind of abstraction two readers gloss differently, which is what holds O2 at 2.
- Scores affected: O1=3, O2=2, K7=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers would fight to keep Coppervale — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS"). Objective DS3: Coppervale sells in DE and FR without a local team — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." [proposal]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the only "how" on the page): "referral growth is our big swing this quarter" (`input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — "our big swing" asserts importance, not a mechanism — so the number decorates the page instead of steering the quarter; it is also the objective's only KR, which leaves nothing leading to steer by mid-cycle.
- Scores affected: K3=1
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral bonus (App Store + Play attributed installs); leading KR CR2.2: drivers sending at least one referral invite `<baseline>` → `<target>` per week (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (Courier's page carries no commitment convention): "*Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06*" (`input/sample-portfolio-2.md` › Courier team (driver app) — Q1 2027 › line 36)
- Evidence (the convention every other team's page states): "*Commitment: KRs are committed unless marked (stretch).*" (`input/sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Evidence (targets that vary wildly in stretch, same page): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (`input/sample-portfolio-2.md` › Objective CR1: Drivers finish every shift without fighting the app › line 39) and "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 0.4-point reliability increment and a 15x growth bet sit on one page with no marker separating must-hit from stretch, so expected attainment cannot be read and the moonshot above cannot be judged as an honest bet; the four other teams in this export all state the convention, so readers will apply their default and treat the 45,000 as committed.
- Scores affected: K3=1 on CR2.1; Courier team K3=2 (search performed: every line of the Courier section, lines 35–49, for "committed", "aspirational", "stretch" and "P0" — no hit; the only commitment statements in the file are on lines 19, 55, 76 and 93, all other teams' pages)
- Suggested rewrite: add to the Courier page header "*Commitment: KRs are committed unless marked (stretch).*" and mark CR2.1 "(stretch)". [proposal]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (`input/sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence: "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (`input/sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 58)
- Evidence: "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (`input/sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 59)
- Why it's a problem: the objective commits the team to continuing its standing job and names no change at all, and per the rubric the two real KR deltas beneath it do not rescue a standing-duty objective — the objective is the thing being scored. The cost of that framing is concrete here: C4's own headline metric, cloud cost per completed delivery, is the team's biggest committed lever and it reads as maintenance.
- Scores affected: O1=2, O2=2, O3=2, K6=2, K7=2
- Suggested rewrite: "Objective CS1: Teams stop losing days to platform incidents, and every delivery costs less to run — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." [proposal]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`input/sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its stated objective): "Execs run Monday mornings from our dashboards" (`input/sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: a store rating shares no noun or domain with leadership dashboard usage and there is no causal chain in two steps from one to the other, so hitting it would not move the objective; the rating is also a driver-app measure, and the driver app belongs to the Courier team page (Confluence page 91116), which commits to crash-free sessions and retention but never to the rating.
- Scores affected: K7=2 on IN1
- Suggested rewrite: replace with a KR that measures the objective — "KR IN1.3: Weekly ops reviews that cite an exec-suite dashboard `<baseline>` → `<target>` per quarter (ops-review notes + Looker usage stats)" — and move the App Store rating to Courier's CR1 if anyone is to own it. [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own convention): "Owners listed per KR." (`input/sample-portfolio-2.md` › Insights team — Q1 2027 › line 76)
- Why it's a problem: no accountable individual is attached, and because this page names an individual on every other KR, the blank cannot be read as falling back to the page owner — it is a declared gap. The KR also asks nine squads outside Insights to act, which is exactly the situation that needs a named chaser.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)." [proposal]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (`input/sample-portfolio-2.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (`input/sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (`input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (`input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (`input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four uniform P0 labels across the whole set encode no trade-off, and the team says so in its own notes; the page also carries a live conditional — the portal ships only "if the billing migration lands early" — so the quarter will force a choice that the priority labels refuse to pre-answer.
- Scores affected: set-level instance (rubric Part 5, rule 9) — it drives no single objective's dimension score, but it is why AC3's K7=2 gap has no stated resolution when the migration slips.
- Suggested rewrite: "P0: AC1 (onboarding time-to-value) and AC2 (escalation backlog) — the two drivers C2 names. P1: AC4 (billing runs itself). P2: AC3 (delivery-promise reporting)." [proposal]

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Evidence (its stated objective): "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (`input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence (where the work actually belongs, per the team's own note): "Portal timing depends on how fast the billing migration goes (see AC3.2)." (`input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: a partner-portal rollout count shares no noun with delivery-promise reporting and has no two-step causal chain to customer trust in reported promises, so hitting it leaves the objective untouched; the page's own note ties the portal to the billing migration under AC4, which is where it belongs.
- Scores affected: K6=2, K7=2 on AC3
- Suggested rewrite: move it to AC4 as "KR AC4.3: Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*", and measure AC3 with "KR AC3.2: Delivery-promise disputes raised by customers `<baseline>` → `<target>` per month (Zendesk view `<view>`)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`input/sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 84)
- Supporting evidence (each team restates its own gate in its notes): "SDK timing per Core Systems' plan." (`input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 49); "GA is gated on schema v3 validation (Insights)." (`input/sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 70); "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (`input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 87)
- Conflict: Courier waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' production validation of schema v3, and Insights' validation waits on Courier's instrumentation. Each of the three teams is first in line behind another, so no execution order exists as written and all three telemetry KRs — plus C4's pipeline-consolidation lever — start the quarter blocked.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — edges Courier→Core Systems (line 46), Core Systems→Insights (line 67), Insights→Courier (line 84) form a three-node cycle.
- Disconfirming checks run: hard-blocking vs soft preference — every edge uses hard sequencing language ("once", "after", "gated on", "sequenced behind") and none says "ideally" or "would benefit from", so no edge is soft; staged-milestone interleaving — searched all three pages for an earlier milestone (beta, RC, preview, staging) that could interleave and found none: Courier names GA specifically, Core Systems' GA is gated on validation "in production", and Insights' validation needs the instrumented stream, so no valid ordering is quotable; awareness-plus-resolution-plan — all three notes sections restate the gate and none names a way to break the cycle, so no downgrade applies.
- Inference labels: that Courier's CR3.1 instrumentation is the same work Insights' IN2.1 waits on is analyst inference — Insights names "Courier instruments the new driver-app event stream" and CR3.1 is the only instrumentation work anywhere on Courier's page, but no document states the equivalence. Every edge itself is quoted verbatim.
- Verdict: CONFIRMED (all six load-bearing quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier and Insights in week 1 and breaks one edge in writing — e.g. GA the SDK against a staging validation of schema v3, or have Courier instrument two pilot flows on a pre-GA build so Insights can validate — then re-date all three KRs against the agreed order.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Company evidence (why it rolls up): "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: one metric name, two measurements — different numerator events (job completed within the window vs. delivery scanned at the destination), different denominators (all completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly) and different systems of record (Ops Console vs. Billing warehouse). The 13-point baseline gap (91% vs. 78%) and the two targets (95% vs. 85%) are therefore not comparable, yet both are reported against the same C2 driver, so an exec rollup of "on-time delivery" can be made to say either thing.
- Detection check that fired: AL-08 heuristic — metric-name blocking across teams, then a diff of each side's stated definition (formula, window, population, data source). The 91%/78% pair also generated an AL-09 candidate; per AL-09's rule it is reported here instead, because the definition split explains the gap.
- Disconfirming checks run: normalize-before-diff — normalized both formulas and they do not reduce to one measurement (they differ on numerator event, denominator population, window and source system); superseded-definition check — searched the company priorities section and all five team pages for a glossary or house definition of on-time delivery rate and found none, so neither definition supersedes the other; AL-03 duplication considered and cross-referenced rather than filed separately, since the collision is the root cause that makes the two teams' targets incomparable.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against the source file)
- Recommended resolution owner: the C2 owner (Noor E., who owns the priorities page) convenes Dispatch (Mei L.) and Accounts (Georg B.) to publish one definition of on-time delivery rate with one system of record, and to restate whichever KR loses its definition against the surviving baseline — before the first monthly customer report of the quarter.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27)
- Dispatch evidence (the dependency and its commitment level): "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31) and "*Commitment: KRs are committed unless marked (stretch).*" (`input/sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's KR is committed under its page's own convention and its full 600 assumes a portal that Accounts lists as stretch and conditions on the billing migration landing early. The scopes disagree as well: Dispatch counts 600 trial starts against a portal Accounts scopes to "the first 40 partner accounts".
- Detection check that fired: AL-12 edge-label comparison on the acknowledged Dispatch→Accounts dependency (AL-01 did not fire — Accounts does carry a portal KR), plus the target-arithmetic check on whether the consumer's number needs the producer's full target.
- Disconfirming checks run: labeling-scheme check — Dispatch's page states its convention explicitly and DS2.2 carries no stretch mark, so the committed reading is the team's own, not an assumption; consumer-hedging check — searched DS2.2's text and Dispatch's notes for a hedge or discount on the portal and found only an assertion of the dependency ("DS2.2 assumes the partner portal launch"), with no reduced expected value; producer-side check — Accounts' notes repeat the condition ("Portal timing depends on how fast the billing migration goes"), which strengthens rather than kills the finding.
- Inference labels: the scope arithmetic — that 600 trial starts cannot come from 40 partner accounts without an unstated trials-per-partner rate — is analyst inference; neither page states that rate.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) and Dispatch lead (Mei L.) decide by end of week 2 whether the portal is committed; if it stays stretch, Dispatch re-baselines DS2.2 to a number reachable without it and records the reduced target.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`input/sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`input/sample-portfolio-2.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: both statements name the same metric, the same instrument and the same period, and they differ by eight points. If the business review is right, AC2.2's "86 → 90" is a twelve-point ask wearing a four-point label — the KR is calibrated against a starting point the company's own review contradicts, and it is committed under the Accounts page's convention.
- Detection check that fired: AL-09 heuristic — the metric catalog holds two stated baselines for canonical metric "Customer CSAT" in the same period, differing far beyond rounding.
- Disconfirming checks run: as-of-date check — both cite Q4 2026 explicitly ("Q4 2026 baseline" and "ended Q4 2026"), so a date difference does not explain the gap; definitional/population split (AL-08) check — both cite "quarterly relationship survey" and no page in the export states a different population, scale or filter for either number, so no definitional explanation was found; supersession check — the Accounts page is dated later (2027-01-08) than the review (2026-12-15) but restates a Q4 2026 baseline rather than a newer measurement, so it does not supersede it.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) reconciles the two figures with the Q4 review owner and restates AC2.2 against the surviving baseline before the quarter's first check-in.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "Ship with confidence *(supports C2 — enterprise churn)*" (`input/sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence (all three child KRs): "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62); "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63); "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64) — all three: `input/sample-portfolio-2.md` › Objective CS2: Ship with confidence
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: the objective claims C2, but none of its three KRs measures churn or any of the three drivers C2 names; all three could be achieved in full in a quarter where enterprise churn rises, which makes the link decorative rather than causal.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's page names as needed? All three fail.
- Disconfirming checks run: parent-page contributor list — the company priorities section names C2's drivers and lists neither deploy velocity, change-failure rate nor CI time among them; child-page mechanism statement — Core Systems' notes mention only the SDK gate and "The cost work is our C4 commitment." (line 70), with no churn mechanism; corpus-wide search — no other page in the export states a delivery-velocity-to-churn relationship, so nothing could be quoted to kill the finding.
- Inference labels: none — all load-bearing text quoted. No causal claim is asserted in either direction; the finding is that no source states one.
- Verdict: CONFIRMED (all five quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) either states the mechanism in the objective — the most quotable candidate is change-failure rate feeding the escalation backlog that C2 names, which Accounts' AC2.1 already measures — or re-anchors CS2 as an internal enabler with no company link, before the quarter's first review.

### [Major] AL-10 Strategy coverage gap: Company priority C1 ↔ all five teams
- Company evidence: "grow ARR from $14M to $17.5M run-rate by end of Q1, led by enterprise dispatch adoption and frictionless self-serve billing." (`input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 10)
- Portfolio evidence (the closest near-misses, from the objectives that claim C1): "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27); "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (`input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23); "Billing-system migration covering 38% → 100% of the 6,400 self-serve accounts (migration tracker)." (`input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 109)
- Conflict: C1's headline outcome is a revenue number dated inside this quarter, and no KR in the portfolio measures revenue. C1's two named levers are staffed — enterprise dispatch adoption by Dispatch, self-serve billing by Accounts — but the three nearest KRs are funnel counts and a migration coverage count, none of which states a conversion rate or a revenue value, so nobody's Q1 scorecard moves when the ARR target misses.
- Detection check that fired: AL-10 top-down strategy trace — for each company priority and each target named under it, search all five team pages for coverage; C1's ARR target returns zero hits.
- Disconfirming checks run: synonym re-search — searched every line of the file for "ARR", "revenue", "run-rate", "MRR" and "bookings"; the only hit is C1 itself on line 10; near-miss check — the three quoted KRs above were examined and each stops short of revenue (trial starts and signed pilots are funnel counts with no stated conversion; the billing migration is coverage of an internal system), so none counts as coverage; named-owner check — the priorities page names an owner for the page ("Owner: Noor E. (CEO)") but assigns the ARR number to no team and names no function outside the swept set, so this is a portfolio hole and not an ownership note; comparison sweep — C3's retention target is carried by Courier's CR1.2 (line 40) and C4's cost target by Core Systems' CS1.2 (line 59), which confirms the gap is specific rather than an artifact of the search. C2's FY27 churn number is likewise unmeasured, but its three named drivers each have an Accounts objective and its horizon runs past this quarter, so it is not filed here.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against the source file)
- Recommended resolution owner: the priorities-page owner (Noor E., CEO) assigns the ARR run-rate number to a named team for Q1 — the two candidates are Dispatch and Accounts, whose objectives already claim C1 — or restates C1's Q1 expectation as the funnel numbers the portfolio actually measures.

### [Minor] AL-05 Cascade drift: Courier ↔ Company priority C3
- Courier evidence: "Every driver in the region hears about Coppervale from another driver" (`input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 42) and its only KR, "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Company evidence: "driver-app weekly retention from 71% to 80% across FY27." (`input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 12)
- Conflict: C3's metric is weekly retention; CR2's only KR counts installs, an acquisition measure. Achieving 45,000 referral installs in full would not by itself move the parent's metric, so the "(supports C3)" link is decorative as written.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KR measures neither the parent's metric nor any driver of it named in the strategy source.
- Disconfirming checks run: parent-page contributor list — C3 states only its retention number and names no workstreams, so no source names referral growth as a needed contribution; child-page mechanism — Courier's notes say only "referral growth is our big swing this quarter" (line 49), which asserts importance rather than a retention mechanism; sibling-coverage check — Courier's CR1.2 does carry C3's own metric ("Driver-app weekly retention 71% → 78%", line 40), so C3 is not left uncovered by the portfolio, which holds this finding at Minor.
- Inference labels: any claim that referral-driven installs dilute a retention cohort would be analyst inference and is not relied on here; the finding rests only on the quoted absence of a stated mechanism.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Courier lead (Tomás R.) either re-anchors CR2 to the growth priority it actually serves or adds a KR measuring retention of referred drivers, so the objective's claim on C3 is paid for.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights in week 1 to break one edge of the telemetry cycle in writing and re-date all three KRs — owner: Core Systems lead, Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with a stated population and system of record, and split DS1's two end-states into ranked objectives — owner: Dispatch lead, Mei L. (resolves §3 AP-13 Ambiguous Denominator, §3 AP-11 Objective as Kitchen Sink).
3. Decide by end of week 2 whether the partner portal is committed or stretch, and re-baseline DS2.2 if it stays stretch — owners: Accounts lead, Georg B., with Dispatch lead, Mei L. (resolves §4 AL-12 Commitment asymmetry).
4. Publish one definition and one system of record for "on-time delivery rate" and restate the losing KR against the surviving baseline — owner: priorities-page owner, Noor E., with Dispatch and Accounts (resolves §4 AL-08 Terminology collision).
5. Reconcile the CSAT baseline against the Q4 2026 business review and restate AC2.2 before the first check-in — owner: Accounts lead, Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Assign C1's ARR run-rate target to a named team for Q1, or restate C1's quarterly expectation as the funnel numbers teams actually measure — owner: CEO, Noor E. (resolves §4 AL-10 Strategy coverage gap).
7. State CS2's mechanism to C2 or re-anchor it, and rewrite CS1 so the objective names the change its KRs deliver — owner: Core Systems lead, Adaeze O. (resolves §4 AL-05 Cascade drift: Core Systems ↔ C2, §3 AP-10 BAU Dressed as OKR).
8. Add the commitment convention to Courier's page, label the referral bet as stretch with a named lever and a leading KR, and re-anchor CR2 — owner: Courier lead, Tomás R. (resolves §3 AP-07 Unmoored Moonshot, §3 AP-08 Committed vs Aspirational Not Labeled, §4 AL-05 Cascade drift: Courier ↔ C3).
9. Rank AC1–AC4 instead of marking all four P0, and move the partner-portal KR under AC4 with a trust measure replacing it in AC3 — owner: Accounts lead, Georg B. (resolves §3 AP-05 Everything Is a P0, §3 AP-12 Orphan KR — Accounts).
10. Replace the App Store rating KR with a dashboard-usage measure and name an individual owner on IN2.2 — owner: Insights lead, Halima D. (resolves §3 AP-12 Orphan KR — Insights, §3 AP-15 Ownerless KR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.5); Critical finding AP-13 Ambiguous Denominator on DS2.4): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `input/sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.2); Critical finding AL-11 Circular dependency, plus AP-07 Unmoored Moonshot): re-run single-team mode — "Review the Courier team's (driver app) Q1 2027 OKRs alone, in depth. Source: `input/sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.1); Critical finding AL-11 Circular dependency, plus AP-10 BAU Dressed as OKR): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `input/sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.4); Critical finding AL-11 Circular dependency, plus AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `input/sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.4), above the needs-rework threshold, and no Critical finding — its findings are Major and are covered by §5 items 3, 5 and 9.
