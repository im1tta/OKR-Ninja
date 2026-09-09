# OKR Portfolio Review — Coppervale, Q1 2027

*Mode: portfolio (5 teams in scope: Dispatch, Courier, Core Systems, Insights, Accounts). Period: Q1 2027, as stated by the source file. Source of record: `sample-portfolio-2.md` (full path: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md`); no Atlassian connection available. Strategy source: the file's "Company Q1 2027 priorities" section (Confluence page 91050), so O4 Strategic Anchoring is scored, not N/A. All source refs below use `sample-portfolio-2.md › <nearest heading> › line N` against that file.*

---

## 1. Executive summary

**Verdict: At risk.** 5 teams reviewed; 2 Critical, 9 Major, 2 Minor findings.
The portfolio's worst alignment risk is **AL-11 Circular dependency**: Courier's instrumentation waits on Core Systems' SDK GA, Core Systems' GA waits on Insights' schema-v3 validation, and Insights' validation waits on Courier's instrumentation — three telemetry KRs with no valid execution order, two of them explicitly committed.
No goodness anti-pattern repeats: the eight goodness findings hit eight distinct anti-patterns, so there is no single most common one; the most consequential is **AP-13 Ambiguous Denominator** (the only Critical goodness finding — Dispatch's "failure rate" KR names no population, so any number can be claimed).
Dispatch's committed trial-starts KR rides on a partner portal that Accounts marks stretch (**AL-12 Commitment asymmetry**), and Dispatch and Accounts report an "On-time delivery rate" under incompatible definitions 13 points apart against the same company priority (**AL-08 Terminology collision**).
Accounts marks all four objectives P0 and states it is "not choosing" (**AP-05 Everything Is a P0**); Accounts' CSAT baseline contradicts the Q4 business review by 8 points (**AL-09 Baseline disagreement**); Core Systems claims the enterprise-churn priority with three delivery-pipeline KRs that touch none of its named drivers (**AL-05 Cascade drift**).
Recommended first action: convene Courier, Core Systems and Insights in week 1 to break the telemetry cycle with a pre-GA SDK milestone.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Dispatch | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Core Systems | 2 | 2 | 2 | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 3 |
| Courier | 4 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 4 | 2 | 2 |
| Insights | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 4 | 2 | 2 |
| Accounts | 4 | 4 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Dispatch C (2.59) · Core Systems B (3.08) · Courier B (3.24) · Insights B (3.39) · Accounts B (3.48).

- Dispatch: K1=3 — DS2.4 states no population for its "failure rate" (AP-13).
- Core Systems: O1=2 — CS1 "Continue running the platform" names no change (AP-10).
- Courier: K3=2 — referral installs 15x with no stated mechanism (AP-07).
- Insights: K7=2 — an App Store rating KR sits under the exec-dashboard objective (AP-12).
- Accounts: K3=2 — CSAT target rests on a baseline the Q4 review contradicts (AL-09).

## 3. Per-team goodness findings

### [Critical] AP-13 Ambiguous Denominator — Dispatch
- Evidence: "Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 29)
- Evidence (sibling KR that does define its population): "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Why it's a problem: the KR never says failure *of what* — dispatched jobs, deliveries, route-plan builds, or API calls — so the base set can be chosen after the fact and 6% → 3% can be claimed or denied at will; the KR three lines above defines its denominator explicitly, so the omission is not this page's house style, and "ops weekly report" names no view that would settle it.
- Scores affected: K1=1, K5=2 (and the Critical cap holds the whole DS2 OKR at 1.9 per the rubric's Roll-Up caps)
- Suggested rewrite: "KR DS2.4: Failed jobs — jobs closed without a completed delivery as a share of all jobs dispatched, measured weekly in the Ops Console — 6% → 3% by end of Q1." [proposal — placeholder target]

### [Minor] AP-11 Objective as Kitchen Sink — Dispatch
- Evidence: "Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions *(supports C1)*" (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 21)
- Evidence (the seam the KRs split along): "Enterprise dispatcher NPS 24 → 40" (sample-portfolio-2.md › Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions › line 22) beside "Signed pilot customers in DE and FR: 0 → 6" (same heading › line 23)
- Why it's a problem: two unrelated end-states — dispatcher satisfaction and geographic expansion — are joined by "and" with disjoint audiences, and the KR set splits one-per-clause, so neither half gets a sufficient set and neither can be ranked against or dropped in favour of the other.
- Scores affected: O1=3, O2=2, K7=3
- Suggested rewrite: "Objective DS1 (ranked first): Enterprise dispatchers would fight to keep Coppervale — KR: Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard 'Dispatcher NPS'). Objective DS3: Coppervale is a credible dispatch choice outside our home market — KR: Signed pilot customers in DE and FR: 0 → 6 (CRM 'Intl Pilots' view)."

### [Major] AP-10 BAU Dressed as OKR — Core Systems
- Evidence: "Objective CS1: Continue running the platform smoothly for every team *(supports C4)*" (sample-portfolio-2.md › Core Systems team — Q1 2027 › line 57)
- Why it's a problem: "Continue running the platform smoothly" is the team's standing job stated with no delta — it is satisfied by default staffing and cannot fail in a way anyone would notice — and "smoothly" is an abstraction two readers would gloss differently; an open-ended duty crammed into a quarter also displaces a real goal from a three-objective set.
- Scores affected: O1=1, O2=2, O3=2
- Suggested rewrite: "Objective CS1: Platform incidents and unit cost stop taxing every product team — KR CS1.1: Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4; KR CS1.2: Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard 'Unit Cost')." (Both existing KRs are sound and are kept; only the standing-duty framing is replaced.)

### [Major] AP-07 Unmoored Moonshot — Courier
- Evidence: "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Evidence (the only supporting text on the page): "referral growth is our big swing this quarter." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 49)
- Why it's a problem: a 15x target with no named lever, no intermediate milestone and no resourcing signal — "our big swing" is enthusiasm, not a mechanism — functions as decoration: nobody can plan against it, forecast it, or tell a miss from a fantasy.
- Scores affected: K3=1, K6=0, K7=2 (single-KR set)
- Suggested rewrite: "KR CR2.1 (aspirational): Driver referral installs 3,000 → `<target>` this quarter via the in-app referral card, shipped by `<date>` (App Store + Play attributed installs); KR CR2.2 (committed, leading): drivers sending at least one referral `<baseline>`% → `<target>`% of weekly active drivers (Amplitude)." [proposal — placeholder target]

### [Minor] AP-08 Committed vs Aspirational Not Labeled — Courier
- Evidence (the Courier page header, which carries no commitment line): "Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06" (sample-portfolio-2.md › Courier team (driver app) — Q1 2027 › line 36)
- Evidence (the convention every other team page states): "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19)
- Evidence (the spread of stretch this leaves unlabeled): "Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics)." (sample-portfolio-2.md › Objective CR1: Drivers finish every shift without fighting the app › line 39) beside "Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)." (sample-portfolio-2.md › Objective CR2: Every driver in the region hears about Coppervale from another driver › line 43)
- Why it's a problem: this is a set-level defect of the Courier page, not of any one KR — a 0.4-point crash-free improvement and a 15x referral moonshot sit in one set with no committed/aspirational marker to separate them, so expected attainment cannot be computed and every sandbag/moonshot judgment on the page is unanchored. Search performed: the whole Courier page (lines 35–49) for "committed", "aspirational", "stretch" and "P0" — no marker anywhere; the other four team pages carry the convention line (Dispatch line 19, Core Systems line 55, Insights line 76, Accounts line 93), so its absence here is a gap, not company practice.
- Scores affected: K3=3 on CR1.2 (its stretch is justified in text but the K3=4 anchor's labelling condition fails); set-level — it is why CR2.1's 15x arrives unmarked
- Suggested rewrite: add to the Courier page header, immediately under its source line: "*Commitment: KRs are committed unless marked (stretch).*" and relabel the outlier: "**KR CR2.1 (stretch):** Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs)."

### [Major] AP-12 Orphan KR — Insights
- Evidence: "Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M." (sample-portfolio-2.md › Objective IN1: Execs run Monday mornings from our dashboards › line 81)
- Evidence (its stated objective): "Objective IN1: Execs run Monday mornings from our dashboards *(supports C4)*" (sample-portfolio-2.md › Insights team — Q1 2027 › line 78)
- Why it's a problem: the App Store rating is set by drivers rating the driver app, and no causal chain in two steps runs from it to leadership using Insights' dashboards — the KR shares no noun, audience or system with its objective, so hitting it would not move IN1 and missing it would not mean IN1 failed. It also parks a driver-app outcome with a team that does not own that surface (Courier's CR1 does).
- Scores affected: K7=2
- Suggested rewrite: move the rating to Courier's CR1 set and replace it with a KR that serves IN1: "KR IN1.3: Exec-suite dashboards whose weekly numbers reconcile to their source system of record `<baseline>`/9 → 9/9 (data QA checklist). Owner: Vik M." [proposal — placeholder target]

### [Major] AP-15 Ownerless KR — Insights
- Evidence: "Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 85)
- Evidence (the page's own promise): "Commitment: KRs are committed unless marked (stretch). Owners listed per KR." (sample-portfolio-2.md › Insights team — Q1 2027 › line 76)
- Why it's a problem: on a page that promises an owner per KR, this is the one KR whose owner is "TBD" — and it is the KR that most needs one, because it asks nine squads outside Insights to change their event conventions, work nobody is accountable for chasing. Search performed: the whole Insights page (lines 74–87) and every other team page for a named owner of v3 onboarding — none found.
- Scores affected: K4=0
- Suggested rewrite: "KR IN2.2: Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: `<named individual>` (Insights), with each squad's onboarding date agreed with that squad's lead by `<date>`." [proposal — placeholder target]

### [Major] AP-05 Everything Is a P0 — Accounts
- Evidence: "Objective AC1 (Priority: P0): New customers reach first value in days, not weeks *(supports C2 — onboarding time-to-value)*" (sample-portfolio-2.md › Accounts team (billing & customer success) — Q1 2027 › line 95)
- Evidence: "Objective AC2 (Priority: P0): Support answers arrive before customers ask twice *(supports C2 — escalation backlog)*" (sample-portfolio-2.md › Accounts team (billing & customer success) — Q1 2027 › line 99)
- Evidence: "Objective AC3 (Priority: P0): Customers trust the delivery promises we report *(supports C2)*" (sample-portfolio-2.md › Accounts team (billing & customer success) — Q1 2027 › line 103)
- Evidence: "Objective AC4 (Priority: P0): Billing runs itself *(supports C1)*" (sample-portfolio-2.md › Accounts team (billing & customer success) — Q1 2027 › line 107)
- Evidence (the team says so itself): "every one of these is P0 for us this quarter — we're not choosing." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Why it's a problem: four of four objectives carry the identical top-priority label and the page states outright that the team is not choosing, so the set encodes no trade-off — when onboarding, escalations, delivery reporting and the billing migration collide mid-quarter, the OKRs give the team no rule for what slips. The defect belongs to the objective set, not to any single objective, so it is filed once here rather than folded into a member's block.
- Scores affected: no single dimension — AP-05 is scored against the Accounts objective set; it is the reason eight committed KRs across four objectives carry no ranking for the quarter
- Suggested rewrite: "Objective AC1 (P0): New customers reach first value in days, not weeks. Objective AC2 (P1): Support answers arrive before customers ask twice. Objective AC3 (P1): Customers trust the delivery promises we report. Objective AC4 (P2 — protected floor only, no new scope beyond the migration): Billing runs itself." (Ranking proposed to follow C2's own stated driver order, onboarding time-to-value first; the team confirms or re-ranks.)

## 4. Alignment findings

### [Critical] AL-11 Circular dependency: Courier ↔ Core Systems ↔ Insights
- Courier evidence: "Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK." (sample-portfolio-2.md › Objective CR3: Every driver action is visible to the teams that need it › line 46)
- Core Systems evidence: "GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard)." (sample-portfolio-2.md › Objective CS3: One telemetry pipeline every product team trusts › line 67)
- Insights evidence: "Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D." (sample-portfolio-2.md › Objective IN2: Every product event lands in one trusted schema › line 84)
- Conflict: the three KRs close a cycle — Courier waits on Core Systems, Core Systems waits on Insights, Insights waits on Courier — so no valid execution order exists and, as written, none of the three can start. Severity is Critical rather than Major because every edge is hard-sequenced and Core Systems' and Insights' KRs are committed under their pages' stated conventions (lines 55 and 76, neither marked stretch), making committed outcomes impossible as sequenced; Courier's edge carries no commitment label at all (see §3 AP-08 Committed vs Aspirational Not Labeled).
- Detection check that fired: graph-structural cycle detection on the dependency map (AL-11) — edges Courier→Core Systems ("once Core Systems GAs the SDK"), Core Systems→Insights ("after Insights validates event schema v3 in production"), Insights→Courier ("after Courier instruments the new driver-app event stream").
- Disconfirming checks run: hard blocking vs soft preference — all three edges use hard sequencing ("once", "after", "after") with no hedge such as "ideally" or "would benefit from", so no downgrade. Staged-milestone interleaving — searched each team's notes for an interim milestone that would unwind the loop: Core Systems "SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment." (line 70), Insights "schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready." (line 87), Courier "SDK timing per Core Systems' plan." (line 49) — all three restate the same blocking order and none names a pre-GA build or partial validation that could interleave, so the check does not kill the finding. Awareness-plus-resolution-plan — no team's text acknowledges the loop or proposes a break, so no downgrade to Minor.
- Inference labels: none — all load-bearing text quoted; every edge in the cycle is verbatim.
- Verdict: CONFIRMED (all three edge quotes re-verified character-for-character against lines 46, 67 and 84)
- Recommended resolution owner: Core Systems lead, owner of the gating SDK GA, to convene Courier and Insights in week 1 and re-cut the sequence around a pre-GA build — SDK v1 release candidate → Courier instruments the 14 flows on the RC → Insights validates schema v3 in production → Core Systems GAs — restating each of the three KRs' conditions accordingly.

### [Major] AL-12 Commitment asymmetry: Dispatch ↔ Accounts
- Dispatch evidence: "600 enterprise trial starts via the partner portal launch" (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 27), committed under the page's convention "Commitment: KRs are committed unless marked (stretch)." (sample-portfolio-2.md › Dispatch team — Q1 2027 › line 19), with the dependency stated as "DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31)
- Accounts evidence: "Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 105), reinforced by "Portal timing depends on how fast the billing migration goes (see AC3.2)." (sample-portfolio-2.md › Objective AC4 (Priority: P0): Billing runs itself › line 111)
- Conflict: a committed Dispatch KR depends entirely on a deliverable its producer labels stretch and conditions on an unrelated migration landing early; the target arithmetic does not meet either — Accounts commits the portal only to "the first 40 partner accounts" while Dispatch expects 600 enterprise trial starts to flow through it.
- Detection check that fired: AL-12 edge-label comparison on the acknowledged dependency Dispatch→Accounts (an edge AL-01 did not flag, because Accounts does carry a partner-portal KR).
- Disconfirming checks run: missing label ≠ mismatch — both pages state a labelling scheme (Dispatch line 19, Accounts line 93) and Accounts applies it explicitly to AC3.2, so this is a real commitment mismatch, not vocabulary drift. Consumer-side hedging or discounting — searched Dispatch's KR text and its notes for a fallback channel or a discounted number; the note says only that the KR "assumes the partner portal launch", so nothing kills or weakens the finding. Same-quarter check — both pages are Q1 2027.
- Inference labels: none — all load-bearing text quoted, including both commitment levels.
- Verdict: CONFIRMED (both KRs and both commitment statements re-verified against lines 19, 27, 31, 93 and 105)
- Recommended resolution owner: Accounts lead, as portal owner, with the Dispatch lead by end of week 2: either promote AC3.2 to committed with the billing-migration risk retired and size it against Dispatch's funnel, or re-cut DS2.2 onto a portal-independent trial channel with a target that does not assume the portal.

### [Major] AL-08 Terminology collision: Dispatch ↔ Accounts
- Dispatch evidence: "On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 26)
- Accounts evidence: "On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%." (sample-portfolio-2.md › Objective AC3 (Priority: P0): Customers trust the delivery promises we report › line 104)
- Conflict: one metric name, two incompatible measurements — different qualifying event (job completion vs destination scan), different population (completed jobs vs all scheduled deliveries including cancellations), different window (weekly vs monthly), different system (Ops Console vs Billing warehouse) — producing baselines 13 points apart. Both feed one company priority, "keeping the delivery promises we report to customers" (sample-portfolio-2.md › Company Q1 2027 priorities › line 11), so an exec reading on-time delivery gets two different truths — while Dispatch's note asserts a single methodology for the pair: "On-time delivery is measured per our Ops Console methodology (see KR DS2.1)." (sample-portfolio-2.md › Objective DS2: Enterprise teams run their whole day in Coppervale dispatch › line 31).
- Detection check that fired: AL-08 blocking key — the same metric name used by two teams; each team's stated definition then diffed on formula, window, population and data source.
- Disconfirming checks run: different wording ≠ different definition — normalized both definitions before diffing; they differ on all four axes, so the check does not kill the finding. Superseded-definition check — searched both pages for a glossary reference or shared definition; neither cites one and the pages are contemporaneous (last updated 2027-01-04 and 2027-01-08). AL-09 pre-check — the 91% vs 78% baseline gap is fully explained by the definitional split, so per the taxonomy this is reported as AL-08 with **AL-09 Baseline disagreement** cross-referenced as the secondary ID rather than double-counted as a separate baseline finding.
- Inference labels: none — both definitions quoted verbatim from the teams' own pages; no equivalence assumed.
- Verdict: CONFIRMED (both definitions re-verified character-for-character against lines 26 and 104)
- Recommended resolution owner: Accounts lead, as owner of the customer-facing delivery-promise report under C2, to convene Dispatch by end of week 2 and publish one canonical definition on the company priorities page, keeping the other as an explicitly renamed internal variant (for example "ops completion-window rate"), with both teams' targets restated against whichever definition survives.

### [Major] AL-09 Baseline disagreement: Accounts ↔ Company Q4 2026 business review
- Accounts evidence: "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)." (sample-portfolio-2.md › Objective AC2 (Priority: P0): Support answers arrive before customers ask twice › line 101)
- Company evidence: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)." (sample-portfolio-2.md › Appendix — Q4 2026 business review (extracts) › line 118)
- Conflict: the same instrument and the same period yield two current values 8 points apart. If the business review is right, Accounts' committed KR is a +12 ask sold as a +4 step, and a P0 objective's expected attainment is calibrated against a number that does not exist.
- Detection check that fired: AL-09 metric-catalog baseline collection — two stated baselines for one canonical metric ("Customer CSAT") in the same period (Q4 2026), differing beyond rounding.
- Disconfirming checks run: different as-of dates — both statements name Q4 2026, so no date explanation. Definitional split (AL-08 pre-check) — both name the same instrument, the "quarterly relationship survey", and neither states a different population, segment or formula; searched both pages and the other four team pages for any other CSAT definition or figure and found none, so no terminology collision explains the gap. Near-miss check — the two other Q4 figures the appendix reports both agree with the team baselines that cite them (driver-app weekly retention 71%, line 119, matching Courier's KR CR1.2; Sev-1 incidents 9, line 120, matching Core Systems' KR CS1.1), which shows the appendix is the reconciled source elsewhere in this portfolio and singles out CSAT as the outlier.
- Inference labels: none — both baseline statements quoted verbatim with their as-of periods.
- Verdict: CONFIRMED (both quotes re-verified against lines 101 and 118)
- Recommended resolution owner: Accounts lead with the Q4 business-review owner, within week 1: agree which figure is the Q4 2026 actual, restate KR AC2.2 against it, and record the survey population on the KR if the two numbers turn out to measure different customer sets.

### [Major] AL-05 Cascade drift: Core Systems ↔ Company Q1 2027 priorities (C2)
- Core Systems evidence: "Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*" (sample-portfolio-2.md › Core Systems team — Q1 2027 › line 61), with its complete KR set — "Deploy frequency 2/week → 8/week (Buildkite deploy log)." (sample-portfolio-2.md › Objective CS2: Ship with confidence › line 62); "Change-failure rate 18% → 8% of production deploys (incident review tags)." (same heading › line 63); "CI pipeline p95 42 min → 15 min (Buildkite analytics)." (same heading › line 64)
- Company evidence: "reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." (sample-portfolio-2.md › Company Q1 2027 priorities › line 11)
- Conflict: the child claims C2 by name, but none of its three KRs measures the parent metric (enterprise logo churn) or any of the three drivers C2 itself names — all three are internal delivery-pipeline metrics, so Core Systems could hit 8 deploys a week, an 8% change-failure rate and a 15-minute CI in a quarter where enterprise churn worsens, and the link would still read as achieved. Severity: AL-05's default here is Minor because C2 does not name Core Systems as a contributor, escalated one level to Major because CS2's KRs are committed under the page's stated convention (line 55) and the parent is an exec-owned company priority.
- Detection check that fired: AL-05 mechanism check on an explicit parent link — the child's KRs measure neither the parent's metric, nor a documented driver of it, nor a deliverable the parent's own page names as needed.
- Disconfirming checks run: parent's own page for named contributing workstreams — C2 enumerates its drivers ("onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers", line 11) and none is deploy cadence, change-failure rate or CI duration; it names no owning team either, so nothing there rescues the link. Child's page for a stated mechanism — Core Systems' notes cover only the SDK and cost work ("SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.", line 70) and say nothing about churn or enterprise customers. Strategy doc for a driver relationship — searched all four company priorities (lines 10–13) for delivery-velocity, deployment or CI language and found none. No check kills or weakens the finding.
- Inference labels: none — both the claimed link and the parent's driver list are quoted; no causal mechanism was inferred in either direction.
- Verdict: CONFIRMED (the parent priority, the child objective and all three child KRs re-verified against lines 11 and 61–64)
- Recommended resolution owner: Core Systems lead with the owner of the company priorities page, by end of week 2: either re-anchor CS2 to C4 (where CS1.2's unit-cost KR already sits) and drop the churn claim, or add one KR measuring a named C2 driver that platform work actually moves — for example escalations caused by production change failures.

## 5. Prioritized action list

1. Convene Courier, Core Systems and Insights in week 1 to re-sequence the telemetry chain around a pre-GA SDK build and restate the three gating KRs — owner: Core Systems lead (resolves §4 AL-11 Circular dependency).
2. Define DS2.4's population in the KR text and split DS1's two-in-one objective before the quarter's first check-in — owner: Dispatch lead (resolves §3 AP-13 Ambiguous Denominator and AP-11 Objective as Kitchen Sink).
3. Reconcile Dispatch's committed 600 trial starts with Accounts' stretch 40-account portal, promoting one or re-cutting the other — owner: Accounts lead with Dispatch lead (resolves §4 AL-12 Commitment asymmetry).
4. Publish one canonical "On-time delivery rate" definition on the company priorities page and rename the surviving variant — owner: Accounts lead (resolves §4 AL-08 Terminology collision, with AL-09 Baseline disagreement as its secondary ID).
5. Settle the Q4 2026 CSAT actual with the business-review owner and restate AC2.2 against it — owner: Accounts lead (resolves §4 AL-09 Baseline disagreement).
6. Re-anchor CS2 to C4 or add a KR measuring one of C2's three named churn drivers — owner: Core Systems lead (resolves §4 AL-05 Cascade drift).
7. Rank Accounts' four P0 objectives into P0/P1/P2 so mid-quarter collisions have a stated tie-breaker — owner: Accounts lead (resolves §3 AP-05 Everything Is a P0).
8. Replace CS1's standing-duty objective with an outcome framing over its two existing KRs — owner: Core Systems lead (resolves §3 AP-10 BAU Dressed as OKR).
9. Re-cut the referral moonshot with a stated lever plus a leading KR, and add the commitment convention to the Courier page — owner: Courier lead (resolves §3 AP-07 Unmoored Moonshot and AP-08 Committed vs Aspirational Not Labeled).
10. Move the App Store rating KR to Courier's CR1 and name an accountable individual for IN2.2 — owner: Insights lead (resolves §3 AP-12 Orphan KR and AP-15 Ownerless KR).

## 6. Suggested single-team re-runs

- **Dispatch** (Critical goodness finding AP-13 Ambiguous Denominator; roll-up C (2.59) is above the needs-rework threshold, so the Critical finding is the qualifying reason): re-run single-team mode — "Review the Dispatch team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Dispatch team — Q1 2027' (Confluence page 91112, DSP-OKR-Q1; owner Mei L.); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Core Systems** (Critical alignment finding AL-11 Circular dependency; roll-up B (3.08)): re-run single-team mode — "Review the Core Systems team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Core Systems team — Q1 2027' (Confluence page 91120, CORE-OKR-Q1; owner Adaeze O.); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Courier** (Critical alignment finding AL-11 Circular dependency; roll-up B (3.24)): re-run single-team mode — "Review the Courier (driver app) team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Courier team (driver app) — Q1 2027' (Confluence page 91116, COUR-OKR-Q1; owner Tomás R.); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Insights** (Critical alignment finding AL-11 Circular dependency; roll-up B (3.39)): re-run single-team mode — "Review the Insights team's Q1 2027 OKRs alone, in depth. Source: /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-repair-setlevel/candidate/fixture2-portfolio/input/sample-portfolio-2.md, section 'Insights team — Q1 2027' (Confluence page 91124, INS-OKR-Q1; owner Halima D.); strategy doc: the same file's 'Company Q1 2027 priorities' section (Confluence page 91050, CO-PRIO-Q1FY27)."
- **Accounts** does not qualify: its roll-up B (3.48) is above the needs-rework threshold and it carries no Critical finding — AP-05 Everything Is a P0 and its AL-08, AL-09 and AL-12 involvements are all Major.
