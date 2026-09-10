# Brightledger — Q3 2026 Portfolio OKR Review

**Mode:** portfolio (4 teams in scope: Payments, Growth, Platform, Data) · **Period:** Q3 2026 · **Strategy source:** "Company Q3 2026 priorities" (C1–C4)
**Corpus:** `input.md` — the single source of OKR content for this run; no Atlassian connection was available, so Jira/Confluence backlog checks could not be run. Source refs below use the short path `input.md`.

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; **5 Critical, 10 Major, 1 Minor** findings.
The portfolio's single worst alignment risk is **AL-02 Conflicting metrics / adversarial incentives**: Payments is driving step-up verification from 35% to 90% of transactions while Growth commits to +10pt checkout conversion on the same funnel — neither page mentions the other team.
The most common goodness anti-pattern is **AP-04 KR Without Baseline** (2 confirmed instances, Growth and Platform); no team scores above K1=2, so ambition is unjudgeable portfolio-wide.
Company priority C4 (Brightledger Capital) is claimed by no team's objective or KR (**AL-10 Strategy coverage gap**).
Platform is the silent dependency of both Payments and Data while its own page holds all non-critical infra requests until Q4 (**AL-07 Resource contention**, **AL-01 Unacknowledged dependency**).
Growth's Aug 15 upgrade launch rides on a billing API that Payments does not GA until Sep 26 (**AL-06 Timeline mismatch**).
Data's D1 objective traces to no company priority and one of its KRs can never be scored (**AL-04 Orphan objective**, **AP-09 Metric Nobody Can Measure**).
Recommended first action: the CEO assigns an owner for C4 this week, and VP Product convenes Payments + Growth on the fraud-friction/conversion pair before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 3 | 2 | 3 | 1 | 1 | 3 | 2 | 3 | 1 | 2 | 2 |
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.25) · Platform C (2.54) · Growth B (2.85) · Payments B (2.98).

- Data: K1=1, K5=1 — one KR states no number and names no measuring system (AP-09).
- Platform: K3=2 — uptime target sits below the quoted 99.95% trailing baseline (AP-06).
- Growth: O2=2 — "magical" and "machine" are abstractions two readers would gloss differently.
- Payments: K1=2 — the API v2 GA milestone carries no metric and no baseline (AP-01).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (input.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" names no score, no formula and no population, and the corpus contains no dashboard or tool that could report it — the only named instrument anywhere in the file is the "Datadog SLO monitor" for uptime (line 89). The KR can never be honestly scored at quarter end. Search performed: the whole file (company priorities, all four team pages, Q2 review appendix) for any data-quality instrument, score, or system of record — no hit.
- Scores affected: K1=0, K5=0 (KR score capped at 1.0), K7=2; caps D1's per-OKR score at 1.9 (D)
- Suggested rewrite: "KR D1.3: Null rate on the `<n>` core tables' required columns `<baseline>`% → `<target>`%, and freshness-SLA breaches per week `<baseline>` → `<target>`, both reported by a new Data Quality dashboard live by `<date>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (input.md › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR is a deliverable, not a measurable result — it begins with "Ship", states no metric and no baseline→target pair, and succeeds in full even if no customer or internal consumer ever moves onto v2. Growth is depending on this same API (line 48), so shipping without adoption also leaves the dependency unresolved.
- Scores affected: K1=0, K2=1 (KR score capped at 1.0), K6=3
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing traffic served by API v2 (0% → `<target>`%) with v2 error rate ≤ `<threshold>`, GA by Sep 26." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (input.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: the target is stated with no starting point, so neither the ambition nor mid-quarter progress can be judged. Search performed: the whole file, including the Q2 2026 business review appendix (lines 89–91, which reports uptime, chargeback rate, step-up coverage and qualified signups) — no trial-to-paid value appears anywhere in the corpus.
- Scores affected: K1=2, K3=2 (calibration unverifiable cap)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% (per `<named analytics dashboard>`) → 22%, measured on trials started in the quarter." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews. *(aspirational)*" (input.md › Objective G2: Turn our funnel into a machine › line 46)
- Why it's a problem: pageviews is a cumulative exposure total that rises with spend and publishing volume without indicating that the funnel converts anything — the outcome objective G2 claims. It also carries no baseline, so its ambition is unjudgeable, and it is the KR in G2's set that serves a different goal (content reach) than the other two.
- Scores affected: K1=2, K2=2, K3=2, K7=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed in `<named analytics system>`." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (input.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, other end of the cross-source claim): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (input.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits *below* the trailing-90-day actual already achieved and reported in the same corpus, so the KR is met by doing nothing — and it permits a reliability regression of 0.05pp while company priority C2 asks the team to "hold enterprise-grade reliability" (line 11).
- Scores affected: K3=1, K1=3 (baseline retrievable from the quoted appendix, not from the KR); contributes to PL1's ≥2-Major cap at 2.4
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.97%, with error budget burn ≤ `<threshold>`% per month." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (input.md › Platform team — Q3 2026 › line 56)
- Why it's a problem: "Keep the lights on" is the team's standing operational duty stated with no delta — it is achieved by default staffing and encodes no choice, which is why the objective's own first KR is a "Maintain" target. Only the ", cheaper" clause carries a real change, and it is the one clause with a genuine baseline→target KR (PL1.2, line 58); the BAU framing is what lets the sandbagged uptime KR and the instrument-less satisfaction KR sit beside it unchallenged.
- Scores affected: O1=2, K6=2, K7=2; contributes to PL1's ≥2-Major cap at 2.4
- Suggested rewrite: "Objective PL1: Every transaction costs us less and nobody notices the infrastructure — KR: cloud spend per 1,000 transactions $4.10 → $3.20; KR: API uptime 99.95% → 99.97%; KR: customer-visible incidents `<baseline>` → `<target>` per quarter." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (input.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Why it's a problem: the target 8/10 is stated with no current value, so the ask could be a half-point or a four-point move. Compounding it, no survey, instrument or cadence is named for the score, and the corpus contains none. Search performed: the whole file for any developer-satisfaction, survey or eNPS value or instrument — no hit; the only named instrument in the corpus is the Datadog SLO monitor (line 89).
- Scores affected: K1=2, K5=1, K2=2, K3=2; contributes to PL1's ≥2-Major cap at 2.4
- Suggested rewrite: "KR PL1.3: Internal developer satisfaction `<baseline>`/10 → 8/10 on the quarterly engineering survey (n ≥ `<minimum responses>`, `<named survey tool>`)." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (input.md › Objective PL2: Earn enterprise trust › line 63)
- Why it's a problem: the KR is a single done/not-done event, so it can only ever score 0% or 100% and gives no mid-cycle signal on whether the quarter's most exec-visible commitment (company priority C2, line 11) is on track. Platform's own notes say the quarter is consumed by "SOC 2 evidence collection" (line 65) — work that has a countable gradient the KR declines to use.
- Scores affected: K1=0, K2=1 (KR score capped at 1.0), K6=3
- Suggested rewrite: "KR PL2.2: Close 100% of the `<n>` open SOC 2 Type II evidence requests (0/`<n>` → `<n>`/`<n>`), audit fieldwork complete and report received by `<date>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Data
- Evidence: "Migrate 100% of product events to unified event schema v2." (input.md › Objective D1: One trustworthy source of truth › line 74)
- Why it's a problem: the KR measures completion of the team's own migration work rather than a result anyone outside the team experiences — the "100%" is a percentage of work delivered, not an outcome, and no baseline states how many events are on v2 today or how many "product events" there are. The objective's promised end-state (a source of truth people actually trust) is untouched by hitting it.
- Scores affected: K1=2, K2=2, K3=2, K7=2
- Suggested rewrite: "KR D1.1: Product events served from unified schema v2 `<baseline>`/`<total>` → `<total>`/`<total>`, with `<target>`% of critical dashboards reading v2 and zero schema-related incidents." [proposal — placeholder target]

## 4. Alignment findings

Blocking keys used for the pairwise checks (per `references/alignment-taxonomy.md` Part 2 Step 3): canonical metric (AL-02, AL-09); metric + surface/population cluster — checkout funnel, onboarding/activation (AL-03); metric name shared across teams, and near-identical definitions (AL-08). Graph-structural checks (AL-01, AL-06, AL-07, AL-11, AL-12) ran on the dependency map built from lines 30, 48 and 82; strategy checks (AL-04, AL-05, AL-10) ran against C1–C4. AL-05, AL-09, AL-11 and AL-12 produced no surviving candidates; the cycle check found no cycle (Platform depends on no one), and the commitment-label check found one convention — "KRs are committed unless marked (aspirational)." (line 19) — applied uniformly on all four pages.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (input.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (input.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification interposes an additional authentication challenge in the checkout flow; taking it from 35% to 90% of transactions means roughly two-thirds of all checkouts newly acquire a friction step in the same quarter Growth commits to a 10-point conversion gain on that same checkout. Payments' own objective concedes the risk in its title — "Cut fraud losses without drama" (line 26) — but neither team's page names the other, and no KR on either side measures the tradeoff.
- Detection check that fired: AL-02 heuristic (2) — known tension pair, where one KR's stated mechanism (step-up verification coverage) is a driver of the other's metric (checkout conversion), surfaced by metric-catalog blocking on the shared checkout-funnel surface.
- Disconfirming checks run: directionality/same-metric check — the metrics differ by name, so this is a mechanism-level rather than same-metric conflict (result: not the Critical-by-opposed-targets path); explicit shared or parent OKR covering both — searched both team pages and the company priorities, where C1 (self-serve revenue) and C3 (fraud) sit above them separately with no reconciling parent OKR, none found; documented split of levers or guardrail — searched both pages' KRs and notes, none found; aspirational-label check — neither KR is marked aspirational under the pages' stated convention (line 19), so the Minor downgrade does not apply.
- Inference labels: the step-up-verification → checkout-friction → conversion mechanism is **analyst inference** — no Brightledger document quotes the tradeoff. The severity escalation is not inferred: it rests on the quoted exec visibility of Payments' objective, "Fraud work is our top ask from leadership after the Q2 incident (company priority C3)." (line 30).
- Verdict: CONFIRMED (both KR quotes re-verified character-for-character; the mechanism linking them remains labeled inference)
- Recommended resolution owner: VP Product convenes Priya N. and Marcus T. to agree a guardrail pair — a chargeback ceiling and a checkout-conversion floor, with step-up applied by risk score rather than blanket coverage — and to restate P2.2 as risk-targeted coverage before mid-quarter. Severity is escalated from AL-02's mechanism-level default (Major) to Critical under the taxonomy's escalation rule, on the quoted exec visibility of the affected objective.

### [Critical] AL-10 Strategy coverage gap: Company strategy ↔ all four teams
- Company evidence: "**C4 — Launch Brightledger Capital:** invoice-financing pilot live with 3 design partners by Sep 30." (input.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss, distinguished): "Ship checkout & billing API v2 to GA by Sep 26." (input.md › Objective P1: Make checkout something customers never think about › line 23) — the only Q3 deliverable in any team's OKRs that touches the money-movement surface a financing product would sit on. It does not count as coverage: it names no financing, lending or design-partner work, and its own objective is about checkout reliability.
- Conflict: a dated, committed company priority has zero contributing children. Four of four teams were swept; C1 is served by Growth's G1/G2, C2 by Platform's PL1.1/PL2, C3 explicitly by Payments' P2 — C4 alone has no objective, KR or note claiming it. The quarter's fourth strategic bet is, as written, nobody's job, and it carries the tightest deadline of the four (Sep 30).
- Detection check that fired: AL-10 top-down strategy trace — each company priority searched across all four teams' objectives, KRs and notes; C4 returned zero contributing children.
- Disconfirming checks run: synonym and program-name re-search — the whole file searched for "Capital", "invoice financing", "financing", "lending", "loan", "credit", "underwriting" and "design partner", with the only hit being C4's own line (line 13); named-owner check on the company priorities page — the page names one owner overall, "Owner: Dana W. (CEO)" (line 8), and assigns no per-priority owner and no function outside the swept team set, so this is a portfolio hole rather than an ownership note; near-miss check — the Payments API v2 KR quoted above, distinguished.
- Inference labels: none — all load-bearing text quoted; the absence claim states its full search scope above.
- Verdict: CONFIRMED (the C4 line and the near-miss KR re-verified character-for-character; the absence re-run against the whole file)
- Recommended resolution owner: Dana W. (CEO) names an owning team for C4 and lands a staffed objective with a design-partner count KR within one week, or explicitly moves the pilot out of Q3 — with a Sep 30 pilot date, an unassigned bet is the portfolio's most time-critical gap.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (input.md › Objective G1: Make the first week with Brightledger magical › line 41), with the dependency stated in the team's notes: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (input.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (input.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: a hard inversion. Growth's consumer milestone needs the new billing API by Aug 15; the producer does not deliver it until Sep 26 — roughly six weeks *after* the need-by date, with no integration margin at all, and only four days before quarter end for Growth to then drive 300 upgrades through the flow. Unlike the Data dependency below, this one is acknowledged on the producer's side; it is the dates, not the awareness, that do not work.
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer's delivery date (Sep 26) versus consumer's need-by date (Aug 15) on the Growth → Payments edge.
- Disconfirming checks run: "late date ≠ inversion" milestone check — searched Payments' page for any earlier milestone (beta, preview, partial or dark-launch availability) that Growth's integration could ride instead of GA; the page names GA and no other milestone, so the tightest quotable reading remains Sep 26; soft-date check — neither date is hedged ("targeting late Q3" or similar), both are stated flat, so the Minor downgrade does not apply; commitment check — under the pages' stated convention (line 19) neither KR is marked aspirational, so both are committed, which is AL-06's Critical condition; awareness check — Growth's note shows the two leads spoke ("Marcus synced with Priya in June, should be fine"), but it names no earlier milestone, no revised date and no resolution plan, so it does not resolve the inversion.
- Inference labels: none — all load-bearing text quoted, including the dependency phrase itself.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against their source lines)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) reconcile the two dates within one week — either Payments commits a dated partial or beta of the billing API that supports self-serve upgrades by `<date>`, or Growth moves G1.3's launch date and restates the 300-upgrade target for the shortened window [proposal — placeholder target]. "Should be fine" is not a plan; the arithmetic in the two quotes says it is not.

### [Critical] AL-01 Unacknowledged dependency: Data → Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (input.md › Objective D2: Own onboarding personalization end-to-end › line 82), carrying the committed KR "Migrate 100% of product events to unified event schema v2." (input.md › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (nearest match on the producer's side, quoted and distinguished): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (input.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Data's committed schema-v2 KR rests on a streaming pipeline migration it explicitly assigns to someone else ("handled at the infra level") while budgeting only "our part". Platform's page contains no objective, KR or note mentioning streaming, pipelines, event schemas or any data migration — and its one relevant statement is an affirmative hold on the whole category of work. Data's plan therefore depends on a project its producer has neither planned nor left room for.
- Detection check that fired: AL-01 edge acknowledgment — the dependency phrase "rides on the streaming pipeline migration" resolved to Platform as the owning team ("at the infra level"), then searched on the producer's side and found absent. Per AL-07's disambiguation rule this edge additionally earns its own AL-01 because it names a distinct deliverable — a migration Platform would have to plan as its own project — rather than a pure capacity or provisioning ask; the capacity arithmetic itself is reported once, under AL-07 below, which this finding cross-references.
- Disconfirming checks run: producer-side OKR search — Platform's section (lines 52–65) searched for "stream", "pipeline", "event", "schema", "data", "warehouse" and "migrat", zero hits; whole-file search for "streaming" and "pipeline" — the only occurrence in the entire corpus is Data's own note at line 82; "missing mention ≠ unacknowledged" backlog check — **could not be run**: no Atlassian connection is available for this review and the corpus is a single exported file, so Platform's Jira epics and committed backlog were not reachable. That unrun check is the one route by which this finding could still be downgraded to Minor; it does not weaken the quoted hold statement, which is a positive assertion rather than an absence.
- Inference labels: resolving "at the infra level" to the Platform team is **analyst inference** — Data's note names a function, not the team by name; Platform is the only infrastructure-owning team in the confirmed scope. All other load-bearing text is quoted.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character; the absence re-run against Platform's section and the whole file)
- Recommended resolution owner: Elena R. (Platform) and Jonas K. (Data) decide within one week whether the streaming pipeline migration is in Platform's Q3 — if it is, it needs a Platform KR; if it is not, D1.1 is not deliverable this quarter and should be rescoped. Severity is Critical rather than AL-01's Major default because Data's KR is committed under the pages' stated convention (line 19) and Platform has explicitly deprioritized the area; the deferral is categorical ("all non-critical infra requests") rather than a naming of this pipeline, which is exactly what the two leads must settle.

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (input.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (input.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (input.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs each draw on Platform's Q3 capacity in the same quarter that Platform declares that capacity fully spent on two other workstreams and holds the remaining category of requests to Q4. Combined demand exceeds declared supply, and neither claimant's page shows any sign of knowing it: Payments assumes a July provisioning date "as discussed in standup", Data assumes its pipeline is "handled at the infra level". Nobody has done this arithmetic, and Platform's own OKRs reserve no slot for either ask. Payments' PCI-scoped infra edge is reported here and only here — it is a provisioning ask, a claim on Platform's capacity itself, so per the taxonomy's disambiguation rule it folds entirely into this aggregate rather than earning a separate AL-01. Data's edge additionally names a distinct deliverable and is cross-referenced above as AL-01.
- Detection check that fired: AL-07 resource-node fan-in — shared-resource mentions grouped by resource rather than by edge, putting two distinct claimants on the Platform node in Q3, then Platform's own page checked for declared supply, which yielded the fully-committed statement.
- Disconfirming checks run: "plural demand ≠ contention" allocation check — searched Platform's section for any capacity table, allocation or named slot for either claimant, none found, and its only capacity statement is the hold quoted above (the Jira/allocation half of this check could not be run: no Atlassian connection, single-file corpus); same-quarter check — all three statements sit on Q3 2026 pages (Payments last updated 2026-07-02, Data 2026-07-01, Platform 2026-07-05), confirmed same quarter; same-resource check — both claimants name infrastructure owned by the one Platform team in scope, not similarly-named pods.
- Inference labels: resolving Data's "at the infra level" to Platform is **analyst inference** (see AL-01 above); Payments names Platform explicitly. The capacity conflict itself is quoted on all three sides.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against their source lines)
- Recommended resolution owner: Elena R. (Platform) publishes a Q3 allocation for the two inbound asks — PCI-scoped infra provisioning and the streaming pipeline migration — and takes the trade-off to the CEO staff meeting within one week, since honouring both while holding C2's SOC 2 commitment is what the quoted statement says Platform cannot do. Payments' and Data's committed KRs (P1.2, D1.1) should not stand unchanged until that allocation exists.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (input.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (input.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to moving the same named metric, on the same population and the same onboarding surface, to two different numbers — 40% and 35%. If the quarter ends at 37%, one team has overshot and the other missed, and no one can say who was accountable. Data's objective goes further and claims the surface outright — "Own onboarding personalization end-to-end" (line 78) — while Growth's G1 set treats first-week activation as its own. Neither page references the other team, and no division of labour is stated anywhere.
- Detection check that fired: AL-03 clustering on target metric plus target population/surface — "new-user activation rate", new signups, onboarding — which put the two KRs in one candidate set with inconsistent targets.
- Disconfirming checks run: "similar objectives ≠ duplication" — searched both team pages for any cross-reference, shared owner, shared epic, or explicit split of surfaces or segments (Growth's notes at line 48 reference Payments, not Data; Data's notes at line 82 reference infra, not Growth), none found; population/surface check — neither KR restricts itself to a distinct segment, geography or platform that would make the two legitimate lanes; parent-objective check — the company priorities name no parent that assigns lanes for activation; AL-02 check — the two KRs push the same metric in the *same* direction with no adversarial mechanism, so AL-02 was correctly not filed.
- Inference labels: none — all load-bearing text quoted. Cross-reference: **AL-08 Terminology collision** is a secondary contributor and is not filed separately (per the taxonomy's one-finding-one-failure-mode rule) — Growth defines activation in its KR as "first invoice sent within 7 days" while Data's KR states no definition, so the two numbers may not even measure the same thing; that ambiguity is part of what the resolution below must settle.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against their source lines)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) agree a single accountable owner for new-user activation and one shared definition and target before the end of month 1; the non-owning team's KR should be restated as a contributing lever (for Data, the personalization experiments themselves) rather than a second target on the same metric.

### [Minor] AL-04 Orphan objective: Data ↔ Company strategy
- Data evidence: "Objective D1: One trustworthy source of truth" (input.md › Data team — Q3 2026 › line 73), whose KRs are "Migrate 100% of product events to unified event schema v2." (line 74), "Cut critical-dashboard data latency from 6h to 1h." (line 75) and "Significantly improve data quality across core tables." (line 76)
- Company strategy evidence: the Q3 priority list in full — "**C1 — Grow self-serve revenue:** mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." · "**C2 — Become enterprise-ready:** complete SOC 2 Type II and hold enterprise-grade reliability." · "**C3 — Cut fraud losses:** bring chargeback rate under 0.5% after the Q2 incident." · "**C4 — Launch Brightledger Capital:** invoice-financing pilot live with 3 design partners by Sep 30." (input.md › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent, and none is findable. The three-way check: (a) explicit parent link — none, the objective and its KRs cite no company priority, unlike Payments which cites C3 by name at line 30; (b) company-level metric or documented driver — none of event-schema coverage, dashboard latency or data quality is a company metric, and no document in the corpus states a driver relationship between any of them and ARR, SOC 2, reliability, chargeback rate or the Capital pilot; (c) strategy-page mention — the company priorities page never mentions data, events, schemas, dashboards or analytics. Zero of three. Data's sibling objective D2 does trace to C1 via activation, which makes D1 the isolated half of the team's quarter.
- Detection check that fired: AL-04 three-way strategy-trace check, run per objective against the company priority list; D1 returned zero of three.
- Disconfirming checks run: self-justification check — searched Data's page for any stated rationale that would downgrade or kill the finding; the team's only note (line 82) is a dependency and sizing statement, not a strategic justification, so nothing was found to quote in D1's defence; capacity-escalation check — the page states an absolute size, "we've sized our part at 3 engineer-months" (line 82), but nowhere states the team's total capacity, so AL-04's Major condition (an orphan consuming a *large stated fraction* of team capacity) cannot be established from quoted text and the finding stays at its Minor default rather than being escalated on an inferred denominator; exploratory-charter check — no charter in the corpus designates Data for exploratory work.
- Inference labels: none — all load-bearing text quoted, and the absence claim states its search above. Note that a data-foundations objective may well be a legitimate enabler; the finding is that the corpus nowhere says so, not that the work is wrong.
- Verdict: CONFIRMED (the objective, its three KRs and all four company priority lines re-verified character-for-character)
- Recommended resolution owner: Jonas K. (Data) adds an explicit parent link to D1 — or, if the honest answer is that it serves the 2027 platform rather than a Q3 priority, states that on the page and gets it acknowledged by Dana W., so the quarter's capacity split is a visible decision rather than an implicit one.

## 5. Prioritized action list

1. Assign an owning team and a staffed objective for company priority C4 within one week, or move the pilot out of Q3 — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Convene Payments + Growth to agree a chargeback-ceiling / conversion-floor guardrail pair and restate step-up coverage as risk-targeted before mid-quarter — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
3. Reconcile the Aug 15 upgrade launch against the Sep 26 billing-API GA — commit a dated partial release or move G1.3 — owner: Priya N. and Marcus T. (resolves §4 AL-06 Timeline mismatch).
4. Decide whether the streaming pipeline migration is in Platform's Q3 and give it a Platform KR, or rescope D1.1 — owner: Elena R. and Jonas K. (resolves §4 AL-01 Unacknowledged dependency).
5. Rewrite D1.3 against a defined data-quality instrument with a baseline, or drop it from the OKR set — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure).
6. Publish a Q3 Platform allocation covering the PCI-scoped infra and pipeline asks and escalate the trade-off to CEO staff — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
7. Name one accountable owner, definition and target for new-user activation across Growth and Data — owner: Marcus T. and Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Reset the uptime KR against the quoted 99.95% trailing baseline and re-frame PL1 away from its keep-the-lights-on framing — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target, AP-10 BAU Dressed as OKR).
9. Add baselines and named systems of record to the trial-to-paid, blog and developer-satisfaction KRs — owner: Marcus T. (Growth) and Elena R. (Platform) (resolves §3 AP-04 KR Without Baseline ×2, AP-03 Vanity Metric).
10. Convert the three delivery-shaped KRs — API v2 GA, SOC 2 completion, schema migration — into adoption or gradient measures — owner: Priya N., Elena R. and Jonas K. (resolves §3 AP-01 Task Masquerading as KR ×2, AP-02 Binary KR with No Gradient).

## 6. Suggested single-team re-runs

All four teams qualify under criterion (b) — each is a party to at least one Critical finding — even though no team's roll-up grade is at or below the rubric's D needs-rework threshold. Ordered by the strength of the case.

- **Data** (roll-up C (2.25); AP-09 Metric Nobody Can Measure, plus AL-01 Unacknowledged dependency and AL-04 Orphan objective): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3; owner Jonas K.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Platform** (roll-up C (2.54); inbound AL-01 Unacknowledged dependency, plus AL-07 Resource contention, AP-06 Sandbagged Target, AP-10 BAU Dressed as OKR, AP-02 Binary KR with No Gradient, AP-04 KR Without Baseline): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3; owner Elena R.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Growth** (roll-up B (2.85); AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch, plus AP-04 KR Without Baseline and AP-03 Vanity Metric): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3; owner Marcus T.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Payments** (roll-up B (2.98); AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch, plus AP-01 Task Masquerading as KR): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `input.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3; owner Priya N.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
