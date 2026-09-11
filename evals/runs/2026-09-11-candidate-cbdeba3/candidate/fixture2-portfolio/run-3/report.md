# Coppervale — Q1 2027 portfolio OKR review

**Mode:** portfolio (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts) · **Period:** Q1 2027 · **Strategy source:** the "Company Q1 2027 priorities" section (C1–C4).
**Corpus:** `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-candidate-cbdeba3/candidate/fixture2-portfolio/input/sample-portfolio-2.md` — source refs below abbreviate it as `sample-portfolio-2.md`; line numbers refer to that file.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema-v3 validation, and Insights waits on Courier's instrumentation — as written no team can start, and the C4 telemetry-consolidation work sits entirely inside the loop.
Most common goodness anti-pattern: none repeats — the eight goodness findings are eight distinct AP-IDs with one instance each; the most damaging is AP-13 Ambiguous Denominator (Dispatch DS2.4), the portfolio's only Critical goodness finding, where "the failure rate" names no population.
Two teams run a metric called "On-time delivery rate" on different formulas, populations, cadences and systems, and both report it up to the same company priority (AL-08 Terminology collision).
Dispatch's committed 600-trial-start KR rides on a partner portal that Accounts lists as an explicit stretch (AL-12 Commitment asymmetry), and Accounts' CSAT target is calibrated on a baseline the Q4 business review contradicts by eight points (AL-09 Baseline disagreement).
Recommended first action: a Core Systems / Insights / Courier sequencing session in week 1 to break the telemetry cycle before any of the three spends the quarter waiting.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 4 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 2 |
| Accounts | 4 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.51) · Core Systems B (3.04) · Courier B (3.25) · Insights B (3.29) · Accounts B (3.47).

- Dispatch: K6=2 — DS1 pairs a lagging NPS with an unrelated pilot count; no leading signal.
- Core Systems: O1=2 — CS1 commits to continuing, not to changing (AP-10 BAU Dressed as OKR).
- Courier: K3=2 — referral installs jump 15x with no stated mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1 carries an App Store rating KR unrelated to exec dashboards (AP-12 Orphan KR).
- Accounts: K3=2 — CSAT target rests on a baseline the Q4 review contradicts (AL-09).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" names no population — failed jobs, failed deliveries, failed route builds and failed API calls all yield different numbers from the same quarter, so any result can be claimed as a hit; the same objective shows the team can state a denominator when it wants to ("as a share of all completed jobs", line 26), which makes the omission here unscoreable rather than stylistic.
- Scores affected: K1=1, K5=3
- Suggested rewrite: "KR DS2.4: Job failure rate — dispatched jobs that end in a failed state as a share of all jobs dispatched that week, measured weekly in the Ops Console — 6% → 3% by end of Q1."

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences (today's enterprise dispatchers vs. prospects in DE and FR) sit under one objective, and the KRs split cleanly along that seam — "Enterprise dispatcher NPS 24 → 40" (line 22) serves the first half and "Signed pilot customers in DE and FR: 0 → 6" (line 23) the second — so each half carries a single KR and the objective can be half-achieved with no way to say whether it happened.
- Scores affected: O2=2, K6=2, K7=3
- Suggested rewrite: "Objective DS1: Enterprise dispatchers would fight to keep Coppervale (supports C1) — KR DS1.1: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS"); KR DS1.2: enterprise dispatchers running `<share>`% of their day's jobs in Coppervale (Ops Console telemetry)." plus a separately ranked "Objective DS3: Coppervale is live with paying dispatch customers in DE and FR (supports C1) — KR DS3.1: Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." [proposal — placeholder target]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — the closest the page comes is "referral growth is our big swing this quarter. SDK timing per Core Systems' plan." (line 49), which states enthusiasm, not a mechanism — so the number decorates the page instead of steering work, and nobody can tell a miss from an honest stretch (the page also carries no committed/aspirational convention — see AP-08 below).
- Scores affected: K3=1, K6=0 (CR2 has a single KR)
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral offer (App Store + Play attributed installs); KR CR2.2 (committed, leading): drivers sending at least one referral invite `<baseline>` → `<target>` per week (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36) — the section's only header line; no commitment convention follows it, unlike Dispatch's "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19).
- Evidence: the unlabeled set mixes stretch sizes that are orders apart — "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) against "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43).
- Why it's a problem: search performed — the whole Courier section (lines 35–49) was read for `committed`, `aspirational`, `stretch` and any P-label, with no hit, while the other four team sections each carry the convention line (lines 19, 55, 76, 93); with labels absent on the one page whose targets vary most, expected attainment is uninterpretable and the 15x referral KR cannot be judged as an honest stretch or a committed miss.
- Scores affected: K3 (drives CR2.1's K3=1 judgement; leaves CR1.1 and CR3.1 unclassifiable)
- Suggested rewrite: add to the Courier page header, "Commitment: KRs are committed unless marked (stretch)." — and mark CR2.1 "(stretch)" while leaving CR1.1, CR1.2, CR3.1 and CR3.2 committed.

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Why it's a problem: the objective asserts continuation of the team's standing job and names no change at all — "smoothly" states no direction, reduction or improvement — so it is achieved by default staffing and displaces a real goal; the two genuine deltas beneath it, "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (line 58) and "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (line 59), cannot rescue an objective that commits the team to continuing rather than to changing anything.
- Scores affected: O1=1, O2=2, K6=2
- Suggested rewrite: "Objective CS1: Teams stop losing days to platform incidents, and every delivery costs Coppervale less to run (supports C4) — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4; KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")."

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Why it's a problem: the objective is "Objective IN1: Execs run Monday mornings from our dashboards" (line 78) and its other two KRs measure leadership dashboard use and dashboard load time; a public App Store rating for the driver app shares no noun, audience or system with exec dashboards and no causal chain in two steps connects it — worse, the surface it measures belongs to Courier, whose objective is "Objective CR1: Drivers finish every shift without fighting the app" (line 38), so the KR also sits with a team that cannot move it.
- Scores affected: K7=2 (IN1 set)
- Suggested rewrite: drop IN1.3 from IN1 and, if the rating matters, land it on Courier's CR1 as "KR CR1.3: Driver-app App Store rating 4.1 → 4.6 (App Store Connect)"; replace it on IN1 with "KR IN1.3: Weekly leadership questions answered from the exec suite without an analyst re-run `<baseline>` → `<target>` (Looker usage stats)." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Why it's a problem: the page's own convention is "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (line 76) and every other Insights KR names a person (Halima D., Vik M.), so "Owner: TBD" is an unfilled slot rather than an inherited owner — and this is the KR that has to pull seven other squads onto v3 conventions, the hardest cross-team ask on the page.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named Insights individual>`."

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: all four objectives carry the same top label — "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95); "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99); "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103); "Objective AC4 (Priority: P0): Billing runs itself" (line 107).
- Evidence: "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: uniform P0 labels across four objectives and eight KRs encode no trade-off, so when the quarter gets tight the sequencing decision is made implicitly by whoever is loudest — and this set already contains a declared internal collision (the portal in AC3.2 waits on the AC4.2 billing migration), exactly the call a priority order is supposed to settle in advance.
- Scores affected: none — AP-05 is a set-level defect; no O1–K7 dimension scores prioritisation.
- Suggested rewrite: "P0: AC2 Support answers arrive before customers ask twice (worst current number on the page: open escalation backlog 210). P1: AC1 New customers reach first value in days, not weeks; AC3 Customers trust the delivery promises we report. P2: AC4 Billing runs itself — the billing-system migration continues as planned work, and AC3.2's portal is funded only after it lands."

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: the three KRs form a closed cycle — Courier → Core Systems → Insights → Courier — so no team can start first; as written the quarter ends with all three KRs at their baselines, and because CR3, CS3 and IN2 all claim C4, the company's telemetry-consolidation priority sits entirely inside the loop.
- Detection check that fired: AL-11 structural check — dependency graph built from the "once/after" phrases in the three KRs; cycle detection returns the three-edge cycle Courier → Core Systems → Insights → Courier.
- Disconfirming checks run: (1) Cycle ≠ deadlock, hard blocking vs. soft preference — each edge re-read ("once Core Systems GAs the SDK", "after Insights validates event schema v3 in production", "after Courier instruments the new driver-app event stream"); all three are hard conditionals, none hedged with soft-preference wording such as `ideally` or `would benefit from` — does not kill. (2) Staged-milestone interleaving — Core Systems' notes offer a pre-GA build, "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70), but Courier's KR conditions on GA specifically and Courier's notes add only "SDK timing per Core Systems' plan." (line 49), so no interleaving exists as written; the check weakens the cycle's inevitability without killing it, and supplies the fix below. (3) Awareness plus a resolution plan — each team's notes show awareness of its own upstream edge only; no page names the cycle or a plan to break it, so no downgrade to Minor.
- Inference labels: none — all three edges are quoted verbatim; no edge is inferred.
- Verdict: CONFIRMED (all load-bearing quotes re-read character-for-character against lines 46, 67, 84, 70 and 49)
- Recommended resolution owner: Core Systems lead convenes Courier and Insights in week 1 — agree that Courier instruments against the code-complete pre-GA SDK v1 so instrumentation → schema-v3 validation → GA runs in that order, and restate the agreed sequence on CR3.1, CS3.1 and IN2.1 before the first check-in.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two measurements — different numerator (jobs completed within the window vs. deliveries scanned at the destination), different denominator (completed jobs vs. all scheduled deliveries including cancellations), different cadence (weekly vs. monthly) and different system (Ops Console vs. Billing warehouse). Both roll up to the same company promise, "keeping the delivery promises we report to customers" (line 11), so an exec reading "On-time delivery rate" gets 91% or 78% depending on which page is open, and the two targets (95% and 85%) are not comparable. The definition split also explains the baseline gap, so AL-09 Baseline disagreement is cross-referenced here as secondary rather than filed separately for this metric.
- Detection check that fired: AL-08 heuristic, form (a) — metric-name blocking: "On-time delivery rate" appears in two teams' KRs; each team's stated definition (formula, window, population, data source) was diffed.
- Disconfirming checks run: (1) Different wording ≠ different definition — both definitions normalised before diffing; they do not reduce to one measurement (populations differ by cancellations and by scheduled-vs-completed, and the instruments differ), so the check does not kill. (2) Superseded page version — searched all five team sections, the company priorities page and the Q4 review appendix for a glossary or shared definition of "on-time"; none exists, and the closest text, "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31), asserts Dispatch's own methodology rather than a company one. Page dates checked: Dispatch last updated 2027-01-04 (line 18), Accounts 2027-01-08 (line 92); neither supersedes a shared definition, because there is none. (3) AL-09 pre-check — the 13-point baseline gap is explained by the definition split, so this is reported as AL-08 per the AL-09 heuristic.
- Inference labels: none — both definitions and the company promise are quoted verbatim.
- Verdict: CONFIRMED (both definition strings re-read character-for-character against lines 26 and 104)
- Recommended resolution owner: the C2 owner (Noor E., CEO) with the Dispatch and Accounts leads: by week 2, either adopt one company definition of "On-time delivery rate" and restate both KRs against it, or rename them distinctly (e.g. `dispatch on-time rate` and `delivery on-time rate`) and state which one C2's customer-facing promise reporting uses.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same instrument and the same period carry two current values eight points apart, and Accounts explicitly labels its number the "Q4 2026 baseline"; if the review's 78 is right, AC2.2 is a +12 ask presented as a +4 one, on a committed KR under a P0 objective serving a named C2 driver.
- Detection check that fired: AL-09 heuristic — the metric catalogue collected every stated baseline for "Customer CSAT"; two values for the same metric and period differ beyond rounding.
- Disconfirming checks run: (1) Different as-of dates — both statements name Q4 2026, and no other CSAT reading exists in the corpus, so dates do not explain the gap. (2) Different populations or definitions (AL-08 pre-check) — both cite the "quarterly relationship survey"; neither page states a segment, region or respondent split and no glossary exists; all five team sections and the appendix were searched for a second CSAT definition with no hit, so a definitional explanation was looked for and not found. (3) Control check on the corpus's other two shared baselines, which agree and isolate CSAT as the disagreement: "Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3)." (line 40) against "Driver-app weekly retention averaged 71% across Q4 (Amplitude)." (line 119), and "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (line 58) against "Sev-1 incidents in Q4: 9 (incident review)." (line 120).
- Inference labels: none — both baseline statements and both control baselines are quoted verbatim.
- Verdict: CONFIRMED (both quotes re-read character-for-character against lines 101 and 118)
- Recommended resolution owner: Accounts lead with the Q4 review owner: agree the Q4 2026 CSAT figure before the quarter's first check-in, re-cut AC2.2's target from the agreed number, and state the survey population on the OKR page.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), committed under the page convention "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19), and dependent per "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31).
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), explicitly labelled "(stretch — only if the billing migration lands early)" (line 105) and echoed in the team's notes: "Portal timing depends on how fast the billing migration goes (see AC3.2)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111).
- Conflict: a committed Dispatch KR depends wholly on a deliverable its producer lists as conditional stretch, and the arithmetic compounds the mismatch — Accounts commits the portal only to "the first 40 partner accounts" while Dispatch's number needs 600 enterprise trial starts to flow through it. If the billing migration runs late, Dispatch loses a committed KR for a reason entirely outside its control.
- Detection check that fired: AL-12 heuristic — on an acknowledged dependency edge (Dispatch → Accounts, partner portal), commitment labels compared across sides (committed-by-convention vs. explicit stretch) and target arithmetic compared (600 trial starts vs. a 40-account rollout).
- Disconfirming checks run: (1) Missing label ≠ mismatch — both teams state a labelling scheme (lines 19 and 93), so the asymmetry is a real difference in declared commitment, not one team's silence; does not kill. (2) Consumer already discounts or hedges the dependence — Dispatch's page was searched for a hedge: the note "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31) asserts the assumption rather than discounting it, and DS2.2 carries no reduced or conditional target; no downgrade. (3) Producer committed elsewhere — the Accounts section was searched for any non-stretch portal item; AC3.2 is the only portal commitment on the page.
- Inference labels: none — both commitment labels, both targets and both notes are quoted verbatim.
- Verdict: CONFIRMED (all load-bearing quotes re-read character-for-character against lines 19, 27, 31, 105 and 111)
- Recommended resolution owner: Accounts lead (portal owner) with the Dispatch lead, in week 1: either promote the portal to a committed AC3.2 with a scope that can carry 600 trial starts, or re-cut DS2.2 to a target Dispatch can hit without the portal and move the portal-dependent number to a stretch KR.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "Objective CS2: Ship with confidence" (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), linked as "(supports C2 — enterprise churn)" (line 61), with KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64).
- Company priority evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the link is decorative — none of CS2's three KRs measures logo churn or any of the three drivers C2 names, and all three could be fully achieved in a quarter where enterprise churn worsens. The KRs are committed under the team's own convention, "Commitment: KRs are committed unless marked (stretch)." (line 55), which is what lifts this above a labelling nit: a committed company priority is showing a contributor that is not contributing, while the drivers C2 does name sit unclaimed by this team.
- Detection check that fired: AL-05 heuristic — explicit parent link present ("supports C2 — enterprise churn"); mechanism check run against the parent's metric and its named drivers; all three child KRs are internal delivery proxies with no stated causal path to churn.
- Disconfirming checks run: (1) Activity KRs ≠ decorative link — the parent's own text (line 11) was searched for named contributing workstreams: it names onboarding time-to-value, the escalation backlog and delivery promises, all three claimed by Accounts (AC1, AC2, AC3 on lines 95, 99, 103) and none a Core Systems deliverable. (2) Mechanism stated elsewhere on the child's page — Core Systems' notes read "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." (line 70): no churn mechanism, and the only strategy claim there is C4; no linked epics or backlog exist in this corpus to search. Neither check kills the finding. (3) Contrast control — CS1 and CS3's C4 links survive the same mechanism check (CS1.2 restates C4's own metric), so the failure is specific to CS2.
- Inference labels: analyst inference — the judgement that deploy frequency, change-failure rate and CI pipeline time would not plausibly move enterprise logo churn. The absence of any stated mechanism is a recorded search over the quoted pages, not an inference.
- Verdict: CONFIRMED (all load-bearing quotes re-read character-for-character against lines 11, 55, 61, 62, 63, 64 and 70)
- Recommended resolution owner: Core Systems lead with the C2 owner (Noor E., CEO) by week 3: either re-anchor CS2 to C4, where its reliability and cost work already lands, or add one KR measuring a C2-named driver — for example incident-driven escalations arriving in the Accounts backlog — so the claimed support shows up in a number.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to break the telemetry cycle by instrumenting against the code-complete pre-GA SDK, then restate the agreed order on CR3.1, CS3.1 and IN2.1 — owner: Core Systems lead (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with an explicit denominator and measurement window before the first check-in — owner: Dispatch lead (resolves §3 AP-13 Ambiguous Denominator).
3. Decide whether the partner portal is committed or stretch, and re-cut whichever of DS2.2 / AC3.2 loses the argument — owner: Accounts lead with Dispatch lead (resolves §4 AL-12 Commitment asymmetry).
4. Adopt one company definition of "On-time delivery rate" — or two distinct names — and state which one C2's promise reporting uses — owner: Noor E. (CEO) as C2 owner (resolves §4 AL-08 Terminology collision).
5. Reconcile the Q4 2026 CSAT figure (78 vs 86) and re-cut AC2.2 from the agreed baseline — owner: Accounts lead with the Q4 review owner (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring a C2-named churn driver — owner: Core Systems lead (resolves §4 AL-05 Cascade drift).
7. Rank the four Accounts objectives P0/P1/P2 and record the portal-vs-migration sequencing decision — owner: Accounts lead (resolves §3 AP-05 Everything Is a P0).
8. Restate CR2.1 as an aspirational target with a named lever plus a committed leading KR, and add the commitment convention to the Courier page — owner: Courier lead (resolves §3 AP-07 Unmoored Moonshot and §3 AP-08 Committed vs Aspirational Not Labeled).
9. Rewrite the CS1 objective so it names the change its two KRs already pay for — owner: Core Systems lead (resolves §3 AP-10 BAU Dressed as OKR).
10. Move the driver-app App Store rating KR to Courier and name an accountable individual on IN2.2 — owner: Insights lead (resolves §3 AP-12 Orphan KR and §3 AP-15 Ownerless KR).

## 6. Suggested single-team re-runs

- **Dispatch** (Critical finding AP-13 Ambiguous Denominator; roll-up C (2.51)): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: the 'Dispatch team — Q1 2027' section of `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-candidate-cbdeba3/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (Critical finding AL-11 Circular dependency; roll-up B (3.25)): re-run single-team mode — "Review the Courier team's (driver app) Q1 2027 OKRs alone, in depth. Source: the 'Courier team (driver app) — Q1 2027' section of `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-candidate-cbdeba3/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (Critical finding AL-11 Circular dependency; roll-up B (3.04)): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: the 'Core Systems team — Q1 2027' section of `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-candidate-cbdeba3/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (Critical finding AL-11 Circular dependency; roll-up B (3.29)): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: the 'Insights team — Q1 2027' section of `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-candidate-cbdeba3/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.47), above the needs-rework threshold, and no Critical finding.
