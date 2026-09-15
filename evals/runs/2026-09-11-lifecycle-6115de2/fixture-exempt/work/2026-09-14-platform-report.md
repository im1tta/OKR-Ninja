# Platform team — Q3 2026 OKR report

*Platform's slice of the Brightledger Q3 2026 portfolio review (cycle date 2026-09-14). This page is an extract of that portfolio-mode run — its heatmap row, the findings that name Platform, and the portfolio actions assigned to or about Platform — not a single-team-mode review; Platform's OKRs were screened at portfolio depth, and §6 of the portfolio review recommends a full-depth single-team re-run. Source: `examples/sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy source: "Company Q3 2026 priorities" (page 88101); prior-period actuals: Q2 2026 business review extract (page 88104). Severity scale, finding templates, and source-ref format per `references/report-format.md`.*

## Heatmap row

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **C (2.2)** — worst of the four teams reviewed, and the only team appearing in three separate alignment findings.

- Platform: K5=1 — "Improve internal developer satisfaction score to 8/10" names no measuring instrument anywhere.

## Goodness findings

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

Not flagged, for the record: "Keep the lights on, cheaper" reads like standing duty but does not fire AP-10 BAU Dressed as OKR — the objective names a change ("cheaper") and KR PL1.2, "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 58), pays for it with a baseline→target pair. "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 62) likewise does not fire AP-01 or AP-13: it states a starting point and a countable, defined population.

## Alignment findings naming Platform

### [Major] AL-07 Resource contention: Payments ↔ Platform ↔ Data
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`examples/sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`examples/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs depend on Platform capacity in Q3 — PCI-scoped infra provisioning for the billing API, and the streaming pipeline the schema v2 rollout rides on — while Platform states its Q3 is already fully committed to two other workstreams and is holding infra requests until Q4. Combined demand exceeds the declared supply, and nobody has done this arithmetic: neither claimant's page acknowledges the hold, and Platform's page names neither claimant.
- Detection check that fired: resource-node fan-in on the dependency map — two claimants grouped onto one owner (Platform), then the owner's own page checked for declared supply, which yielded an explicit fully-committed statement (AL-07 heuristic). Classified at the resource node, not edge-by-edge; Payments' provisioning ask is a pure capacity claim and folds into this finding entirely.
- Disconfirming checks run: "plural demand ≠ contention" — searched Platform's page for a capacity or allocation table and for any epic/allocation covering either claimant: the page contains only the two objectives PL1 and PL2, five KRs, and the hold statement, with no allocation table and no mention of PCI infra, provisioning, or a pipeline; confirmed both claims fall in the same quarter (both pages headed "Q3 2026", lines 52 and 69) and name the same resource (Platform / "the infra level"), not similarly-named pods; checked whether either ask is explicitly exempted by the hold's "non-critical" qualifier — neither team's text claims criticality on Platform's behalf, and Platform names no exemptions.
- Inference labels: that "the infra level" in Data's note resolves to the Platform team is analyst inference — Data's note does not name Platform; Platform is the only infrastructure-owning team in the four-team scope.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against the source; the one inferred link is labelled above)
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 allocation decision for the two claimed items within one week — accept, stage, or refuse each — so Payments and Data can re-plan; escalate to Dana W. (CEO) if both must be refused, since the Payments edge sits on the critical path of the portfolio review's AL-06 Timeline mismatch.

### [Major] AL-01 Unacknowledged dependency: Data → Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`examples/sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Dependency phrase quoted: "rides on the streaming pipeline migration" and "expect the pipeline itself to be handled at the infra level" (same source ref, line 82)
- Data's dependent KR: "Cut cross-source metric discrepancies flagged by the weekly exec-dashboard reconciliation check from 14 to 0, by serving all product events from unified event schema v2." (`examples/sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (the partial match, quoted and distinguished): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`examples/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65) — this is a capacity statement, not an acknowledgment: it neither names the pipeline migration nor commits to it, and on its face defers it.
- Conflict: the streaming pipeline migration is a distinct deliverable — a build the producer would have to plan as its own project, beyond allocating capacity — and it appears nowhere in Platform's objectives, KRs, or notes, while a committed Data KR (D1.1, "from 14 to 0") depends on the schema v2 rollout that rides on it. Cross-references AL-07 Resource contention above, under which the capacity arithmetic is reported exactly once.
- Detection check that fired: dependency-map edge acknowledgment — a named external deliverable extracted from a "rides on" phrase, resolved to its owning team, with no hit on the producer's side (AL-01 heuristic). Filed separately from the AL-07 aggregate because this edge names a distinct deliverable, not the owner's capacity itself.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched the entire corpus for "pipeline", "streaming", "migration" and "schema": every hit is on Data's own lines 74 and 82; Platform's page (88221, lines 52–65) contains none of them. No Jira/backlog source is available in this corpus, so the search is bounded by the export — stated rather than assumed. Checked whether Data's own note already discounts the dependency — it does the opposite: it states an expectation ("expect the pipeline itself to be handled at the infra level") with no owner, date, or confirmation.
- Inference labels: that "the infra level" resolves to the Platform team is analyst inference — Data's note does not name Platform; Platform is the only infrastructure-owning team in scope.
- Verdict: CONFIRMED (all quotes re-verified character-for-character; the resolution of "the infra level" to Platform is labelled inference above)
- Recommended resolution owner: Jonas K. (Data) to get the streaming pipeline migration named, sized, and owned — by Platform or by Data itself — within one week, since D1.1's committed 14 → 0 target is unreachable without it.

## Actions naming Platform

Numbering preserved from the portfolio review's §5 prioritized action list so the two pages cross-reference.

4. Publish a Q3 allocation decision — accept, stage, or refuse — for the PCI-scoped infra provisioning and the streaming pipeline migration — owner: Elena R. (Platform) (resolves AL-07 Resource contention).
5. Get the streaming pipeline migration named, sized, and owned before relying on schema v2 for D1.1's committed 14 → 0 target — owner: Jonas K. (Data), with Platform as the named producer (resolves AL-01 Unacknowledged dependency).
7. Replace the developer satisfaction KR with a named survey instrument, sample size, and quoted baseline, or drop it from the OKR set — owner: Elena R. (Platform) (resolves AP-09 Metric Nobody Can Measure — Platform).
9. Re-target API uptime against the quoted 99.95% trailing-90-day actual instead of 99.9% — owner: Elena R. (Platform) (resolves AP-06 Sandbagged Target).
10. Rewrite the four delivery-and-no-baseline KRs across the portfolio — Platform's share is PL2.2 — as baseline→target measures using the rewrites above — owner for Platform's share: Elena R. (Platform) (resolves AP-01 Task Masquerading as KR — Platform).

## Re-run recommendation

Platform qualifies for a full-depth single-team re-run under criterion (b) of the portfolio review's §6 — it carries a Critical finding (AP-09 Metric Nobody Can Measure on KR PL1.3). Its roll-up grade, C (2.2), is above the rubric's D-or-below needs-rework threshold, so criterion (a) does not apply. Ready-to-paste prompt: "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: the Platform section of the local export `examples/sample-portfolio.md` (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: 'Company Q3 2026 priorities' (page 88101, CO-PRIO-Q3); prior-period actuals in the Q2 2026 business review extract (page 88104)."
