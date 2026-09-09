# Brightledger — Q3 2026 OKR Portfolio Review

*Mode: portfolio (4 teams in scope: Payments, Growth, Platform, Data). Period: Q3 2026. Strategy source: "Company Q3 2026 priorities" (Confluence page 88101, CO-PRIO-Q3). Corpus: `input.md` (the four team pages, the company priorities page, and the Q2 2026 business-review appendix).*

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed for Q3 2026; 18 findings — 5 Critical, 12 Major, 1 Minor.
The portfolio's worst alignment risk is **AL-02 Conflicting metrics / adversarial incentives**: Payments is committed to driving step-up verification from 35% to 90% of transactions while Growth is committed to +10pt checkout conversion on the same funnel, and neither page mentions the other team.
Two further Criticals sit beside it: **AL-06 Timeline mismatch** (Growth's committed Aug 15 upgrade flow runs on a billing API that Payments does not GA until Sep 26) and **AL-10 Strategy coverage gap** (company priority C4, Brightledger Capital, has no team behind it anywhere in the portfolio).
The most common goodness anti-pattern is **AP-04 KR Without Baseline** — four KRs across three of the four teams state a target with no starting point, making ambition and progress both unjudgeable.
Platform and Data each carry a Critical **AP-09 Metric Nobody Can Measure** and land lowest on the heatmap (C (2.3) and C (2.2) respectively).
Platform is also the portfolio's capacity bottleneck: two teams assume its help in a quarter its own page calls fully committed (**AL-07 Resource contention**), and one of those asks names a deliverable absent from Platform's plans (**AL-01 Unacknowledged dependency**).
Recommended first action: a joint Payments/Growth session to set a shared fraud-vs-conversion guardrail and re-sequence the billing API against Growth's Aug 15 date, before mid-quarter.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 3 | 2 | 3 | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.2) · Platform C (2.3) · Growth B (2.8) · Payments B (3.1).

- Data: K1=1, K5=1 — the data-quality KR names no metric and no system of record (AP-09).
- Platform: K3=2 — the uptime KR targets less than the quoted trailing baseline (AP-06).
- Growth: K1=2 — two KRs state a target with no starting value (AP-04).
- Payments: K1=2 — the API v2 KR is a ship date with nothing countable (AP-01).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`input.md` › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: The KR names no metric, no scale, no target and no system of record, so it can never be honestly scored and D1 can never be shown achieved or missed. Search performed: all four team pages, the company priorities page, and the Q2 2026 business-review appendix in this file — the only named system of record anywhere in the corpus is "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input.md` › Appendix — Q2 2026 business review (extracts) › line 89), and no data-quality instrument appears at all.
- Scores affected: K1=0, K5=0, K3=2 (unverifiable-calibration cap), K7=2; per-OKR D1 capped at 1.9 by the rubric's Critical anti-pattern cap.
- Suggested rewrite: "KR D1.3: Core-table validation pass rate `<baseline>`% → `<target>`% across the `<N>` tables named in the core-table registry, run weekly by the schema v2 validation job." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Data
- Evidence: "Migrate 100% of product events to unified event schema v2." (`input.md` › Objective D1: One trustworthy source of truth › line 74)
- Evidence: "Ship personalized onboarding checklists to 100% of new signups." (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 79)
- Why it's a problem: Both KRs open with a delivery verb and measure completion of the team's own work rather than a result anyone outside the team experiences — each succeeds in full even if no dashboard gets more trustworthy and no signup activates. Neither states a baseline→target pair; "100%" is a scope statement, not a measured change.
- Scores affected: K2=2 (both KRs), K1=2 (both KRs), K3=2 (both, unverifiable-calibration cap).
- Suggested rewrite: "KR D1.1: Product events served from unified event schema v2 `<baseline>`% → 100% of daily event volume, with schema-validation error rate ≤ `<threshold>`%." / "KR D2.1: New signups completing their personalized checklist `<baseline>`% → `<target>`% within 7 days of signup." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Data
- Evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Why it's a problem: The KR states a target with no current value, so neither its ambition nor mid-quarter progress can be judged. Search performed: all four team pages, the company priorities page, and the Q2 review appendix — the only activation figure in the corpus is Growth's, on an explicitly different and defined population ("first invoice sent within 7 days"), so it is not retrievable as Data's baseline (see also §4 AL-03).
- Scores affected: K1=2, K3=2 (unverifiable-calibration cap), K5=2.
- Suggested rewrite: "KR D2.2: New-user activation rate (Growth's shared definition: first invoice sent within 7 days) `<baseline, as of Q2>`% → `<target>`%, measured on the shared activation dashboard." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Why it's a problem: The KR quantifies an internal state against a "score" that no instrument in the corpus produces, so it can never be honestly scored. Search performed: all four team pages, the company priorities page, and the Q2 review appendix — no survey, eNPS instrument, tool, or dashboard for developer satisfaction appears anywhere; the KR also states no baseline, so AP-04 KR Without Baseline co-occurs here.
- Scores affected: K1=1, K5=1, K3=2 (unverifiable-calibration cap), K7=2; per-OKR PL1 capped at 1.9 by the rubric's Critical anti-pattern cap.
- Suggested rewrite: "KR PL1.3: Internal developer NPS `<baseline>` → `<target>`, quarterly survey of all product engineers (n ≥ `<N>`) run on `<named survey tool>`, first wave by `<date>`." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, other document): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: The target sits below the quoted trailing baseline, so the KR is achieved by letting reliability degrade and cannot be missed without a large regression. It also serves company priority C2's "hold enterprise-grade reliability" with a bar the company has already cleared.
- Scores affected: K3=1, K1=2 (the KR cites no baseline of its own, which is what conceals the sandbag).
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.98%, measured monthly against the same monitor." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input.md` › Objective PL2: Earn enterprise trust › line 63)
- Why it's a problem: The KR is done/not-done, so mid-cycle it can only score 0% or 100% and gives the team no steering signal on the company's dated C2 commitment. Nothing countable is stated — no evidence-collection scope, no finding count, no audit date.
- Scores affected: K1=0, K2=1; the KR's own score is capped at 1.0 by the rubric's K1=0 cap.
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II evidence requests (baseline 0/`<N>`), with the auditor's report received by `<date>`." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Evidence (objective it sits under): "Keep the lights on, cheaper" (`input.md` › Objective PL1: Keep the lights on, cheaper › line 56)
- Why it's a problem: There is no causal chain in two steps or fewer from a developer satisfaction score to either uptime or cloud spend, and the KR shares no nouns or domain with its objective — hitting it would not move PL1. It is the third unrelated cluster in a two-clause objective, which is why the KR set reads as a metrics grab bag.
- Scores affected: K7=2, K6=2.
- Suggested rewrite: "KR PL1.3: Median time-to-restore for Sev-1 incidents `<baseline>` min → `<target>` min, from the on-call incident log." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input.md` › Objective PL1: Keep the lights on, cheaper › line 56)
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Why it's a problem: The objective names the team's standing operational duty and its lead KR asks only for maintenance, so half the objective is achieved by default staffing and displaces a real goal in a quarter the team already calls fully committed. Only the "cheaper" clause carries a delta.
- Scores affected: O1=2, K3=1, K6=2.
- Suggested rewrite: "Objective PL1: Brightledger costs less to run every month without anyone noticing — KR: cloud spend per 1,000 transactions $4.10 → $3.20; KR: API uptime 99.95% → 99.98%." (Move the standing reliability duty to a health-metric section outside the OKRs.) [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`input.md` › Objective G2: Turn our funnel into a machine › line 46)
- Evidence (objective it sits under): "Turn our funnel into a machine" (`input.md` › Objective G2: Turn our funnel into a machine › line 43)
- Why it's a problem: Pageviews rise with publishing volume and paid distribution without indicating anything about funnel efficiency, the outcome G2 claims, so the KR can be hit while conversion and signups both fall. It is correctly marked "(aspirational)", so AP-08 does not apply — the defect is the metric, not the label.
- Scores affected: K2=2, K1=2, K7=2 (it is the orphan KR in G2's set).
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed on the signup-source report." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`input.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Evidence: "Reach 50,000 monthly blog pageviews." (`input.md` › Objective G2: Turn our funnel into a machine › line 46)
- Why it's a problem: Both state a target with no starting point, so nobody can say whether 22% is a stretch or already the status quo, and mid-quarter progress is unreadable. Search performed: all four team pages, the company priorities page, and the Q2 review appendix — the appendix carries only uptime, chargeback/step-up coverage, and qualified signups, so neither baseline is retrievable. Growth's sibling KRs show the team knows how to do this ("from 31% to 40%", "from 2,100/mo to 2,800/mo").
- Scores affected: K1=2 (both KRs), K3=2 (both, unverifiable-calibration cap).
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, monthly cohort, per the signup funnel report." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input.md` › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: The KR is a delivery milestone whose only failure mode is lateness — it scores 100% on the ship date even if no traffic runs on v2 and checkout gets no better, which is the opposite of what P1 claims. It is also the KR two other teams depend on (see §4 AL-06 and §4 AL-07), so its lack of an adoption measure hides integration risk.
- Scores affected: K1=0, K2=1; the KR's own score is capped at 1.0 by the rubric's K1=0 cap.
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing requests served by API v2 by Sep 26 (baseline 0%), with v2 error rate ≤ `<threshold>`% and v1 deprecation date published." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`input.md` › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence (the dependency phrase): "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`input.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`input.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's consumer date (Aug 15) precedes its producer's delivery date (Sep 26) by roughly six weeks, so the flow Growth commits to launching runs on an API that has not reached GA when it launches — and the 300-upgrade target then has under five weeks of quarter left. Both KRs are committed under their pages' stated convention ("Commitment: KRs are committed unless marked (aspirational).", lines 19 and 36).
- Detection check that fired: dependency-map edge date comparison (AL-06 heuristic) — producer delivery date vs. consumer need-by date, a hard inversion.
- Disconfirming checks run: "late date ≠ inversion" — searched Payments' page for any earlier beta/preview milestone that could satisfy Growth's integration: none stated, the page names only the GA date, and Growth's note names no milestone qualifier, so the tightest quotable reading is GA-to-need-by and the inversion stands. Quarter-boundary check: both dates fall inside Q3 2026, so the inversion is internal to the cycle, not a period artifact.
- Inference labels: none — all load-bearing text quoted (dates, dependency, and commitment convention are each verbatim from the pages).
- Verdict: CONFIRMED (every quote re-fetched and matched character-for-character against the source file).
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree, within two weeks, either a contract-stable billing API beta by `<date before Aug 15>` or a revised G1.3 launch date and a re-based upgrade target [proposal — placeholder target].

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`input.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`input.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: Payments' lever is added authentication friction at checkout, applied to nearly three times as many transactions as today, while Growth's target requires taking friction out of the same checkout surface; optimizing either KR predictably degrades the other, and neither page mentions the other team. The same friction also pulls against Payments' own "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22).
- Detection check that fired: metric-catalog blocking on the shared checkout surface, then the AL-02 known-tension-pair check (fraud controls vs. acquisition/conversion) — a mechanism-level opposition, not a same-metric one.
- Disconfirming checks run: "shared metric ≠ conflict" — directionality checked, the two metrics are different names on one coupled surface, so the same-metric branch does not apply; searched both pages and the company priorities page for a shared or parent OKR covering both (none — C1 and C3 sit in separate priorities with no reconciliation), and for a documented split of levers or an exemption carve-out (none; Payments' own note says only "Fraud work is our top ask from leadership after the Q2 incident (company priority C3).", line 30). No hedge or guardrail is stated on either side, so the candidate survives.
- Inference labels: the step-up-verification → checkout-friction → conversion mechanism is **analyst inference** — no document in this corpus states the tradeoff.
- Verdict: CONFIRMED (both KR quotes re-fetched and matched character-for-character; the mechanism is labeled inference above and is not presented as quoted fact).
- Severity note: Major by AL-02's mechanism-level default, escalated one level because both KRs are committed under their pages' stated convention (lines 19 and 36) and the collision meets the Critical definition — two teams actively working against each other.
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. within two weeks and agree a shared guardrail pair — a chargeback-rate ceiling plus a checkout-conversion floor — with step-up coverage staged against it rather than ramped flat to 90% [proposal — placeholder target].

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (`input.md` › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss, distinguished): "Ship checkout & billing API v2 to GA by Sep 26." (`input.md` › Objective P1: Make checkout something customers never think about › line 23) — the only Q3 KR touching billing infrastructure, but it names no financing, lending, or design-partner work and sits under a checkout-experience objective, so it is not coverage of C4.
- Conflict: A dated, named company priority for this quarter has zero contributing objectives or KRs anywhere in the portfolio; the pilot is due Sep 30 and no team has committed a single measurable step toward it.
- Detection check that fired: top-down strategy trace (AL-10 heuristic) — company objective with zero contributing children across the full swept team set.
- Disconfirming checks run: "zero hits ≠ coverage gap" — re-searched all four team pages, their notes, and the Q2 review appendix under the synonyms and program names "capital", "financ", "lend", "design partner", and "invoice-financing"; the sole hit in the entire file is line 13, the priority statement itself. Checked C4's own line for a named owner outside the swept team set — the priorities page names only "Dana W. (CEO)" as page owner (line 8) and assigns C4 to no function, so this is a portfolio hole rather than an ownership note. For contrast, C1, C2 and C3 each resolve to team objectives, so the sweep is not producing false absences.
- Inference labels: none — all load-bearing text quoted; the absence claim states its full search scope and terms above.
- Verdict: CONFIRMED (the C4 text and the near-miss KR were re-fetched and matched character-for-character; the absence search was re-run over the whole corpus).
- Recommended resolution owner: Dana W. (CEO) to assign C4 an owning team and a Q3 objective before the first month-end, or to move the pilot out of the Q3 priority list; whichever team takes it needs a design-partner-count KR (0 → 3) dated ahead of Sep 30 [proposal — placeholder target].

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`input.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Two teams book Platform's Q3 capacity — one for PCI-scoped provisioning in July, one for a streaming pipeline migration — against a page that declares the quarter already fully committed to two other workstreams and is turning non-critical infra work away until Q4. Nobody has done this arithmetic: neither claimant's page acknowledges Platform's hold, and Platform's page acknowledges neither claimant. Combined committed demand exceeds a declared supply of zero spare capacity, and both dependent KRs (P1.2, D1.1) are committed.
- Detection check that fired: dependency-map resource-node fan-in (AL-07 heuristic) — resource mentions grouped by owner put two claimants on Platform in the same quarter, then the owner's page was checked for declared supply and yielded the fully-committed statement. Classified at the resource node, not edge-by-edge: Payments' ask is the owner's capacity itself (provisioning), so that edge folds into this aggregate entirely and is not filed as a separate AL-01; the capacity arithmetic is reported once, here.
- Disconfirming checks run: "plural demand ≠ contention" — searched Platform's page and notes for a capacity or allocation table, a scheduled slot, or any assignment covering either claimant: none exists, and the only capacity statement present is the hold quoted above, so the allocation is not living outside the OKR pages. Confirmed both claims fall in the same quarter (all pages are titled Q3 2026) and name the same resource (Platform / "the infra level" — Platform is the only infrastructure team in scope and no similarly-named pod appears in the corpus). Nothing falsifies or partially allocates the demand.
- Inference labels: resolving Data's "the infra level" to the Platform team is **analyst inference** (Data names a level, not a team); every other link is quoted.
- Verdict: CONFIRMED (all three quotes re-fetched and matched character-for-character; the one inferred resolution is labeled above).
- Recommended resolution owner: Elena R. (Platform) to publish, within two weeks, either a Q3 allocation naming the PCI-scoped provisioning and the pipeline migration with dates, or a written decline — so Payments and Data can re-plan P1.2 and D1.1 against a real answer rather than a standup recollection.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Data evidence (the dependent KR): "Migrate 100% of product events to unified event schema v2." (`input.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (nearest miss, distinguished): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input.md` › Objective PL2: Earn enterprise trust › line 65) — the closest Platform text to the ask, and it points the other way: it neither names the pipeline nor reserves room for it.
- Conflict: The streaming pipeline migration is a distinct deliverable — a project Platform would have to plan and build, not merely capacity or access it grants — and it appears nowhere in Platform's objectives, KRs, or notes, while Data's committed D1.1 rests on it. Data has sized only "our part", so the larger half of the work has no owner who knows about it.
- Detection check that fired: dependency-map edge acknowledgment (AL-01 heuristic) — the deliverable named in the consumer's dependency phrase was searched for on the producer's side and produced no hit. Filed in addition to §4 AL-07 because this edge names a distinct deliverable rather than a pure capacity ask; the capacity arithmetic itself is reported only under AL-07, which this finding cross-references.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched the whole Platform section (lines 52–66: objectives, KRs and notes) for "pipeline", "stream", "schema", "event", "data" and "provision": zero hits, so there is no partially matching item and no scheduled epic in the corpus to downgrade against. No Jira or backlog source was available in this run, which is recorded as a limit on the absence claim rather than treated as coverage.
- Inference labels: resolving "the infra level" to the Platform team is **analyst inference**; the deliverable, the dependence, and the absence are quoted or searched.
- Verdict: CONFIRMED (both Data quotes and the Platform near-miss re-fetched and matched character-for-character; the absence search was re-run over the Platform section).
- Recommended resolution owner: Jonas K. (Data) to take the streaming pipeline migration to Elena R. (Platform) before the quarter's first check-in and get it either scheduled with a date or explicitly declined, so D1.1 can be re-scoped rather than silently missed.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`input.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Data evidence (the ownership claim): "Own onboarding personalization end-to-end" (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 78)
- Conflict: Two teams carry the same metric on the same population for the same quarter with incompatible targets — 40% and 35% — and no division of labor: Data claims onboarding "end-to-end" while Growth's entire first objective is the first-week experience. Whichever number lands, one team's KR is wrong, and nobody is accountable for the metric as a whole.
- Detection check that fired: pairwise check blocked on canonical metric + population (AL-03 heuristic) — "new-user activation rate", new signups, Q3 2026 — the only cluster in the metric catalog with two claimant teams.
- Disconfirming checks run: "similar objectives ≠ duplication" — searched both pages, including their notes, for any cross-reference, shared epic, joint owner or lane split: Growth's note names only Payments ("Marcus synced with Priya in June"), Data's note names only infra, and neither page mentions the other team; searched the company priorities page for a parent objective assigning lanes: none. Checked for different populations, surfaces, segments or geographies that would make this legitimate division of labor: Data states no population at all, so there is no disambiguating text to quote and the finding stands. Cross-reference **AL-08 Terminology collision** (secondary, per the one-finding-one-failure-mode rule): Growth defines the metric in-line as "(first invoice sent within 7 days)" while Data's page defines it nowhere, so the two targets are not even known to be measuring the same thing — this corrupts the comparison but is a consequence of the same situation, not a separate one.
- Inference labels: none — all load-bearing text quoted; the definition asymmetry is quoted on Growth's side and searched-and-absent on Data's.
- Verdict: CONFIRMED (all three quotes re-fetched and matched character-for-character; a corpus-wide search for "activation" returns exactly these two KR lines).
- Recommended resolution owner: VP Product to assign one accountable team for new-user activation and one shared definition and target before the quarter's first check-in, with the other team's KR restated as a contributing lever (Data's personalization surface, Growth's funnel) rather than a second owner of the same number.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (`input.md` › Objective D1: One trustworthy source of truth › line 73)
- Data evidence (capacity claim): "we've sized our part at 3 engineer-months" (`input.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Company evidence: "Grow self-serve revenue", "Become enterprise-ready", "Cut fraud losses", "C4 — Launch Brightledger Capital" (`input.md` › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent, its KR metrics (event-schema migration coverage, critical-dashboard latency, data quality) are none of the four company metrics nor documented drivers of them, and no priority mentions data platform, schema, or reporting work. Half of Data's objective set therefore serves nothing the company has declared for Q3 — while C4 sits unstaffed (see §4 AL-10).
- Detection check that fired: strategy-trace leaf with no parent (AL-04 heuristic) — the three-way check returned zero of three.
- Disconfirming checks run: "no parent link ≠ orphan" — (a) explicit parent link: searched Data's page and notes, none stated, unlike Payments which does cite "(company priority C3)" (line 30); (b) metric linkage: compared D1's three KR metrics against C1's ARR, C2's SOC 2 and reliability, C3's chargeback rate and C4's pilot — no match, and no driver relationship is stated anywhere in the corpus; (c) strategy-page mention: searched the priorities page for "data", "platform" and "developer" — no hits. Checked Data's page for a self-justification or an exploratory charter that could downgrade or kill the finding: none present.
- Inference labels: none — all load-bearing text quoted; the absence claims state their searches above.
- Verdict: CONFIRMED (all quotes re-fetched and matched character-for-character).
- Severity note: held at AL-04's Minor default — the capacity claim quoted above sizes the work but never states it as a fraction of the team, and Data's team size appears nowhere in the corpus, so the "large stated fraction of team capacity" condition for Major is not met; the objective carries no commitment label either (the page's convention labels KRs, not objectives), so the committed-marking escalation does not apply.
- Recommended resolution owner: Jonas K. (Data) to state D1's parent priority explicitly, or to have Dana W. (CEO) confirm data-platform work as a standing enabler outside the Q3 priority list, before the quarter's first check-in.

## 5. Prioritized action list

1. Convene Payments and Growth to agree a shared fraud-vs-conversion guardrail pair and stage step-up coverage against it — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
2. Re-sequence the billing API dependency by agreeing either a contract-stable beta before Aug 15 or a revised G1.3 date — owner: Priya N. with Marcus T. (resolves §4 AL-06 Timeline mismatch).
3. Assign company priority C4 an owning team with a dated design-partner KR, or remove it from the Q3 list — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
4. Replace Platform's developer-satisfaction KR with an incident-recovery metric that serves PL1 and has a named source — owner: Elena R. (resolves §3 AP-09 Metric Nobody Can Measure — Platform and §3 AP-12 Orphan KR — Platform).
5. Replace Data's data-quality KR with a countable validation pass rate produced by a named job — owner: Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure — Data).
6. Publish a Q3 infra allocation or an explicit decline covering the PCI-scoped provisioning and the streaming pipeline migration — owner: Elena R. (resolves §4 AL-07 Resource contention and §4 AL-01 Unacknowledged dependency).
7. Assign one accountable team, one definition and one target for new-user activation — owner: VP Product (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Reset the uptime KR against the quoted 99.95% trailing baseline and move the standing reliability duty out of the OKR set — owner: Elena R. (resolves §3 AP-06 Sandbagged Target and §3 AP-10 BAU Dressed as OKR).
9. Add a stated baseline to every target that lacks one and swap the blog-pageview KR for a signup-attributed metric — owner: Marcus T. with Jonas K. (resolves §3 AP-04 KR Without Baseline for Growth and Data, and §3 AP-03 Vanity Metric — Growth).
10. Convert the SOC 2 audit and API v2 milestones into graded KRs with countable mid-quarter progress — owner: Elena R. with Priya N. (resolves §3 AP-02 Binary KR with No Gradient and §3 AP-01 Task Masquerading as KR).

## 6. Suggested single-team re-runs

All four teams qualify under §6's criteria; they are listed in order of need — Platform and Data first, where the trigger is a Critical goodness defect in the team's own OKRs, then Growth and Payments, whose trigger is a shared Critical alignment risk.

- **Platform** (roll-up C (2.3); qualifies on Critical §3 AP-09 Metric Nobody Can Measure, alongside AP-06, AP-02, AP-12 and AP-10 and inbound §4 AL-07 / §4 AL-01): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `input.md` › section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3), owner Elena R.; strategy doc: the same file's 'Company Q3 2026 priorities' section (Confluence page 88101, CO-PRIO-Q3); prior-period baselines in the same file's 'Appendix — Q2 2026 business review (extracts)' (page 88104)."
- **Data** (roll-up C (2.2); qualifies on Critical §3 AP-09 Metric Nobody Can Measure, alongside AP-01 and AP-04 and §4 AL-01 / §4 AL-03 / §4 AL-04): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `input.md` › section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3), owner Jonas K.; strategy doc: the same file's 'Company Q3 2026 priorities' section (Confluence page 88101, CO-PRIO-Q3); prior-period baselines in the same file's 'Appendix — Q2 2026 business review (extracts)' (page 88104)."
- **Growth** (roll-up B (2.8), above the needs-rework threshold; qualifies on Critical §4 AL-02 Conflicting metrics / adversarial incentives and Critical §4 AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `input.md` › section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3), owner Marcus T.; strategy doc: the same file's 'Company Q3 2026 priorities' section (Confluence page 88101, CO-PRIO-Q3); prior-period baselines in the same file's 'Appendix — Q2 2026 business review (extracts)' (page 88104)."
- **Payments** (roll-up B (3.1), above the needs-rework threshold; qualifies on Critical §4 AL-02 Conflicting metrics / adversarial incentives and Critical §4 AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `input.md` › section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3), owner Priya N.; strategy doc: the same file's 'Company Q3 2026 priorities' section (Confluence page 88101, CO-PRIO-Q3); prior-period baselines in the same file's 'Appendix — Q2 2026 business review (extracts)' (page 88104)."
