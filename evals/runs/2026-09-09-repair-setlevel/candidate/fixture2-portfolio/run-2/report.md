# Coppervale — Q1 2027 OKR Portfolio Review

*Scope: 5 teams (Dispatch, Courier, Core Systems, Insights, Accounts) · Period: Q1 2027 · Mode: portfolio · Source: `sample-portfolio-2.md` (Confluence export: company priorities page 91050, team pages 91112 / 91116 / 91120 / 91124 / 91128, Q4 business review page 91031) · Strategy source: "Company Q1 2027 priorities" (page 91050).*

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The worst alignment risk is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — three committed KRs with no valid execution order, and no team's page shows awareness of the loop.
The most consequential goodness defect is **AP-13 Ambiguous Denominator** (Dispatch's "failure rate" KR, the portfolio's only Critical goodness finding); no anti-pattern recurs — each of the eight found appears exactly once, spread across four teams, so quality problems here are individual defects rather than a systemic drafting habit.
Two shared numbers are not shared at all: "On-time delivery rate" carries two incompatible definitions (Dispatch vs Accounts) and Customer CSAT carries two different Q4 baselines (Accounts vs the Q4 business review).
Accounts marks all four objectives P0 and says so explicitly, so the portfolio's most-loaded team encodes no trade-off; Core Systems' one C2-linked objective measures nothing C2 names.
Recommended first action: Core Systems (as the SDK owner) convenes Courier and Insights within one week to break the telemetry loop by agreeing a staged sequence, before any of the three can start their quarter.

---

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.49) · Core Systems B (3.03) · Courier B (3.17) · Insights B (3.34) · Accounts B (3.45).

- Dispatch: K7=2 — DS2's trial-starts KR measures acquisition, not daily dispatch use.
- Core Systems: O1=2 — "Continue running the platform smoothly" restates the standing job, no delta.
- Courier: K3=2 — referral installs 3,000 → 45,000 is 15x with no stated mechanism.
- Insights: K7=2 — an App Store rating KR sits under the exec-dashboard objective.
- Accounts: K3=2 — CSAT baseline 86 contradicts the Q4 review's 78, so ambition is unverifiable.

---

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" names no population — failed jobs, failed routes, failed deliveries or failed trial starts are all plausible readings — and a search of the whole export for "failure" returns only this KR and Core Systems' unrelated "Change-failure rate 18% → 8% of production deploys" (line 63), so no definition exists anywhere to settle it; any of several numbers can be reported as 3% and none can be disputed.
- Scores affected: K1=1, K5=2
- Suggested rewrite: "KR DS2.4: Job failure rate — dispatched jobs that end in a failed or cancelled state as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — the denominator and named source are OKR-Ninja's; the 6% → 3% figures are quoted from line 29]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (`sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — dispatcher satisfaction and DE/FR market entry — are bundled into one objective, and its KRs split cleanly into those two unrelated groups ("Enterprise dispatcher NPS 24 → 40", line 22; "Signed pilot customers in DE and FR: 0 → 6", line 23), so the team can hit half the objective and call it done, with no way to rank the halves against each other.
- Scores affected: O2=2, K6=2 (DS1 set), K7=3
- Suggested rewrite: split into two ranked objectives — "O DS1 (ranked first): Enterprise dispatchers get through their whole day without leaving Coppervale. KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard 'Dispatcher NPS')." and "O DS3: Coppervale is a real option for logistics operators in DE and FR. KR: Signed pilot customers in DE and FR: 0 → 6 (CRM 'Intl Pilots' view)." [proposal — objective text is OKR-Ninja's; both KR targets are quoted from lines 22–23]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter. SDK timing per Core Systems' plan." (`sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target carries no named lever, no intermediate milestone and no resourcing signal — the page's only "how" is the phrase "our big swing", which states appetite, not mechanism — so the number cannot be planned against or honestly scored mid-quarter, and it is the sole KR under its objective.
- Scores affected: K3=1, K6=0 (CR2 set), K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral prompt shipped in week 2 (App Store + Play attributed installs); leading KR CR2.2 (committed): share of active drivers sending at least one referral invite `<baseline>`% → `<target>`% (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (set-level — the Courier page header states no commitment convention): "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (`sample-portfolio-2.md` › Courier team (driver app) — Q1 2027 › line 36)
- Evidence (the convention every other team page carries, absent here): "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Evidence (stretch varies wildly inside the unlabeled set): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (`sample-portfolio-2.md` › Objective CR1: Drivers finish every shift without fighting the app › line 39) and "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a search of the Courier section (lines 35–49) for "commit", "aspiration", "stretch" and "P0" returns nothing, while the same search returns the convention line on all four other team pages (lines 19, 55, 76, 93); a set that mixes a 0.4-point reliability increment with a 15x bet and labels neither corrupts expected-attainment maths and leaves every reader — including the two teams sequenced behind CR3.1 — to guess which Courier KRs are promises.
- Scores affected: set-level (no single O/K instance); it is why K3 must be judged unaided at CR1.1=3 and CR2.1=1
- Suggested rewrite: add to the Courier page header, matching the org convention quoted at line 19 — "Commitment: KRs are committed unless marked (stretch)." — and mark CR2.1 "(stretch)" while leaving CR1.1, CR1.2, CR3.1 and CR3.2 committed. [proposal — no new numbers]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (`sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue" plus "smoothly" describes the team's standing duty rather than a change it intends to cause, so the objective is achieved by default staffing and displaces a real goal; it also pulls in an unrelated KR — "Cloud cost per completed delivery $0.42 → $0.30" (line 59) serves the company's cost priority, not platform smoothness.
- Scores affected: O1=2, O2=2, O3=2, K7=2
- Suggested rewrite: "O CS1: Product teams stop losing days to platform incidents. KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Engineering hours lost to platform incidents per month `<baseline>` → `<target>` (incident review)." — and move "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard 'Unit Cost')" under its own cost objective, where its C4 link is direct. [proposal — placeholder target; the Sev-1 and cost figures are quoted from lines 58–59]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: there is no causal chain in two steps or fewer from a consumer app-store rating to leadership using the exec dashboard suite, and the KR shares no noun, audience or system with its objective — it measures the driver app, a surface Courier owns; hitting it would not move the objective, and missing it would not show the objective failed.
- Scores affected: K7=2 (IN1 set), K6=3
- Suggested rewrite: replace with a KR that measures the objective's own end-state — "KR IN1.3: Share of the Monday exec review's agenda metrics served from the exec suite rather than ad-hoc extracts `<baseline>`/`<total>` → `<target>`/`<total>` (Looker usage stats)" — and hand "Driver-app App Store rating 4.1 → 4.6 (App Store Connect)" to Courier under CR1, where driver experience is the stated outcome. [proposal — placeholder target; the 4.1 → 4.6 figures are quoted from line 81]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (`sample-portfolio-2.md` › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page's own convention promises a named owner per KR and every other Insights KR has one (Halima D., Vik M., lines 79–84), so "TBD" is an unfilled slot rather than a convention gap — and it sits on the one KR that needs seven other squads to change behaviour, which is exactly the work that stalls without a single accountable name.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights), with the nine squad leads listed in the tracker." [proposal — owner name to be filled by the Insights lead; the 2/9 → 9/9 figures are quoted from line 85]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence (set-level — all four objectives carry the same top priority): "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (`sample-portfolio-2.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95); "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99); "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103); "Objective AC4 (Priority: P0): Billing runs itself" (line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (`sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four uniform P0 labels — with a note making the refusal to rank explicit — encode no trade-off, so when eight committed KRs across onboarding, support, delivery reporting and a billing migration compete for one team, sequencing falls to whoever asks loudest mid-quarter rather than to the plan; it is also why Accounts never told Dispatch that the partner portal (AC3.2) is the piece most likely to slip (see §4 AL-12 Commitment asymmetry).
- Scores affected: set-level (no single O/K instance); its closest downstream effect is K7=2 on the AC3 set, where the conditional portal KR sits under a P0 objective about delivery-promise trust
- Suggested rewrite: rank the existing four without changing their text — "P0: AC3 Customers trust the delivery promises we report (the C2 driver two other teams depend on). P1: AC1 New customers reach first value in days, not weeks. P1: AC2 Support answers arrive before customers ask twice. P2: AC4 Billing runs itself — migration continues; the portal (AC3.2) drops first if AC3 or AC1 are at risk." [proposal — the ranking is OKR-Ninja's; objective text is quoted from lines 95–107]

---

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema-v3 validation in production, and Insights waits on Courier's driver-app instrumentation — a closed three-team cycle in which nobody can start, so every KR on the loop (CR3.1, CS3.1, IN2.1, plus CR3.2 which measures loss on instrumented flows) fails as written. Each page shows awareness of its own upstream only — "SDK timing per Core Systems' plan." (line 49), "GA is gated on schema v3 validation (Insights)." (line 70), "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (line 87) — and none mentions the loop or a plan to break it.
- Detection check that fired: graph-structural cycle detection on the dependency map (AL-11 heuristic) — three "once/after" edges resolving to the closed cycle Courier → Core Systems → Insights → Courier.
- Disconfirming checks run: hard blocking vs soft preference — all three edges use hard sequencing language ("once", "after", "after"), none says "ideally" or "would benefit from", so no edge is soft; staged-milestone interleaving — searched all three pages and their notes (lines 46–49, 67–70, 84–87) for a beta or partial-scope milestone that could break the loop and found none, the only pre-GA state stated being "SDK v1 is code-complete" (line 70), which CR3.1 is not written to build on; commitment level — Core Systems (line 55) and Insights (line 76) both state "Commitment: KRs are committed unless marked (stretch)." and none of the three KRs is marked stretch. Result: the cycle survives every check.
- Inference labels: identifying Insights' "the new driver-app event stream" with Courier's "all 14 core driver flows" is analyst inference — no document states the equivalence, though each edge names its counterparty team explicitly, so no edge itself is inferred.
- Verdict: CONFIRMED (all three edge quotes re-verified character-for-character against lines 46, 67 and 84)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier and Insights within one week to agree a staged sequence — e.g. a pre-GA SDK build against schema v3 for one Courier flow, Insights validates on that flow, Courier completes the remaining 13, Core Systems GAs — and each team restates its KR's precondition against the agreed milestone.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two different measurements — a completed-jobs denominator versus all scheduled deliveries including cancellations, weekly versus monthly, Ops Console versus Billing warehouse — which is why the two baselines sit 13 points apart (91% vs 78%). Dispatch asserts a single house methodology — "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31) — while Accounts reports the customer-facing number the company priority refers to ("keeping the delivery promises we report to customers", line 11), so any exec rollup of "on-time delivery" mixes two incompatible figures. The 13-point baseline gap is a secondary AL-09 Baseline disagreement reading, reported here instead because the definitional split fully explains it.
- Detection check that fired: metric-name blocking (AL-08 form (a)) — the string "On-time delivery rate" appears in two teams' KRs; each side's formula, window, population and data source were then diffed.
- Disconfirming checks run: normalize-before-diffing — normalized, the populations genuinely differ (completed jobs vs all scheduled deliveries including cancellations), as do window and system of record, so this is not cosmetic wording drift; superseded-definition check — searched all five team pages, the company priorities page and the Q4 appendix for a glossary or shared definition and found none, and the pages' last-updated dates (Dispatch 2027-01-04, Accounts 2027-01-08) show neither definition supersedes the other. Result: the collision stands.
- Inference labels: none — both definitions, both systems of record and the exec-reporting link (line 11) are quoted; no mechanism is inferred.
- Verdict: CONFIRMED (both definitions re-verified character-for-character against lines 26 and 104)
- Recommended resolution owner: Accounts lead (Georg B.), as owner of the customer-reported number, agrees one canonical "On-time delivery rate" definition with Dispatch lead (Mei L.) before the first monthly business review; the other team renames its metric (e.g. "job on-time completion") and both KRs restate baseline and target under the agreed definition.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), committed under the page rule "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)", marked "(stretch — only if the billing migration lands early)" (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's committed 600-trial-start KR rides entirely on a portal its producer lists as stretch and conditional on a separate billing migration; Dispatch's note shows it knows who builds the portal but not at what commitment level — "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31) — and its 600 assumes the full stretch deliverable rather than an expected value.
- Detection check that fired: edge label comparison on an acknowledged dependency (AL-12 heuristic) — the dependency is not an AL-01, because Accounts does carry the portal, but the two ends carry mismatched commitment labels.
- Disconfirming checks run: missing-label check — both teams state a labelling scheme (Dispatch line 19, Accounts line 93), so this is a genuine mismatch rather than one side simply never stating a level; consumer-hedging check — searched Dispatch's KR text and notes (lines 27, 31) for any discount, contingency or reduced fallback number and found none, while Accounts' own note reinforces the conditionality ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111). Result: the finding stands at full strength.
- Inference labels: none — both commitment labels, the dependency sentence and the conditionality note are quoted.
- Verdict: CONFIRMED (both sides re-verified character-for-character against lines 19, 27, 31, 105 and 111)
- Recommended resolution owner: Dispatch lead (Mei L.) and Accounts lead (Georg B.) decide within two weeks either to promote the portal to a committed Accounts KR with a dated milestone, or to re-cut DS2.2 to a portal-independent trial-start number with the portal-dependent portion split out as an explicitly stretch KR.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`sample-portfolio-2.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: two stated current values eight points apart for the same metric, the same named instrument and the same period — the KR even labels its number "Q4 2026 baseline". If 78 is right, AC2.2 is a +12 ask carrying a committed label (line 93) under a P0 objective, not the +4 step the page implies; if 86 is right, the number the company reported to leadership in its Q4 review is understated.
- Detection check that fired: metric-catalog baseline collection (AL-09 heuristic) — two stated baselines for the same canonical metric and period differing beyond rounding.
- Disconfirming checks run: as-of-date check — both statements name Q4 2026, so no timing explanation exists; definition/population check (AL-08 first) — both name the "quarterly relationship survey", and a search of the export for "CSAT" returns only these two lines, with no second definition, population split or alternative instrument to explain the gap. Result: no innocent explanation found.
- Inference labels: none — both baselines and both instrument descriptions are quoted; this finding does not assert which figure is correct.
- Verdict: CONFIRMED (both baselines re-verified character-for-character against lines 101 and 118)
- Recommended resolution owner: Accounts lead (Georg B.) reconciles the CSAT baseline with the Q4 review owner before the quarter's first check-in and restates AC2.2 against the agreed figure; if 78 stands, the 90 target must be re-calibrated or re-labelled.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities (C2)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Core Systems evidence: "Objective CS2: Ship with confidence" (`sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 61), whose three KRs are "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Conflict: C2 names its three drivers explicitly and none of them is deploy frequency, change-failure rate or CI duration; all three CS2 KRs could be hit in full in a quarter where enterprise logo churn worsens, so the stated parent link is decorative. This is drift, not a coverage hole: Accounts covers all three of C2's named drivers (AC1.1 line 96, AC2.1 line 100, AC3.1 line 104), so C2 is staffed — CS2 simply is not what staffs it.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic) — the child's KRs measure neither the parent's metric nor any driver the parent names.
- Disconfirming checks run: parent-page contributing-workstream check — line 11 enumerates C2's drivers and none matches a CS2 KR; child-page mechanism check — Core Systems' notes state only "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." (line 70), naming no churn mechanism; corpus-wide check — a search for "churn" across the whole export returns only the company priority (line 11) and the CS2 heading (line 61), so no document states a release-throughput→churn driver relationship. Result: no documented mechanism; the link is decorative.
- Inference labels: the finding asserts the absence of any documented mechanism, not that release throughput cannot affect churn; the judgement that these three KRs would not move C2's metric is analyst inference.
- Verdict: CONFIRMED (the company priority and all three CS2 KRs re-verified character-for-character against lines 11 and 61–64)
- Recommended resolution owner: Core Systems lead (Adaeze O.) with the C2 owner (Noor E.) either re-parents CS2 to C4 — where CS1.2 and CS3 already sit — or adds a KR measuring one of C2's three named drivers, before the quarter's first business review.

---

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to break the telemetry loop with a staged pre-GA sequence and restate each KR's precondition — owner: Core Systems lead Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Define the denominator and system of record for Dispatch's failure-rate KR before the quarter's first weekly ops review — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator).
3. Agree one canonical "On-time delivery rate" definition and rename the other team's metric — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-08 Terminology collision).
4. Decide whether the partner portal is committed or stretch and re-cut Dispatch's 600 trial starts accordingly — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Customer CSAT baseline against the Q4 business review and restate AC2.2 — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Re-parent "Ship with confidence" to C4 or add a KR measuring one of C2's three named drivers — owner: Core Systems lead Adaeze O. (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 and name what drops if the quarter tightens — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Attach a named lever and a leading KR to the referral target, or relabel it aspirational — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot).
9. Reframe CS1 as a change with a delta and move the cost KR to its own C4 objective — owner: Core Systems lead Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR).
10. Move the App Store rating KR to Courier and name an accountable owner for the v3 onboarding KR — owner: Insights lead Halima D. (resolves §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR).

*Below the top ten (Minor, fix at the next page edit): split Dispatch's DS1 into two ranked objectives (§3 AP-11 Objective as Kitchen Sink) — owner: Mei L.; add the commitment convention line to the Courier page and label its KRs (§3 AP-08 Committed vs Aspirational Not Labeled) — owner: Tomás R.*

---

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.49); Critical §3 AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md` › 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.03); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md` › 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.17); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md` › 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.34); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md` › 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.45), above the rubric's needs-rework threshold, and no Critical finding (its findings are Major — §3 AP-05, §4 AL-08, §4 AL-12, §4 AL-09).
