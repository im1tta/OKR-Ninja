# Brightledger — Q3 2026 OKR Portfolio Review

*Mode: portfolio (4 teams in scope: Payments, Growth, Platform, Data) · Period: Q3 2026 · Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` (single canonical corpus; no Atlassian sources available) · Strategy source: the file's "Company Q3 2026 priorities" section (C1–C4)*

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 7 Critical, 6 Major, 1 Minor findings.
The portfolio's biggest threat is AL-07 Resource contention: Payments and Data both build committed Q3 KRs on Platform infra work while Platform's own page declares Q3 capacity fully committed and defers infra requests to Q4 — nobody has done the arithmetic.
Three more Critical collisions sit behind it: Growth needs the new billing API by Aug 15 while Payments ships it Sep 26 (AL-06 Timeline mismatch); Payments takes step-up verification to 90% of transactions while Growth commits to +10pt checkout conversion on the same surface (AL-02 Conflicting metrics / adversarial incentives); and company priority C4 (Brightledger Capital) has zero contributing objectives anywhere in the portfolio (AL-10 Strategy coverage gap).
The most common quality issue is AP-04 KR Without Baseline (4 KR instances across Growth, Platform and Data), and two KRs — Platform's developer-satisfaction score and Data's "data quality" KR — can never be honestly scored at all (AP-09 Metric Nobody Can Measure, Critical).
Grades: Platform C (2.15) · Data C (2.23) · Growth C (2.64) · Payments B (2.77) — no team is above B.
Recommended first action: a Platform/Payments/Data capacity reconciliation before mid-quarter, because two committed KRs and two other findings depend on its outcome.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| Data | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 3 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.23) · Growth C (2.64) · Payments B (2.77).

- Platform: K5=1 — "internal developer satisfaction score" names no instrument that exists (AP-09 Metric Nobody Can Measure).
- Data: K1=2 — "Significantly improve data quality" states neither metric nor target (AP-09, AP-04).
- Growth: K1=2 — two KRs state targets with no baseline anywhere in the corpus (AP-04 KR Without Baseline).
- Payments: K1=2 — the API v2 GA KR is a ship date, not a measurement (AP-01 Task Masquerading as KR).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no survey, instrument, or dashboard defining a "developer satisfaction score" exists anywhere in the corpus — searched all four team OKR pages, the company priorities page, and the Q2 business-review appendix, whose only named instrument is in "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (same file › Appendix — Q2 2026 business review (extracts) › line 89) — so the KR can never be honestly scored; it also states no current value, leaving "8/10" unjudgeable as ambition or progress.
- Scores affected: K5=0, K1=1, K3=2 (KR capped at 1.0; objective PL1 capped at 1.9 by the Critical anti-pattern cap)
- Suggested rewrite: "KR PL1.3: Quarterly internal developer survey (n ≥ `<respondents>`, run in `<named survey tool>`): developer satisfaction `<baseline>`/10 → 8/10, same instrument and question wording each quarter." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (same file › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing actual, so the KR is met by doing nothing new and would still score green through a reliability regression — while the company priority it serves reads "**C2 — Become enterprise-ready:** complete SOC 2 Type II and hold enterprise-grade reliability." (same file › Company Q3 2026 priorities › line 11).
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing-90-day actual, Datadog SLO monitor) → 99.97%, reported monthly, with no calendar month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: a completion verb with no metric and no baseline→target pair — it measures that the team finished a task, not that any enterprise customer trusts Brightledger more; and it can only be scored 0% or 100%, so it gives leadership no steering signal until the audit lands.
- Scores affected: K1=0, K2=1, K3=2 (KR capped at 1.0)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence tasks closed `<baseline>`/`<total>` → `<total>`/`<total>` by `<date>`, auditor's Type II report received by `<date>` with zero qualified exceptions." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no data-quality score, check, or dashboard is defined for this anywhere in the corpus — searched all four team pages, the company priorities page, and the Q2 appendix; the only named instrument on Data's own page is "the weekly exec-dashboard reconciliation check" (same file › Objective D1: One trustworthy source of truth › line 74), which counts cross-source discrepancies rather than table quality — so "Significantly" can be claimed or denied at will, and the KR states neither a starting value nor a target.
- Scores affected: K1=0, K5=0, K3=2 (KR capped at 1.0; objective D1 capped at 1.9 by the Critical anti-pattern cap)
- Suggested rewrite: "KR D1.3: Core-table rows failing the `<named data-quality suite>` checks `<baseline>`% → `<target>`%, run daily across the `<N>` core tables and reported on the same weekly dashboard as D1.1." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the KR states a target with no starting point, and none is retrievable — searched all four team OKR pages, the company priorities page, and the Q2 business-review appendix, which reports only uptime, chargeback rate, step-up coverage, and "Qualified signups averaged 2,100/mo across Q2." (same file › Appendix — Q2 2026 business review (extracts) › line 91) — so neither the ambition nor mid-quarter progress can be judged.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<funnel dashboard>`) → 22%, monthly signup cohorts measured 30 days after trial start." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Evidence (commitment label on the same KR): "*(aspirational)*" (same file › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing cadence and paid distribution without indicating that the funnel converts anything, so the KR can be hit while the objective's own conversion and signup KRs miss; and no current pageview figure appears anywhere in the corpus (searched all four team pages, the priorities page, and the Q2 appendix), so 50,000 is unanchored.
- Scores affected: K1=2, K2=2, K3=2, K7=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed first-touch in `<attribution report>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery event with no metric and no baseline→target pair — it succeeds on the GA date even if no traffic moves to v2 and checkout gets no easier for customers; and until Sep 26 it can only be scored 0% or 100%, which is also why the Growth dependency on it (§4 AL-06 Timeline mismatch) carries no visible progress signal.
- Scores affected: K1=0, K2=1, K3=2 (KR capped at 1.0)
- Suggested rewrite: "KR P1.2: Card transaction volume served by checkout & billing API v2 0% → `<target>`% by Sep 26, with v2 error rate ≤ `<threshold>` (source: `<checkout dashboard>`)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (same file › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (same file › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs (P1.2 and D1.1) assume Platform capacity inside Q3, while Platform's own page declares that quarter fully committed to other work and defers infra requests to Q4 — combined demand exceeds the only stated supply and no page shows anyone reconciling it. Payments' ask is a pure provisioning/capacity claim and folds into this aggregate entirely; Data's edge additionally names a distinct deliverable and is reported separately below (AL-01), with the capacity arithmetic counted only once, here.
- Detection check that fired: AL-07 resource-node fan-in — grouping every dependency mention by resource puts two Q3 claimants on Platform infra; checking the resource owner's own page for declared supply yields the fully-committed statement.
- Disconfirming checks run: "Plural demand ≠ contention" — allocation outside OKR pages: no Jira/roadmap source is in scope (local file only) and Platform's page names no allocation, epic, or reserved capacity for either claimant, so nothing falsifies the arithmetic; same-quarter check — all three pages are headed Q3 2026 ("Payments team — Q3 2026" line 17, "Platform team — Q3 2026" line 52, "Data team — Q3 2026" line 69); same-resource check — both asks land on Platform-owned infrastructure, not similarly-named groups. Result: the finding survives.
- Inference labels: resolving Data's "handled at the infra level" to the Platform team is analyst inference — Data's note never names Platform; Payments' edge names Platform verbatim.
- Verdict: CONFIRMED (all three quotes re-opened and matched character-for-character against their source lines)
- Recommended resolution owner: Platform lead (Elena R.) to convene Priya N. and Jonas K. and publish a Q3 infra allocation — which of the PCI-scoped provisioning and the streaming pipeline migration Platform will take, by what date, and what the other team must re-plan — before mid-quarter.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74); dependency phrase: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (same file › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Holding all non-critical infra requests until Q4." (same file › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Data's committed KR D1.1 requires a streaming pipeline migration that Data explicitly does not own, and that deliverable appears in no team's objectives, KRs, or notes anywhere in the portfolio; the presumed owner has instead deferred non-critical infra requests to Q4, after the KR must land.
- Detection check that fired: AL-01 edge acknowledgment — resolving the dependency phrase's named work ("the streaming pipeline migration") to an owning team and searching that owner's OKRs for the deliverable, with no hit.
- Disconfirming checks run: "Missing mention ≠ unacknowledged" — no Jira/backlog source exists in scope, so the absence search covered the whole corpus (all four team pages, the company priorities page, the Q2 appendix) for "streaming", "pipeline", "migration", "schema", and "event": zero hits outside Data's own two lines. Partial-match check — Platform's nearest items are "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (same file › Objective PL1: Keep the lights on, cheaper › line 58) and "Complete the SOC 2 Type II audit." (same file › Objective PL2: Earn enterprise trust › line 63); neither covers a pipeline migration. Result: absence stands, and the Minor downgrade for work sitting in a backlog cannot apply because no backlog is visible.
- Inference labels: the owner attribution — that "the infra level" means the Platform team — is analyst inference; the deliverable's absence from every page in scope is searched-and-quoted, not inferred. Cross-reference: AL-07 Resource contention (root cause for the capacity arithmetic, reported once, above).
- Verdict: PLAUSIBLE (both quotes verified verbatim; the producer-side attribution rests on an inferred link, so the finding does not claim CONFIRMED)
- Recommended resolution owner: Data lead (Jonas K.) to obtain a named owner and date for the streaming pipeline migration from Platform within two weeks, or re-scope D1.1 to the events Data can serve without it.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41); dependency phrase: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (same file › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (same file › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date (Aug 15) precedes the producer's delivery date (Sep 26) by roughly six weeks — a hard inversion with no integration margin at all, on KRs both pages mark committed by convention ("Commitment: KRs are committed unless marked (aspirational)." — Growth line 36; Payments line 19).
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer delivery date vs. consumer need-by date on the Growth → Payments billing-API edge.
- Disconfirming checks run: "Late date ≠ inversion" — searched Payments' page for an earlier beta/EAP/limited-availability milestone Growth's integration could ride on; the page states only GA on Sep 26, and Growth's note names no alternative milestone. Awareness/resolution-plan check — Growth's note shows contact ("Marcus synced with Priya in June") but its conclusion, "should be fine", states no date, no milestone, and no plan, so it does not downgrade the finding. Result: the inversion stands.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both dated statements re-opened and matched character-for-character)
- Recommended resolution owner: Payments lead (Priya N.) with Growth lead (Marcus T.) — agree by end of July either a dated pre-GA billing-API milestone Growth can build on or a revised G1.3 launch date, and record it on both pages.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (same file › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and taking its coverage from 35% to 90% of transactions predictably suppresses the completion metric Growth commits to raising by ten points in the same quarter; neither page mentions the other team's target, so the tradeoff is nobody's decision.
- Detection check that fired: AL-02 surface-lever key — both KRs sit on the checkout surface, Payments' stated lever ("step-up verification coverage") is a verification/friction control there, and Growth targets that surface's conversion metric. The metric-identity key generates nothing for this pair; the surface-lever key does.
- Disconfirming checks run: shared or parent OKR covering both — none; the two objectives trace to different company priorities ("**C3 — Cut fraud losses:** bring chargeback rate under 0.5% after the Q2 incident." line 12 and "**C1 — Grow self-serve revenue:** mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." line 10). Documented split of levers — searched both pages' notes; Payments' note discusses infra and priority C3, Growth's discusses the billing API, neither allocates checkout friction. Directionality — Payments' lever raises friction while Growth's metric requires reducing it: opposed. Lookalike control — the pair "Raise checkout success rate from 91.2% to 95% for card transactions." (same file › Objective P1: Make checkout something customers never think about › line 22) vs. Growth's conversion KR was also generated on this surface and killed (different definitions and populations, same direction, no control lever on either side); that per-candidate kill does not remove the checkout surface from generation, and this candidate survives on its own lever.
- Inference labels: the friction → conversion mechanism is analyst inference — no Brightledger document states the tradeoff.
- Verdict: CONFIRMED (both quotes re-opened and matched character-for-character)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. and set a shared guardrail pair — a `<chargeback ceiling>` alongside a `<self-serve conversion floor>` — plus a risk-segmented step-up policy, within two weeks [proposal — placeholder target].

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company evidence: "**C4 — Launch Brightledger Capital:** invoice-financing pilot live with 3 design partners by Sep 30." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss, distinguished): "Ship checkout & billing API v2 to GA by Sep 26." (same file › Objective P1: Make checkout something customers never think about › line 23) — the only KR in the portfolio creating new commercial surface area, and it is a payments/billing API with no financing, lending, or design-partner content.
- Conflict: a dated company priority with a hard Sep 30 deadline has zero contributing objectives or KRs across all four teams in scope — the portfolio has a hole, and whoever is meant to deliver the pilot is not in this OKR set.
- Detection check that fired: AL-10 top-down strategy trace — for each of C1–C4, search all teams' OKRs for coverage; C1, C2, and C3 each resolve to at least one team objective, C4 resolves to none.
- Disconfirming checks run: "Zero hits ≠ coverage gap" — re-searched all four team pages, their notes, and the Q2 appendix under synonyms and program names ("Capital", "invoice financing", "financing", "lending", "design partner", "pilot"): zero hits. Named-owner check on the priority's own page — C4 names no owning function, and the page's only named owner is "Dana W. (CEO)" (same file › Company Q3 2026 priorities › line 8), so this is not a priority explicitly assigned to a function outside the swept team set.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (the priority line and the near-miss KR both re-verified verbatim)
- Recommended resolution owner: Dana W. (CEO) to name an owning team for C4 and either add a Q3 objective for the pilot or restate C4's date, before the quarter's mid-point — three design partners by Sep 30 is unreachable if no team has started.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (same file › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to the same metric on the same population from the same 31% baseline, with inconsistent targets (40% vs. 35%) and no stated division of labor, so nobody is accountable for the number — and Data's objective claims the surface outright: "Own onboarding personalization end-to-end" (same file › Objective D2: Own onboarding personalization end-to-end › line 78). Cross-reference: AL-08 Terminology collision — only Growth's page defines the metric ("first invoice sent within 7 days"), Data's KR states no definition, so the two targets may not even measure the same event.
- Detection check that fired: AL-03 clustering by target metric plus target population/surface — "new-user activation rate", new signups, same quarter, two teams in one cluster.
- Disconfirming checks run: "Similar objectives ≠ duplication" — searched both pages for a mutual reference, shared epic, joint owner, or explicit lane split; Growth's note names only the billing-API sync with Payments ("Marcus synced with Priya in June", line 48) and Data's note names only its pipeline dependency (line 82); the company priorities page assigns no lanes. Different-population check — neither page states a segment, surface, or geography that would separate the two; both write "new-user activation rate" from 31%. Result: duplication stands.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both KRs re-opened and matched character-for-character)
- Recommended resolution owner: VP Product to assign one accountable team and one target for new-user activation, recording the other team's contribution as a supporting KR, before the first monthly check-in.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 73)
- Company evidence: "**C1 — Grow self-serve revenue:** mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." · "**C2 — Become enterprise-ready:** complete SOC 2 Type II and hold enterprise-grade reliability." · "**C3 — Cut fraud losses:** bring chargeback rate under 0.5% after the Q2 incident." · "**C4 — Launch Brightledger Capital:** invoice-financing pilot live with 3 design partners by Sep 30." (same file › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent and the three-way trace finds none — its metrics (cross-source discrepancies, dashboard latency) are not company-level metrics and no priority names them as a driver; the priorities page never mentions data, reporting, or dashboards.
- Detection check that fired: AL-04 three-way check on the strategy trace — (a) explicit parent link: absent; (b) a KR metric that is a company metric or a documented driver of one: none of C1–C4's metrics (ARR, SOC 2, chargeback rate, financing pilot) appears in D1's KRs; (c) mention in a strategy page: none.
- Disconfirming checks run: "No parent link ≠ orphan" — all three legs were run before flagging, and inferred parents were counted against the finding, not for it. Team self-justification check — Data's page offers only a sizing statement, "we've sized our part at 3 engineer-months" (same file › Objective D2: Own onboarding personalization end-to-end › line 82), which states cost, not a parent, and names no fraction of team capacity, so the Major escalation condition is not met and the finding stays Minor.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (objective and priority lines re-verified verbatim)
- Recommended resolution owner: Data lead (Jonas K.) to state D1's parent priority explicitly at the next portfolio review, or have the CEO add a data-trust priority — exec-dashboard trust may deserve a pillar, but today it has none.

## 5. Prioritized action list

1. Convene Platform, Payments, and Data to publish one Q3 infra allocation covering the PCI-scoped provisioning and the streaming pipeline migration — owner: Elena R., Platform lead (resolves §4 AL-07 Resource contention and §4 AL-01 Unacknowledged dependency).
2. Agree either a dated pre-GA billing-API milestone or a revised G1.3 launch date, recorded on both pages — owner: Priya N. with Marcus T. (resolves §4 AL-06 Timeline mismatch).
3. Set a shared checkout guardrail pair (chargeback ceiling plus self-serve conversion floor) and a risk-segmented step-up policy — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Name an owning team for company priority C4 and add its Q3 objective, or restate C4's date — owner: Dana W., CEO (resolves §4 AL-10 Strategy coverage gap).
5. Rewrite PL1.3 against a named survey instrument with a stated baseline, or move developer satisfaction to a health metric outside the OKRs — owner: Elena R. (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
6. Rewrite D1.3 against a named data-quality check with baseline and target, and state D1's parent priority or retire the objective — owner: Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure — Data and §4 AL-04 Orphan objective).
7. Assign one accountable team and one target for new-user activation, with the other team's work recorded as a supporting KR — owner: VP Product (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Re-baseline the uptime KR to the quoted 99.95% trailing actual and set a target above it — owner: Elena R. (resolves §3 AP-06 Sandbagged Target).
9. Convert the two delivery KRs (P1.2 and PL2.2) into adoption and closure ratios with baselines — owners: Priya N. and Elena R. (resolves §3 AP-01 Task Masquerading as KR, both instances, each with AP-02 Binary KR with No Gradient).
10. Add a baseline to G1.1 and replace the blog-pageview KR with a blog-sourced signup measure — owner: Marcus T. (resolves §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure on PL1.3, plus Critical AL-07 Resource contention): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (page 88101, CO-PRIO-Q3); prior-period actuals: the 'Appendix — Q2 2026 business review (extracts)' section (page 88104)."
- **Data** (roll-up C (2.23); Critical AP-09 Metric Nobody Can Measure on D1.3, plus Critical AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (page 88101, CO-PRIO-Q3); prior-period actuals: the 'Appendix — Q2 2026 business review (extracts)' section (page 88104)."
- **Growth** (roll-up C (2.64); qualifies on the Critical alignment findings AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (page 88101, CO-PRIO-Q3); prior-period actuals: the 'Appendix — Q2 2026 business review (extracts)' section (page 88104)."
- **Payments** (roll-up B (2.77); qualifies on the Critical alignment findings AL-02 Conflicting metrics / adversarial incentives and AL-07 Resource contention): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (page 88101, CO-PRIO-Q3); prior-period actuals: the 'Appendix — Q2 2026 business review (extracts)' section (page 88104)."
