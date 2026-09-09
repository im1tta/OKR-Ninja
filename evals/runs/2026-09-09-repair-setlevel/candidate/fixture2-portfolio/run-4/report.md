# Coppervale — Q1 2027 OKR portfolio review

**Scope:** 5 teams (Dispatch, Courier, Core Systems, Insights, Accounts) · Period: Q1 2027 · Mode: portfolio.
**Sources:** local export `sample-portfolio-2.md` (absolute path: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md`); strategy source: its "Company Q1 2027 priorities" section (C1–C4). All source refs below use `sample-portfolio-2.md › <nearest heading> › line N` against that file.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The portfolio's single worst alignment risk is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' schema validation, and Insights' validation waits on Courier's instrumentation — a three-team cycle with no valid execution order as written, and the whole C4 telemetry-consolidation programme sits inside it.
No goodness anti-pattern repeats across teams — the eight goodness findings land on eight distinct AP-IDs — so the most consequential is **AP-13 Ambiguous Denominator** (Dispatch), the only Critical goodness finding: a committed KR moves an undefined "failure rate" from 6% to 3%.
Two teams also disagree with each other and with the company's own record about what the numbers mean: "On-time delivery rate" carries two incompatible definitions 13 points apart (AL-08), and Accounts' CSAT baseline of 86 contradicts the Q4 review's 78 (AL-09).
Accounts has the cleanest KR craft in the portfolio (A, 3.50) yet carries three of the four Major alignment findings — the defects there are cross-team, not local.
Recommended first action: Core Systems convenes Courier and Insights in week 1 to break the telemetry cycle by naming which artefact ships first.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.59) · Core Systems B (3.00) · Courier B (3.23) · Insights B (3.34) · Accounts A (3.50).

- Dispatch: K7=2 — DS2 mixes an undefined failure-rate KR with an acquisition KR (AP-13 Ambiguous Denominator).
- Core Systems: O1=2 — CS1 states the standing job, not a delta (AP-10 BAU Dressed as OKR).
- Courier: K3=2 — the referral KR is a 15x jump with no mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1 carries an App Store rating KR unrelated to exec dashboards (AP-12 Orphan KR).
- Accounts: K3=2 — CSAT ambition unjudgeable while the baseline is contradicted by the Q4 review (AL-09).

## 3. Per-team goodness findings

### Dispatch

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: the KR never says failure rate *of what* — completed jobs, scheduled deliveries, route-plan builds, or portal trial starts — so the population can be chosen after the fact and neither the 6% baseline nor the 3% target can be audited. The same objective's other rate KR pins its population down ("as a share of all completed jobs", line 26), so the omission is not a page-wide convention that a reader could resolve.
- Scores affected: K1=1, K2=2, K5=2 (Critical anti-pattern cap applies: per-OKR score for DS2 capped at 1.9)
- Suggested rewrite: "KR DS2.4: Failed delivery jobs — jobs closed with a failure disposition as a share of all completed jobs, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal; the 6% and 3% figures are quoted from line 29, the population and system of record are placeholders for Dispatch to confirm]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — existing enterprise dispatchers versus two new markets — sit under one objective, and its KRs split cleanly into the two unrelated groups: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (line 22) and "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (line 23). No trade-off between satisfaction work and expansion work can be settled against this objective, because both are "the" objective.
- Scores affected: O2=2, K6=3, K7=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers get through their day without leaving Coppervale. Objective DS3: Coppervale is a real option for logistics operators in DE and FR." — with DS1.1 staying under DS1 and DS1.2 moving to DS3. [proposal]

### Core Systems

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue" plus the team's standing duty states no change in the world; the objective is satisfied by default staffing, so it cannot fail, and it occupies an objective slot that a real platform bet would otherwise hold. Its own KRs do carry deltas ("Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4.", line 58), which makes the BAU framing purely a loss of focus — the objective under-describes what the team is actually committing to.
- Scores affected: O1=1, O2=2, O3=2
- Suggested rewrite: "Objective CS1: Product teams stop losing days to platform incidents and platform cost stops scaling with volume." — keeping CS1.1 and CS1.2 unchanged as its KRs. [proposal]

### Courier

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter" (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: the target is a 15x jump on a single quarter, and the only accompanying "how" anywhere on the page calls it a "big swing" — no named lever, no intermediate milestone, no resourcing signal, and no aspirational label. A number this size with no mechanism behind it functions as decoration: it will neither steer the quarter nor be believed at review time. (Searched the whole Courier section, lines 35–49, for a stated lever, incentive, budget, or milestone behind the referral number; the notes line above is the only candidate.)
- Scores affected: K3=1, K6=0 (CR2 is a single-KR set), K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter (App Store + Play attributed installs), via the in-app referral bonus; leading KR CR2.2 (committed): drivers who send ≥1 referral invite `<baseline>` → `<target>` weekly (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36) — the set's entire header; no commitment convention anywhere on it.
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) alongside "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 0.4-point reliability improvement and a 15x growth bet carry identical implied weight, so expected attainment for the team cannot be computed and neither sandbagging nor moonshotting can be judged from the page. Three of the five team pages state a convention verbatim — "Commitment: KRs are committed unless marked (stretch)." (lines 19, 55, 93) — and Courier's does not, so this is a gap against Coppervale's own house standard, not a portfolio-wide omission. (Search performed: all of lines 35–49 for "committed", "aspirational", "stretch", "P0", "priority", "confidence" — no hits.)
- Scores affected: K3 across the Courier set (K3=1 on CR2.1 versus K3=3–4 elsewhere; Courier K3 team dimension = 2)
- Suggested rewrite: add to the Courier page header, "Commitment: KRs are committed unless marked (stretch)." and mark CR2.1 "(stretch)". [proposal]

### Insights

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: hitting this KR would not move the objective it sits under — "Execs run Monday mornings from our dashboards" (line 78). There is no causal chain in two steps from a public app-store rating to leadership dashboard usage, and the KR shares no noun or surface with the objective; the metric belongs to the driver-app experience that Courier owns ("Drivers finish every shift without fighting the app", line 38). Insights can hit both of its real IN1 KRs and still fail this one for reasons entirely outside its control.
- Scores affected: K7=2
- Suggested rewrite: move the App Store rating to Courier's CR1 set, and replace it with "KR IN1.3: Exec-suite dashboards opened before 10:00 on Mondays `<baseline>` → `<target>` per week (Looker usage stats). Owner: Vik M." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76) — the page's own convention, which removes any team-level fallback.
- Why it's a problem: the one KR that requires moving seven other squads is the one KR with no accountable individual, on a page that names an owner for every other KR — so "TBD" reads as unassigned rather than inherited. Cross-squad onboarding fails silently without a person who owns the calendar for it. (Search performed: the whole Insights section, lines 74–87, for any owner attached to IN2.2 — the page states owners per KR and IN2.2's is "TBD"; no other section names an owner for v3 onboarding.)
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)." [proposal]

### Accounts

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0)" (line 95), "Objective AC2 (Priority: P0)" (line 99), "Objective AC3 (Priority: P0)" (line 103), "Objective AC4 (Priority: P0)" (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry the identical top label and the page says outright that no choice was made, so the set encodes no trade-off — when the billing migration slips, nothing in the OKRs tells the team which of onboarding, escalations, delivery reporting, or billing gives way. The team is simultaneously the sole owner of all three of C2's named churn drivers and of the partner portal that Dispatch's committed KR depends on (see §4 AL-12), so this is exactly the team that most needs a stated rank.
- Scores affected: none — AP-05 is scoped to the objective set as a whole; no O or K dimension in the rubric measures cross-objective prioritisation, which is why the defect is invisible in Accounts' A (3.50) roll-up.
- Suggested rewrite: "P0: AC1 (onboarding time-to-value) and AC2 (escalation backlog) — the two C2 drivers with no second owner. P1: AC4 (billing). P2: AC3, with AC3.2 (partner portal) either promoted to committed for Dispatch or explicitly deferred." [proposal]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier waits on Core Systems, Core Systems waits on Insights, Insights waits on Courier. Each of the three KRs is first in line behind another, so no execution order satisfies the text as written and all three KRs — plus the C4 telemetry-consolidation priority they serve — fail together.
- Detection check that fired: AL-11 structural cycle detection on the dependency map (edges built from the blocking phrases in each KR: Courier’s "once Core Systems GAs the SDK", Core Systems’ "after Insights validates event schema v3 in production", Insights’ "after Courier instruments the new driver-app event stream"), yielding the 3-cycle Courier → Core Systems → Insights → Courier.
- Disconfirming checks run: (1) hard-blocking vs soft-preference re-read of every edge — all three phrases quoted above state a hard precondition; none of the three sections contains a softening word (searched lines 45–49, 66–70 and 83–87 for "ideally", "prefer", "benefit", "if possible"), so no edge is soft. (2) Staged-milestone interleaving — Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) shows a pre-GA build exists, which *could* let Courier instrument before GA; but Courier's KR conditions explicitly on GA and no page authorises instrumenting or validating against a pre-GA SDK, so no interleaving is quotable — the check weakens the cycle's inevitability without breaking it, and the resolution it hints at is exactly what the teams must now agree. (3) Awareness-plus-resolution-plan — Courier's "SDK timing per Core Systems' plan." (line 49) and Insights' "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (line 87) show each team sees its own edge, but neither states a plan that breaks the cycle, so no downgrade to Minor.
- Inference labels: none — all three edges are quoted verbatim from their owners' pages; the pre-GA interleaving discussed above is labelled as a possibility, not as an established plan.
- Verdict: CONFIRMED (all three edge quotes re-verified character-for-character against lines 46, 67 and 84)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) in week 1 to name the artefact that ships first — most plausibly instrumenting one driver flow against the code-complete pre-GA SDK to unblock schema validation — and to restate CR3.1, CS3.1 and IN2.1 with that order written into their text.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name carries two different measurements — different success event (job completed vs scanned at destination), different population (all completed jobs vs all scheduled deliveries including cancellations), different cadence (weekly vs monthly) and different system of record (Ops Console vs Billing warehouse) — producing a 13-point baseline gap. Both feed the same company promise, "keeping the delivery promises we report to customers" (line 11), so any exec rollup or customer-facing figure silently depends on which team's number is used.
- Detection check that fired: AL-08 form (a), same metric name used by two teams; each team's stated definition was located and diffed field by field (numerator event, denominator population, window, data source).
- Disconfirming checks run: (1) Normalise-before-diff — the two definitions do not reduce to the same measurement: Accounts' denominator includes cancellations and requires a destination scan, Dispatch's is restricted to completed jobs, so the populations differ by construction, not wording. (2) Superseded-definition check — both pages are current for Q1 2027 (Dispatch "Last updated 2027-01-04", line 18; Accounts "Last updated 2027-01-08", line 92) and neither cites a shared glossary; Dispatch instead asserts its own methodology, "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31). (3) AL-09 pre-check — the 91% vs 78% baseline gap is fully explained by the definitional split, so per the AL-09 heuristic this is reported as AL-08, not as a baseline disagreement.
- Inference labels: none — both definitions are quoted in full from their own pages.
- Verdict: CONFIRMED (both definition quotes re-verified character-for-character against lines 26 and 104)
- Recommended resolution owner: Insights (Halima D.) as owner of shared reporting convenes Dispatch and Accounts to publish one canonical on-time-delivery definition, and to re-baseline DS2.1 and AC3.1 against it, before the first monthly C2 report of the quarter.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), acknowledged in "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31), under the page rule "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" marked "(stretch — only if the billing migration lands early)" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), reinforced by "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111)
- Conflict: Dispatch carries a committed number that is wholly contingent on a deliverable its producer labels stretch and conditions on a *different* project landing early. Dispatch's KR has no fallback and no discount; if the billing migration runs to plan rather than early, DS2.2 fails for reasons entirely outside Dispatch's control.
- Detection check that fired: AL-12 label comparison on an acknowledged dependency edge — the edge was excluded from AL-01 because both sides name the portal, then each side's commitment wording was compared (Dispatch: committed by page default and unmarked; Accounts: explicitly "(stretch — only if the billing migration lands early)").
- Disconfirming checks run: (1) Labelling-scheme check — Dispatch states its convention verbatim on line 19 and DS2.2 carries no "(stretch)" marker, so the KR is committed under the team's own scheme rather than by our assumption. (2) Consumer-hedging check — searched the Dispatch section (lines 17–31) for a discount, fallback, or conditional on the portal; the note on line 31 acknowledges the dependency but hedges nothing, so no downgrade. (3) AL-01 pre-check — Accounts does carry a portal KR, so the dependency is acknowledged and this is not an unacknowledged dependency.
- Inference labels: the observation that 600 trial starts must come through the 40 partner accounts Accounts plans to bring live is **analyst inference** — the two KRs use different units and no document states the relationship. The commitment-label mismatch itself is fully quoted and inferred from nothing.
- Verdict: CONFIRMED (both commitment labels and both notes re-verified character-for-character against lines 19, 27, 31, 105 and 111)
- Recommended resolution owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) in week 1 — either promote AC3.2 to committed with the migration risk carried elsewhere, or re-cut DS2.2 to the trial volume the stretch case actually supports and label the remainder aspirational.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities (C2)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Core Systems evidence: "Ship with confidence" claiming "(supports C2 — enterprise churn)" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Conflict: the parent link is asserted but decorative. None of the three KRs measures churn or any of the three drivers C2 names for itself; all three are internal delivery-pipeline metrics that could be hit in full during a quarter in which enterprise churn worsens, and C2's actual drivers are all owned by Accounts (AC1, AC2, AC3). Core Systems is credited against a company priority it has no measured path to.
- Detection check that fired: AL-05 mechanism check on an explicit parent link in the strategy trace — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's own page names as needed? All three answers are no.
- Disconfirming checks run: (1) Parent-page named-contributor check — C2 names its own drivers verbatim ("onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers"); deployment velocity, change-failure rate and CI time appear nowhere among them. (2) Child-page stated-mechanism check — Core Systems' notes offer no churn mechanism: "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." (line 70). (3) Corpus-wide driver search — searched every section and the Q4 appendix for "churn": only two hits exist, line 11 and the CS2 heading itself, so no document anywhere states that shipping cadence drives enterprise retention.
- Inference labels: none — the parent link is quoted from the child's own heading and the finding rests on quoted absence, not on an inferred link. (No causal path from deploy frequency to churn is asserted or denied here; the defect is that neither side states one.)
- Verdict: CONFIRMED (parent and all three child KR quotes re-verified character-for-character against lines 11, 61–64)
- Recommended resolution owner: Core Systems lead (Adaeze O.) with the C2 owner — either re-anchor CS2 to C4 (where CS1.2's cost KR already lands), or add a KR that measures a C2 driver Core Systems can actually move (for example incident-driven escalations opened against Accounts' backlog), before mid-quarter review.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Business-review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same instrument and the same period produce two starting values eight points apart. Read against the team's number, AC2.2 is a +4 improvement; read against the reviewed actual, it is a +12 ask — a committed KR whose ambition, staffing and probability of success all change depending on which page is right.
- Detection check that fired: AL-09 — the metric catalog collected every stated baseline per canonical metric; "Customer CSAT" carries two baselines for the same metric and the same period differing far beyond rounding.
- Disconfirming checks run: (1) As-of-date check — both cite Q4 2026 explicitly ("Q4 2026 baseline" / "ended Q4 2026"), so a timing explanation is unavailable. (2) Same-instrument check — both name "quarterly relationship survey", so the gap is not two different surveys. (3) AL-08 definitional-split pre-check — searched all five team sections, the company priorities and the appendix for any second CSAT definition, population, segment or formula; the file contains exactly two CSAT mentions (lines 101 and 118) and neither defines a population, so no definitional explanation exists to reclassify this as a terminology collision.
- Inference labels: none — both baselines are quoted with their as-of periods.
- Verdict: CONFIRMED (both baseline quotes re-verified character-for-character against lines 101 and 118)
- Recommended resolution owner: Accounts lead (Georg B.) with the Q4 business-review owner — reconcile the Q4 CSAT figure and restate AC2.2 against the agreed baseline in week 2, before the quarter's target is socialised.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to name which telemetry artefact ships first and rewrite CR3.1, CS3.1 and IN2.1 with that order in their text — owner: Core Systems lead, Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Define the population behind Dispatch's failure-rate KR and restate DS2.4 with its denominator and system of record — owner: Dispatch lead, Mei L. (resolves §3 AP-13 Ambiguous Denominator).
3. Publish one canonical "On-time delivery rate" definition and re-baseline DS2.1 and AC3.1 against it before the first monthly C2 report — owner: Insights lead, Halima D. (resolves §4 AL-08 Terminology collision).
4. Decide whether the partner portal is committed or stretch, and re-cut whichever of AC3.2 or DS2.2 loses that argument — owner: Accounts lead, Georg B., with Dispatch lead, Mei L. (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Q4 2026 CSAT baseline against the business review and restate AC2.2 — owner: Accounts lead, Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring a C2 driver Core Systems can move — owner: Core Systems lead, Adaeze O. (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives and publish the trade-off the team says it is not making — owner: Accounts lead, Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Attach a named lever and an aspirational label to the referral target, and add a leading referral KR beneath it — owner: Courier lead, Tomás R. (resolves §3 AP-07 Unmoored Moonshot).
9. Name an individual owner for IN2.2 and move the App Store rating KR out of IN1 to Courier — owner: Insights lead, Halima D. (resolves §3 AP-15 Ownerless KR and §3 AP-12 Orphan KR).
10. Restate CS1 as a delta rather than the standing job, add Courier's missing commitment convention, and split Dispatch's DS1 into two ranked objectives — owners: Core Systems lead Adaeze O., Courier lead Tomás R., Dispatch lead Mei L. (resolves §3 AP-10 BAU Dressed as OKR, §3 AP-08 Committed vs Aspirational Not Labeled, §3 AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.59); qualifies on Critical finding AP-13 Ambiguous Denominator, plus AP-11 Objective as Kitchen Sink and inbound AL-08 / AL-12): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: local export sample-portfolio-2.md, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.23); qualifies on Critical finding AL-11 Circular dependency, plus AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: local export sample-portfolio-2.md, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.00); qualifies on Critical finding AL-11 Circular dependency, plus AP-10 BAU Dressed as OKR and AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: local export sample-portfolio-2.md, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.34); qualifies on Critical finding AL-11 Circular dependency, plus AP-12 Orphan KR and AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: local export sample-portfolio-2.md, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.50), above the needs-rework threshold, and no Critical finding — its four Major findings (AP-05, AL-08, AL-12, AL-09) are all resolvable through §5 without a deeper single-team pass.
