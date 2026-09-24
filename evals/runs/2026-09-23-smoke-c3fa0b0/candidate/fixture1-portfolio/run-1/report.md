## 1. Executive summary

**Verdict: At risk. Brightledger's Q3 2026 portfolio cannot be delivered as written.** This was a portfolio-mode review of 4 teams (Payments, Growth, Platform, Data) from the local export, checked against the Company Q3 2026 priorities (C1–C4). It found 14 findings: 4 Critical, 9 Major and 1 Minor.
The worst alignment risk is AL-07 Resource contention. Payments needs PCI-scoped infra for API v2, which it assumes arrives in July. Data needs a streaming pipeline for schema v2. Both depend on Platform, whose own page says Q3 is fully committed and holds non-critical infra requests until Q4.
That bottleneck feeds AL-06 Timeline mismatch. Growth commits to launch self-serve upgrades by Aug 15 on a billing API that Payments commits to GA only by Sep 26.
Company priority C4 (the Brightledger Capital pilot, due Sep 30) has no team objective contributing to it (AL-10 Strategy coverage gap).
The most common goodness anti-pattern is AP-04 KR Without Baseline, on 3 KRs (Growth G1.1 and G2.3, Platform PL1.3). The only Critical goodness finding is AP-09 Metric Nobody Can Measure on Data's D1.3.
Roll-up grades: Payments B (2.84), Growth C (2.64), Platform C (2.40), Data C (2.34). No team is at the D needs-rework threshold, but every team is part of a Critical finding, so §6 recommends four single-team re-runs.
Recommended first action: Platform, Payments and Data agree how Platform's Q3 infra capacity is allocated, then re-date P1.2 and D1.1 (§5 item 1).

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Data | 2 | 3 | 3 | 1 | 3 | 3 | 2 | 3 | 2 | 2 | 3 |
| Platform | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Data C (2.34) · Platform C (2.40) · Growth C (2.64) · Payments B (2.84).
- Data: O4=1 — D1 traces to no company priority (AL-04 Orphan objective).
- Platform: K3=2 — uptime target sits below the Q2 review's 99.95% trailing figure (AP-06 Sandbagged Target).
- Growth: K1=2 — two KRs set targets with no baseline anywhere (AP-04 KR Without Baseline).
- Payments: K1=2 — API v2 KR is a ship-by-date milestone (AP-01 Task Masquerading as KR).

## 3. Per-team goodness findings

These findings are at screening depth (portfolio mode). There is one block per KR, and any other anti-pattern that applies to the same KR goes on its Also line. Blocks are grouped by team, worst roll-up first, then ordered by severity.

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: The KR never defines data quality, does not list the core tables, and gives no size for the improvement. Nothing in the corpus measures it: quality and tables appear only on this line, and the page's one named instrument, the weekly exec-dashboard reconciliation check, belongs to D1.1. As written, the KR cannot be scored.
- Scores affected: K1=1, K5=0 (per-KR score capped at 1.0; D1 capped at 1.9 by the Critical cap)
- Suggested rewrite: "KR: Share of the `<N>` named core tables passing daily automated data-quality tests (freshness, null rate, uniqueness) in `<data-quality tool>`: `<baseline>`% → `<target>`%." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: The Q2 business review already puts trailing-90-day API uptime at 99.95%, above the KR's 99.9% floor. The KR is therefore met even if uptime falls below its Q2 level, so hitting it shows nothing was held or gained.
- Scores affected: K3=1, K1=3 (the baseline is only available from the Q2 review)
- Suggested rewrite: "KR: API uptime, trailing 90 days per Datadog SLO monitor: 99.95% (the Q2 review figure quoted above) → `<target, at least 99.95>`%." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 59)
- Evidence: "Keep the lights on, cheaper" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 56)
- Also: AP-04 KR Without Baseline
- Why it's a problem: The KR shares no noun with its objective, and nothing on Platform's page links internal developer satisfaction to uptime or cloud spend. Hitting 8/10 would not show that the lights stayed on more cheaply (AP-12). The KR also gives no starting score and names no survey instrument, and neither appears anywhere in the corpus: Platform's section has none, and the Q2 review's only Platform figure is uptime. So 8/10 cannot be judged as ambition or as progress (AP-04).
- Scores affected: K1=2, K3=2, K5=2; K7=2 for the PL1 set (PL1 capped at 2.4 because it carries three Major anti-patterns, counting AP-06)
- Suggested rewrite: "KR (moved under a separate developer-experience objective): Internal developer satisfaction, quarterly `<survey instrument>`, n ≥ `<n>`: `<current score>`/10 → 8/10." and, in its place under PL1, "KR: Sev-1 incidents per quarter: `<current count>` → `<target>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: The KR opens with Complete and has no metric, no baseline→target pair and no measure moved by anyone outside Platform, so it just restates the deliverable (AP-01). It is done-or-not-done: it reads 0% until the audit closes, so any slippage only shows once it is already late (AP-02). This holds even though company priority C2 itself is worded as completing SOC 2 Type II.
- Scores affected: K1=0, K2=1, K3=2 (per-KR score capped at 1.0; PL2 capped at 2.4 because it carries two Major anti-patterns)
- Suggested rewrite: "KR: SOC 2 Type II controls with auditor-accepted evidence: `<baseline>`/`<total>` → `<total>`/`<total>`, audit report received by `<date>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: The KR states no starting value, and none exists anywhere in the corpus. The search covered Growth's section, the company priorities, the other three team pages and the Q2 review, whose only Growth figure is qualified signups. So 22% cannot be judged as a stretch or a sandbag, and progress cannot be measured from a starting value.
- Scores affected: K1=2, K3=2 (K3 capped because calibration cannot be verified)
- Suggested rewrite: "KR: Trial-to-paid conversion for trials started in Q3, converted within `<N>` days (source: `<billing analytics report>`): `<current rate>`% → 22%." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 46)
- Evidence: "Turn our funnel into a machine" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 43)
- Also: AP-04 KR Without Baseline
- Why it's a problem: Blog pageviews rise with exposure and spend without showing that the funnel converts. Conversion is what G2 and its sibling KRs on checkout conversion and qualified signups are about (AP-03). The KR also gives no current pageview figure and none exists in the corpus, so 50,000 cannot be calibrated (AP-04). Marking it aspirational makes it uncommitted, but it still measures the wrong thing.
- Scores affected: K1=2, K2=2, K3=2 (G2 capped at 2.4 because it carries two Major anti-patterns)
- Suggested rewrite: "KR (aspirational): Qualified signups whose first session started on a blog article: `<baseline>`/mo → `<target>`/mo (source: `<web analytics attribution report>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient · AP-14 Date as Target
- Why it's a problem: The KR opens with Ship and has no metric, no baseline→target pair and no measure moved by anyone outside Payments, so it restates a delivery instead of a result (AP-01). It reads 0% until GA and 100% after (AP-02), and the only way it can fail is by missing Sep 26 (AP-14).
- Scores affected: K1=0, K2=1, K3=2 (per-KR score capped at 1.0; P1 capped at 2.4 because it carries three Major anti-patterns)
- Suggested rewrite: "KR: Card checkout transactions served by checkout & billing API v2: 0% → `<target>`% by Sep 26, with checkout success rate on v2 at or above `<current rate>`%." [proposal — placeholder target]

## 4. Alignment findings

Dependency map (consumer → producer): Payments → Platform (PCI-scoped infra), Growth → Payments (billing API v2), Data → Platform (streaming pipeline). There are no cycles.

Blocking keys used:
- Conflicting metrics: metric identity, plus surface and lever.
- Duplication: metric plus population.
- Terminology: shared metric names.
- Baseline disagreement: baselines stated for a shared metric.
- Graph checks on the three edges and on Platform as a shared resource.
- Strategy trace over C1–C4.

Candidates killed by a disconfirming check and not reported:
- Payments' checkout success rate against Growth's checkout conversion: a look-alike pair.
- A terminology collision and a baseline disagreement on activation: only one side defines activation, and both state 31%.
- A commitment asymmetry on Growth → Payments: both KRs are committed.
- Orphan status for the other seven objectives: each has an explicit or inferred parent.
- Cascade drift on P2 → C3: P2.1 moves C3's own metric.

Severity basis: each page says KRs are committed unless marked aspirational. That page-level rule counts as committed for the base severity rules, but not as an explicit per-KR mark for escalation.

### [Critical] AL-07 Resource contention: Payments ↔ Data ↔ Platform
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Payments evidence: "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Platform evidence: "Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Payments' P1.2 needs PCI-scoped infra that it assumes Platform provisions in July. Data's D1.1 rides on a streaming pipeline that Data expects the infra level to handle. Platform, however, declares Q3 fully committed to SOC 2 evidence collection and the cost work, and holds non-critical infra requests until Q4. That leaves two committed Q3 demands and no spare capacity declared, and Payments' July need-by falls inside the Q4 hold. This is Critical rather than the default Major because two other findings depend on it: AL-06 Timeline mismatch (through P1.2) and AL-01 Unacknowledged dependency (through D1.1).
- Detection check that fired: resource-node fan-in (AL-07 heuristic). Grouping resource requests by owner shows two same-quarter claimants on Platform, and Platform's own page states a capacity limit. Under the AL-07/AL-01 aggregation rule, Payments' provisioning ask belongs entirely to this finding.
- Disconfirming checks run:
  - Plural demand ≠ contention: no Jira epics or allocation table are in scope (file export only). Platform's section (lines 52–65) names no PCI, provisioning, pipeline, streaming or schema work, and its note states outright that Q3 has no spare capacity. Result: not falsified.
  - Same quarter: both KRs sit on Q3 pages, and Payments' need-by is July. Result: confirmed.
  - Same resource: Payments names Platform, and Data's infra level resolves to Platform (labelled below). Result: confirmed.
  - Distinct deliverable: Data's pipeline migration is a project Platform would have to plan, not just a capacity request, so it also gets its own AL-01 finding below. The capacity arithmetic is reported only here.
- Inference labels:
  - Analyst inference: Data's phrase the infra level (line 82) means Platform. Platform's page is the only one that treats infra requests as its own (line 65), and Payments ties the infra to Platform provisioning (line 30).
  - Analyst inference: Payments' July need-by falls under the Q4 hold only if Platform classes the PCI-scoped infra as non-critical, which its page does not say.
- Verdict: CONFIRMED (all six quotes re-checked character-for-character against the source; the inferred owner link is labelled)
- Recommended resolution owner: Platform (Elena R.) should convene Payments (Priya N.) and Data (Jonas K.) immediately. Together they decide whether the PCI-scoped infra and the pipeline migration take priority over part of the cost work or formally move to Q4, and re-date P1.2 and D1.1 to match. If the decision affects the SOC 2 work behind C2, escalate to Dana W. (CEO).

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth evidence: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's committed G1.3 launches on the new billing API by Aug 15, but Payments commits only to GA by Sep 26, up to six weeks later. No earlier API v2 milestone appears anywhere, so the launch depends on nothing that has been committed. If GA lands on its deadline, only the last days of Q3 remain for the 300 upgrades. This is Critical because the dates are hard-inverted between two committed KRs (neither is marked aspirational).
- Detection check that fired: date comparison along the dependency edge (AL-06 heuristic). The consumer's need-by date (Aug 15) comes before the producer's delivery (by Sep 26).
- Disconfirming checks run:
  - Late date ≠ inversion: I searched the whole file for an earlier or partial API v2 milestone (beta, preview, early, milestone) and found none. The tightest reading the text supports is GA by Sep 26, so the inversion stands.
  - Producer acknowledgment: P1.2 commits the deliverable itself, so this is not an unacknowledged dependency. But Payments' page never mentions Growth, upgrades or Aug 15, and Growth's "should be fine" note gives no date or plan. Result: not weakened.
  - Commitment labels: both pages use the same committed-unless-marked rule and neither KR is marked, so there is no commitment asymmetry. The root cause is timing.
- Inference labels:
  - Analyst inference: Growth's new billing API is Payments' checkout & billing API v2. The names match, and Growth's note cites Priya, owner of the Payments page (line 18).
  - Analyst inference: the upgrade flow needs production GA, not a sandbox.
  - Q3 ending Sep 30 is a calendar fact, not a quote.
  - Upstream, P1.2's own date depends on Platform's PCI-scoped infra (AL-07 Resource contention above).
- Verdict: CONFIRMED (all three quotes re-checked character-for-character; inferred links are labelled)
- Recommended resolution owner: Growth (Marcus T.) with Payments (Priya N.), now, because the plan's own dates leave no slack. Either Payments commits a dated pre-GA milestone the upgrade flow can build on, or Growth moves G1.3's launch after GA and resets the 300-upgrade target.

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments, Growth, Platform, Data
- Company priorities evidence: "C4 — Launch Brightledger Capital" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Company priorities evidence: "invoice-financing pilot live with 3 design partners by Sep 30." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Growth evidence (closest near-miss, not coverage): "first invoice sent within 7 days" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Conflict: Company priority C4, an invoice-financing pilot live with 3 design partners by Sep 30, has no contributing objective, KR or note on any of the four in-scope team pages. The problem is a missing contribution, not an extra one. This is Critical because it is a dated priority on the CEO-owned priorities page with no coverage among the teams reviewed.
- Detection check that fired: top-down strategy trace (AL-10 heuristic). C4 has no contributing objectives or KRs among the 8 team objectives and 21 KRs.
- Disconfirming checks run:
  - Zero hits ≠ coverage gap: I re-searched all four team sections (lines 17–82) and the Q2 review (lines 86–91) for synonyms and program names: Capital, financing, invoice-financing, pilot, design partner, lending, loan, credit, advance, C4, Sep 30. Every hit is on line 13 itself. The only near-miss, Growth's activation definition, is about sending invoices, not financing them. Result: the gap stands.
  - Named owner: C4's line assigns no owner outside the teams reviewed. The page names only its own owner, Dana W. (CEO), so this is not a case of the work belonging to another team.
- Inference labels: none — all load-bearing text is quoted; the absence claim rests on the stated search.
- Verdict: CONFIRMED (quotes re-checked character-for-character; search stated)
- Recommended resolution owner: Dana W. (CEO, owner of the priorities page) should name an owning team for C4, or formally re-date or de-scope it, immediately. The pilot's own deadline is Sep 30.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 74)
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (closest partial match): "Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 65)
- Conflict: Data's committed D1.1 rides on a streaming pipeline migration that Data expects the infra level to deliver. Nothing on Platform's page (objectives, KRs or note) mentions a pipeline, streaming, schema or migration, and its only relevant line defers non-critical infra requests to Q4. The capacity side of this dependency is reported once, under AL-07 Resource contention.
- Detection check that fired: dependency-phrase extraction (AL-01 heuristic). The phrases rides on and expect the pipeline itself to be handled at the infra level point to work outside Data. That work resolves to Platform, and Platform's side has no matching deliverable.
- Disconfirming checks run:
  - Missing mention ≠ unacknowledged: Platform's backlog and Jira epics are not in scope (file export only). On the exported page, Platform names its Q3 work as SOC 2 evidence collection and the cost work; neither is a pipeline migration. Result: the finding survives, with the absence claim limited to the export.
  - Distinct deliverable (AL-07 aggregation rule): Data sized only its own part, at 3 engineer-months, so the pipeline is a project Platform would have to plan, not just a capacity request. It is therefore filed alongside AL-07.
  - Severity: Platform defers all non-critical infra requests but never says whether this migration is non-critical. The condition for Critical (explicit deprioritization) is not shown, so the default Major applies.
- Inference labels: analyst inference — the infra level means Platform (same basis as AL-07 Resource contention above).
- Verdict: CONFIRMED (all three quotes re-checked character-for-character; the owner link is labelled)
- Recommended resolution owner: Data (Jonas K.) with Platform (Elena R.), as part of the same capacity decision as AL-07. Either put the streaming pipeline migration on Platform's plan with an owner, size and date, or re-scope or re-date D1.1.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 80)
- Data evidence: "Own onboarding personalization end-to-end" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 78)
- Conflict: Both teams independently commit to the same metric, for the same new users and from the same 31% baseline, but to different targets (40% vs 35%). Data also claims to own onboarding end-to-end, while Growth's objective covers the same first week. With no cross-reference, shared owner or agreed split of work, nobody knows which target counts or who owns onboarding. This is Major because one metric has two inconsistent targets.
- Detection check that fired: clustering by metric and population (AL-03 heuristic). New-user activation rate over new users' first 7 days appears on both pages.
- Disconfirming checks run:
  - Similar objectives ≠ duplication: same population, same 7-day window (Data's D2.1 also targets the first 7 days, line 79), same baseline, and no segment split. Growth's page never mentions Data, Jonas, onboarding or personalization. Data's page never mentions Growth or Marcus. The company priorities assign no split of responsibility, and Growth's only cross-team note is a billing-API sync with Payments. Result: the finding survives.
  - Terminology collision: only Growth defines activation, and the identical name and 31% baseline point to a single measurement, so there is no second definition to compare. Not filed.
  - Conflicting metrics: both push the metric the same way and the targets are nested. Not filed.
- Inference labels: analyst inference — Data's undefined new-user activation rate is the same measure as Growth's first invoice sent within 7 days (identical name and 31% baseline).
- Verdict: CONFIRMED (all three quotes re-checked character-for-character)
- Recommended resolution owner: Growth (Marcus T.) with Data (Jonas K.), before either team ships onboarding work. They should agree one accountable owner, one Q3 target, one written definition of activation, and an explicit split of onboarding work.

### [Major] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: Payments' KR expands step-up verification coverage from 35% to 90% of transactions, while Growth commits to lifting self-serve checkout conversion from 58% to 68%. If self-serve signup payments are among those transactions, each added step-up challenge adds friction to the checkout Growth needs to convert, so pushing one KR predictably hurts the other. Neither page mentions the other team. This is Major, a conflict through mechanism rather than a shared metric, and not escalated because the link rests on the inferences below.
- Detection check that fired: surface-and-lever blocking key (AL-02 heuristic). Both KRs sit on the checkout, P2.2's stated lever is a verification step (a friction control), and G2.1 targets conversion on that same checkout. The metric-identity key generated nothing because the KRs share no metric.
- Disconfirming checks run:
  - Shared metric ≠ conflict: there is no shared metric and no shared or parent OKR covering both (P2 cites company priority C3; G2 cites none). There is also no documented split of the lever: Payments' page never mentions Growth or self-serve, and Growth's never mentions fraud or verification. Result: the finding survives.
  - Payments' own wording (P2's without drama, P1's never think about) may signal an intent to keep step-up light, but no KR or guardrail commits to it. Result: does not kill the finding.
  - Killed sibling: Payments' checkout success rate for card transactions (P1.1, line 22) against G2.1 is a look-alike pair. The two metrics have different definitions and populations, move in the same direction, and neither side pulls a lever against the other, so that pair was dropped. Dropping it does not affect this finding.
- Inference labels:
  - Analyst inference: Growth's self-serve checkout runs through Payments' checkout. The only support is Growth's note that self-serve upgrades will use the new billing API (line 48) and Payments' checkout & billing API v2 (line 23).
  - Analyst inference: the friction→conversion mechanism, which no Brightledger document states.
  - Analyst inference: reading coverage as a step-up challenge on each covered transaction.
- Verdict: PLAUSIBLE — both quotes re-checked character-for-character, but the shared checkout and the mechanism are inferred.
- Recommended resolution owner: Payments (Priya N.) with Growth (Marcus T.), before step-up coverage rises above its 35% starting point. They should agree how step-up applies to self-serve checkout (for example, risk-based targeting) and set a checkout-conversion floor of `<floor>`% on the P2.2 rollout [proposal — placeholder target], then re-base G2.1.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "One trustworthy source of truth" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D1: One trustworthy source of truth › line 73)
- Data evidence: "we've sized our part at 3 engineer-months" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Objective D2: Own onboarding personalization end-to-end › line 82)
- Company priorities evidence: "C1 — Grow self-serve revenue" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 10)
- Company priorities evidence: "C2 — Become enterprise-ready" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 11)
- Company priorities evidence: "C3 — Cut fraud losses" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 12)
- Company priorities evidence: "C4 — Launch Brightledger Capital" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md › Company Q3 2026 priorities › line 13)
- Conflict: D1 has no traceable parent. It cites no company priority. None of its KR metrics (cross-source discrepancies, dashboard latency, data quality) is a company-level metric or a documented driver of one. C1–C4 never mention data, dashboards or metric quality. Even so, Data has sized its schema v2 part at 3 engineer-months. This is Minor because that capacity figure is not stated as a share of the team's capacity.
- Detection check that fired: three-way strategy check (AL-04 heuristic) on explicit link, metric linkage and mention on the strategy page. Result: 0 of 3.
- Disconfirming checks run:
  - No parent link ≠ orphan: there is no explicit link. The only company-priority reference on any team page is Payments' C3 note (line 30). The nearest candidate parent, C2's enterprise-grade reliability, is measured in the corpus as API uptime (Q2 review, line 89), not as data latency or quality, so there is no inferred parent either. Result: the finding survives.
  - Team justification or exploratory charter: none on Data's page. Result: the finding survives.
- Inference labels: none — all load-bearing text is quoted; the absence claim rests on the stated three-way check.
- Verdict: CONFIRMED (all six quotes re-checked character-for-character)
- Recommended resolution owner: Data (Jonas K.) with the priorities owner Dana W. (CEO), before the 3 engineer-months are spent. Either name D1's parent priority with a metric link (for example, which C1–C4 readouts depend on the exec dashboard) or de-prioritize D1.

## 5. Prioritized action list

1. Convene Platform, Payments and Data to allocate Platform's Q3 infra capacity: decide whether the PCI-scoped infra and the streaming pipeline migration take priority over part of the cost work or formally move to Q4, and re-date P1.2 and D1.1 to match — owner: Platform lead Elena R. (resolves §4 AL-07 Resource contention and §4 AL-01 Unacknowledged dependency).
2. Re-sequence Growth's self-serve upgrade launch against API v2, either on a dated pre-GA milestone committed by Payments or by moving G1.3 after GA and resetting its 300-upgrade target — owner: Growth lead Marcus T., with Payments lead Priya N. (resolves §4 AL-06 Timeline mismatch).
3. Assign an owning team to company priority C4's invoice-financing pilot, or formally re-date or de-scope it — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
4. Replace D1.3 with a KR that names its core tables, its data-quality tests and a baseline — owner: Data lead Jonas K. (resolves §3 AP-09 Metric Nobody Can Measure).
5. Agree one owner, one Q3 target and one written definition for new-user activation, and split onboarding work between Growth and Data — owner: Growth lead Marcus T., with Data lead Jonas K. (resolves §4 AL-03 Duplicated / overlapping objectives).
6. Set a checkout-conversion floor on the step-up rollout and agree how step-up applies to self-serve checkout before coverage rises above 35% — owner: Payments lead Priya N., with Growth lead Marcus T. (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
7. Convert the two milestone KRs, P1.2 (API v2 GA) and PL2.2 (SOC 2 audit), into KRs that show progress during the quarter — owners: Priya N. for P1.2 and Elena R. for PL2.2 (resolves both §3 AP-01 Task Masquerading as KR findings).
8. Re-base Platform's uptime KR on the Q2 review's 99.95% trailing figure, and move the developer-satisfaction KR under its own objective with a named survey and a baseline — owner: Platform lead Elena R. (resolves §3 AP-06 Sandbagged Target and §3 AP-12 Orphan KR).
9. Give G1.1 a sourced baseline and replace G2.3's blog pageviews with a funnel outcome — owner: Growth lead Marcus T. (resolves §3 AP-04 KR Without Baseline and §3 AP-03 Vanity Metric).
10. Name D1's parent company priority with a metric link, or de-prioritize D1 before its 3 engineer-months are spent — owner: Data lead Jonas K., with Dana W. (resolves §4 AL-04 Orphan objective).

## 6. Suggested single-team re-runs

- **Data**. Reason: roll-up C (2.34), above the D needs-rework threshold, but it has Critical findings: §3 AP-09 Metric Nobody Can Measure, and it is a claimant in §4 AL-07 Resource contention. Re-run single-team mode: "Review the Data team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Data team — Q3 2026' (lines 69–82; Confluence page 88225, owner Jonas K.); prior-period actuals: 'Appendix — Q2 2026 business review (extracts)' in the same file (lines 86–91); strategy doc: 'Company Q3 2026 priorities' in the same file (lines 7–13; Confluence page 88101)."
- **Platform**. Reason: roll-up C (2.40); Critical: the overcommitted team in §4 AL-07 Resource contention. Re-run single-team mode: "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Platform team — Q3 2026' (lines 52–65; Confluence page 88221, owner Elena R.); prior-period actuals: 'Appendix — Q2 2026 business review (extracts)' in the same file (lines 86–91); strategy doc: 'Company Q3 2026 priorities' in the same file (lines 7–13; Confluence page 88101)."
- **Growth**. Reason: roll-up C (2.64); Critical: the dependent team in §4 AL-06 Timeline mismatch. Re-run single-team mode: "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Growth team — Q3 2026' (lines 34–48; Confluence page 88217, owner Marcus T.); prior-period actuals: 'Appendix — Q2 2026 business review (extracts)' in the same file (lines 86–91); strategy doc: 'Company Q3 2026 priorities' in the same file (lines 7–13; Confluence page 88101)."
- **Payments**. Reason: roll-up B (2.84); Critical: the delivering team in §4 AL-06 Timeline mismatch, and a claimant in §4 AL-07 Resource contention. Re-run single-team mode: "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-portfolio/input/sample-portfolio.md, section 'Payments team — Q3 2026' (lines 17–30; Confluence page 88213, owner Priya N.); prior-period actuals: 'Appendix — Q2 2026 business review (extracts)' in the same file (lines 86–91); strategy doc: 'Company Q3 2026 priorities' in the same file (lines 7–13; Confluence page 88101)."
