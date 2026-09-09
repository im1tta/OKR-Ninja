# Coppervale — Q1 2027 OKR portfolio review

## 1. Executive summary

**Verdict: At risk.** The quarter contains a three-team dependency cycle that cannot execute as written, and one KR that cannot be honestly scored at all.
Scope: 5 teams (Dispatch, Courier, Core Systems, Insights, Accounts), period Q1 2027, single source `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture2-portfolio/input/sample-portfolio-2.md`; strategy source is that file's "Company Q1 2027 priorities" section (C1–C4). Referred to below as `sample-portfolio-2.md`.
14 findings: **2 Critical, 9 Major, 3 Minor** (8 goodness, 6 alignment).
Worst alignment risk: **AL-11 Circular dependency** — Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation. No team's page shows awareness of the loop, so the C4 telemetry program has no valid start.
Most common goodness anti-pattern: none repeats — eight distinct AP-XX modes fire once each, one per instance. The most damaging is **AP-13 Ambiguous Denominator** (Dispatch's "failure rate" KR, the portfolio's only Critical goodness finding).
Second theme worth naming: two teams carry a KR called "On-time delivery rate" with different populations, windows and systems of record (AL-08 Terminology collision), and the metric feeds a company priority.
Ambition calibration is the portfolio's weakest dimension — K3 is 2 for all five teams.
Recommended first action: Core Systems convenes Courier and Insights within one week to break the SDK/schema/instrumentation cycle before any of the three teams starts building.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 |
| Core Systems | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 3 | 4 | 2 | 2 |
| Courier | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.6) · Core Systems B (3.1) · Courier B (3.2) · Insights B (3.3) · Accounts A (3.6).

- Dispatch: K3=2 — no trend or prior actual in the corpus to calibrate five of six targets against.
- Core Systems: O3=2 — "Continue running the platform smoothly" is an open-ended duty crammed into one quarter.
- Courier: K3=2 — an unlabeled 15x referral-install target sits beside modest reliability commitments.
- Insights: K7=2 — an App Store rating KR sits under the exec-dashboards objective it cannot move.
- Accounts: K3=2 — the CSAT baseline contradicts the Q4 review, so its ambition is uncalibrated.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: the KR never says failure rate *of what* — dispatched jobs, route builds, deliveries or API calls are all plausible populations in this team's material, so any number can be claimed and the KR can never be honestly scored. The contrast sits one KR earlier in the same set, where the denominator is spelled out: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26). The system of record is generic too — "ops weekly report" names no dashboard or query.
- Scores affected: K1=1, K3=2, K5=2
- Suggested rewrite: "KR DS2.4: Job failure rate — `<jobs closed without a completed delivery>` as a share of `<all jobs dispatched in the week>`, measured weekly in the Ops Console — 6% → 3% by end of Q1." (6% and 3% are quoted from the current KR; the population and the system of record are OKR-Ninja proposals — `<placeholders>` for the team to fix.)

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two and-joined end-states with disjoint audiences (existing enterprise dispatchers vs. prospective customers in new geographies) are bundled into one objective, and the KRs split cleanly along that seam — "Enterprise dispatcher NPS 24 → 40" (line 22) serves the first clause, "Signed pilot customers in DE and FR: 0 → 6" (line 23) the second — so the objective encodes no priority between them, and "Delight" is an abstraction two readers would gloss differently.
- Scores affected: O2=2, K6=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers rate Coppervale the best tool on their desk — KR: Enterprise dispatcher NPS 24 → 40 (Delighted dashboard 'Dispatcher NPS'). Objective DS3: Coppervale wins its first customers in DE and FR — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM 'Intl Pilots' view)." (Both targets are quoted from the current KRs; the split and the ranking are OKR-Ninja proposals.)

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: "Continue running" states the team's standing job with no delta — it is achieved by default staffing and is unfailable as written, which displaces a real goal from a three-objective set. "smoothly" is also an abstraction with no shared reading, and the objective's two KRs point at different end-states (reliability in CS1.1, unit cost in CS1.2), so nothing in the objective's own wording is testable.
- Scores affected: O1=2, O3=2, K7=2
- Suggested rewrite: "Objective CS1: Platform incidents stop stealing product teams' quarters — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4; KR CS1.2: engineer-hours lost to platform incidents `<baseline>` → `<target>` per month [proposal — placeholder target]. Move the C4 unit-cost KR ('Cloud cost per completed delivery $0.42 → $0.30') under an explicitly cost-framed objective, and keep 'running the platform' as a health metric outside the OKR set." (Quoted figures are from lines 58–59; the new KR and the restructure are OKR-Ninja proposals.)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 15x target in one quarter with no mechanism, no intermediate milestone and no resourcing signal anywhere on the page — the team's only stated "how" is "referral growth is our big swing this quarter." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49), which names no lever. A target of this shape functions as decoration: it will be missed by default and tells nobody what to do on Monday.
- Scores affected: K3=1
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via `<named referral lever>`; KR CR2.2 (committed, leading): drivers who share a referral link at least once `<baseline>` → `<target>` per month (App Store + Play attributed installs)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier (KR set)
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39)
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 0.4-point reliability improvement and a 15x growth bet sit in one set with no commitment labels, so expected attainment is uninterpretable and neither sandbag nor moonshot judgments can be made. Search performed for a labelling scheme: the Courier page header and notes (lines 35–36, 49) and every Courier KR line (39–47) — no "committed", "aspirational" or "stretch" marker appears anywhere on the page; the other four team pages each carry "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19, and likewise lines 55, 76, 93), so the convention exists at Coppervale and Courier alone opts out.
- Scores affected: K3=2 (Courier team score; no label separates the 15x bet from the must-hits)
- Suggested rewrite: add to the Courier page header "Commitment: KRs are committed unless marked (stretch)." and relabel: "KR CR1.1 (committed): Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics). KR CR2.1 (aspirational): Driver referral installs 3,000 → 45,000 this quarter." (Convention line quoted from line 19; targets quoted from lines 39 and 43.)

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: the stated objective is "Objective IN1: Execs run Monday mornings from our dashboards" (line 78); a public app-store rating shares no noun, audience or system with exec dashboard usage, and there is no causal chain in two steps from store rating to leadership dashboard adoption. It also measures a surface Insights does not own — the driver app belongs to Courier — so hitting it would prove nothing about IN1, while diluting the two KRs that do serve it.
- Scores affected: K7=2
- Suggested rewrite: move the store-rating measure to Courier's CR1 set, and replace it with an IN1-coherent KR: "KR IN1.3: Monday leadership reviews run entirely from the exec suite `<baseline>` → `<target>` of reviews per quarter (Looker usage stats)." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Why it's a problem: "Owner: TBD" leaves the KR with no accountable individual on a page whose own convention is "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76) — every other Insights KR names a person (lines 79, 80, 81, 84). This KR also carries the portfolio's widest cross-team ask (seven more squads onboarded), which is exactly the work that stalls without a named driver. Search performed: the Insights page (lines 74–87) and all four other team pages — no individual is attached to this KR anywhere in the corpus.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named Insights individual>`." (Target quoted from line 85; the owner is a placeholder for the team to fill.)

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself" (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 107)
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four objectives carrying an identical P0 label, with the team explicitly declining to rank them, means the set encodes no trade-off — when the quarter gets tight the sequencing decision falls to whoever is loudest, and eight committed KRs across four top-priority objectives leave each target's ambition unresourceable and therefore unjudgeable. The team's own notes make the contention concrete: "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111) — two of the four P0s already compete for the same runway.
- Scores affected: K3=2 (eight committed KRs across four equally-ranked P0 objectives leave every target's ambition unresourced and therefore uncalibrated)
- Suggested rewrite: "P0: AC1 and AC2 — the two C2 drivers the company page names first. P1: AC3. Deferred to next cycle: AC4, with the billing migration tracked as a delivery milestone outside the OKR set." (The ranking is an OKR-Ninja proposal; the C2 driver ordering is quoted from sample-portfolio-2.md › Company Q1 2027 priorities › line 11.)

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: the three KRs close a loop — Courier waits on Core Systems' GA, Core Systems waits on Insights' validation, Insights waits on Courier's instrumentation — so none of the three can start, and the C4 telemetry-consolidation program has no valid execution order as written.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — the "once/after" edges quoted from lines 46, 67 and 84 close a three-node cycle (Courier → Core Systems → Insights → Courier).
- Disconfirming checks run: (a) hard blocking vs. soft preference — all three edges use hard sequencing wording ("once", "after", "after"), none says "ideally" or "would benefit from", so no edge is soft; (b) staged-milestone interleaving — Core Systems' notes close the pre-GA escape hatch, "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70), and Insights' notes confirm hard sequencing rather than a parallel path, "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (line 87); (c) awareness plus resolution plan — all three teams' notes searched (lines 49, 70, 87): Courier's "SDK timing per Core Systems' plan." (line 49) shows awareness of one edge only and states no plan for the loop, so no downgrade applies.
- Inference labels: identifying the work Insights names ("after Courier instruments the new driver-app event stream") with Courier's KR CR3.1 is analyst inference — CR3.1 is the only instrumentation KR in Courier's material and is itself gated on the SDK GA, so the cycle holds on either reading. All three edge quotes are verbatim.
- Verdict: CONFIRMED (all three edge quotes re-fetched and matched character-for-character; two of the three edges are committed under their pages' stated convention, "Commitment: KRs are committed unless marked (stretch)." (lines 55 and 76), and no edge is soft — hence Critical rather than Major)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) within one week to cut one edge — e.g. ship a pre-GA SDK build Courier may instrument against, or let Insights validate schema v3 on an existing event stream — and rewrite all three KRs to state the agreed sequence.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two different measurements — different populations (completed jobs vs. all scheduled deliveries including cancellations), different windows (weekly vs. monthly) and different systems of record (Ops Console vs. Billing warehouse). Both roll up to the company priority "keeping the delivery promises we report to customers" (sample-portfolio-2.md › Company Q1 2027 priorities › line 11), so an exec reading "On-time delivery rate" gets two irreconcilable numbers and neither team's target can be checked against the other's.
- Detection check that fired: AL-08 metric-name blocking — "On-time delivery rate" is used by two teams; each team's definition was hunted on its own page and diffed (form (a): same name, different definition).
- Disconfirming checks run: (a) normalize both definitions before diffing — normalization does not converge: the denominators differ materially (cancellations excluded from one base, included in the other) and the sources differ, so these are not one measurement under different wording; (b) superseded page version — page dates checked (Dispatch last updated 2027-01-04, Accounts 2027-01-08), and no shared glossary or later definition exists anywhere in the corpus; Dispatch instead asserts its own methodology, "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31); (c) AL-09 Baseline disagreement check — the 91% vs 78% baseline gap is explained by the definition split, so it is reported here as AL-08 rather than as a separate baseline finding, per AL-09's disconfirming rule.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both definitions and the company priority re-fetched and matched character-for-character; the metric feeds an exec-level company priority, hence Major rather than the default Minor)
- Recommended resolution owner: Insights lead (Halima D.), as the portfolio's metric-definition owner, arbitrates one canonical "On-time delivery rate" (single population, window and system of record) with Dispatch and Accounts before mid-quarter; the other team renames its measure.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch" (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), under the page convention "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19) — DS2.2 carries no stretch marker, so it is committed.
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" marked "(stretch — only if the billing migration lands early)" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's committed 600-trial-start KR depends entirely on a deliverable its producer has explicitly labelled a conditional stretch, and the arithmetic assumes more than that stretch target delivers — 600 trial starts sourced from a portal scoped to "the first 40 partner accounts". Dispatch's own note asserts the opposite of the stretch label: "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31).
- Detection check that fired: AL-12 edge label comparison on an acknowledged dependency — the Dispatch → Accounts portal edge is acknowledged on both sides (so not AL-01) and the commitment labels on each side are mismatched; target arithmetic was compared too (600 vs. 40).
- Disconfirming checks run: (a) labelling-scheme check — Dispatch states its scheme explicitly on line 19, so the missing marker on DS2.2 is a real "committed", not an absent vocabulary; (b) consumer hedging — Dispatch's KR text and notes searched (lines 27, 31): the note asserts the portal launch and asserts Accounts owns it "this quarter" rather than discounting or hedging it, so the check strengthens rather than kills the finding; Accounts' own note confirms the conditionality, "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111).
- Inference labels: none — all load-bearing text quoted, including both commitment labels.
- Verdict: CONFIRMED (both KRs, both commitment markers and both notes re-fetched and matched character-for-character)
- Recommended resolution owner: Dispatch lead (Mei L.) and Accounts lead (Georg B.) agree within two weeks either to promote the portal KR to committed with the billing-migration risk resourced, or to re-baseline DS2.2 to the trial volume 40 partner accounts can actually produce.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company (Q4 2026 business review)
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, the same named instrument and the same stated period carry two starting values eight points apart. Accounts' committed target is calibrated from 86; measured from the reviewed actual of 78 the same KR is a +12 ask, not +4 — so either the target is far harder than the team has planned for, or the company review reports a number the team does not recognise.
- Detection check that fired: AL-09 metric-catalog baseline collection — every stated baseline for "Customer CSAT" was collected across the corpus, and the two values for the same metric and period differ beyond rounding.
- Disconfirming checks run: (a) as-of dates — both statements are explicitly Q4 2026 (the KR says "Q4 2026 baseline", the review says "ended Q4 2026"), so a date difference does not explain the gap; (b) AL-08 definitional split — all five team pages and the company priorities section searched for a second CSAT definition, population or instrument: both sides name the same "quarterly relationship survey" and no other definition exists in the corpus, so a population difference does not explain it either.
- Inference labels: none — both baseline statements and their as-of periods are quoted verbatim.
- Verdict: CONFIRMED (both statements re-fetched and matched character-for-character; AC2.2 is committed under the Accounts convention on line 93, hence Major)
- Recommended resolution owner: Accounts lead (Georg B.) reconciles the CSAT baseline with the Q4 review owner before mid-quarter and restates AC2.2 from the agreed number.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "Objective CS2: Ship with confidence" linked as "(supports C2 — enterprise churn)" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the link is decorative. All three child KRs are internal delivery-pipeline measures; none measures enterprise logo churn, and none of C2's three explicitly named drivers is deploy velocity, change-failure rate or CI time. Core Systems could hit 8 deploys a week on a 15-minute pipeline in a quarter where enterprise churn worsens, and nothing in either document would notice.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KRs measure neither the parent's metric, nor a driver the parent's own page names, nor a deliverable that page calls for.
- Disconfirming checks run: (a) mechanism documented outside the child's OKR text — the parent's own page lists its contributing drivers exhaustively ("driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers", line 11) and the pipeline metrics are not among them; (b) child's own justification — Core Systems' notes searched, stating only "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." and "The cost work is our C4 commitment." (line 70), with no churn mechanism anywhere; (c) coverage near-miss — C2's three drivers are in fact claimed by Accounts (AC1, AC2, AC3 on lines 95, 99, 103), so C2 is not uncovered and the defect is this child's link specifically, not a portfolio hole.
- Inference labels: none — the failed mechanism check rests entirely on quoted text from both pages.
- Verdict: CONFIRMED (parent, child link and all three child KRs re-fetched and matched character-for-character). Severity: Minor by AL-05's default (C2 does not name Core Systems as a contributor), escalated one level to Major because CS2's KRs are explicitly committed under the page's stated convention on line 55.
- Recommended resolution owner: Core Systems lead (Adaeze O.) either re-parents CS2 to C4, where the pipeline metrics genuinely belong, or adds a KR measuring a named C2 driver, and confirms the re-parenting with the C2 owner (Noor E.) before mid-quarter.

### [Minor] AL-05 Cascade drift: Courier ↔ Company priority C3
- Courier evidence: "Objective CR2: Every driver in the region hears about Coppervale from another driver" linked as "(supports C3)" (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 42), with its single KR "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43)
- Company evidence: "driver-app weekly retention from 71% to 80% across FY27." (sample-portfolio-2.md › Company Q1 2027 priorities › line 12)
- Conflict: referral installs are an acquisition measure; C3's only metric is weekly retention. The child KR does not measure the parent metric and is nowhere named as a driver of it, so the objective could be fully achieved in a quarter where retention falls.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KR measures neither the parent's metric nor a documented driver of it.
- Disconfirming checks run: (a) mechanism documented elsewhere — C3's line names no contributing workstreams, and Courier's notes offer only "referral growth is our big swing this quarter." (line 49), a capacity statement rather than a mechanism; (b) near-miss check — the same team traces to C3 correctly one objective earlier, "Driver-app weekly retention 71% → 78%" described as a "Q1 step toward the FY27 80% goal in C3" (line 40), which shows the team can trace properly and confines the defect to CR2; that correct trace also means C3 is covered, so this is drift, not a coverage gap.
- Inference labels: the finding rests on the documentary check (no stated driver relationship on either page); any claim that installs would actively dilute the retention cohort is analyst inference and carries no weight here.
- Verdict: CONFIRMED (parent priority, child objective, its link and its KR re-fetched and matched character-for-character). Severity: Minor — AL-05's default, since C3 names no contributor and Courier's page states no commitment convention that would trigger an escalation.
- Recommended resolution owner: Courier lead (Tomás R.) either adds a retention-linked KR under CR2 or re-parents CR2 to a driver-supply priority and says so on the page, before mid-quarter.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to cut one edge of the telemetry cycle and rewrite all three KRs with the agreed sequence — owner: Core Systems lead (Adaeze O.), within one week (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with a stated population and a named system of record, or drop it — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Arbitrate one canonical "On-time delivery rate" definition across Dispatch and Accounts before the metric reaches an exec review — owner: Insights lead (Halima D.) (resolves §4 AL-08 Terminology collision).
4. Reconcile the committed 600-trial-start KR with the portal's stretch label and its 40-account scope — owners: Dispatch lead (Mei L.) and Accounts lead (Georg B.) (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the CSAT baseline against the Q4 review and restate AC2.2 from the agreed number — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
6. Re-parent CS2 to C4 or add a KR measuring a named C2 driver — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-05 Cascade drift, Core Systems ↔ C2).
7. Rank the four Accounts objectives and defer the lowest so the set encodes a trade-off — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Move the App Store rating KR to Courier and name an individual owner for IN2.2 — owner: Insights lead (Halima D.) (resolves §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR).
9. Split the referral bet into an aspirational target plus a committed leading KR, and adopt the company commitment-labelling convention on the Courier page — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled).
10. Restate CS1 as a change rather than a continuation, moving the standing duty to a health-metric section — owner: Core Systems lead (Adaeze O.) (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.6); qualifies on criterion (b) — Critical AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.2); qualifies on criterion (b) — Critical AL-11 Circular dependency): re-run single-team mode — "Review the Courier team's (driver app) Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.1); qualifies on criterion (b) — Critical AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.3); qualifies on criterion (b) — Critical AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.6), above the needs-rework threshold, and no Critical finding (its findings are Major — AP-05, AL-08, AL-09, AL-12).
