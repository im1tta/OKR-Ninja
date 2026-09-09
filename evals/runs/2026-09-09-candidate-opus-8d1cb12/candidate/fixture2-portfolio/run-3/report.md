# Coppervale — Q1 2027 OKR Portfolio Review

Mode: **portfolio** (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027, as stated by the source export. Strategy source: "Company Q1 2027 priorities" (Confluence page 91050, CO-PRIO-Q1FY27). Sole corpus: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.

The portfolio's worst alignment risk is **AL-11 Circular dependency**: Courier's instrumentation waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' schema validation, and Insights' validation waits on Courier's instrumentation — three committed KRs with no valid execution order as written, and the C4 telemetry-consolidation priority sits on all three.

Two teams then publish an identically named "On-time delivery rate" computed from different populations, windows, and systems of record — 91% → 95% versus 78% → 85% (AL-08 Terminology collision) — and Accounts' committed CSAT KR states a Q4 2026 baseline eight points above the Q4 business review's own number (AL-09 Baseline disagreement).

No goodness anti-pattern repeats across teams; the most consequential is **AP-13 Ambiguous Denominator** — Dispatch's undefined "failure rate" is the portfolio's only Critical quality defect, and it caps Objective DS2 at a D.

Quality is otherwise solid: every objective carries an explicit strategy link, every KR but one names a system of record, and C2, C3 and C4 each have a team carrying their headline metric.

Recommended first action: Core Systems convenes Courier and Insights within one week to break the telemetry cycle — until it is broken, three teams' Q1 telemetry KRs are unplannable.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 2 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.49) · Core Systems B (3.10) · Courier B (3.30) · Insights B (3.34) · Accounts B (3.45).

- Dispatch: K6=2, K7=2 — DS2's set carries an undefined failure rate plus an off-objective trial-starts KR.
- Core Systems: O1=2, O2=2, O3=2 — CS1 "Continue running the platform smoothly" is standing duty, not a delta.
- Courier: K3=2 — CR2.1's 15x referral-install target states no mechanism anywhere on the page.
- Insights: K6=2, K7=2 — IN1 carries a driver-app rating KR that moves no dashboard outcome.
- Accounts: K3=2, K6=2 — CSAT baseline is disputed; AC3's portal KR predicts nothing in its set.

## 3. Per-team goodness findings

### Dispatch

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never says what fails or over what population — failed dispatch jobs, failed route builds, failed API calls and failed deliveries would each yield a different number, so any result can be claimed as 3%. The same page proves the team can do better, defining DS2.1 as "jobs completed within the promised window as a share of all completed jobs" (same file › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26); and "ops weekly report" names no dashboard or view, so a second reader cannot reproduce the figure either.
- Scores affected: K1=1, K2=2, K5=2 (triggers the rubric's Critical anti-pattern cap, holding Objective DS2 at 1.9)
- Suggested rewrite: "KR DS2.4: Dispatch job failure rate — jobs that end in a failed state as a share of all jobs dispatched in the week, measured weekly in the Ops Console view `<named view>` — 6% → 3% by end of Q1." (6%, 3% and "by end of Q1" are quoted from the source; the population and named view are OKR-Ninja's proposal) [proposal — placeholder source of record]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." and "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (same file › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › lines 22 and 23)
- Why it's a problem: two and-joined end-states with disjoint audiences — existing enterprise dispatchers' satisfaction, and new-market entry — and the KRs split cleanly into those two unrelated groups, so hitting one half while missing the other still reads as partial success on a single objective nobody can rank. "Delight" is also exactly the kind of abstraction two readers gloss differently.
- Scores affected: O1=3, O2=2, K6=2, K7=3
- Suggested rewrite: split into two ranked objectives, reusing the quoted KRs unchanged — "O DS1 (ranked first): Enterprise dispatchers pick Coppervale over the tool they used last quarter. KR DS1.1: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." and "O DS1b: Coppervale runs live dispatch for paying customers in DE and FR. KR DS1b.1: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)."

### Core Systems

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue" and "smoothly" describe the team's standing job with no delta — the objective is achieved by default staffing and cannot be failed in any way the text makes visible, so it consumes an OKR slot a real change could occupy. It also drags the objective's time-boundedness down: an open-ended duty has no end-of-quarter truth condition.
- Scores affected: O1=2, O2=2, O3=2, K7=2
- Suggested rewrite: "O CS1: Product teams stop losing days to platform incidents. KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Engineer-days lost to platform incidents per quarter `<baseline>` → `<target>` (incident review)." Move "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")" to its own C4 cost objective, and move the standing keep-it-up duty to a health-metric section outside the OKRs. [proposal — placeholder targets]

### Courier

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (same file › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — "our big swing" states enthusiasm, not a mechanism — so the number functions as decoration rather than a goal, and CR2 has no second KR that could steer toward it mid-quarter.
- Scores affected: K3=1, K6=0, K7=2, O4=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter (App Store + Play attributed installs), via `<named referral lever>`. KR CR2.2 (committed, leading): Active drivers sending ≥1 referral invite `<baseline>`% → `<target>`% of weekly active drivers (Amplitude)." [proposal — placeholder targets]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: the Courier page states no commitment convention. Searched every page in the corpus for a labeling scheme — it appears verbatim on four of five team pages: "Commitment: KRs are committed unless marked (stretch)." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19; same file › Core Systems team — Q1 2027 › line 55; same file › Accounts team (billing & customer success) — Q1 2027 › line 93) and "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (same file › Insights team — Q1 2027 › line 76) — and is absent from the Courier block (lines 35–49), whose only note reads "referral growth is our big swing this quarter. SDK timing per Core Systems' plan." (same file › Objective CR3: Every driver action is visible to the teams that need it › line 49).
- Evidence: the unlabeled set spans "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (same file › Objective CR1: Drivers finish every shift without fighting the app › line 39) and "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (same file › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: the set mixes a 0.4-point reliability increment with a 15x growth bet and marks neither, so expected attainment is uncomputable and no reader can tell whether missing the referral number is a failure or a priced-in stretch. It also changes how downstream consumers read Courier's dependencies — Insights and Core Systems both sequence work behind Courier KRs whose commitment level is unstated.
- Scores affected: K3=2 (Courier team dimension), K6=2
- Suggested rewrite: add to the Courier page, matching the four other team pages verbatim — "Commitment: KRs are committed unless marked (stretch)." — and mark CR2.1 "(stretch)", leaving CR1.1, CR1.2, CR3.1 and CR3.2 unmarked.

### Insights

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: there is no causal chain in two steps from an App Store rating to whether executives run Monday mornings from Insights' dashboards — the KR shares no noun, surface or audience with its objective, and it measures a product Insights does not own (Courier's driver app, whose own objective already targets driver experience). Hitting 4.6 would leave IN1 exactly as true or false as before.
- Scores affected: K7=2, K6=3
- Suggested rewrite: move this KR to Courier under "Objective CR1: Drivers finish every shift without fighting the app", and replace it in IN1 with "KR IN1.3: Weekly ops reviews run from the exec suite — weeks in Q1 where the review used the exec dashboards `<baseline>`/13 → 13/13 (Looker usage stats). Owner: Vik M." [proposal — placeholder baseline]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Why it's a problem: "Owner: TBD" leaves the most cross-cutting KR on the page — it requires seven squads outside Insights to change how they emit events — with nobody accountable, on a page that otherwise promises an owner per KR: "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (same file › Insights team — Q1 2027 › line 76). A KR whose owner is unresolved at the start of the quarter is the one that silently slips.
- Scores affected: K4=0, K2=2
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named Insights individual>`." — and name, in the KR text, the nine squads counted in the denominator.

### Accounts

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" · "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" · "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" · "Objective AC4 (Priority: P0): Billing runs itself" (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Accounts team (billing & customer success) — Q1 2027 › lines 95, 99, 103, 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (same file › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: a uniform P0 label across all four objectives encodes no trade-off, and the team says so outright — so when the quarter tightens, the sequencing decision gets made implicitly by whoever is loudest rather than by the plan. It has an immediate cross-team cost: Dispatch's committed DS2.2 depends on the portal that AC3.2 marks stretch, and nothing in a flat P0 list tells Accounts that the portal outranks the billing migration.
- Scores affected: K7=3 (set-level; no single objective is downgraded — the defect is the absent ranking across the set)
- Suggested rewrite: rank the existing objectives without rewording them — "P0: AC1 New customers reach first value in days, not weeks. P1: AC3 Customers trust the delivery promises we report; AC2 Support answers arrive before customers ask twice. P2: AC4 Billing runs itself." — and replace the note with "Ranked; if the quarter tightens, AC4's migration slips before AC1–AC3." (the ranking itself is OKR-Ninja's proposal, to be set by the Accounts lead)

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (same file › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (same file › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier → Core Systems → Insights → Courier closes a cycle in the dependency graph; each team has placed itself behind another, so none can start, and all three KRs serve C4's "consolidate our duplicated data and telemetry pipelines" (same file › Company Q1 2027 priorities › line 13).
- Detection check that fired: graph-structural — cycle detection on the directed dependency map (AL-11 heuristic), built from the "once"/"after" phrases extracted in Step 2.
- Disconfirming checks run: (1) *Cycle ≠ deadlock — hard blocking vs soft preference*: all three edges use hard sequencing wording ("once Core Systems GAs the SDK", "after Insights validates event schema v3 in production", "after Courier instruments the new driver-app event stream"), and no soft-preference hedge (ideally, would benefit from, or similar) appears on any of the three pages — does not kill. (2) *Staged-milestone interleaving*: Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (same file › Objective CS3: One telemetry pipeline every product team trusts › line 70) shows a pre-GA milestone that could in principle let Courier instrument first, but Courier's own KR names GA — not code-complete — as its gate, so the interleaving is not what is written; narrows the claim to no valid execution order as written, does not kill. (3) *Awareness plus a resolution plan*: each team acknowledges exactly one edge ("SDK timing per Core Systems' plan.", same file › Objective CR3: Every driver action is visible to the teams that need it › line 49; "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready.", same file › Objective IN2: Every product event lands in one trusted schema › line 87) and no page names the cycle or a way out — does not kill; no downgrade earned.
- Inference labels: none — all load-bearing text quoted; every edge of the cycle is a verbatim quote from its own team's page.
- Verdict: CONFIRMED (all three edge quotes and both note quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) within one week to cut one edge — the cheapest cut is Courier instrumenting against the code-complete SDK rather than GA, which Core Systems' own note says already exists — and to restate CR3.1, CS3.1 and IN2.1 in the agreed order before any of the three is planned.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (same file › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two incompatible measurements — different populations (completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly) and different systems of record (Ops Console vs. Billing warehouse) — producing a 13-point baseline gap and two committed targets that cannot both describe the same reality. C2 makes this a customer-facing number: "keeping the delivery promises we report to customers" (same file › Company Q1 2027 priorities › line 11); Dispatch meanwhile asserts its own methodology as canonical: "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (same file › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31).
- Detection check that fired: metric-catalog blocking — the same metric name used by two teams (AL-08 form (a)); both definitions pulled and diffed on formula, window, population and data source.
- Disconfirming checks run: (1) *Different wording ≠ different definition*: normalized both definitions before diffing; they differ on all four axes, not merely in phrasing — does not kill. (2) *Superseded definition*: searched all five team pages, the company priorities page and the Q4 2026 business-review appendix for a shared glossary, a canonical formula, or a newer definition either team defers to; the only candidate is Dispatch's own note claiming its methodology, which Accounts' page never references — does not kill. (3) *AL-09 pre-check*: the 91% vs 78% baseline gap is fully explained by the definition split, so per the AL-09 heuristic this is reported as AL-08 with AL-09 Baseline disagreement cross-referenced as the secondary ID, not double-counted as a second finding.
- Inference labels: none — both definitions, both baselines and the company priority are quoted.
- Verdict: CONFIRMED (both definitions re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) to agree one company definition of "On-time delivery rate" before the first customer-facing report of Q1 — or, if both measurements are genuinely needed, rename them (e.g. dispatch on-time completion rate vs. delivered-on-promise rate) [proposal — placeholder names] and restate both KRs against the chosen definitions.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company Q4 review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (same file › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the KR names Q4 2026 as its baseline and the Q4 2026 review of record reports the same instrument eight points lower, so the KR's apparent +4 ask is really a +12 ask. The target is calibrated against a starting point the corpus contradicts, and nothing here is marked stretch — the page states "Commitment: KRs are committed unless marked (stretch)." (same file › Accounts team (billing & customer success) — Q1 2027 › line 93).
- Detection check that fired: metric-catalog collection of every stated baseline per canonical metric — two values for "Customer CSAT" in the same period differing beyond rounding (AL-09 heuristic).
- Disconfirming checks run: (1) *Different as-of dates*: both sides name Q4 2026 explicitly ("Q4 2026 baseline" / "ended Q4 2026") — does not kill. (2) *Different populations or definitions (AL-08)*: both name the same instrument, the "quarterly relationship survey", and no page in the corpus defines a second CSAT population — does not kill; this is a disagreement, not a definition split. (3) *Restatement search*: searched all five team pages, the company priorities page and the appendix for a third CSAT value, a correction, or any note reconciling 86 with 78 — none found, so no explanation exists in the corpus.
- Inference labels: none — both values, both instrument names and both period labels quoted.
- Verdict: CONFIRMED (both statements re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) to reconcile with the Q4 business-review owner and restate AC2.2 against the agreed number in the first two weeks of the quarter, before any mid-quarter check-in scores it.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." and "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › lines 27 and 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (same file › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105) and "Portal timing depends on how fast the billing migration goes (see AC3.2)." (same file › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: DS2.2 is unmarked and therefore committed under its page's own convention, yet its entire 600-trial number rests on a portal Accounts labels stretch and conditions on an unrelated migration landing early. The ambition is coupled too: DS2.2 assumes 600 enterprise trial starts flow through a portal whose owner scopes it at "the first 40 partner accounts" — Dispatch is not merely assuming Accounts' stretch lands, it is assuming a portal an order of magnitude wider in reach than the one Accounts describes.
- Detection check that fired: dependency-map edge label comparison — an acknowledged edge (Dispatch names Accounts as the portal owner) whose two sides carry mismatched commitment labels, plus full-target arithmetic coupling (AL-12 heuristic).
- Disconfirming checks run: (1) *Missing label ≠ mismatch*: both pages state an explicit labeling scheme — "Commitment: KRs are committed unless marked (stretch)." (same file › Dispatch team — Q1 2027 › line 19; same file › Accounts team (billing & customer success) — Q1 2027 › line 93) — so the labels are real and comparable: DS2.2 unmarked, AC3.2 marked stretch — does not kill. (2) *Consumer hedging or discounting*: searched Dispatch's page for any discount, contingency or hedge on the portal assumption; the note is a flat assumption ("DS2.2 assumes the partner portal launch"), with no fallback and no discounted expected value — does not kill. (3) *Producer-side acknowledgment*: Accounts does carry the portal work, so this is an AL-12 and not an AL-01 Unacknowledged dependency.
- Inference labels: none — both commitment labels, both scopes and both notes quoted; the 600-vs-40 comparison uses only quoted numbers.
- Verdict: CONFIRMED (both sides' quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Dispatch lead (Mei L.) with Accounts lead (Georg B.) to decide in week one either to promote AC3.2 to committed with the billing migration resequenced behind it, or to re-cut DS2.2 to a number the 40-account portal scope can actually produce and move the remainder to a stretch KR.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities
- Core Systems evidence: "Ship with confidence" — tagged "*(supports C2 — enterprise churn)*" — with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log).", "Change-failure rate 18% → 8% of production deploys (incident review tags)." and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (`.../fixture2-portfolio/input/sample-portfolio-2.md` › Objective CS2: Ship with confidence › lines 61, 62, 63, 64)
- Company priorities evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (same file › Company Q1 2027 priorities › line 11)
- Conflict: CS2 claims C2 explicitly, but none of its three KRs measures logo churn or any of the three drivers C2's own page names — the parent enumerates its mechanisms and Core Systems' internal delivery metrics are not among them. All three KRs could be fully hit in a quarter where enterprise churn worsens, the tell for a decorative link; meanwhile every driver C2 does name is already carried by Accounts (AC1, AC2, AC3), so the trace adds no coverage.
- Detection check that fired: strategy-trace mechanism check — an explicit parent link whose child KRs measure neither the parent's metric nor a documented driver of it (AL-05 heuristic).
- Disconfirming checks run: (1) *Activity KRs ≠ decorative link — check the parent's page for named contributing workstreams*: C2 names exactly three drivers, and deploy frequency, change-failure rate and CI duration are none of them — does not kill; it strengthens the finding, because the parent was specific rather than silent. (2) *Stated driver relationship elsewhere in the corpus*: searched all five team pages, the company priorities page and the Q4 2026 appendix for any text linking delivery throughput, deploy frequency or CI time to enterprise churn or retention; Core Systems' only note is about telemetry and cost — "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." (same file › Objective CS3: One telemetry pipeline every product team trusts › line 70) — none found. (3) *Better-fitting parent*: CS2's KRs would trace soundly to C4's lean-operations pillar, which is why this is a misrouted trace rather than an orphan objective.
- Inference labels: none — the parent's driver list and all three child KRs are quoted; OKR-Ninja asserts no causal mechanism of its own, only the absence of one in the corpus.
- Verdict: CONFIRMED (parent priority and all three child KRs re-verified character-for-character against the source file). Severity note: AL-05's default here is Minor (C2 does not name Core Systems as a contributor), escalated one level to Major under the taxonomy's escalation rule because CS2's KRs are explicitly committed — "Commitment: KRs are committed unless marked (stretch)." (same file › Core Systems team — Q1 2027 › line 55).
- Recommended resolution owner: Core Systems lead (Adaeze O.) to either re-anchor CS2 to C4 in the next OKR revision, or add one KR measuring a C2-named driver Core Systems can actually move, agreed with the Accounts lead who owns all three named drivers today.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to cut one edge of the telemetry cycle — starting with instrumenting against the code-complete SDK — owner: Core Systems lead Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Define DS2.4's denominator and system of record, and split DS1 into two ranked objectives — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator, AP-11 Objective as Kitchen Sink).
3. Agree one company definition of "On-time delivery rate", or rename the two measurements and restate both baselines — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-08 Terminology collision).
4. Decide whether the partner portal is committed or DS2.2 is re-cut to the portal's real 40-account scope — owner: Dispatch lead Mei L. with Accounts lead Georg B. (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Q1 CSAT baseline against the Q4 2026 business review and restate AC2.2 — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4, or add a KR measuring one of C2's three named churn drivers — owner: Core Systems lead Adaeze O. (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 and publish what slips first if the quarter tightens — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Replace CS1 with a delta objective and move the standing platform duty to a health-metric section — owner: Core Systems lead Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR).
9. Add the missing commitment convention to the Courier page and re-cut CR2.1 into an aspirational target plus a committed leading KR — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot, AP-08 Committed vs Aspirational Not Labeled).
10. Move the App Store rating KR to Courier and name an accountable individual for IN2.2 — owner: Insights lead Halima D. (resolves §3 AP-12 Orphan KR, AP-15 Ownerless KR).

## 6. Suggested single-team re-runs

Routing is governed by the rubric's roll-up grade and by Critical findings, never by heatmap cells. No team's roll-up grade falls at or below the needs-rework threshold (D); four teams qualify on criterion (b), a Critical finding.

- **Dispatch** (roll-up C (2.49); Critical AP-13 Ambiguous Denominator on KR DS2.4, which holds Objective DS2 at D (1.9)): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91112 (DSP-OKR-Q1), section 'Dispatch team — Q1 2027' of the portfolio export at `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Courier** (roll-up B (3.30); party to Critical AL-11 Circular dependency via KR CR3.1, plus AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier team's (driver app) Q1 2027 OKRs alone, in depth. Source: Confluence page 91116 (COUR-OKR-Q1), section 'Courier team (driver app) — Q1 2027' of the portfolio export at `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Core Systems** (roll-up B (3.10); party to Critical AL-11 Circular dependency via KR CS3.1, plus AP-10 BAU Dressed as OKR and AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91120 (CORE-OKR-Q1), section 'Core Systems team — Q1 2027' of the portfolio export at `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."
- **Insights** (roll-up B (3.34); party to Critical AL-11 Circular dependency via KR IN2.1, plus AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91124 (INS-OKR-Q1), section 'Insights team — Q1 2027' of the portfolio export at `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy doc: 'Company Q1 2027 priorities', Confluence page 91050 (CO-PRIO-Q1FY27), in the same file."

**Accounts** does not qualify: roll-up B (3.45), above the needs-rework threshold, and no Critical finding — its Major issues (AP-05 Everything Is a P0, and its side of AL-08, AL-09 and AL-12) are all handled by the §5 actions without a full re-run.
