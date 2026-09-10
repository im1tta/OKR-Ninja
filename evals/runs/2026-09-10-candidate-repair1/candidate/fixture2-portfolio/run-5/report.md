# Coppervale — Q1 2027 OKR portfolio review

Mode: **portfolio** (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027, as stated by the source file. Strategy source: the file's "Company Q1 2027 priorities" section (C1–C4). Corpus: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` only — no Atlassian connection was available, so every absence claim below states the search performed over that file.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 10 Major, 3 Minor findings.

The portfolio's worst alignment risk is **AL-11 Circular dependency**: Courier's instrumentation waits on Core Systems' SDK GA, that GA waits on Insights' schema validation, and Insights' validation waits on Courier's instrumentation — three committed KRs with no valid execution order as written.

The most common goodness issue is **AP-12 Orphan KR** (two KRs measure outcomes their stated objective does not claim — Insights' App Store rating, Accounts' partner portal).

Two teams publish contradictory definitions of "On-time delivery rate", the very number C2 promises customers (**AL-08 Terminology collision**), and Accounts calibrates a committed CSAT target against a baseline the Q4 review contradicts by 8 points (**AL-09 Baseline disagreement**).

One Critical goodness defect: Dispatch commits to halving "the failure rate" without ever naming the population (**AP-13 Ambiguous Denominator**).

Recommended first action: Core Systems convenes Courier and Insights in week 1 to break the SDK/schema/instrumentation cycle before any of the three KRs can start.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 |
| Core Systems | 3 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.5) · Core Systems B (3.1) · Courier B (3.3) · Insights B (3.4) · Accounts A (3.6).

- Dispatch: K7=2 — DS2's trial-starts KR chases acquisition, not the objective's whole-day usage.
- Core Systems: O3=2, O2=2 — "Continue running the platform smoothly" is open-ended standing duty.
- Courier: K3=2 — referral installs 3,000 → 45,000 is 15x with no stated mechanism.
- Insights: K7=2 — App Store rating KR is unrelated to the exec-dashboards objective.
- Accounts: K3=2 — CSAT baseline 86 contradicts the Q4 review's 78; ambition unverifiable.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never names its population — failed jobs, failed routes, failed deliveries or failed deploys all read as candidates and would give different numbers — so the 6% → 3% claim cannot be honestly scored; the team's own neighbouring KR shows it knows how ("jobs completed within the promised window as a share of all completed jobs", same page, line 26).
- Scores affected: K1=1, K7=2 (DS2 set)
- Suggested rewrite: "KR DS2.4: Dispatch job failure rate — jobs that end without a completed delivery as a share of all jobs dispatched that week, measured weekly in the Ops Console — 6% → 3% by end of Q1 (ops weekly report)." [proposal — the population and window are OKR-Ninja's; the 6% and 3% figures are quoted from the existing KR]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Delight enterprise dispatchers and expand Coppervale into two new regions" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences (existing enterprise dispatchers vs. new DE/FR markets), and the KRs split cleanly along that seam — "Enterprise dispatcher NPS 24 → 40" (line 22) serves the first, "Signed pilot customers in DE and FR: 0 → 6" (line 23) the second — so hitting one and missing the other leaves the objective unjudgeable.
- Scores affected: O2=2, K6=3, K7=3
- Suggested rewrite: "Objective DS1: Enterprise dispatchers would rather use Coppervale than the tool they had — KR DS1.1: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." and "Objective DS3 (ranked second): Coppervale runs live routes in DE and FR — KR DS3.1: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." [proposal — both KR texts are quoted from the existing objective; only the objective wording is OKR-Ninja's]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Continue running the platform smoothly for every team" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: the objective commits the team to continuing its standing job and names no change — no direction, no reduction, nothing that differs from today; per AP-10 the two genuine deltas in its KRs ("Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4.", line 58; "Cloud cost per completed delivery $0.42 → $0.30", line 59) do not rescue an objective whose text is about continuation.
- Scores affected: O1=3, O2=2, O3=2
- Suggested rewrite: "Objective CS1: Cut platform incidents and unit cost until no team plans around us — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." [proposal — objective wording is OKR-Ninja's; both KRs are quoted unchanged]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — "big swing" states intent, not a mechanism — and it is the objective's only KR, so the quarter's biggest number has nothing steering it.
- Scores affected: K3=1, K6=0 (CR2 set), K7=2 (CR2 set)
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral bonus (App Store + Play attributed installs)." plus a leading KR "KR CR2.2 (committed): Drivers sending ≥ 1 referral invite per week `<baseline>` → `<target>` (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the convention Courier's page lacks, present on every other team page): "KRs are committed unless marked (stretch)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Dispatch team — Q1 2027 › line 19)
- Why it's a problem: this is a set-level defect on the Courier page — searched the whole Courier section (lines 35–49: page header, three objectives, five KRs, notes) for the words committed, aspirational and stretch, and for any ~0.7-target convention, and found none, while the set's stretch ranges from a 0.4-point reliability improvement to a 15x install target; nobody reading it can tell which numbers are must-hits, which corrupts both attainment expectations and the moonshot judgement above.
- Scores affected: K3=2 (team dimension), K6=2 (team dimension)
- Suggested rewrite: add the page-level line "Commitment: KRs are committed unless marked (stretch)." to the Courier page header and mark CR2.1 "(stretch)", leaving CR1.1, CR1.2, CR3.1 and CR3.2 committed. [proposal — the convention line is quoted from the Dispatch page, line 19]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its stated objective): "Execs run Monday mornings from our dashboards" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: no causal chain in two steps runs from a driver-app store rating to executives using Looker dashboards; the metric shares no noun, audience or surface with the objective and is moved by the driver app, which is Courier's material ("Drivers finish every shift without fighting the app", line 38). Hitting 4.6 would say nothing about whether the objective happened.
- Scores affected: K7=2 (IN1 set)
- Suggested rewrite: move the rating KR to Courier's CR1 and replace it with "KR IN1.3: Exec-suite dashboards meeting their weekly freshness SLA `<baseline>`/12 → 12/12 (Looker admin panel). Owner: Vik M." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own convention): "Owners listed per KR." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page promises a named owner on every KR and the other four carry one ("Owner: Halima D.", line 79; "Owner: Vik M.", lines 80 and 81); "TBD" names nobody accountable for the one KR that needs nine other squads' time, so it will be nobody's job when the quarter gets tight.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named Insights individual>`, with each squad's own lead named in the onboarding tracker row." [proposal — baseline and target quoted from the existing KR]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence (the team says so itself): "every one of these is P0 for us this quarter — we're not choosing." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry the identical top label, so the set encodes no trade-off; when the billing migration runs late — which the same note says gates the portal — nothing on the page says which of the four gives, and the answer will be improvised mid-quarter.
- Scores affected: set-level — no single scored instance moves (AP-05 is scoped to the objective set per the rubric's one-finding-per-instance rule); the consequence surfaces in §4 AL-12 Commitment asymmetry, where the unranked stretch item carries another team's committed KR.
- Suggested rewrite: "P0: AC2 (escalation backlog) and AC1 (time-to-value) — the two C2 drivers named on the company page. P1: AC4 (billing). P2: AC3, whose stretch KR AC3.2 is dropped if the migration slips past week `<n>`." [proposal — ranking is OKR-Ninja's; objective texts unchanged]

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Evidence (its stated objective): "Customers trust the delivery promises we report" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Why it's a problem: partner-portal availability moves no customer's trust in the delivery promises Coppervale reports — the objective's other KR, the on-time delivery rate (line 104), is what does — and the team's own note ties the portal to billing instead ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111), which is objective AC4's territory. Filed under AC3 it hides the fact that AC3 rests on a single measure.
- Scores affected: K7=2 (AC3 set)
- Suggested rewrite: move the portal KR under "Objective AC4 (Priority: P0): Billing runs itself" beside the migration KR it depends on, and give AC3 a second measure: "KR AC3.2: Delivery-promise disputes raised by enterprise accounts `<baseline>`/month → `<target>`/month (Zendesk view `<view name>`)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: Courier → Core Systems → Insights → Courier is a closed cycle of hard gates; each team's KR cannot start until the next team's finishes, so as written none of the three can begin and the C4 telemetry-consolidation work has no valid execution order.
- Detection check that fired: AL-11 cycle detection on the dependency map — three edges, each carrying its own verbatim blocking phrase ("once Core Systems GAs the SDK", "after Insights validates event schema v3 in production", "after Courier instruments the new driver-app event stream").
- Disconfirming checks run: hard blocking vs. soft preference — all three edges use the unconditional sequencing words once and after (quoted in the evidence lines above), and none of the three carries a softening qualifier such as ideally or would benefit from, so no edge is soft. Staged-milestone interleaving — checked all three teams' notes for a pre-GA path: Core Systems' "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) and Insights' "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (line 87) each restate the gate, and Courier's "SDK timing per Core Systems' plan." (line 49) defers to it; no page states that Courier may instrument against the pre-GA build, so no interleaving is quotable. Awareness plus resolution plan — searched all five team sections and the company priorities page; no team names the cycle or a plan to break it, so no downgrade applies.
- Inference labels: none — all three edges quoted verbatim; the observation that a code-complete SDK could support a pre-GA interleaving is offered only as the recommendation below, not as evidence.
- Verdict: CONFIRMED (each quote re-read character-for-character against lines 46, 67 and 84)
- Recommended resolution owner: Core Systems (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) in week 1 to fix one order — the obvious candidate, given "SDK v1 is code-complete" (line 70), is Courier instrumenting on the pre-GA build, Insights validating schema v3 against that traffic, and GA following — and to rewrite the three gating clauses to match.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Company-side stake: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: one metric name, two measurements — different populations (completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly), different systems of record (Ops Console vs. Billing warehouse). Both teams will report "On-time delivery rate" into the same C2 promise, 13 points apart, and neither number is wrong on its own terms.
- Detection check that fired: AL-08 form (a) — a metric name used by ≥ 2 teams; each team's stated definition pulled and diffed.
- Disconfirming checks run: normalize-before-diff — the two definitions do not reduce to the same measurement: one counts only completed jobs, the other includes cancellations in its denominator, and the data sources differ. Superseded-definition check — searched all five team sections, the company priorities page and the Q4 appendix for a shared glossary or a newer definition; none exists, and Dispatch's note asserts its own instead ("On-time delivery is measured per our Ops Console methodology (see KR DS2.1).", line 31). AL-09 pre-check — the 91% vs. 78% baseline gap is explained by the definition split, so it is reported here as AL-08 rather than as AL-09 Baseline disagreement, per that entry's first disconfirming check.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both definitions re-read character-for-character against lines 26 and 104)
- Recommended resolution owner: Noor E. (CEO, owner of the C1–C4 priorities page) rules on one canonical "on-time delivery rate" for customer-facing reporting — including whether cancellations count — and has both teams restate DS2.1 and AC3.1 against it before the first monthly business review.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: two stated Q4 2026 baselines for the same instrument, eight points apart. Accounts' KR is committed ("KRs are committed unless marked (stretch).", line 93) and reads as a +4 ask; measured from the business review's 78 it is a +12 ask, so the quarter is calibrated against a starting point at least one of the two documents gets wrong.
- Detection check that fired: metric-catalog baseline collection — every stated baseline per canonical metric compared; two values for "Customer CSAT" in the same period differing far beyond rounding.
- Disconfirming checks run: as-of dates — both explicitly say Q4 2026, so no date offset explains the gap. Definition split (AL-08) — both cite the same instrument by name, "quarterly relationship survey", and a search of all five team sections and the appendix for a second CSAT definition, population or segment (e.g. enterprise-only) that would legitimately read higher found none, so AL-08 does not explain it and the finding stands as AL-09.
- Inference labels: none — both baselines quoted with their as-of periods.
- Verdict: CONFIRMED (both quotes re-read character-for-character against lines 101 and 118)
- Recommended resolution owner: Accounts (Georg B.) with the Q4-review owner: reconcile the two figures and restate AC2.2 against the agreed baseline — including its n and segment — before Q1 targets are locked.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), committed by its page's convention: "KRs are committed unless marked (stretch)." (same file › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's committed 600 trial starts arrive "via the partner portal launch", and the portal exists on the Accounts side only as an explicitly conditional stretch item. A committed number depends end-to-end on a deliverable its producer has said it may not build this quarter.
- Detection check that fired: AL-12 edge label comparison on an acknowledged cross-team dependency — Dispatch names the owner ("DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter.", line 31), so AL-01 Unacknowledged dependency does not fire and the edge is checked for label and arithmetic mismatch instead.
- Disconfirming checks run: labeling scheme — both pages state the same convention ("KRs are committed unless marked (stretch).", lines 19 and 93), so the labels are directly comparable and DS2.2 carries no stretch marking. Hedging or discounted arithmetic — searched Dispatch's KR text and notes for any discount on the portal landing: the note states the assumption without qualifying the 600, and Accounts' own note confirms rather than removes the condition ("Portal timing depends on how fast the billing migration goes (see AC3.2).", line 111).
- Inference labels: none — both commitment levels quoted from the pages' own conventions.
- Verdict: CONFIRMED (both quotes and both convention lines re-read character-for-character against lines 19, 27, 93 and 105)
- Recommended resolution owner: Dispatch (Mei L.) and Accounts (Georg B.) decide in week 2 either to promote the portal to a committed Accounts KR with the migration resourced accordingly, or to split DS2.2 into a portal-independent committed target plus a stretch increment riding on AC3.2.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities
- Core Systems evidence: "Ship with confidence" claiming "(supports C2 — enterprise churn)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CS2: Ship with confidence › line 61), with its full KR set: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63), "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 11)
- Conflict: the parent priority enumerates its three drivers and none of them is engineering delivery velocity; none of CS2's three KRs measures churn or any named driver of it. All three could be hit in a quarter where enterprise logo churn worsens, which makes the stated link decorative.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic) — the child KRs measure neither the parent metric, nor a documented driver of it, nor a deliverable the parent's page names as needed.
- Disconfirming checks run: mechanism documented outside the child's OKR text — searched C2's own text for named contributing workstreams (it names exactly three drivers, all of them Accounts' material and covered by AC1 and AC2), searched Core Systems' notes ("SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.", line 70 — which speaks to C4, not C2), and searched all five team pages for any statement that deploy frequency, change-failure rate or CI time drives enterprise churn; nothing found, so no quote kills the finding.
- Inference labels: none — the absence of a mechanism is established from the parent's own quoted driver list rather than inferred.
- Verdict: CONFIRMED (parent and all three child KRs re-read character-for-character against lines 11 and 61–64)
- Recommended resolution owner: Core Systems (Adaeze O.) with Noor E. as C2 owner: either re-anchor CS2 to C4 (where CS1.2's unit-cost work already sits) or add one KR measuring a named C2 driver — e.g. change failures that breach the delivery promises reported to customers — by the end of week 2.

### [Minor] AL-05 Cascade drift: Courier ↔ Company Q1 2027 priorities
- Courier evidence: "Every driver in the region hears about Coppervale from another driver" claiming "(supports C3)" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 42), with its only KR: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43)
- Company evidence: "driver-app weekly retention from 71% to 80% across FY27." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md` › Company Q1 2027 priorities › line 12)
- Conflict: C3's single metric is a retention rate; CR2's single KR is an install count. Attributed installs could reach 45,000 in a quarter where weekly retention falls, so the claimed support rests on no mechanism the two numbers share.
- Detection check that fired: strategy-trace mechanism check on an explicit parent link (AL-05 heuristic).
- Disconfirming checks run: mechanism documented elsewhere — C3's text names only the retention metric and no contributing workstreams; Courier's notes say "referral growth is our big swing this quarter." (line 49), which states priority, not a retention mechanism; searched all five team pages and found no statement that referred drivers retain better. Severity check — Courier's other objective does carry C3's actual metric ("Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3).", line 40), so the priority is not left uncovered and the finding stays Minor.
- Inference labels: the observation that new installs dilute a retention cohort is analyst inference — no Coppervale document states it; the finding itself rests on the quoted mismatch between an install count and a retention rate.
- Verdict: CONFIRMED (parent, child objective and child KR re-read character-for-character against lines 12, 42 and 43)
- Recommended resolution owner: Courier (Tomás R.) either re-anchors CR2 to the growth side of C1 or adds a retention-linked KR to it (e.g. week-4 retention of referred drivers vs. all drivers) when the target is re-cut per §3 AP-07.

## 5. Prioritized action list

1. Convene Courier and Insights to fix one execution order for pre-GA instrumentation, schema v3 validation and SDK GA, then rewrite the three gating clauses — owner: Core Systems lead Adaeze O. (resolves §4 AL-11 Circular dependency).
2. Rewrite KR DS2.4 with a named population, denominator and window before the first weekly ops review — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator).
3. Rule on one canonical "on-time delivery rate" definition for C2 reporting and have both teams restate their KRs against it — owner: Noor E. (CEO), with the Dispatch and Accounts leads (resolves §4 AL-08 Terminology collision).
4. Reconcile the 86 vs 78 Q4 2026 CSAT figures and restate AC2.2 against the agreed baseline — owner: Accounts lead Georg B. (resolves §4 AL-09 Baseline disagreement).
5. Decide whether the partner portal becomes a committed Accounts KR or DS2.2 splits into portal-independent and portal-dependent halves — owner: Dispatch lead Mei L. with Accounts lead Georg B. (resolves §4 AL-12 Commitment asymmetry).
6. Re-anchor CS2 to C4 or add one KR measuring a named C2 churn driver — owner: Core Systems lead Adaeze O. (resolves §4 AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities).
7. Rank the four P0 objectives and state which one gives if the billing migration slips — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Add the commitment convention to the Courier page, label CR2.1 aspirational, and re-cut it with a stated lever plus a leading KR — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot, §3 AP-08 Committed vs Aspirational Not Labeled, §4 AL-05 Cascade drift: Courier ↔ Company Q1 2027 priorities).
9. Move the two orphan KRs to the objectives that own their metrics and name a person against IN2.2 — owner: Insights lead Halima D. with Accounts lead Georg B. (resolves §3 AP-12 Orphan KR — Insights, §3 AP-12 Orphan KR — Accounts, §3 AP-15 Ownerless KR).
10. Rewrite CS1 to name the change it commits to and split DS1 into two ranked objectives — owner: Core Systems lead Adaeze O. and Dispatch lead Mei L. (resolves §3 AP-10 BAU Dressed as OKR, §3 AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.5); Critical §3 AP-13 Ambiguous Denominator, plus §4 AL-08 Terminology collision and §4 AL-12 Commitment asymmetry): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1, owner Mei L.); strategy doc: the same file's 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.1) but a Critical finding — §4 AL-11 Circular dependency — plus §3 AP-10 BAU Dressed as OKR and §4 AL-05 Cascade drift): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1, owner Adaeze O.); strategy doc: the same file's 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.3) but a Critical finding — §4 AL-11 Circular dependency — plus §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled): re-run single-team mode — "Review the Courier team's (driver app) Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1, owner Tomás R.); strategy doc: the same file's 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.4) but a Critical finding — §4 AL-11 Circular dependency — plus §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1, owner Halima D.); strategy doc: the same file's 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.6), above the rubric's needs-rework threshold, and no Critical finding (its findings are Major — §3 AP-05, §3 AP-12, §4 AL-08, §4 AL-09, §4 AL-12).
