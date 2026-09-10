# Coppervale — Q1 2027 Portfolio OKR Review

Mode: **portfolio** (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027 (as stated by the source document). Strategy source: the "Company Q1 2027 priorities" section (C1–C4) of the same file. Sole source of OKR content: `input.md`.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 10 Major, 3 Minor findings.
The portfolio's biggest threat is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' schema validation, and Insights' validation waits on Courier's instrumentation — a three-team cycle with no valid execution order as written, which stalls the telemetry half of priority C4.
The most common quality issue is **AP-12 Orphan KR** (2 of 5 teams: Insights parks a driver-app App Store rating under a dashboards objective; Accounts parks the partner portal under a delivery-promises objective).
The one Critical goodness defect is **AP-13 Ambiguous Denominator** on Dispatch DS2.4, whose "failure rate" names no population and therefore cannot be honestly scored.
Two teams also report the same metric name, "On-time delivery rate", under incompatible definitions that both feed the company's C2 promise-keeping claim (AL-08 Terminology collision), and Accounts' CSAT baseline contradicts the Q4 business review by 8 points (AL-09 Baseline disagreement).
Recommended first action: convene Courier + Core Systems + Insights to break the telemetry cycle before mid-quarter, using Core Systems' own "code-complete" SDK state as the entry point.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.54) · Core Systems B (3.06) · Courier B (3.24) · Insights B (3.42) · Accounts B (3.47).

- Dispatch: K7=2 — DS2 pairs an undefined failure-rate KR with an off-objective trial-start KR.
- Core Systems: O1=2 — CS1 and CS2 name the team's own activity, not a changed end-state.
- Courier: K3=2 — CR2.1's 15x referral target carries no mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1 carries an orphan App Store rating KR (AP-12 Orphan KR).
- Accounts: K3=2 — AC2.2's calibration is unverifiable; its stated baseline contradicts the Q4 review.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch (supports C1) › line 29)
- Evidence (contrast, same objective): "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch (supports C1) › line 26)
- Why it's a problem: "the failure rate" names no population — failed jobs, failed deliveries, failed route plans and failed portal trials are all plausible readings in this objective, and each yields a different number, so any result can be claimed. Its sibling KR DS2.1 shows the team can specify a denominator, which makes the omission a defect rather than a convention.
- Scores affected: K1=1, K2=2, K3=2, K5=2; per-OKR DS2 capped at 1.9 (D) by the Critical-anti-pattern cap
- Suggested rewrite: "KR DS2.4: Job failure rate — jobs ending in a failed state as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target; the 6% and 3% figures are quoted from the existing KR, the population and system of record are the proposal]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (`input.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions (supports C1) › line 21)
- Evidence (the KRs split along the "and"): "Enterprise dispatcher NPS 24 → 40" and "Signed pilot customers in DE and FR: 0 → 6" (`input.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions (supports C1) › lines 22–23)
- Why it's a problem: two and-joined outcome clauses with disjoint audiences (existing enterprise dispatchers vs. prospects in new geographies), and the KRs cluster into two unrelated groups of one — neither KR gives evidence about the other half, so the objective can be half-achieved and reported as done.
- Scores affected: O1=3, O2=2, O4=3, K7=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers would be angry if Coppervale were taken away — KR: Enterprise dispatcher NPS 24 → 40. Objective DS3: Coppervale is a credible dispatch choice in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6." (Both targets quoted from the existing KRs; the split into two ranked objectives is OKR-Ninja's proposal.)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver (supports C3) › line 43)
- Evidence (the only accompanying "how" on the page): "Notes: referral growth is our big swing this quarter. SDK timing per Core Systems' plan." (`input.md` › Objective CR3: Every driver action is visible to the teams that need it (supports C4) › line 49)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — "our big swing" states intent, not mechanism — so the KR functions as decoration rather than a goal, and it is the sole KR under its objective. Searched for a mechanism: the Courier section (lines 35–49) in full, including both notes lines; nothing beyond the quoted sentence.
- Scores affected: K3=1, K6=0, K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs), via the in-app referral bonus; leading KR CR2.2 (committed): drivers who send ≥1 referral invite `<baseline>` → `<target>` monthly (Amplitude)." [proposal — placeholder target; the 3,000/45,000 figures are quoted from the existing KR]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (absent on Courier's page): "Commitment: KRs are committed unless marked (stretch)." — present at lines 19 (Dispatch), 55 (Core Systems), 76 (Insights) and 93 (Accounts), and absent from the Courier section (`input.md` › Dispatch team — Q1 2027 › line 19)
- Evidence (the stretch spread this leaves unlabeled): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." vs "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md` › Objective CR1: Drivers finish every shift without fighting the app (supports C3) › line 39; and › Objective CR2: Every driver in the region hears about Coppervale from another driver (supports C3) › line 43)
- Why it's a problem: Courier is the only team of five without a commitment convention, while its targets range from a 0.4-point reliability increment to a 15x referral swing. Expected attainment cannot be computed, and downstream teams (Insights depends on Courier's instrumentation) cannot tell which Courier KR is a must-hit. Searched for labels: the whole Courier section, lines 35–49, for "committed", "aspirational", "stretch" and "P0" — no hit.
- Scores affected: K3=3 on CR1.2 (a stretch justified by the C3 cascade but unlabelled, so the K3=4 anchor cannot be met)
- Suggested rewrite: add the portfolio convention to the page header — "*Commitment: KRs are committed unless marked (stretch).*" (quoted from the four peer team pages) — and mark CR2.1 "(stretch)".

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (`input.md` › Objective CS1: Continue running the platform smoothly for every team (supports C4) › line 57)
- Why it's a problem: "Continue" plus "smoothly" describes the team's standing job with no stated delta — the objective is satisfied by default staffing and two readers would not agree on what "smoothly" means, so it occupies an objective slot that a real change could have used. (Its KRs do carry genuine deltas — "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." at line 58 — which is exactly what the objective should have been framed around.)
- Scores affected: O1=2, O2=2, O3=2
- Suggested rewrite: "Objective CS1: No team loses a day to a platform incident or an unexplained cloud bill — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard 'Unit Cost')." (Both KRs quoted unchanged from lines 58–59; only the objective text is OKR-Ninja's proposal.)

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`input.md` › Objective IN1: Execs run Monday mornings from our dashboards (supports C4) › line 81)
- Evidence (its stated objective): "Objective IN1: Execs run Monday mornings from our dashboards" (`input.md` › Objective IN1: Execs run Monday mornings from our dashboards (supports C4) › line 78)
- Why it's a problem: there is no causal chain in two steps or fewer from the driver app's public App Store rating to executives using Looker dashboards on Monday morning; the KR shares no noun or domain with its objective, and the levers that move it sit in the driver app, not in Insights' dashboards. Achieving it would tell nobody whether IN1 happened. Searched Courier's OKRs for a counterpart App Store rating KR (lines 35–49): none; nearest is "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (line 39), which is a different metric with a different system of record.
- Scores affected: K7=2 on the IN1 set, K6=3
- Suggested rewrite: move the rating to Courier's CR1 set and replace it with a dashboards-outcome KR — "KR IN1.3: Exec-suite dashboards answering a leadership question without an analyst ticket `<baseline>` → `<target>` per month (Looker usage stats + Jira analyst queue)." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`input.md` › Objective IN2: Every product event lands in one trusted schema (supports C4) › line 85)
- Evidence (the page's own convention it breaks): "Owners listed per KR." (`input.md` › Insights team — Q1 2027 › line 76)
- Why it's a problem: no accountable individual is attached, on a page whose own header promises one per KR — and this is the KR that requires nine other squads to change their event conventions, the cross-team coordination most likely to stall without a named driver. Searched for an owner: the Insights section (lines 74–87) and the page header; the only owner statements are "Owner: Halima D." (lines 79, 84) and "Owner: Vik M." (lines 80–81).
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)." (Metric, baseline, target and source quoted unchanged from line 85.)

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0)", "Objective AC2 (Priority: P0)", "Objective AC3 (Priority: P0)", "Objective AC4 (Priority: P0)" (`input.md` › Accounts team (billing & customer success) — Q1 2027 › lines 95, 99, 103, 107)
- Evidence (the team says so itself): "every one of these is P0 for us this quarter — we're not choosing." (`input.md` › Objective AC4 (Priority: P0): Billing runs itself (supports C1) › line 111)
- Why it's a problem: a uniform P0 label across all four objectives encodes no trade-off, so the set gives no guidance when onboarding, escalations, delivery reporting and the billing migration collide — and they will, because the same team's own note already makes the partner portal contingent on the billing migration ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111). Downstream, Dispatch is committed against that same contingent item (see §4 AL-12).
- Scores affected: none directly — AP-05 is a set-level prioritization defect with no per-objective or per-KR dimension in the rubric; it is reported on its own evidence and is why §5 cannot simply defer to Accounts' own ordering.
- Suggested rewrite: "P0: AC1 (onboarding time-to-value) — the driver the company page names first for C2. P1: AC2, AC4. P2: AC3, whose partner-portal KR is already contingent." (Ranking is OKR-Ninja's proposal; objective texts unchanged.)

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report (supports C2) › line 105)
- Evidence (its stated objective): "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report (supports C2) › line 103)
- Why it's a problem: partner accounts going live on a portal has no two-step causal path to customers trusting reported delivery promises, and shares no noun with the objective; the portal's actual consumer is Dispatch's trial-start KR under C1 ("600 enterprise trial starts via the partner portal launch", line 27), not C2's promise-keeping. Parked here, the KR is invisible to the team that depends on it and its stretch label is easy to miss — which is exactly what happened (see §4 AL-12).
- Scores affected: K7=2 on the AC3 set, K2=3
- Suggested rewrite: move the KR under AC4 (Billing runs itself, supports C1) as "KR AC4.3 (stretch — only if the billing migration lands early): Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)", and leave AC3 with a second promise-keeping KR — "KR AC3.2: Delivery-promise disputes raised by enterprise customers `<baseline>` → `<target>` monthly (Zendesk)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`input.md` › Objective CR3: Every driver action is visible to the teams that need it (supports C4) › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`input.md` › Objective CS3: One telemetry pipeline every product team trusts (supports C4) › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`input.md` › Objective IN2: Every product event lands in one trusted schema (supports C4) › line 84)
- Conflict: Courier → Core Systems → Insights → Courier is a closed cycle in the dependency graph — each team's KR is first in line behind another's, so no execution order exists as written and all three C4 telemetry KRs (CR3.1, CS3.1, IN2.1) can end the quarter at zero without anyone having been late.
- Detection check that fired: graph-structural cycle detection on the dependency map, built from the "once …", "after …" blocking phrases in the three KRs (AL-11 heuristic).
- Disconfirming checks run: (1) *Cycle ≠ deadlock — hard blocking vs. soft preference*: all three edges re-read; each uses a hard gate ("once Core Systems GAs the SDK", "after Insights validates event schema v3 in production", "after Courier instruments the new driver-app event stream"), none uses soft wording — the cycle survives. (2) *Staged-milestone interleaving*: Core Systems' notes state "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) — a pre-GA SDK exists that could break the cycle, but Courier's KR gates on **GA**, not on code-complete, so no interleaving is available on the text as written; this weakens nothing in the finding but supplies the resolution below. (3) *Awareness plus a resolution plan*: each team's notes acknowledge its own single edge — "SDK timing per Core Systems' plan." (line 49) and "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (line 87) — but no page mentions the cycle or a plan to break it, so no downgrade applies.
- Inference labels: none — all three edges are quoted verbatim; no edge is inferred.
- Verdict: CONFIRMED (all three edge quotes and both notes re-verified character-for-character)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) within the first two weeks of Q1 to re-gate one edge — the cheapest is Courier instrumenting against the code-complete SDK build rather than GA, letting Insights validate schema v3, then Core Systems GA; whichever edge is chosen, amend that KR's text so the gate is written down.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch (supports C1) › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report (supports C2) › line 104)
- Company evidence (why it matters above the two teams): "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input.md` › Company Q1 2027 priorities › line 11)
- Conflict: one metric name, two incompatible measurements — different populations (completed jobs vs. all scheduled deliveries *including cancellations*), different events (completion vs. destination scan), different windows (weekly vs. monthly) and different systems of record (Ops Console vs. Billing warehouse). Both feed C2's "delivery promises we report to customers", so an exec rollup will show 95% and 85% for "on-time delivery" in the same quarter with no way to reconcile them, and neither team can be held to the other's number.
- Detection check that fired: metric-catalog blocking on metric name used by ≥2 teams, then diffing each side's stated formula, window, population and data source (AL-08 form (a) heuristic).
- Disconfirming checks run: (1) *Different wording ≠ different definition*: both definitions normalized (numerator event, denominator population, window, source) — they differ on all four axes, so the finding survives. (2) *Superseded definition*: searched all "on-time" and "promise" occurrences in the corpus (lines 11, 26, 31, 103, 104); the only other mention is Dispatch's own note "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31), which asserts Dispatch's methodology rather than a shared or newer one — no shared glossary exists, so no definition is superseded. (3) *Cross-reference / division of labor*: neither team's page references the other's on-time metric; Dispatch's note is a self-reference. (4) *AL-09 Baseline disagreement considered and rejected as the root cause*: the 91% vs. 78% baseline gap is fully explained by the definitional split (a denominator that includes cancellations and all scheduled deliveries must read lower), so per AL-09's disconfirming check this is reported as AL-08, cross-referencing AL-09.
- Inference labels: the direction of the definitional effect on the baselines (broader denominator ⇒ lower rate) is analyst inference; the definitions, baselines and targets are all quoted.
- Verdict: CONFIRMED (both definitions, both baselines and the company priority re-verified character-for-character)
- Recommended resolution owner: the C2 owner (Noor E., CEO, as owner of the company priorities page) rules on one canonical "On-time delivery rate" definition and system of record before the first monthly business review; the loser of the ruling renames its metric (e.g. Dispatch's becomes "Dispatch on-time completion rate") so both can coexist without colliding in the rollup.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`input.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice (supports C2 — escalation backlog) › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`input.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, the same named instrument ("quarterly relationship survey") and the same period (Q4 2026) carry two different values — 86 on the OKR page, 78 in the business review. If 78 is right, Accounts' committed KR is a 12-point ask presented as a 4-point one, and its attainment will be scored against a starting point that the company's own review contradicts.
- Detection check that fired: metric-catalog baseline collection — two stated baselines for one canonical metric in the same period differing beyond rounding (AL-09 heuristic).
- Disconfirming checks run: (1) *Different as-of dates*: both sides explicitly say Q4 2026 — no date explanation. (2) *Different populations (AL-08 explanation)*: both cite the same "quarterly relationship survey"; the review adds a sample size ("n = 412") but no different population or segment, and no other CSAT definition exists in the corpus (searched every "CSAT", "satisfact" and "NPS" occurrence: lines 22, 101, 118 — line 22 is a different metric, dispatcher NPS) — no definitional explanation found. (3) *Rounding*: an 8-point gap on a 0–100 scale is far beyond rounding.
- Inference labels: none — both values, both instrument names and both periods are quoted; which figure is correct is not asserted here.
- Verdict: CONFIRMED (both statements re-verified character-for-character)
- Recommended resolution owner: Accounts lead (Georg B.) with the Q4 review's owner reconciles the two figures in week 1 and restates AC2.2 against the surviving number — if 78 stands, the KR reads "Customer CSAT 78 → `<target>` (quarterly relationship survey, n ≥ 412)" and its ambition must be re-agreed [proposal — placeholder target].

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." and, on the same page, "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch (supports C1) › lines 27 and 31)
- Dispatch evidence (its commitment convention, which makes DS2.2 committed): "Commitment: KRs are committed unless marked (stretch)." (`input.md` › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report (supports C2) › line 105)
- Conflict: Dispatch's committed 600 trial starts ride entirely on a deliverable Accounts has explicitly labelled stretch and conditional on a separate migration. The arithmetic is worse than the labels: even at 100% of its stretch target Accounts' portal reaches only "the first 40 partner accounts", against which Dispatch has booked 600 enterprise trial starts. Dispatch's note asserts Accounts "owns the portal build this quarter" without registering either the stretch label or the condition.
- Detection check that fired: dependency-map edge label comparison on an acknowledged (non-AL-01) edge — committed consumer vs. stretch producer, plus full-target arithmetic coupling (AL-12 heuristic).
- Disconfirming checks run: (1) *Missing label ≠ mismatch*: both teams have explicit labelling schemes (lines 19 and 93, identical wording) and Accounts marks AC3.2 "(stretch)" explicitly, so the mismatch is real and not a vocabulary artefact. (2) *Consumer already discounts or hedges the producer*: Dispatch's only statement about the dependency is the assumption at line 31, which asserts ownership rather than hedging, and no discount appears in the 600 figure — no hedging found, so no downgrade. (3) *Producer's condition already met*: Accounts' own note ties the portal to the migration — "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111) — and its migration KR is itself at "38% → 100%" (line 109), so the condition is open, not satisfied. Cross-reference: §3 AP-12 Orphan KR — Accounts (the portal KR is also parked under the wrong objective, which is part of why its stretch label went unnoticed).
- Inference labels: none — both commitment levels, both targets and the assumption are quoted; the 600-vs-40 gap is arithmetic on quoted numbers.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character)
- Recommended resolution owner: Dispatch lead (Mei L.) and Accounts lead (Georg B.) agree in week 1 either to promote the portal to a committed Accounts KR with a date, or to relabel DS2.2 as stretch and re-baseline Dispatch's committed trial-start number against channels Dispatch controls.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*", with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log).", "Change-failure rate 18% → 8% of production deploys (incident review tags)." and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (`input.md` › Objective CS2: Ship with confidence (supports C2 — enterprise churn) › lines 61–64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input.md` › Company Q1 2027 priorities › line 11)
- Conflict: the parent names its three drivers explicitly — onboarding time-to-value, the escalation backlog, delivery promises — and none of CS2's three KRs measures any of them, nor churn itself. All three are internal engineering-velocity metrics; Core Systems could hit 8 deploys/week, an 8% change-failure rate and a 15-minute CI pipeline in a quarter where enterprise logo churn rises, which is the signature of a decorative link.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent names as needed? All three answers are no (AL-05 heuristic).
- Disconfirming checks run: (1) *Activity KRs ≠ decorative link — mechanism documented elsewhere*: searched the whole corpus for a stated relationship between deploy/CI metrics and churn — every "churn", "retention", "time-to-value" and "escalation" occurrence (lines 11, 12, 40, 61, 95, 96, 99, 100, 119); the only hit inside the Core Systems section is the claim itself at line 61. Core Systems' own notes name a different parent for its other work — "The cost work is our C4 commitment." (line 70) — and say nothing about churn. No mechanism found, so the finding survives. (2) *Parent names this child as a contributor*: the company page names three drivers and no team; Core Systems is not among them. (3) *Severity*: the parent does not name this child as a contributor, so the AL-05 default is Minor; escalated one level to Major because CS2's KRs are explicitly committed under the page's own convention — "Commitment: KRs are committed unless marked (stretch)." (line 55) — which is the taxonomy's stated escalation condition.
- Inference labels: the claim that velocity metrics can improve while churn worsens is analyst inference; the parent's named drivers and the child's KRs are quoted.
- Verdict: CONFIRMED (the objective, its three KRs, the company priority and the commitment line all re-verified character-for-character)
- Recommended resolution owner: Core Systems lead (Adaeze O.) with the C2 owner re-parents CS2 to C4 (where reliability and unit cost already live) or adds one KR that measures a driver C2 actually names — e.g. "Enterprise escalations caused by production change `<baseline>` → `<target>` per quarter (incident review tags)" [proposal — placeholder target].

### [Minor] AL-05 Cascade drift: Courier ↔ Company priority C3
- Courier evidence: "Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)*", with its single KR "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver (supports C3) › lines 42–43)
- Company evidence: "**C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80% across FY27." (`input.md` › Company Q1 2027 priorities › line 12)
- Conflict: C3's only metric is weekly retention of drivers already using the app; CR2's only KR counts new installs. Referral installs are an acquisition measure with no stated path to retention, and a 15x install influx of new drivers can dilute a weekly-retention cohort — so CR2 could be fully achieved in a quarter where C3's metric falls.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link — the child's sole KR measures neither the parent's metric nor a driver the parent names (AL-05 heuristic).
- Disconfirming checks run: (1) *Mechanism documented elsewhere*: searched Courier's section and the company page for a stated referral→retention relationship; Courier's note says only "referral growth is our big swing this quarter." (line 49) — intent, not mechanism — and C3 names no acquisition driver. (2) *Sibling coverage kills the finding?* No: the same team's CR1.2 does cascade C3 correctly — "Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3)." (line 40) — which is why this finding is scoped to CR2 alone and rated Minor: C3 is not left uncovered, it is merely also claimed by an objective that cannot move it. (3) *Severity*: the parent does not name Courier's referral work as a contributor and Courier applies no commitment labels at all (see §3 AP-08), so no escalation condition is met — Minor stands.
- Inference labels: the new-driver dilution mechanism is analyst inference; the objective, its KR and the company priority are quoted.
- Verdict: CONFIRMED (all quotes re-verified character-for-character)
- Recommended resolution owner: Courier lead (Tomás R.) either re-parents CR2 to C1 (growth) or adds a retention-linked KR to CR2 — e.g. "Referred drivers still active in week 4 `<baseline>` → `<target>`% (Amplitude cohort)" [proposal — placeholder target].

## 5. Prioritized action list

1. Convene Courier + Core Systems + Insights to break the telemetry cycle by re-gating one edge — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-11 Circular dependency).
2. Rewrite Dispatch DS2.4 with an explicit denominator and system of record — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Rule on one canonical "On-time delivery rate" definition and rename the other before the first monthly business review — owner: C2 owner (Noor E., CEO) (resolves §4 AL-08 Terminology collision).
4. Reconcile the Q4 2026 CSAT figure and re-baseline AC2.2 against the surviving number — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
5. Settle the partner portal's commitment level and move the KR to the objective it actually serves — owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) (resolves §4 AL-12 Commitment asymmetry and §3 AP-12 Orphan KR — Accounts).
6. Re-parent CS2 to C4 or add a KR measuring a driver C2 names — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-05 Cascade drift: Core Systems ↔ C2).
7. Rank the four Accounts objectives P0/P1/P2 so the quarter encodes a trade-off — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Split CR2.1 into a labelled aspirational referral target plus a committed leading KR with a named lever — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot).
9. Name an owner for IN2.2 and move the App Store rating KR out of IN1 to Courier — owner: Insights lead (Halima D.) (resolves §3 AP-15 Ownerless KR and §3 AP-12 Orphan KR — Insights).
10. Reframe CS1 around the delta its own KRs already commit to — owner: Core Systems lead (Adaeze O.) (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.54); qualifies on criterion (b) — Critical finding §3 AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Dispatch team — Q1 2027' (lines 17–31); strategy doc: the 'Company Q1 2027 priorities' section (C1–C4, lines 7–13) of the same file."
- **Courier** (roll-up B (3.24); qualifies on criterion (b) — Critical finding §4 AL-11 Circular dependency): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Courier team (driver app) — Q1 2027' (lines 35–49); strategy doc: the 'Company Q1 2027 priorities' section (C1–C4, lines 7–13) of the same file."
- **Core Systems** (roll-up B (3.06); qualifies on criterion (b) — Critical finding §4 AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Core Systems team — Q1 2027' (lines 53–70); strategy doc: the 'Company Q1 2027 priorities' section (C1–C4, lines 7–13) of the same file."
- **Insights** (roll-up B (3.42); qualifies on criterion (b) — Critical finding §4 AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Insights team — Q1 2027' (lines 74–87); strategy doc: the 'Company Q1 2027 priorities' section (C1–C4, lines 7–13) of the same file."

Accounts does not qualify: its roll-up grade is B (3.47), above the rubric's needs-rework threshold, and it carries no Critical finding. Note that a single-team re-run cannot itself resolve AL-11 — one team in scope produces no AL-XX findings — so the three telemetry teams' re-runs are for depth on their own KRs, while the cycle is resolved by action §5.1.
