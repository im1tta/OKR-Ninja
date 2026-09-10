# Coppervale Q1 2027 — Portfolio OKR Review

Mode: portfolio (5 teams). Period: Q1 2027. Source: `input.md` (company priorities page, five team pages, Q4 2026 business-review appendix). Strategy source in scope: "Company Q1 2027 priorities" (C1–C4).

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 10 Major, 2 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — three workstreams with no valid execution order as written.
The most common quality issue is AP-12 Orphan KR (Insights and Accounts each carry a KR that would not move its stated objective).
Dispatch is the weakest set: KR DS2.4 measures an undefined "failure rate", which caps its objective at D and blocks honest scoring.
Dispatch and Accounts both target "On-time delivery rate" while meaning different populations, sources, and cadences (AL-08 Terminology collision), against a company priority that promises customers exactly that number.
Dispatch's committed 600 trial starts depend on a portal Accounts lists only as a stretch item (AL-12 Commitment asymmetry).
Recommended first action: convene Courier, Core Systems and Insights to break the telemetry cycle by naming one starting milestone before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.48) · Core Systems B (2.93) · Accounts B (3.20) · Courier B (3.21) · Insights B (3.25).

- Dispatch: K7=2 — DS2 mixes trial-start acquisition into a daily-usage objective; DS2.4 undefined.
- Core Systems: O1=2 — CS1 restates the standing job; CS2 is a delivery verb, not an outcome.
- Accounts: K6=2 — AC3 pairs a lagging rate with an unrelated portal milestone, no leading indicator.
- Courier: K3=2 — the 15x referral target has no mechanism, milestone, or resourcing signal.
- Insights: K7=2 — an App Store rating KR sits under a dashboards objective it cannot move.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" names no population — failed job assignments, failed route builds, failed deliveries and failed API calls would each yield a different number, so the KR can be declared hit against whichever base looks best and can never be honestly scored. The sibling KR on the same page defines its base explicitly ("as a share of all completed jobs", line 26), so the omission is not this page's convention.
- Scores affected: K1=1, K5=2; per Roll-Up cap 2 (confirmed Critical anti-pattern) objective DS2 is capped at 1.90 (D), which drives the team to C (2.48).
- Suggested rewrite: "KR DS2.4: Failed job assignments as a share of all jobs dispatched, measured weekly in the Ops Console: 6% → 3% by end of Q1." (Proposal; the 6% and 3% figures are reused verbatim from line 29, the denominator and source of record are OKR-Ninja's.)

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`input.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — dispatcher satisfaction and geographic expansion — and the KRs split cleanly along that seam ("Enterprise dispatcher NPS 24 → 40", line 22; "Signed pilot customers in DE and FR: 0 → 6", line 23), so neither half can fail visibly on its own. "Delight" is also an abstraction two readers would gloss differently.
- Scores affected: O2=2, O4=2, K7=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers would fight to keep Coppervale — KR: Enterprise dispatcher NPS 24 → 40. Objective DS1b (ranked second): Coppervale runs live dispatch in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6." (Proposal; both KR figures reused verbatim from lines 22–23.)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 15x target with no lever, intermediate milestone, or resourcing signal anywhere on the page — the only "how" offered is "referral growth is our big swing this quarter" (line 49), which names no mechanism. Searched: Courier's objective text, all five Courier KRs (lines 39–47) and the team's notes line. As the sole KR under CR2 it also leaves the objective with no steering signal mid-quarter.
- Scores affected: K3=1, K6=0, K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral bonus (App Store + Play attributed installs). KR CR2.2 (committed, leading): Share of weekly active drivers who send at least one referral `<baseline>` → `<target>`, monthly." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: Courier's page header carries only "*Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06*" (`input.md` › Courier team (driver app) — Q1 2027 › line 36), while every other team's page states "Commitment: KRs are committed unless marked (stretch)." (same file › Dispatch team — Q1 2027 › line 19; repeated at lines 55, 76, 93)
- Why it's a problem: searched the whole Courier section (lines 35–49) for "commit", "stretch", "aspiration", "P0" and "must-hit" — no marker of any kind. Courier's targets vary wildly in stretch, from "Crash-free sessions 99.2% → 99.6%" (line 39) to the 15x referral target (line 43), so expected attainment cannot be computed and the moonshot above cannot be read as honest ambition rather than a coming miss. It also leaves Courier's edge of the AL-11 cycle (§4) with no commitment level.
- Scores affected: K3=2 (team dimension); set-level defect, no single per-KR score
- Suggested rewrite: Add to the Courier page header: "Commitment: KRs are committed unless marked (stretch)." — then label CR2.1 "(stretch)" and leave CR1.1, CR1.2, CR3.1 and CR3.2 unmarked as committed. (Proposal; the convention line is reused verbatim from line 19.)

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (`input.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue" plus "running the platform smoothly" describes the team's standing job with no delta — it is achieved by default staffing and displaces a real goal — and "smoothly" is an abstraction two readers would gloss differently. Its two KRs do carry genuine deltas, which is why the fix is to reframe the objective rather than delete the set.
- Scores affected: O1=1, O2=2, O3=2, K7=2
- Suggested rewrite: "Objective CS1: Product teams stop losing days to platform incidents — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." Move KR CS1.2 (cloud cost per completed delivery) under a separate objective, "Every delivery costs less to run than it did last quarter", since unit cost is not a reliability outcome. (Proposal; CS1.1 reused verbatim from line 58.)

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`input.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: there is no causal chain in two steps or fewer from a driver-app store rating to execs running Monday mornings from Insights' dashboards, and the KR shares no noun or audience with its objective (drivers and the App Store versus execs and Looker). Insights does not build the driver app either, so hitting it would record another team's result on Insights' page.
- Scores affected: K7=2, K6=3
- Suggested rewrite: "KR IN1.3: Leadership viewers who open at least three exec-suite dashboards in a week `<baseline>` → `<target>` (Looker usage stats). Owner: Vik M." — and move the App Store rating target to Courier under Objective CR1, where the app is owned. [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`input.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Why it's a problem: no accountable individual is attached, on a page that explicitly states "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (line 76) — every other Insights KR names a person, so this is an omission rather than a page convention. The KR also requires seven other squads to act, which is exactly the case where an unnamed owner means nobody chases it.
- Scores affected: K4=0, K1=3, K2=2
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual on the Insights team>`." (Proposal; the metric line is reused verbatim from line 85.)

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (`input.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95); the same label repeats on "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99), "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103) and "Objective AC4 (Priority: P0): Billing runs itself" (line 107); the team's notes confirm the intent: "every one of these is P0 for us this quarter — we're not choosing" (line 111)
- Why it's a problem: a uniform top-priority label across all four objectives encodes no trade-off, so when the quarter tightens the choice gets made implicitly by whoever is loudest. It is already biting: AC3.2's portal is gated on AC4.2's billing migration, and Dispatch has built a committed KR on top of that same portal (§4 AL-12).
- Scores affected: No single dimension; per Roll-Up cap 3 this Major combines with AP-12 on AC3 to cap AC3 at 2.40 (C), lowering the team from 3.40 to 3.20.
- Suggested rewrite: "P0: AC2 (escalation backlog) and AC3 (delivery promises) — the two C2 drivers whose quoted current numbers are worst. P1: AC1. P2: AC4, whose migration is the stated gate on AC3.2 and is therefore sequenced, not co-equal." (Proposal.)

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Why it's a problem: standing up a partner portal has no causal path in two steps or fewer to customers trusting the delivery promises Coppervale reports, and it shares no noun with its objective. The KR's own gate — the billing migration — belongs to Objective AC4, which is where it would sit if the set were coherent.
- Scores affected: K2=2, K6=2, K7=2; combines with AP-05 to trigger the ≥2-Major cap on AC3 (2.40, C)
- Suggested rewrite: Move the portal KR verbatim under "Objective AC4 (Priority: P0): Billing runs itself", and replace it under AC3 with: "KR AC3.2: Customer-raised disputes about reported delivery promises `<baseline>` → `<target>` per month (Zendesk)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`input.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`input.md` › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`input.md` › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier waits on Core Systems, Core Systems waits on Insights, Insights waits on Courier — a three-node cycle in which every team is second in line, so none of KR CR3.1, CS3.1 or IN2.1 can start or be delivered as written. Each team's notes restate its own edge as a hard gate rather than resolving it: "SDK timing per Core Systems' plan." (line 49), "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70), "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (line 87).
- Detection check that fired: dependency-graph cycle detection (AL-11 structural heuristic) over the "once / after" edges collected in the dependency map.
- Disconfirming checks run: (1) Hard blocking vs soft preference — re-read all three edges; all use hard gating language ("once", "after", "after") and none says "ideally" or "would benefit from", so no edge is soft. (2) Staged-milestone interleaving — searched all three pages for distinct milestone stages that could interleave (beta, alpha, preview, pilot, early access): none appears; Core Systems offers only GA, and Insights' gate is Courier's instrumentation of "the new driver-app event stream", which is the same work CR3.1 blocks on the SDK for. (3) Awareness plus a resolution plan — each team acknowledges its own dependency, but no page states a plan to break the cycle; the closest near-miss, "SDK v1 is code-complete" (line 70), removes build risk but not the schema-validation gate the same sentence imposes, so it does not downgrade the finding.
- Inference labels: none — all three edges quoted verbatim; commitment levels read from the pages' own stated conventions.
- Verdict: CONFIRMED (all three KR quotes and all three notes lines re-verified character-for-character against the source file)
- Severity note: Core Systems' and Insights' edges are committed per "Commitment: KRs are committed unless marked (stretch)." (lines 55 and 76). Courier's page states no commitment level at all (§3 AP-08), so its edge carries an absent label rather than a soft one — the edge wording itself is a hard block. Rated Critical because the cycle sits on the critical path of three teams' objectives and blocks two further findings.
- Recommended resolution owner: Core Systems lead (owner of the middle node) to convene Courier and Insights within one week and name one starting milestone — the plausible cut is validating schema v3 against a pre-GA SDK on one instrumented Courier flow, turning one hard gate into a staged one; the three affected KRs are then re-dated from that decision.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two different measurements — different success events (completed job vs scanned at destination), different denominators (all completed jobs vs all scheduled deliveries including cancellations), different cadences (weekly vs monthly) and different systems of record (Ops Console vs Billing warehouse). The two sit 13 points apart today and both feed the same company promise, "keeping the delivery promises we report to customers" (line 11), so any exec or customer rollup shows two irreconcilable numbers for one claim.
- Detection check that fired: metric-catalog blocking on an identical metric name used by two teams, then definition diff (AL-08 form (a) heuristic).
- Disconfirming checks run: (1) Normalize before diffing — normalized both definitions on formula, window, population and data source; they differ on all four, so they are not the same measurement in different words. (2) Superseding glossary — searched the company priorities page and both teams' notes for a shared definition; none exists, and Dispatch's notes entrench its own instead: "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31). (3) Baseline-gap explanation — the 91% vs 78% gap is explained by the definitional split (Accounts' denominator includes cancellations), so per the AL-09 heuristic it is reported here as AL-08 and not double-counted as a baseline disagreement.
- Inference labels: none — both definitions, both baselines and the company promise are quoted verbatim.
- Verdict: CONFIRMED (both definition strings and the company priority line re-verified character-for-character)
- Recommended resolution owner: the C2 owner (CEO, per the priorities page) to pick one canonical definition and one system of record before the first monthly report; the losing team keeps its measure as a renamed internal diagnostic (for example "dispatch-side on-time rate") rather than a second "On-time delivery rate".

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`input.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), on a page stating "Commitment: KRs are committed unless marked (stretch)." (same file › Dispatch team — Q1 2027 › line 19), with the dependency named in Dispatch's notes: "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's committed 600 trial starts rest entirely on a deliverable Accounts labels stretch and conditions on a second deliverable ("only if the billing migration lands early"). The arithmetic is worse than the labels: Accounts commits the portal to "the first 40 partner accounts" at best, while Dispatch's number assumes a launch broad enough to source 600 enterprise trials — Dispatch is banking not only on Accounts' stretch item landing, but on it landing far beyond its stated scope.
- Detection check that fired: acknowledged-edge label comparison on the dependency map (AL-12 heuristic) — the edge is acknowledged on both sides, so it is not AL-01; the commitment labels differ.
- Disconfirming checks run: (1) Missing label vs mismatch — both pages state their labelling schemes explicitly (Dispatch line 19, Accounts line 93), so this is a genuine mismatch and not two vocabularies. (2) Consumer hedging — searched Dispatch's KR text and notes for a discount or hedge; "assumes the partner portal launch" (line 31) records the assumption but applies no discount to the 600 and offers no fallback, so the finding stands. (3) Producer's own gate — Accounts' notes confirm rather than relieve the condition: "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111).
- Inference labels: none — both commitment labels, both targets and both notes lines are quoted verbatim.
- Verdict: CONFIRMED (all four quoted spans re-verified character-for-character)
- Recommended resolution owner: Dispatch lead with Accounts lead, within two weeks — either Accounts promotes the portal to committed at a scope that can source the trials, or Dispatch re-baselines DS2.2 to what 40 partner accounts can produce and moves the remainder to a labelled stretch KR. Cross-reference: §3 AP-05, which is why nothing in Accounts' P0 list can currently be traded to fund that promotion.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`input.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Business-review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`input.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the KR names Q4 2026 as its baseline and the same instrument as the business review, but states 86 where the review states 78. The KR's stated ask is +4 points; against the reviewed actual it is +12 — a materially different quarter of work on a committed KR, and whichever figure is wrong, one of the two documents is misreporting customer health.
- Detection check that fired: metric-catalog baseline collection — two stated baselines for the same canonical metric and the same period differing beyond rounding (AL-09 heuristic).
- Disconfirming checks run: (1) As-of dates — both explicitly cite Q4 2026, so a date difference does not explain the gap. (2) Definitional split (AL-08) — both name the same instrument, "quarterly relationship survey"; searched both pages and the company priorities page for a second CSAT definition, population or segment split (enterprise-only vs all customers) and found none, so the AL-08 route is closed and this stands as AL-09. (3) Corroboration of the appendix — its other two figures are reproduced exactly by the teams that own them ("Driver-app weekly retention 71% → 78%", line 40 against line 119; "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4", line 58 against line 120), so the appendix is the corpus's reliable baseline source and the 86 is the outlier.
- Inference labels: none — both figures, both instrument names and the two corroborating baselines are quoted verbatim.
- Verdict: CONFIRMED (both CSAT statements and both corroborating figures re-verified character-for-character)
- Recommended resolution owner: Accounts lead to reconcile with the business-review owner within one week and restate AC2.2 against the agreed figure; if 78 stands, the target needs a mechanism or a re-scope, because +12 points in one quarter is not the bet the page currently describes.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (`input.md` › Objective CS2: Ship with confidence › line 61), with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Company evidence: "C2 — Keep enterprise customers for life:** reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input.md` › Company Q1 2027 priorities › line 11)
- Conflict: C2 enumerates its own drivers — onboarding time-to-value, the escalation backlog, and delivery promises — and internal delivery velocity is none of them. All three CS2 KRs measure the team's own pipeline; none measures churn, a named C2 driver, or any deliverable C2 asks for, so all three could be hit in full in a quarter where enterprise churn worsens. The link is decorative.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic) — child KRs measure neither the parent's metric nor a documented driver of it.
- Disconfirming checks run: (1) Mechanism documented elsewhere — checked the parent's own page, which lists C2's contributing drivers explicitly and omits delivery velocity, so the parent does not name this child as a needed contribution. (2) Child's own justification — searched Core Systems' notes, which claim only "The cost work is our C4 commitment." (line 70) and say nothing linking CS2 to churn. (3) Coverage elsewhere — the three named C2 drivers are in fact staffed by Accounts (AC1, AC2, AC3, lines 95–104), so this is drift on one child link rather than a strategy coverage gap. No check weakened the finding.
- Inference labels: none — the parent's driver list, the child's claimed link and all three child KRs are quoted verbatim.
- Verdict: CONFIRMED (the parent priority line, the objective line and all three KR lines re-verified character-for-character)
- Severity note: rated Major rather than the default Minor because CS2's KRs are explicitly committed under "Commitment: KRs are committed unless marked (stretch)." (line 55) — the taxonomy's escalation rule for committed objectives.
- Recommended resolution owner: Core Systems lead with the C2 owner (CEO), within two weeks: either re-anchor CS2 to C4, where the platform-efficiency work already sits, or add one KR that measures a named C2 driver — for example enterprise-reported incident minutes during onboarding `<baseline>` → `<target>` [proposal — placeholder target].

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to name one starting milestone that breaks the telemetry cycle — owner: Core Systems lead (resolves §4 AL-11 Circular dependency).
2. Define the denominator of DS2.4's failure rate and restate the KR against it — owner: Dispatch lead (resolves §3 AP-13 Ambiguous Denominator).
3. Pick one canonical "On-time delivery rate" definition and system of record for the portfolio — owner: C2 owner (CEO) (resolves §4 AL-08 Terminology collision).
4. Re-scope DS2.2's committed 600 trial starts to what Accounts' stretch portal can support, and move the portal KR under AC4 — owner: Dispatch lead with Accounts lead (resolves §4 AL-12 Commitment asymmetry and §3 AP-12 Orphan KR — Accounts).
5. Reconcile the CSAT baseline against the Q4 2026 business review and restate AC2.2 — owner: Accounts lead (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring a named C2 driver — owner: Core Systems lead (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 so the quarter encodes a trade-off — owner: Accounts lead (resolves §3 AP-05 Everything Is a P0).
8. Add a mechanism and a leading KR to the referral target, and adopt the commitment convention on Courier's page — owner: Courier lead (resolves §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled).
9. Name an owner for IN2.2 and move the App Store rating KR to Courier — owner: Insights lead (resolves §3 AP-15 Ownerless KR and §3 AP-12 Orphan KR — Insights).
10. Reframe CS1 from "Continue running the platform smoothly" to a stated change and split the cost KR out — owner: Core Systems lead (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.48); Critical AP-13 Ambiguous Denominator, plus AP-11 and both sides of AL-08 / AL-12): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.21), above the needs-rework threshold, but carries the Critical AL-11 Circular dependency; also AP-07, AP-08): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (2.93), above the needs-rework threshold, but carries the Critical AL-11 Circular dependency; also AP-10, AL-05): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.25), above the needs-rework threshold, but carries the Critical AL-11 Circular dependency; also AP-12, AP-15): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.20) is above the needs-rework threshold and it carries no Critical finding.

Note on the three cycle teams: a single-team re-run cannot resolve AL-11 itself — single-team mode produces no cross-team findings — so each re-run addresses that team's own goodness depth while §5 action 1 carries the cycle.
