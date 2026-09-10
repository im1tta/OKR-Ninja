# OKR-Ninja — Single-team review: Platform, Q3 2026

**Mode:** single-team (exactly one team in confirmed scope) · **Team:** Platform · **Period:** Q3 2026 · **Source:** `input/sample-portfolio.md` (Platform OKR page, lines 3–16; Q2 2026 business review appendix, lines 18–23).

**Sources searched (for all absence claims below):** the single provided export `input/sample-portfolio.md` in full — the Platform OKR page ("Source: Confluence page 88221 (PLAT-OKR-Q3)", line 4) and the business-review appendix ("Source: Confluence page 88104 (Q2-REVIEW)", line 19). No Atlassian connection was available, and no company or portfolio strategy document was provided. Nothing else was consulted.

---

## 1. Verdict summary

**Verdict: Usable but flawed — two of five KRs cannot be honestly scored as written, and the quarter's headline reliability target is a sandbag.**
Roll-up grade: **C (2.15)** — above the rubric's needs-rework threshold, but carrying one Critical defect that blocks trust in Objective PL1.
Findings: **1 Critical, 3 Major, 0 Minor**, across 2 objectives and 5 key results, all scored exhaustively.
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, no scale definition and no baseline, so it can never be honestly scored.
Close behind: **AP-06 Sandbagged Target** — the committed 99.9% uptime KR sits *below* the 99.95% trailing-90-day figure the company's own Q2 review reports.
No company-level strategy document was in scope, so **company-level strategy tracing was out of scope**: O4 Strategic Anchoring is scored **N/A** for both objectives per the rubric and recorded as a gap in §2 below, not as a finding.
This is a single-team review: no cross-team alignment (AL-XX) findings are produced, because one team cannot supply both sides' verbatim quotes. One outbound dependency mention is recorded, unverified, in §4.
Recommended first action: replace KR PL1.3 with a survey-instrumented, baselined measure — or drop it from the OKR set — before any Q3 grading happens.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 2 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — PL1 1.9 (D, capped by a Critical anti-pattern; pre-cap 2.24) · PL2 2.4 (C, capped by two Major anti-patterns on one OKR; pre-cap 2.52).
- Platform: K5=1 — two KRs name no system of record and one names no instrument at all (AP-09 Metric Nobody Can Measure).

**O4 gap note (rubric-mandated, recorded here and not as a finding):** no strategy source exists anywhere in the corpus searched above, so O4 is scored **N/A** for both objectives and excluded from the roll-up. Neither objective states a parent — the OKR page carries no "supports…"/pillar line — so strategic anchoring is unjudgeable rather than absent-and-scored-zero. Supply the company Q3 2026 priorities page and O4 becomes scorable for both objectives.

### Per-instance breakdown

**Objectives**

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 2 | 2 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

Drivers (quoted spans, per Evidence Discipline rule 2):
- **PL1 O1=2** — "Objective PL1: Keep the lights on, cheaper" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 7`): "Keep the lights on" names the team's standing state, not a change in the world; only "cheaper" carries a delta, and deleting it leaves the objective with no outcome at all.
- **PL1 O2=2** — same span: "Keep the lights on" is exactly the kind of abstraction two readers gloss differently (availability? incident count? simply continuing to operate?), and "cheaper" attaches to no named noun.
- **PL1 O3=3** and **PL2 O3=3** — neither objective restates a period; both inherit it unambiguously from the page heading "Platform team — Q3 2026" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 3`).
- **PL2 O1=4** — "Objective PL2: Earn enterprise trust" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 12`): a changed end-state held by someone outside the team, with no delivery verb and no named solution.
- **PL2 O2=3** — same span: short and plain, but "trust" is one abstraction that two readers would operationalize differently (audit certificates? uptime? contractual terms?).
- **PL1 O4=N/A · PL2 O4=N/A** — see the O4 gap note above.

**Key results**

| KR | K1 | K2 | K3 | K4 | K5 | per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." | 1 | 3 | 2 | 3 | 0 | 1.0 (capped: K5=0) |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 "Complete the SOC 2 Type II audit." | 0 | 1 | 2 | 3 | 2 | 1.0 (capped: K1=0) |

Drivers (quoted spans, per Evidence Discipline rule 2):
- **PL1.1 K1=3** — "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`) states metric, target and unit but no baseline in the KR itself; the baseline is retrievable from the same corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`) — and no measurement window is stated.
- **PL1.1 K3=1** — sandbag; see §3 AP-06.
- **PL1.1 K5=3** — the KR names no source, but "(Datadog SLO monitor)" (line 21) is the single obvious system of record for this metric elsewhere in the corpus.
- **PL1.2 K1=3** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`) carries baseline, target and unit; only the measurement window is unstated.
- **PL1.2 K3=3** — same span: a 22% unit-cost reduction from a stated baseline is clearly a stretch, but no justification or mechanism is given anywhere on the page.
- **PL1.2 K5=2** — same span: neither the cloud-cost system of record nor the source of the "1,000 transactions" denominator is named, and the search above found no candidate dashboard in the corpus.
- **PL1.3 K1=1, K3=2, K5=0** — see §3 AP-09; K3 additionally hits the rubric's unverifiable cap (no baseline or trend for this metric anywhere in the sources searched above), and calibration is therefore unverifiable rather than judged.
- **PL1.3 K2=3** — "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) measures internal-customer sentiment, a proxy whose causal link to anything the objective claims is never stated.
- **PL2.1 K1=3** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`) states baseline ("currently 7 open") and target (100%) against a bounded population; the measurement window is unstated.
- **PL2.1 K2=3** — same span: closing High-severity findings is a credible proxy for the objective's outcome, but the KR does not state the link.
- **PL2.1 K3=3** — same span: full closure of a known 7-item backlog is a modest, properly-labeled committed stretch under "KRs are committed unless marked (aspirational)." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 5`).
- **PL2.1 K5=2** — same span: no tracker, report or dashboard of record is named for pen-test findings, and none appears in the sources searched.
- **PL2.2 K1=0, K2=1** — see §3 AP-01; **K3=2** is the unverifiable cap (no baseline or magnitude exists to calibrate), and **K5=2** because "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`) implies an auditor's report but names no system of record.
- **K4=3 for all five KRs** — "Owner: Elena R." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 4`) names an individual on the OKR source, but at page level only; no KR carries its own accountable owner.

**KR sets**

| KR set | K6 | K7 |
|---|---|---|
| PL1 | 2 | 2 |
| PL2 | 2 | 3 |

- **PL1 K6=2** — all three KRs are end-of-quarter truths with no leading indicator to steer by mid-cycle: "Maintain API uptime at or above 99.9%." (line 8), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9), "Improve internal developer satisfaction score to 8/10." (line 10), all at `input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper`.
- **PL1 K7=2** — the set splits across two clauses and carries one orphan: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) serves neither "the lights on" nor "cheaper" in "Objective PL1: Keep the lights on, cheaper" (line 7).
- **PL2 K6=2** — both KRs are compliance milestones — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) and "Complete the SOC 2 Type II audit." (line 14), at `input/sample-portfolio.md › Objective PL2: Earn enterprise trust` — so nothing in the set predicts or confirms the stated outcome.
- **PL2 K7=3** — one coverage gap: no KR touches whether enterprises actually extended trust (deals unblocked, security reviews passed) in "Objective PL2: Earn enterprise trust" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 12`).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: no survey, instrument, scale definition, respondent base or system of record for a "developer satisfaction score" appears anywhere in the sources searched above, so the 8/10 can never be honestly scored — and with no current value stated or retrievable, neither its ambition nor mid-quarter progress can be judged; the KR also shares no domain with its objective, "Objective PL1: Keep the lights on, cheaper" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 7`), so hitting it would not move either the reliability or the cost clause.
- Scores affected: K5=0, K1=1, K3=2, K7=2 (PL1 per-KR score capped at 1.0; PL1 per-OKR score capped at 1.9)
- Suggested rewrite: "KR (moved out of PL1 to a developer-experience objective): Internal developer satisfaction, quarterly platform survey run in the last two weeks of Q3 — instrument `<named survey tool>`, respondents `<n ≥ 40>` of the internal engineering population — `<baseline>`/10 (Q2 run) → 8/10; published to `<dashboard>`." [proposal — placeholder target] If no instrument can be stood up this quarter, drop the KR from the OKR set rather than carry an unscoreable commitment.

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Objective PL1: Keep the lights on, cheaper" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 7`)
- Why it's a problem: "Keep the lights on" is the team's standing operational duty stated with no delta — it is achieved by default staffing and cannot be failed in a way anyone would notice — and it occupies an objective slot that a real Q3 outcome could hold; only the trailing "cheaper" carries any change, and the objective's own KR set confirms the framing with "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`).
- Scores affected: O1=2, O2=2, K7=2
- Suggested rewrite: "Objective PL1: Every Brightledger transaction costs materially less to serve, with no reliability regression customers can feel." Move the standing availability duty to a health-metrics section outside the OKRs, where 99.9% availability is tracked as a guardrail rather than as a goal. [proposal]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target sits *below* the trailing-90-day actual the company's own Q2 review reports, so the KR is achieved by letting reliability degrade — a quarter of doing nothing new, or slightly worse, scores 100%. Under "KRs are committed unless marked (aspirational)." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 5`) this is a committed goal, so it also anchors the team's expected-attainment picture at a number already beaten.
- Scores affected: K3=1, K6=2
- Suggested rewrite: "KR PL1.1: API uptime — Datadog SLO monitor, trailing 90 days — 99.95% (Q2 actual) → 99.98%, sustained through Q3; error budget burn ≤ `<threshold>`% at the mid-quarter checkpoint as the leading indicator." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable that begins with "Complete", with no metric and no baseline→target pair, so it measures that the work happened rather than any result an enterprise customer experiences; and because it is a single done/not-done event, mid-cycle scoring can only be 0% or 100% — the team gets no signal about whether it is on track until the audit either lands or does not.
- Scores affected: K1=0, K2=1, K3=2, K6=2 (PL2 per-KR score capped at 1.0; PL2 per-OKR score capped at 2.4 by two Major anti-patterns on one OKR)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II readiness — controls with complete evidence collected `<0>`/`<N>` → `<N>`/`<N>` by `<date>`, tracked in `<GRC system>`; observation window open from `<start date>` with zero exceptions logged, and the auditor's Type II report received by end of Q3." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 16`) — **unverified — counterparty not in scope.** The note states a cross-team capacity decision — other teams' infra requests are deferred out of Q3 — but names no requesting team, and no other team's material is in scope to check whether any of them has a Q3 commitment that depends on the deferred work. Context from the same line: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 16`). No severity is assigned and this is not a finding.

## 5. Prioritized action list

1. Replace KR PL1.3 with a survey-instrumented, baselined measure — or drop it from the Q3 set — before any Q3 grading happens; owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure).
2. Reset the uptime KR against the quoted 99.95% trailing-90-day baseline and add a mid-quarter error-budget checkpoint; owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a graded evidence-completion measure with a stated denominator and tracker; owner: Platform lead (Elena R.) with the compliance owner (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Reframe Objective PL1 around the cost outcome and move the standing availability duty to a health-metrics section outside the OKRs; owner: Platform lead (Elena R.) (resolves §3 AP-10 BAU Dressed as OKR).
5. Name the system of record for every KR — cloud-cost dashboard, transaction denominator, pen-test tracker, audit evidence store; owner: Platform lead (Elena R.) (raises the K5=1 column in §2; addresses PL1.2, PL2.1 and PL2.2 K5=2).
6. Add at least one leading indicator to each objective's KR set so mid-quarter steering is possible; owner: Platform lead (Elena R.) (addresses K6=2 for both sets in §2).
7. Obtain the company Q3 2026 strategy page and re-score O4 for both objectives; owner: Platform lead (Elena R.) with the exec sponsor (resolves the O4 N/A gap note in §2).
8. Confirm with the teams whose infra requests are being deferred that none of their Q3 commitments depends on the held work; owner: Platform lead (Elena R.) (addresses the §4 outbound dependency note).
