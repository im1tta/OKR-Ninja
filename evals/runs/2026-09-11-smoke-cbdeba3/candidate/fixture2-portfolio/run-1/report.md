# Coppervale — Q1 2027 OKR portfolio review

*Mode: portfolio (5 teams in scope). Period: Q1 2027. Corpus: `sample-portfolio-2.md` (company priorities page, five team OKR pages, Q4 2026 business-review appendix). Strategy source in scope: "Company Q1 2027 priorities" (C1–C4).*

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The portfolio's biggest threat is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems gates that GA on Insights' schema validation, and Insights sequences its validation behind Courier's instrumentation — three teams, no valid execution order.
Quality defects do not repeat: each of the 8 goodness findings is a distinct AP-XX ID, so no anti-pattern is "most common"; the most severe is **AP-13 Ambiguous Denominator** (Dispatch's DS2.4 names a "failure rate" with no population, so it can never be honestly scored).
Two teams report the same metric name under incompatible definitions (AL-08 Terminology collision on "On-time delivery rate": 91% → 95% vs 78% → 85%), and Accounts calibrates a committed CSAT target against a baseline the Q4 review contradicts by 8 points (AL-09 Baseline disagreement).
Dispatch's committed 600-trial-start KR rides on a partner portal Accounts lists as stretch (AL-12 Commitment asymmetry), and Core Systems' churn-linked objective measures only its own release pipeline (AL-05 Cascade drift).
Recommended first action: a Courier/Core Systems/Insights sequencing session in week 1 to break the telemetry cycle before any of the three teams' Q1 plans can be trusted.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 4 | 2 | 3 |
| Accounts | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.54) · Core Systems B (3.14) · Insights B (3.39) · Courier B (3.43) · Accounts A (3.58).

- Dispatch: K6=2 — DS1's two KRs are both end-of-quarter outcomes, leaving no mid-cycle steering signal.
- Core Systems: O1=2 — "Continue running the platform smoothly" and "Ship with confidence" name no changed end-state.
- Insights: K7=2 — IN1.3's App Store rating KR serves a different objective than exec dashboard use.
- Courier: K3=2 — CR2.1's 15x referral-install target states no mechanism, milestone, or resourcing signal.
- Accounts: K3=2 — AC2.2's CSAT baseline contradicts the Q4 review's 78, so ambition is unverifiable.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never states its population — failed jobs as a share of all jobs, failed route builds, failed API calls, or failed deliveries are all readable from the text, and each would give a different number, so any result can be claimed at quarter end. Its system of record is named only as "ops weekly report", which no other KR on the page cites, so even the agreed reading could not be checked.
- Scores affected: K1=1, K5=2, K2=3
- Suggested rewrite: "KR DS2.4: Failed dispatch jobs — jobs ending in a failure state as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (`sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (`sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing dispatchers' satisfaction and net-new geographic expansion — sit under one objective, and the KRs split cleanly into those two unrelated groups, so hitting one and missing the other leaves the objective's status undefined. "Delight" is also the kind of abstraction two readers gloss differently.
- Scores affected: O1=3, O2=2, K6=2, K7=3
- Suggested rewrite: "O DS1 (ranked first): Enterprise dispatchers would fight to keep Coppervale — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS"). O DS3: Coppervale runs live routes in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)."

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (`sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence: "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (`sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 58)
- Evidence: "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (`sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 59)
- Why it's a problem: the objective statement commits the team to *continuing* its standing duty and names no change at all — no direction, reduction, or improvement — so it is achieved by default staffing while displacing a goal that would say what gets better. The two real deltas quoted beneath it do not rescue it: the anti-pattern is a property of the objective, not of its KRs.
- Scores affected: O1=2, O2=2, O3=2
- Suggested rewrite: "O CS1: Product teams stop losing days to platform incidents, and platform cost stops eating our unit economics — KR: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4; KR: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")."

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence: "Execs run Monday mornings from our dashboards" (`sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: there is no causal chain in two steps or fewer from a public App Store rating of the driver app to leadership's use of Insights' dashboards; the KR shares no noun, audience, or surface with its objective, and the driver app belongs to Courier. Hitting it would not move IN1, and missing it would not tell a reader that IN1 failed.
- Scores affected: K7=2, K6=3
- Suggested rewrite: "KR IN1.3: Monday-review decisions citing an exec-suite dashboard `<baseline>` → `<target>` per quarter (source: Monday review notes)." [proposal — placeholder target] — and move the App Store rating KR under a Courier objective that owns the driver app.

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (`sample-portfolio-2.md` › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page's own convention is that owners are listed per KR, and this is the one KR that names none — "TBD" is a blank, not an owner — so the only KR whose delivery depends on nine other squads has nobody accountable for chasing them. Search performed: the Insights section (lines 74–87) and every other team section in the corpus were searched for any named individual attached to v3 onboarding; none appears.
- Scores affected: K4=0, K6=2
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)."

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 49)
- Why it's a problem: the target is a 15x step inside one quarter and the only "how" anywhere on the page calls it a "big swing" — no named lever, no intermediate milestone, no resourcing signal, and no aspirational label to set expectations. A target nobody can plan against decorates the page instead of steering the quarter, and it is the sole KR under CR2, so the objective has no fallback signal when it misses.
- Scores affected: K3=1, K6=0, K7=3
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → 12,000 this quarter (App Store + Play attributed installs), via the in-app referral prompt shipping in week 3. KR CR2.2 (committed, leading): Drivers sending ≥1 referral invite per week `<baseline>` → `<target>` (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (`sample-portfolio-2.md` › Courier team (driver app) — Q1 2027 › line 36)
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (`sample-portfolio-2.md` › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the convention every other team states, absent here): "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Why it's a problem: the set mixes a 0.4-point reliability increment with a 15x acquisition bet and carries no commitment convention and no per-KR label, so expected attainment cannot be computed and neither sandbagging nor moonshot can be judged from the page. Because Courier also sits on the telemetry cycle in §4, the downstream teams cannot tell whether CR3.1 is a promise or a hope. Search performed: the entire Courier section (lines 35–49), including its header line and its notes line, was searched for "committed", "aspirational", "stretch", and any 0.7-target convention — no match, while four of the five team pages carry the convention line quoted above.
- Scores affected: K3=2, K6=2
- Suggested rewrite: add to the Courier page header "Commitment: KRs are committed unless marked (stretch)." and then mark CR1.1, CR1.2, CR3.1 and CR3.2 committed and CR2.1 "(stretch)".

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (`sample-portfolio-2.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (`sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (`sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (`sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry an identical P0 label and the notes make the refusal to rank explicit, so the set encodes no trade-off — when onboarding, escalations, delivery reporting and the billing migration collide mid-quarter, the page gives the team no rule for what gives. It also makes the portfolio's other findings harder to resolve: §4's partner-portal asymmetry and the disputed CSAT baseline both sit inside this unranked block.
- Scores affected: K7=3, K3=2
- Suggested rewrite: "AC1 (P0): New customers reach first value in days, not weeks. AC2 (P0): Support answers arrive before customers ask twice. AC3 (P1): Customers trust the delivery promises we report. AC4 (P1): Billing runs itself." — with the notes line replaced by "If AC1 or AC2 is at risk at mid-quarter, AC4's migration slips first."

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 84)
- Core Systems evidence (notes): "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (`sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 70)
- Insights evidence (notes): "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 87)
- Conflict: Courier waits on Core Systems' SDK GA, Core Systems gates that GA on Insights' schema-v3 validation, and Insights sequences that validation behind Courier's instrumentation — a three-team cycle in which every team is second in line, so none of the three KRs has a valid execution order as written and all three can stall at 0% while every team reports itself blocked.
- Detection check that fired: graph-structural cycle detection on the dependency map (AL-11 heuristic) — edges Courier→Core Systems ("once Core Systems GAs the SDK"), Core Systems→Insights ("after Insights validates event schema v3 in production"), Insights→Courier ("after Courier instruments the new driver-app event stream").
- Disconfirming checks run: hard-block vs. soft-preference re-read of every edge — all three use blocking language ("once", "after", "gated on") and none hedges with "ideally" or "would benefit from", so no edge is soft. Staged-milestone interleaving — Core Systems' note that "SDK v1 is code-complete" shows a pre-GA build exists, but CR3.1 conditions on GA rather than on code-complete and no page states a pre-GA instrumentation path, so the milestones do not interleave as written. Awareness-plus-resolution-plan downgrade — all three notes lines were searched; each restates its own dependency and none proposes a sequencing resolution, so the downgrade to Minor does not apply. Commitment levels: Core Systems and Insights both state "KRs are committed unless marked (stretch)" and neither KR is marked, so two edges are explicitly committed; Courier's page states no convention (see §3 AP-08), but its edge is hard-blocking on its face.
- Inference labels: none — all three edges are quoted verbatim from the teams' own KR text.
- Verdict: CONFIRMED (all five quotes re-fetched and matched character-for-character against their source lines)
- Recommended resolution owner: Core Systems lead (Adaeze O.) to convene Courier and Insights in week 1 and cut one edge — e.g. Courier instruments against the code-complete SDK build, Insights validates v3 on that stream, Core Systems then GAs — and restate all three KRs with the agreed order before mid-quarter.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Company-priority evidence (why it rolls up): "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: one metric name, two incompatible measurements — different populations (completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly), different systems of record (Ops Console vs. Billing warehouse) — producing baselines 13 points apart and targets 10 points apart. Both feed C2's promise about "keeping the delivery promises we report to customers", so any exec rollup of "on-time delivery rate" is meaningless and neither team's number can be compared with the other's. Cross-reference: this definition split is also what explains the 91% vs. 78% baseline gap, which is why it is reported here rather than as AL-09 Baseline disagreement; the inconsistent targets on one shared-sounding outcome would otherwise read as AL-03 Duplicated / overlapping objectives.
- Detection check that fired: metric-catalog blocking on a metric name used by ≥2 teams (AL-08 heuristic, form (a)), followed by a formula/window/population/source diff of each team's stated definition.
- Disconfirming checks run: "different wording ≠ different definition" — both definitions normalized on numerator, denominator, window and data source; they diverge on all four, so they are not the same measurement. Superseded-page check — Dispatch's page was last updated 2027-01-04 and Accounts' 2027-01-08; neither cites the other's definition and no shared glossary page exists in the corpus, so neither supersedes the other. Near-miss quoted: Dispatch's note "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." asserts its own methodology but never reconciles it with Accounts'. AL-09 pre-check — a definitional explanation for the differing baselines was searched for and found, so the gap is not filed as a separate baseline disagreement.
- Inference labels: none — both definitions and both targets are quoted verbatim, and the exec-rollup exposure rests on the quoted C2 text.
- Verdict: CONFIRMED (all three quotes re-fetched and matched character-for-character against their source lines)
- Recommended resolution owner: Insights lead (Halima D.), as owner of the shared metric layer, to convene Dispatch and Accounts and publish one canonical "on-time delivery rate" definition with a single system of record before mid-quarter; DS2.1 and AC3.1 are then restated against it, with any segment-specific variant kept under a distinct name.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27)
- Dispatch evidence (commitment level): "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures" (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Accounts evidence (commitment level): "(stretch — only if the billing migration lands early)" (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: DS2.2 carries no stretch marker, so under Dispatch's own stated convention it is committed — and all 600 of its trial starts route through a portal Accounts lists as an explicitly conditional stretch item, conditional in turn on a second uncertainty (the billing migration's pace). Dispatch's committed number silently assumes 100% of Accounts' stretch deliverable lands, and lands early enough in the quarter for 600 trials to start; Accounts' stretch covers only "the first 40 partner accounts".
- Detection check that fired: dependency-map edge label comparison on an acknowledged (non-AL-01) edge — commitment labels compared on both sides, plus target-arithmetic coupling (AL-12 heuristic).
- Disconfirming checks run: "missing label ≠ mismatch" — Dispatch's labeling scheme was located and quoted rather than inferred, so DS2.2's unmarked status reads as committed by the page's own rule. Consumer-hedging check — Dispatch's note "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." states the assumption but discounts nothing and names no fallback, so the hedging that would kill or downgrade the finding is absent. AL-01 check — Accounts does carry the portal work (AC3.2), so this is not an unacknowledged dependency. Scale check — 40 partner accounts against 600 expected trial starts, so even a landed stretch may not carry the committed number.
- Inference labels: none — both commitment levels and both targets are quoted verbatim.
- Verdict: CONFIRMED (all four quotes re-fetched and matched character-for-character against their source lines)
- Recommended resolution owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) to decide in week 2 either to promote the portal to committed with the billing migration resourced accordingly, or to re-baseline DS2.2 to the trial volume reachable without the portal (`<revised target>`) and label the portal-dependent remainder stretch [proposal — placeholder target].

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`sample-portfolio-2.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: both statements name the same metric, the same instrument ("quarterly relationship survey") and the same period (Q4 2026), yet differ by 8 points. If the review's 78 is right, Accounts' committed KR is a +12 ask presented internally as a +4 one, and its ambition, its resourcing, and every mid-quarter progress call are calibrated against a starting point that does not exist.
- Detection check that fired: metric-catalog baseline collection for the canonical metric "Customer CSAT" — two stated baselines for the same metric and period differing beyond rounding (AL-09 heuristic).
- Disconfirming checks run: as-of date check — both are explicitly Q4 2026, so a date offset does not explain the gap. Definitional check (AL-08 pre-check) — both cite the "quarterly relationship survey"; the Accounts section (lines 91–111), the company priorities section (lines 7–13) and the appendix (lines 115–120) were searched for any CSAT definition, population split, or segment filter and none exists, so no population difference legitimises two values. Near-miss: the review's "n = 412" is the only population detail stated anywhere, and Accounts states none to contrast it against.
- Inference labels: none — both baseline statements are quoted verbatim; no value was computed or recalled.
- Verdict: CONFIRMED (both quotes re-fetched and matched character-for-character against their source lines)
- Recommended resolution owner: Accounts lead (Georg B.) to reconcile with the Q4 review's owner in week 1 and restate AC2.2 against the agreed number before the KR is locked; if 78 stands, re-scope the target and record the change in the notes.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (`sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence (child KRs in full): "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (`sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 62); "Change-failure rate 18% → 8% of production deploys (incident review tags)." (`sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 63); "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (`sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: CS2 claims C2 as its parent, but all three of its KRs are internal delivery-pipeline metrics and none measures enterprise churn or any of the three drivers C2 itself names. Every one of them could be hit in a quarter where enterprise churn worsens — the tell for a decorative link — and because C2's real drivers are all carried by Accounts, the claim also overstates how much of the churn priority is actually staffed.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic) — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's own page names as needed? All three answers are no.
- Disconfirming checks run: "activity KRs ≠ decorative link" — C2's own text was searched for named contributing workstreams and it names three ("onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers"), none of which is deploy velocity, CI time, or change-failure rate. Core Systems' notes were searched for a stated driver relationship: "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." names no churn mechanism. No other document in the corpus states that release velocity drives enterprise retention. Near-miss: change-failure rate is the one KR with a plausible customer-visible path, but no source states it, so it does not rescue the link. Escalation: CS2's KRs are committed under the page's stated convention, which lifts the default Minor to Major.
- Inference labels: the change-failure-rate → churn path weighed in the near-miss check is analyst inference and was not relied on; the finding rests only on quoted text.
- Verdict: CONFIRMED (all quotes re-fetched and matched character-for-character against their source lines)
- Recommended resolution owner: Core Systems lead (Adaeze O.) to agree with the C2 owner in week 2 either to re-parent CS2 to a delivery-capability priority or to add a KR measuring a C2-named driver (e.g. incidents touching enterprise accounts `<baseline>` → `<target>`) [proposal — placeholder target].

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to break the telemetry sequencing cycle and restate all three KRs in the agreed order — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-11 Circular dependency).
2. Rewrite Dispatch's DS2.4 with a named failure population, an explicit denominator and a system of record — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Publish one canonical "on-time delivery rate" definition and system of record, then restate DS2.1 and AC3.1 against it — owner: Insights lead (Halima D.) (resolves §4 AL-08 Terminology collision).
4. Decide whether the partner portal is committed or Dispatch's 600-trial-start KR is re-baselined without it — owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Q4 2026 CSAT baseline with the business review and restate AC2.2 against the agreed number — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
6. Re-parent Core Systems' CS2 or add a KR measuring a driver C2 actually names — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-05 Cascade drift).
7. Rank Accounts' four objectives P0/P1 and state what slips first when they collide — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Name an accountable individual for IN2.2 and move the App Store rating KR off the exec-dashboard objective — owner: Insights lead (Halima D.) (resolves §3 AP-15 Ownerless KR, AP-12 Orphan KR).
9. Add Courier's commitment convention and re-scope CR2.1 to a labeled aspirational target with a stated lever plus a leading KR — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot, AP-08 Committed vs Aspirational Not Labeled).
10. Restate Core Systems' CS1 as a change rather than a continuation, and split Dispatch's DS1 into two ranked objectives — owners: Core Systems lead (Adaeze O.) and Dispatch lead (Mei L.) (resolves §3 AP-10 BAU Dressed as OKR, AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.54); qualifies on criterion (b) — Critical finding AP-13 Ambiguous Denominator, plus inbound AL-08 Terminology collision and AL-12 Commitment asymmetry): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1, owner Mei L.); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.14); qualifies on criterion (b) — Critical finding AL-11 Circular dependency, plus AP-10 BAU Dressed as OKR and AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1, owner Adaeze O.); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.39); qualifies on criterion (b) — Critical finding AL-11 Circular dependency, plus AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1, owner Halima D.); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.43); qualifies on criterion (b) — Critical finding AL-11 Circular dependency, plus AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1, owner Tomás R.); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.58) is above the needs-rework threshold and the team carries no Critical finding.
