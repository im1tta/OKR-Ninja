# Brightledger — Q3 2026 portfolio OKR review

*OKR-Ninja portfolio-mode audit · cycle date 2026-09-14 · scope: Payments, Growth, Platform, Data (4 teams) · period: Q3 2026 · corpus: `examples/sample-portfolio.md` (Confluence export: company priorities page 88101, team pages 88213 / 88217 / 88221 / 88225, Q2 business review 88104) · strategy source: "Company Q3 2026 priorities" (C1–C4).*

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings. No team reaches B; all four land at C.
The portfolio's biggest threat is AL-10 Strategy coverage gap: company priority C4 (Brightledger Capital, dated Sep 30) has zero coverage — no objective, KR, or note in any of the four teams mentions Capital, invoice financing, design partners, or a pilot.
Two more Criticals are cross-team: AL-06 Timeline mismatch (Growth commits to self-serve upgrades by Aug 15 on a billing API that GAs Sep 26) and AL-02 Conflicting metrics / adversarial incentives (Payments pushes step-up verification to 90% of transactions while Growth commits to +10pt checkout conversion).
The most common quality issue is AP-04 KR Without Baseline (3 instances across Growth and Platform: trial-to-paid conversion, blog pageviews, developer satisfaction).
Two KRs are unscoreable as written (AP-09 Metric Nobody Can Measure — Platform's developer satisfaction score, Data's "data quality") and cap both teams' affected objectives at D.
Platform is the portfolio's single choke point: it declares Q3 fully committed while Payments and Data both plan on infra work from it (AL-07 Resource contention, AL-01 Unacknowledged dependency).
Recommended first action: assign an owner for C4 this week, before the Sep 30 date makes the question moot.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |
| Data | 3 | 2 | 3 | 1 | 3 | 3 | 2 | 3 | 1 | 2 | 3 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.2) · Data C (2.3) · Growth C (2.6) · Payments C (2.7).

- Platform: K5=1 — "Improve internal developer satisfaction score to 8/10" names no measuring instrument anywhere.
- Data: K5=1 and O4=1 — "Significantly improve data quality across core tables" has no system of record.
- Growth: K1=2 — "Increase trial-to-paid conversion to 22%" states a target with no baseline.
- Payments: K1=2 — "Ship checkout & billing API v2 to GA by Sep 26" counts nothing measurable.

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`examples/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline
- Search performed for the absence claim: the full corpus (company priorities page 88101, all four team pages 88213/88217/88221/88225, and the Q2 business-review appendix 88104) searched for "satisfaction", "survey", "eNPS", "score" — the only hit is this KR itself; no instrument, survey cadence, sample size, or dashboard is named anywhere, and no prior value for the score appears.
- Why it's a problem: the "developer satisfaction score" is defined only in the team's head — no system of record could report 8/10 honestly, so the KR can never be scored; and with no current value, the 8 is neither ambition nor progress.
- Scores affected: K5=0, K1=1, K3=2 (unverifiable-calibration cap)
- Suggested rewrite: "KR PL1.3: Internal developer survey (quarterly, n ≥ `<respondents>`, run on `<named survey tool>`): satisfaction `<baseline>`/10 → 8/10, question wording frozen for the year." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`examples/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (baseline, other end of the cross-source claim): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`examples/sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Why it's a problem: the target sits 0.05pt *below* the trailing-90-day actual, so the quarter is won by changing nothing — a classic "maintain/at or above" sandbag against a baseline the corpus itself states.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, measured on the same monitor, with error-budget burn reported weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`examples/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is the delivery itself — it begins with a completion verb, states no metric and no baseline→target pair, and nothing outside the team moves; it also scores 0% until the audit lands and 100% the day it does, so mid-quarter progress is invisible.
- Scores affected: K1=0, K2=1, K3=2
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence requests closed `<0>`/`<N>` → `<N>`/`<N>` (auditor's request tracker), with the Type II observation window opened by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`examples/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Search performed for the absence claim: the full corpus (pages 88101, 88213, 88217, 88221, 88225, 88104) searched for "quality", "score", "dashboard", "check" — the only data-quality hit is this KR; the corpus names exactly one measurement instrument for the Data team, "the weekly exec-dashboard reconciliation check" (line 74), and it measures discrepancies, not "quality".
- Why it's a problem: "data quality" names no metric, no scale and no system of record, and "Significantly" supplies direction without magnitude — at quarter end any outcome can be argued to satisfy it, so the KR is unscoreable rather than merely vague.
- Scores affected: K5=0, K1=1, K3=2 (unverifiable-calibration cap)
- Suggested rewrite: "KR D1.3: Core-table freshness and completeness violations raised by the nightly data-quality suite `<baseline>`/week → `<target>`/week, suite covering the `<N>` core tables listed in `<catalog>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`examples/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Search performed for the absence claim: all four team pages and the Q2 business-review appendix searched for "trial-to-paid" and "conversion" — the appendix states Q2 actuals for uptime, chargebacks, step-up coverage and qualified signups (lines 89–91) but no trial-to-paid figure, and no other page carries one.
- Why it's a problem: with no starting point stated and none retrievable in the corpus, 22% could be a stretch or already banked — both ambition and mid-quarter progress are unjudgeable, and the KR sits on a committed objective.
- Scores affected: K1=2, K3=2 (unverifiable-calibration cap)
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<Q2 actual>`% → 22%, trials started in the quarter, measured weekly on `<named analytics dashboard>`." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`examples/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Search performed for the absence claim: all four team pages and the Q2 review appendix searched for "blog" and "pageview" — this KR is the only occurrence; no current pageview figure exists anywhere in the corpus.
- Why it's a problem: pageviews rise with spend and syndication without telling anyone whether the funnel converts, which is what the objective claims; and with no "from" value the 50,000 cannot be read as ambition. The KR is labelled "*(aspirational)*", which sets expectation but does not make the number meaningful.
- Scores affected: K2=2, K1=2, K3=2
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed first-touch in `<named analytics dashboard>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`examples/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR measures the team's own delivery — a shipping verb, a date, no baseline→target pair and no measure anyone outside Payments moves — so it scores 100% on Sep 26 even if no caller has migrated, and 0% until then. Two other teams are planning against this date (see §4 AL-06), which makes the missing adoption measure expensive.
- Scores affected: K1=0, K2=1, K3=2
- Suggested rewrite: "KR P1.2: Checkout & billing traffic served by API v2 `<0>`% → `<target>`% of production calls (baseline 0 at GA), with v2 error rate ≤ v1's `<current rate>`, first external caller integrated by `<date>`." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ all four teams
- Company priority evidence: "C4 — Launch Brightledger Capital:" / "invoice-financing pilot live with 3 design partners by Sep 30." (`examples/sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Portfolio-side evidence (near-miss, quoted and distinguished): the closest thing to a financing product anywhere in the four teams is Payments' "Ship checkout & billing API v2 to GA by Sep 26." (`examples/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23) — a payments API, not invoice financing, and it names no design partners and no pilot.
- Conflict: a dated company priority with a hard Sep 30 deadline has no contributing objective, KR, or even a note in any of the four teams in scope; nobody in the swept portfolio is accountable for it.
- Detection check that fired: top-down strategy trace — company objective with zero contributing children (AL-10 heuristic).
- Disconfirming checks run: re-searched all four team pages under synonyms and programme names — "Capital", "financing", "invoice-financing", "design partner", "pilot" — all four terms occur exactly once in the corpus, on the company priorities line itself; checked the company priority's own page for a named owner outside the swept team set — page 88101 names only "Dana W. (CEO)" as page owner, no delivery owner for C4, so this is not an ownership note; checked the Q2 review appendix for an in-flight programme — none.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both the priority line and the near-miss re-verified character-for-character against the source)
- Recommended resolution owner: Dana W. (CEO) to name an owning team for C4 and a Q3 KR set within one week, or to move the Sep 30 pilot date on the priorities page — the deadline is 16 days out from this review.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`examples/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41)
- Growth dependency evidence: "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`examples/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`examples/sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: the consumer's need-by date (Aug 15) precedes the producer's delivery date (Sep 26) by six weeks — Growth's committed upgrade flow is scheduled to launch on an API that does not reach GA until after the quarter's upgrade window is nearly over, and Growth's own note treats the dependency as settled ("should be fine") without a date.
- Detection check that fired: dependency-map edge date comparison — hard inversion, need-by < delivery (AL-06 heuristic).
- Disconfirming checks run: "late date ≠ inversion" — checked which milestone Growth actually needs, i.e. whether an earlier beta would suffice: Payments' page states only the GA date and no beta, staged milestone, or earlier availability anywhere (lines 22–24, 30), so the tightest quotable reading is GA on Sep 26; checked for a hedge or discount in Growth's own arithmetic — the note says "should be fine", which asserts the opposite of a hedge; checked commitment labels on both sides — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 19 and 36) and neither KR is marked aspirational.
- Inference labels: none — all load-bearing text quoted. (That the upgrade flow cannot launch before the API it "will use" is the teams' own stated relationship, not an inferred one.)
- Verdict: CONFIRMED (all four quotes re-verified character-for-character against the source)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree within one week either an earlier partial/beta availability date for the billing API or a revised G1.3 launch date and upgrade target.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`examples/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`examples/sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control on the checkout surface, and Payments commits to raising its coverage from just over a third of transactions to nearly all of them in the same quarter that Growth commits to a 10-point lift in completion on that surface. Neither KR, and neither team's notes, mentions the other.
- Detection check that fired: surface-lever blocking key — both KRs sit on the checkout surface, Payments' stated lever (verification coverage) is a friction control there, and Growth targets that surface's conversion metric (AL-02 key 2). The metric-identity key generated nothing here; Payments' "Raise checkout success rate from 91.2% to 95% for card transactions." (line 22) and Growth's checkout conversion are lookalike checkout metrics with different populations pushing the same direction, and that candidate was correctly killed — a kill that does not remove the checkout surface from key-2 generation.
- Disconfirming checks run: shared or parent OKR covering both — none; the company priorities page has C1 (revenue) and C3 (fraud) as separate priorities with no shared guardrail. Documented split of levers — searched both team pages and their notes; Payments' note claims fraud work as "our top ask from leadership after the Q2 incident (company priority C3)." (line 30) but says nothing about a conversion floor, and Growth's note (line 48) says nothing about verification. Directionality — confirmed opposed at the mechanism level. Commitment levels — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 19 and 36); neither KR is marked aspirational, which escalates this from Major to Critical.
- Inference labels: the verification-friction → checkout-conversion mechanism is analyst inference — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against the source; the causal mechanism is labelled inference above)
- Recommended resolution owner: Dana W. (CEO) to convene Priya N. and Marcus T. before the mid-quarter checkpoint and set a shared guardrail pair — a chargeback ceiling and a checkout-conversion floor — with step-up coverage staged against it rather than targeted directly. [proposal — placeholder target]

### [Major] AL-07 Resource contention: Payments ↔ Platform ↔ Data
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`examples/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`examples/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs depend on Platform capacity in Q3 — PCI-scoped infra provisioning for the billing API, and the streaming pipeline the schema v2 rollout rides on — while Platform states its Q3 is already fully committed to two other workstreams and is holding infra requests until Q4. Combined demand exceeds the declared supply, and nobody has done this arithmetic: neither claimant's page acknowledges the hold, and Platform's page names neither claimant.
- Detection check that fired: resource-node fan-in on the dependency map — two claimants grouped onto one owner (Platform), then the owner's own page checked for declared supply, which yielded an explicit fully-committed statement (AL-07 heuristic). Classified at the resource node, not edge-by-edge; Payments' provisioning ask is a pure capacity claim and folds into this finding entirely.
- Disconfirming checks run: "plural demand ≠ contention" — searched Platform's page for a capacity or allocation table and for any epic/allocation covering either claimant: the page contains only the two objectives PL1 and PL2, five KRs, and the hold statement, with no allocation table and no mention of PCI infra, provisioning, or a pipeline; confirmed both claims fall in the same quarter (both pages headed "Q3 2026", lines 52 and 69) and name the same resource (Platform / "the infra level"), not similarly-named pods; checked whether either ask is explicitly exempted by the hold's "non-critical" qualifier — neither team's text claims criticality on Platform's behalf, and Platform names no exemptions.
- Inference labels: that "the infra level" in Data's note resolves to the Platform team is analyst inference — Data's note does not name Platform; Platform is the only infrastructure-owning team in the four-team scope.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against the source; the one inferred link is labelled above)
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 allocation decision for the two claimed items within one week — accept, stage, or refuse each — so Payments and Data can re-plan; escalate to Dana W. (CEO) if both must be refused, since the Payments edge sits on the critical path of §4 AL-06.

### [Major] AL-01 Unacknowledged dependency: Data → Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Dependency phrase quoted: "rides on the streaming pipeline migration" and "expect the pipeline itself to be handled at the infra level" (same source ref, line 82)
- Data's dependent KR: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (`examples/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (the partial match, quoted and distinguished): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`examples/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65) — this is a capacity statement, not an acknowledgment: it neither names the pipeline migration nor commits to it, and on its face defers it.
- Conflict: the streaming pipeline migration is a distinct deliverable — a build the producer would have to plan as its own project, beyond allocating capacity — and it appears nowhere in Platform's objectives, KRs, or notes, while a committed Data KR (D1.1, "from 14 to 0") depends on the schema v2 rollout that rides on it. Cross-references §4 AL-07 Resource contention, under which the capacity arithmetic is reported exactly once.
- Detection check that fired: dependency-map edge acknowledgment — a named external deliverable extracted from a "rides on" phrase, resolved to its owning team, with no hit on the producer's side (AL-01 heuristic). Filed separately from the AL-07 aggregate because this edge names a distinct deliverable, not the owner's capacity itself.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched the entire corpus for "pipeline", "streaming", "migration" and "schema": every hit is on Data's own lines 74 and 82; Platform's page (88221, lines 52–65) contains none of them. No Jira/backlog source is available in this corpus, so the search is bounded by the export — stated rather than assumed. Checked whether Data's own note already discounts the dependency — it does the opposite: it states an expectation ("expect the pipeline itself to be handled at the infra level") with no owner, date, or confirmation.
- Inference labels: that "the infra level" resolves to the Platform team is analyst inference — Data's note does not name Platform; Platform is the only infrastructure-owning team in scope.
- Verdict: CONFIRMED (all quotes re-verified character-for-character; the resolution of "the infra level" to Platform is labelled inference above)
- Recommended resolution owner: Jonas K. (Data) to get the streaming pipeline migration named, sized, and owned — by Platform or by Data itself — within one week, since D1.1's committed 14 → 0 target is unreachable without it.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`examples/sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate from 31% to 35% via onboarding experiments." (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Data's ownership claim: "Objective D2: Own onboarding personalization end-to-end" (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 78)
- Conflict: two teams commit to the same metric, from the same stated baseline of 31%, to two different targets (40% and 35%) in the same quarter, with no cross-reference, shared owner, or split of lanes — and Data simultaneously claims end-to-end ownership of the onboarding surface that Growth's objective G1 also targets. If the quarter ends at 37%, both teams can claim a hit and a miss. Secondary: the two pages define the metric differently by omission — Growth states a formula ("first invoice sent within 7 days"), Data states none, so the shared 31% baseline is the only evidence the two numbers measure the same thing (AL-08 Terminology collision, cross-referenced, not filed separately).
- Detection check that fired: clustering on target metric + target population — same canonical metric ("new-user activation rate"), same population (new users), same baseline, two targets; then the mutual-reference check on both pages came back empty (AL-03 heuristic).
- Disconfirming checks run: "similar objectives ≠ duplication" — checked for a legitimate split by population, surface, segment or geography: neither KR restricts itself to a segment or surface, and Data's own objective claims the surface "end-to-end"; searched both team pages and both notes (lines 48 and 82) for any cross-reference to the other team on activation — Growth's note mentions Payments only, Data's note mentions infra only; checked for a parent objective assigning lanes — the company priorities page (lines 10–13) contains no activation objective and assigns no lanes; checked whether the differing targets are explained by different definitions (AL-08) — the shared 31% baseline argues they are the same measurement, so the gap is a target disagreement, not a definitional one.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against the source)
- Recommended resolution owner: Marcus T. (Growth) and Jonas K. (Data) to agree one owner, one target, and one written definition of "activated" before the next cycle checkpoint; the other team carries it as a supporting KR or drops it.

### [Minor] AL-04 Orphan objective: Data ↔ Company Q3 2026 priorities
- Data evidence: "Objective D1: One trustworthy source of truth" (`examples/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 73)
- Company strategy evidence: "C1 — Grow self-serve revenue:" / "C2 — Become enterprise-ready:" / "C3 — Cut fraud losses:" / "C4 — Launch Brightledger Capital:" (`examples/sample-portfolio.md` › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent, and none of the four company priorities covers data trustworthiness, reporting, or analytics — the objective consumes two of the Data team's five KRs with no stated line to company strategy. Data's sibling objective D2 does trace (its activation KR drives self-serve revenue under C1); D1 does not.
- Detection check that fired: strategy trace, three-way check — (a) explicit parent link: none on Data's page; (b) KR metric is a company-level metric or a documented driver of one: D1's metrics are internal discrepancy counts and dashboard latency, neither named in C1–C4; (c) mention in the strategy page: the priorities page contains no data, reporting, dashboard, or analytics language (AL-04 heuristic).
- Disconfirming checks run: "no parent link ≠ orphan" — ran all three legs above before flagging, and re-read Data's own notes for a self-justification that would downgrade or kill the finding: the note (line 82) discusses only the pipeline dependency and sizing, and offers no strategic rationale; checked for an exploratory-charter statement on Data's page — none; checked the capacity claim for the Major escalation — "we've sized our part at 3 engineer-months" (line 82) quantifies effort but states no fraction of the team's capacity and attaches to the schema v2 rollout specifically, so the finding stays Minor.
- Inference labels: the D2 → C1 trace cited as contrast is analyst inference (Data's page states no parent for either objective); the D1 orphan claim itself rests on quoted text and the recorded search.
- Verdict: CONFIRMED (the objective line and all four priority lines re-verified character-for-character against the source)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to either state D1's parent priority on page 88225 or confirm at the next portfolio review that trustworthy reporting is an accepted un-parented platform investment.

## 5. Prioritized action list

1. Name an owning team and a Q3 KR set for company priority C4, or move its Sep 30 date — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Reconcile the self-serve upgrade launch date with the billing API GA date, agreeing either an earlier partial availability or a revised G1.3 date and target — owner: Priya N. (Payments) with Marcus T. (Growth) (resolves §4 AL-06 Timeline mismatch).
3. Convene Payments and Growth to set a shared chargeback-ceiling / checkout-conversion-floor guardrail pair and stage step-up coverage against it — owner: Dana W. (CEO) (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Publish a Q3 allocation decision — accept, stage, or refuse — for the PCI-scoped infra provisioning and the streaming pipeline migration — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
5. Get the streaming pipeline migration named, sized, and owned before relying on schema v2 for D1.1's committed 14 → 0 target — owner: Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
6. Settle one owner, one target, and one written definition for new-user activation rate — owner: Marcus T. (Growth) with Jonas K. (Data) (resolves §4 AL-03 Duplicated / overlapping objectives).
7. Replace the developer satisfaction KR with a named survey instrument, sample size, and quoted baseline, or drop it from the OKR set — owner: Elena R. (Platform) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
8. Replace "Significantly improve data quality" with a countable violation rate from a named suite over a listed table set — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
9. Re-target API uptime against the quoted 99.95% trailing-90-day actual instead of 99.9% — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target).
10. Rewrite the four delivery-and-no-baseline KRs — P1.2, PL2.2, G1.1 and G2.3 — as baseline→target measures using the §3 rewrites — owners: Priya N. (Payments), Elena R. (Platform), Marcus T. (Growth) (resolves §3 AP-01 Task Masquerading as KR ×2, AP-04 KR Without Baseline, AP-03 Vanity Metric).

## 6. Suggested single-team re-runs

All four teams qualify under criterion (b) — each carries at least one Critical finding. No team qualifies under criterion (a): every roll-up grade is C, above the rubric's D-or-below needs-rework threshold.

- **Platform** (roll-up C (2.2); Critical AP-09 Metric Nobody Can Measure on KR PL1.3, plus AL-07 Resource contention and inbound AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: the Platform section of the local export `examples/sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: 'Company Q3 2026 priorities' (page 88101, CO-PRIO-Q3); prior-period actuals in the Q2 2026 business review extract (page 88104)."
- **Data** (roll-up C (2.3); Critical AP-09 Metric Nobody Can Measure on KR D1.3, plus AL-01 Unacknowledged dependency and AL-04 Orphan objective): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: the Data section of the local export `examples/sample-portfolio.md` (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: 'Company Q3 2026 priorities' (page 88101, CO-PRIO-Q3); prior-period actuals in the Q2 2026 business review extract (page 88104)."
- **Payments** (roll-up C (2.7); Critical AL-02 Conflicting metrics / adversarial incentives and Critical AL-06 Timeline mismatch, both on committed KRs): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: the Payments section of the local export `examples/sample-portfolio.md` (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: 'Company Q3 2026 priorities' (page 88101, CO-PRIO-Q3); prior-period actuals in the Q2 2026 business review extract (page 88104)."
- **Growth** (roll-up C (2.6); Critical AL-02 Conflicting metrics / adversarial incentives and Critical AL-06 Timeline mismatch, plus AP-04 KR Without Baseline and AP-03 Vanity Metric): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: the Growth section of the local export `examples/sample-portfolio.md` (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: 'Company Q3 2026 priorities' (page 88101, CO-PRIO-Q3); prior-period actuals in the Q2 2026 business review extract (page 88104)."
