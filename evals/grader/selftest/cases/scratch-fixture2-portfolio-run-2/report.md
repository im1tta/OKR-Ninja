# Coppervale — Q1 2027 OKR Portfolio Review

*Mode: portfolio (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027, as stated by the source file. Source: `input.md` (local export; no Atlassian connection available). Strategy source: the file's "Company Q1 2027 priorities" section (C1–C4).*

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 12 Major, 3 Minor findings.
The portfolio's biggest threat is **AL-11 Circular dependency**: Courier waits on Core Systems' SDK GA, Core Systems waits on Insights' schema validation, and Insights waits on Courier's instrumentation — three committed KRs with no valid execution order as written.
The most common quality issue is **AP-12 Orphan KR** (2 instances: Insights carries a driver-app App Store rating KR under an exec-dashboard objective; Accounts carries a partner-portal milestone under a delivery-trust objective).
Two teams also report an on-time delivery rate to the same company priority under incompatible definitions and baselines (AL-08 Terminology collision), and Dispatch's committed trial-start number rests on an Accounts KR explicitly marked stretch (AL-12 Commitment asymmetry).
Measurement hygiene is otherwise strong: every KR names a system of record, and all four company priorities have at least one contributing team objective.
Recommended first action: Core Systems convenes Courier and Insights this week to break the telemetry cycle before any of the three KRs can start.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |
| Core Systems | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 4 | 2 | 3 |
| Courier | 4 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 3 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.59) · Core Systems B (3.07) · Accounts B (3.22) · Courier B (3.23) · Insights B (3.37).

- Dispatch: K3=2, K7=2 — one KR's population is undefined; trial starts sit off its objective.
- Core Systems: O1=2 — "Continue running the platform smoothly" is standing duty, not a changed end-state.
- Accounts: K3=2 — CSAT baseline contradicts the Q4 review, so calibration is unverifiable.
- Courier: K3=2 — referral installs target is a 15x jump with no stated mechanism.
- Insights: K7=2 — App Store rating KR serves a different objective than the one stated.

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "**KR DS2.4:** Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (`input.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29`)
- Why it's a problem: "the failure rate" names no population — failed jobs, failed route builds, failed API calls and failed deliveries are all plausible readings on this page, and each yields a different number, so any result can be claimed as a hit. The contrast is visible one KR up: DS2.1 spells out its numerator and denominator in full.
- Scores affected: K1=1, K5=2, K3=2 (calibration unverifiable while the population is undefined), K7=2
- Suggested rewrite: "**KR DS2.4:** Dispatch job failure rate — jobs closed as failed as a share of `<all jobs dispatched in the week>`, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder denominator; the 6% and 3% figures are quoted from the current KR]

### [Major] AP-03 Vanity Metric — Dispatch
- Evidence: "**KR DS2.2:** 600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." (`input.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27`)
- Why it's a problem: the objective it sits under is "Enterprise teams run their whole day in Coppervale dispatch" — a depth-of-use end-state — but trial starts is a cumulative acquisition count that rises with portal traffic and campaign push whether or not a single enterprise team runs a full day in the product. (Also reads as AP-12 Orphan KR; reported once here as the vanity-metric root.)
- Scores affected: K2=2, K7=2
- Suggested rewrite: "**KR DS2.2:** Enterprise accounts running a full dispatch day in Coppervale (all shifts planned and closed in-product, ≥4 days/week) `<baseline>` → `<target>` accounts, measured weekly in the Ops Console." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "### Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions *(supports C1)*" (`input.md › Dispatch team — Q1 2027 › line 21`)
- Why it's a problem: two disjoint end-states — dispatcher satisfaction and geographic expansion — are bundled under one objective with one KR each, so the objective can be half-achieved with no way to say whether it succeeded, and neither half gets a full KR set. "Delight" is also the kind of abstraction two readers gloss differently.
- Scores affected: O2=2, K6=3, K7=3
- Suggested rewrite: split into "**Objective DS1 (ranked first):** Enterprise dispatchers would be annoyed to lose Coppervale" (KR: dispatcher NPS 24 → 40, quarterly in-product survey, Delighted dashboard "Dispatcher NPS") and "**Objective DS3:** Coppervale is a live option for logistics operators in DE and FR" (KR: signed pilot customers in DE and FR 0 → 6, CRM "Intl Pilots" view). [proposal — objective text is OKR-Ninja's; the KR figures are quoted from DS1.1 and DS1.2]

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "**KR CR2.1:** Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43`)
- Why it's a problem: a 15x quarterly target with no named lever, no intermediate milestone and no resourcing signal anywhere on the page — the team's only supporting text is "referral growth is our big swing this quarter" (line 49), which asserts importance rather than a mechanism. A number nobody can plan against functions as decoration, and it is the sole KR under its objective.
- Scores affected: K3=1, K6=0, O4=2
- Suggested rewrite: "**KR CR2.1 (aspirational):** Driver referral installs 3,000 → `<target>` this quarter via the in-app referral prompt shipping in week `<n>`; **leading KR (committed):** drivers sending ≥1 referral 0 → `<target>` per week (App Store + Play attributed installs)." [proposal — placeholder targets; the 3,000 baseline is quoted]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence: Courier's page header carries only "*Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06*" (`input.md › Courier team (driver app) — Q1 2027 › line 36`), while the other four team pages each state "*Commitment: KRs are committed unless marked (stretch).*" (`input.md › Dispatch team — Q1 2027 › line 19`)
- Why it's a problem: Courier is the one team with no commitment convention, and its targets range from "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (line 39) to a 15x install target — so readers cannot tell which of those is a must-hit, and expected attainment for the team cannot be computed. It also leaves the Courier edge of the telemetry cycle (§4 AL-11) unlabelled.
- Scores affected: K3=1 (CR2.1, compounding AP-07), team-level calibration
- Suggested rewrite: add to the Courier page header "*Commitment: KRs are committed unless marked (stretch).*" and mark CR2.1 as "(stretch)" while leaving CR1.1, CR1.2, CR3.1 and CR3.2 unmarked. [proposal — label text mirrors the convention quoted from the other four pages]

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "### Objective CS1: Continue running the platform smoothly for every team *(supports C4)*" (`input.md › Core Systems team — Q1 2027 › line 57`)
- Why it's a problem: "Continue running the platform smoothly" describes the team's standing job, not a change it intends to produce this quarter — it is achieved by default staffing, cannot fail in a way anyone would notice, and occupies an objective slot a real goal could hold. "Smoothly" is also undefined, and one of its two KRs (cloud cost per delivery) measures spend rather than smoothness.
- Scores affected: O1=1, O2=2, O3=2, K6=2, K7=2
- Suggested rewrite: "**Objective CS1:** No product team loses a day to platform failures — **KR CS1.1:** Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4; **KR CS1.2:** team-days lost to platform incidents `<baseline>` → `<target>` per quarter (incident review)." Move "Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost")." under a cost objective that names C4's unit-economics goal. [proposal — placeholder target; the Sev-1 and cost figures are quoted from CS1.1 and CS1.2]

### [Major] AP-12 Orphan KR — Insights
- Evidence: "**KR IN1.3:** Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (`input.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81`)
- Why it's a problem: the objective is "Execs run Monday mornings from our dashboards" — an App Store rating moves no dashboard-adoption outcome, shares no nouns or audience with it, and there is no causal chain from store rating to exec dashboard usage in two steps or fewer. It also sits on a surface Insights does not build: the driver app belongs to Courier, whose own objective is "Drivers finish every shift without fighting the app *(supports C3)*" (line 38), so the KR is measured by a team with no lever over it.
- Scores affected: K7=2
- Suggested rewrite: "**KR IN1.3:** Exec-suite dashboards whose weekly refresh completes before Monday 07:00 `<baseline>` → `<target>`% (Looker job monitor). Owner: Vik M." — and hand the App Store rating to Courier under CR1 if it is to be tracked at all. [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "**KR IN2.2:** Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`input.md › Objective IN2: Every product event lands in one trusted schema › line 85`)
- Why it's a problem: the page states "*Commitment: KRs are committed unless marked (stretch). Owners listed per KR.*" (line 76) and every other Insights KR names an individual — this one says "TBD", so the most cross-team-dependent KR on the page is the one nobody is accountable for. It is also the KR that needs an owner most, since it requires work from nine squads (see §4 AL-01).
- Scores affected: K4=0
- Suggested rewrite: "**KR IN2.2:** Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual on Insights>`." [proposal — owner name to be filled by the Insights lead; the metric is quoted unchanged]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "### Objective AC1 (Priority: P0): New customers reach first value in days, not weeks *(supports C2 — onboarding time-to-value)*" (line 95), "### Objective AC2 (Priority: P0): Support answers arrive before customers ask twice *(supports C2 — escalation backlog)*" (line 99), "### Objective AC3 (Priority: P0): Customers trust the delivery promises we report *(supports C2)*" (line 103), "### Objective AC4 (Priority: P0): Billing runs itself *(supports C1)*" (line 107), and "Notes: every one of these is P0 for us this quarter — we're not choosing." (line 111) — all `input.md › Accounts team (billing & customer success) — Q1 2027`
- Why it's a problem: four of four objectives carry an identical top-priority label and the team states outright that it is "not choosing", so the set encodes no trade-off — when the quarter gets tight nobody knows what gives, and eight KRs across onboarding, support, delivery reporting and a billing migration all claim first call on the same team.
- Scores affected: K7=2 (AC3), per-OKR cap applied to AC3 (two Major anti-patterns), team roll-up 3.22
- Suggested rewrite: "Objective AC1 (Priority: P0) … Objective AC2 (Priority: P1) … Objective AC3 (Priority: P1) … Objective AC4 (Priority: P2 — billing migration continues, portal deferred)", with the notes line replaced by "If we must drop one, AC4's migration slips first." [proposal — ranking is OKR-Ninja's; objective texts are quoted unchanged]

### [Major] AP-12 Orphan KR — Accounts
- Evidence: "**KR AC3.2:** Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (`input.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105`)
- Why it's a problem: the objective is about customers trusting reported delivery promises; a partner portal going live for 40 accounts is a delivery milestone on a different surface with no chain to delivery-promise trust, and it shares no nouns with the objective. It belongs with the self-serve/billing work in AC4, where its actual dependency (the billing migration) already lives.
- Scores affected: K2=1, K6=2, K7=2
- Suggested rewrite: move the portal KR under AC4 unchanged, and replace it with "**KR AC3.2:** Enterprise disputes of reported on-time delivery figures `<baseline>` → `<target>` per month (Zendesk view `<view name>`)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "**KR CR3.1:** Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`input.md › Objective CR3: Every driver action is visible to the teams that need it › line 46`)
- Core Systems evidence: "**KR CS3.1:** GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`input.md › Objective CS3: One telemetry pipeline every product team trusts › line 67`)
- Insights evidence: "**KR IN2.1:** Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (`input.md › Objective IN2: Every product event lands in one trusted schema › line 84`)
- Conflict: Courier gates on Core Systems' GA, Core Systems gates GA on Insights' validation, and Insights gates validation on Courier's instrumentation — a three-team cycle in which every team is second in line, so none of the three KRs can start and all three fail together. Two of the three teams' pages state their commitment convention as "KRs are committed unless marked (stretch)" (lines 55 and 76) and none of these KRs is marked stretch.
- Detection check that fired: AL-11 structural cycle detection on the dependency map — edges extracted from the blocking phrases "once Core Systems GAs the SDK", "after Insights validates event schema v3 in production" and "after Courier instruments the new driver-app event stream".
- Disconfirming checks run: (1) hard blocking vs soft preference — all three edges use hard gating language ("once", "after", "after"), none uses soft-preference wording such as ideally or would benefit from → cycle survives. (2) staged-milestone interleaving — Core Systems' note "Notes: SDK v1 is code-complete; GA is gated on schema v3 validation (Insights)." (line 70) shows a usable pre-GA build exists, but CR3.1 gates specifically on GA and no edge references a pre-GA milestone, so no valid interleaving exists as the KRs are written → cycle survives (this is, however, the cheapest resolution). (3) awareness plus resolution plan — Courier's "SDK timing per Core Systems' plan." (line 49) and Insights' "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream" (line 87) show each team sees its own edge, but no page acknowledges the cycle or states a plan to break it → no downgrade.
- Inference labels: none — all three edges quoted verbatim; the code-complete near-miss is quoted, not inferred.
- Verdict: CONFIRMED (all four load-bearing quotes re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Core Systems lead (owner of the GA gate) to convene Courier and Insights within the first week of the quarter and agree an execution order — most cheaply, Courier instruments the driver-app event stream on the quoted code-complete pre-GA SDK, Insights validates schema v3 against that stream, and Core Systems' GA follows; then restate all three KRs to name the milestone each actually needs.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "**KR DS2.2:** 600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials")." and "Notes: DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (`input.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › lines 27 and 31`), under the page rule "*Commitment: KRs are committed unless marked (stretch).*" (line 19)
- Accounts evidence: "**KR AC3.2:** Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." and "*Notes: every one of these is P0 for us this quarter — we're not choosing. Portal timing depends on how fast the billing migration goes (see AC3.2).*" (`input.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › lines 105 and 111`)
- Conflict: Dispatch's DS2.2 is committed by its page's stated convention and depends entirely on a portal that Accounts lists as stretch and conditions on an unrelated billing migration; worse, the arithmetic assumes more than Accounts' full stretch target — 600 trial starts routed through a portal Accounts scopes to "the first 40 partner accounts".
- Detection check that fired: AL-12 edge label comparison on an acknowledged cross-team dependency (Accounts does list the portal, so AL-01 did not fire), plus the target-arithmetic check — A's number requires more than B's full stretch target.
- Disconfirming checks run: (1) missing label ≠ mismatch — Dispatch's page states its labeling scheme explicitly and DS2.2 carries no "(stretch)" marker, while AC3.2 carries one, so both commitment levels are read from the teams' own vocabulary rather than inferred → mismatch stands. (2) consumer hedging — Dispatch's note says the KR "assumes the partner portal launch" with no discount, no fallback and no reference to Accounts' stretch label → no hedge found, finding stands at full severity.
- Inference labels: none — both commitment levels and both numbers are quoted; the 600-vs-40 comparison is arithmetic on quoted figures.
- Verdict: CONFIRMED (both sides' quotes re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Accounts lead to convene Dispatch within two weeks and pick one — Accounts commits the portal (removing the stretch label and the billing-migration condition) at a scope that can carry Dispatch's trial volume, or Dispatch re-baselines DS2.2 onto a channel it controls and moves the portal-dependent portion to a stretch KR of its own.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "**KR DS2.1:** On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (`input.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26`)
- Accounts evidence: "**KR AC3.1:** On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (`input.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104`)
- Conflict: one metric name, four differences — numerator (jobs completed in window vs deliveries scanned at destination), denominator (all completed jobs vs all scheduled deliveries including cancellations), cadence (weekly vs monthly) and system of record (Ops Console vs Billing warehouse). Both teams anchor to the same company promise, "keeping the delivery promises we report to customers" (line 11), so leadership and customers will see two different figures under that one name — 95% and 85% — for the same quarter, and neither team's page acknowledges the other's definition.
- Detection check that fired: AL-08 metric-name blocking — "On-time delivery rate" used by two teams; each team's definition hunted and diffed on formula, window, population and data source. The 13-point baseline gap (91% vs 78%) surfaced first as an AL-09 Baseline disagreement candidate; per the AL-09 disconfirming check it is explained by the definitional split, so it is reported here as the root cause with AL-09 cross-referenced.
- Disconfirming checks run: (1) different wording ≠ different definition — both definitions normalized (numerator / denominator / window / source) and diffed: all four components differ, and the wider Accounts denominator (scheduled deliveries including cancellations) mechanically explains the lower baseline → collision is real. (2) superseded glossary — searched the whole export for a shared definition, glossary or metric-catalog page either team defers to; none exists, the only two definitions are the ones quoted. (3) severity — AL-08's default is Minor; raised to Major because the colliding metric feeds a customer-facing company priority (C2) that both teams report against.
- Inference labels: the claim that the wider denominator drives the lower baseline is analyst inference from the two quoted definitions; no team document states it.
- Verdict: CONFIRMED (both definitions re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Insights lead (owner of the shared reporting layer) to convene Dispatch and Accounts before mid-quarter, publish one canonical on-time-delivery definition — numerator, denominator, cadence, system of record — and re-baseline both KRs against it, or rename one metric so the two never appear side by side in an exec rollup.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "**KR AC2.2:** Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (`input.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101`)
- Company evidence: "Customer health: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)."" (`input.md › Appendix — Q4 2026 business review (extracts) › line 118`)
- Conflict: the KR cites a "Q4 2026 baseline" of 86 for the same instrument the business review reports at 78 for the same period — an eight-point gap. Accounts' committed target of 90 is either a +4 improvement or a +12 one depending on which number is right, so the KR's ambition and its mid-quarter progress are both unreadable.
- Detection check that fired: AL-09 metric-catalog baseline collection — every stated baseline per canonical metric compared across sources; "Customer CSAT" carries two values for Q4 2026.
- Disconfirming checks run: (1) different as-of dates — both statements name Q4 2026 explicitly → same period, no date explanation. (2) different populations / definitional split (AL-08) — both name the same instrument, "quarterly relationship survey", and no other CSAT definition or segment appears anywhere in the export → no definitional explanation found. (3) commitment level — Accounts' page states "*Commitment: KRs are committed unless marked (stretch).*" (line 93) and AC2.2 is unmarked, so the metric carries a committed target → Major rather than Minor.
- Inference labels: none — both figures, both instrument names and both period labels are quoted.
- Verdict: CONFIRMED (both quotes re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Accounts lead with the Q4 business-review owner to reconcile the Q4 2026 CSAT figure within two weeks and restate AC2.2 against the agreed number, citing the survey run it comes from.

### [Major] AL-01 Unacknowledged dependency: Insights ↔ Dispatch / Courier / Core Systems / Accounts
- Insights evidence: "**KR IN2.2:** Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (`input.md › Objective IN2: Every product event lands in one trusted schema › line 85`)
- Counterparty evidence (nearest matches, both distinguished): "**KR CS3.1:** GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (`input.md › Objective CS3: One telemetry pipeline every product team trusts › line 67`) and "**KR CR3.1:** Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (`input.md › Objective CR3: Every driver action is visible to the teams that need it › line 46`)
- Conflict: IN2.2 requires seven more product squads to do adoption work this quarter, but no team in scope carries a KR, objective or note committing to onboarding onto v3 event conventions. Core Systems' "internal apps live on it 1 → 3" counts SDK adoption by internal apps, not squads adopting v3 conventions, and Courier's CR3.1 is instrumentation with the SDK — neither names the conventions onboarding, and neither is sized to seven squads. The KR is committed by the page's convention and has no owner (§3 AP-15).
- Detection check that fired: AL-01 dependency extraction — "Product squads onboarded" names external work by other teams; resolved to the product teams in scope and searched on their side for the deliverable.
- Disconfirming checks run: (1) missing mention ≠ unacknowledged — searched all five team sections plus the company priorities and the Q4 appendix for "v3", "schema", "conventions" and "onboard": every "v3"/"schema" hit is on the Core Systems or Insights pages (lines 67, 70, 83, 84, 85, 87), and the only "onboard" hits outside IN2.2 are Accounts' customer-onboarding KRs (lines 96, 97), a different subject → no squad-side commitment found. (2) backlog check — the taxonomy's Jira/epic search could not be run: this review has one local export in scope and no Atlassian connection, so squads may hold the work off-OKR; this is why the verdict below is PLAUSIBLE rather than CONFIRMED. (3) near-miss quoting — the two closest items are quoted above and distinguished.
- Inference labels: the reading that the "Product squads" of IN2.2 are the teams in this export is analyst inference — the export covers five teams while the KR counts nine squads, so four are outside the reviewed scope.
- Verdict: PLAUSIBLE (all quotes verified verbatim, but the absence claim could not be tested against squad backlogs, and four of the nine squads are outside the export)
- Recommended resolution owner: Insights lead to name an owner for IN2.2 and secure a dated v3-onboarding commitment from each squad lead by end of week 3, or re-scope the KR to the squads that have actually committed.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company priority C2
- Core Systems evidence: "### Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" with KRs "**KR CS2.1:** Deploy frequency 2/week → 8/week (Buildkite deploy log).", "**KR CS2.2:** Change-failure rate 18% → 8% of production deploys (incident review tags)." and "**KR CS2.3:** CI pipeline p95 42 min → 15 min (Buildkite analytics)." (`input.md › Core Systems team — Q1 2027 › lines 61–64`)
- Company evidence: "**C2 — Keep enterprise customers for life:** reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (`input.md › Company Q1 2027 priorities › line 11`)
- Conflict: CS2 claims C2 explicitly, but all three of its KRs are internal delivery-throughput measures and none of them is C2's metric or one of the three drivers C2 itself names. Core Systems could hit 8 deploys a week, an 8% change-failure rate and a 15-minute CI pipeline in a quarter where enterprise churn rises — the link is decorative, and it lets a company priority look staffed by work that cannot move it.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's own page names as needed? All three answers are no.
- Disconfirming checks run: (1) mechanism documented elsewhere — C2's own text names its contributing workstreams and none is a delivery-throughput metric; Core Systems' notes say only "*Notes: SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.*" (line 70), which states a C4 mechanism, not a churn one. (2) corpus search for the driver relationship — searched the export for "churn": it appears exactly twice, in C2 (line 11) and in this objective's own claim (line 61), so nothing in the corpus documents deploy velocity as a churn driver → check failed, finding stands. (3) severity — AL-05's default here is Minor (C2 does not name Core Systems as a contributor); raised to Major because CS2's KRs are committed under the page rule "*Commitment: KRs are committed unless marked (stretch).*" (line 55).
- Inference labels: none — the parent's named drivers, the child's claim and all three child KRs are quoted; no mechanism is asserted on the team's behalf.
- Verdict: CONFIRMED (all load-bearing quotes re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Core Systems lead with the C2 owner (Noor E., CEO) before mid-quarter — either re-anchor CS2 to C4, where its reliability and cost work already lands, or add one KR measuring a driver C2 actually names (e.g. escalations caused by production defects).

### [Minor] AL-05 Cascade drift: Courier ↔ Company priority C3
- Courier evidence: "### Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)*" with its single KR "**KR CR2.1:** Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (`input.md › Courier team (driver app) — Q1 2027 › lines 42–43`)
- Company evidence: "**C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80% across FY27." (`input.md › Company Q1 2027 priorities › line 12`)
- Conflict: C3 is a retention priority with a single named metric, while CR2's only KR counts new installs — an acquisition measure. Hitting 45,000 referral installs would not move weekly retention, and the same team already carries the KR that does ("**KR CR1.2:** Driver-app weekly retention 71% → 78%", line 40), so CR2's claim on C3 is decorative.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child KR measures neither the parent's metric nor a driver the parent names.
- Disconfirming checks run: (1) mechanism documented elsewhere — C3 names only weekly retention; Courier's notes offer "Notes: referral growth is our big swing this quarter." (line 49), which asserts priority, not a retention mechanism → no documented driver relationship found. (2) parent-metric coverage elsewhere in the same team — CR1.2 already covers C3's metric, so C3 is not left uncovered by this finding, which is why it is Minor rather than a coverage gap. (3) severity — no commitment label exists anywhere on the Courier page (§3 AP-08), so the committed-objective escalation does not apply → stays Minor.
- Inference labels: the further concern that a 15x install surge of low-intent referred drivers would depress the weekly-retention cohort CR1.2 targets is analyst inference — no team document states this tradeoff.
- Verdict: CONFIRMED (both quotes re-fetched and matched character-for-character against the source file)
- Recommended resolution owner: Courier lead to re-anchor CR2 before mid-quarter — either point it at C1 (growth), where an acquisition metric belongs, or keep C3 and add a retention-quality KR on referred drivers specifically.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights to break the telemetry cycle by naming the milestone each KR actually needs (the SDK is already code-complete) — owner: Core Systems lead (resolves §4 AL-11 Circular dependency).
2. Redefine DS2.4's population — numerator, denominator, cadence and system of record — before the first weekly ops review — owner: Dispatch lead (resolves §3 AP-13 Ambiguous Denominator).
3. Decide whether the partner portal is committed or stretch, and re-scope Dispatch's 600 trial starts to match — owner: Accounts lead with Dispatch lead (resolves §4 AL-12 Commitment asymmetry).
4. Publish one canonical on-time-delivery definition and re-baseline both teams' KRs against it — owner: Insights lead (resolves §4 AL-08 Terminology collision, cross-referencing AL-09).
5. Reconcile the Q4 2026 CSAT figure (86 vs 78) and restate AC2.2 against the agreed baseline — owner: Accounts lead (resolves §4 AL-09 Baseline disagreement).
6. Name an owner for IN2.2 and get a dated v3-onboarding commitment from each squad lead, or re-scope the KR — owner: Insights lead (resolves §4 AL-01 Unacknowledged dependency and §3 AP-15 Ownerless KR).
7. Re-anchor CS2 to C4 or add a KR on a driver C2 names, and rewrite CS1 as a changed end-state — owner: Core Systems lead (resolves §4 AL-05 Cascade drift: Core Systems and §3 AP-10 BAU Dressed as OKR).
8. Rank the four Accounts objectives P0/P1/P2 and move the portal KR under AC4 — owner: Accounts lead (resolves §3 AP-05 Everything Is a P0 and AP-12 Orphan KR — Accounts).
9. Add Courier's commitment convention, mark CR2.1 aspirational with a named lever, and re-anchor CR2 — owner: Courier lead (resolves §3 AP-07 Unmoored Moonshot, AP-08 Committed vs Aspirational Not Labeled and §4 AL-05 Cascade drift: Courier).
10. Replace Insights' App Store rating KR with a dashboard-reliability measure, and split Dispatch's DS1 into two objectives — owners: Insights lead and Dispatch lead (resolves §3 AP-12 Orphan KR — Insights, AP-03 Vanity Metric and AP-11 Objective as Kitchen Sink).

## 6. Suggested single-team re-runs

- **Dispatch** (roll-up C (2.59); Critical §3 AP-13 Ambiguous Denominator): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (roll-up B (3.23); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Courier team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (roll-up B (3.07); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (roll-up B (3.37); Critical §4 AL-11 Circular dependency): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: `input.md`, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1); strategy doc: the 'Company Q1 2027 priorities' section of the same file (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: roll-up B (3.22), above the needs-rework threshold, and no Critical finding.
