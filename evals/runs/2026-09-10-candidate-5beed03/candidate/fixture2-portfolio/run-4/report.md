# Coppervale — Q1 2027 OKR portfolio audit

**Scope (confirmed at intake).** Mode: **portfolio** (5 teams in scope → 2+ teams). Teams enumerated from the export's team sections: Dispatch, Courier (driver app), Core Systems, Insights, Accounts (billing & customer success). Period: **Q1 2027**, as stated by the file. Source: one local file, `sample-portfolio-2.md` (a Confluence export; no Atlassian connection available, so Jira/Confluence lookups were not possible and every absence claim below is scoped to this file). Strategy source: the file's **Company Q1 2027 priorities** section (Confluence page 91050, CO-PRIO-Q1FY27), which enables strategy tracing and O4 scoring. Line numbers in source refs refer to `sample-portfolio-2.md`.

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; **2 Critical, 9 Major, 3 Minor** findings.
The single worst alignment risk is **AL-11 Circular dependency**: Courier, Core Systems and Insights each gate their telemetry KR on one of the other two ("once Core Systems GAs the SDK" → "after Insights validates event schema v3" → "after Courier instruments the new driver-app event stream"), so no execution order exists as written and all three KRs can fail while every team does exactly what its page says.
Goodness anti-patterns: **no anti-pattern repeats** — the eight §3 findings are eight distinct AP-XX instances across four teams — so there is no single most common one; the most consequential is **AP-13 Ambiguous Denominator** (Dispatch DS2.4 targets "the failure rate" of a population it never names).
Two numbers that reach executives do not agree with the company's own pages: the on-time delivery rate metric carries two incompatible definitions and baselines across Dispatch and Accounts (AL-08), and Accounts' stated Q4 2026 CSAT baseline is 8 points above the Q4 business review's (AL-09).
Dispatch has the weakest set (C, 2.5) and the only Critical goodness finding; Accounts scores best (A, 3.5) but labels all four of its objectives P0 (AP-05), so its page encodes no trade-off.
Core Systems' "Ship with confidence" claims the enterprise-churn priority whose own text names three other drivers, none of them Core Systems' (AL-05).
Recommended first action: Core Systems convenes Courier and Insights in week 1 to break the telemetry cycle at one edge (pre-GA SDK beta, validated on the instrumented subset).

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 2 | 3 |
| Core Systems | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 4 | 3 | 3 | 4 | 3 | 2 | 3 | 3 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.5) · Core Systems B (3.1) · Courier B (3.3) · Insights B (3.4) · Accounts A (3.5).

- Dispatch: K3=2 — DS2.4's 6%→3% sits on a population the KR never names (AP-13).
- Core Systems: O1=2, O2=2 — "Continue running the platform smoothly" and "Ship with confidence" name no change.
- Courier: K3=2 — referral installs 3,000 → 45,000 is 15x with no stated mechanism (AP-07).
- Insights: K7=2 — an App Store rating KR sits under an exec-dashboard objective (AP-12).
- Accounts: K3=2 — CSAT target calibrated on 86 while the Q4 review states 78 (AL-09).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Why it's a problem: "the failure rate" never states its population — failed jobs as a share of jobs dispatched, of routes built, of deliveries attempted, or of API calls are all readable from the text and would give different numbers, so any of them can be claimed as 3%. The page defines a denominator for its neighbouring KR ("as a share of all completed jobs", line 26) and for this one it does not; the page note covers on-time delivery only ("On-time delivery is measured per our Ops Console methodology (see KR DS2.1).", line 31), and no other definition of a failure rate appears anywhere in the export.
- Scores affected: K1=1, K3=2, K5=2
- Suggested rewrite: "KR DS2.4: Failed dispatch jobs — jobs ending in a failed state as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions" (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 21)
- Why it's a problem: two "and"-joined end-states with disjoint audiences — today's enterprise dispatchers and two new geographies — and the KRs split cleanly along that seam ("Enterprise dispatcher NPS 24 → 40", line 22; "Signed pilot customers in DE and FR: 0 → 6", line 23), so hitting either KR leaves half the objective untouched and no single conversation covers the whole thing. "Delight" is also the kind of abstraction two readers gloss differently.
- Scores affected: O2=2, K6=2
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers recommend Coppervale to their peers. — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard 'Dispatcher NPS')." plus "Objective DS3: Coppervale wins its first paying dispatch customers in DE and FR. — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM 'Intl Pilots' view)." [proposal]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team" (sample-portfolio-2.md › Core Systems team — Q1 2027 › line 57)
- Why it's a problem: the objective commits the team to continuing its standing job — "Continue running the platform smoothly" names no direction, reduction, or improvement, nothing that differs from today — so it is achieved by default staffing and displaces a real goal. Per AP-10 the deltas in its KRs ("Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4", line 58) do not rescue a standing-duty objective; the objective is the thing the anti-pattern is about.
- Scores affected: O1=2, O2=2
- Suggested rewrite: "Objective CS1: Teams get a quieter and cheaper platform than they had in Q4. — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4. — KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard 'Unit Cost')." [proposal]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence: "referral growth is our big swing this quarter" (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target in one quarter with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — the only supporting text asserts importance ("our big swing"), which is not a mechanism — so the number functions as decoration rather than a goal, and CR2 has no second KR to steer by. Searched the Courier section (lines 35–49) and the whole export for a referral programme, incentive, campaign or headcount statement: none appears.
- Scores affected: K3=1, K6=0
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app 'invite a driver' reward shipping in week 3 (App Store + Play attributed installs). — KR CR2.2 (committed): Drivers sending at least one invite `<baseline>` → `<target>` per week (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36) — the Courier page header carries no commitment convention, unlike every other team page, e.g. "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Evidence: "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) sits unlabeled beside "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43)
- Why it's a problem: the set mixes a modest reliability floor with a 15x swing and never says which are must-hits, so expected attainment cannot be computed and the sandbag/moonshot judgment on every Courier KR is unmoored. Search recorded: every line of the export was searched for the terms `committed`, `aspirational`, `stretch` and `P0` — the convention appears on Dispatch (line 19), Core Systems (line 55), Insights (line 76) and Accounts (line 93), and `(stretch` appears once, on AC3.2 (line 105); nothing of the kind appears in the Courier section (lines 35–49).
- Scores affected: K3=2 (team aggregate — calibration judged without labels)
- Suggested rewrite: add to the Courier page header "Commitment: KRs are committed unless marked (aspirational)." and mark CR1.1, CR1.2, CR3.1 and CR3.2 committed and CR2.1 "(aspirational)". [proposal]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence: "Objective IN1: Execs run Monday mornings from our dashboards" (sample-portfolio-2.md › Insights team — Q1 2027 › line 78)
- Why it's a problem: there is no causal chain in two steps or fewer from a public app-store rating to executives running Monday mornings on Looker dashboards, and the KR shares no noun, surface or audience with its objective — it would be fully achieved in a quarter where no exec opens a dashboard. The rating belongs to the team that owns the driver app, whose objective is "Drivers finish every shift without fighting the app" (line 38).
- Scores affected: K7=2, K6=2
- Suggested rewrite: move the rating KR to Courier under CR1, and replace it with "KR IN1.3: Monday leadership sessions where every reported metric loads from the exec suite without a manual export `<baseline>` → `<target>` per quarter (Looker usage stats). Owner: Vik M." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence: "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: the page's own convention promises an owner per KR and every other Insights KR names one (Halima D. or Vik M., lines 79–84), so "Owner: TBD" leaves the one KR that requires nine other squads to change their instrumentation with nobody accountable for chasing them. Search recorded: the Insights section (lines 74–87) and the full export were searched for any other owner, DRI, or accountable name attached to IN2.2 — none exists.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights), with a named counterpart on each squad's page." [proposal]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks" (sample-portfolio-2.md › Accounts team (billing & customer success) — Q1 2027 › line 95); "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice" (line 99); "Objective AC3 (Priority: P0): Customers trust the delivery promises we report" (line 103); "Objective AC4 (Priority: P0): Billing runs itself" (line 107)
- Evidence: "Notes: every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four objectives and eight KRs carry one uniform top-priority label and the page says outright that no trade-off was made, so the set encodes no ranking — when the billing migration slips (which the same note says gates the portal), nothing on the page tells the team what to protect and what to drop.
- Scores affected: none of the eleven dimensions score prioritisation — this is a set-level defect recorded against the Accounts objective set as a whole (per the rubric's one-finding-per-instance rule, a set is its own instance)
- Suggested rewrite: "Objective AC1 (P0): New customers reach first value in days, not weeks. Objective AC2 (P1): Support answers arrive before customers ask twice. Objective AC3 (P1): Customers trust the delivery promises we report. Objective AC4 (P2): Billing runs itself — or move the billing migration to the programme plan and keep AC4.1 under AC1." [proposal]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: three KRs form a closed wait cycle — Courier waits on the SDK GA, the GA waits on schema-v3 validation, and validation waits on Courier's instrumentation. No valid execution order exists as written, so all three KRs (and the C4 telemetry-consolidation priority they serve) can fail in a quarter where every team does exactly what its page says.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — edges Courier→Core Systems ("once Core Systems GAs the SDK"), Core Systems→Insights ("after Insights validates event schema v3 in production"), Insights→Courier ("after Courier instruments the new driver-app event stream").
- Disconfirming checks run: hard-blocking vs soft preference — all three edges use hard sequencing words ("once", "after") and none is hedged with a soft preference such as `ideally` or `would benefit from`, so no edge is soft; staged-milestone interleaving — each page's notes were read for a staged plan ("Notes: SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." line 70; "Notes: schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." line 87; "SDK timing per Core Systems' plan." line 49) and each merely restates its own edge — no beta milestone, no subset validation, no interleaving is documented; awareness-plus-resolution-plan downgrade — awareness is present on all three pages, a resolution plan is not, so no downgrade applies.
- Inference labels: identifying Courier's "all 14 core driver flows with telemetry SDK v1" as the "new driver-app event stream" Insights waits on is analyst inference (it is the only driver-app instrumentation work anywhere in the export); the three sequencing edges themselves are quoted, not inferred.
- Verdict: CONFIRMED (all three edge quotes re-read against lines 46, 67 and 84 and matched character-for-character; surrounding notes checked for reversal)
- Recommended resolution owner: Core Systems (Adaeze O.) convenes Courier (Tomás R.) and Insights (Halima D.) in week 1 to break the cycle at one edge — ship the SDK to Courier as a pre-GA beta, let Insights validate schema v3 on the instrumented subset, and gate GA on that validation.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two formulas (completed jobs vs all scheduled deliveries including cancellations), two windows (weekly vs monthly) and two systems of record (Ops Console vs Billing warehouse). Both objectives report into the same company priority — "keeping the delivery promises we report to customers" (line 11) — so the on-time number an executive sees depends on which team's page was opened, and the 13-point baseline gap (91% vs 78%) is a definitional artefact rather than a measurement dispute. Rated Major because the colliding metric feeds a company-level rollup (C2).
- Detection check that fired: AL-08 form (a), same name / different definition — the metric name is used by two teams, so each team's definition was pulled and diffed on formula, window, population and data source.
- Disconfirming checks run: normalize-before-diff — normalised, the two definitions do not reduce to one measurement (different numerator event, different denominator population, different window), so the collision stands; superseded-definition check — the export was searched for a glossary or shared definition page and none exists; the closest text is Dispatch's own note "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (line 31), which asserts one team's methodology rather than a company standard and therefore does not resolve the split; AL-09 pre-check — the baseline gap is explained by the definitional split, so this is reported as AL-08 rather than AL-09 per the taxonomy's ordering.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both definitions re-read against lines 26 and 104 and matched character-for-character)
- Recommended resolution owner: the C2 owner (Noor E., CEO) decides one company definition of the on-time delivery rate metric before the first monthly business review; Dispatch and Accounts then restate their targets against it and rename the second measure (for example `billed on-time rate`) so one name never carries two formulas.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), under the page's convention "Commitment: KRs are committed unless marked (stretch)." (line 19), with the note "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM)" labelled "(stretch — only if the billing migration lands early)" (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), with the note "Portal timing depends on how fast the billing migration goes (see AC3.2)." (line 111)
- Conflict: Dispatch's committed KR depends end-to-end on a deliverable Accounts labels stretch and conditions on an unrelated billing migration; worse, the arithmetic assumes not just delivery but scale — 600 trial starts are expected from a portal Accounts scopes to "the first 40 partner accounts". If Accounts hits its stretch exactly, Dispatch still needs roughly fifteen trial starts per partner account.
- Detection check that fired: AL-12 edge label comparison on an acknowledged dependency — AL-01 did not fire because Accounts does carry the portal work (AC3.2); the commitment labels on the two sides of the edge were then compared, along with the target arithmetic.
- Disconfirming checks run: labeling-scheme check — Dispatch's page states its own convention (line 19), so DS2.2's lack of a "(stretch)" marker means committed rather than merely unlabeled, and Accounts' "(stretch — only if the billing migration lands early)" is explicit, so this is a genuine mismatch rather than two vocabularies; consumer-hedging check — Dispatch's note states the dependency but hedges nothing about it landing and applies no discount to the 600 figure, so no hedging kills or downgrades the finding.
- Inference labels: none — both commitment labels and both numbers are quoted; the 600-vs-40 arithmetic is read directly from the two quotes.
- Verdict: CONFIRMED (both quotes and both commitment labels re-read against lines 27, 19, 105 and 111)
- Recommended resolution owner: Accounts (Georg B.) and Dispatch (Mei L.) decide in week 1 whether the partner portal is committed; if it stays stretch, Dispatch re-cuts DS2.2 onto a channel it controls — for example "Enterprise trial starts from direct sales outreach 0 → `<target>`" — and keeps a smaller portal-contingent KR [proposal — placeholder target].

### [Major] AL-09 Baseline disagreement: Accounts ↔ company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Q4 business review evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same metric, the same instrument and the same period are stated eight points apart, and Accounts explicitly labels its number "Q4 2026 baseline". If 78 is the true starting point, a committed +4 is really a +12 ask on a P0 objective, and the quarter's expected attainment is wrong from day one.
- Detection check that fired: AL-09 — the metric catalog collected every stated baseline per canonical metric; two baselines for "Customer CSAT" in the same period differ far beyond rounding.
- Disconfirming checks run: as-of-date check — both statements name Q4 2026, so different as-of dates cannot explain the gap; definitional (AL-08) check — both name the same instrument, "quarterly relationship survey", and the export contains no second CSAT definition, population or segment (searched every line for the terms `CSAT` and `satisfaction`: only lines 101 and 118 mention it), so no definitional split explains it; near-miss check — no other CSAT figure exists anywhere in the corpus.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both statements re-read against lines 101 and 118 and matched character-for-character)
- Recommended resolution owner: Accounts (Georg B.) reconciles with the owner of the Q4 business review page (91031) in week 1 and restates AC2.2 against the agreed number before Q1 targets are locked.

### [Major] AL-05 Cascade drift: Core Systems ↔ company priority C2
- Core Systems evidence: "Objective CS2: Ship with confidence" tagged "(supports C2 — enterprise churn)" (sample-portfolio-2.md › Core Systems team — Q1 2027 › line 61), with its three KRs "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (line 62), "Change-failure rate 18% → 8% of production deploys (incident review tags)." (line 63) and "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (line 64), all committed by the page's convention "Commitment: KRs are committed unless marked (stretch)." (line 55)
- Company evidence: company priority C2, "Keep enterprise customers for life": "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the parent names its three drivers and none of them is deployment throughput, change-failure rate or CI duration; all three child KRs could be hit in full during a quarter in which enterprise logo churn worsens, and the three drivers C2 does name are already carried by Accounts (AC1, AC2, AC3). The link is decorative, which also hides that Core Systems' real strategic contribution this quarter is the C4 cost and telemetry work. Rated Major rather than the taxonomy's default Minor because the child KRs are committed and the parent is an exec-visible company priority.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KRs measure neither the parent's metric (logo churn) nor any documented driver of it, nor a deliverable the parent's own page names as needed.
- Disconfirming checks run: documented-mechanism search — C2's own text was checked for named contributing workstreams (it names three, none matching), the Core Systems page notes were checked ("Notes: SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." line 70 — no churn mechanism), and the Q4 2026 business review extracts were checked (lines 118–120 — reliability is reported as a Sev-1 count with no churn linkage); nothing in the export names deploy frequency, change-failure rate or CI time as a churn driver, so the finding survives.
- Inference labels: none — the absence of a mechanism is stated against the parent's own quoted driver list rather than inferred.
- Verdict: CONFIRMED (parent and child quotes re-read against lines 11 and 61–64)
- Recommended resolution owner: Core Systems (Adaeze O.) with the C2 owner (Noor E., CEO) either re-anchor CS2 to C4 — where CS1.2's unit-cost KR already sits — or add a quoted, agreed churn mechanism to C2 naming reliability as a driver, before the mid-quarter check-in.

### [Minor] AL-05 Cascade drift: Courier ↔ company priority C3
- Courier evidence: "Objective CR2: Every driver in the region hears about Coppervale from another driver" tagged "(supports C3)" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 42), with its only KR "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (line 43)
- Company evidence: company priority C3, "Make drivers love the app": "driver-app weekly retention from 71% to 80% across FY27." (sample-portfolio-2.md › Company Q1 2027 priorities › line 12)
- Conflict: C3's only metric is weekly retention; CR2's single KR counts new installs, which does not measure retention and can push it down as newly acquired drivers enter the weekly cohort. Courier's other objective already carries the parent metric directly ("Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3).", line 40), so CR2's claim on C3 adds a link nothing has to honour.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KR measures neither the parent metric nor a documented driver of it.
- Disconfirming checks run: documented-mechanism search — Courier's page notes were checked and state only "referral growth is our big swing this quarter" (line 49), which asserts priority rather than a referral→retention mechanism; the company priorities section, the other four team pages and the Q4 business review extracts were searched for any statement linking referral or install volume to retention and none exists. Severity held at the taxonomy's default Minor: the Courier page carries no commitment convention at all (see §3 AP-08), so the committed-objective escalation does not apply.
- Inference labels: the mechanism by which new installs dilute a weekly retention cohort is analyst inference — no Coppervale document states it.
- Verdict: CONFIRMED (both quotes re-read against lines 42–43 and 12)
- Recommended resolution owner: Courier (Tomás R.) re-anchors CR2 at the mid-quarter check-in — either to a retention-linked referral measure ("referred drivers still active in week 4 `<baseline>` → `<target>`") or explicitly to C1's growth pillar rather than C3 [proposal — placeholder target].

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to break the telemetry wait cycle at one edge (pre-GA SDK beta → subset validation → GA) — owner: Core Systems lead Adaeze O., week 1 (resolves §4 AL-11 Circular dependency).
2. Rewrite DS2.4 with a named population and, while the page is open, split DS1 into its two end-states — owner: Dispatch lead Mei L. (resolves §3 AP-13 Ambiguous Denominator, §3 AP-11 Objective as Kitchen Sink).
3. Decide one company definition of the on-time delivery rate metric and have both teams restate their targets against it — owner: Noor E. (CEO, C2 owner) (resolves §4 AL-08 Terminology collision).
4. Settle whether the partner portal is committed or stretch, and re-cut Dispatch's 600 trial starts accordingly — owner: Accounts lead Georg B. with Dispatch lead Mei L., week 1 (resolves §4 AL-12 Commitment asymmetry).
5. Reconcile the Q4 2026 CSAT baseline with the business-review page and restate AC2.2 — owner: Accounts lead Georg B., week 1 (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor "Ship with confidence" to C4, or get a churn mechanism written into C2 — owner: Core Systems lead Adaeze O. with Noor E. (resolves §4 AL-05 Cascade drift: Core Systems ↔ C2).
7. Rank the four Accounts objectives P0/P1/P2 and state what gets dropped if the billing migration slips — owner: Accounts lead Georg B. (resolves §3 AP-05 Everything Is a P0).
8. Re-cut the referral KR with a stated lever plus a leading KR, add a commitment convention to the Courier page, and re-anchor CR2's parent link — owner: Courier lead Tomás R. (resolves §3 AP-07 Unmoored Moonshot, §3 AP-08 Committed vs Aspirational Not Labeled, §4 AL-05 Cascade drift: Courier ↔ C3).
9. Move the App Store rating KR to Courier and name an accountable individual for the v3 onboarding KR — owner: Insights lead Halima D. (resolves §3 AP-12 Orphan KR, §3 AP-15 Ownerless KR).
10. Reframe CS1 around the change it intends — a quieter and cheaper platform than Q4 — rather than continuing the standing duty — owner: Core Systems lead Adaeze O. (resolves §3 AP-10 BAU Dressed as OKR).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.5); Critical §3 AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.1); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.3); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.4); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-5beed03/candidate/fixture2-portfolio/input/sample-portfolio-2.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up A (3.5), above the needs-rework threshold, and no Critical finding.
