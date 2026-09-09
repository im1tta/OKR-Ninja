# Brightledger — Q3 2026 OKR Portfolio Review

Mode: **portfolio** (4 teams in scope: Payments, Growth, Platform, Data). Period: Q3 2026, as stated by the source. Source: `input.md` (local export; no Atlassian connection available). Strategy source: the "Company Q3 2026 priorities" section of the same file (C1–C4).

---

## 1. Executive summary

**Verdict: Not ready as written.** 4 teams reviewed; 6 Critical, 9 Major, 2 Minor findings.
The worst alignment risk is **AL-07 Resource contention**: Payments and Data both build committed Q3 work on Platform infra, while Platform's own page declares Q3 fully committed and holds non-critical infra requests until Q4 — the arithmetic has not been done anywhere.
Second Critical exposure: **AL-10 Strategy coverage gap** — company priority C4 (Brightledger Capital, dated Sep 30) has zero coverage across all four teams.
Growth's committed Aug 15 upgrade launch depends on a billing API its producer commits to only on Sep 26 (**AL-06 Timeline mismatch**), and Growth and Data hold conflicting targets on the same activation metric (**AL-03 Duplicated / overlapping objectives**).
The most common goodness anti-pattern is **AP-01 Task Masquerading as KR** — 3 KRs across 2 of 4 teams measure delivery instead of result. Two KRs name metrics no system in the corpus can report (**AP-09 Metric Nobody Can Measure**), and Platform's uptime KR is set below its own quoted trailing baseline (**AP-06 Sandbagged Target**).
Recommended first action: a Platform capacity session with Payments and Data, before the July provisioning date Payments has already assumed, to allocate or explicitly refuse the two infra asks.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 3 |
| Platform | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.25) · Platform C (2.29) · Growth B (2.82) · Payments B (3.05).

- Data: K1=1, K5=1 — "Significantly improve data quality" names no metric and no system of record (AP-09).
- Platform: K1/K3/K5=2 — sandbagged uptime target plus an unmeasurable developer-satisfaction score (AP-06, AP-09).
- Growth: K1=2 — trial-to-paid and blog-pageview targets state no baseline (AP-04, AP-03).
- Payments: K1=2 — "Ship checkout & billing API v2 to GA" states no metric at all (AP-01).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 59`)
- Why it's a problem: the KR quantifies an internal state with no instrument — searching the whole corpus (company priorities page, all four team pages, the Q2 business-review appendix) for a survey, score, dashboard, or prior value returns nothing, and only "Datadog SLO monitor" (`input.md › Appendix — Q2 2026 business review (extracts) › line 89`) is named as a system of record anywhere. As written the KR can never be honestly scored.
- Scores affected: K1=1, K5=1, K3=2 (calibration unverifiable — no baseline anywhere)
- Suggested rewrite: "KR PL1.3: Quarterly internal developer survey (new instrument, first run by `<date>`, n ≥ `<respondents>` of the platform's internal users): satisfaction `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 57`); prior actual: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input.md › Appendix — Q2 2026 business review (extracts) › line 89`)
- Why it's a problem: the target sits below the trailing actual quoted in the same corpus, so the KR is achieved by a measurable regression — the anchor case for AP-06 Sandbagged Target and for K3=1.
- Scores affected: K3=1, K1=3 (baseline absent from the KR but retrievable from the quoted Q2 extract)
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, monthly, error-budget burn reported weekly." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 56`); supporting KR: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 57`)
- Why it's a problem: keeping systems running is the team's standing job stated with no delta, and "Maintain" is the catalog's detection cue; a quarter of default staffing satisfies half the objective while displacing a real goal.
- Scores affected: O1=3, O4=2, K3=1 (on PL1.1), K6=2, K7=2
- Suggested rewrite: "Objective PL1: Brightledger serves each transaction for less without customers noticing any change in reliability. KR: cloud spend per 1,000 transactions $4.10 → $3.20. KR: uptime holds at or above 99.95% (Q2 trailing-90-day actual)." (Move the standing availability duty to a health-metrics section outside the OKRs.)

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input.md › Objective PL2: Earn enterprise trust › line 63`)
- Why it's a problem: done/not-done with no numeric scale — mid-quarter the KR can only be scored 0% or 100%, so the team cannot steer and leadership cannot see slippage before it is terminal. It carries company priority C2 ("complete SOC 2 Type II and hold enterprise-grade reliability", `input.md › Company Q3 2026 priorities › line 11`), which makes the blind spot expensive.
- Scores affected: K1=0, K2=1, K3=2 (KR score capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II audit findings (baseline: 0/`<N>` closed), all evidence requests answered within `<days>` days, auditor's report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`input.md › Objective D1: One trustworthy source of truth › line 76`)
- Why it's a problem: no metric, no target, and no instrument — "data quality" is defined only in the authors' heads, and a corpus search (company priorities page, all four team pages, Q2 appendix; terms "quality", "dashboard", "monitor", "score") finds no system that could report it. The KR can be declared achieved or missed at will.
- Scores affected: K1=0, K5=0, K3=2 (KR score capped at 1.0 by the K1=0 / K5=0 rule); drives K6=2 for the D1 set
- Suggested rewrite: "KR D1.3: Null-or-duplicate defect rate across the `<N>` core tables `<baseline>`% → `<target>`%, measured nightly and published on `<named dashboard>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Data
- Evidence: "Ship personalized onboarding checklists to 100% of new signups." (`input.md › Objective D2: Own onboarding personalization end-to-end › line 79`); same pattern: "Migrate 100% of product events to unified event schema v2." (`input.md › Objective D1: One trustworthy source of truth › line 74`)
- Why it's a problem: both KRs measure delivery coverage rather than a result — shipping a checklist to every signup succeeds even if no one completes it, and a completed migration succeeds even if dashboards get no better. Neither states a baseline→target pair.
- Scores affected: D2.1 K1=2, K2=1; D1.1 K1=2, K2=2, K3=2
- Suggested rewrite: "KR D2.1: `<baseline>`% → `<target>`% of new signups complete their personalized onboarding checklist within 7 days." / "KR D1.1: `<M>`/`<N>` → `<N>`/`<N>` production event types emitting schema v2, with all critical dashboards reading v2 only." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`input.md › Objective G1: Make the first week with Brightledger magical › line 39`)
- Why it's a problem: no starting point is stated, and the Q2 business-review extract (searched for trial, conversion, and paid figures) reports only qualified signups, chargeback rate, step-up coverage, and uptime — so neither ambition nor progress can be judged, and mid-quarter movement is unreadable.
- Scores affected: K1=2, K3=2 (calibration unverifiable), K5=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, monthly signup cohort, per `<named analytics source>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews. *(aspirational)*" (`input.md › Objective G2: Turn our funnel into a machine › line 46`)
- Why it's a problem: pageviews rise with spend and syndication without indicating that the funnel converts anything, which is what the objective claims; the KR also states no baseline, so even the exposure it measures cannot be judged. It is the one KR in the set no skeptic would accept as evidence of a working funnel.
- Scores affected: K1=2, K2=2, K3=2, K5=2; drives K7=2 for the G2 set
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, first-touch attribution, per `<named analytics source>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input.md › Objective P1: Make checkout something customers never think about › line 23`)
- Why it's a problem: the KR begins with "Ship", carries no metric and no baseline→target pair, and succeeds on the ship date even if no traffic moves to v2 — the objective ("customers never think about" checkout) is untouched by it. Its only failure mode is lateness.
- Scores affected: K1=0, K2=1, K3=2 (KR score capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing API calls served by v2 by Sep 26, with v2 error rate ≤ `<threshold>`% and p95 latency no worse than v1." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`input.md › Objective P2: Cut fraud losses without drama › line 30`)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input.md › Objective D2: Own onboarding personalization end-to-end › line 82`)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input.md › Objective PL2: Earn enterprise trust › line 65`)
- Conflict: two teams' committed Q3 work assumes Platform capacity in the same quarter in which Platform declares its capacity already spent and gates non-critical infra requests to Q4; nobody has reconciled the combined demand against the declared supply. Payments has additionally assumed a July provisioning date that appears in no Platform commitment.
- Detection check that fired: AL-07 resource-node fan-in — grouping every shared-resource mention by resource put two claimants on Platform in one quarter; checking the owner's page for declared supply returned the fully-committed statement. Payments' ask is a pure provisioning/capacity claim and folds into this aggregate entirely; Data's named deliverable additionally earns its own AL-01 below.
- Disconfirming checks run: allocation outside the OKR pages — no Jira/backlog access in this run and no capacity or allocation table anywhere in the corpus (searched all four team pages and the appendix for "infra", "provision", "capacity", "roadmap"); same-quarter check — all three statements sit on Q3 2026 pages (Payments last updated 2026-07-02, Data 2026-07-01, Platform 2026-07-05); same-resource check — both asks are infrastructure asks and Platform is the only infrastructure-owning team in scope. No allocation found, so the finding stands rather than being killed or downgraded.
- Inference labels: routing Data's "the infra level" to the Platform team is **analyst inference** — Data never names Platform, though Platform's own page uses the same term ("infra requests") and is the sole infra owner among the four teams in scope. Payments' claim on Platform is quoted, not inferred. Severity escalated Major → Critical: both claimant KRs are committed under their pages' stated convention ("Commitment: KRs are committed unless marked (aspirational).", `input.md › Payments team — Q3 2026 › line 19`) and this resource node sits on the critical path of two further findings (the AL-01 below, and the AL-06 billing-API date whose producer KR depends on this same provisioning).
- Verdict: PLAUSIBLE (all quotes re-verified character-for-character; the Data→Platform routing is inferred and is load-bearing for the second-claimant count)
- Recommended resolution owner: Platform lead (Elena R.) to convene Priya N. and Jonas K. within one week and either allocate the PCI-scoped provisioning and the streaming pipeline work in Q3 or refuse them in writing, so Payments' and Data's KRs can be re-scoped before the July date Payments has assumed.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input.md › Objective D2: Own onboarding personalization end-to-end › line 82`), supporting the committed KR "Migrate 100% of product events to unified event schema v2." (`input.md › Objective D1: One trustworthy source of truth › line 74`)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input.md › Objective PL2: Earn enterprise trust › line 65`)
- Conflict: the streaming pipeline migration is a distinct deliverable someone must plan and staff as its own project, and it appears in no team's objectives or KRs — Data has assigned it to "the infra level", and the only infra owner in scope has explicitly deprioritized the category it falls into. D1.1 is committed on top of work nobody owns.
- Detection check that fired: AL-01 dependency-edge acknowledgment — the phrase "rides on" plus a named external deliverable resolved to an infra owner, then searched on the producer's side with no hit. This is the deliverable-naming edge that stands separately from the AL-07 aggregate above; the capacity arithmetic is reported once, there.
- Disconfirming checks run: producer tracks it outside OKRs — no Jira or backlog is available in this run, so the absence is asserted only over the stated corpus; corpus search for "streaming", "pipeline", "schema", "event", "warehouse", "migration" across the company priorities page, all four team pages and the Q2 appendix returns hits only on Data's own two lines (74, 82) — zero on Platform's page. The nearest near-miss on Platform's side is "Holding all non-critical infra requests until Q4", which is a refusal, not coverage.
- Inference labels: resolving "the infra level" to the Platform team is **analyst inference** (Data names no team); the absence itself is producer-independent — the pipeline migration appears in no team's OKRs at all.
- Verdict: PLAUSIBLE (quotes verified verbatim; the owning-team attribution is inferred)
- Recommended resolution owner: Data lead (Jonas K.) to put the streaming pipeline migration in front of Platform at the next portfolio review with a named owner and size, or re-scope D1.1 to the events Data can migrate without it, before end of July.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`input.md › Objective G1: Make the first week with Brightledger magical › line 41`), with "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`input.md › Objective G2: Turn our funnel into a machine › line 48`)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input.md › Objective P1: Make checkout something customers never think about › line 23`)
- Conflict: the consumer's committed launch date (Aug 15) precedes the producer's committed availability date (Sep 26) by roughly six weeks, with no integration margin and no earlier milestone quoted anywhere — Growth's committed KR cannot ship on the dependency it names.
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer's delivery date versus consumer's need-by date, a hard inversion.
- Disconfirming checks run: "which milestone does the consumer actually need" — Growth's text says only "will use the new billing API" with no beta/preview qualifier, and Payments' page states no date other than GA Sep 26 (the Payments section was searched for any earlier beta, preview, or pilot date — none), so the tightest quotable reading is GA; soft-date check — both dates are stated flatly, neither hedged, and both KRs are committed under their pages' stated convention. Neither check weakens the finding.
- Inference labels: none — all load-bearing text quoted. (Growth's own hedge, "should be fine", is quoted rather than characterized.)
- Verdict: CONFIRMED (both dated statements re-verified character-for-character against their source lines)
- Recommended resolution owner: Payments lead (Priya N.) with Growth lead (Marcus T.) to agree by mid-July either a dated partial/beta cut of the billing API that Growth can build against before Aug 15, or a revised G1.3 launch date — and to record the agreed date on both pages instead of in a standup.

### [Critical] AL-10 Strategy coverage gap: Company strategy ↔ all four teams
- Company strategy evidence: "invoice-financing pilot live with 3 design partners by Sep 30." — priority C4, Launch Brightledger Capital (`input.md › Company Q3 2026 priorities › line 13`)
- Portfolio evidence (near-miss, distinguished): "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`input.md › Objective G1: Make the first week with Brightledger magical › line 40`) — the only occurrence of "invoice" in any team's OKRs, and it measures onboarding activation, not invoice financing.
- Conflict: a dated, committed company priority has no contributing objective or KR on any of the four teams' pages; as the portfolio stands, C4 cannot be delivered by Sep 30 because nobody is working on it.
- Detection check that fired: AL-10 top-down strategy trace — for each company priority, search all team OKRs for coverage. C1 (self-serve ARR) is served by Growth's funnel KRs, C2 by Platform PL2.2 and PL1.1, C3 explicitly by Payments P2 ("Fraud work is our top ask from leadership after the Q2 incident (company priority C3).", `input.md › Objective P2: Cut fraud losses without drama › line 30`); C4 returns zero contributors.
- Disconfirming checks run: synonym and program-name re-search across the whole file — "capital", "financ", "lend", "design partner", "pilot", "invoice" — returns only the C4 line itself and the Growth activation KR quoted above; owner check on the priority's own page — the company priorities section names an overall page owner ("Owner: Dana W. (CEO)", `input.md › Company Q3 2026 priorities › line 8`) but assigns C4 to no function inside or outside the swept team set, so this is a portfolio hole rather than an ownership note. Neither check kills the finding.
- Inference labels: none — all load-bearing text quoted; the near-miss is quoted and distinguished rather than silently dismissed.
- Verdict: CONFIRMED (the C4 line and the near-miss re-verified character-for-character)
- Recommended resolution owner: CEO (Dana W.) to name an owning team and a Q3 objective for C4 at the next portfolio review, or to move the pilot out of Q3 — before the quarter's first month closes, since the pilot is dated Sep 30.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`input.md › Objective G1: Make the first week with Brightledger magical › line 40`)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`input.md › Objective D2: Own onboarding personalization end-to-end › line 80`), under the objective "Own onboarding personalization end-to-end" (`input.md › Objective D2: Own onboarding personalization end-to-end › line 78`)
- Conflict: two teams hold a committed KR on the same metric for the same population with inconsistent targets — 40% versus 35% — while Data's objective claims end-to-end ownership of the surface Growth is also working. Nobody can say who is accountable for the number, and the quarter can end with the same metric scored as a hit by one team and a miss by the other.
- Detection check that fired: AL-03 clustering by target metric plus target population — "new-user activation rate" for new signups appears in two teams' KRs; the cluster was then checked for any mutual reference, shared owner, or explicit split.
- Disconfirming checks run: different population/surface/segment — both KRs address new users of the same product and Data's own surface claim is "end-to-end", so no lane split is stated; cross-reference search — Growth's notes name only Payments ("Marcus synced with Priya in June", line 48) and Data's notes name only "the infra level" (line 82), so neither page mentions the other team; parent objective assigning lanes — the company priorities section (lines 10–13) names no owner for activation. All three fail to kill the candidate; the inconsistent targets hold it at Major.
- Inference labels: none — all load-bearing text quoted. Cross-references: AL-02 Conflicting metrics / adversarial incentives (incompatible targets on one metric) and AL-08 Terminology collision (Growth defines activation as "first invoice sent within 7 days"; Data's KR states no definition or window) are secondary to this root cause and are not double-counted as separate findings.
- Verdict: CONFIRMED (both KR quotes and both notes lines re-verified character-for-character)
- Recommended resolution owner: VP Product to assign one accountable team for new-user activation and one target before the end of July, with the other team's KR restated as a contributing lever under the agreed definition.

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`input.md › Objective P2: Cut fraud losses without drama › line 28`)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`input.md › Objective G2: Turn our funnel into a machine › line 44`)
- Conflict: step-up verification is added checkout friction, and Payments commits to applying it to nine transactions in ten (up from roughly one in three) in the same quarter Growth commits to a ten-point conversion lift on the same checkout surface. Neither KR mentions the other team and no shared guardrail exists. The same lever also pulls against Payments' own "Raise checkout success rate from 91.2% to 95% for card transactions." (`input.md › Objective P1: Make checkout something customers never think about › line 22`).
- Detection check that fired: AL-02 known tension pair — one KR's mechanism (verification friction) is a driver of the other's metric (checkout conversion), surfaced by blocking on the shared checkout surface rather than on an identical metric name.
- Disconfirming checks run: directionality / compatible targets — the metric names differ, so this is a mechanism-level pair rather than same-metric opposition; shared or parent OKR covering both — none in the corpus (the company priorities list C1 and C3 separately, with no guardrail linking them); documented split of levers — both team pages and their notes were searched for any friction/conversion tradeoff, exemption, or risk-segmentation statement, and none exists. The absence of a documented mechanism in the teams' own material holds this at mechanism level rather than same-metric Critical.
- Inference labels: the friction→conversion mechanism is **analyst inference** — no Brightledger document in the corpus states the tradeoff.
- Verdict: PLAUSIBLE (both quotes verified verbatim; the causal coupling is inferred, not documented in the corpus)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. to agree a guardrail pair — a chargeback ceiling alongside a conversion floor — plus a risk-based rule limiting step-up to `<risk-band>` transactions rather than a flat 90%, within two weeks [proposal — placeholder target].

### [Minor] AL-08 Terminology collision: Payments ↔ Growth
- Payments evidence: "Raise checkout success rate from 91.2% to 95% for card transactions." (`input.md › Objective P1: Make checkout something customers never think about › line 22`)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`input.md › Objective G2: Turn our funnel into a machine › line 44`)
- Conflict: both teams commit to raising a "checkout" number in Q3, the two figures differ by 33 points because they measure different populations and events, and neither page states a formula, window, or system of record. Any exec rollup that speaks of "checkout" in Q3 will conflate a payment-authorization rate with a funnel conversion rate.
- Detection check that fired: AL-08 metric-name scan — the term "checkout" is used in KRs by two teams; each team's pages were then hunted for a definition (formula, window, population, data source) to diff.
- Disconfirming checks run: normalize both definitions before diffing — there is nothing to normalize, since a corpus search for definitions, glossary entries, or named systems returns only "Datadog SLO monitor" for uptime (line 89) and no source for either checkout metric; superseded-page check — both pages are current Q3 2026 pages (Payments last updated 2026-07-02, Growth 2026-06-28). Definitions absent on both sides is itself the Minor case in the taxonomy.
- Inference labels: none — all load-bearing text quoted; no claim is made that the two metrics are the same measurement.
- Verdict: CONFIRMED (both quotes re-verified character-for-character; the absence of definitions verified by search over the full corpus)
- Recommended resolution owner: Payments lead (Priya N.) and Growth lead (Marcus T.) to publish a one-line definition and a named system of record for each checkout metric, and to rename one of them, before the first Q3 business review.

### [Minor] AL-04 Orphan objective: Data ↔ Company strategy
- Data evidence: "One trustworthy source of truth" (`input.md › Objective D1: One trustworthy source of truth › line 73`), with the team's own capacity claim "we've sized our part at 3 engineer-months" (`input.md › Objective D2: Own onboarding personalization end-to-end › line 82`)
- Company strategy evidence: the Q3 priority list reads "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." (C1), "complete SOC 2 Type II and hold enterprise-grade reliability." (C2), "bring chargeback rate under 0.5% after the Q2 incident." (C3) and "invoice-financing pilot live with 3 design partners by Sep 30." (C4) (`input.md › Company Q3 2026 priorities › lines 10–13`)
- Conflict: half of Data's quarter sits under an objective with no parent — no explicit link, no KR measuring a company-level metric or a documented driver of one, and no mention of data infrastructure in the priorities page. Data's own strongest justification is a sizing note, not a strategic claim.
- Detection check that fired: AL-04 three-way check on the strategy trace — (a) explicit parent link: none on the Data page; (b) KR metric is a company metric or documented driver: event-schema migration coverage, dashboard latency and "data quality" appear in no company priority; (c) strategy-page mention: no data, schema, pipeline, or reporting language in lines 10–13. Zero of three.
- Disconfirming checks run: inferred parents count against the finding, so no credit was given for a chain from data quality to C1 or C3; team-charter check — the file states no exploratory or enabling charter for Data (the Data section and the priorities page were both searched); capacity-fraction check — Data quotes "3 engineer-months" but states no team size, so a "large stated fraction of team capacity" cannot be established and the finding stays at the default severity instead of escalating to Major.
- Inference labels: none — all load-bearing text quoted; the potential enabling link to C1/C3 is named only to record that it was considered and not credited.
- Verdict: CONFIRMED (the objective, the capacity note and all four priority lines re-verified character-for-character)
- Recommended resolution owner: Data lead (Jonas K.) to state D1's parent priority and the company metric it moves, or to fold the schema and latency work under the activation objective (D2) that already traces to C1, at the next portfolio review.

## 5. Prioritized action list

1. Convene Platform, Payments and Data on Q3 infra capacity and allocate or refuse both asks in writing before the assumed July provisioning date — owner: Platform lead (Elena R.) (resolves §4 AL-07 Resource contention).
2. Assign an owning team and a Q3 objective to company priority C4, or move the pilot out of Q3 — owner: CEO (Dana W.) (resolves §4 AL-10 Strategy coverage gap).
3. Agree a dated beta cut of billing API v2 that Growth can integrate before Aug 15, or move G1.3's launch date, and record it on both pages — owner: Payments lead (Priya N.) with Growth lead (Marcus T.) (resolves §4 AL-06 Timeline mismatch).
4. Get the streaming pipeline migration owned and sized by a named team, or re-scope D1.1 to what Data can migrate alone — owner: Data lead (Jonas K.) (resolves §4 AL-01 Unacknowledged dependency).
5. Assign one accountable team and one target for new-user activation, restating the other team's KR as a contributing lever — owner: VP Product (resolves §4 AL-03 Duplicated / overlapping objectives).
6. Set a joint fraud/conversion guardrail pair and a risk-based step-up rule instead of flat 90% coverage — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
7. Replace the two unmeasurable KRs with instrumented metrics that name their system of record — owners: Platform lead (Elena R.) and Data lead (Jonas K.) (resolves §3 AP-09 Metric Nobody Can Measure, both instances).
8. Reset the uptime KR against the quoted 99.95% trailing baseline and move the standing availability duty out of the OKRs — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target and §3 AP-10 BAU Dressed as OKR).
9. Convert the four delivery-milestone KRs into adoption or outcome measures with baselines — owners: Priya N. (P1.2), Jonas K. (D1.1, D2.1), Elena R. (PL2.2) (resolves §3 AP-01 Task Masquerading as KR, both blocks, and §3 AP-02 Binary KR with No Gradient).
10. Add stated baselines and named metric sources to the trial-to-paid and blog KRs, replacing pageviews with a funnel metric — owner: Growth lead (Marcus T.) (resolves §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.29); Critical findings §3 AP-09 Metric Nobody Can Measure, §4 AL-07 Resource contention, §4 AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Data** (roll-up C (2.25); Critical findings §3 AP-09 Metric Nobody Can Measure, §4 AL-01 Unacknowledged dependency, §4 AL-07 Resource contention): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Payments** (roll-up B (3.05), above the needs-rework threshold, but party to Critical findings §4 AL-06 Timeline mismatch and §4 AL-07 Resource contention): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."
- **Growth** (roll-up B (2.82), above the needs-rework threshold, but party to Critical finding §4 AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3). Period: Q3 2026."

All four teams qualify under criterion (b) — each is party to at least one Critical finding — while no team's roll-up grade is at or below the rubric's needs-rework threshold of D. Platform and Data are the two whose own OKR text carries the Critical goodness defects, and should be re-run first.
