# OKR-Ninja portfolio review — Coppervale, Q1 2027

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed in portfolio mode (Dispatch, Courier, Core Systems, Insights, Accounts; period Q1 2027; strategy source: Company Q1 2027 priorities); 13 findings: 2 Critical, 8 Major, 3 Minor.
The portfolio's biggest threat is AL-11 Circular dependency: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema v3 validation, and Insights waits on Courier's instrumentation, so the telemetry consolidation that C4 relies on cannot start as written.
Dispatch's committed trial-starts KR rests on a partner portal that Accounts lists only as stretch (AL-12 Commitment asymmetry), and the same two teams target an on-time delivery rate defined in two incompatible ways (AL-08 Terminology collision).
Accounts' CSAT baseline of 86 contradicts the Q4 business review's 78 for the same survey and quarter (AL-09 Baseline disagreement).
No goodness anti-pattern is most common: eight distinct anti-patterns appear once each. The most severe is AP-13 Ambiguous Denominator on Dispatch's undefined failure-rate KR.
Recommended first action: Core Systems convenes Courier and Insights to agree one execution order for the SDK GA → instrumentation → schema-validation chain.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 3 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.51; DS2 capped at 1.9 by its Critical anti-pattern) · Core Systems B (2.99) · Courier B (3.32) · Insights B (3.44) · Accounts A (3.53).
- Dispatch: K3=2, K6=2 — DS2.4's failure rate has no population (AP-13); DS1's two KRs pair nothing.
- Core Systems: O1–O4=2 — CS1 is standing duty (AP-10); CS2's churn link is decorative (AL-05).
- Courier: K3=2, K6=2 — referral installs jump 15x with no mechanism (AP-07); CR2 has one KR.
- Insights: K4=3, K7=3 — IN2.2's owner is TBD (AP-15); IN1.3 is an orphan KR (AP-12).
- Accounts: K3=2 — AC2.2's CSAT baseline 86 contradicts the Q4 review's 78 (AL-09).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: The KR never says what is failing (deliveries, jobs or route plans) or over which population, and nothing else on the Dispatch page (lines 17–31) defines it. Any number can be claimed, so the 6% → 3% move can be neither scored honestly nor calibrated.
- Scores affected: K1=1, K3=2, K5=3 (KR DS2.4); the Critical-anti-pattern cap limits DS2's per-OKR score to 1.9
- Suggested rewrite: "KR DS2.4: Failed deliveries — dispatched jobs that end without a completed delivery, as a share of all dispatched jobs, weekly in the ops weekly report — `<baseline>`% → `<target>`% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22)
- Evidence: "Signed pilot customers in DE and FR: 0 → 6" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 23)
- Why it's a problem: The objective joins two end-states with "and" that serve different audiences: satisfaction of existing enterprise dispatchers, and entry into new countries. Each clause gets exactly one KR, so the objective can be half-met, neither KR steers the other, and the "delight" half rests on a single abstraction that readers will interpret differently.
- Scores affected: O1=3, O2=2, K6=2 (DS1)
- Suggested rewrite: "O DS1 (ranked first): Enterprise dispatchers recommend Coppervale dispatch to their peers — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey)." and a separate "O DS3: Coppervale dispatch wins its first customers in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM 'Intl Pilots' view)." (figures from lines 22–23)

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: The objective says the team will keep doing its standing job and names nothing that would differ from today, so normal staffing achieves it (path (a)). Its KRs do contain real deltas (Sev-1 incidents, line 58; cloud cost per completed delivery, line 59), but they do not rescue it, because the objective commits the team to continuing rather than to changing anything.
- Scores affected: O1=1, O2=2, O3=2, O4=2 (CS1)
- Suggested rewrite: "O CS1: Product teams stop losing days to platform incidents — KR: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." with the cost KR moved under an objective that names its change: "O: Every completed delivery costs less to run — KR: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard 'Unit Cost')." (figures from lines 58–59)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: 3,000 → 45,000 is a 15x jump in one quarter, and the Courier page (lines 35–49) names no lever, intermediate milestone or resourcing behind it. The note calling referrals the big swing states a priority, not a mechanism, so the target is decoration rather than a plan. It is also CR2's only KR, which leaves no leading signal to steer by.
- Scores affected: K3=1 (KR CR2.1); K6=0 (CR2, single KR)
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter (App Store + Play attributed installs), driven by `<named referral incentive>`; leading KR CR2.2: active drivers who send at least one referral invite `<baseline>` → `<target>`." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36)
- Evidence: "Crash-free sessions 99.2% → 99.6%" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: A search of the whole Courier page (lines 35–49) found no committed, stretch or aspirational marker. It is the only one of the five team pages without a commitment convention in its header (the other four state one at lines 19, 55, 76 and 93). Its targets range from a 0.4-point crash-free gain to a 15x install jump, so nobody can tell which KRs are must-hits. That undermines moonshot judgments and the planning of the committed Insights KR that waits on Courier (§4 AL-11).
- Scores affected: K3 held at ≤ 3 on all five Courier KRs (anchor 4 requires a commitment label)
- Suggested rewrite: Add "Commitment: KRs are committed unless marked (stretch)." to the Courier page header and mark "KR CR2.1 (stretch): Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)."; CR1.1, CR1.2, CR3.1 and CR3.2 stay unmarked, meaning committed.

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence: "Execs run Monday mornings from our dashboards" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: The KR shares no noun or domain with its objective: it measures a driver-facing app-store rating, while the objective is about executives running their week from Insights dashboards. No causal chain of two steps or fewer links the two, so reaching 4.6 says nothing about whether executives use the dashboards. The driver app is Courier's product (line 35), and no Courier KR mentions the rating.
- Scores affected: K7=2 (IN1)
- Suggested rewrite: "KR IN1.3: Monday leadership ops reviews run from the exec suite: `<baseline>` → `<target>` of the quarter's Monday reviews (Looker usage stats). Owner: Vik M." [proposal — placeholder target]; if the App Store rating is still wanted, it moves to Courier's CR1.

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Owners listed per KR." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: The page assigns an owner to each KR, and a search of lines 74–87 shows this is the only one of Insights' five KRs without a named person. Nobody is accountable for a KR that needs seven more product squads to change how they emit events.
- Scores affected: K4=1 (KR IN2.2)
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)."

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: All four objectives carry the same top label, and the page says outright that it is not choosing, so the set records no trade-off. The page ties portal timing to the billing migration (line 111), yet if the migration runs late nothing says whether migration, portal, onboarding or support work gives way first.
- Scores affected: none (set-level anti-pattern; no rubric dimension scores prioritization)
- Suggested rewrite: "P0: AC4 Billing runs itself (serves C1, the only priority dated to end of Q1, and gates the partner portal). P1: AC1 New customers reach first value in days, not weeks; AC2 Support answers arrive before customers ask twice. P2: AC3 Customers trust the delivery promises we report." (proposal; ranking for Accounts to confirm)

## 4. Alignment findings

Dependency map (consumer → producer): Dispatch → Accounts (partner portal); Courier → Core Systems (SDK v1 GA); Core Systems → Insights (schema v3 validation); Insights → Courier (driver-app event stream). Strategy trace: all 14 objectives cite a company priority, and each of C1–C4 has at least one contributing objective, so no orphan objective or strategy coverage gap was found. Blocking keys used:
- Metric catalog by identity, name and stated baseline: on-time delivery rate, Customer CSAT, driver-app weekly retention, Sev-1 incidents, cloud cost per completed delivery, and the p95 latencies.
- Surface-lever pairs on each shared surface: partner portal, telemetry pipeline and schema, driver app, new-account onboarding, and dashboards.
- Resource fan-in per producer: every producer has one claimant, so there is no contention.

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Core Systems evidence: "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 70)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Insights evidence: "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 87)
- Company evidence: "consolidate our duplicated data and telemetry pipelines" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Company Q1 2027 priorities › line 13)
- Conflict: Courier waits for Core Systems' SDK GA, Core Systems waits for Insights to validate schema v3 in production, and Insights waits for Courier's instrumentation. As written, this three-team loop has no valid execution order, so CR3.1, CS3.1 and IN2.1 are all blocked, and so is the pipeline consolidation that C4 names as its lever.
- Detection check that fired: AL-11 cycle detection on the directed dependency map (edges Courier → Core Systems, Core Systems → Insights, Insights → Courier). Each edge comes from an explicit blocking phrase in the KR text and the team notes.
- Disconfirming checks run:
  - Hard vs. soft edges: all three are hard blocks (once, after, gated on, sequenced behind), not preferences, so the cycle survives.
  - Staged-milestone interleaving: Courier's KR needs GA, not a pre-GA build. Core Systems notes that SDK v1 is code-complete, but no page lets Courier instrument on a pre-GA build, so no valid order exists as written.
  - Awareness plus resolution plan: each team names only its own upstream (notes at lines 49, 70 and 87), and none mentions the loop or a plan, so there is no downgrade.
  - Commitment labels on the Insights → Courier edge: Courier's page states no commitment level (§3 AP-08), so no label mismatch is asserted and the cycle is the root cause.
- Inference labels: analyst inference that the new driver-app event stream Insights waits on is the output of Courier's CR3.1 instrumentation (CR3.1 is the only instrumentation KR on the Courier page, lines 35–49). Every blocking edge itself is quoted.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against its source line)
- Recommended resolution owner: Core Systems lead Adaeze O. convenes Courier (Tomás R.) and Insights (Halima D.) before Q1 execution starts to agree one order. For example: Courier instruments on the code-complete SDK v1 build, Insights validates schema v3 on that stream, then Core Systems GAs. All three teams then restate their KR preconditions to match.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27)
- Dispatch evidence: "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Dispatch evidence: "Commitment: KRs are committed unless marked (stretch)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Accounts evidence: "(stretch — only if the billing migration lands early)" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Accounts evidence: "Portal timing depends on how fast the billing migration goes (see AC3.2)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: Dispatch's DS2.2 is committed, since it is unmarked under its page's convention, and its 0 → 600 trial starts exist only if the partner portal launches. Accounts lists the portal as a stretch that depends on the billing migration landing early. Dispatch's committed number therefore silently assumes the whole of Accounts' stretch item.
- Detection check that fired: AL-12 edge-label comparison on the acknowledged Dispatch → Accounts edge: a committed consumer against a stretch producer, with full-target coupling (no portal means no trial starts).
- Disconfirming checks run:
  - Labeling scheme: both pages use the same convention (lines 19 and 93), so the mismatch is real, not a vocabulary difference.
  - Consumer hedging: Dispatch's note states an assumption with no discount or fallback channel, so nothing hedges the dependence.
  - Unacknowledged dependency: not applicable, because Accounts acknowledges the portal in AC3.2.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against its source line)
- Recommended resolution owner: Dispatch lead Mei L. and Accounts lead Georg B. decide before Q1 execution starts whether the portal is committed. If it stays stretch, Dispatch marks DS2.2 (stretch) or re-bases it on a trial channel it controls.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Dispatch evidence: "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Accounts evidence: "giving those partners the same on-time delivery reporting AC3.1 measures" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Company evidence: "keeping the delivery promises we report to customers" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: Both teams have a committed KR under the same metric name, but the two definitions differ on every axis:
  - numerator: jobs completed vs. deliveries scanned at the destination
  - denominator: all completed jobs vs. all scheduled deliveries including cancellations
  - cadence: weekly vs. monthly
  - system: Ops Console vs. Billing warehouse

  That is why the baselines are 91% and 78% for the same promise. The partner portal will show partners Accounts' version while Dispatch steers by its own, and this is exactly the delivery-promise reporting that C2 ties to enterprise churn.
- Detection check that fired: AL-08 form (a), one metric name used by two teams, with the definitions compared on formula, window, population and data source.
- Disconfirming checks run:
  - Normalization: the definitions do not reduce to one measurement, because cancellations count against Accounts' rate and are absent from Dispatch's. The collision survives.
  - Superseded definition: there is no shared glossary and no newer definition on either page (Dispatch last updated 2027-01-04, Accounts 2027-01-08). The collision survives.
  - Baseline disagreement: the definition split explains the 91% vs. 78% gap, so it is reported here rather than as a separate baseline finding.
  - Metric-identity conflict (same name, same direction, different targets): killed, because the two are lookalike metrics with different definitions.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against its source line)
- Recommended resolution owner: Accounts lead Georg B., whose AC3.1 definition feeds partner-facing reporting, agrees with Dispatch lead Mei L. on one canonical on-time definition, or on two distinct metric names, before the partner portal reports any on-time number. Both KRs are then restated against it.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company (Q4 2026 business review)
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: Accounts and the company's Q4 business review give different Q4 2026 values for the same survey (86 vs. 78). Either AC2.2's committed +4-point target is really a +12-point ask (78 → 90), or the review is wrong. As-of dates: the Accounts page was last updated 2027-01-08 and the Q4 review 2026-12-15.
- Detection check that fired: AL-09 baseline collection in the metric catalog: two stated baselines for Customer CSAT, from the same survey and period, differing by more than rounding.
- Disconfirming checks run:
  - As-of dates: both state the Q4 2026 reading of the same quarterly survey, so different periods do not explain the gap.
  - Definitional split: a search of the Accounts page (lines 91–111) and the review extract (lines 115–120) found no segment, population or scale qualifier on either side.
  - Consistency control: the same review's other baselines match the teams' KRs (driver-app weekly retention 71%, lines 40 and 119; Sev-1 incidents 9, lines 58 and 120), so the gap is specific to CSAT and not a sign of a stale extract.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against its source line)
- Recommended resolution owner: Accounts lead Georg B. reconciles the Q4 2026 CSAT reading with whoever published the Q4 business review (Confluence page 91031) before Q1 execution starts, and restates AC2.2 from the verified baseline.

### [Minor] AL-05 Cascade drift: Core Systems ↔ Company (C2)
- Core Systems evidence: "Ship with confidence" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence: "supports C2 — enterprise churn" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61)
- Core Systems evidence: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 62)
- Core Systems evidence: "Change-failure rate 18% → 8% of production deploys (incident review tags)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 63)
- Core Systems evidence: "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: CS2 claims to support C2, but none of its three KRs measures enterprise logo churn or any of the three drivers C2 names, and no path from release engineering to churn is stated. All three KRs could be hit in a quarter where enterprise churn gets worse, so the link is decorative. It is rated Minor because C2 does not name Core Systems as a contributor.
- Detection check that fired: AL-05 mechanism check on an explicit parent link: the child KRs are delivery-process measures with no stated path to the parent metric.
- Disconfirming checks run:
  - Parent's named contributors: C2's own line names onboarding time-to-value, the escalation backlog and delivery promises, not release engineering, so the finding survives.
  - Child's own justification: Core Systems' notes (line 70) cover only the SDK gate and the cost work, so the finding survives.
  - Linked epics or strategy docs: none are in scope (single-file corpus, no Atlassian connection), so there is nothing further to check.
- Inference labels: none for the finding, which rests on the search stated above. A possible unstated path (fewer failed changes lead to fewer customer-facing incidents and lower churn) is analyst inference, and it is what CS2 would need to state and measure.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against its source line)
- Recommended resolution owner: Core Systems lead Adaeze O. acts before Q1 execution starts: either add a KR that measures the churn-relevant effect (for example, failed changes that reach enterprise accounts, `<baseline>` → `<target>` [proposal — placeholder target]) or drop the C2 link.

## 5. Prioritized action list

1. Break the telemetry dependency loop by agreeing one execution order (for example, instrument on the code-complete SDK v1 build, validate schema v3, then GA) and restating CR3.1, CS3.1 and IN2.1 to match — owner: Core Systems lead Adaeze O. with Courier and Insights (resolves §4 AL-11 Circular dependency).
2. Define the population behind DS2.4's failure rate and restate the KR with an explicit numerator, denominator and cadence — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator).
3. Decide whether the partner portal is committed this quarter and, if it stays stretch, mark DS2.2 (stretch) or re-base it on a channel Dispatch controls — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-12 Commitment asymmetry).
4. Agree one canonical on-time delivery definition, or two distinct names, before the partner portal reports it, and restate DS2.1 and AC3.1 against it — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-08 Terminology collision).
5. Reconcile the Q4 2026 CSAT reading with the Q4 business review and restate AC2.2 from the verified baseline — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Rank Accounts' four P0 objectives so the migration-versus-portal trade-off is decided in advance — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
7. Add a commitment convention to the Courier page and either back CR2.1 with a named lever and a leading KR or mark it aspirational — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled).
8. Rewrite CS1 around a named change, and either give CS2's C2 link a churn-relevant KR or drop the link — owner: Core Systems lead Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR and §4 AL-05 Cascade drift).
9. Replace IN1.3 with a KR that measures executive dashboard use and name an owner for IN2.2 — owner: Insights lead Halima D. (resolves §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR).
10. Split DS1 into two ranked objectives, one for dispatcher satisfaction and one for DE/FR expansion — owner: Dispatch lead Mei L. (resolves §3 AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.51), above the needs-rework threshold, but it has a Critical finding: §3 AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: local file /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: section 'Company Q1 2027 priorities' in the same file (Confluence page 91050, CO-PRIO-Q1FY27); baseline evidence: section 'Appendix — Q4 2026 business review (extracts)' in the same file."
- **Core Systems** (roll-up B (2.99); involved in the Critical §4 AL-11 Circular dependency, which §5 item 1 resolves jointly): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: local file /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: section 'Company Q1 2027 priorities' in the same file (Confluence page 91050, CO-PRIO-Q1FY27); baseline evidence: section 'Appendix — Q4 2026 business review (extracts)' in the same file."
- **Courier** (roll-up B (3.32); involved in the Critical §4 AL-11 Circular dependency, which §5 item 1 resolves jointly): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: local file /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: section 'Company Q1 2027 priorities' in the same file (Confluence page 91050, CO-PRIO-Q1FY27); baseline evidence: section 'Appendix — Q4 2026 business review (extracts)' in the same file."
- **Insights** (roll-up B (3.44); involved in the Critical §4 AL-11 Circular dependency, which §5 item 1 resolves jointly): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: local file /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: section 'Company Q1 2027 priorities' in the same file (Confluence page 91050, CO-PRIO-Q1FY27); baseline evidence: section 'Appendix — Q4 2026 business review (extracts)' in the same file."
- **Accounts** does not qualify: roll-up A (3.53) and no Critical finding.
