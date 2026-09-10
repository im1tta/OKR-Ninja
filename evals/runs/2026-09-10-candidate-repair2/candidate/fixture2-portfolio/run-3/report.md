# Coppervale — Q1 2027 portfolio OKR review

*Scope: 5 teams (Dispatch, Courier, Core Systems, Insights, Accounts), period Q1 2027, portfolio mode. Source: `sample-portfolio-2.md` (company priorities page 91050, five team OKR pages, Q4 2026 business-review appendix). Strategy source in scope: "Company Q1 2027 priorities" (C1–C4).*

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency: Courier's telemetry instrumentation waits on Core Systems' SDK GA, that GA waits on Insights' schema v3 validation, and that validation waits on Courier's instrumentation — three teams, no valid execution order as written, and the loop sits on C4's telemetry consolidation.
Second Critical: AP-13 Ambiguous Denominator on Dispatch's "failure rate" KR, which can never be honestly scored.
No goodness anti-pattern repeats — each of the 8 quality findings is a distinct AP-ID; the highest-severity is AP-13 Ambiguous Denominator (Dispatch), and the most systemic is AP-05 Everything Is a P0 (Accounts, all four objectives P0).
Two teams report "On-time delivery rate" under incompatible definitions and baselines (AL-08 Terminology collision) on a metric C2 names as a company priority, and Accounts' committed CSAT target is calibrated on a baseline the Q4 review contradicts by 8 points (AL-09 Baseline disagreement).
Recommended first action: convene Courier, Core Systems and Insights to break the telemetry cycle by naming one entry point before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.54) · Core Systems B (3.31) · Courier B (3.34) · Insights B (3.44) · Accounts A (3.56).

- Dispatch: K6=2 — DS1's two KRs are both quarter-end lagging measures, no leading signal.
- Core Systems: K6=2 — CS1 pairs two lagging quarter-end counts, nothing steers mid-cycle.
- Courier: K3=2 — referral-install target is a 15x jump with no stated mechanism (AP-07).
- Insights: K7=2 — IN1 carries an App Store rating KR unrelated to dashboard usage (AP-12).
- Accounts: K3=2 — CSAT target calibrated on a baseline the Q4 review contradicts (AL-09).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never states its population — failed jobs, failed route builds, failed API calls or failed deliveries are all live readings on this page, and each yields a different number, so any result can be claimed as a hit. Every neighbouring Dispatch KR names its denominator ("as a share of all completed jobs", line 26); this one does not.
- Scores affected: K1=1, K5=2, K3=3
- Suggested rewrite: "KR DS2.4: Dispatch job failure rate — jobs cancelled or aborted after dispatch as a share of all dispatched jobs, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions *(supports C1)* › line 21)
- Why it's a problem: two unrelated end-states with disjoint audiences (existing enterprise dispatchers vs. new DE/FR markets) sit under one objective, and its KRs split cleanly along that seam — "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (line 22) serves the first, "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (line 23) the second — so the objective encodes no trade-off if one half slips. "Delight" also reads differently to two people (O2=2).
- Scores affected: O1=3, O2=2, K7=3
- Suggested rewrite: "DS1 (ranked first): Enterprise dispatchers choose Coppervale over their old console — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS"). DS1b: Coppervale runs live routes in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)."

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)* › line 43)
- Why it's a problem: a 15x quarter-over-quarter target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — the only supporting text is "referral growth is our big swing this quarter." (line 49), which states enthusiasm, not a mechanism. The KR decorates the plan instead of steering it, and as CR2's only KR nothing else in the set can be steered by.
- Scores affected: K3=1, K6=0, K7=2
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app invite flow (App Store + Play attributed installs); leading KR CR2.2 (committed): drivers sending ≥1 invite 0 → `<target>`/week (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (`sample-portfolio-2.md` › Courier team (driver app) — Q1 2027 › line 36) — the page header carries no commitment convention, and a search of the whole Courier block (lines 35–49) for "commit", "stretch" and "aspiration" returns zero hits, while the four other team pages each state "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19).
- Why it's a problem: Courier's targets vary wildly in stretch — "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (line 39) is a routine must-hit while the 15x "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43) is an explicit big swing — yet nothing marks which is which, so expected attainment for the set cannot be computed and the moonshot is scored as if it were a commitment. This is a defect of the set, not of any one KR.
- Scores affected: K3=2 (team aggregate), K6=2 (team aggregate)
- Suggested rewrite: add to the Courier page header: "Commitment: KRs are committed unless marked (stretch)." and mark CR2.1 "(stretch)"; leave CR1.1, CR1.2, CR3.1 and CR3.2 committed.

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (`sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team *(supports C4)* › line 57)
- Why it's a problem: the objective commits the team to continuing its standing job and names no change — "Continue running… smoothly" is what the team is already staffed to do, so it is achieved by default and displaces a real goal. The two real deltas underneath it, "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (line 58) and "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (line 59), do not rescue it: deltas in the KRs never rescue a standing-duty objective, because the objective is the thing the anti-pattern is about.
- Scores affected: O1=2, O2=3, K6=2, K7=3
- Suggested rewrite: "CS1: Cut the reliability and cost drag every product team pays — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")."

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards *(supports C4)* › line 81)
- Why it's a problem: the stated objective is "Execs run Monday mornings from our dashboards" (line 78); a public app-store rating shares no noun, audience or surface with exec dashboard usage and there is no causal chain in two steps from store reviews to leadership viewers — moving it would not move the objective. It also measures a surface Insights does not own (the driver app is Courier's, lines 35–49), so hitting it would credit Insights for another team's outcome.
- Scores affected: K7=2, K2=4 (measures a real outcome — the wrong one)
- Suggested rewrite: drop IN1.3 from IN1 and replace with "KR IN1.3: Leadership decisions logged against an exec-suite dashboard in the Monday review 0 → `<target>` per month (Looker usage stats + review notes). Owner: Halima D." [proposal — placeholder target]; if the store rating matters, it belongs to Courier under CR1.

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema *(supports C4)* › line 85)
- Why it's a problem: the KR names no accountable individual, on a page that explicitly promises one — "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (line 76) — and every other Insights KR carries a name (Halima D., Vik M.). This is also the one KR whose delivery depends on seven squads outside Insights, so "TBD" leaves the hardest coordination in the portfolio with nobody driving it.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights)."

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (`sample-portfolio-2.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks *(supports C2 — onboarding time-to-value)* › line 95); "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99); "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103); "Objective AC4 (Priority: P0): Billing runs itself" (line 107); "every one of these is P0 for us this quarter — we're not choosing." (`sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself *(supports C1)* › line 111)
- Why it's a problem: four of four objectives carry an identical top-priority label and the team says in writing that it is not choosing, so the set encodes no trade-off — when the quarter tightens, the sequencing decision falls to whoever is loudest rather than to the plan. This is a defect of the objective set, not of any single objective or KR.
- Scores affected: K7=3 (team aggregate); no single objective's score changes
- Suggested rewrite: "P0: AC1 (onboarding time-to-value) and AC2 (escalation backlog) — the two drivers C2 names first. P1: AC4 (billing). P2 / accept slip: AC3, whose portal KR is already conditional on the billing migration."

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it *(supports C4)* › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts *(supports C4)* › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema *(supports C4)* › line 84)
- Conflict: Courier waits on Core Systems' GA, Core Systems waits on Insights' validation, Insights waits on Courier's instrumentation — a three-edge cycle with no entry point, so as written none of the three KRs can start, and all three serve C4's "consolidate our duplicated data and telemetry pipelines" (line 13).
- Detection check that fired: AL-11 structural cycle detection on the dependency map — Courier → Core Systems ("once Core Systems GAs the SDK"), Core Systems → Insights ("after Insights validates event schema v3 in production"), Insights → Courier ("after Courier instruments the new driver-app event stream").
- Disconfirming checks run: hard-blocking vs. soft preference — all three edges use hard sequencing words ("once", "after", "after"), none says "ideally" or "would benefit from", so no edge is soft. Staged-milestone interleaving — Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) shows a pre-GA build exists that could break the loop, but Courier's KR gates on GA, not on code-complete, so no interleaving is committed anywhere in the text; this weakens the deadlock's inevitability without killing the cycle as written. Awareness plus a resolution plan — searched all three teams' Notes lines (49, 70, 87): each names its own upstream ("SDK timing per Core Systems' plan.", line 49; "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream", line 87), none acknowledges the loop or proposes an order.
- Inference labels: none — all three edges are quoted verbatim; the "code-complete could break the loop" reading is labeled analyst inference and is not load-bearing for the finding.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) to convene Courier and Insights in week 1 and name the entry point in writing — most cheaply, Courier instruments against the code-complete SDK v1 pre-GA, unblocking Insights' validation and then Core Systems' GA — and to restate all three KRs against that order.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch *(supports C1)* › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report *(supports C2)* › line 104)
- Conflict: one metric name, two different measurements — different populations (completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly), different systems of record (Ops Console vs. Billing warehouse) — which is why the same quarter starts at 91% for one team and 78% for the other. C2 makes this an exec-level number ("keeping the delivery promises we report to customers", line 11) and AC3.2 promises partners "the same on-time delivery reporting AC3.1 measures" (line 105), so two incompatible numbers will travel under one name to customers.
- Detection check that fired: AL-08 form (a) — same metric name used by ≥2 teams; each team's definition hunted on its own page and diffed (formula, window, population, data source all differ).
- Disconfirming checks run: normalize-before-diffing — normalized, the two formulas still differ on the denominator (completed jobs excludes cancellations; scheduled deliveries includes them) and on the measurement point (completion in the Ops Console vs. destination scan in Billing), so they are not the same measurement in different words. Superseded-definition check — searched both pages and the appendix for a shared glossary or a newer definition; none exists, and Dispatch's note asserts its own methodology instead ("On-time delivery is measured per our Ops Console methodology (see KR DS2.1).", line 31). AL-09 pre-check — the 91% vs. 78% baseline gap is explained by this definition split, so it is reported here as AL-08, not as a separate baseline disagreement.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both definitions re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) to publish one company definition of "on-time delivery rate" — naming population, measurement point, window and system of record — and restate DS2.1 and AC3.1 against it (or rename one metric) before the first monthly customer report of Q1.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch *(supports C1)* › line 27), committed by the page's own convention "Commitment: KRs are committed unless marked (stretch)." (`sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19) and dependent per "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures *(stretch — only if the billing migration lands early)*." (`sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report *(supports C2)* › line 105)
- Conflict: Dispatch's committed 600-trial-start number rests entirely on a portal that its producer lists as an explicitly conditional stretch — and conditional on a second thing, the billing migration ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111). Dispatch's arithmetic assumes 100% of a deliverable Accounts has priced at "only if"; the portal is also scoped to 40 partner accounts, while Dispatch expects 600 enterprise trial starts through it.
- Detection check that fired: AL-12 edge-label comparison on an acknowledged dependency — the portal edge is acknowledged by both sides (so not AL-01), and the commitment labels on the two ends do not match (committed-by-default vs. "stretch").
- Disconfirming checks run: missing-label check — not applicable here; both sides state a labelling scheme, Dispatch's page convention (line 19) and Accounts' explicit "(stretch …)" tag (line 105), so this is a genuine mismatch, not two vocabularies. Consumer-hedging check — searched Dispatch's KR text and Notes (lines 27, 31) for any discount or hedge on the portal ("assumes", "if", "% of"); the note says "assumes the partner portal launch" flatly, with no reduced expectation, so nothing kills or downgrades the finding.
- Inference labels: none — all load-bearing text quoted, including both commitment labels.
- Verdict: CONFIRMED (both quotes and both commitment labels re-verified character-for-character against the source file)
- Recommended resolution owner: Dispatch lead (Mei L.) and Accounts lead (Georg B.) to agree in week 2 either that Accounts commits the portal (moving AC3.2 off stretch) or that DS2.2 is re-based on a non-portal channel with a discounted target.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice *(supports C2 — escalation backlog)* › line 101)
- Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`sample-portfolio-2.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, the same named instrument and the same period carry two starting values eight points apart. If 78 is right, Accounts' committed "+4" is really a "+12" ask against a P0 objective, and the quarter's progress reporting will disagree with the business review from week one.
- Detection check that fired: AL-09 metric-catalog baseline collection — canonical metric "Customer CSAT" collected two stated baselines for the same period (86 on the OKR page, 78 in the Q4 review) differing far beyond rounding.
- Disconfirming checks run: definitional-split check (AL-08 first) — both sides name the identical instrument, "quarterly relationship survey", and neither states a different population or segment, so no AL-08 explanation exists; this stays AL-09. As-of-date check — both refer to Q4 2026 (the OKR says "Q4 2026 baseline", the review says "ended Q4 2026"), so different as-of dates do not explain the gap. Searched the whole file for any other CSAT figure or reconciliation note: lines 101 and 118 are the only two mentions.
- Inference labels: none — both baseline statements quoted verbatim with their periods and instrument.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Accounts lead (Georg B.) to reconcile with the Q4 business-review owner within one week and restate AC2.2 from the agreed number before the quarter's first check-in.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities (C2)
- Core Systems evidence: "Ship with confidence *(supports C2 — enterprise churn)*" (`sample-portfolio-2.md` › Objective CS2: Ship with confidence *(supports C2 — enterprise churn)* › line 61), with its full KR set: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62); "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63); "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Company priorities evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: the objective claims C2, but none of its three KRs measures churn or any of the three drivers C2 itself names — they measure the team's own delivery pipeline. All three could be hit in a quarter where enterprise churn worsens, which is the tell for a decorative link; meanwhile Accounts already owns C2's three named drivers (AC1, AC2, AC3), so nothing depends on this claim being true.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — child KRs measure neither the parent's metric (logo churn) nor a documented driver of it (the parent page names three, and deploy pipeline health is not among them).
- Disconfirming checks run: documented-mechanism-elsewhere check — searched the company priorities page (lines 10–13) for named contributing workstreams (it names onboarding time-to-value, the escalation backlog and delivery-promise reporting, none of them Core Systems'), and Core Systems' own Notes line (line 70) for a stated causal path to churn — it discusses only the SDK and "The cost work is our C4 commitment.", so no source names CS2's deliverables as a needed contribution to churn. Nothing found that kills the finding. Severity: Minor by default (C2 does not name this child as a contributor), escalated one level to Major because the KRs are committed by the page's convention ("Commitment: KRs are committed unless marked (stretch).", line 55).
- Inference labels: none — parent, child, the claimed link and all three child KRs are quoted; no parent link was inferred.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (Adaeze O.) to either re-anchor CS2 to C4 (where deploy and CI economics genuinely sit) or add one KR that measures a C2-named driver — e.g. "escalations caused by production changes `<baseline>` → `<target>` (Zendesk view "Escalations — Open")" [proposal — placeholder target] — agreed with Accounts, before the quarter's first review.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to name one entry point into the telemetry sequence (instrument against the code-complete SDK pre-GA) and restate CR3.1, CS3.1 and IN2.1 against that order — owner: Core Systems lead Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Define the denominator and system of record for Dispatch's failure-rate KR, and split DS1's two end-states into separate objectives — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator, §3 AP-11 Objective as Kitchen Sink).
3. Publish one company definition of "on-time delivery rate" and restate DS2.1 and AC3.1 against it before the first customer report of Q1 — owner: Accounts lead Georg B. with Dispatch lead Mei L. (resolves §4 AL-08 Terminology collision).
4. Decide whether the partner portal is committed or stretch, and re-base Dispatch's 600 trial starts on that answer — owner: Dispatch lead Mei L. with Accounts lead Georg B. (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Q4 2026 CSAT baseline with the business-review owner and restate AC2.2 from the agreed figure — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring a C2-named churn driver — owner: Core Systems lead Adaeze O. (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 instead of marking all four P0 — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Rewrite CS1's objective to name the change its KRs already deliver, instead of "Continue running the platform smoothly" — owner: Core Systems lead Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR).
9. Drop the App Store rating KR from IN1 and name an accountable individual on IN2.2 — owner: Insights lead Halima D. (resolves §3 AP-12 Orphan KR, §3 AP-15 Ownerless KR).
10. Add a commitment convention to the Courier page and give the referral moonshot a stated mechanism plus a leading KR — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot, §3 AP-08 Committed vs Aspirational Not Labeled).

## 6. Suggested single-team re-runs

- **Dispatch** (Critical finding: AP-13 Ambiguous Denominator; roll-up C (2.54)): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (Critical finding: party to AL-11 Circular dependency; also AP-10 BAU Dressed as OKR, AL-05 Cascade drift; roll-up B (3.31)): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (Critical finding: party to AL-11 Circular dependency; also AP-07 Unmoored Moonshot; roll-up B (3.34)): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (Critical finding: party to AL-11 Circular dependency; also AP-12 Orphan KR, AP-15 Ownerless KR; roll-up B (3.44)): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.56), above the needs-rework threshold, and no Critical finding (its findings are AP-05, AL-08, AL-09 and AL-12, all Major).
