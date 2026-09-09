# Brightledger — Q3 2026 OKR Portfolio Review

*Mode: portfolio (4 teams — Payments, Growth, Platform, Data). Period: Q3 2026. Strategy source: "Company Q3 2026 priorities" (C1–C4) in the same file.*
*Corpus (single source): `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture1-portfolio/input/sample-portfolio.md`. Source refs below abbreviate it as `sample-portfolio.md`; line numbers refer to that file.*

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 10 Major, 0 Minor findings. No team's OKR set is trustworthy as written.
The portfolio's worst alignment risk is **AL-02 Conflicting metrics / adversarial incentives** (Payments ↔ Growth): Payments commits to step-up verification on 90% of transactions while Growth commits to a +10pt lift in checkout conversion on the same surface — neither page mentions the other team.
Two further Critical alignment failures: **AL-06 Timeline mismatch** — Growth's committed Aug 15 upgrade launch needs a billing API that Payments GAs on Sep 26; and **AL-10 Strategy coverage gap** — company priority C4 (Brightledger Capital, due Sep 30) has zero coverage in any of the four teams' OKRs.
Platform is the load-bearing team nobody booked: Payments and Data both assume its infra capacity in a quarter Platform declares "fully committed" (**AL-07 Resource contention**), and Data's streaming-pipeline dependency appears nowhere in Platform's plans (**AL-01 Unacknowledged dependency**).
The most common goodness anti-pattern is **AP-04 KR Without Baseline** — three KRs across three teams (Growth, Platform, Data) state a target with no starting point. Two KRs are Critical because no system of record exists for them at all (**AP-09 Metric Nobody Can Measure**).
Recommended first action: convene Payments + Growth on a joint fraud/conversion guardrail before mid-quarter, and get an owner named for C4 in the same week.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Data | 2 | 2 | 3 | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 3 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.18) · Growth C (2.63) · Payments B (3.14).

- Platform: K1=2, K5=2 — developer-satisfaction and SOC 2 KRs name no metric and no source.
- Data: K1=1, K5=1 — "Significantly improve data quality" states no metric and no system.
- Growth: K1=2 — trial-to-paid and blog-pageview KRs state targets with no baseline.
- Payments: K1=2 — the API v2 GA KR is a milestone with nothing countable.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no "internal developer satisfaction score" instrument exists anywhere in the corpus — searched all four team pages, the company priorities page, and the Q2 business-review appendix for `satisfaction`, `survey`, `score`, `eNPS` and any named tool; the only hit is this KR itself, and the only named system of record in the whole corpus is Datadog for uptime (line 89). The KR also states no current value, so 8/10 can be judged as neither ambition nor progress.
- Scores affected: K1=1, K5=0, K3=2 (KR capped at 1.0 by the K5=0 rule; PL1 capped at 1.9 by the Critical-anti-pattern rule)
- Suggested rewrite: "KR PL1.3: Developer experience survey (quarterly, n ≥ `<team size>`, run in `<named survey tool>`): satisfaction `<baseline>`/10 → 8/10, with the instrument and question set published before the first run." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56)
- Also: AP-11 Objective as Kitchen Sink
- Why it's a problem: `keep the lights on` is the team's standing operational duty rather than a changed end-state, so the objective is largely achieved by default staffing; and it bundles three disjoint end-states — uptime, cloud cost, and developer satisfaction — whose KRs cluster into unrelated groups.
- Scores affected: O1=1, K7=2
- Suggested rewrite: "PL1: Brightledger serves every transaction at a unit cost the business can scale on — KR: cloud spend per 1,000 transactions $4.10 → $3.20 (sample-portfolio.md line 58)." Move the uptime commitment to a standing health metric outside the OKRs, and split developer experience into its own objective if it is worth a quarter's focus. [proposal]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits below the trailing actual quoted in the same corpus — the KR is already achieved and can be met by letting reliability degrade by 0.05pt, so it encodes no commitment at all.
- Scores affected: K3=1, K1=3
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing 90 days, Datadog SLO monitor) → 99.97%, measured monthly on the same monitor; error budget burn reported weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: "Complete" names a deliverable, not a measurable result, and the KR has no numeric scale — it can only score 0% or 100%, so nobody can tell in August whether the quarter is on track or lost.
- Scores affected: K1=0, K2=1 (KR capped at 1.0 by the K1=0 rule; PL2 capped at 2.4 by the two-Major rule)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence collection `<0>`/`<N>` controls evidenced → `<N>`/`<N>` by Sep 12, auditor's report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" is never defined, and no quality score, test suite, or dashboard appears anywhere in the corpus — searched all four team pages, the company priorities page, and the Q2 appendix for `quality`, `table` and any named tool; the only hit is this KR — while `significantly` sets no threshold, so the KR can never be honestly scored either way.
- Scores affected: K1=0, K5=0, K3=2 (KR capped at 1.0; D1 capped at 1.9 by the Critical-anti-pattern rule)
- Suggested rewrite: "KR D1.3: Core-table freshness and completeness checks passing `<baseline>`% → `<target>`% of daily runs across the `<N>` core tables, measured by `<named data-quality tool>`; zero Sev-1 data incidents on those tables." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no current trial-to-paid value is stated here or retrievable anywhere in the corpus — searched the Growth page, the other three team pages, the company priorities page, and the Q2 business-review appendix, which reports only uptime, chargeback/step-up and qualified signups (lines 89–91). Without a starting point the 22% is unjudgeable as ambition and unreadable as progress.
- Scores affected: K1=2, K3=2 (calibration unverifiable)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, cohort-dated by trial start, weekly from `<named analytics dashboard>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing and paid distribution regardless of whether the funnel becomes "a machine", so the KR can be hit while qualified signups and checkout conversion stand still; and with no current pageview figure anywhere in the corpus (searched all four team pages, company priorities, and the Q2 appendix) the 50,000 cannot be read as ambition.
- Scores affected: K2=2, K1=2, K3=2, K7=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed at first touch in `<named analytics dashboard>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: shipping to GA is a delivery milestone with no baseline→target pair — the KR succeeds on Sep 26 even if no traffic ever moves to v2 and no customer notices, which is the opposite of the objective's stated end-state.
- Scores affected: K1=0, K2=1 (KR capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing requests served by API v2 (0% → `<target>`%) with v2 error rate ≤ `<threshold>`% and no regression in the 91.2% → 95% checkout success rate (sample-portfolio.md line 22)." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface; taking coverage from 35% to 90% of transactions predictably suppresses the completion metric Growth has committed to lifting by 10 points. Neither page names the other team, and no shared guardrail exists.
- Detection check that fired: AL-02 surface-lever key — both KRs sit on the checkout surface, Payments' stated lever (step-up verification coverage) is a friction/risk control there, and Growth targets that surface's conversion metric. The metric-identity key generated nothing (the two KRs share no canonical metric name).
- Disconfirming checks run: shared or parent OKR covering both — none found (searched both team pages and the company priorities page; C1 and C3 are separate priorities pursued by separate teams); documented split of levers — none found; directionality — confirmed opposed at mechanism level. Separately, the lookalike pair "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) vs. Growth's checkout conversion was generated and correctly killed — different definitions and populations, same direction, no control lever on either side; per the taxonomy that kill is per-candidate and does not touch this one.
- Inference labels: the verification-friction → checkout-conversion mechanism is **analyst inference** — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product convenes Priya N. (Payments) and Marcus T. (Growth) to set a paired guardrail — a chargeback ceiling plus a checkout-conversion floor, with step-up applied risk-based rather than at flat coverage — before mid-quarter.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41), with the dependency stated as "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date (Aug 15) precedes the producer's delivery date (Sep 26) by roughly six weeks, with no integration margin — Growth's committed launch is impossible as sequenced, and the 300 upgrades that depend on it have only the quarter's final four days to accrue.
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer's delivery date vs. consumer's need-by date, hard inversion.
- Disconfirming checks run: `late date ≠ inversion` — searched both pages for an earlier milestone (beta, preview, partial availability) that could satisfy Growth's Aug 15 launch; the corpus states only the Sep 26 GA date, so no interleaving reading is available. Commitment levels — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 19, 36) and neither KR carries an aspirational marker, so both are committed. The quoted June sync was checked as a possible resolution and contains no date commitment ("should be fine"), so it does not weaken the finding.
- Inference labels: none — all load-bearing text quoted; the "new billing API" ↔ "checkout & billing API v2" identification comes from Growth's own note naming the API it will use.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 41, 48 and 23)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree in writing within one week either a dated partial/beta interface for the upgrade flow before Aug 15, or a re-dated G1.3 launch with a revised upgrade count.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ all four teams
- Company evidence: "C4 — Launch Brightledger Capital" — "invoice-financing pilot live with 3 design partners by Sep 30." (sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Portfolio evidence (the absence): the closest thing to a financing-adjacent commitment in any team's OKRs is Payments' "Ship checkout & billing API v2 to GA by Sep 26." (sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23), which is a payments API milestone and names neither invoice financing nor design partners.
- Conflict: a dated company priority with a hard Sep 30 deadline has no objective, KR, or note in any of the four teams in scope — the portfolio has a hole where a quarter of the company's stated agenda should be.
- Detection check that fired: AL-10 top-down strategy trace — company objectives with zero contributing children. C1, C2 and C3 all resolve to team objectives (C1 → Growth G1/G2, C2 → Platform PL1/PL2, C3 → Payments P2, which cites it explicitly); C4 resolves to nothing.
- Disconfirming checks run: `zero hits ≠ coverage gap` — re-searched all four team pages, the company priorities page and the Q2 appendix under synonyms and program names (`Capital`, `invoice financing`, `financing`, `lending`, `underwriting`, `design partner`); the only occurrence in the entire corpus is line 13 itself. The company priorities page was also checked for a named owner outside the swept team set — the page names only "Dana W. (CEO)" as its own owner (line 8) and assigns C4 to no function, so this is a portfolio hole rather than an ownership note.
- Inference labels: none — all load-bearing text quoted; the absence claim states its full search scope above.
- Verdict: CONFIRMED (the C4 text re-verified character-for-character against line 13; the absence search re-run across the whole file)
- Recommended resolution owner: Dana W. (CEO) to name an accountable team and owner for C4 within one week, or to strike it from the Q3 priorities — a Sep 30 pilot with no team behind it on July 5 is already at risk.

### [Major] AL-07 Resource contention: Payments ↔ Data ↔ Platform
- Payments evidence (claimant): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work." and "Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams book Platform's Q3 infra capacity for work that gates their own committed KRs, in a quarter Platform has declared fully committed elsewhere and closed to non-critical infra requests. Combined demand exceeds the stated supply and nobody has done the arithmetic; Payments' provisioning ask is a pure capacity claim and folds into this finding entirely.
- Detection check that fired: AL-07 resource-node fan-in — grouping resource mentions by owner puts two distinct claimants on Platform in the same quarter, and the owner's own page, checked for declared supply, yields an explicit fully-committed statement.
- Disconfirming checks run: `plural demand ≠ contention` — searched Platform's OKR page (lines 52–66) for any allocation, scheduled work item, or capacity table covering either claimant; none exists, and no Jira/backlog source is available in this corpus, which is recorded as a limit on the search rather than as evidence of allocation. Same-quarter check — all three pages are Q3 2026. Same-resource check — both claims name infra provisioning by the Platform/infra function, not similarly-named groups.
- Inference labels: Data's phrase "at the infra level" resolving to the Platform team is **analyst inference** — the note does not name Platform, and Platform is the only infra-owning team in scope.
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against lines 30, 82 and 65)
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 allocation for infra asks and state explicitly which of the two claims she will not serve, so Payments and Data can re-plan; escalate to the CEO if both must be served.

### [Major] AL-01 Unacknowledged dependency: Data → Platform
- Data evidence: "Migrate 100% of product events to unified event schema v2." (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74), with the dependency stated as "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (the near-miss): Platform's OKRs commit only to "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 58) and "Complete the SOC 2 Type II audit." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63) — neither is the streaming pipeline migration, and Platform adds "Holding all non-critical infra requests until Q4." (sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: the streaming pipeline migration is a named deliverable — a project Platform would have to plan and staff, not merely capacity to allocate — and it appears nowhere in Platform's objectives, KRs, or notes, while Data's committed schema-v2 KR rides on it. Data has also sized only "our part", so nobody has sized the pipeline itself.
- Detection check that fired: AL-01 edge acknowledgment on the dependency map — the deliverable named on the consumer's side has no hit on the producer's side. Cross-reference: this edge sits inside the §4 AL-07 Resource contention above; the capacity arithmetic is reported once, there, and this finding covers only the missing deliverable.
- Disconfirming checks run: `missing mention ≠ unacknowledged` — searched the whole corpus for `pipeline`, `streaming`, `schema` and `event`: the only hits are Data's own lines 74 and 82, with zero occurrences anywhere in Platform's section (lines 52–66). No Jira or backlog source is connected for this run, so an unscheduled backlog item cannot be ruled out; that limit is why the severity stays at the default rather than escalating.
- Inference labels: Data's "the infra level" resolving to the Platform team is **analyst inference** (Platform is the only infra-owning team in scope).
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 74, 82, 58, 63 and 65)
- Recommended resolution owner: Jonas K. (Data) and Elena R. (Platform) to size and schedule the streaming pipeline migration jointly — or to agree it will not happen in Q3, in which case D1.1's "100%" needs re-scoping before the quarter's midpoint.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to moving the same named metric on the same population in the same quarter, to inconsistent targets (40% vs. 35%), with no cross-reference, shared owner, or division of labour between them — and Data's objective claims the surface outright ("Own onboarding personalization end-to-end", line 78) while Growth's onboarding KR sits inside its own objective. When both land, nobody can say who was accountable or which number was the goal.
- Detection check that fired: AL-03 clustering by target metric plus target population/surface — "new-user activation rate", new signups, Q3 2026 — followed by the mutual-reference check, which found none. Secondary, cross-referenced rather than double-counted: the same pair is an AL-08 Terminology collision risk — Growth defines the metric as "first invoice sent within 7 days" (line 40) and Data states no definition at all, so the 40% and 35% may not even be the same measurement.
- Disconfirming checks run: `similar objectives ≠ duplication` — searched both team pages for cross-references, a shared epic, a joint owner, or an explicit lane split (e.g. by surface, segment or geography); the only cross-team reference on Growth's page is to Payments ("Marcus synced with Priya in June", line 48) and Data's notes mention only infra (line 82). No parent objective assigning lanes exists on the company priorities page. Populations were checked for a legitimate split and none is stated — both KRs address new users generally.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 40 and 80)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to agree one activation definition, one target and one accountable team this month; the other team's KR becomes a stated contribution, not a second target.

### [Major] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73), whose stated capacity claim is "we've sized our part at 3 engineer-months" (sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Company evidence: the four Q3 priorities are "C1 — Grow self-serve revenue", "C2 — Become enterprise-ready", "C3 — Cut fraud losses" and "C4 — Launch Brightledger Capital" (sample-portfolio.md › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 consumes a stated multi-engineer-month commitment for a quarter but serves no declared company priority — its KRs (schema migration, dashboard latency, data quality) move none of the company-level metrics, and no priority names data infrastructure as a dependency.
- Detection check that fired: AL-04 three-way check, all three negative — (a) no explicit parent link or label on D1 (contrast Payments, whose notes cite "company priority C3", line 30); (b) no KR metric is a company-level metric or a documented driver of one — C1's metric is "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." (line 10), C2's is "complete SOC 2 Type II and hold enterprise-grade reliability." (line 11), C3's is "bring chargeback rate under 0.5% after the Q2 incident." (line 12); (c) no mention of the data platform, event schema, or dashboards anywhere on the company priorities page.
- Disconfirming checks run: `no parent link ≠ orphan` — ran the full three-way check above before flagging. Searched the Data page for a self-justification or charter that would downgrade or kill the finding (e.g. an exploratory-work mandate or a stated future platform strategy); the notes contain only the sizing and infra-dependency statement quoted above. D2, by contrast, does trace to C1 via activation, so this finding is scoped to D1 alone.
- Inference labels: none — all load-bearing text quoted; no inferred parent link was credited to the objective, per the taxonomy's rule that inferred parents count against the finding.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 73, 82 and 10–13)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to either state D1's parent priority explicitly and the metric it moves, or re-cut D1 as the enabling layer under a named priority, before mid-quarter re-planning.

## 5. Prioritized action list

1. Convene Payments and Growth to set a paired fraud/conversion guardrail and a risk-based step-up policy — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
2. Re-sequence the self-serve upgrade launch against a dated billing-API interface, or re-date G1.3 — owner: Priya N. with Marcus T. (resolves §4 AL-06 Timeline mismatch).
3. Assign an accountable team and owner to company priority C4, or strike it from Q3 — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
4. Publish a Q3 infra allocation naming which of the Payments and Data claims Platform will serve — owner: Elena R. (resolves §4 AL-07 Resource contention).
5. Size and schedule the streaming pipeline migration jointly, or re-scope D1.1's 100% target — owner: Elena R. with Jonas K. (resolves §4 AL-01 Unacknowledged dependency).
6. Settle one activation definition, one target and one accountable team across Growth and Data — owner: Marcus T. with Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
7. State D1's parent priority and the company metric it moves, or re-cut the objective — owner: Jonas K. (resolves §4 AL-04 Orphan objective).
8. Replace the two unmeasurable KRs with instrumented ones before any mid-quarter check-in — owner: Elena R. (PL1.3) and Jonas K. (D1.3) (resolves §3 AP-09 Metric Nobody Can Measure, both instances).
9. Re-baseline the uptime KR on the quoted 99.95% trailing actual and move the standing duty out of the OKR set — owner: Elena R. (resolves §3 AP-06 Sandbagged Target, AP-10 BAU Dressed as OKR).
10. Add baselines and adoption/outcome measures to the milestone and baseline-free KRs — owner: each team lead for P1.2, PL2.2, G1.1, G2.3 (resolves §3 AP-01 Task Masquerading as KR, AP-04 KR Without Baseline, AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure, plus inbound AL-07 Resource contention and AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Data** (roll-up C (2.18); Critical AP-09 Metric Nobody Can Measure, plus AL-01, AL-03 and AL-04): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Growth** (roll-up C (2.63); Critical AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Payments** (roll-up B (3.14), above the needs-rework threshold; qualifies solely on Critical AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
