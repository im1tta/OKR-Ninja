# Brightledger — Q3 2026 portfolio OKR review

Scope: 4 teams (Payments, Growth, Platform, Data), period Q3 2026, strategy source "Company Q3 2026 priorities" (Confluence page 88101). Mode: **portfolio**. Source corpus: `sample-portfolio.md` only (no Atlassian connection; no Jira/backlog available to search).

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings.
The worst alignment risk is **AL-07 Resource contention**: Payments and Data both book Platform's Q3 capacity ("assuming Platform provisions this in July"; "expect the pipeline itself to be handled at the infra level") while Platform's own page declares "Q3 is fully committed" and holds infra requests to Q4 — two committed KRs rest on capacity nobody has allocated.
Downstream of that, Growth's Aug 15 upgrade launch depends on a billing API whose only stated date is Sep 26 (AL-06 Timeline mismatch), and Data's streaming-pipeline dependency appears nowhere in Platform's OKRs (AL-01 Unacknowledged dependency).
Company priority C4 (Brightledger Capital, due Sep 30) has zero coverage across all four teams (AL-10 Strategy coverage gap).
The most common quality issue is **AP-04 KR Without Baseline** — three KRs across Growth and Platform state a target with no starting point.
Two KRs cannot be honestly scored at all (AP-09 Metric Nobody Can Measure, Platform and Data), and Payments and Growth are pushing the checkout funnel in opposite directions (AL-02 Conflicting metrics / adversarial incentives).
Recommended first action: Elena R. publishes a Q3 yes/no on the PCI-scoped infra and the streaming pipeline migration this week — three findings unblock on that answer.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Data | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.27) · Growth C (2.59) · Payments B (3.10).

- Platform: K5=2 — developer-satisfaction and SOC 2 KRs name no system of record (AP-09).
- Data: K1=2 — "Significantly improve data quality across core tables." states nothing countable.
- Growth: K1=2 — two KRs state targets with no baseline (AP-04 KR Without Baseline).
- Payments: K1=2 — the API v2 GA milestone KR carries no metric and no baseline.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no survey, instrument, or dashboard defining a "developer satisfaction score" exists anywhere in the corpus (all four team pages, the company priorities page and the Q2 appendix were searched) and no KR creates one, so the 8/10 can never be honestly scored; it also states no current value, leaving the ambition unjudgeable.
- Scores affected: K1=1, K5=1, K3=2 (per-OKR PL1 capped at 1.9 by the Critical cap)
- Suggested rewrite: "KR PL1.3: Quarterly internal developer survey (n ≥ `<respondents>`, run in `<named survey tool>`): satisfaction `<baseline>`/10 → 8/10, same instrument every quarter." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" is given no formula, score, or system of record anywhere in the corpus (all four team pages, company priorities and the Q2 appendix searched), and "Significantly" sets no magnitude — at quarter end nobody can say whether this happened or not.
- Scores affected: K1=0, K5=0, K3=2 (KR score capped at 1.0; per-OKR D1 capped at 1.9)
- Suggested rewrite: "KR D1.3: Core-table rows failing the `<named data-quality test suite>` `<baseline>`% → `<target>`%, measured weekly over the same table list as D1.1 (source: `<data-quality dashboard>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR begins with "Ship", names no metric and no baseline→target pair, so it is satisfied by the release event itself even if no traffic, no customer and no error rate moves — the only way to fail it is to be late.
- Scores affected: K1=0, K2=1, K3=2 (KR score capped at 1.0 by the K1=0 cap)
- Suggested rewrite: "KR P1.2: `<share>`% of checkout and billing API calls served by v2 by Sep 26 (0% → `<share>`%), with v2 error rate ≤ `<threshold>`% (source: `<API gateway dashboard>`)." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the KR names a 22% target with no starting point, and no trial-to-paid figure exists anywhere in the corpus — the Q2 business-review appendix reports only chargebacks, uptime and qualified signups — so neither the ambition nor mid-quarter progress can be judged.
- Scores affected: K1=2, K3=2 (calibration unverifiable per the rubric's no-baseline cap)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, monthly cohort basis (source: `<funnel dashboard>`)." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid distribution without indicating the funnel outcome G2 claims — the KR can be hit while signups and conversion stay flat; and no current pageview figure appears in any searched page, so 50,000 is uncalibrated. The "*(aspirational)*" marker on the same line limits the damage but does not make the metric informative.
- Scores affected: K1=2, K2=2, K3=2, K7=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, first-touch attribution (source: `<attribution report>`)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, second document): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing-90-day actual, so the KR is achieved by changing nothing and would still score green through a fivefold increase in downtime — while company priority C2 asks the company to "hold enterprise-grade reliability".
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → ≥ 99.97% monthly, with error-budget burn reviewed weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR begins with "Complete" and restates the deliverable rather than any result measure; with no numeric scale it can only score 0% or 100% mid-cycle, so the team gets no steering signal until the audit lands or doesn't.
- Scores affected: K1=0, K2=1 (KR score capped at 1.0), K6=3
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II evidence requests (0/`<N>` → `<N>`/`<N>`), auditor's report received by `<date>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41); dependency phrase: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's need-by date for the new billing API is Aug 15; the only date Payments states for that API is Sep 26 GA — the consumer ships roughly six weeks before its dependency exists, and the 300-upgrade target depends on a flow that cannot be live on time.
- Detection check that fired: AL-06 dependency-map edge date comparison — consumer need-by (Aug 15) precedes producer delivery (Sep 26), a hard inversion.
- Disconfirming checks run: **Late date ≠ inversion** — searched Payments' page for an earlier beta/EA/preview milestone of API v2: none exists, "by Sep 26" is the only date on the page. Commitment level — both pages state "Commitment: KRs are committed unless marked (aspirational)." (`sample-portfolio.md` › Payments team — Q3 2026 › line 19) and neither KR carries the aspirational marker, so both sides are committed. No contingency is stated on Growth's side beyond "should be fine".
- Inference labels: none — all load-bearing text quoted. (The June sync between Marcus and Priya is quoted as asserted; it names no date and changes neither page's dates.)
- Verdict: CONFIRMED (every quote re-fetched and matched character-for-character against the source)
- Recommended resolution owner: Priya N. (Payments) with Marcus T. (Growth) — decide within one week whether an Aug 15 partial/beta cut of the billing API is possible, or re-date G1.3 and its 300-upgrade target into the post-Sep-26 window.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments · Growth · Platform · Data
- Company evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (`sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Payments evidence: "Objective P1: Make checkout something customers never think about" (line 21) and "Objective P2: Cut fraud losses without drama" (line 26) (`sample-portfolio.md` › Payments team — Q3 2026)
- Growth evidence: "Objective G1: Make the first week with Brightledger magical" (line 38) and "Objective G2: Turn our funnel into a machine" (line 43) (`sample-portfolio.md` › Growth team — Q3 2026)
- Platform evidence: "Objective PL1: Keep the lights on, cheaper" (line 56) and "Objective PL2: Earn enterprise trust" (line 61) (`sample-portfolio.md` › Platform team — Q3 2026)
- Data evidence: "Objective D1: One trustworthy source of truth" (line 73) and "Objective D2: Own onboarding personalization end-to-end" (line 78) (`sample-portfolio.md` › Data team — Q3 2026)
- Conflict: C4 is a dated company priority with a Sep 30 deadline, and none of the eight team objectives — nor any of their KRs or notes — touches invoice financing, design partners, or a pilot. The quarter's most time-boxed company bet has no staffed child.
- Detection check that fired: AL-10 top-down strategy trace — a company objective with zero contributing children across the full swept team set.
- Disconfirming checks run: **Zero hits ≠ coverage gap** — re-searched all four team sections under synonyms and program names ("Capital", "financ", "invoice-financing", "design partner", "pilot"): the only occurrence in the corpus is line 13 itself, so there is no near-miss to quote. Checked the company objective's own page for an owner outside the swept teams: the page names only "Owner: Dana W. (CEO)" (line 8) for the priorities page as a whole and assigns C4 to no function.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Dana W. (CEO) — name an owning team and its Q3 KRs for C4, or move the pilot out of Q3, before the mid-quarter review; a Sep 30 pilot with no owner at the start of the quarter will not land.

### [Critical] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82); the dependent KR: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (`sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65); closest partially-matching items on Platform's side: "Objective PL1: Keep the lights on, cheaper" (line 56) and "Objective PL2: Earn enterprise trust" (line 61)
- Conflict: Data's committed D1.1 requires all product events to be served from schema v2, which its own note says rides on a streaming pipeline migration Data does not own; nothing in Platform's objectives, KRs or notes mentions that migration, and Platform's note defers infra requests to Q4. The deliverable D1.1 rests on is in nobody's plan.
- Detection check that fired: AL-01 dependency-map edge acknowledgment check — the phrases "rides on" and "handled at the infra level" resolve to the infrastructure owner (Platform); a search of Platform's page for "streaming", "pipeline", "schema" and "migration" returns zero hits. Platform's two objectives are the only partial matches, and they cover reliability/cost and SOC 2/pen-test work — neither is a data-pipeline build, so neither covers the need.
- Disconfirming checks run: **Missing mention ≠ unacknowledged** — a producer may track work outside its OKRs, but this corpus is a single-file export with no Jira project, epic list, or backlog available and no Atlassian connection in scope; the absence claim is therefore bounded to Platform's OKR page and the company priorities page, stated here as a limitation. Per the AL-07/AL-01 disambiguation rule this finding covers only the missing named deliverable; the capacity arithmetic is reported once, below, under AL-07 Resource contention (cross-referenced).
- Inference labels: resolving "the infra level" to the Platform team is analyst inference — Data's note names no team; it is supported by Platform being the only infrastructure-owning team in scope and by Platform's own use of the same word in "Holding all non-critical infra requests until Q4."
- Verdict: CONFIRMED (all quotes re-fetched and matched character-for-character; severity is Critical because Data's KR is committed under its page's commitment convention and Platform has explicitly deferred this request class to Q4)
- Recommended resolution owner: Elena R. (Platform) with Jonas K. (Data) — within one week, either place the streaming pipeline migration in Platform's Q3 plan with a date, or re-scope D1.1 to the events that can move without it.

### [Major] AL-07 Resource contention: Payments · Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (declared supply): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams book the same Q3 capacity — Payments assumes July provisioning of PCI-scoped infra, Data assumes the streaming pipeline is handled "at the infra level" — from a team that states its quarter is fully committed to SOC 2 and cost work and is holding infra requests to Q4. Combined committed demand exceeds the only declared supply statement in the corpus, and neither assumption is acknowledged anywhere on Platform's page.
- Detection check that fired: AL-07 resource-node fan-in — every cross-team resource mention was grouped by owning resource; Platform carries two distinct claimants in the same quarter, which then failed the declared-supply check against Platform's own capacity statement.
- Disconfirming checks run: **Plural demand ≠ contention** — checked for an allocation living outside the OKR pages: no capacity/allocation table, Jira board, or scheduled epics exist in this corpus (single-file export, no Atlassian connection), so no allocation falsifies the finding; confirmed both claims fall in the same period (both pages headed "— Q3 2026") and name the same resource rather than similarly-named pods (Payments names "Platform" explicitly; Data's "infra level" is labeled below). Per the AL-07/AL-01 disambiguation rule, Payments' ask is a pure provisioning/capacity claim and folds entirely into this finding, while Data's named deliverable additionally carries its own AL-01 above; the capacity arithmetic appears only here.
- Inference labels: resolving Data's "the infra level" to the Platform team is analyst inference (Data's note names no team); "as discussed in standup" is quoted as Payments' assertion and is not treated as a Platform commitment — no Platform document confirms it.
- Verdict: CONFIRMED (all quotes re-fetched and matched character-for-character)
- Recommended resolution owner: Elena R. (Platform) — publish a Q3 allocation decision on the PCI-scoped infra and the streaming pipeline within one week, including an explicit "no" if that is the answer, so Payments and Data can re-plan while the quarter is young.

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface; taking coverage from 35% to 90% of transactions predictably suppresses completion on the same surface Growth commits to lift by ten points. Neither team's page mentions the other, so the trade is being made implicitly, quarter-long, by two separate teams.
- Detection check that fired: AL-02 surface-lever key — both KRs sit on the checkout surface, Payments' stated lever ("step-up verification coverage") is a verification/friction control there, and Growth targets that surface's conversion metric. The metric-identity key produced nothing for this pair (the metric names differ), which is exactly the pair a catalog-only pass would miss.
- Disconfirming checks run: shared or parent OKR covering both — none found (searched company priorities C1–C4 and both team pages; C1 and C3 sit above the two KRs separately, with no shared guardrail); documented split of levers — none found; directionality — confirmed opposed (the lever raises friction on the surface whose throughput the other KR must raise). Separately generated and killed on the same surface: Payments' "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) against Growth's checkout conversion — lookalike checkout metrics with different populations pushing the same direction with no control lever on either side; that kill does not weaken this candidate.
- Inference labels: the verification→conversion mechanism is analyst inference — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-fetched and matched character-for-character)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth), arbitrated by Dana W. — agree a guardrail pair before step-up coverage passes `<coverage>`%: a chargeback ceiling for Growth's experiments and a checkout-conversion floor for Payments' rollout [proposal — placeholder target].

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to the same metric, from the same 31% baseline, on the same population, with different targets (40% vs 35%) — so the quarter has two answers to the question of whether activation succeeded, and no single accountable owner. Data's objective claims to "Own onboarding personalization end-to-end" while Growth's G1 owns the first week those same signups live through.
- Detection check that fired: AL-03 clustering by target metric plus target population (new-user activation rate, new signups). AL-02's metric-identity key also fires (same canonical metric, same direction, incompatible targets) and is cross-referenced here — per the one-finding-one-failure-mode rule the root cause is the undivided ownership, not the metric arithmetic.
- Disconfirming checks run: **Similar objectives ≠ duplication** — searched both pages for a cross-reference, shared epic, joint owner, or explicit lane split: Growth's note names only Payments ("Marcus synced with Priya in June"), Data's note names only the infra level, and neither page mentions the other team; no parent objective in the company priorities assigns lanes. Population/surface split — not evidenced: both KRs start from the identical 31% baseline, and Growth's stated definition "(first invoice sent within 7 days)" is the only definition in the corpus. A definitional split would be AL-08 Terminology collision, but Data states no definition to diff.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Dana W. (CEO) — assign one accountable owner and one target for new-user activation within one week; Growth and Data then split levers explicitly (funnel surface vs personalization model) and cross-link both pages.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "Objective D1: One trustworthy source of truth" (`sample-portfolio.md` › Data team — Q3 2026 › line 73); its KRs measure "cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check" (line 74) and "critical-dashboard data latency" (line 75)
- Company evidence: "C1 — Grow self-serve revenue" (line 10) · "C2 — Become enterprise-ready" (line 11) · "C3 — Cut fraud losses" (line 12) · "C4 — Launch Brightledger Capital" (line 13) (`sample-portfolio.md` › Company Q3 2026 priorities)
- Conflict: D1 claims no parent priority, none of its KR metrics is a company-level metric or a stated driver of one, and the priorities page never mentions data, dashboards, or reporting — the objective consumes a quarter with nothing above it that it serves.
- Detection check that fired: AL-04 strategy-trace leaf with no parent — the three-way check (explicit link, metric linkage, strategy-page mention) returned zero of three.
- Disconfirming checks run: **No parent link ≠ orphan** — (a) explicit link: Data's page carries none, unlike Payments' page which cites "(company priority C3)" (line 30), showing this corpus does use explicit links where they exist; (b) metric linkage: C1's metric is "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3.", C2's is "complete SOC 2 Type II and hold enterprise-grade reliability.", C3's is "bring chargeback rate under 0.5% after the Q2 incident." and C4's is the invoice-financing pilot — none is measured or documented as driven by D1's KRs; (c) strategy-page mention: searched the priorities section for "data", "dashboard", "metric", "quality", "latency" and "schema" — zero hits. Severity held at Minor: the capacity escalation was checked and not met — Data quotes "we've sized our part at 3 engineer-months" (line 82) but states no team size, so the taxonomy's large-stated-fraction-of-capacity condition is not evidenced.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED
- Recommended resolution owner: Jonas K. (Data) with Dana W. — state D1's parent priority at the next portfolio review, or propose a data-trust priority for the company page; D1.1's exec-dashboard reconciliation metric is the strongest candidate anchor.

## 5. Prioritized action list

1. Publish Platform's Q3 allocation decision on the PCI-scoped infra and the streaming pipeline migration, including an explicit "no" — owner: Elena R. (resolves §4 AL-07 Resource contention and §4 AL-01 Unacknowledged dependency).
2. Re-sequence Growth's Aug 15 upgrade launch against the Sep 26 billing-API GA, or agree an earlier partial cut — owner: Marcus T. with Priya N. (resolves §4 AL-06 Timeline mismatch).
3. Name an owning team and Q3 KRs for company priority C4, or move the pilot out of Q3 — owner: Dana W. (resolves §4 AL-10 Strategy coverage gap).
4. Replace the two unscoreable KRs with instrumented measures before the first check-in — owners: Elena R. (PL1.3) and Jonas K. (D1.3) (resolves both §3 AP-09 Metric Nobody Can Measure blocks).
5. Agree a chargeback-ceiling / conversion-floor guardrail pair before step-up coverage rises — owner: Priya N. with Marcus T. (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
6. Assign one accountable owner and one target for new-user activation, then split levers in writing — owner: Dana W. (resolves §4 AL-03 Duplicated / overlapping objectives).
7. Re-target Platform's uptime KR above the quoted 99.95% trailing baseline — owner: Elena R. (resolves §3 AP-06 Sandbagged Target).
8. Convert the API v2 GA and SOC 2 audit KRs into graded adoption and closure measures — owners: Priya N. and Elena R. (resolves both §3 AP-01 Task Masquerading as KR blocks and AP-02 Binary KR with No Gradient).
9. Add a baseline to the trial-to-paid KR and replace the blog-pageview KR with attributed signups — owner: Marcus T. (resolves §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).
10. State D1's parent company priority, or propose a data-trust priority for the company page — owner: Jonas K. (resolves §4 AL-04 Orphan objective).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.15); qualifies on a Critical finding: AP-09 Metric Nobody Can Measure, plus inbound AL-01 Unacknowledged dependency and AL-07 Resource contention): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88221 (PLAT-OKR-Q3), section 'Platform team — Q3 2026' of the local export `sample-portfolio.md`; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Data** (roll-up C (2.27); qualifies on Critical findings: AP-09 Metric Nobody Can Measure and AL-01 Unacknowledged dependency against its committed D1.1): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88225 (DATA-OKR-Q3), section 'Data team — Q3 2026' of the local export `sample-portfolio.md`; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Growth** (roll-up C (2.59); qualifies on the Critical AL-06 Timeline mismatch against its committed G1.3): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88217 (GRW-OKR-Q3), section 'Growth team — Q3 2026' of the local export `sample-portfolio.md`; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
- **Payments** (roll-up B (3.10), above the needs-rework threshold, but qualifies on the Critical AL-06 Timeline mismatch it is the producer side of): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: Confluence page 88213 (PAY-OKR-Q3), section 'Payments team — Q3 2026' of the local export `sample-portfolio.md`; strategy doc: 'Company Q3 2026 priorities', Confluence page 88101 (CO-PRIO-Q3)."
