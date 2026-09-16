# OKR-Ninja single-team report — Platform (Q3 2026)

## 1. Verdict summary

**Verdict: Needs work — team roll-up C (2.15); PL1 is graded D and cannot be trusted as written.**
Mode: single-team (1 team in confirmed scope: Platform; period: Q3 2026 as the page states; source: local OKR export).
Findings: 1 Critical, 2 Major, 0 Minor.
Worst finding: AP-09 Metric Nobody Can Measure. PL1.3's developer satisfaction score has no instrument and no baseline anywhere in the source, and it does not serve its objective.
The two Major findings: AP-06 Sandbagged Target (the uptime target sits below the quoted Q2 actual) and AP-01 Task Masquerading as KR (the SOC 2 KR is a done/not-done milestone).
Objective grades: PL1 D (1.9) · PL2 C (2.4).
Company-level strategy tracing was out of scope: no strategy document was provided. O4 Strategic Anchoring is therefore N/A and left out of the roll-up.
Recommended first action: define the developer-satisfaction instrument and baseline, and move that KR out of PL1.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grade (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15).
- PL1 scores D (1.9): the weighted score of 2.65 is capped at 1.9 by the Critical AP-09 Metric Nobody Can Measure on PL1.3.
- PL2 scores C (2.4): the weighted score of 2.52 is capped at 2.4 by two Major anti-patterns on PL2.2.
- Team caps checked: K1 ≤ 1 on 2 of 5 KRs, which is not more than half. The strategy cap does not apply because there is no strategy corpus.
- Platform: K1=2 — SOC 2 KR is a pure milestone (K1=0); satisfaction score undefined (K1=1).

**O4 = N/A — gap note:** no company or portfolio strategy source exists in the corpus. Searched: the Platform team section (lines 3–16) and the Q2 business-review appendix (lines 18–23). Neither objective states a parent, so strategic anchoring could not be scored.

**Per-instance breakdown**

Objectives (O1 · O2 · O3 · O4):
- **PL1** "Keep the lights on, cheaper" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7)
  - O1=3: "Keep the lights on" is a standing duty. Only "cheaper" names a change, and PL1.2 realizes it with a baseline→target pair.
  - O2=3: the idiom "Keep the lights on" names no specific system as its subject.
  - O3=3: the period is inherited from the heading "Platform team — Q3 2026" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 3) and not restated.
  - O4=N/A.
- **PL2** "Earn enterprise trust" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12)
  - O1=4: a changed end-state with no delivery verb.
  - O2=3: "enterprise trust" leaves implicit whose trust is meant, and trust in what.
  - O3=3: the period is inherited from "Platform team — Q3 2026" (line 3).
  - O4=N/A.

Key results (K1 · K2 · K3 · K4 · K5 → per-KR score):
- **PL1.1** "Maintain API uptime at or above 99.9%." (… › Objective PL1: Keep the lights on, cheaper › line 8) → 2.8
  - K1=3: the KR states no baseline. One is retrievable from "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (… › Appendix — Q2 2026 business review (extracts) › line 21). The measurement window is unstated.
  - K2=4.
  - K3=1: the target is below the Q2 actual (see §3 AP-06).
  - K4=3: only the page-level "Owner: Elena R." (… › Platform team — Q3 2026 › line 4); no owner on the KR.
  - K5=3: a system is named only in the appendix, "Datadog SLO monitor" (line 21).
- **PL1.2** "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (… › Objective PL1: Keep the lights on, cheaper › line 9) → 3.0
  - K1=3: the measurement window is unstated.
  - K2=4.
  - K3=3: "from $4.10 to $3.20" is committed under "KRs are committed unless marked (aspirational)." (… › Platform team — Q3 2026 › line 5). No trend or justification is quoted.
  - K4=3: page-level "Owner: Elena R." only.
  - K5=2: no billing or transaction-count system of record is named.
- **PL1.3** "Improve internal developer satisfaction score to 8/10." (… › Objective PL1: Keep the lights on, cheaper › line 10) → 2.2
  - K1=1: the score is undefined and has no baseline.
  - K2=4.
  - K3=2: no baseline anywhere, so calibration is unverifiable (rubric cap).
  - K4=3: page-level "Owner: Elena R." only.
  - K5=1: no survey instrument exists in the corpus.
- **PL2.1** "Close 100% of pen-test findings rated High or above (currently 7 open)." (… › Objective PL2: Earn enterprise trust › line 13) → 2.8
  - K1=3: the baseline "(currently 7 open)" is present. The window is unstated, and so is whether new High findings join the denominator.
  - K2=3: a remediation proxy whose link to trust is carried only by the objective.
  - K3=3: committed, with no trend quoted.
  - K4=3: page-level "Owner: Elena R." only.
  - K5=2: no pen-test report or tracker is named.
- **PL2.2** "Complete the SOC 2 Type II audit." (… › Objective PL2: Earn enterprise trust › line 14) → 1.6, capped at 1.0 because K1=0
  - K1=0.
  - K2=1: a delivery milestone.
  - K3=2: no baseline, so calibration is unverifiable.
  - K4=3: page-level "Owner: Elena R." only.
  - K5=2: nothing defines what counts as "complete", and no audit tracker is named.

KR sets (K6 · K7):
- **PL1:**
  - K6=2: all three KRs are lagging (uptime, cost, satisfaction) and none is a leading indicator.
  - K7=2: one orphan KR, "Improve internal developer satisfaction score to 8/10." (line 10).
- **PL2:**
  - K6=2: both KRs are proxies (remediation, audit), and no lagging KR measures trust itself.
  - K7=3: one coverage gap — no KR measures whether enterprises actually extend "enterprise trust" (line 12).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10)
- Evidence: "Keep the lights on, cheaper" (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: The KR puts a number on an internal state without naming a survey, an instrument, or a current value. I searched the Platform team section (lines 3–16) and the Q2 business-review appendix (lines 18–23); the only measurement system named there is the Datadog SLO monitor for uptime. So the 8/10 can never be honestly scored, and its ambition cannot be judged. On top of that, it sits under an objective about uptime and cost, and higher developer satisfaction would move neither.
- Scores affected: PL1.3 K1=1, K3=2, K5=1; PL1 set K7=2; PL1 roll-up capped at 1.9 (D)
- Suggested rewrite: Remove the KR from PL1 and restate it in a developer-experience objective or a health-metric section as: "KR: Internal developer satisfaction — mean score on `<developer survey instrument>` question `<question>`, run quarterly (n ≥ `<n>`): `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21)
- Why it's a problem: The committed target is below the Q2 actual quoted in the business review. The KR can therefore be met while reliability gets worse than last quarter. A "Maintain" target that the baseline already exceeds is exactly the sandbag pattern.
- Scores affected: PL1.1 K3=1
- Suggested rewrite: "KR PL1.1: API uptime, trailing 90 days per Datadog SLO monitor, from 99.95% (Q2 actual) to ≥ `<target>`% by end of Q3." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: "Complete" names a deliverable with no metric and no baseline→target pair, so the KR restates the work instead of measuring a result. It is also done/not-done: mid-quarter it can only score 0% or 100%, which gives no signal on whether the audit is on track.
- Scores affected: PL2.2 K1=0 (KR score capped at 1.0), K2=1, K3=2; with two Major anti-patterns, PL2 roll-up capped at 2.4 (C)
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II audit findings (baseline: 0/`<N>` closed, per `<audit tracker>`), Type II report received by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (/Users/difan/orca/workspaces/OKR_Reviewer/hawksbill/evals/runs/2026-09-15-smoke-capture-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16) — unverified — counterparty not in scope

## 5. Prioritized action list

1. Define the survey instrument and baseline for the developer-satisfaction KR and move it out of PL1 — owner: Platform page owner (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, with AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Reset the uptime KR's target above the quoted 99.95% trailing-90-day Q2 actual — owner: Platform reliability lead (resolves §3 AP-06 Sandbagged Target).
3. Replace the SOC 2 completion KR with a graded audit-finding closure measure — owner: Platform compliance lead (resolves §3 AP-01 Task Masquerading as KR, with AP-02 Binary KR with No Gradient).
4. Link each objective to the company strategy document so O4 Strategic Anchoring can be scored in a follow-up review — owner: Platform page owner (Elena R.) (resolves §2 O4 N/A gap note).
