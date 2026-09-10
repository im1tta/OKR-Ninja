# Coppervale — Q1 2027 OKR portfolio review

*Scope: 5 teams (Dispatch, Courier, Core Systems, Insights, Accounts), period Q1 2027, portfolio mode. Sources: `sample-portfolio-2.md` (Confluence export: company priorities page 91050, five team OKR pages, Q4 2026 business-review extract). Strategy source in scope: "Company Q1 2027 priorities" (page 91050, CO-PRIO-Q1FY27). No Atlassian connection was available for this run, so every absence claim below is bounded by that export.*

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 14 Major, 2 Minor findings.
The portfolio's biggest threat is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — a three-team cycle with no valid execution order, and no team's page shows awareness of it.
Two teams' committed plans also ride on text the other side never promised: Dispatch's committed 600 trial starts depend on a partner portal Accounts marks "(stretch)" (AL-12 Commitment asymmetry), and Dispatch and Accounts report "On-time delivery rate" under two different formulas and baselines into the same company priority (AL-08 Terminology collision).
The most common quality issue is **AP-01 Task Masquerading as KR** (Courier and Accounts each count their own rollout as the result), tied with **AP-12 Orphan KR** (Insights and Accounts each carry a KR that would not move its objective).
Only one KR is outright unmeasurable: Dispatch's failure-rate KR names no population (AP-13 Ambiguous Denominator), which caps its objective at D.
Recommended first action: Core Systems convenes Courier and Insights this week to break the telemetry cycle by naming which milestone (code-complete SDK vs. GA) actually unblocks instrumentation.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 3 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.5) · Core Systems B (3.2) · Courier B (3.2) · Insights B (3.3) · Accounts B (3.4).

- Dispatch: K6=2 — DS1's two KRs are unrelated lagging measures; DS2 capped at D by AP-13.
- Core Systems: O1=2, O2=2 — two objectives state standing duty and abstraction, not change.
- Courier: K3=2 — one KR is a 15x install target with no stated mechanism.
- Insights: K7=2 — an App Store rating KR sits under an exec-dashboard objective.
- Accounts: K7=2 — the partner-portal KR serves a different objective than the one it sits under.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never states the population — failed dispatch jobs, failed route builds, failed deliveries and failed deploys are all live readings on this page — so the 3% can be claimed against whichever base is most flattering, and the KR can never be honestly scored. Its cited source is a generic weekly report rather than a named system of record, so no second reader can reconstruct the number.
- Scores affected: K1=1, K5=2 (this Critical anti-pattern caps objective DS2 at 1.9 per the rubric's roll-up caps)
- Suggested rewrite: "KR DS2.4: Failed dispatch jobs — jobs cancelled or returned undelivered as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — the population and source are placeholders; 6% and 3% are quoted from line 29]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing enterprise dispatchers and prospects in two new countries — are bundled into one objective, and its KRs split cleanly into the same two groups with nothing in common, so the objective can be half-achieved and cannot be scored as one thing. "Delight" is also the kind of abstraction two readers would gloss differently.
- Scores affected: O1=3, O2=2, K6=2, K7=3
- Suggested rewrite: "Objective DS1: Enterprise dispatchers would rather run their day in Coppervale than in the tools they replaced. — KR DS1.1: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS"). — Objective DS3 (ranked second): Coppervale is live with paying logistics customers in DE and FR. — KR DS3.1: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." [proposal — figures reused verbatim from lines 22–23]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target carries no named lever, no intermediate milestone and no resourcing signal — the only supporting text on the page calls it a "big swing" without saying how installs get there — so the number functions as decoration rather than a goal anyone can plan against or fail honestly.
- Scores affected: K3=1, K6=0 (CR2 is a single-KR set)
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app refer-a-driver bonus (App Store + Play attributed installs). — KR CR2.2 (committed, leading): Drivers sending ≥1 referral invite `<baseline>` → `<target>` per week (Amplitude)." [proposal — placeholder targets]

### [Major] AP-01 Task Masquerading as KR — Courier
- Evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Why it's a problem: the KR opens with a delivery verb and its 0/14 → 14/14 measure counts Courier's own rollout — per AP-01, a coverage count of the team's own delivery is the deliverable restated as a number, not a result anyone outside the team experiences. It is fully satisfied the day the last flow is wired up, whether or not the objective's actual claim — that driver actions are visible to the teams that need them — is true.
- Scores affected: K2=1, K3=2, K5=3
- Suggested rewrite: "KR CR3.1: Core driver flows whose events are queryable by other teams in the shared pipeline at under 1% loss: 0/14 → 14/14 (Grafana "Courier Events" board), with teams outside Courier running ≥1 weekly report off driver-flow events 0 → `<target>`." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (the set's spread of stretch): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39), alongside "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the convention every other team states): "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Why it's a problem: the Courier page is the only team page in the export with no commitment convention — a search of the whole file for "Commitment", "committed", "stretch" and "aspirational" returns lines 19, 55, 76, 93 and 105, none of them inside Courier's section (lines 35–49) — so a 0.4-point reliability improvement and a 15x growth bet carry the same implied promise, and neither expected attainment nor the moonshot judgement in AP-07 can be calibrated.
- Scores affected: K3=2 (Courier team dimension)
- Suggested rewrite: add to the page header "Commitment: KRs are committed unless marked (stretch)." and mark KR CR2.1 "(stretch)", leaving CR1.1, CR1.2, CR3.1 and CR3.2 committed. [proposal — convention text reused verbatim from line 19]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence: "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 58)
- Evidence: "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 59)
- Why it's a problem: the objective commits the team to continuing its standing job and names no change — no direction, reduction or improvement over today — which is exactly the shape AP-10 catches. Under the anti-pattern's rule the two genuine baseline→target deltas in its KRs do not rescue it: the objective, not its KRs, is what the anti-pattern is about, and as written a quarter of pure business-as-usual scores it achieved.
- Scores affected: O1=2, O2=2
- Suggested rewrite: "Objective CS1: Cut the platform's incident load and unit cost until no team plans around us. — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. — KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." [proposal — KR figures reused verbatim from lines 58–59]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its objective): "Objective IN1: Execs run Monday mornings from our dashboards" (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: moving the driver-app store rating would not put a single exec on an Insights dashboard — the KR shares no noun, surface or audience with its objective and there is no causal chain in two steps from a store rating to Monday-morning dashboard use. The levers that move that rating sit in the driver app, which Courier owns — its quality KRs are "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) — so Insights is accountable for a number it cannot move.
- Scores affected: K7=2 (IN1 set coherence)
- Suggested rewrite: "KR IN1.3: Weekly exec reviews in which every agenda item is answered from a dashboard view with no ad-hoc data request: `<baseline>` → `<target>` per quarter (Looker usage stats)." [proposal — placeholder targets]; if the App Store rating is to be owned at all, it belongs in Courier's CR1 set.

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own convention): "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page states that owners are listed per KR, and a sweep of the Insights section (lines 74–87) finds a named individual on IN1.1, IN1.2, IN1.3 and IN2.1 and "TBD" only here. The KR also asks seven further squads outside Insights to do the work, so with no accountable individual there is nobody to chase them — the KR most likely to slip is the one nobody is answerable for.
- Scores affected: K4=1
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights), with each squad's named migration contact recorded in the tracker." [proposal — owner placeholder; figures reused verbatim from line 85]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry the same top priority and the page says outright that no trade-off was made, so the set encodes no decision — when the billing migration runs late, which the page's own note says would sink the partner portal, nothing here says what gives, and eight KRs all claim first call on the same capacity.
- Scores affected: none at the instance level — AP-05 is scoped to the whole objective set per the rubric's one-finding-per-instance rule; its cost surfaces as the unranked contingency behind §4 AL-12 Commitment asymmetry.
- Suggested rewrite: "P0: AC1 New customers reach first value in days, not weeks. P1: AC2, AC3. P2: AC4 Billing runs itself — the migration continues, and the partner portal leaves the quarter unless AC1 lands by week `<n>`." [proposal — objective text reused verbatim from lines 95 and 107; ranking and week are placeholders]

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Evidence (its objective): "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Why it's a problem: making a partner portal available to 40 partner accounts has no causal chain in two steps to whether customers trust the delivery promises Coppervale reports — the KR shares no noun or audience with AC3, and its own contingency ties it to the billing migration, which lives under AC4. Its only real consumer is Dispatch's trial-start KR (see §4 AL-12 Commitment asymmetry), which the objective it sits under never mentions.
- Scores affected: K2=2, K6=2, K7=2 (AC3 set)
- Suggested rewrite: move it under AC4 and restate it as adoption — "KR AC4.3 (stretch — only if the billing migration lands early): Partner accounts self-serving at least one invoice through the partner portal 0 → 40 (Partner CRM)." [proposal — figures and stretch label reused verbatim from line 105]

### [Major] AP-01 Task Masquerading as KR — Accounts
- Evidence: "Billing-system migration covering 38% → 100% of the 6,400 self-serve accounts (migration tracker)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 109)
- Why it's a problem: the measure is a migration coverage percentage of Accounts' own delivery — the shape AP-01's exclusion clause names as still firing, because no self-serve account experiences anything different when a row moves to the new system. The objective's real claim, that billing runs itself, is left resting on AC4.1 alone: coverage could hit 100% while manual corrections stay flat.
- Scores affected: K2=1, K3=2, K5=3
- Suggested rewrite: "KR AC4.2: Self-serve accounts invoiced end-to-end on the new billing system with no manual correction that month: 38% → 100% of the 6,400 self-serve accounts (Billing QA dashboard)." [proposal — figures reused verbatim from line 109]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier waits on Core Systems' GA, Core Systems waits on Insights' production validation, and Insights waits on Courier's instrumentation — a closed three-team cycle in which no team can start, so three KRs (CR3.1, CS3.1, IN2.1) and the C4 telemetry-consolidation priority they all serve are unachievable as written.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — three edges (Courier→Core Systems, Core Systems→Insights, Insights→Courier), each carrying an "once"/"after" blocking phrase quoted above.
- Disconfirming checks run: hard blocking vs. soft preference — a search of the whole export for "ideally", "would benefit" and "prefer" returns no hits and all three edges read as gates, so no edge is soft; staged-milestone interleaving — Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 70) and Insights' note "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 87) each restate their own gate and neither states a pre-GA path Courier may use, so no valid interleaving is quotable; awareness-plus-resolution-plan — each note names only its own upstream and no page names the cycle, so no downgrade applies.
- Inference labels: none — all load-bearing text quoted; every edge in the cycle carries its own verbatim quote.
- Verdict: CONFIRMED (all three edge quotes and both notes re-read character-for-character against the export)
- Recommended resolution owner: Core Systems lead (Adaeze O.) to convene Courier and Insights in week 1 of the quarter and cut one edge in writing — the quotable option is letting Courier instrument against the code-complete SDK build (line 70) so Insights can validate v3 in production and Core Systems can then GA — then rewrite CR3.1, CS3.1 and IN2.1 to name the milestone each truly needs.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name carries two formulas — different numerator, different denominator (all completed jobs vs. all scheduled deliveries including cancellations), different cadence (weekly vs. monthly) and different system of record (Ops Console vs. Billing warehouse) — producing 91% and 78% for the same quarter. Both objectives roll into the company priority that names "keeping the delivery promises we report to customers" (sample-portfolio-2.md › Company Q1 2027 priorities › line 11), so the exec view of that promise has two irreconcilable numbers and neither team is accountable for the other's.
- Detection check that fired: AL-08 blocking — a metric name used by ≥2 teams; each team's page hunted for a definition and the two definitions diffed on formula, window, population and data source.
- Disconfirming checks run: normalize-then-diff — the definitions do not reduce to one measurement (the cancellation population alone separates them), so the collision is real rather than cosmetic; superseded-glossary check — the export contains no glossary, and Dispatch's note asserts a team-local method, "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31), which is the opposite of a shared definition; AL-09 pre-check — the 91% vs. 78% baseline gap is explained by the definition split, so per AL-09's control it is reported here as AL-08 rather than as a second baseline finding; AL-02 lookalike control — not filed as a metric conflict, since both targets move the same direction.
- Inference labels: the adversarial reading — that Dispatch can raise its rate by cancelling at-risk jobs, which its denominator drops and Accounts' denominator keeps — is analyst inference; no Coppervale document states the tradeoff. Cross-references AL-02 Conflicting metrics / adversarial incentives and AL-09 Baseline disagreement as secondary IDs.
- Verdict: CONFIRMED (both definitions re-read character-for-character against their pages)
- Recommended resolution owner: Insights lead (Halima D.), as owner of the exec suite this number lands in, to convene Dispatch and Accounts and publish one on-time-delivery definition — one formula, one system of record, one cadence — before the mid-quarter review, with both targets restated against it.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), on a page stating "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19), with the note "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), with the note "Portal timing depends on how fast the billing migration goes (see AC3.2)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: a committed Dispatch KR is fully coupled to a deliverable its producer marks explicitly stretch and conditional — and the arithmetic does not survive even the stretch landing, since Dispatch counts on 600 trial starts flowing through a portal Accounts scopes to the first 40 partner accounts.
- Detection check that fired: AL-12 edge-label comparison on an acknowledged dependency edge (Dispatch→Accounts, acknowledged by AC3.2 and therefore not an AL-01), plus the target-arithmetic coupling check (600 against 40).
- Disconfirming checks run: labeling-scheme check — Dispatch states its own convention (line 19) and DS2.2 carries no "(stretch)" mark, so the committed reading is Dispatch's own rather than inferred; consumer-hedging check — Dispatch's note says its KR "assumes" the launch rather than discounting it, and Accounts' note makes the timing conditional on the billing migration, so both checks strengthen rather than kill the finding.
- Inference labels: none — both commitment labels and both numbers are quoted from the two pages.
- Verdict: CONFIRMED (both quotes and both commitment labels re-read against their pages)
- Recommended resolution owner: Dispatch lead (Mei L.) with Accounts lead (Georg B.), in week 1: either Accounts commits the portal for a named account count and date, or DS2.2 is re-cut onto a trial source Dispatch controls and the portal-dependent share is labelled stretch on both pages.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the KR cites a Q4 2026 baseline of 86 for a metric the Q4 2026 business review reports at 78 — same named instrument, same period, an eight-point gap. The KR's apparent +4 is really a +12 ask, so its ambition, its expected attainment and any mid-quarter progress read against 86 are all mis-calibrated, on a KR the page's convention makes committed.
- Detection check that fired: AL-09 metric-catalog blocking — every stated baseline collected per canonical metric; two values for "Customer CSAT" in the same period differ beyond rounding.
- Disconfirming checks run: as-of-date check — both statements name Q4 2026, so no timing difference explains the gap; AL-08 definition-split check — both cite the same "quarterly relationship survey" and the export contains no second CSAT definition, so no population difference explains it; sample check — the review states n = 412 and the KR states no different population.
- Inference labels: none — both baseline statements quoted verbatim with their as-of period.
- Verdict: CONFIRMED (both figures re-read character-for-character against their pages)
- Recommended resolution owner: Accounts lead (Georg B.) to reconcile with the Q4 review owner in week 1 and restate AC2.2 from the surviving number — if 78 stands, the KR needs re-targeting or a stretch label, because a 12-point CSAT gain and a 210 → 60 backlog cut in one quarter are not the same size of bet.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), whose KRs are "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64) — all three under sample-portfolio-2.md › Objective CS2: Ship with confidence
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: C2 enumerates its three drivers and engineering delivery cadence is not among them; none of CS2's KRs measures churn, a named driver of it, or a deliverable C2's text calls for. All three could be hit in full in a quarter where enterprise churn rises, which makes the "(supports C2 — enterprise churn)" link decorative — and it is the only place Core Systems claims a retention contribution.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — do the child's KRs measure the parent metric, a documented driver of it, or a deliverable the parent's page names? All three legs fail.
- Disconfirming checks run: documented-mechanism search — the priorities page names three drivers (quoted above) and no engineering-velocity workstream; Core Systems' own note claims only the cost work, "The cost work is our C4 commitment." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 70); a search of the export for "churn" returns lines 11 and 61 only, so no page states a deploy-frequency-to-churn relationship; near-miss check — C2's three named drivers are each staffed by Accounts (AC1, AC2, AC3), confirming the drivers are covered elsewhere rather than by CS2.
- Inference labels: none — the parent's drivers and all three child KRs are quoted; the absence of a linking mechanism rests on the stated search, not on inference.
- Verdict: CONFIRMED (parent priority and all three KRs re-read against their pages)
- Recommended resolution owner: Core Systems lead (Adaeze O.) with the priorities owner (Noor E., CEO): either re-anchor CS2 to C4 Run lean, where CI and deploy economics genuinely sit, or add one KR measuring a named C2 driver — otherwise the company reads CS2 as churn work that is not.

### [Major] AL-05 Cascade drift: Courier ↔ Company Q1 2027 priorities
- Courier evidence: "Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)*" (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 42), whose single KR is "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Company evidence: "driver-app weekly retention from 71% to 80% across FY27." (sample-portfolio-2.md › Company Q1 2027 priorities › line 12)
- Conflict: C3's only stated metric is weekly retention, while CR2's only KR counts attributed installs — an acquisition measure. Achieving 45,000 referral installs would not move weekly retention, so an objective consuming the team's self-declared big swing this quarter claims a pillar it cannot move.
- Detection check that fired: AL-05 mechanism check on the explicit "(supports C3)" parent link — the child KR measures neither the parent metric nor a documented driver of it.
- Disconfirming checks run: documented-mechanism search — Courier's note offers only "referral growth is our big swing this quarter." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49), with no path from installs to retention, and the priorities page names no referral or acquisition workstream under C3; sibling-coverage check — Courier's own "Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 40) already carries C3's metric properly, which isolates CR2's link as decorative rather than as a second contribution to the same pillar.
- Inference labels: the new-cohort dilution mechanism — a large install influx depressing a weekly retention cohort — is analyst inference; no Coppervale document states it, and the finding does not depend on it, since the mechanism check already fails.
- Verdict: CONFIRMED (parent metric, objective link and KR re-read against their pages)
- Recommended resolution owner: Courier lead (Tomás R.) to either re-anchor CR2 to a growth priority — C1 Win mid-market logistics is the only one in the export that names growth — or add a retention-linked KR (for example week-4 retention of referred drivers) so the C3 claim is paid for.

### [Major] AL-01 Unacknowledged dependency: Insights ↔ Dispatch / Courier / Core Systems / Accounts
- Insights evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Counterparty evidence (closest near-misses, both partial): "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46) and "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Conflict: the KR moves seven further squads from 2/9 to 9/9 on work those squads must perform — adopting v3 event conventions — while no other team in the export commits to it and the KR itself names no owner. Insights carries the number; the delivery sits in other teams' quarters.
- Detection check that fired: AL-01 edge-acknowledgment check — dependency phrases extracted per KR ("Product squads onboarded to…"), resolved to owning teams, then searched on the producers' side.
- Disconfirming checks run: search-before-absence — a search of the whole export for "v3" and "convention" returns lines 67, 70, 84, 85 and 87 only, all on the Insights and Core Systems pages, while "onboard" elsewhere returns only Accounts' customer-onboarding KRs (lines 95–97) and the company priority (line 11); near-miss check — Courier's instrumentation KR and Core Systems' SDK-adoption KR (quoted above) cover SDK rollout, not conformance to v3 event conventions, and neither names the conventions or the onboarding tracker; backlog check — no Jira or Confluence backlog was reachable in this run, so the producers' unscheduled backlog could not be swept, which bounds the claim to the export.
- Inference labels: the mapping from "Product squads" to the four other teams in this export is analyst inference — the KR names no squad, and the export holds five teams against a denominator of nine.
- Verdict: PLAUSIBLE (both quotes verified verbatim, but the counterparty set is inferred and no source outside the export could be searched)
- Recommended resolution owner: Insights lead (Halima D.) to name the nine squads and the KR's owner in week 1, and to secure either a landing KR or a scheduled epic per squad before the number is treated as committed.

## 5. Prioritized action list

1. Convene Courier and Insights to break the telemetry cycle by naming the milestone that actually unblocks instrumentation (code-complete SDK vs. GA) and rewriting CR3.1, CS3.1 and IN2.1 accordingly — owner: Core Systems lead, Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Redefine DS2.4's population and system of record, and split DS1 into a dispatcher-satisfaction objective and a regional-expansion objective — owner: Dispatch lead, Mei L. (resolves §3 AP-13 Ambiguous Denominator and AP-11 Objective as Kitchen Sink).
3. Publish one on-time-delivery definition — one formula, one denominator, one system of record — and restate both teams' targets against it — owner: Insights lead, Halima D. (resolves §4 AL-08 Terminology collision; cross-refs AL-02 and AL-09).
4. Settle the partner portal in writing: commit it with an account count and a date, or re-cut DS2.2 and label the portal-dependent share stretch on both pages — owner: Dispatch lead, Mei L., with Accounts lead, Georg B. (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the CSAT baseline against the Q4 2026 review and restate AC2.2 from the surviving number — owner: Accounts lead, Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 and CR2 to the priorities their KRs actually move, or add one KR each that measures a named driver of C2 and of C3 — owner: Noor E. (CEO, priorities-page owner) with both team leads (resolves both §4 AL-05 Cascade drift findings).
7. Name the nine squads and an accountable owner for IN2.2, secure a landing commitment per squad, and move the App Store rating KR out of IN1 — owner: Insights lead, Halima D. (resolves §4 AL-01 Unacknowledged dependency, §3 AP-15 Ownerless KR and AP-12 Orphan KR — Insights).
8. Rank the four P0 objectives, move the partner-portal KR under AC4, and restate the billing migration as an invoicing outcome — owner: Accounts lead, Georg B. (resolves §3 AP-05 Everything Is a P0, AP-12 Orphan KR — Accounts and AP-01 Task Masquerading as KR — Accounts).
9. Add the commitment convention to the Courier page, label CR2.1 stretch with a named referral lever, and restate CR3.1 as queryable-events adoption — owner: Courier lead, Tomás R. (resolves §3 AP-08 Committed vs Aspirational Not Labeled, AP-07 Unmoored Moonshot and AP-01 Task Masquerading as KR — Courier).
10. Rewrite CS1's objective to name the change its KRs already deliver instead of the continuation of standing duty — owner: Core Systems lead, Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.5); Critical AP-13 Ambiguous Denominator on KR DS2.4): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91112 (DSP-OKR-Q1), 'Dispatch team — Q1 2027', as exported in `sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.2), above the needs-rework threshold, but party to the Critical AL-11 Circular dependency as the SDK-GA edge): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91120 (CORE-OKR-Q1), 'Core Systems team — Q1 2027', as exported in `sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.2); party to the Critical AL-11 Circular dependency as the instrumentation edge): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91116 (COUR-OKR-Q1), 'Courier team (driver app) — Q1 2027', as exported in `sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.3); party to the Critical AL-11 Circular dependency as the schema-validation edge): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91124 (INS-OKR-Q1), 'Insights team — Q1 2027', as exported in `sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.4), above the needs-rework threshold, and no Critical finding — its findings are Major (AP-05, AP-12, AP-01, AL-08, AL-09, AL-12).
