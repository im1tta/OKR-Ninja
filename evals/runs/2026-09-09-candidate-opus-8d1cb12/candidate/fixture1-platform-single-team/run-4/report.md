# OKR-Ninja — Single-team review: Platform, Q3 2026

*Mode: single-team (exactly one team in confirmed scope: Platform). Period: Q3 2026, as stated by the source page. Source of record: `input/sample-portfolio.md` — full path `evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md`; source refs below abbreviate it to `input/sample-portfolio.md` and their line numbers refer to that file. No Atlassian source was available; no strategy document was in scope.*

## 1. Verdict summary

**Verdict: Needs rework before the quarter can be trusted.** Roll-up grade **C (2.15)**, dragged down by Objective PL1 at **D (1.9)**.
5 KRs and 2 objectives were scored exhaustively; 4 findings: **1 Critical, 3 Major, 0 Minor**.
The worst finding is **AP-09 Metric Nobody Can Measure** on KR PL1.3 — an 8/10 "developer satisfaction score" that no instrument in the corpus can produce, so the KR can never be honestly scored.
Two of the five KRs are unscoreable or ungraded as written (PL1.3 and PL2.2), and a third, PL1.1, targets a level the team has already exceeded per its own Q2 review.
The set's real strengths: the page states a commitment convention, and PL1.2 is a properly baselined outcome KR.
**Company-level strategy tracing was out of scope** — no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored N/A for both objectives per the rubric and recorded as a gap in §2 rather than as a finding.
**Recommended first action:** rewrite KR PL1.3 around a named survey instrument with a stated baseline, or drop it from Q3 (resolves §3 AP-09 Metric Nobody Can Measure).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 2 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (capped by a Critical anti-pattern), Objective PL2 **C (2.4)** (capped by two Major anti-patterns on one OKR).

- Platform: K1=2 — two of five KRs state no measurable baseline→target pair at all.

**O4 gap note (N/A):** no company, portfolio, or strategy source of any kind exists in the corpus — searched the whole of `input/sample-portfolio.md` (lines 1–24: the Platform OKR page, lines 3–16, and the Q2 2026 business review appendix, lines 18–23); no strategic pillar, bet, or company priority is stated anywhere. Per the rubric, O4 is scored **N/A** for both objectives and excluded from the roll-up, and this gap is recorded here: neither objective can be shown to serve a company priority, and no team-level conclusion about strategic anchoring should be drawn from this review.

### Per-instance breakdown (dimensions whose scores vary)

Objectives:

| Instance | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 2 | 2 | 2 | N/A |
| PL2 "Earn enterprise trust" | 4 | 4 | 3 | N/A |

- PL1 O1=2 — "Keep the lights on, cheaper" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 7`): the only delta in the objective is "cheaper"; "Keep the lights on" states the team's standing condition, not a changed end-state.
- PL1 O2=2 — "Keep the lights on, cheaper" (same ref): "the lights" is an abstraction two readers would gloss differently — all production infrastructure, the public API, or on-call load.
- PL1 O3=2 — "Keep the lights on, cheaper" (same ref): the quarter is inherited unambiguously from "## Platform team — Q3 2026" (line 3), but keeping the lights on is an open-ended standing duty crammed into a cycle, so it can be neither achieved nor failed within Q3.
- PL2 O3=3 — "Earn enterprise trust" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 12`): period not restated in the objective, inherited unambiguously from the page heading "## Platform team — Q3 2026" (line 3).

Key results (K1–K5 per KR; K6–K7 per KR set):

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR |
|---|---|---|---|---|---|---|
| PL1.1 Maintain API uptime | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 Cloud spend per 1,000 tx | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 Developer satisfaction | 1 | 4 | 2 | 3 | 1 | 2.2 |
| PL2.1 Pen-test findings closed | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 SOC 2 Type II audit | 0 | 1 | 2 | 3 | 2 | 1.0 (capped: K1=0) |

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 3 | 3 |

Spans driving each score ≤ 3:

- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`): metric, target and unit present; baseline absent from the KR but retrievable from "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`); measurement window unstated.
- PL1.1 K3=1 — same two quotes: sandbag, see §3 AP-06.
- PL1.1 K4=3 — team named and the individual is derivable from the same page: "Owner: Elena R." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 4`). Same basis for K4=3 on every KR below.
- PL1.1 K5=3 — the KR names no source, but the corpus names one obvious system of record for this exact metric: "(Datadog SLO monitor)" (line 21).
- PL1.2 K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`): metric, baseline, target, unit and denominator all present; measurement window unstated.
- PL1.2 K3=3 — same quote: a stretch (a ~22% unit-cost cut) with no stated justification or mechanism; labelled committed by "KRs are committed unless marked (aspirational)." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 5`).
- PL1.2 K5=2 — same quote: plausibly measurable but the source is unnamed, and a cloud billing console and a transaction counter would each give a different denominator.
- PL1.3 K1=1, K3=2, K5=1 — "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`): a qualitative state dressed as a metric with no defined score; no baseline anywhere in the corpus, so K3 is capped at 2 and calibration is unverifiable; the data collection does not exist and no KR builds it. See §3 AP-09.
- PL2.1 K1=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`): metric, baseline ("currently 7 open"), target and population all present; measurement window unstated.
- PL2.1 K2=3 — same quote: closing High findings is a proxy output whose link to enterprise trust is credible but never stated in the text.
- PL2.1 K3=3 — same quote: 7 open → 0 is a real stretch, justification absent.
- PL2.1 K5=2 — same quote: no tracker, scanner, or report of record is named for pen-test findings anywhere in the corpus.
- PL2.2 K1=0, K2=1, K3=2, K5=2 — "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`): nothing countable, a pure done/not-done milestone; a delivery milestone as the measure; no baseline or target exists to calibrate, so K3 is capped at 2; the report of record is unnamed. See §3 AP-01.
- PL1 K6=2 — the set is three end-state truths ("Maintain API uptime at or above 99.9%.", line 8; "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", line 9; "Improve internal developer satisfaction score to 8/10.", line 10) with no leading indicator that predicts any of them mid-quarter.
- PL1 K7=2 — "Improve internal developer satisfaction score to 8/10." (line 10) is an orphan against "Keep the lights on, cheaper" (line 7); see §3 AP-09's `Also:` line.
- PL2 K6=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) does lead "Complete the SOC 2 Type II audit." (line 14), but the pairing is nowhere stated in the text.
- PL2 K7=3 — one coverage gap: both KRs are compliance artifacts; nothing in the set measures anything an enterprise customer actually experiences, so "Earn enterprise trust" (line 12) can be fully hit while trust is unchanged.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: no survey, dashboard, or instrument that could produce an "internal developer satisfaction score" appears anywhere in the corpus — searched the entire source file (the Platform OKR page, lines 3–16, and the Q2 2026 business review appendix, lines 18–23), whose only named instrument is the "(Datadog SLO monitor)" for uptime (line 21) — so the 8/10 can never be honestly scored; it also states no current value, leaving both ambition and progress unjudgeable, and its success would not move "Keep the lights on, cheaper" (line 7), whose other two KRs measure uptime and unit cost.
- Scores affected: K1=1, K3=2 (capped, unverifiable), K5=1, K7=2 (PL1 set)
- Suggested rewrite: "KR: Internal-developer satisfaction with Platform services, quarterly survey on `<named survey instrument>` (n ≥ `<respondents>`): `<baseline>`/10 → 8/10" plus a companion KR "Survey instrument live and first wave fielded by `<date>`", and move both under a new "Objective PL3: Internal developers stop working around the platform" rather than leaving them under PL1. [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: the team's own Q2 business review records "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`), so the committed target sits *below* the trailing baseline — the KR is already met on the day it is written and permits a reliability regression of 0.05 points while still scoring 100%.
- Scores affected: K3=1, K1=3
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% trailing-90-day (Q2 actual, per the Datadog SLO monitor) → 99.97%, measured monthly on the same Datadog SLO monitor." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input/sample-portfolio.md › Platform team — Q3 2026 › line 7`)
- Why it's a problem: "Keep the lights on" is the Platform team's standing operational duty, achieved by default staffing and stated with no delta, so the objective sets no goal on its reliability half and takes an OKR slot the quarter's real work could occupy; only "cheaper" carries any change, and the objective's open-endedness also means it can neither be achieved nor failed inside Q3.
- Scores affected: O1=2, O2=2, O3=2
- Suggested rewrite: "Objective PL1: Serving a transaction costs materially less than it did in Q2, and customers cannot tell the difference." Keep the cost KR as-is, move the standing uptime duty out of the OKRs into a health-metric section as a guardrail at the quoted 99.95% trailing-90-day level, and reclaim the freed slot for the quarter's actual bet. [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable, not a measured result — it begins with "Complete", names no metric and no baseline→target pair — and because it is a single done/not-done event it can only ever score 0% or 100%, so it gives no mid-quarter signal about whether the audit is on track and no partial credit for the evidence work the page says the quarter is spent on.
- Scores affected: K1=0, K2=1, K3=2 (capped, unverifiable), K5=2
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence controls closed `<baseline>`/`<total>` → `<total>`/`<total>`, observation window opened by `<date>`, and the auditor's Type II report received by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** The Platform team defers unnamed other teams' infrastructure requests out of the quarter; whether any other team's Q3 OKRs depend on that work cannot be checked with one team in scope.
- "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** A full-capacity declaration that leaves no room for cross-team asks; confirming or refuting contention would require the counterparty teams' OKRs.

## 5. Prioritized action list

1. Rewrite KR PL1.3 around a named survey instrument with a stated baseline, or drop it from Q3 — owner: Platform lead (Elena R., page owner) (resolves §3 AP-09 Metric Nobody Can Measure).
2. Re-baseline KR PL1.1 against the quoted 99.95% trailing-90-day figure and set a target above it — owner: Platform lead (Elena R., page owner) (resolves §3 AP-06 Sandbagged Target).
3. Replace the binary SOC 2 KR with a graded evidence-closure count plus dated audit milestones — owner: Platform lead with the compliance/security owner (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Reframe Objective PL1 around the cost change and move the standing uptime duty to a health-metric section outside the OKRs — owner: Platform lead (Elena R., page owner) (resolves §3 AP-10 BAU Dressed as OKR).
5. Name the system of record for cloud spend per 1,000 transactions and for pen-test findings on the OKR page — owner: Platform lead (addresses K5=2 on PL1.2 and PL2.1, §2).
6. Add one KR to Objective PL2 that measures enterprise-experienced trust rather than a compliance artifact — owner: Platform lead with the enterprise account owner (addresses K7=3 on the PL2 set, §2).
7. State the measurement window on every KR (weekly, monthly, or end-of-quarter) — owner: Platform lead (addresses K1=3 on PL1.1, PL1.2 and PL2.1, §2).
8. Circulate the two deferral statements in §4 to the teams whose Q3 work touches Platform infrastructure and confirm nothing is blocked — owner: Platform lead (resolves §4 outbound dependency notes).
9. Obtain the company Q3 priorities page and re-score O4 for both objectives — owner: Platform lead (resolves the §2 O4 gap note).
