# Coppervale Q1 2027 OKR portfolio review

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed (Dispatch, Courier, Core Systems, Insights, Accounts; Q1 2027, strategy source: Company Q1 2027 priorities); 2 Critical, 9 Major, 2 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency. Courier waits for Core Systems to GA the SDK. Core Systems waits for Insights to validate schema v3. Insights waits for Courier to instrument the driver app. No valid order exists for the three committed telemetry KRs behind C4.
No goodness anti-pattern recurs (8 goodness findings, 8 distinct IDs). The most serious is AP-13 Ambiguous Denominator on Dispatch's failure-rate KR, which cannot be honestly scored.
Dispatch has a committed partner-portal trial KR, but Accounts lists the portal as stretch (AL-12 Commitment asymmetry). The two teams also report different numbers under the same on-time delivery rate name (AL-08 Terminology collision).
Recommended first action: the Core Systems, Courier and Insights leads agree a staged SDK and schema sequence that breaks the cycle in the first weeks of the quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.47) · Core Systems B (3.03) · Courier B (3.23) · Insights B (3.36) · Accounts A (3.53).
- Dispatch: K6=2 — DS1's NPS and pilot KRs measure separate halves, no indicator pairing.
- Core Systems: O1=2 — CS1 continues standing operations, naming no change (AP-10 BAU Dressed as OKR).
- Courier: K3=2 — CR2.1's 15x referral-install target has no mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1.3's driver-app rating is unrelated to exec dashboards (AP-12 Orphan KR).
- Accounts: O3=3 — Q1 period inherited from the page title, not restated; nothing below 3.

## 3. Per-team goodness findings

### Dispatch

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: the KR never says what is failing (dispatched jobs, completed deliveries, route plans or app sessions) or across which population, so 6% and 3% can be claimed from any base. A search of the Dispatch page (lines 17–31) finds the word failure only in this KR, with no definition anywhere on the page. This Critical finding caps DS2's per-OKR score at 1.9.
- Scores affected: K1=1, K2=2
- Suggested rewrite: "KR DS2.4: Failed dispatch jobs — jobs dispatched that end without a completed delivery, as a share of all jobs dispatched, weekly from the ops weekly report — `<baseline>`% → `<target>`% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: the objective joins two end-states with "and", and they concern different audiences: how satisfied existing enterprise dispatchers are, and entry into new regions. Each KR measures only one clause, so the objective states no single outcome and its KRs do not pair.
- Scores affected: O2=2, K6=2
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers would recommend Coppervale dispatch to a peer — KR DS1.1: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey). Objective DS3: Coppervale wins its first customers in DE and FR — KR DS3.1: Signed pilot customers in DE and FR: 0 → 6 (CRM view)." [proposal — numbers reused from the source]

### Core Systems

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence: "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 58)
- Evidence: "Cloud cost per completed delivery $0.42 → $0.30" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 59)
- Why it's a problem: the objective says the team will keep doing its standing job and names no change from today, so it fires under path (a). The two real improvements in its KRs do not rescue it, because the objective commits the team to continuing, not changing. It is also an open-ended effort squeezed into one quarter.
- Scores affected: O1=1, O2=2, O3=2
- Suggested rewrite: "Objective CS1: Product teams stop losing days to Sev-1 incidents this quarter — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." and "Objective CS4: Every completed delivery costs less to run — KR CS4.1: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard)." [proposal — numbers reused from the source]

### Courier

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: going from 3,000 to 45,000 is a 15x target. The Courier page (lines 35–49: objective CR2, its only KR, and the notes) names no mechanism, milestone or resourcing for it. The notes state an intent, not a method, and the KR is not labeled aspirational. C3's cohort finding explains why referrals matter, not how installs could grow fifteenfold in one quarter.
- Scores affected: K3=1
- Suggested rewrite: "KR CR2.1 (stretch): Driver referral installs 3,000 → `<target>` this quarter (App Store + Play attributed installs), driven by `<named referral lever>`; KR CR2.2: Drivers sending ≥1 referral invite per week `<baseline>` → `<target>` (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36)
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: Courier's is the only team page with no commitment convention. Dispatch, Core Systems, Insights and Accounts each have a commitment line under their page header, but a search of Courier's lines 35–49 for the terms committed, stretch and aspirational finds none. Courier's targets range from a 0.4-point reliability gain to a 15x install goal, so nobody can tell what attainment to expect or judge which targets are sandbags or moonshots. This finding is about the whole set and is separate from the AP-07 finding on CR2.1.
- Scores affected: K3=3 (CR1.1, CR1.2 — stretch unlabeled)
- Suggested rewrite: "Commitment: KRs are committed unless marked (stretch). … KR CR2.1 (stretch): Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." [proposal — numbers reused from the source]

### Insights

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence: "Execs run Monday mornings from our dashboards" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: the driver app's public store rating has nothing in common with executives running Monday reviews from Insights dashboards, and no short causal chain links the two. Reaching 4.6 would not move the objective, and the driver app belongs to the Courier team.
- Scores affected: K7=2 (IN1)
- Suggested rewrite: "KR IN1.3: Weekly leadership ops reviews run from the exec suite `<baseline>` → `<target>` of `<n>` reviews (Looker usage stats). Owner: Vik M." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Owners listed per KR." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page's own convention gives every KR an owner, and every other Insights KR (lines 79, 80, 81, 84) names one. IN2.2's owner is TBD. This is the only KR that needs nine other squads to act, and nobody is accountable for it.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)." [proposal]

### Accounts

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: all four objectives are P0, and the page says outright that the team is not choosing, so the set shows no trade-off. The billing migration already gates AC3.2's portal, and if it slips, nothing on the page says what gives way. The defect belongs to the whole set, not to any one objective.
- Scores affected: none directly (set-level trade-off defect; no rubric dimension scores ranking)
- Suggested rewrite: "P0: AC1 New customers reach first value in days, not weeks; AC4 Billing runs itself (its migration gates AC3.2). P1: AC2 Support answers arrive before customers ask twice. P2: AC3 Customers trust the delivery promises we report." [proposal — ranking for the Accounts owner to confirm]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Courier evidence: "SDK timing per Core Systems' plan." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Core Systems evidence: "GA is gated on schema v3 validation (Insights)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 70)
- Insights evidence: "after Courier instruments the new driver-app event stream" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Insights evidence: "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 87)
- Conflict: Courier instruments only after Core Systems GAs SDK v1. Core Systems GAs only after Insights validates schema v3. Insights validates only after Courier instruments the new driver-app event stream. Each team is waiting on another, so CR3.1, CS3.1 and IN2.1 cannot start as written, and C4's pipeline consolidation stalls with them.
- Detection check that fired: graph-structural cycle detection on the dependency map (AL-11 heuristic). The cycle's edges are Courier → Core Systems (line 46), Core Systems → Insights (line 67) and Insights → Courier (line 84).
- Disconfirming checks run:
  - Hard vs. soft wording: all three edges use hard blocking terms ("once", "after", "gated on", "sequenced behind"), not preferences.
  - Staged-milestone interleaving: Courier waits for GA, not a beta. The code-complete SDK ("SDK v1 is code-complete", line 70) is never offered to Courier before GA, and Insights names no other event source. No workable order can be quoted.
  - Awareness plus resolution plan: each team notes what it is waiting on, but none has a plan to break the cycle.
  - Commitment: Core Systems and Insights KRs are committed by page convention ("Commitment: KRs are committed unless marked (stretch)." at lines 55 and 76). Courier's page states no convention, so its edge is unlabeled rather than soft.
  - Result: not killed.
- Inference labels: that the "new driver-app event stream" Insights waits on is the instrumentation Courier plans in CR3.1 is analyst inference. It is supported by CR3.1 being the only instrumentation work on Courier's page (lines 35–49).
- Verdict: CONFIRMED (all six quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) to agree a staged order. For example, Insights validates schema v3 against events from `<n>` driver flows instrumented on the code-complete pre-GA SDK, and Core Systems then GAs it, by `<week 2 of Q1>` [proposal — placeholder target].

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27)
- Dispatch evidence: "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Dispatch evidence: "Commitment: KRs are committed unless marked (stretch)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Accounts evidence: "(stretch — only if the billing migration lands early)" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Accounts evidence: "Portal timing depends on how fast the billing migration goes (see AC3.2)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: Dispatch's DS2.2 is unmarked, so its page convention makes it committed. Its 600 trial starts assume a portal launch that Accounts lists as stretch and only if the billing migration lands early. Accounts' portal also targets 40 partner accounts for delivery reporting, not enterprise trial starts, so even a full Accounts hit may not be the launch Dispatch is counting on.
- Detection check that fired: edge label comparison on an acknowledged dependency (AL-12 heuristic). AC3.2 acknowledges the Dispatch → Accounts edge at line 31, so AL-01 was not flagged, and the two sides carry different labels (committed vs. stretch).
- Disconfirming checks run:
  - Labeling scheme: both pages state the same convention (lines 19 and 93), so the mismatch is real, not a difference in vocabulary.
  - Consumer hedging: Dispatch's note states the assumption with no discount or fallback.
  - Producer acknowledgment: AC3.2 acknowledges a portal but scopes it to partner accounts. That does not remove the label mismatch.
  - Result: not killed.
- Inference labels: that AC3.2's partner portal is the same portal launch DS2.2 counts on is analyst inference, supported by Dispatch's note naming Accounts as the portal owner.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Dispatch lead (Mei L.) and Accounts lead (Georg B.) decide before the billing migration's first checkpoint at `<date>`. Either Accounts commits the portal, with a scope that covers enterprise trials, or DS2.2 is marked (stretch) and re-based on a channel that does not need the portal [proposal — placeholder target].

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Dispatch evidence: "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Accounts evidence: "giving those partners the same on-time delivery reporting AC3.1 measures" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Company evidence: "keeping the delivery promises we report to customers" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: one metric name has two definitions. Dispatch divides by completed jobs, weekly, from the Ops Console. Accounts divides by all scheduled deliveries including cancellations, monthly, from the Billing warehouse. The company therefore has two on-time delivery rates (baselines 91% and 78%) for the same customer promise that C2 names, and Accounts is about to share its version with partners.
- Detection check that fired: the same metric name is used by two teams, and their definitions were compared on formula, window, population and data source (AL-08 form (a) heuristic).
- Disconfirming checks run:
  - Normalization: the definitions differ on denominator (completed jobs vs. scheduled deliveries including cancellations), window (weekly vs. monthly) and source (Ops Console vs. Billing warehouse), so they are not the same measurement.
  - Superseded definition: both are current Q1 2027 pages (last updated 2027-01-04 and 2027-01-08), and neither references a shared glossary.
  - Baseline gap: the definition split explains the 91% vs. 78% difference, so it is reported here rather than as a separate baseline finding.
  - Duplication: the different populations are a legitimate split of work, so no duplicated-objective finding stands.
  - Severity: Minor by default, raised to Major because both KRs are committed and the metric feeds C2's customer-facing promise.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the source file)
- Recommended resolution owner: C2 owner (Noor E.) has Dispatch (Mei L.) and Accounts (Georg B.) agree one definition of on-time delivery rate, or rename one of the two metrics, before AC3.2's partner reporting ships.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: Accounts gives the Q4 2026 result of the same survey as 86, while the company's Q4 review gives 78. AC2.2's committed four-point target may really be a twelve-point ask, set against the wrong starting value.
- Detection check that fired: metric-catalog baseline comparison. Two baselines are stated for the metric Customer CSAT for the same period (Q4 2026), and they differ by more than rounding (AL-09 heuristic).
- Disconfirming checks run:
  - As-of dates: both statements label the value Q4 2026 (review page last updated 2026-12-15, Accounts page 2027-01-08). Nothing in the file mentions a later re-cut of the survey.
  - Definitional split: both name the same quarterly relationship survey, and no other CSAT definition, population or segment appears in the file, so a terminology collision does not explain the gap.
  - Result: not killed.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) reconciles AC2.2's baseline with the owner of the Q4 business review, then restates the KR from the confirmed Q4 value before the first monthly check-in.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company (C2)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Core Systems evidence: "Ship with confidence" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence: "supports C2 — enterprise churn" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 62)
- Core Systems evidence: "Change-failure rate 18% → 8% of production deploys (incident review tags)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 63)
- Core Systems evidence: "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 64)
- Conflict: CS2 claims to support enterprise churn, but none of its three KRs measures churn or any of the three drivers C2 names. Deploy frequency, change-failure rate and CI time could all hit target in a quarter where enterprise churn gets worse, so the link is decorative.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic). The child KRs measure neither the parent's metric, a documented driver of it, nor a deliverable the parent names.
- Disconfirming checks run:
  - Parent's named contributors: C2 names onboarding time-to-value, the escalation backlog and delivery promises. None of these is deployment or CI work.
  - Child's own justification: Core Systems' notes (line 70) discuss only the SDK and cost work and state no link to churn.
  - Linked epics: none available (local file only, no Atlassian connection).
  - Result: not killed.
  - Severity: Minor by default, because C2 does not name Core Systems as a contributor. Raised to Major because CS2's KRs are committed under the page convention.
- Inference labels: none. All load-bearing text is quoted. Any path from change-failure rate to churn would be analyst inference, so none was assumed.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) and the C2 owner (Noor E.), before the first monthly OKR check-in. Either re-link CS2 to the priority its KRs actually serve, or add a KR that measures one of C2's named drivers.

## 5. Prioritized action list

1. Convene Courier and Insights to agree a staged SDK and schema v3 sequence that breaks the telemetry deadlock — owner: Core Systems lead Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Define the population and the failure event behind DS2.4's failure rate, then re-baseline it — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator).
3. Decide together whether Accounts commits the partner portal or Dispatch marks DS2.2 as stretch — owner: Dispatch lead Mei L. with Accounts lead Georg B. (resolves §4 AL-12 Commitment asymmetry).
4. Agree one definition of on-time delivery rate, or rename one metric, before partner reporting ships — owner: C2 owner Noor E. (resolves §4 AL-08 Terminology collision).
5. Reconcile AC2.2's CSAT baseline with the Q4 business review and restate the target — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Rewrite CS1 so it names a change, and either re-link CS2 or give it a KR that measures one of C2's named drivers — owner: Core Systems lead Adaeze O. (resolves §4 AL-05 Cascade drift and §3 AP-10 BAU Dressed as OKR).
7. Adopt the portfolio's commitment convention, and give CR2.1 a stated mechanism and a stretch label — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled).
8. Name an owner for IN2.2 and replace IN1.3 with a KR that measures exec dashboard use — owner: Insights lead Halima D. (resolves §3 AP-15 Ownerless KR and §3 AP-12 Orphan KR).
9. Rank Accounts' four objectives so the page says what gives way if the billing migration slips — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
10. Split DS1 into two objectives, one for dispatcher satisfaction and one for the new regions — owner: Dispatch lead Mei L. (resolves §3 AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.47), above the needs-rework threshold; Critical AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' in the same file (Confluence page 91050)."
- **Courier** (roll-up B (3.23), above the needs-rework threshold; Critical AL-11 Circular dependency): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' in the same file (Confluence page 91050)."
- **Core Systems** (roll-up B (3.03), above the needs-rework threshold; Critical AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' in the same file (Confluence page 91050)."
- **Insights** (roll-up B (3.36), above the needs-rework threshold; Critical AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' in the same file (Confluence page 91050)."
- Accounts does not qualify (roll-up A (3.53), no Critical finding).
