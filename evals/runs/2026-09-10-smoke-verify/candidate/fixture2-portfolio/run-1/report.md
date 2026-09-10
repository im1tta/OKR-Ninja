# Coppervale — Q1 2027 OKR portfolio review

*Scope (confirmed at intake): 5 teams — Dispatch, Courier, Core Systems, Insights, Accounts — period Q1 2027, portfolio mode. Source corpus: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (local export; no Atlassian connection). Strategy source in scope: the file's "Company Q1 2027 priorities" section (Confluence page 91050). Source refs below abbreviate that path to `input/sample-portfolio-2.md`; line numbers refer to it exactly as it is.*

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 3 Minor findings.
The portfolio's biggest threat is AL-11 Circular dependency: Core Systems' SDK GA waits on Insights' schema validation, which waits on Courier's instrumentation, which waits on Core Systems' GA — the entire C4 telemetry programme has no valid execution order as written.
Two teams also report the same company metric, "On-time delivery rate", under two different formulas 13 points apart (AL-08 Terminology collision), and Accounts' committed CSAT KR is calibrated on a baseline the company's own Q4 review contradicts (AL-09 Baseline disagreement).
No goodness anti-pattern repeats — each of the eight per-team findings is a distinct AP-ID — so the most consequential is the only Critical one: AP-13 Ambiguous Denominator (Dispatch's "failure rate" KR, scoreable at any value the team likes).
Quality is otherwise high by portfolio standards: every KR names a system of record, and all four company priorities have at least one committed team objective behind them.
Recommended first action: Core Systems convenes Insights and Courier in week 1-2 to break the telemetry cycle before any of the three teams' C4 KRs can start.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 4 | 3 | 3 | 3 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.5) · Core Systems B (3.0) · Courier B (3.2) · Insights B (3.4) · Accounts A (3.5).

- Dispatch: K6=2 — DS1's two KRs are both end-state truths; no mid-cycle steering signal.
- Core Systems: O1=2 — CS1 states standing duty, not a change (AP-10 BAU Dressed as OKR).
- Courier: K3=2 — CR2.1's 15x referral-install target carries no mechanism (AP-07 Unmoored Moonshot).
- Insights: K7=2 — IN1.3's App Store rating serves no part of IN1 (AP-12 Orphan KR).
- Accounts: K3=2 — AC2.2's CSAT baseline is contradicted by the Q4 review (AL-09 Baseline disagreement).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never states its population — failed jobs as a share of dispatched jobs, failed route builds, failed deliveries, or failed API calls all read plausibly on a dispatch page and each yields a different number, so the KR can be reported as hit or missed at will. The team's neighbouring KR spells its denominator out — "jobs completed within the promised window as a share of all completed jobs" (input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26) — so the omission is not a page convention.
- Scores affected: K1=1, K5=2
- Suggested rewrite: "KR DS2.4: Job failure rate — jobs ending in a failed state as a share of all jobs dispatched, measured weekly in `<named Ops Console view>` — 6% → 3% by end of Q1." (6% and 3% quoted from the corpus; denominator and source are OKR-Ninja proposals) [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (input/sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 21)
- Evidence: "Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS")." (input/sample-portfolio-2.md › Objective DS1 › line 22) and "Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view)." (input/sample-portfolio-2.md › Objective DS1 › line 23)
- Why it's a problem: two *and*-joined end-states with disjoint audiences — today's enterprise dispatchers, and two markets Coppervale is not in yet — and the KRs split cleanly into one per clause, so each end-state is carried by a single KR and the objective can be reported as a hit while half of it failed.
- Scores affected: O2=2, K6=2, K7=3
- Suggested rewrite: split into "Objective DS1a: Enterprise dispatchers would fight to keep Coppervale" (KR: "Enterprise dispatcher NPS 24 → 40", plus a leading KR such as weekly active dispatch seats `<baseline>` → `<target>`) and "Objective DS1b: Coppervale is a real option for DE and FR fleets" (KR: "Signed pilot customers in DE and FR: 0 → 6", plus qualified DE/FR fleet evaluations `<baseline>` → `<target>`). [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (input/sample-portfolio-2.md › Objective CS1: Continue running the platform smoothly for every team › line 57)
- Evidence (the KRs beneath it): "Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4." (input/sample-portfolio-2.md › Objective CS1 › line 58) and "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." (input/sample-portfolio-2.md › Objective CS1 › line 59)
- Why it's a problem: the objective commits the team to continuing its standing job and names no change at all — "smoothly" is the state the platform is already claimed to be in, not a direction — which is AP-10's path (a); the two genuine deltas quoted above sit in the KRs and, per the rubric, deltas in the KRs never rescue a standing-duty objective. As written, CS1 is achieved by default staffing and displaces a goal that would not be.
- Scores affected: O1=1, O2=2, O3=2
- Suggested rewrite: "Objective CS1: No team's quarter is interrupted by our platform, and every delivery costs less to run — KR: Sev-1 incidents per quarter 9 → ≤ 4; KR: Cloud cost per completed delivery $0.42 → $0.30." (KR numbers quoted from the corpus; the objective text is OKR-Ninja's proposal)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the only "how" on the page): "referral growth is our big swing this quarter." (input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target in a single quarter with no named lever, no intermediate milestone and no resourcing signal — "big swing" states emphasis, not mechanism — so the number functions as decoration rather than a goal, and nothing on the page marks it aspirational (see AP-08 below).
- Scores affected: K3=1, K6=0
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via `<named referral lever>`; KR CR2.2 (committed): drivers sending at least one referral invite `<baseline>` → `<target>` per week (App Store + Play attributed installs)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (Courier's page header, which carries no commitment convention): "*Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06*" (input/sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36)
- Evidence (what the other four pages carry): "*Commitment: KRs are committed unless marked (stretch).*" (input/sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19; identically at line 55 Core Systems, line 76 Insights, line 93 Accounts)
- Evidence (targets that vary wildly in stretch, unlabeled): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (input/sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) against "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (input/sample-portfolio-2.md › Objective CR2 › line 43)
- Search performed for the absence claim: all five team pages (lines 17–111) and the company priorities page (lines 7–13) were read for the terms `committed`, `commitment`, `aspirational`, `stretch` and `P0`. Four team pages state the convention on their header line; Courier's header (lines 35–37) states none, and no `stretch` or `aspirational` marker appears on any Courier KR (lines 38–49).
- Why it's a problem: the set mixes a 0.4-point reliability must-hit with a 15x bet and labels neither, so expected attainment cannot be computed and CR2.1's ambition has no anchor to be judged against — exactly the corruption AP-08 describes.
- Scores affected: K3=1 on CR2.1 (calibration left unanchored)
- Suggested rewrite: add to the Courier page header "Commitment: KRs are committed unless marked (stretch)." and relabel "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter". [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its stated objective): "Objective IN1: Execs run Monday mornings from our dashboards" (input/sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 78)
- Why it's a problem: there is no causal chain in two steps or fewer from the driver app's public store rating to leadership using Insights' dashboards; the KR shares no noun, audience, surface or data source with its objective, and the outcome it measures belongs to the Courier team's app. Hitting it would not move IN1 at all.
- Scores affected: K7=2
- Suggested rewrite: move the store rating to Courier's driver-app objective and replace with "KR IN1.3: Monday leadership reviews run from the exec suite `<baseline>` → `<target>` of the quarter's 13 weeks (Looker usage stats)." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own convention): "*Commitment: KRs are committed unless marked (stretch). Owners listed per KR.*" (input/sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page states that owners are listed per KR and every other Insights KR names one, so "Owner: TBD" is a gap rather than a house style — and it lands on the one KR whose delivery depends on nine other squads cooperating, leaving the set's hardest coordination with nobody accountable for it.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named Insights individual>`, with the adopting engineer named per squad in the onboarding tracker." [proposal]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (input/sample-portfolio-2.md › Objective AC1 (Priority: P0): New customers reach first value in days, not weeks › line 95); "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99); "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103); "Objective AC4 (Priority: P0): Billing runs itself" (line 107)
- Evidence (the team's own statement of the trade-off it declines to make): "every one of these is P0 for us this quarter — we're not choosing." (input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry the identical top label and the notes confirm the refusal to rank, so the set encodes no trade-off; when the quarter tightens, the eight KRs get triaged by whoever escalates loudest instead of by a stated priority — and one P0 objective depends on a stretch KR another team has committed against (see §4 AL-12 Commitment asymmetry).
- Scores affected: set-level instance — prioritization is not an O1–K7 dimension, so no dimension score moves; the defect is that Accounts' A (3.5) roll-up overstates how executable this set is.
- Suggested rewrite: "Objective AC1 (Priority: P0) … Objective AC2 (Priority: P1) … Objective AC3 (Priority: P1) … Objective AC4 (Priority: P2 — only AC4.1 is a Q1 commitment; the migration continues at current staffing)." [proposal]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Core Systems ↔ Insights ↔ Courier
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (input/sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Conflict: each KR is gated on the next team's completion — Core Systems waits on Insights, Insights waits on Courier, Courier waits on Core Systems. No valid execution order exists as written, so all three of the portfolio's C4 telemetry KRs are unstartable on their own terms.
- Detection check that fired: graph-structural cycle detection on the dependency map (AL-11) — edges built from the `after…`, `after…`, `once…` phrases, cycle Courier → Core Systems → Insights → Courier.
- Disconfirming checks run: hard-blocking vs soft preference — all three edges are hard conditionals (`after`, `after`, `once`), none reads `ideally` or `would benefit from`, so no edge is soft; staged-milestone interleaving — Core Systems' note "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (input/sample-portfolio-2.md › Objective CS3 › line 70) shows a possible break (instrumenting against the code-complete build), but Courier's KR conditions on GA rather than code-complete, so no interleaving exists in the text as written — the check weakens the finding's inevitability, not the cycle; awareness plus resolution plan — Insights' "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (line 87) and Courier's "SDK timing per Core Systems' plan." (line 49) show each team sees its own inbound edge, but no team's text shows awareness of the loop or names a break, so no downgrade applies.
- Inference labels: none — all three edges quoted verbatim from the KRs themselves.
- Verdict: CONFIRMED (each edge quote re-fetched and matched character-for-character against its line)
- Recommended resolution owner: Core Systems lead (Adaeze O.) convenes Insights and Courier in the first two weeks of Q1 to choose the break point — the quotable candidate is Courier instrumenting a subset of flows against the code-complete SDK so Insights can validate v3 and Core Systems can then GA — and all three KRs are restated with the agreed sequence and dates.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Company-priority context: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: one metric name carries two formulas, two populations, two windows and two systems of record — completed jobs weekly from the Ops Console versus all scheduled deliveries including cancellations monthly from the Billing warehouse — which is why the two baselines sit 13 points apart (91% vs 78%). C2 asks the company to be judged on "the delivery promises we report to customers" using a number that means two different things to the two teams that report it.
- Detection check that fired: AL-08 form (a) — metric name used by two or more teams; each team's definition hunted on its own page and diffed on formula, window, population and data source.
- Disconfirming checks run: normalize-before-diffing — the definitions do not reduce to the same measurement (numerator events differ: "jobs completed within the promised window" vs "deliveries scanned at the destination inside the promised window"; denominators differ on cancellations; weekly vs monthly; Ops Console vs Billing warehouse), so the collision is real and not verbal drift; superseded-page check — no glossary or shared-definition page exists in the corpus and both pages are current (Dispatch "Last updated 2027-01-04", Accounts "Last updated 2027-01-08"), so neither definition supersedes the other; AL-09 pre-check — the 91%/78% baseline gap is fully explained by the definition split, so this is filed as AL-08 with AL-09 Baseline disagreement cross-referenced as the secondary ID rather than double-counted.
- Inference labels: none — both definitions quoted verbatim; the 13-point gap is arithmetic on the two quoted baselines.
- Verdict: CONFIRMED (both definitions re-fetched and matched character-for-character)
- Recommended resolution owner: Noor E., owner of the company priorities page that reports the promise metric, rules on one canonical definition (naming numerator event, denominator, window and system of record) before the first monthly business review; Dispatch and Accounts then restate DS2.1 and AC3.1 against it, keeping their own baselines only if the chosen definition preserves them.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (input/sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), committed under the page rule "*Commitment: KRs are committed unless marked (stretch).*" (input/sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures *(stretch — only if the billing migration lands early)*." (input/sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105)
- Conflict: Dispatch's committed KR is built on a deliverable Accounts marks stretch and conditions on the billing migration landing early; and the arithmetic assumes not just that the portal ships but that it scales — 600 enterprise trial starts through a portal Accounts scopes to "the first 40 partner accounts".
- Detection check that fired: AL-12 edge label comparison on an acknowledged dependency — Dispatch's notes acknowledge the edge ("DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter.", input/sample-portfolio-2.md › Objective DS2 › line 31), so AL-01 does not apply; comparing commitment labels across the edge then shows committed against stretch.
- Disconfirming checks run: labeling-vocabulary check — both teams state the identical convention line ("KRs are committed unless marked (stretch)", lines 19 and 93), so the mismatch is a real difference in commitment level, not two vocabularies; consumer-hedging check — Dispatch's note assumes the launch rather than discounting it, DS2.2 carries no stretch marker and no partial-portal fallback, and Accounts reinforces the conditionality ("Portal timing depends on how fast the billing migration goes (see AC3.2).", input/sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111), so no hedge kills or downgrades the finding.
- Inference labels: the scale coupling (600 trial starts sourced from a portal live for 40 partner accounts) is analyst inference from the two quoted numbers — no document states the conversion assumption; the commitment mismatch itself is quoted, not inferred.
- Verdict: CONFIRMED (both KR quotes and both convention lines re-fetched and matched character-for-character)
- Recommended resolution owner: Accounts lead (Georg B.) and Dispatch lead (Mei L.) decide by end of week 2 either to promote AC3.2 to committed with the billing migration resequenced behind it, or to re-label DS2.2 as stretch and re-baseline Dispatch's trial-start commitment on channels that do not depend on the portal.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (input/sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (input/sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, from the same named instrument, as of the same period, is stated eight points apart. If the Q4 review is right, AC2.2 is a +12 ask rather than the +4 it reads as — the team's committed satisfaction target is calibrated on a starting point the company's own review contradicts, and nobody can tell mid-quarter whether it is on track.
- Detection check that fired: AL-09 metric-catalog baseline collection — every stated baseline per canonical metric compared; the canonical metric `Customer CSAT` appears twice for Q4 2026 with different values.
- Disconfirming checks run: as-of-date check — both statements name Q4 2026, so no timing explanation exists; definition/population check first (per AL-08 precedence) — both name the "quarterly relationship survey"; the review adds only its sample size ("n = 412") and no different population or formula, and no other CSAT definition appears anywhere in the corpus (all five team pages and the priorities page were searched for `CSAT` and `satisfaction`), so no definitional split explains the gap.
- Inference labels: none — both values, both instruments and both as-of periods quoted verbatim.
- Verdict: CONFIRMED (both statements re-fetched and matched character-for-character)
- Recommended resolution owner: Accounts lead (Georg B.) reconciles the two figures with the owner of the Q4 review (page 91031) before the KR is locked in week 1; if 78 stands, AC2.2 is restated as "Customer CSAT 78 → `<target>` (quarterly relationship survey)". [proposal — placeholder target]

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priorities (C2)
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (input/sample-portfolio-2.md › Objective CS2: Ship with confidence › line 61), with all three of its KRs: "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63), "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64) — committed under "*Commitment: KRs are committed unless marked (stretch).*" (input/sample-portfolio-2.md › Core Systems team — Q1 2027 › line 55)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (input/sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the child claims C2 explicitly, but none of its three KRs measures churn or any of the three drivers C2 names — they are internal delivery-throughput metrics, and all three could be hit in full in a quarter where enterprise churn worsens. The link is decorative, and because C2 is a committed company priority the claim also credits Core Systems with churn work no KR is doing.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — do the child's KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's page names as needed? All three fail.
- Disconfirming checks run: parent-page contributor list — C2 enumerates its drivers ("onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers") and Core Systems' delivery throughput is not among them; child's own justification — Core Systems' notes claim only the cost work ("The cost work is our C4 commitment.", input/sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 70) and say nothing about churn; documented driver relationship elsewhere — no page in the corpus links deploy frequency, change-failure rate or CI time to churn or to any C2 driver.
- Inference labels: none — the parent's driver list and all three child KRs are quoted; no mechanism is asserted beyond what the quotes contain.
- Verdict: CONFIRMED (parent and all child quotes re-fetched and matched character-for-character)
- Recommended resolution owner: Core Systems lead (Adaeze O.) re-anchors CS2 to C4, where the team's own notes place its commitment, or adds one KR measuring an enterprise-visible reliability outcome that the C2 owner accepts as a churn driver — decided before the objective reaches the exec rollup.

### [Minor] AL-05 Cascade drift: Courier ↔ Company priorities (C3)
- Courier evidence: "Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)*" (input/sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 42), whose only KR is "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43)
- Company evidence: "**C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80% across FY27." (input/sample-portfolio-2.md › Company Q1 2027 priorities › line 12)
- Conflict: C3's metric is weekly retention; CR2's single KR counts newly attributed installs. Achieving it moves an acquisition number that the parent does not measure, and a 15x install surge would plausibly dilute the weekly-retention cohort with low-intent drivers — the objective can be fully achieved in a quarter where the parent metric moves the wrong way.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child's KR measures neither the parent's metric nor a documented driver of it nor a deliverable C3's page names.
- Disconfirming checks run: parent-page contributor list — C3 names no workstreams or contributing deliverables at all; child's own justification — Courier's notes offer only "referral growth is our big swing this quarter." (input/sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49), which states priority, not a path to retention; documented driver relationship — nothing in the corpus links referral installs to retention; near-miss that downgrades the finding — Courier's CR1.2 does measure the parent metric ("Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3).", input/sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 40), so C3 is not left unserved — only CR2's claim on it is decorative, which is why this is Minor.
- Inference labels: the install-surge → retention-dilution mechanism is analyst inference; no Coppervale document states that tradeoff.
- Verdict: CONFIRMED (both sides' quotes re-fetched and matched character-for-character)
- Recommended resolution owner: Courier lead (Tomás R.) either pays for the C3 claim with a retention KR on referred drivers — "week-4 retention of referral-sourced drivers `<baseline>` → `<target>`" [proposal — placeholder target] — or drops the "(supports C3)" label and asks the CEO to fund CR2 as an acquisition bet no current company priority covers.

## 5. Prioritized action list

1. Convene Core Systems, Insights and Courier to pick a break point in the telemetry sequence and restate all three KRs — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-11 Circular dependency).
2. Define the denominator and system of record for the failure-rate KR before Dispatch's OKRs are locked — owner: Dispatch lead (Mei L.) (resolves §3 AP-13 Ambiguous Denominator).
3. Rule on one canonical "On-time delivery rate" definition and restate DS2.1 and AC3.1 against it — owner: Noor E. (company priorities page) (resolves §4 AL-08 Terminology collision, and its secondary AL-09 Baseline disagreement).
4. Reconcile the two Q4 2026 CSAT baselines (86 vs 78) and re-baseline AC2.2 — owner: Accounts lead (Georg B.) (resolves §4 AL-09 Baseline disagreement).
5. Decide whether the partner portal is committed or Dispatch's DS2.2 becomes stretch — owner: Accounts lead (Georg B.) with Dispatch lead (Mei L.) (resolves §4 AL-12 Commitment asymmetry).
6. Re-anchor CS2 to C4 or add a KR measuring a churn driver C2 names — owner: Core Systems lead (Adaeze O.) (resolves §4 AL-05 Cascade drift: Core Systems ↔ Company priorities (C2)).
7. Rank Accounts' four objectives and name the one that yields when the quarter tightens — owner: Accounts lead (Georg B.) (resolves §3 AP-05 Everything Is a P0).
8. Split CR2.1 into an aspirational referral target plus a committed leading KR, and add a commitment convention to the Courier page — owner: Courier lead (Tomás R.) (resolves §3 AP-07 Unmoored Moonshot, §3 AP-08 Committed vs Aspirational Not Labeled, and pays for §4 AL-05 Cascade drift: Courier ↔ Company priorities (C3)).
9. Name an accountable owner for IN2.2 and move the App Store rating KR to Courier — owner: Insights lead (Halima D.) (resolves §3 AP-15 Ownerless KR, §3 AP-12 Orphan KR).
10. Rewrite CS1 as a change statement and split DS1 into its two end-states — owner: Core Systems lead (Adaeze O.) and Dispatch lead (Mei L.) (resolves §3 AP-10 BAU Dressed as OKR, §3 AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.5); Critical AP-13 Ambiguous Denominator — qualifies under criterion (b)): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91112 (DSP-OKR-Q1), section 'Dispatch team — Q1 2027' of the local export `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (lines 17–31); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27), lines 7–13 of the same export."
- **Core Systems** (roll-up B (3.0); party to Critical AL-11 Circular dependency — qualifies under criterion (b)): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91120 (CORE-OKR-Q1), section 'Core Systems team — Q1 2027' of the local export `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (lines 53–70); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27), lines 7–13 of the same export."
- **Insights** (roll-up B (3.4); party to Critical AL-11 Circular dependency — qualifies under criterion (b)): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91124 (INS-OKR-Q1), section 'Insights team — Q1 2027' of the local export `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (lines 74–87); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27), lines 7–13 of the same export."
- **Courier** (roll-up B (3.2); party to Critical AL-11 Circular dependency — qualifies under criterion (b)): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: Confluence page 91116 (COUR-OKR-Q1), section 'Courier team (driver app) — Q1 2027' of the local export `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture2-portfolio/input/sample-portfolio-2.md` (lines 35–49); strategy doc: 'Company Q1 2027 priorities' (Confluence page 91050, CO-PRIO-Q1FY27), lines 7–13 of the same export."
- **Accounts** does not qualify: roll-up A (3.5), above the needs-rework threshold, and no Critical finding (its four findings are Major or below).
