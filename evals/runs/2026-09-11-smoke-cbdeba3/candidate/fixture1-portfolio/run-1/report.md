# Brightledger — Q3 2026 Portfolio OKR Review

**Scope confirmed at intake (portfolio mode — 4 teams):** Payments, Growth, Platform, Data · Period: Q3 2026 (as stated by the source file) · Source: `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` (single canonical corpus; no Atlassian connection available) · Strategy source: the file's "Company Q3 2026 priorities" section (C1–C4).

---

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings.
The portfolio's biggest threat is AL-02 Conflicting metrics / adversarial incentives: Payments is driving step-up verification coverage to 90% of transactions while Growth commits to a 10-point rise in checkout conversion on the same surface, and neither page mentions the other team.
Close behind: Growth's committed Aug 15 upgrade launch depends on a billing API whose only stated GA date is Sep 26 (AL-06 Timeline mismatch), and company priority C4 (Brightledger Capital) has no contributing objective anywhere in the portfolio (AL-10 Strategy coverage gap).
Platform is the single point of contention — two teams' plans assume its capacity in a quarter its own page declares fully committed (AL-07 Resource contention).
The most common quality issue is AP-04 KR Without Baseline (3 KRs across Growth and Platform state a target with no starting point); two KRs — one on Platform, one on Data — are Critical AP-09 Metric Nobody Can Measure.
Recommended first action: a joint Payments/Growth session on the checkout funnel, before the fraud rollout starts.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Data | 3 | 3 | 3 | 1 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |
| Growth | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.38) · Growth C (2.64) · Payments B (3.10).

- Platform: K5=2 — developer-satisfaction KR names no instrument; uptime target sits below quoted 99.95% baseline.
- Data: O4=1 — objective D1 traces to no company priority, and one KR is unmeasurable.
- Growth: O2=2 — both objectives rest on metaphors; two KRs state targets with no baseline.
- Payments: K1=2 — the API v2 KR is a delivery date with no metric or baseline.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no "internal developer satisfaction score" instrument exists anywhere in the corpus — searched the Platform page (lines 52–65), all three other team pages, the company priorities page, and the Q2 business review appendix (lines 86–91, whose only named instrument is "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)."); the KR can never be honestly scored, and with no current value the 8/10 is also unjudgeable as ambition.
- Scores affected: K5=0, K1=1, K3=2, K7=2 (PL1 set)
- Suggested rewrite: "KR PL1.3: Internal developer survey (`<survey instrument>`, n ≥ `<respondents>`, run in month 1 and month 3): satisfaction `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: nothing countable is stated — no metric, no baseline, no target, and no system of record; searched the Data page (lines 69–82), the other three team pages, and the Q2 appendix (lines 86–91) for a data-quality score or dashboard, and the only named instrument is the "weekly exec-dashboard reconciliation check" in KR D1.1, which counts cross-source discrepancies rather than table quality. "Significantly" cannot be scored at quarter end.
- Scores affected: K1=0, K5=0, K3=2, K2=2
- Suggested rewrite: "KR D1.3: Rows failing the `<data-quality suite>` checks across the `<N>` core tables `<baseline>`% → `<target>`%, evaluated daily." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: the KR carries neither a baseline→target pair nor a result measure anyone outside the team moves — it is satisfied the moment the team declares GA, even if no traffic, no customer, and no latency or success-rate number changes. Its only failure mode is lateness.
- Scores affected: K1=0, K2=1, K3=2
- Suggested rewrite: "KR P1.2: Production checkout requests served by API v2 0% → `<target>`% by Sep 26, with v2 error rate ≤ `<threshold>`%." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no current trial-to-paid value is stated and none is retrievable — searched the Growth page (lines 34–48), the company priorities page (lines 7–13), and the Q2 business review appendix (lines 86–91), which reports only uptime, chargeback rate, step-up coverage, and qualified signups. Without a starting point, 22% is unjudgeable as ambition and unscorable as progress.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, monthly signup cohort, from `<funnel dashboard>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with spend and syndication without indicating that the funnel converts anything, which is what the objective claims; and with no current pageview figure stated anywhere in the corpus (searched the Growth page and the Q2 appendix), the 50,000 could already be met.
- Scores affected: K2=2, K1=2, K3=2, K7=2 (G2 set)
- Suggested rewrite: "KR G2.3 (aspirational): Qualified signups attributed to blog content `<baseline>`/mo → `<target>`/mo, per `<analytics tool>` first-touch attribution." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (prior actual): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits *below* the quoted trailing-90-day actual, so the KR is achieved by letting reliability degrade — it encodes permission to regress rather than ambition, and it is the reliability half of company priority C2.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, measured monthly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a completion verb with no metric and no baseline→target pair, so it measures the team's own delivery rather than a result; and because it is done/not-done, mid-quarter scoring can only read 0% or 100% — the team cannot show or steer progress on the company's C2 commitment until the last day.
- Scores affected: K1=0, K2=1, K3=2, K6=3 (PL2 set)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence items closed 0/`<total>` → `<total>`/`<total>`, auditor's report received by `<date>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and Payments is committing to apply it to nearly three times as many transactions (35% → 90%) in the same quarter Growth commits to a 10-point rise in conversion on that surface; neither page mentions the other team's target.
- Detection check that fired: AL-02 surface-lever key — both KRs sit on the checkout surface, Payments' stated lever (step-up verification coverage) is a friction control there, and Growth targets that surface's conversion metric. (The metric-identity key generates nothing here — the names differ.)
- Disconfirming checks run: directionality — the lever and the target are opposed, not aligned; shared or parent OKR covering both — searched both team sections and the company priorities page, none found; documented split of levers (e.g. verification applied only outside the self-serve segment) — searched both teams' notes lines 30 and 48, none found. Separately, the lookalike pair "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) vs. this same Growth KR was generated and killed — different definitions and populations, same direction, no control lever — which does not affect this candidate.
- Inference labels: the verification-friction → conversion-drop mechanism is analyst inference; no Brightledger document states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T.; agree a shared guardrail pair — a chargeback ceiling plus a self-serve checkout-conversion floor — and a verification-targeting rule before the step-up rollout begins.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence (dependency): "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date (Aug 15) precedes the producer's only stated delivery date (Sep 26) by six weeks — a hard inversion, on KRs both pages label committed ("Commitment: KRs are committed unless marked (aspirational)." lines 19 and 36).
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer delivery date vs. consumer need-by date on the Growth → Payments billing-API edge.
- Disconfirming checks run: `late date ≠ inversion` — searched the Payments section (lines 17–30) for any earlier milestone (beta, private preview, partial availability) that would suffice for Growth's integration; the only dated statement is the Sep 26 GA, and Growth's note names no milestone short of "the new billing API". Soft-date reading — neither date is hedged. Prior-coordination check — Growth's "Marcus synced with Priya in June, should be fine." is quoted above; it records a conversation, not a date, and does not reconcile the two.
- Inference labels: none — all load-bearing text quoted (the need-by date, the dependency statement, and the delivery date each come from the corpus verbatim).
- Verdict: CONFIRMED (all three quotes re-verified against lines 41, 48 and 23)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree within two weeks either an earlier partial-availability milestone for the billing API that covers upgrades, or a revised G1.3 launch date; whichever moves, the committed label on the other side must be restated.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ portfolio (all four teams)
- Company evidence: "C4 — Launch Brightledger Capital:" … "invoice-financing pilot live with 3 design partners by Sep 30." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Portfolio evidence (nearest miss): "Ship checkout & billing API v2 to GA by Sep 26." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23) — a payments/billing API, not invoice financing; nothing in it serves a financing pilot or a design-partner count.
- Conflict: a dated company priority with a hard Sep 30 deadline has zero contributing objectives or KRs in the portfolio. C1, C2 and C3 each have contributing children (Growth's conversion and signup KRs; Platform's SOC 2 and uptime KRs; Payments' chargeback KR), so the hole is specific to C4.
- Detection check that fired: AL-10 top-down strategy trace — each company objective searched against all four teams' OKRs for contributing children; C4 returned zero.
- Disconfirming checks run: synonym re-search — swept all four team sections (lines 17–82) and both note blocks for `Capital`, `financing`, `invoice financing`, `lending`, `credit`, `design partner`, `pilot`: zero hits. Named-owner check — the C4 line names no owner outside the swept team set, so this is not an ownership note; the priorities page lists only "Dana W. (CEO)" as page owner (line 8). Near-miss check — the closest surface is the billing API above, quoted and distinguished.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (the C4 spans and the near-miss quote re-verified against lines 13 and 23)
- Recommended resolution owner: Dana W. (CEO) to either assign C4 to a team with an objective and KRs this cycle, or record it as deferred — the Sep 30 date leaves no room for a mid-quarter start.

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed Q3 work assumes Platform capacity in a quarter Platform declares fully committed to two other workstreams — combined demand against a declared zero-slack supply, and nobody has done the arithmetic. Payments' ask is provisioning (pure capacity), so it folds into this finding entirely; Data's pipeline migration is a distinct deliverable and additionally carries its own AL-01 finding below, which cross-references this one. The capacity arithmetic is reported here once.
- Detection check that fired: AL-07 resource-node fan-in — grouping every external-resource mention by owner put two claimants (Payments, Data) on the Platform node in the same quarter; checking Platform's page for declared supply returned the fully-committed statement.
- Disconfirming checks run: `plural demand ≠ contention` — checked Platform's own OKRs (lines 52–65) for an allocation covering either claimant: PL1 and PL2 name only cost reduction, uptime, developer satisfaction, pen-test closure and SOC 2; no capacity or allocation table exists in the corpus and no Jira/backlog source is available, so nothing falsifies the finding. Same-quarter check — all three pages are labeled Q3 2026 (lines 17, 52, 69). Same-resource check — both claimants name Platform/infra, not similarly-named pods.
- Inference labels: "the infra level" is read as the Platform team — analyst inference; Data's note does not name Platform explicitly, and Platform is the only infrastructure-owning team in scope.
- Verdict: PLAUSIBLE (all quotes verified verbatim, but the Data → Platform edge rests on the inferred resolution of "the infra level")
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 capacity allocation naming what she will and will not take from Payments and Data, before the end of July — the month Payments' note already assumes the provisioning happens.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Data evidence (dependent KR): "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (nearest match, does not cover it): "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 58) — an infrastructure cost target, not a pipeline migration; delivering it would not migrate any event stream.
- Conflict: Data's committed KR D1.1 requires all product events to run on schema v2, which its own note says rides on a streaming pipeline migration it expects someone else to run — and the streaming pipeline appears nowhere in Platform's objectives or KRs. The producer never planned the work the consumer's number assumes. Cross-reference: the overbooked-quarter half of this situation is the AL-07 Resource contention finding above; this finding is the missing deliverable, not the capacity arithmetic.
- Detection check that fired: AL-01 edge acknowledgment — the dependency phrases "rides on" and "handled at the infra level" were resolved to Platform, then Platform's inventory was searched for the named deliverable and returned nothing.
- Disconfirming checks run: `missing mention ≠ unacknowledged` — searched Platform's full section (lines 52–65) for `streaming`, `pipeline`, `migration`, `schema`, `event`, `data`: zero hits; no Jira or backlog source exists in this corpus, so the usual rescue (work tracked in a backlog rather than the OKRs) cannot be confirmed and is stated as a limitation rather than assumed. Partial-match check — the nearest Platform item is quoted above and distinguished. Deprioritization check — Platform's "Holding all non-critical infra requests until Q4." (line 65) points away from the work, not toward it.
- Inference labels: "the infra level" resolved to the Platform team — analyst inference (Platform is the only infrastructure-owning team in scope).
- Verdict: PLAUSIBLE (all quotes verified verbatim; the owning-team resolution of "the infra level" is inferred)
- Recommended resolution owner: Jonas K. (Data) to take the streaming pipeline migration to Elena R. (Platform) for an explicit accept-or-decline in July; if declined, KR D1.1's "all product events" clause has to be rescoped before the quarter is trusted.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: two teams commit to the same metric, off the same 31% baseline, over the same population and quarter, with different targets (40% vs 35%) — so at 37% both teams can report a different verdict and neither is accountable for the gap. Data's objective claims to "Own onboarding personalization end-to-end" while Growth's first-week objective covers the same surface, with no split of lanes anywhere.
- Detection check that fired: AL-03 clustering by target metric plus target population — "new-user activation rate", identical 31% baseline, same new-user population, same cycle.
- Disconfirming checks run: cross-reference search — read both teams' note blocks (line 48 and line 82) and both full sections for any mention of the other team; Growth's note names only Payments, Data's names only "the infra level", neither names the other. Shared/parent objective assigning lanes — none on the company priorities page (lines 7–13). Population/surface split (e.g. Growth owns web, Data owns in-product personalization) — searched both objectives and all their KRs; asserted nowhere. Definition split — Growth defines activation as "first invoice sent within 7 days" and Data states no definition, so an AL-08 definitional explanation for the different targets cannot be established from the corpus; the shared 31% baseline argues they are the same measure.
- Inference labels: none for the duplication itself — both KRs, both targets and the shared baseline are quoted; that the two measures are identical is supported by the shared baseline rather than assumed.
- Verdict: CONFIRMED (both quotes re-verified against lines 40 and 80)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to name one accountable owner for activation and one target this quarter; the other team keeps a contributing KR phrased as its own lever, not as the shared outcome.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "### Objective D1: One trustworthy source of truth" (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 73)
- Company evidence: "C1 — Grow self-serve revenue:" … "C2 — Become enterprise-ready:" … "C3 — Cut fraud losses:" … "C4 — Launch Brightledger Capital:" (`/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md` › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent, and none of the four company priorities covers internal data trustworthiness; its KR metrics (discrepancy count, dashboard latency) are not company-level metrics and no document names them as drivers of ARR, enterprise readiness, chargebacks, or the financing pilot. Real work, but the portfolio cannot say what it buys this quarter.
- Detection check that fired: AL-04 three-way check — (a) explicit parent link: none in the Data section; (b) KR metric is a company metric or documented driver: no, checked against C1–C4; (c) mention in the strategy page: none.
- Disconfirming checks run: `no parent link ≠ orphan` — re-ran all three legs before flagging and searched the Data page for its own justification; the only rationale-like text is the sizing note at line 82, which explains cost, not strategic contribution. Exploratory-charter check — no charter text exists in the corpus for any team. Capacity-scale check — the one stated capacity figure, "we've sized our part at 3 engineer-months" (line 82), is scoped to the schema v2 part of one KR and does not establish a large fraction of team capacity, which keeps this at Minor rather than Major.
- Inference labels: none — all load-bearing text quoted; no parent was inferred (an inferred parent would count against the finding, not for it).
- Verdict: CONFIRMED (the objective heading and the four priority spans re-verified against lines 73 and 10–13)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to state D1's parent priority explicitly, or to record it as a platform-health investment held outside the OKR set.

## 5. Prioritized action list

1. Convene Payments and Growth on the checkout funnel and set a joint guardrail pair (chargeback ceiling + self-serve conversion floor) before the step-up rollout — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
2. Reconcile the billing-API dates — either an earlier partial-availability milestone or a revised G1.3 launch date — owner: Priya N. with Marcus T. (resolves §4 AL-06 Timeline mismatch).
3. Assign company priority C4 to a team with an objective and KRs this cycle, or record it as deferred — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
4. Replace the two unscoreable KRs (Platform PL1.3, Data D1.3) with instrumented metrics naming their system of record — owners: Elena R., Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure, both instances).
5. Publish a Q3 Platform capacity allocation naming what Platform will and will not take from Payments and Data, before end of July — owner: Elena R. (resolves §4 AL-07 Resource contention).
6. Get an explicit accept-or-decline from Platform on the streaming pipeline migration, and rescope KR D1.1 if declined — owner: Jonas K. (resolves §4 AL-01 Unacknowledged dependency).
7. Name one accountable owner and one target for new-user activation across Growth and Data — owners: Marcus T. and Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
8. Reset the uptime KR against the quoted 99.95% trailing-90-day actual — owner: Elena R. (resolves §3 AP-06 Sandbagged Target).
9. Rewrite the two delivery-milestone KRs (Payments P1.2, Platform PL2.2) as adoption and closure measures with baselines — owners: Priya N., Elena R. (resolves §3 AP-01 Task Masquerading as KR, both instances, and AP-02 Binary KR with No Gradient).
10. Add a baseline to G1.1 and replace the blog-pageview KR with an attributed-signup measure — owner: Marcus T. (resolves §3 AP-04 KR Without Baseline and AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure, plus AP-06 Sandbagged Target and inbound AL-07 Resource contention / AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Data** (roll-up C (2.38); Critical AP-09 Metric Nobody Can Measure, plus AL-01 Unacknowledged dependency and AL-04 Orphan objective): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Growth** (roll-up C (2.64); qualifies on Critical alignment findings AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
- **Payments** (roll-up B (3.10) — above the needs-rework threshold, but qualifies on Critical alignment findings AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-portfolio/input/sample-portfolio.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 88101, CO-PRIO-Q3)."
