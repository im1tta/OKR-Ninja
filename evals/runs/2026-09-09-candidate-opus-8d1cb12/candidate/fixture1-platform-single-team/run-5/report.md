# OKR-Ninja — Single-team review: Platform, Q3 2026

**Scope confirmed at intake:** exactly one team — Platform — for the period the source states, Q3 2026 ("Platform team — Q3 2026", line 3). One team in scope selects **single-team mode**: full-depth goodness scoring of every objective and key result, outbound dependency notes only, and no cross-team (AL-XX) findings.

**Sources searched (the complete corpus for this run):** one local export, `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md` — referred to below as `input/sample-portfolio.md` — containing (a) the Platform OKR page, "Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05" (line 4), and (b) the "Appendix — Q2 2026 business review (extracts)", "Source: Confluence page 88104 (Q2-REVIEW)" (line 19). No Atlassian connection was available and no company or portfolio strategy document was provided; every absence claim below rests on this enumerated search.

---

## 1. Verdict summary

**Verdict: At risk — trustworthy in shape, not in measurement.** Platform's roll-up is **C (2.15)**, but that average hides a split: Objective PL2 lands at C (2.4) while Objective PL1 falls to **D (1.9)** on a Critical cap.
4 findings: **1 Critical, 3 Major, 0 Minor**.
The worst is **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, no baseline, and no system of record anywhere in the corpus, so the KR can never be honestly scored.
Close behind, the quarter's headline reliability KR is a sandbag: the target "at or above 99.9%" sits *below* the 99.95% trailing-90-day actual quoted in the same file (AP-06 Sandbagged Target), and the SOC 2 KR is a binary deliverable with no gradient (AP-01 Task Masquerading as KR · AP-02 Binary KR with No Gradient).
Objective PL1 itself reads as standing duty rather than a goal (AP-10 BAU Dressed as OKR).
**Company-level strategy tracing was out of scope for this run** — no strategy document was provided, so O4 Strategic Anchoring is scored N/A and excluded from the roll-up (gap recorded in §2).
**Recommended first action:** Elena R. rewrites KR PL1.3 against a named survey instrument with a stated baseline — or replaces it with a KR that actually serves PL1 — before the quarter's mid-point review.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (weighted 2.53, capped at 1.9 by a confirmed Critical anti-pattern), Objective PL2 **C (2.4)** (weighted 2.64, capped at 2.4 by two Major anti-patterns on one OKR). Team caps checked and not triggered: 2 of 5 KRs carry K1 ≤ 1 (not more than half); the strategy-trace cap does not apply because no strategy corpus is present.

- Platform: K1=2 — one KR is a bare milestone, another a scoreless satisfaction number.

**O4 = N/A — mandated gap note.** No strategy source exists in the corpus. Searched: the entire provided export (`input/sample-portfolio.md`), covering the Platform OKR page (Confluence 88221) and the Q2 business-review appendix (Confluence 88104); no Atlassian connection and no strategy page were available. Per the rubric, O4 is therefore scored N/A and excluded from every roll-up rather than guessed, and this gap is recorded here in the score section rather than as a §3 finding: neither "Keep the lights on, cheaper" (line 7) nor "Earn enterprise trust" (line 12) states a link to a company priority, and none could be checked.

### Per-instance breakdown

**Objectives**

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 2 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 4 | 3 | N/A |

Quoted spans driving the scores ≤ 3:
- PL1 O1=2 and O2=3 — "Keep the lights on, cheaper" (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 7). Half the objective is a standing state with no delta ("Keep the lights on") and only "cheaper" names a change in the world, so it sits below the outcome anchors; the same idiom is the one abstraction two readers would gloss differently, holding O2 short of the memorable-and-specific anchor.
- PL1 O3=3 and PL2 O3=3 — the period is inherited unambiguously from the page heading "Platform team — Q3 2026" (`input/sample-portfolio.md` › Platform team — Q3 2026 › line 3) but is restated in neither objective.
- PL2 O1=4 and O2=4 — "Earn enterprise trust" (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 12): a changed end-state for a named audience, no delivery verb, three words, no metric baked in.

**Key results** (per-KR score = mean(K1..K5), caps applied after)

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 Maintain API uptime | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 Cloud spend per 1,000 transactions | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 Developer satisfaction | 1 | 4 | 2 | 3 | 1 | 2.2 |
| PL2.1 Pen-test findings | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 SOC 2 Type II | 0 | 1 | 2 | 3 | 2 | 1.0 (capped from 1.6 — K1=0) |

Quoted spans driving the scores ≤ 3:
- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 8): metric, target and unit are present and the baseline is retrievable from a cited source in the same corpus, "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 21), but the KR states no measurement window of its own.
- PL1.1 K3=1 — same two quotes: the target sits below the quoted trailing actual (AP-06, §3).
- PL1.1 K5=3 — the metric's system of record is not named in the KR but is a standard one identified elsewhere in the corpus: "(Datadog SLO monitor)" (line 21).
- PL1.2 K1=3 and K3=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 9): named metric, numeric baseline, numeric target and unit, but no measurement window; the ~22% reduction is a clear stretch off a stated baseline with no justification written down.
- PL1.2 K5=2 — same quote: no dashboard, query or finance system of record is named for cloud spend or for the transaction denominator, and the corpus names none; cloud billing and a finance ledger would give different numbers.
- PL1.3 K1=1, K3=2, K5=1 — "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 10): a qualitative state dressed as a metric with no defined score, no baseline anywhere in the searched corpus (K3 held at the unverifiable-calibration cap), and a measurement that would require data collection that does not exist, with no KR or task in the set to build it.
- PL2.1 K1=3, K2=3, K3=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 13): metric, defined population, baseline "(currently 7 open)" and target are all present but no measurement window is stated; closure of High findings is a proxy whose link to the objective's trust outcome is carried by the objective rather than by the KR; and full closure of a stated 7-item backlog is a properly-committed modest stretch under "Commitment: KRs are committed unless marked (aspirational)." (`input/sample-portfolio.md` › Platform team — Q3 2026 › line 5).
- PL2.1 K5=2 — same quote: the pen-test report, a security backlog and a ticket tracker are all plausible sources, none is named here or anywhere in the corpus.
- PL2.2 K1=0, K2=1, K3=2, K5=2 — "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 14): nothing countable, a pure done/not-done milestone; the measure is delivery of an audit, not a result anyone outside the team experiences; with no numbers at all, calibration is unverifiable and held at the cap; and no system of record for audit completion is named.
- All five KRs K4=3 — "Owner: Elena R." (`input/sample-portfolio.md` › Platform team — Q3 2026 › line 4): the owning team's page names one individual, derivable from the same source, but no KR carries its own accountable owner.

**KR sets**

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1, PL1.2, PL1.3) | 2 | 2 |
| PL2 (PL2.1, PL2.2) | 2 | 3 |

- PL1 K6=2 — "Maintain API uptime at or above 99.9%.", "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." and "Improve internal developer satisfaction score to 8/10." (lines 8–10) are all end-state measures; nothing in the set is a leading indicator that predicts any of them.
- PL1 K7=2 — "Improve internal developer satisfaction score to 8/10." (line 10) is an orphan against "Keep the lights on, cheaper" (line 7): it serves a different goal from the set's reliability and cost KRs (AP-12, §3).
- PL2 K6=2 — "Close 100% of pen-test findings rated High or above (currently 7 open)." and "Complete the SOC 2 Type II audit." (lines 13–14) are both compliance inputs; the set contains no lagging measure of the trust they are meant to predict.
- PL2 K7=3 — one coverage gap against "Earn enterprise trust" (line 12): both KRs measure security evidence, none measures whether enterprises actually came to trust Brightledger.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 10)
- Evidence (objective the KR is meant to serve): "Keep the lights on, cheaper" (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 7)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: "internal developer satisfaction score" names no survey, instrument or dashboard, and the searched corpus (the Platform OKR page and the Q2 business-review appendix) contains none, so no system of record could report the number as defined and the KR can never be honestly scored; it also states a target with no "from", leaving both ambition and progress unjudgeable; and its success would not move "Keep the lights on, cheaper" — the KR shares no nouns or domain with the objective's reliability and cost end-states and no causal chain of two steps or fewer connects them.
- Scores affected: K1=1, K5=1, K3=2, K7=2
- Suggested rewrite: re-home the measure under a platform-experience objective and instrument it — "KR: Internal developer satisfaction, quarterly Platform survey on `<named survey instrument>`, n ≥ `<30>` engineers: `<baseline>`/10 → 8/10, reported from `<dashboard of record>`." If it stays under PL1, replace it with a KR the objective actually needs — "KR: Unplanned infra toil per on-call week: `<baseline>` h → `<target>` h (source: `<on-call tracker>`)." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 7)
- Evidence (the standing duty restated as the set's first KR): "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 8)
- Why it's a problem: "Keep the lights on" is the team's routine operational duty presented as a goal — it is achieved by default staffing and states no delta, so it displaces a real goal for a quarter the team already calls fully committed; only the "cheaper" clause proposes a change in the world.
- Scores affected: O1=2, O2=3
- Suggested rewrite: "Objective PL1: Each transaction costs Brightledger measurably less to serve, with no customer-visible loss of reliability — KR: cloud spend per 1,000 transactions $4.10 → $3.20 (already stated, line 9). Move the standing availability duty out of the OKRs into a health-metrics section: API uptime ≥ 99.95% trailing 90 days, Datadog SLO monitor (baseline quoted, line 21)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence (baseline, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 21)
- Why it's a problem: the target is at or below the actual the corpus already reports — 99.9% is lower than the 99.95% trailing-90-day figure — so the KR is met on the quarter's first day by changing nothing, and it quietly licenses a reliability regression rather than committing to a result.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime, trailing 90 days per the Datadog SLO monitor: 99.95% (Q2 actual, line 21) → `<99.98%>`, with no Sev-1 exceeding `<30>` minutes." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and states no metric and no baseline-to-target pair — it measures that work happened, not a result; and because it is done or not done, mid-cycle scoring can only read 0% or 100%, so the team gets no steering signal and no partial credit for the evidence work the page itself says the quarter is spent on.
- Scores affected: K1=0, K2=1, K6=2
- Suggested rewrite: "KR PL2.2: SOC 2 Type II controls operating with evidence collected: `<0>`/`<42>` → `<42>`/`<42>` controls at `<90>` days of evidence, auditor fieldwork closed and the Type II report received by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

Single-team mode produces no AL-XX alignment findings — one team cannot supply both sides' verbatim quotes — so each cross-team mention below is recorded as a note only, with no severity.

- **Capacity freeze on other teams' infra requests** — "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 16). Platform declares its quarter closed to non-critical infra work from elsewhere in the company. No counterparty is named in Platform's material, and whether any other team's plan depends on that work was not checked. **Unverified — counterparty not in scope.**

No other cross-team dependency mention appears in Platform's own material; the appendix's Payments and Growth lines are other teams' Q2 metrics, not Platform commitments or dependencies.

## 5. Prioritized action list

1. Rewrite KR PL1.3 around a named survey instrument with a stated baseline, or replace it with a KR that serves PL1 — owner: Elena R., Platform lead (resolves §3 AP-09 Metric Nobody Can Measure, AP-04 KR Without Baseline, AP-12 Orphan KR).
2. Reset the uptime KR against the quoted 99.95% trailing-90-day baseline before the quarter's first check-in — owner: Elena R. (resolves §3 AP-06 Sandbagged Target).
3. Convert KR PL2.2 into a graded control-closure measure with an auditor-report date — owner: Elena R. (resolves §3 AP-01 Task Masquerading as KR, AP-02 Binary KR with No Gradient).
4. Recast Objective PL1 as a cost-and-reliability outcome and move the standing availability duty to a health-metrics section outside the OKRs — owner: Elena R. (resolves §3 AP-10 BAU Dressed as OKR).
5. Name the system of record and measurement window for cloud spend per 1,000 transactions and for pen-test findings — owner: Platform metrics owner (resolves §2 K5=2 on PL1.2 and PL2.1, K1=3 windows).
6. Add one leading indicator to each objective — an in-quarter steering signal for cost and for SOC 2 evidence — owner: Elena R. (resolves §2 K6=2 on both KR sets).
7. Add a trust-outcome KR to PL2, such as enterprise security reviews passed without escalation — owner: Elena R. with the enterprise sales lead (resolves §2 K7=3 coverage gap).
8. Attach a named accountable individual to each KR rather than to the page as a whole — owner: Elena R. (resolves §2 K4=3 across all five KRs).
9. Obtain the company Q3 strategy page and re-score O4 for both objectives — owner: Elena R. (resolves §2's O4 = N/A gap note, strategy tracing out of scope this run).
