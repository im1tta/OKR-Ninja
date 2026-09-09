# Brightledger — Q3 2026 OKR Portfolio Review

*Scope: Payments, Growth, Platform, Data (4 teams — portfolio mode). Period: Q3 2026, as stated by the source file. Strategy source: the "Company Q3 2026 priorities" section (Confluence page 88101, CO-PRIO-Q3). Sole source: `sample-portfolio.md`. No Atlassian connection was available; all source refs are local-file refs into that export.*

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 10 Major, 1 Minor findings.
The worst alignment risk is AL-07 Resource contention: Payments and Data both stake committed Q3 KRs on Platform infrastructure work while Platform's own page declares its quarter full and defers infra requests to Q4 — three committed KRs across three teams sit behind one closed door.
Two further Criticals compound it: AL-06 Timeline mismatch (Growth needs the billing API six weeks before Payments ships it) and AL-10 Strategy coverage gap (company priority C4, Brightledger Capital, has zero coverage in any of the four teams' OKRs).
The most common goodness anti-pattern is AP-04 KR Without Baseline — 3 instances across 2 teams (Growth's G1.1 and G2.3, Platform's PL1.3), each stating a target with no starting point.
Two KRs are unmeasurable as written (AP-09 Metric Nobody Can Measure, one each in Platform and Data), so neither can be honestly scored at quarter end.
No team reaches the needs-rework threshold on roll-up grade, but every team carries at least one Critical finding.
Recommended first action: Platform, Payments and Data leads reconcile the Q3 infra queue against Platform's stated capacity before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 2 | 2 | 3 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 3 |
| Platform | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Payments | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.12) · Platform C (2.29) · Growth C (2.58) · Payments B (3.10).

- Data: K1=1, K5=1 — "Significantly improve data quality across core tables." names no metric, no source.
- Platform: K3=2 — "Maintain API uptime at or above 99.9%." sits below the quoted 99.95% baseline.
- Growth: K1=2 — "Increase trial-to-paid conversion to 22%." states a target with no baseline anywhere.
- Payments: K1=2 — "Ship checkout & billing API v2 to GA by Sep 26." counts nothing; it is done or not done.

## 3. Per-team goodness findings

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR begins with a delivery verb and carries no baseline→target pair, so it succeeds on the day the API ships even if no customer's checkout improves — exactly the outcome the objective promises. Under the page's own convention ("Commitment: KRs are committed unless marked (aspirational).", line 19) it counts as a committed result while measuring only a schedule.
- Scores affected: K1=0, K2=1 (per-KR score capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR P1.2: `<target>`% of card checkout sessions served by checkout & billing API v2 (0% → `<target>`%), with authorization error rate no worse than the v1 rate, by Sep 26." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews. *(aspirational)*" (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid distribution without indicating anything about the funnel the objective claims to be tuning, and no current pageview figure appears anywhere in the export, so neither the ambition nor the progress can be judged. Search performed: the full `sample-portfolio.md` export — company priorities, all four team pages, and the Q2 business-review appendix; the appendix reports qualified signups, chargeback rate, step-up coverage and uptime, and no pageview or traffic figure.
- Scores affected: K1=2, K2=2, K3=2, K5=2; K7=2 for the G2 set
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed first-touch in `<analytics system>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the KR states a destination with no starting point, so 22% could be a stretch or a number the team already clears — neither ambition nor mid-quarter progress is judgeable. Search performed: the full `sample-portfolio.md` export, including the Q2 2026 business-review appendix (lines 89–91), which reports qualified signups, chargeback rate, step-up coverage and uptime but no trial-to-paid conversion value; Growth's own page states no current figure. Note the contrast with the neighbouring KR G1.2, which does state its baseline.
- Scores affected: K1=2, K3=2 (calibration unverifiable cap)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<funnel dashboard>`) → 22%, monthly cohort." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: the KR quantifies an internal state on a "score" that is defined nowhere — no survey, instrument, cadence, respondent population or current value appears in the corpus — so the number can never be honestly scored, and there is no KR or task to build the instrument. It also does not serve its objective: a satisfaction score moving would not make the lights stay on or make them cheaper, the two end-states "Objective PL1: Keep the lights on, cheaper" (line 56) actually names. Search performed: the full `sample-portfolio.md` export; the only named measurement system anywhere in it is the "Datadog SLO monitor" cited for uptime (line 89), and no survey or developer-experience instrument appears on Platform's page or elsewhere.
- Scores affected: K1=1, K5=1, K3=2; K7=2 for the PL1 set
- Suggested rewrite: Move it out of PL1 and give it an instrument — "KR: Quarterly internal developer survey (n ≥ `<respondents>`, run in `<survey tool>`): overall satisfaction `<baseline>`/10 → 8/10, plus median CI wait time `<baseline>`m → `<target>`m." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, other document): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing-90-day actual reported in the same export, so the KR is achieved by the system continuing to behave exactly as it already does — it encodes no delta and consumes an OKR slot that company priority C2's reliability ask deserves. The "Maintain" framing is the tell.
- Scores affected: K3=1, K1=3 (baseline absent from the KR but retrievable from the appendix)
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.98%, measured monthly; and error-budget burn ≤ `<threshold>`% per month." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Objective PL1: Keep the lights on, cheaper" (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56)
- Also: AP-11 Objective as Kitchen Sink
- Why it's a problem: "Keep the lights on" is the team's standing operational duty rather than a change it intends to bring about, so half the objective is achieved by default staffing; the "cheaper" clause bolts a second, unrelated end-state onto it, and the three KRs beneath split into three unrelated groups — availability, unit cost, and developer sentiment — with no shared outcome.
- Scores affected: O1=2, O4=2; K6=2, K7=2 for the PL1 set
- Suggested rewrite: Split into two ranked objectives — "PL1 (ranked first): Brightledger's API is boring — customers never notice it. PL2: We serve every transaction for meaningfully less than last quarter." — and move the standing availability duty to a health-metric section outside the OKRs, keeping the cost KR under the second. [proposal]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Why it's a problem: the KR is done or not done, so it reads 0% for eleven weeks and 100% in the twelfth — there is no mid-cycle signal that would let anyone intervene, and the audit is the load-bearing half of company priority C2. Contrast the neighbouring KR PL2.1, which does carry a gradient ("currently 7 open", line 62).
- Scores affected: K1=0, K2=1 (per-KR score capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence collection `<collected>`/`<total>` controls complete → 100% by `<date>`; auditor's final report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" names no metric, "core tables" names no table set, and "Significantly" names no magnitude, and no system of record for any of the three appears in the corpus — at quarter end the KR can be declared achieved or missed with equal justification. Search performed: the full `sample-portfolio.md` export — Data's page (lines 69–82) including its notes, the other three team pages, the company priorities, and the Q2 business-review appendix; no data-quality metric, table inventory, or measurement tool appears anywhere.
- Scores affected: K1=0, K5=0, K3=2 (per-KR score capped at 1.0 by the K1=0/K5=0 rule)
- Suggested rewrite: "KR D1.3: Null-or-late-arriving rows across the `<N>` core tables named in `<data catalog>`: `<baseline>`% → `<target>`%, measured daily by `<data-quality monitor>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Data
- Evidence: "Migrate 100% of product events to unified event schema v2." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Why it's a problem: the KR is the migration itself — a delivery verb with a completion percentage and no starting point — so it can be fully achieved while dashboards stay as untrustworthy as they were; nothing in it measures the trustworthiness the objective promises. It is also the KR whose delivery depends on work no other team has committed to (see §4, AL-01 Unacknowledged dependency).
- Scores affected: K1=2, K2=2, K3=2
- Suggested rewrite: "KR D1.1: Product events served from unified schema v2 `<baseline>`% → 100%, with schema-validation failures below `<threshold>`% of events and zero v1/v2 reconciliation breaks on the `<N>` critical dashboards." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed Q3 KRs land on the same resource node — Platform's infrastructure capacity — in the same quarter, and Platform's own page declares that capacity already spent and explicitly defers the request class to Q4. Combined demand exceeds a declared supply of zero; nobody in the portfolio has done this arithmetic. Payments' ask is a pure provisioning claim on Platform's capacity, so it folds into this finding rather than standing as its own edge.
- Detection check that fired: AL-07 resource-node fan-in on the dependency map — grouping every mention of a shared team/system by resource put two claimants on Platform in the same quarter, and checking the owner's page for declared supply returned the fully-committed statement.
- Disconfirming checks run: the plural demand is not contention control — no allocation table, scheduled epic, or assignment covering either claimant exists in the corpus (searched Platform's full page, lines 52–65, for "PCI", "infra", "provision", "streaming", "pipeline", "schema": the only hit is the deferral sentence itself; no Jira access was available for this run and the export contains no issue links); same-quarter check — all three pages are Q3 2026 (lines 17, 52, 69); same-resource check — Payments names "Platform" explicitly, Data names "the infra level", and Platform is the only infrastructure team in the confirmed scope. Result: finding stands, not falsified, with the Data→Platform resolution labeled below.
- Inference labels: resolving Data's "the infra level" to the Platform team is analyst inference — Data's text never names Platform; Platform's own claim to that territory is quoted ("Holding all non-critical infra requests until Q4."). Payments' edge names Platform verbatim and is not inferred. Payments' "as discussed in standup" refers to a conversation that is not in the corpus and is not treated as an acknowledgement.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 30, 82 and 65)
- Recommended resolution owner: Platform lead (Elena R.) to convene Payments (Priya N.) and Data (Jonas K.) inside two weeks and either publish a Q3 allocation for the PCI-scoped infra and the streaming pipeline migration or force both consumer KRs to be rescoped; severity escalated from Major to Critical because both claimant KRs are committed under their pages' stated convention and the contention sits on the critical path of the AL-06 and AL-01 findings below.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence (the dependency): "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date precedes the producer's delivery date by roughly six weeks — Growth commits to launching on Aug 15 a flow that runs on an API its producer commits to shipping on Sep 26, leaving negative integration margin. Both KRs are committed under their pages' stated conventions, and the only recorded reconciliation is "should be fine".
- Detection check that fired: AL-06 edge-date comparison on the dependency map — producer's delivery date (Sep 26) versus consumer's need-by date (Aug 15) on the Growth→Payments billing-API edge; hard inversion.
- Disconfirming checks run: the late date is not an inversion control — checked whether an earlier milestone would satisfy Growth: Growth's text names no milestone qualifier ("will use the new billing API"), and Payments' page states no beta, preview, or partial-availability date anywhere (lines 21–30), so the tightest quotable reading is GA on Sep 26; quarter-boundary check — Sep 26 falls inside Q3 2026, so the producer's date is not itself out of period; also checked whether Growth's flow might run on the existing v1 API — Growth's text says "the new billing API", which only v2 satisfies. Result: finding stands.
- Inference labels: none — all load-bearing text quoted. Growth's "should be fine" is quoted as the parties' own hedge, not read as a schedule agreement.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 41, 48 and 23)
- Recommended resolution owner: Growth lead (Marcus T.) and Payments lead (Priya N.) to agree within one week either a v2 date Growth can build against or an Aug 15 launch on the existing API, and to restate G1.3's date accordingly; note that P1.2's own date is itself exposed to the AL-07 contention above.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ all four teams
- Company evidence: "C4 — Launch Brightledger Capital:" (sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Company evidence: "invoice-financing pilot live with 3 design partners by Sep 30." (sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (the absence, quoted from the only near-miss): the closest any team comes to the invoicing/financing domain is Payments' "Objective P1: Make checkout something customers never think about" (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 21), whose KRs measure checkout success, API v2 shipping and authorization latency — none of which is a financing product, a pilot, or a design-partner count.
- Conflict: a dated, committed company priority has zero contributing children anywhere in the portfolio. C1, C2 and C3 each have at least one team's objective serving them; C4 has none, so a Sep 30 company commitment enters the quarter unstaffed and unmeasured.
- Detection check that fired: AL-10 top-down strategy trace — each company priority searched across all four team pages for contributing objectives or KRs; C4 returned zero.
- Disconfirming checks run: the zero hits are not a coverage gap control — re-searched the full export under synonyms and program names ("Capital", "financing", "invoice-financing", "design partner", "pilot"); the only occurrences of any of them are on line 13 itself, and no team page mentions them; checked the company objective's own page for a named owner assigning C4 to a function outside the swept team set — line 13 names none, and the priorities page's only stated owner is "Owner: Dana W. (CEO)" (line 8), which is the page owner, not a delivery assignment; near-miss quoted and distinguished above. Result: finding stands.
- Inference labels: none — all load-bearing text quoted. The claim is scoped to the four teams enumerated in this export; a team outside the export could hold C4, which the corpus neither shows nor rules out.
- Verdict: CONFIRMED (both company quotes and the near-miss re-verified character-for-character against lines 13 and 21)
- Recommended resolution owner: CEO (Dana W.) to name an owning team for C4 and have that team publish an objective with a design-partner count and a pilot-live date before the end of month 1, or to formally drop C4 from the Q3 priority list; rated Critical because C4 is a dated company commitment with zero coverage.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Data evidence (the dependent KR): "Migrate 100% of product events to unified event schema v2." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (the closest thing to acknowledgement, and why it does not cover the need): "Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65) — a deferral of the request class, not a commitment to build the streaming pipeline migration; Platform's five KRs cover uptime, cloud spend, developer satisfaction, pen-test findings and SOC 2, and none names a pipeline, a migration, or event streaming.
- Conflict: Data's committed KR D1.1 depends on a named deliverable — the streaming pipeline migration — that Data explicitly assigns to someone else and that appears nowhere in the producer's objectives, KRs or notes. This is a distinct missing deliverable, not merely a claim on capacity, so it is reported separately from the AL-07 contention it sits inside; the capacity arithmetic is reported once, above.
- Detection check that fired: AL-01 edge-acknowledgement check — the dependency phrase "rides on" resolved to an external producer ("the infra level"), then searched the producer's side for the deliverable and found nothing.
- Disconfirming checks run: the missing mention is not unacknowledged control — searched Platform's entire page (lines 52–65: both objectives, all five KRs, the source line and the notes) for "streaming", "pipeline", "schema", "event", "migration", "data": zero hits. No Jira or backlog access was available for this run and the export contains no issue links or epics, so the absence claim is scoped to the OKR pages in this export and cannot exclude an unlisted backlog item; the near-miss above is quoted and distinguished. Result: finding stands at Major rather than Critical, because the only Platform text touching the area defers a request class without naming this deliverable.
- Inference labels: resolving "the infra level" to the Platform team is analyst inference — Data's text never names Platform; Platform is the only infrastructure team in the confirmed scope and claims the infra-request queue in its own quoted notes.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 82, 74 and 65)
- Recommended resolution owner: Data lead (Jonas K.) to get the streaming pipeline migration either onto Platform's Q3 plan with an owner and a date or off D1.1's critical path within two weeks; cross-references the AL-07 Resource contention finding above, which carries the capacity arithmetic.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to the same named metric on the same population in the same quarter with inconsistent targets — 40% and 35% — and neither page references the other team, so at quarter end nobody can say who was accountable for activation or which number was the goal. Data's objective goes further and claims the whole surface: "Objective D2: Own onboarding personalization end-to-end" (line 78), while Growth's G1 set treats first-week activation as its central KR.
- Detection check that fired: AL-03 clustering by target metric + target population — "new-user activation rate" for new users appears in exactly two teams' KRs; the cluster was then checked for mutual reference, shared owner, or explicit split and found to have none.
- Disconfirming checks run: the similar objectives are not duplication control — checked for different populations, surfaces or segments that would make this a legitimate division of labor: both KRs say "new-user activation rate" with no segment, surface or geography qualifier on either side; checked for cross-references, a shared epic, or a parent objective assigning lanes by searching every team's page for the other team's name — Growth's page names only Payments ("Marcus synced with Priya in June", line 48) and Data's names no team at all; checked for a joint owner — the pages list different owners, "Owner: Marcus T." (line 35) and "Owner: Jonas K." (line 70). Result: finding stands; no disambiguating text exists to quote.
- Inference labels: none — all load-bearing text quoted. Note that the two KRs' equivalence rests on the shared metric name only: Growth defines the metric ("first invoice sent within 7 days") and Data states no definition, so a hidden AL-08 Terminology collision could be masking a larger or smaller gap than 5 points; that secondary ID is cross-referenced here rather than filed separately.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 40 and 80)
- Recommended resolution owner: the two leads' shared manager to assign a single accountable team for new-user activation and one target before mid-quarter, with the other team's KR restated as a contributing lever (e.g. Data owning checklist coverage and experiment throughput, Growth owning the activation rate itself); Data must also publish the metric's definition so the two numbers are comparable at all.

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and Payments commits to applying it to nearly three times as many transactions in the same quarter that Growth commits to a ten-point conversion gain on that same surface. Each team's lever works against the other's number, and neither KR, note, nor objective mentions the other team.
- Detection check that fired: AL-02 surface-lever blocking key — both KRs sit on the checkout surface, Payments' stated lever ("step-up verification coverage") is a verification/friction control there, and Growth targets that surface's conversion metric. The metric-identity key generated nothing for this pair, since the two KRs share no metric name.
- Disconfirming checks run: shared or parent OKR covering both — none found (searched all four team pages and the company priorities; C1 and C3 are separate priorities with no joint guardrail); documented split of levers — none found (neither page mentions the other team or a conversion/fraud tradeoff); directionality — Payments' friction control rises while Growth's throughput metric must also rise, so the coupling is adversarial, not aligned. Separately killed on its own evidence, without suppressing this candidate: the lookalike pair "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) against Growth's same conversion KR — same direction, different definitions and populations ("for card transactions" vs "for self-serve signups"), no control lever on either side, so not reported. Result: this candidate stands.
- Inference labels: the step-up-verification→conversion mechanism is analyst inference — no Brightledger document in this export states the tradeoff; the objective's own "without drama" (line 26) is the closest the corpus comes to acknowledging a customer-experience cost, and it names no metric.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. and agree a guardrail pair — a chargeback-rate ceiling and a self-serve checkout-conversion floor, e.g. `<conversion floor>`% — plus a risk-based (rather than blanket) step-up policy, within two weeks [proposal — placeholder target].

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "Objective D1: One trustworthy source of truth" (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73)
- Company evidence: the full Q3 priority list is "C1 — Grow self-serve revenue:", "C2 — Become enterprise-ready:", "C3 — Cut fraud losses:" and "C4 — Launch Brightledger Capital:" (sample-portfolio.md › Company Q3 2026 priorities › lines 10–13) — none of which names data, analytics, event schemas, or dashboards.
- Conflict: half of the Data team's quarter serves an objective with no traceable parent. Its KRs measure event-schema migration, dashboard latency and data quality; none of these is a company-level metric or a documented driver of one, and the strategy page never mentions the area. Compare Payments, whose page states its parent outright: "Fraud work is our top ask from leadership after the Q2 incident (company priority C3)." (line 30).
- Detection check that fired: AL-04 three-way check on the strategy trace — (a) explicit parent link: none on Data's page; (b) KR metric that is a company-level metric or a documented driver of one: none of C1–C4's metrics (ARR, SOC 2, chargeback rate, financing pilot) is measured or driven in a documented step by D1's KRs; (c) mention in a department or company strategy page: none. Zero of three.
- Disconfirming checks run: the no-parent-link is not an orphan control — ran the full three-way check above rather than flagging on the missing label alone, and searched Data's page including its notes (line 82) for a self-stated justification: the notes discuss only sizing and the pipeline dependency, offering no strategic rationale to quote in the finding's defence; also checked whether an inferred parent exists and counted it against the finding rather than for it. Result: finding stands, at Minor.
- Inference labels: none — all load-bearing text quoted. The absence of a data-platform priority is quoted from the priority list itself rather than assumed.
- Verdict: CONFIRMED (Data's objective and all four company priority labels re-verified character-for-character against lines 73 and 10–13)
- Recommended resolution owner: Data lead (Jonas K.) and the CEO to either attach D1 to a named priority with a stated mechanism — the likeliest is C1, via the activation and conversion metrics D1's dashboards feed — or reallocate the effort; rated Minor rather than Major because Data's only quoted capacity claim, "we've sized our part at 3 engineer-months" (line 82), states an absolute size and not a fraction of team capacity, so the large-stated-fraction test for Major is not met by quoted evidence.

## 5. Prioritized action list

1. Convene Platform, Payments and Data to reconcile the Q3 infra queue against Platform's stated capacity and publish an allocation or rescope both consumer KRs — owner: Platform lead (Elena R.) (resolves §4 AL-07 Resource contention).
2. Agree a billing-API-v2 date Growth can build against, or relaunch G1.3 on the existing API, and restate the dates on both sides — owner: Growth lead (Marcus T.) with Payments lead (Priya N.) (resolves §4 AL-06 Timeline mismatch).
3. Assign an owning team and a measurable objective for company priority C4, or drop it from the Q3 list — owner: CEO (Dana W.) (resolves §4 AL-10 Strategy coverage gap).
4. Replace Platform's developer-satisfaction KR with a survey-instrumented metric or move it out of PL1 — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
5. Define Data's data-quality metric, table set and monitor, or drop the KR — owner: Data lead (Jonas K.) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
6. Get the streaming pipeline migration onto Platform's Q3 plan with an owner and a date, or off D1.1's critical path — owner: Data lead (Jonas K.) (resolves §4 AL-01 Unacknowledged dependency).
7. Name one accountable team and one target for new-user activation, and publish the metric's definition on both pages — owner: the shared manager of Growth and Data (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Set a joint fraud/conversion guardrail pair and a risk-based step-up policy before step-up coverage scales past its current 35% — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
9. Rewrite Platform's uptime KR against the quoted 99.95% trailing baseline, split objective PL1, and give the SOC 2 KR a gradient — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target, AP-10 BAU Dressed as OKR, AP-02 Binary KR with No Gradient).
10. Add baselines and outcome measures to the four output-shaped KRs — P1.2, G1.1, G2.3 and D1.1 — before the quarter's first check-in — owners: Payments, Growth and Data leads (resolves §3 AP-01 Task Masquerading as KR ×2, AP-04 KR Without Baseline, AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Data** (roll-up C (2.12), the portfolio's lowest; Critical AP-09 Metric Nobody Can Measure, plus Critical AL-07 Resource contention as a claimant and Major AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: the Data team section of the local export `sample-portfolio.md` (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Platform** (roll-up C (2.29); Critical AP-09 Metric Nobody Can Measure, plus Critical AL-07 Resource contention as the resource owner): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: the Platform team section of the local export `sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Also in the file: a Q2 2026 business-review appendix (page 88104) carrying Platform's trailing uptime actual."
- **Growth** (roll-up C (2.58); Critical AL-06 Timeline mismatch as the consumer): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: the Growth team section of the local export `sample-portfolio.md` (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Also in the file: a Q2 2026 business-review appendix (page 88104) carrying Growth's qualified-signup actual."
- **Payments** (roll-up B (3.10); Critical AL-06 Timeline mismatch as the producer and Critical AL-07 Resource contention as a claimant): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: the Payments team section of the local export `sample-portfolio.md` (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Also in the file: a Q2 2026 business-review appendix (page 88104) carrying Payments' chargeback and step-up actuals."

All four teams qualify under criterion (b) — each carries at least one Critical finding. No team qualifies under criterion (a): no roll-up grade is at or below the rubric's needs-rework threshold of D.
