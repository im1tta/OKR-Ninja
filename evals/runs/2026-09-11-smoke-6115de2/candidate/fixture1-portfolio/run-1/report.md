# Brightledger — Q3 2026 portfolio OKR review

Mode: **portfolio** (4 teams in scope: Payments, Growth, Platform, Data). Period: Q3 2026, as stated by the source file. Strategy source: the "Company Q3 2026 priorities" section of the same file.
Corpus (only source read): `sample-portfolio.md` — full path `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md`. All source refs below use `sample-portfolio.md` with line numbers into that file.

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 9 Major, 0 Minor findings.
The worst alignment risk is AL-10 Strategy coverage gap: company priority C4 ("Launch Brightledger Capital") has zero coverage in all four teams' OKRs, with a stated Sep 30 date.
Two more Criticals sit on the checkout funnel: AL-06 Timeline mismatch (Growth commits to launching on the new billing API by Aug 15; Payments GAs it Sep 26) and AL-02 Conflicting metrics / adversarial incentives (Payments adds step-up verification friction while Growth targets +10pt checkout conversion).
The most common goodness issue is AP-04 KR Without Baseline (3 KRs across Growth and Platform state a target with no starting point).
Two KRs cannot be honestly scored at all (AP-09 Metric Nobody Can Measure — Platform and Data), and Platform is the unwitting supplier for two other teams' plans while its own page declares Q3 fully committed (AL-07 Resource contention).
Recommended first action: the CEO names an owner and a Q3 landing zone for C4 this week; Growth and Payments then resequence the Aug 15 / Sep 26 dependency before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| Data | 3 | 3 | 3 | 1 | 3 | 3 | 2 | 3 | 2 | 2 | 3 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.2) · Data C (2.4) · Growth C (2.7) · Payments B (2.8).

- Platform: K5=1 — "Improve internal developer satisfaction score to 8/10." names no measuring instrument anywhere.
- Data: O4=1 — "One trustworthy source of truth" traces to no stated company priority C1–C4.
- Growth: O2=2 — "magical" and "machine" are abstractions two readers would gloss differently.
- Payments: K1=2 — "Ship checkout & billing API v2 to GA by Sep 26." states no metric at all.

## 3. Per-team goodness findings

### Platform

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no "internal developer satisfaction score" is defined or instrumented anywhere in the corpus — searched all four team pages (lines 17–83), the company priorities page (lines 7–13) and the Q2 business review appendix (lines 86–91) for a survey, instrument or dashboard, and found none — so the number can never be honestly scored; and with no current value stated or retrievable, the 8/10 cannot be read as ambition or as progress.
- Scores affected: K5=0, K1=1, K3=2, K2=2 (KR capped at 1.0 by the K5=0 rule; OKR PL1 capped at 1.9)
- Suggested rewrite: "KR PL1.3: Quarterly internal developer survey (n ≥ `<respondents>`, run on `<named survey tool>`): developer satisfaction `<baseline>`/10 → 8/10, same instrument and question wording both quarters." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, other side of the corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits *below* the trailing-90-day actual the company's own Q2 review reports, so the KR is achieved by the system degrading slightly and demands no work — the definition of AP-06 Sandbagged Target.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing 90 days, Datadog SLO monitor) → 99.97%, measured monthly on the same monitor, with error-budget burn reported weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a completion verb with no metric, no baseline→target pair and no measure anyone outside Platform moves, so it restates the deliverable instead of measuring a result; and because it is a single done/not-done event, mid-quarter scoring can only ever be 0% or 100%, hiding slippage until the quarter ends.
- Scores affected: K1=0, K2=1, K3=2 (KR capped at 1.0 by the K1=0 rule; OKR PL2 capped at 2.4 by the two-Major rule)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence requests closed `<baseline>`/`<total>` → `<total>`/`<total>`, auditor fieldwork complete and report received by `<date>`, tracked weekly on the audit tracker." [proposal — placeholder target]

### Data

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" names no score, no threshold and no system of record — the only data check named anywhere in the corpus is "the weekly exec-dashboard reconciliation check" (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74), which measures cross-source discrepancies, not table quality — and "Significantly" supplies direction without magnitude, so no one can ever say whether the KR was hit.
- Scores affected: K5=0, K1=1, K3=2 (KR capped at 1.0 by the K5=0 rule; OKR D1 capped at 1.9)
- Suggested rewrite: "KR D1.3: Core-table data-quality failures — null-rate, freshness and referential checks failing across the `<N>` core tables, from `<named test suite>`, measured weekly — `<baseline>` → `<target>` failures per week." [proposal — placeholder target]

### Growth

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid promotion without any signup, activation or revenue moving, so the KR does not indicate the funnel outcome its objective claims; and stating 50,000 with no current value — none appears on the Growth page (lines 34–48) or in the Q2 review appendix (lines 86–91) — makes both its ambition and its progress unjudgeable.
- Scores affected: K2=2, K1=2, K3=2 (OKR G2 capped at 2.4 by the two-Major rule)
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed in `<analytics system>`, with blog sessions demoted to a health metric rather than a KR." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the KR states a target with no starting point, and no trial-to-paid figure exists anywhere in the corpus — searched the Growth page (lines 34–48), the other three team pages, the company priorities page (lines 7–13) and the Q2 business review appendix (lines 86–91), which reports only chargeback rate, step-up coverage, uptime and qualified signups — so neither the ambition nor mid-quarter progress can be judged.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<analytics system>`) → 22%, measured on trials started in the quarter." [proposal — placeholder target]

### Payments

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb plus a date with no metric, no baseline→target pair and no measure that anyone outside Payments moves — it succeeds the moment the release is cut, even if no traffic ever runs on v2; and as a single event it offers no gradient, so its only failure mode is lateness.
- Scores affected: K1=0, K2=1, K3=2 (KR capped at 1.0 by the K1=0 rule; OKR P1 capped at 2.4 by the two-Major rule)
- Suggested rewrite: "KR P1.2: Checkout & billing traffic served by API v2 `<baseline>`% → `<target>`% of transactions by Sep 26, with v2 error rate ≤ `<threshold>`, measured weekly on `<named dashboard>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments + Growth + Platform + Data
- Company evidence: "Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss, Growth): "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Conflict: C4 is a dated company priority with a hard Sep 30 date and zero contributing objectives or KRs in any of the four teams in scope; nobody in the portfolio is on the hook for the pilot.
- Detection check that fired: AL-10 top-down strategy trace — for each company objective, search all teams' OKRs for coverage; C4 returned zero contributing children.
- Disconfirming checks run: synonym and program-name re-search across lines 17–91 for "capital", "financ", "invoice-financing", "lending" and "design partner" — zero hits outside line 13, so no coverage hides under another name; the nearest miss quoted above is an onboarding activation metric that mentions invoices being *sent*, not invoice financing, and contributes nothing to the pilot; checked the company page for a named owner assigning C4 outside the swept team set — the page names only "Owner: Dana W. (CEO)" for the whole priorities page (line 8), so this is a portfolio hole, not an ownership note against an out-of-scope function.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 13 and 40)
- Recommended resolution owner: Dana W. (CEO) to name an accountable team and a Q3 landing zone for C4 within one week, or to restate C4 as a Q4 priority — the Sep 30 date cannot survive a staffing decision taken much later.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41) — with the dependency stated in Growth's own notes: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's launch date (Aug 15) precedes its dependency's GA date (Sep 26) by roughly six weeks, so Growth's committed launch — and the 300 upgrades that ride on it — cannot happen as sequenced; the integration margin is not thin, it is negative.
- Detection check that fired: AL-06 dependency-map date comparison — producer's delivery date vs. consumer's need-by date on the Growth → Payments edge; hard inversion.
- Disconfirming checks run: "late date ≠ inversion" — checked which milestone Growth actually needs; Growth's note names only "the new billing API" with no beta, preview or partial-availability milestone, and Payments' page names only GA (line 23), so no earlier quotable milestone exists that Aug 15 could ride on; commitment levels checked — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 19 and 36) and neither KR is marked aspirational, which is what makes this Critical rather than Major; checked for awareness plus a resolution plan — Growth's only hedge is "should be fine", which asserts the opposite of a plan.
- Inference labels: none — all load-bearing text quoted; the link from G1.3 to Payments' API v2 is quoted rather than inferred, since Growth's note names both the billing API and G1.3 by ID.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 41, 48 and 23)
- Recommended resolution owner: Marcus T. (Growth) and Priya N. (Payments) to agree within two weeks either an earlier partial-availability date for the upgrade endpoints or a revised G1.3 launch date after GA, and to restate the 300-upgrade target against the surviving window.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and Payments is committing to apply it to nearly three times as many transactions (35% → 90%) in the same quarter that Growth commits to a 10-point lift in checkout conversion on that surface; neither page mentions the other team, so nobody owns the trade-off.
- Detection check that fired: AL-02 surface-lever blocking key — both KRs touch the checkout surface, Payments' stated lever (step-up verification coverage) is a friction control there, and Growth targets that surface's conversion metric. The metric-identity key generated nothing for this pair; the two KRs share no canonical metric name.
- Disconfirming checks run: shared or parent OKR covering both — none found; the objectives are "Cut fraud losses without drama" (line 26) and "Turn our funnel into a machine" (line 43), with no joint owner and no cross-reference on either page; documented split of levers — none found anywhere in lines 17–48; directionality — confirmed coupled and opposing (more verification challenges on the same checkout flow whose completion Growth must raise); commitment labels — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 19 and 36) and neither KR is marked aspirational, which escalates the default Major for a mechanism-level conflict to Critical. Separately, the lookalike pair Payments "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) ↔ Growth's line 44 was generated and **killed** — different definitions and populations (card transactions vs. self-serve signups), same direction, no control lever on either side — and that kill does not touch this candidate.
- Inference labels: the verification-friction → conversion-drop mechanism is **analyst inference** — no Brightledger document in this corpus states the trade-off.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. within two weeks and set a shared guardrail pair — a chargeback ceiling and a checkout-conversion floor (`<ceiling>`% / `<floor>`%) — plus a risk-scored step-up rollout so coverage rises only where fraud risk justifies the friction [proposal — placeholder target].

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed Q3 plans draw on Platform's capacity in the same quarter in which Platform declares that capacity already fully spent and defers infra requests to Q4 — combined demand exceeds declared supply, and neither claimant's page shows the arithmetic ever being done. Payments' ask is a pure provisioning/capacity claim and is aggregated here in full; Data's ask additionally names a distinct deliverable and earns the separate AL-01 finding below, which cross-references this one. The capacity arithmetic is reported once, here.
- Detection check that fired: AL-07 resource-node fan-in — grouping every external-team mention by resource put two claimants on Platform for Q3, and Platform's own page, checked for declared supply, yields the fully-committed statement.
- Disconfirming checks run: "plural demand ≠ contention" — searched Platform's whole section (lines 52–66) for an allocation covering either claimant, using the terms "PCI", "provision", "pipeline", "stream", "schema", "event" and "data", and found zero hits, so no documented allocation exists on the OKR page; no Jira, capacity table or allocation link exists in this corpus and Platform's page references none, so the "allocated outside the OKR pages" falsification could not be established; confirmed both claims fall in the same quarter (all four pages are titled "Q3 2026") and name the same team, not similarly-named groups.
- Inference labels: that "the infra level" in Data's note denotes the Platform team is **analyst inference** — Data's note names no team; the resource identity on the Payments edge is quoted ("Platform provisions this in July").
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 30, 82 and 65)
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 allocation decision within one week — which of the PCI-scoped infra and the streaming pipeline migration, if either, fits inside the committed quarter — so Payments and Data can re-plan against a real answer rather than against "as discussed in standup".

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82) — dependency phrase: "rides on the streaming pipeline migration"; the dependent KR is "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (closest partial match on the producer's side): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: the streaming pipeline migration is a distinct deliverable someone must plan and build, and it appears nowhere in Platform's objectives, KRs or notes; Data's committed KR D1.1 depends on it while Data has sized only "our part" and assumes the rest happens "at the infra level". Cross-reference: this edge also feeds the AL-07 Resource contention finding above, which carries the capacity arithmetic; this finding is the missing acknowledgment of the deliverable itself.
- Detection check that fired: AL-01 edge-acknowledgment check — resolve the dependency mention to its owning team, then search that owner's OKRs for the deliverable; no hit.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched Platform's entire section (lines 52–66: objectives PL1 and PL2, all five KRs and the team notes) for "pipeline", "stream", "schema", "event", "warehouse" and "data", returning zero hits; no Jira or backlog source exists in this corpus and Platform's page links none, so no scheduled-epic downgrade could be established; the closest partial match is Platform's capacity note quoted above, which does not cover the need — it defers infra requests rather than committing the migration.
- Inference labels: that "the infra level" denotes the Platform team is **analyst inference** (Data's note names no team); the deliverable itself and Data's dependence on it are quoted.
- Verdict: PLAUSIBLE — every quote re-verified against lines 82, 74 and 65, but the producer-side identification rests on the inferred reading of "at the infra level", so the finding is not promoted to CONFIRMED.
- Recommended resolution owner: Jonas K. (Data) to take the streaming pipeline migration to Elena R. (Platform) within one week and get it either scheduled with an owner and a date or explicitly declined — and, if declined, to re-scope KR D1.1 before the quarter's midpoint.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to the same metric, on the same population, from the same 31% baseline, to two different targets (40% vs 35%) in the same quarter — so no one is accountable for a single number, and both teams run onboarding work on one surface with no division of labour; Data's objective goes further and claims the surface outright: "Own onboarding personalization end-to-end" (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 78).
- Detection check that fired: AL-03 clustering by target metric + target population — "new-user activation rate", new signups, same quarter, same 31% baseline — followed by the mutual-reference check, which found none.
- Disconfirming checks run: "similar objectives ≠ duplication" — searched Growth's section (lines 34–48) for any mention of the Data team or its owner and Data's section (lines 69–83) for any mention of Growth or its owner: zero hits either way, so there is no cross-reference, no shared epic, no joint owner and no quoted lane split by surface, segment or geography; checked the company priorities page (lines 7–13) for a parent objective assigning lanes — none exists; checked whether an AL-08 definition split explains the two targets — Growth defines activation as "first invoice sent within 7 days" while Data states no definition, so the gap is a target disagreement rather than a documented population difference (AL-08 Terminology collision cross-referenced as secondary rather than double-counted; the root cause is the undivided duplicate work).
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 40 and 80)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to agree one owner and one activation target before mid-quarter — e.g. Data owning the personalization surface, Growth owning the funnel number — and to publish the shared activation definition alongside it.

### [Major] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73), whose KRs are "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (line 74), "Cut critical-dashboard data latency from 6h to 1h." (line 75) and "Significantly improve data quality across core tables." (line 76)
- Company evidence: "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." / "complete SOC 2 Type II and hold enterprise-grade reliability." / "bring chargeback rate under 0.5% after the Q2 incident." / "invoice-financing pilot live with 3 design partners by Sep 30." (sample-portfolio.md › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent priority, and none of its three KR metrics is a company-level metric or a stated driver of one — the four company priorities are self-serve ARR, SOC 2 and reliability, chargeback rate, and the Capital pilot; internal dashboard reconciliation and data latency serve none of them without an unstated assumption.
- Detection check that fired: AL-04 three-way check — (a) explicit parent link: absent; (b) a KR metric that is a company-level metric or a documented driver of one: none of the three matches C1–C4; (c) a mention in a department strategy page: no department page exists in this corpus. Zero of three.
- Disconfirming checks run: "no parent link ≠ orphan" — ran all three legs above rather than flagging on the missing label alone; searched the Data page (lines 69–83) for the team's own justification or charter, which would downgrade or kill the finding, and found only "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (line 82) — a sizing statement that names no strategic parent and states no fraction of team capacity; note that the team's *other* objective, D2, does trace (its activation KR is a driver of C1), so this is one orphan objective, not an unanchored team.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 73–76 and 10–13)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to state D1's parent priority explicitly — or to re-frame D1 around the priority it actually serves — before the quarter's midpoint. Severity is raised one level from AL-04's Minor default because the Data page marks these KRs committed: "Commitment: KRs are committed unless marked (aspirational)." (sample-portfolio.md › Data team — Q3 2026 › line 71).

## 5. Prioritized action list

1. Name an accountable team and a Q3 landing zone for company priority C4, or move it to Q4 — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Resequence the self-serve upgrade launch against the billing API v2 GA date and restate the 300-upgrade target — owners: Marcus T. (Growth) and Priya N. (Payments) (resolves §4 AL-06 Timeline mismatch).
3. Set a joint chargeback-ceiling / checkout-conversion-floor guardrail pair and a risk-scored step-up rollout — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Replace the developer-satisfaction KR with a named survey instrument, baseline and target, or drop it — owner: Elena R. (Platform) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
5. Replace "Significantly improve data quality across core tables." with a counted check-failure metric from a named test suite — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
6. Publish a Q3 infra allocation decision covering the PCI-scoped infra and the streaming pipeline migration — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
7. Get the streaming pipeline migration scheduled or explicitly declined, then re-scope KR D1.1 accordingly — owner: Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
8. Agree one owner, one activation target and one shared activation definition for new-user activation — owners: Marcus T. (Growth) and Jonas K. (Data) (resolves §4 AL-03 Duplicated / overlapping objectives).
9. State D1's parent company priority explicitly, or re-frame the objective around the priority it serves — owner: Jonas K. (Data) (resolves §4 AL-04 Orphan objective).
10. Rewrite the four remaining defective KRs against their quoted baselines — uptime against the 99.95% Q2 actual, both delivery KRs as adoption measures, and the two baseline-free targets — owners: Elena R. (Platform), Priya N. (Payments), Marcus T. (Growth) (resolves §3 AP-06 Sandbagged Target, both AP-01 Task Masquerading as KR blocks, AP-04 KR Without Baseline and AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.2); qualifies on the Critical AP-09 Metric Nobody Can Measure, alongside AP-06 Sandbagged Target, AP-01 Task Masquerading as KR and inbound AL-07 Resource contention / AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: the 'Platform team — Q3 2026' section of `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3), together with the Q2 2026 business review appendix in the same file; strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Data** (roll-up C (2.4); qualifies on the Critical AP-09 Metric Nobody Can Measure, alongside AL-04 Orphan objective, AL-01 Unacknowledged dependency and AL-03 Duplicated / overlapping objectives): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: the 'Data team — Q3 2026' section of `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md` (Confluence page 88225, DATA-OKR-Q3), together with the Q2 2026 business review appendix in the same file; strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Growth** (roll-up C (2.7); qualifies on the Critical AL-06 Timeline mismatch and AL-02 Conflicting metrics / adversarial incentives, alongside AP-03 Vanity Metric and AP-04 KR Without Baseline): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: the 'Growth team — Q3 2026' section of `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md` (Confluence page 88217, GRW-OKR-Q3), together with the Q2 2026 business review appendix in the same file; strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Payments** (roll-up B (2.8) — above the needs-rework threshold, so it qualifies solely on the Critical alignment findings AL-06 Timeline mismatch and AL-02 Conflicting metrics / adversarial incentives): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: the 'Payments team — Q3 2026' section of `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-portfolio/input/sample-portfolio.md` (Confluence page 88213, PAY-OKR-Q3), together with the Q2 2026 business review appendix in the same file; strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
