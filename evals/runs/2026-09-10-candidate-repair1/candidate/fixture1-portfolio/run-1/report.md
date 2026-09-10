# Brightledger — Q3 2026 OKR portfolio audit

**Scope (confirmed at intake):** 4 teams — Payments, Growth, Platform, Data — as enumerated in the export. **Period:** Q3 2026 (as stated by the file). **Sources:** `sample-portfolio.md` only (Confluence export of pages 88101, 88213, 88217, 88221, 88225, 88104); no Atlassian connection available, so no Jira/Confluence search was possible beyond this corpus. **Strategy source:** the "Company Q3 2026 priorities" section (page 88101, CO-PRIO-Q3). **Mode: portfolio (4 teams ≥ 2).**

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings.
The worst alignment risk is **AL-10 Strategy coverage gap**: company priority C4 (Brightledger Capital, dated Sep 30) has no objective, KR, or note in any of the four teams — a committed, dated company bet with zero owners in the portfolio.
Two more Criticals sit on the checkout funnel: Growth needs the new billing API six weeks before Payments ships it (**AL-06 Timeline mismatch**), and Payments' step-up verification push and Growth's checkout-conversion target pull the same surface in opposite directions with no acknowledgement on either page (**AL-02 Conflicting metrics / adversarial incentives**).
Platform is the portfolio's chokepoint: its page declares the quarter fully committed while Payments and Data both plan around Platform delivering for them (**AL-07 Resource contention**, **AL-01 Unacknowledged dependency**).
The most common goodness anti-pattern is **AP-04 KR Without Baseline** — 3 KRs across Growth and Platform state a target with no starting point. Two KRs (Platform, Data) are Critical because no system of record could ever score them (**AP-09 Metric Nobody Can Measure**).
Recommended first action: the CEO assigns or explicitly drops C4 this week; Payments and Growth then resequence the billing-API dependency before Aug 15.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 4 | 3 | 2 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| Data | 2 | 3 | 3 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.25) · Growth C (2.66) · Payments B (3.09).

- Platform: K5=1 — the developer-satisfaction score names no measuring system, and none exists in the corpus.
- Data: O4=1 — objective D1 traces to none of the four stated company Q3 priorities.
- Growth: O2=2 — "magical" and "machine" are abstractions two readers would gloss differently.
- Payments: K1=2 — the API v2 GA key result states no metric, baseline, or target.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: no "internal developer satisfaction score" is defined anywhere in the corpus and no survey, tool, or dashboard is named that could report it, so the KR can never be honestly scored; it also states no current value, and its success would not move an objective about uptime and cloud cost. Search performed: all four team sections, the company priorities section, and the Q2 business-review appendix of `sample-portfolio.md` were searched for a satisfaction or survey instrument — the only named measurement system in the whole corpus is the "Datadog SLO monitor" (line 89), which measures uptime.
- Scores affected: K5=0, K1=1, K3=2, K2=2 (KR capped at 1.0 by the K5=0 rule); PL1 per-OKR capped at 1.9 by the Critical anti-pattern cap.
- Suggested rewrite: "KR PL1.3: Median merge-to-production deploy time `<baseline>` min → `<target>` min, weekly from `<CI dashboard>`." [proposal — placeholder target] If the team wants the satisfaction measure itself, it belongs under a developer-experience objective, instrumented: "Quarterly developer survey (n ≥ `<respondents>`, run on `<survey tool>`): satisfaction `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" is never defined, "core tables" is never enumerated, and no test suite, dashboard, or check is named that could produce a number — unlike sibling KR D1.1, which names "the weekly exec-dashboard reconciliation check" (line 74). The KR can be declared achieved or missed at will. Search performed: all four team sections plus the appendix of `sample-portfolio.md`; the only data measurement systems named anywhere are Data's own reconciliation check (line 74) and the Datadog SLO monitor (line 89).
- Scores affected: K1=0, K5=0, K2=2, K3=2 (KR capped at 1.0); D1 per-OKR capped at 1.9 by the Critical anti-pattern cap.
- Suggested rewrite: "KR D1.3: Core tables passing every automated quality test on the nightly run `<baseline>`/`<n>` → `<n>`/`<n>`, reported weekly from `<data-quality dashboard>`." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (prior actual, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits 0.05 points *below* the already-achieved trailing-90-day actual, so the KR is satisfied by letting reliability degrade — it encodes no improvement and consumes a KR slot that could carry the enterprise-reliability work C2 asks for.
- Scores affected: K3=1, K1=3
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing-90-day actual, Datadog SLO monitor) → 99.97%, measured monthly on the same monitor." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb with no metric, no starting point, and no outside-moved measure, so it restates the work instead of measuring a result; and because it is done/not-done, it can only be scored 0% or 100% — the team has no steering signal at any point mid-quarter.
- Scores affected: K1=0, K2=1, K3=2 (KR capped at 1.0); PL2 per-OKR capped at 2.4 by the two-Major cap.
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence tasks closed 0/`<total tasks>` → `<total tasks>`/`<total tasks>`, with the auditor's final report received by `<date>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR is satisfied the moment the API is declared GA, whether or not a single transaction runs on it — it measures the team's own delivery, not any result a customer experiences, and it carries neither a baseline→target pair nor an adoption measure to make progress visible mid-quarter.
- Scores affected: K1=0, K2=1 (KR capped at 1.0); K7=2 for the P1 set.
- Suggested rewrite: "KR P1.2: Card checkout volume served by API v2 `<baseline>`% → `<target>`% by Sep 26, with authorization error rate no higher than v1's `<v1 error rate>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no starting value is given, so neither the ambition nor mid-quarter progress can be judged — 22% could be a stretch or already true today. Search performed: all four team sections plus the Q2 business-review appendix of `sample-portfolio.md`; the appendix reports Q2 actuals for uptime, chargebacks, step-up coverage, and qualified signups only (lines 89–91) — no trial-to-paid figure exists anywhere in the corpus.
- Scores affected: K1=2, K3=2 (calibration unverifiable)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, monthly signup cohorts, from `<funnel dashboard>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid distribution without any signup, activation, or revenue moving, so the number can be hit while the funnel objective is untouched; and with no starting value stated, 50,000 cannot be read as ambition either.
- Scores affected: K2=2, K1=2, K3=2, K7=2 for the G2 set; G2 per-OKR capped at 2.4 by the two-Major cap.
- Suggested rewrite: "KR G2.3 (aspirational): Qualified signups first-touch-attributed to the blog `<baseline>`/mo → `<target>`/mo, from `<analytics dashboard>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ all four teams
- Company priorities evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss, Payments): "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23) — a payments-platform delivery with no financing, underwriting, or design-partner content; it does not cover C4.
- Conflict: a dated, non-aspirational company priority with a hard Sep 30 deadline has zero contributing objectives or KRs anywhere in the portfolio, and no team's notes mention it. C1, C2 and C3 all have visible children (Growth's funnel KRs, Platform's "Complete the SOC 2 Type II audit." (line 63), Payments' "Reduce chargeback rate from 0.9% to 0.45% of transactions." (line 27)); C4 alone has none.
- Detection check that fired: AL-10 top-down strategy trace — each company objective searched across all teams' OKRs for coverage; C4 returned zero contributing children.
- Disconfirming checks run: re-searched under synonyms and program names across all four team sections and the appendix ("capital", "financ", "invoice-financing", "design partner", "lend", "underwrit") — the only hit in the entire corpus is line 13, the priority itself; checked C4's own line for a named owner outside the swept team set — none is named, so this is a portfolio hole rather than an ownership note; the nearest miss (Payments' API v2) is quoted above and does not count as coverage.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (every quote re-verified character-for-character against `sample-portfolio.md`)
- Recommended resolution owner: Dana W. (CEO, owner of the priorities page) to either assign C4 to a named team with an objective and a Sep 30-dated KR, or strike it from the Q3 priorities before mid-quarter.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41); dependency stated as "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date (Aug 15) precedes the producer's only stated delivery date (Sep 26) by roughly six weeks, so Growth's committed launch is scheduled on top of an API that does not exist yet — and the "should be fine" note shows the gap was never checked against the dates.
- Detection check that fired: AL-06 edge-date comparison on the dependency map — producer delivery date vs. consumer need-by date on the Growth→Payments billing-API edge.
- Disconfirming checks run: "late date ≠ inversion" — searched Payments' section for an earlier beta or preview milestone that could satisfy Growth's integration; the only date on the page is the Sep 26 GA, and Growth never names a milestone short of the API itself, so the tightest quotable reading stands; commitment labels checked on both pages — both state "KRs are committed unless marked (aspirational)." (lines 19, 36) and neither KR carries a label, so both are committed.
- Inference labels: none — all load-bearing text quoted; the inversion is arithmetic on two quoted dates.
- Verdict: CONFIRMED (both dates re-verified character-for-character against their pages)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree by end of July either an Aug 15 billing-API milestone Growth can build on, or a revised G1.3 launch date; whichever moves, the 300-upgrade target must be re-based on the remaining weeks.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is an added friction step on the checkout surface, and Payments plans to take it from roughly a third of transactions to nine in ten in the same quarter Growth commits to a ten-point conversion lift on that same surface; each team's success lever works directly against the other's number, and neither page mentions the other team.
- Detection check that fired: AL-02 surface-lever blocking key — both KRs sit on the checkout surface, step-up verification is a stated friction/risk control there, and the counterpart KR targets that surface's conversion metric.
- Disconfirming checks run: shared or parent OKR covering both — none found (the two objectives sit on different pages, 88213 and 88217, with no cross-reference); documented split of levers — none found; directionality — confirmed opposed at the mechanism level; commitment labels — neither KR is marked "(aspirational)", so both are committed under each page's stated convention (lines 19, 36). Separately, the lookalike pair Payments "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) vs. Growth's checkout conversion KR was generated by the metric-identity key and **killed**: different definitions and populations (card authorization success vs. self-serve signup checkout completion), same direction, no control lever on either side. That kill is per-candidate and does not affect the step-up pair.
- Inference labels: the verification→conversion friction mechanism is **analyst inference** — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against their pages; the mechanism remains labeled inference)
- Recommended resolution owner: Dana W. (CEO) or the product lead over both teams to convene Priya N. and Marcus T. within two weeks and set a shared guardrail pair — a chargeback ceiling plus a checkout-conversion floor — so one KR cannot be hit by breaking the other. Severity note: AL-02's default for a mechanism-level conflict is Major, escalated one level here because both objectives are committed under their pages' stated convention.

### [Major] AL-07 Resource contention: Platform ↔ Payments · Data
- Platform evidence (declared supply): "Q3 is fully committed between SOC 2 evidence collection and the cost work." and "Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30), serving "Ship checkout & billing API v2 to GA by Sep 26." (line 23)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82), serving "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (line 74)
- Conflict: two teams have committed KRs whose delivery depends on Platform capacity in Q3, while Platform's own page states that quarter is already fully committed to two other workstreams and that non-critical infra requests are held to Q4 — nobody has done the arithmetic, and both claims rest on assumptions ("assuming", "expect") rather than on anything Platform has agreed to in writing.
- Detection check that fired: AL-07 resource-node fan-in — every shared-resource mention across all teams grouped by owner; Platform came back with two distinct claimants in the same quarter, and the owner's page was then checked for declared supply.
- Disconfirming checks run: "plural demand ≠ contention" — Platform's page was searched for any allocation, capacity table, or scheduled commitment covering either claimant; none exists, and the only capacity statement is the fully-committed line quoted above (no Jira is available in this run, so the search is bounded by this corpus and stated as such); same-quarter check — all three pages are Q3 2026; same-resource check — both claims name Platform or the infra level, not similarly-named groups. The Payments edge is a pure provisioning ask (Platform's capacity itself), so it folds into this aggregate entirely rather than being filed separately; the Data edge additionally names a distinct deliverable and is filed as its own AL-01 below, cross-referencing this finding. The capacity arithmetic is reported once, here.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Elena R. (Platform) to state in writing before end of July which of the two asks Q3 can absorb; whichever is refused, that consumer's KR (Payments' Sep 26 GA or Data's schema-v2 KR) is re-scoped or re-dated in the same conversation.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82) — the dependency phrase is "rides on the streaming pipeline migration", and it carries Data's committed KR "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (line 74)
- Platform evidence (partial match, distinguished): Platform's entire Q3 set is "Maintain API uptime at or above 99.9%." / "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." / "Improve internal developer satisfaction score to 8/10." (lines 57–59) and "Close 100% of pen-test findings rated High or above (currently 7 open)." / "Complete the SOC 2 Type II audit." (lines 62–63), plus "Holding all non-critical infra requests until Q4." (line 65) — no pipeline, streaming, or event-infrastructure work appears in any of them.
- Conflict: Data's committed discrepancy KR is built on a streaming pipeline migration that Data explicitly does not own and has not sized, and the presumed owner's OKRs contain no such deliverable and an explicit hold on non-critical infra requests. Unlike the Payments provisioning ask, this is a distinct build the producer would have to plan as its own project, so it is a missing acknowledgment on top of — and cross-referenced to — the AL-07 Resource contention above.
- Detection check that fired: AL-01 edge-acknowledgment check on the dependency map — the Data→Platform edge's named deliverable was searched for in the producer's inventory and returned nothing.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — the producer's backlog would normally be searched next, but no Jira or Confluence connection is available in this run, so the search scope is the whole of `sample-portfolio.md`: all four team sections, the company priorities section, and the appendix were searched for "streaming", "pipeline", "schema", and "event"; the only hits in the corpus are Data's own line 74 and line 82. Platform's nearest statement is the Q4 hold quoted above, which points away from the work rather than toward it. Severity note: kept at the AL-01 default of Major rather than escalated, because Platform's hold covers "non-critical infra requests" generally and does not name this pipeline as deprioritized.
- Inference labels: the resolution of "the infra level" to the Platform team is **analyst inference** — Data never names Platform, though Platform is the only infrastructure-owning team in scope.
- Verdict: PLAUSIBLE — the ownership link is inferred rather than quoted, and the producer's backlog could not be searched in this run.
- Recommended resolution owner: Jonas K. (Data) to take the pipeline migration to Elena R. (Platform) before end of July and get it either onto Platform's plan with a date, or explicitly refused so D1.1 can be re-scoped.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to moving the same named metric from the same 31% baseline to two different targets in the same quarter, with no division of labor and no cross-reference — and Data's objective claims the surface "end-to-end" while Growth is independently running the same population. Whether the company's activation goal is 40% or 35% is unanswerable as written, and both teams can claim credit for the same movement.
- Detection check that fired: AL-03 clustering by target metric plus target population — "new-user activation rate", same 31% baseline, same new-signup population, in two teams' KRs; inconsistent targets within the cluster.
- Disconfirming checks run: "similar objectives ≠ duplication" — searched both team sections and all four teams' notes for a mutual reference, a shared owner, or an explicit lane split (Growth's note names only Payments (line 48); Data's note names only the infra level (line 82)); searched for different populations, surfaces or segments that would make this legitimate division of labor — both KRs say "new-user activation rate" over new signups with no segment qualifier; checked AL-08 as an alternative explanation — the shared 31% baseline shows the two teams are using the same measurement, so this is duplication, not a terminology collision; checked for a parent objective assigning lanes — the company priorities section (lines 10–13) names no activation owner.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to agree one owner and one target for new-user activation before mid-quarter; the other team's KR becomes a contributing input (for example Data's personalization experiments) measured on its own metric.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73), whose KRs measure "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0" (line 74) and "Cut critical-dashboard data latency from 6h to 1h." (line 75).
- Company priorities evidence: the full Q3 list is "C1 — Grow self-serve revenue" / "C2 — Become enterprise-ready" / "C3 — Cut fraud losses" / "C4 — Launch Brightledger Capital" (sample-portfolio.md › Company Q3 2026 priorities › lines 10–13).
- Conflict: D1 claims no parent, none of its KR metrics is a company-level metric or a documented driver of one, and no company priority mentions data quality, dashboards, or internal reporting — so a full objective's worth of Data's quarter serves nothing the company has declared. Data's own page offers no charter or justification for it either; the only capacity statement it makes is "we've sized our part at 3 engineer-months" (line 82).
- Detection check that fired: AL-04 three-way check — explicit parent link (none), KR metric that is a company-level metric or documented driver (none of C1–C4 names reporting accuracy or latency), mention in a department or company strategy page (none). Zero of three.
- Disconfirming checks run: "no parent link ≠ orphan" — re-read all four company priorities for an implied home for internal data quality and found none (C2's "complete SOC 2 Type II and hold enterprise-grade reliability." (line 11) covers audit and reliability, not analytics accuracy); searched Data's page for a self-justification or an exploratory charter that would kill the finding — none is present. Severity note: kept Minor by default, since the one quoted capacity figure ("3 engineer-months") is not stated as a large fraction of the team.
- Inference labels: none — all load-bearing text quoted; the absence claims name their search above.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against their pages)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to either state D1's parent priority explicitly on the page (the likeliest candidate being C2's enterprise-readiness reporting needs) or accept it as declared platform-health work outside the Q3 OKR set.

## 5. Prioritized action list

1. Assign company priority C4 to a named team with a Sep 30-dated KR, or strike it from the Q3 priorities — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Resequence the Growth↔Payments billing-API dependency — either an Aug 15 API milestone or a new G1.3 date, decided before end of July — owner: Priya N. (Payments) with Marcus T. (Growth) (resolves §4 AL-06 Timeline mismatch).
3. Convene Payments and Growth to set a shared checkout guardrail pair (chargeback ceiling plus conversion floor) within two weeks — owner: Dana W. (CEO) (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Replace the two unscoreable KRs with instrumented measures before the quarter's first check-in — owners: Elena R. (Platform) and Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure, both instances).
5. Publish Platform's Q3 capacity decision on the PCI-scoped infra and the streaming pipeline, and re-scope whichever consumer KR is refused — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
6. Take the streaming pipeline migration to Platform for a dated commitment or an explicit refusal — owner: Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
7. Agree one owner and one target for new-user activation rate, demoting the other team's KR to a contributing input — owner: Marcus T. (Growth) with Jonas K. (Data) (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Re-base the uptime KR on the quoted 99.95% trailing-90-day actual — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target).
9. Rewrite the four delivery-shaped and baseline-free KRs (P1.2, PL2.2, G1.1, G2.3) as baseline→target measures — owners: Priya N., Elena R., Marcus T. (resolves §3 AP-01 Task Masquerading as KR both instances, AP-04 KR Without Baseline, AP-03 Vanity Metric).
10. State D1's parent priority on the Data page or move it out of the Q3 OKR set — owner: Jonas K. (Data) (resolves §4 AL-04 Orphan objective).

## 6. Suggested single-team re-runs

No team's roll-up grade reaches the rubric's needs-rework threshold (all four are C or better), but each of the four teams carries at least one Critical finding, so all four qualify under criterion (b).

- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure on KR PL1.3): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88221 (PLAT-OKR-Q3), as exported in `sample-portfolio.md` › Platform team — Q3 2026; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Data** (roll-up C (2.25); Critical AP-09 Metric Nobody Can Measure on KR D1.3): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88225 (DATA-OKR-Q3), as exported in `sample-portfolio.md` › Data team — Q3 2026; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Growth** (roll-up C (2.66); Critical AL-06 Timeline mismatch and AL-02 Conflicting metrics / adversarial incentives): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88217 (GRW-OKR-Q3), as exported in `sample-portfolio.md` › Growth team — Q3 2026; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Payments** (roll-up B (3.09); Critical AL-06 Timeline mismatch and AL-02 Conflicting metrics / adversarial incentives): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88213 (PAY-OKR-Q3), as exported in `sample-portfolio.md` › Payments team — Q3 2026; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
