# Coppervale — Q1 2027 OKR portfolio review

**Mode:** portfolio (5 teams in scope) · **Period:** Q1 2027 · **Strategy source:** "Company Q1 2027 priorities" (Confluence page 91050, C1–C4)
**Teams in scope:** Dispatch · Courier (driver app) · Core Systems · Insights · Accounts (billing & customer success)
**Corpus:** `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md` — the single source read for this review. Source refs below shorten it to `sample-portfolio-2.md › <heading> › line N`; line numbers are that file's own.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 1 Minor findings.
The portfolio's worst alignment risk is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — a three-team cycle with no valid execution order, and no team's page shows awareness of it.
The most common goodness anti-pattern is **AP-12 Orphan KR**; no anti-pattern repeats across teams, so the tie is broken by impact — the orphan pattern is what drives K7 Set Coherence & Sufficiency to the portfolio's weakest column.
Two teams report an "On-time delivery rate" under one name with different numerators, denominators, windows, and systems of record (AL-08), while the company's C2 priority depends on "keeping the delivery promises we report to customers."
Dispatch carries the only Critical goodness defect: a KR whose percentage has no stated population (AP-13), which caps its DS2 objective at D.
Accounts states the strongest OKR set in the portfolio but ranks all four objectives P0 (AP-05), so it encodes no trade-off.
Recommended first action: convene Courier, Core Systems, and Insights to break the telemetry cycle before mid-quarter — three teams' Q1 KRs are unstartable until one edge is cut.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.51) · Core Systems B (3.07) · Courier B (3.22) · Insights B (3.30) · Accounts B (3.49).

- Dispatch: K7=2 — DS1 bundles two unrelated end-states; DS2.2 measures acquisition, not daily use.
- Core Systems: O1=2 — CS1 states a standing duty, not a change (AP-10 BAU Dressed as OKR).
- Courier: K3=2 — CR2.1's 15x referral target states no mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1.3 measures the driver app, not exec dashboard use (AP-12 Orphan KR).
- Accounts: K3=2 — AC2.2's stated CSAT baseline of 86 contradicts the Q4 actual of 78.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: the KR never says failure rate *of what* — dispatched jobs, route-plan builds, delivery attempts, or API calls are all plausible populations on this page, and the sibling KR DS2.1 shows the team knows how to state a denominator ("as a share of all completed jobs"), so any of several numbers could be claimed as 3%. The named source, "ops weekly report", is a document rather than a system of record, so no reader can reconstruct the population from the tooling either.
- Scores affected: K1=1, K5=2 (this Critical anti-pattern caps the DS2 per-OKR score at 1.9)
- Suggested rewrite: "KR DS2.4: Dispatch job failure rate — jobs ending in a `<named failure state>` as a share of all jobs dispatched, measured weekly in the Ops Console on the same denominator convention as KR DS2.1 — 6% → 3% by end of Q1 2027." [proposal — placeholder denominator]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing enterprise dispatchers versus prospective customers in new geographies — and the KRs split cleanly along that seam rather than jointly evidencing one outcome: "Enterprise dispatcher NPS 24 → 40" (line 22) serves the first clause and "Signed pilot customers in DE and FR: 0 → 6" (line 23) serves the second, so neither clause has a second KR to corroborate it. "Delight" is also the kind of abstraction two readers gloss differently, which is what holds O2 at 2.
- Scores affected: O2=2, K7=2
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers run their console day on Coppervale instead of their old one — KR DS1.1 unchanged: 'Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")'. Objective DS3 (ranked second): Coppervale runs live enterprise dispatch in DE and FR — KR DS3.1 unchanged: 'Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)'; KR DS3.2: dispatch jobs completed in DE/FR `<baseline>` → `<target>` per week." [proposal — placeholder target]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "referral growth is our big swing this quarter" (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Also: AP-08 Committed vs Aspirational Not Labeled
- Why it's a problem: CR2.1 is a 15x target and the page's only supporting text calls it a "big swing" — that names an attitude, not a mechanism: no referral feature, campaign, incentive, intermediate milestone, or resourcing signal appears anywhere on the Courier page, so the number decorates the plan rather than steering it. The absence compounds the labeling gap: I searched the whole Courier section (lines 35–49) for the terms `committed`, `stretch`, and `aspirational` and found none of them, while the other four team pages each carry "*Commitment: KRs are committed unless marked (stretch).*" (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19) — so a 15x bet and a 0.4-point crash-free tightening sit at the same, unstated, commitment level, and neither expected attainment nor the moonshot judgement can be made from the page.
- Scores affected: K3=1 (CR2.1), team K3=2
- Suggested rewrite: add to the Courier page header "*Commitment: KRs are committed unless marked (aspirational).*", then: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter (App Store + Play attributed installs), driven by the in-app referral card shipping in week `<n>`; KR CR2.2 (committed): drivers sending ≥1 referral invite `<baseline>` → `<target>` per week (Amplitude)." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue running the platform smoothly for every team" states the team's standing job with no change of state in it — it is achieved by default staffing, and it occupies an objective slot that a real delta could hold. The KRs beneath it do carry deltas ("Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4", line 58), which is why the finding is Major rather than Critical, but the objective they hang under promises no world any team can recognise as different at quarter's end, and "smoothly" is exactly the abstraction two readers gloss differently.
- Scores affected: O1=1, O2=2
- Suggested rewrite: "Objective CS1: Product teams stop losing days to platform incidents and cost surprises — KR CS1.1 unchanged: 'Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4'; KR CS1.2 unchanged: 'Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")'; KR CS1.3: product-team engineer-days lost to platform incidents `<baseline>` → `<target>` per quarter." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence: "Objective IN1: Execs run Monday mornings from our dashboards" (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: there is no causal chain in two steps or fewer from a public App Store rating to executives running Monday mornings from Insights' dashboards — the KR shares no noun, audience, surface, or system of record with its objective (its siblings measure Looker viewers and Looker load time). Achieving 4.6 would leave the objective exactly where it started, and missing it would say nothing about the dashboards; worse, the levers that move an app-store rating live in the driver app, which the Courier team owns, so Insights has taken a number it cannot act on.
- Scores affected: K7=2 (IN1 set), K6=3
- Suggested rewrite: "KR IN1.3: Monday exec-review dashboards refreshed, green, and loaded before 08:00 on review day: `<baseline>`/`<total>` → `<total>`/`<total>` (Looker schedule monitor)" — and move "Driver-app App Store rating 4.1 → 4.6 (App Store Connect)" to Courier's Objective CR1, whose team owns the app's quality levers. [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the owner field is filled in with "TBD" on a page that promises "Owners listed per KR" and names an individual on every other Insights KR (Halima D., Vik M.), so this is a stated gap rather than a convention the team does not use. It is also the KR that most needs a named driver: onboarding seven more squads is coordination work across teams that are not Insights, and no one is accountable for chasing them. I searched the whole corpus for any other assignment of this work and found none outside line 85.
- Scores affected: K4=0 (IN2.2), team K4=3
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual on the Insights team>`; squads and their onboarding dates listed on the tracker by week `<n>`." [proposal — placeholder owner]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four objectives and eight KRs all carry the same top-priority label, and the team's own note makes the refusal explicit — a uniform P0 across the whole set encodes no trade-off, so when onboarding, escalations, delivery reporting, and the billing migration compete for the same people mid-quarter, nothing on the page says what gives. The label carries no information once it is on everything, and the one KR that does state a trade-off ("Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*.", line 105) contradicts the claim that all four are equally non-negotiable.
- Scores affected: no rubric dimension scores cross-objective prioritisation, so this is recorded as a set-level defect and does not move Accounts' O1–K7 cells
- Suggested rewrite: "P0: AC1 New customers reach first value in days, not weeks. P1: AC2 Support answers arrive before customers ask twice; AC3 Customers trust the delivery promises we report. P2 (drop to the roadmap if AC1 slips): AC4 Billing runs itself." [proposal — the ranking is OKR-Ninja's, not the team's; Accounts owns the final order]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier → Core Systems → Insights → Courier is a closed cycle, and every edge is written as a hard precondition ("once", "after", "after"), so no team can start: the SDK cannot GA before the schema is validated, the schema cannot be validated before the driver-app stream is instrumented, and the stream cannot be instrumented before the SDK GAs. Four KRs across three teams — CR3.1, CS3.1, IN2.1, and CR3.2, which measures loss on the flows CR3.1 would instrument — are unstartable as written.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — three quotable consumer→producer edges forming a closed loop.
- Disconfirming checks run: (a) hard block vs. soft preference — all three edges re-read; none carries a softening term such as `ideally`, `prefer`, or `would benefit from`; all three use bare temporal preconditions, so no edge is soft; (b) staged-milestone interleaving — Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) raises the possibility that Courier could instrument against a pre-GA build, but no team's text authorises that, and Courier's KR names GA specifically, so no valid interleaving is quotable; (c) awareness plus resolution plan (the downgrade path) — each team's notes acknowledge only its own inbound edge ("SDK timing per Core Systems' plan.", line 49; "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready.", line 87), and no page mentions the cycle or a plan to break it, so no downgrade applies.
- Inference labels: none — all three edges are quoted verbatim; the pre-GA interleaving raised in disconfirming check (b) is explicitly *not* relied on and is labelled analyst inference where mentioned.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 46, 67, 70, 84, 87)
- Recommended resolution owner: Core Systems (Adaeze O.) to convene Courier and Insights within two weeks and cut one edge — the cheapest candidate is releasing SDK v1 to Courier as a pre-GA build so instrumentation can start, with GA staying gated on schema validation; whichever edge is cut, all three KRs must be re-sequenced on their pages before the cycle's first milestone. [proposal — placeholder target]

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: one metric name carries two different measurements — different numerator (job completed in window vs. delivery scanned at destination), different denominator (all completed jobs vs. all scheduled deliveries *including cancellations*), different window (weekly vs. monthly), and different system of record (Ops Console vs. Billing warehouse). Accounts' denominator is strictly larger, which is why the same company reports 91% and 78% for "On-time delivery rate" in the same quarter, and C2 makes this the number Coppervale reports to customers — so an exec rollup or a customer QBR can cite either figure truthfully and neither team is wrong.
- Detection check that fired: AL-08 form (a), same name / different definition — the metric-catalog diff of formula, window, population, and data source for a metric name used by two teams.
- Disconfirming checks run: (a) different wording ≠ different definition — both definitions normalised (numerator, denominator, window, source) and they differ on all four axes, so the collision is real, not cosmetic; (b) superseded definition — searched the corpus for a glossary or shared metric-definition page, none exists, and the two pages' last-updated dates (2027-01-04 and 2027-01-08) show neither supersedes the other; (c) AL-09 Baseline disagreement considered as the root cause for the 91% vs. 78% gap and rejected — the definitional split fully explains the gap, and AL-09's own heuristic routes such cases to AL-08; (d) AL-03 Duplicated / overlapping objectives considered and rejected — the populations genuinely differ and each team measures the surface it owns, so this is a naming collision, not duplicated work. Dispatch's note "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31) confirms the team knows its own definition is local, but neither page references the other's.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both definitions and the C2 line re-verified character-for-character against lines 26, 104, 11)
- Recommended resolution owner: Accounts (Georg B.), as owner of the customer-facing number under C2, to agree one canonical definition with Dispatch (Mei L.) before the first monthly customer report of Q1 — publish it as a named metric definition, and rename whichever team's internal measure diverges (e.g. `<internal-measure name>`) so the two never collide in a rollup again. [proposal — placeholder target]

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27)
- Dispatch evidence: "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: DS2.2 is unmarked on a page that states "Commitment: KRs are committed unless marked (stretch)." (line 19), so it is a committed KR — and it depends entirely on a deliverable that its producer has labelled stretch and made conditional on a second, unrelated programme landing early. The arithmetic is worse than a straight label mismatch: Dispatch's 600 trial starts assume not merely 100% of Accounts' stretch but well beyond it, since Accounts' full stretch target is a portal live for only "the first 40 partner accounts". Dispatch's note states the assumption without hedging it.
- Detection check that fired: AL-12 edge-label comparison on an acknowledged cross-team dependency — the producer's deliverable is present in its OKRs (so this is not AL-01), but the commitment labels on the two ends do not match and the consumer's target arithmetic consumes the producer's full stretch.
- Disconfirming checks run: (a) missing label ≠ mismatch — both teams have explicit labelling schemes (Dispatch line 19, Accounts line 93, both "*Commitment: KRs are committed unless marked (stretch).*"), so the labels are read from stated conventions rather than inferred; (b) consumer already discounts the producer — Dispatch's notes (line 31) and Accounts' notes ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111) were both searched for a hedge, a contingency, or a discounted expected value, and neither contains one; (c) producer acknowledgment — AC3.2 does name the portal, which correctly rules out AL-01 Unacknowledged dependency as the classification.
- Inference labels: none — all load-bearing text quoted, including both commitment conventions.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against lines 19, 27, 31, 105)
- Recommended resolution owner: Dispatch (Mei L.) to take the question to Accounts (Georg B.) in the first two weeks of Q1 and settle it one of three ways — Accounts promotes the portal to committed, Dispatch re-labels DS2.2 aspirational, or DS2.2's target is rebased on a portal-independent channel at a figure the two teams size together. [proposal — placeholder target]

### [Major] AL-09 Baseline disagreement: Accounts ↔ Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the KR names its baseline as the Q4 2026 figure from the quarterly relationship survey and states it as 86; the Q4 2026 business review states the same instrument's same-period result as 78. Both cite "quarterly relationship survey" and both name Q4 2026, so one of the two numbers is wrong. The gap is not cosmetic: it reframes a +12-point ask as a +4-point one, so the KR reads as a modest improvement while the real work is three times larger — and this sits under a P0 objective whose page declares its KRs committed.
- Detection check that fired: AL-09 metric-catalog baseline collection — two stated current values for the same canonical metric and the same period, differing far beyond rounding.
- Disconfirming checks run: (a) different as-of dates — both sides say Q4 2026 explicitly, so no timing explanation exists; (b) different populations or definitions (the AL-08 route) — both quote the same instrument name, "quarterly relationship survey", and the corpus was searched for any second CSAT definition, segment split, or alternate survey, of which there is none (CSAT appears only on lines 101 and 118); (c) superseding page version — the business-review page (91031) is dated 2026-12-15 and the Accounts page (91128) 2027-01-08, so Accounts wrote later and had the review available, which strengthens rather than kills the finding.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 101 and 118)
- Recommended resolution owner: Accounts (Georg B.) to reconcile the baseline against the Q4 relationship survey of record in week 1 and restate AC2.2 on whichever figure survives — if 78 is correct, the target and the staffing behind it need re-sizing, not just the number on the page. [proposal — placeholder target]

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priorities
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." · "Change-failure rate 18% → 8% of production deploys (incident review tags)." · "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (sample-portfolio-2.md › Objective CS2: Ship with confidence › lines 62, 63, 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: CS2 claims C2 as its parent, but none of its three KRs measures enterprise churn or any of the three drivers C2 names for it — the parent page enumerates its own contributing levers, and deploy frequency, change-failure rate, and CI latency are not among them. All three KRs could be hit in full in a quarter where enterprise churn worsens, which is the tell for a decorative link: a sound engineering-velocity set wearing someone else's parent.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child's KRs measure neither the parent's metric, nor a documented driver of it, nor a deliverable the parent's own page names as needed.
- Disconfirming checks run: (a) mechanism documented outside the child's OKR text — C2's own line was searched for named contributing workstreams and it names three, none of which CS2 touches; Core Systems' notes ("SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.", line 70) were searched for a stated velocity→churn path and contain none, referring the team's own commitment to C4 instead; (b) a better-fitting parent — C4's "consolidate our duplicated data and telemetry pipelines" (line 13) is already claimed by CS1 and CS3, so the drift is a mis-parenting of CS2 specifically, not a team-wide anchoring failure; (c) severity check — C2 does not name Core Systems as a contributor, which makes this Minor by AL-05's default, escalated one level to Major because CS2's KRs are explicitly committed under "Commitment: KRs are committed unless marked (stretch)." (line 55).
- Inference labels: the claim that deploy frequency, change-failure rate, and CI latency cannot plausibly move enterprise logo churn through any of C2's stated drivers is analyst inference — no Coppervale document states or denies the relationship; the absence of any stated mechanism is quoted fact.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 11, 13, 55, 61, 62, 63, 64, 70)
- Recommended resolution owner: Core Systems (Adaeze O.) with the C2 owner to either re-parent CS2 under a priority its KRs actually serve, or add one KR measuring a named C2 driver — for example enterprise-visible incidents `<baseline>` → `<target>` per quarter — before the first monthly strategy review. [proposal — placeholder target]

## 5. Prioritized action list

1. Convene Courier, Core Systems, and Insights to cut one edge of the telemetry cycle and re-sequence CR3.1, CS3.1, and IN2.1 — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with a stated population and a system of record before the first weekly ops report — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Agree one canonical "on-time delivery rate" definition and rename the divergent internal measure — owner: Accounts lead (Georg B.) with Dispatch (resolves §4 AL-08 Terminology collision).
4. Settle whether the partner portal is committed or DS2.2 is aspirational, and rebase the 600 if neither — owner: Dispatch lead (Mei L.) with Accounts (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile AC2.2's CSAT baseline against the Q4 relationship survey of record and re-size the target — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
6. Re-parent CS2 or add a KR measuring one of C2's named churn drivers — owner: Core Systems lead (Adaeze O.) with the C2 owner (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 so the set encodes a trade-off — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Move the App Store rating KR to Courier and name an individual owner for the v3 onboarding KR — owner: Insights lead (Halima D.) (resolves §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR).
9. State the referral mechanism behind CR2.1 and add a commitment convention to the Courier page — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot and its AP-08 Committed vs Aspirational Not Labeled).
10. Restate CS1 as a change in the world rather than a standing duty — owner: Core Systems lead (Adaeze O.) (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.51); Critical AP-13 Ambiguous Denominator, plus AL-08 Terminology collision and AL-12 Commitment asymmetry): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91112 (DSP-OKR-Q1), section 'Dispatch team — Q1 2027' of the local export `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Courier (driver app)** (roll-up B (3.22); qualifies on the Critical AL-11 Circular dependency, with AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91116 (COUR-OKR-Q1), section 'Courier team (driver app) — Q1 2027' of the local export `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Core Systems** (roll-up B (3.07); qualifies on the Critical AL-11 Circular dependency, with AP-10 BAU Dressed as OKR and AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91120 (CORE-OKR-Q1), section 'Core Systems team — Q1 2027' of the local export `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Insights** (roll-up B (3.30); qualifies on the Critical AL-11 Circular dependency, with AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91124 (INS-OKR-Q1), section 'Insights team — Q1 2027' of the local export `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Accounts (billing & customer success)** does not qualify: its roll-up grade B (3.49) is above the rubric's needs-rework threshold and it carries no Critical finding.
