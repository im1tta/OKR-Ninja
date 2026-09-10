# OKR-Ninja — Single-team review: Platform, Q3 2026

**Mode:** single-team (exactly one team in confirmed scope → depth, not breadth). **Period:** Q3 2026, as stated by the source page. **Source (canonical, and the only source consulted):** `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md` — the Platform OKR page (lines 3–16) and the Q2 2026 business-review appendix (lines 18–23). No Atlassian source was available; no company/org strategy document was provided. Per single-team mode, no cross-team (AL-XX) analysis was performed.

---

## 1. Verdict summary

**Verdict: Usable but flawed — roll-up C (2.15).** The set can be run this quarter, but one key result cannot be honestly scored at all and two others measure completion rather than a result.

- 1 team reviewed; 2 objectives and 5 key results scored exhaustively. Findings: **1 Critical, 3 Major, 0 Minor**.
- Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no survey, dashboard, or instrument anywhere in the corpus, so it can never be scored honestly.
- Next worst: **AP-06 Sandbagged Target** — the uptime KR targets 99.9% while the same corpus reports a trailing-90-day actual of 99.95%; the target is achieved by doing nothing.
- Objective PL1 presents the team's standing duty as a goal (**AP-10 BAU Dressed as OKR**); PL2's SOC 2 key result is a task with no gradient (**AP-01 Task Masquerading as KR**, also **AP-02 Binary KR with No Gradient**).
- The healthier half is the objectives' framing and two key results — PL2 "Earn enterprise trust" is a clean outcome statement, and KR PL1.2 and KR PL2.1 both carry a stated baseline and target.
- **Company-level strategy tracing was out of scope:** no strategy document was provided and none exists in the corpus, so **O4 Strategic Anchoring is scored N/A** for both objectives and excluded from the roll-up (rubric Part 1, O4). See the gap note in §2.
- Recommended first action: replace KR PL1.3 with a measurable KR that has a named instrument and a baseline, before the quarter's mid-point check-in.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — mean of OKR PL1 **D (1.9)** and OKR PL2 **C (2.4)**.
- Platform: K1=2 — two of five KRs state a target with no usable baseline or no countable metric at all (AP-09, AP-01/AP-02).

**O4 gap note (rubric-mandated, recorded here and not as a finding):** O4 Strategic Anchoring is **N/A** for both objectives and excluded from every mean, because no strategy source exists in the corpus. Search performed: the entire supplied file — the Platform OKR page (lines 3–16, including the source/owner line 4, the commitment line 5, both objective blocks, and the notes line 16) and the Q2 2026 business review appendix (lines 18–23). Neither objective states a parent ("Keep the lights on, cheaper" and "Earn enterprise trust" carry no link text), and no company priority, pillar, or bet appears anywhere in the corpus. No Atlassian connection was available and no other source was consulted. The gap is real: as written, neither objective can be traced to a company priority by a reader of this page.

### Per-instance breakdown (dimensions whose scores vary)

**Objectives**

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 2 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 4 | 3 | N/A |

- PL1 O1=2 — "Keep the lights on, cheaper" (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): the first clause names no changed end-state, only the team's standing duty; only "cheaper" is a delta, so the outcome is half-present. See §3 AP-10.
- PL1 O2=3 — "Keep the lights on, cheaper" (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): memorable, plain and under 15 words, but it is an idiom with no specific noun subject — one small, identifiable gap.
- PL1 O3=3 and PL2 O3=3 — the period is inherited unambiguously from "## Platform team — Q3 2026" (`.../input/sample-portfolio.md › Platform team — Q3 2026 › line 3`) and is not restated in either objective.
- PL2 O1=4 / O2=4 — "Earn enterprise trust" (`.../input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`): a changed end-state with no delivery verb, achievable by routes other than the one the KRs name; three words, plain language, specific subject, no metric embedded.

**Key results**

| KR | K1 | K2 | K3 | K4 | K5 | per-KR |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." | 1 | 4 | 2 | 3 | 1 | 2.2 |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 "Complete the SOC 2 Type II audit." | 0 | 1 | 2 | 3 | 2 | 1.0 (capped: K1=0) |

- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`): metric, target and unit are present and the missing baseline is retrievable from a cited source in the same corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`.../input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`). The measurement window is unstated. Because the baseline **is** retrievable, AP-04 KR Without Baseline does not fire here.
- PL1.1 K3=1 — sandbag; see §3 AP-06.
- PL1.1 K5=3 — the metric names no source itself, but the corpus shows a single obvious system of record: "(Datadog SLO monitor)" (`.../input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`).
- PL1.2 K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`): metric, numeric baseline, numeric target and unit all present; measurement window unstated.
- PL1.2 K3=3 — a properly-labelled committed KR ("Commitment: KRs are committed unless marked (aspirational)." — `.../input/sample-portfolio.md › Platform team — Q3 2026 › line 5`) at a stated stretch from a stated baseline, with no justification of the size given.
- PL1.2 K5=2 — plausibly measurable, but "cloud spend per 1,000 transactions" (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`) names no system of record and none appears in the corpus; a billing export and a transaction count from different systems would give different numbers.
- PL1.3 K1=1, K3=2, K5=1 — see §3 AP-09. K3 is capped at 2 because no baseline or trend for this metric exists anywhere in the corpus, so calibration is unverifiable.
- PL2.1 K1=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`.../input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`): the population is explicitly bounded ("rated High or above", baseline "currently 7 open"), so the percentage has a defined denominator and AP-13 Ambiguous Denominator does not fire; the measurement window is unstated.
- PL2.1 K2=3 — closing findings is a remediation output, credibly linked to the objective's trust outcome but not itself experienced outside the team.
- PL2.1 K3=3 — clearing the full known backlog is a stretch, but no trend or prior-period closure rate is quoted anywhere in the corpus to size it against.
- PL2.1 K5=2 — the pen-test finding register is unnamed and no tracker appears in the corpus.
- PL2.2 K1=0, K2=1, K5=2 — see §3 AP-01. K3=2 by the unverifiable-calibration cap (no baseline or trend anywhere in the corpus).
- K4=3 for all five KRs — no KR names an individual, but one is derivable from the same source: "Owner: Elena R." (`.../input/sample-portfolio.md › Platform team — Q3 2026 › line 4`). AP-15 Ownerless KR therefore does not fire.

**KR sets**

| KR set | K6 | K7 |
|---|---|---|
| PL1 | 2 | 2 |
| PL2 | 2 | 2 |

- PL1 K6=2 — uptime, cost per transaction and a satisfaction score are three independent end-state truths; nothing in the set is a leading indicator that predicts another, and no causal pairing is stated.
- PL1 K7=2 — "Improve internal developer satisfaction score to 8/10." (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) is an orphan serving a different goal than "Keep the lights on, cheaper" (`.../input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`), and the reliability clause is covered only by a target below its own baseline.
- PL2 K6=2 — both KRs measure compliance completion; neither is a leading indicator of enterprise trust, and any link between closing pen-test findings and passing the audit is nowhere stated.
- PL2 K7=2 — "Earn enterprise trust" (`.../input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`) has no KR touching whether enterprise customers actually trust the product (deals, renewals, security-review outcomes), and "Complete the SOC 2 Type II audit." (`.../input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`) records an event rather than a facet of trust — two gaps.

**Set-level anti-patterns checked and not fired:** AP-08 Committed vs Aspirational Not Labeled does not fire — the page states a convention: "Commitment: KRs are committed unless marked (aspirational)." (`.../input/sample-portfolio.md › Platform team — Q3 2026 › line 5`). AP-05 Everything Is a P0 does not fire — the team has 2 objectives and no priority labels at all.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence (objective this KR sits under): "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: the "internal developer satisfaction score" names no survey, instrument, or system of record, and none exists anywhere in the corpus, so the 8/10 can never be honestly scored; it also states no current value, so ambition and progress are both unjudgeable, and satisfaction moves neither of the objective's two clauses — uptime and cost per transaction — so hitting it would not move "Keep the lights on, cheaper".
- Search performed for the absent instrument and baseline: the whole supplied file — the Platform OKR page (lines 3–16) and the Q2 2026 business review appendix (lines 18–23, whose only Platform line is the Datadog uptime figure). No Atlassian connection was available and no other source was consulted.
- Scores affected: K1=1, K5=1, K3=2 (unverifiable-calibration cap), K7=2 (PL1 set)
- Suggested rewrite (replaces the orphan with a KR that serves this objective): "KR PL1.3: Developer time lost to platform incidents and failed builds, from `<dashboard>`: `<baseline>` hours/month → `<target>` hours/month, measured monthly through Q3 2026." [proposal — placeholder target] If the team wants to keep a satisfaction measure, move it under its own developer-experience objective and name the instrument: "KR: Internal developer satisfaction, quarterly platform survey run in `<survey tool>` (n ≥ `<respondents>`): `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Evidence (the standing duty restated as its first KR): "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: "Keep the lights on" is the team's routine operational duty presented as a goal — it states no delta and is achieved by default staffing — so only the "cheaper" clause carries a real end-state, and the objective's headline commits a quarter of attention to work that would happen anyway.
- Scores affected: O1=2
- Suggested rewrite: "Objective PL1: Every 1,000 transactions costs measurably less to serve, with no reliability regression customers can feel." [proposal] Move the uptime floor out of the OKRs into a standing SLO health-metric section, where a target at or near the current level is the correct thing to state.

### [Major] AP-06 Sandbagged Target — Platform
- Evidence (OKR side): "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline side, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target of 99.9% sits **below** the trailing-90-day actual of 99.95% reported in the same document, so the KR is already met on the day it is written and encodes no ambition; scoring it green at quarter end would tell leadership nothing.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.98%, monthly SLO attainment through Q3 2026." [proposal — placeholder target] (The 99.95% baseline is quoted from line 21; 99.98% is a placeholder for the team to set.)

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable, not a result — it begins with "Complete", names no metric and no baseline→target pair, so it succeeds on the audit being finished rather than on any trust being earned; and because it is done/not-done, mid-cycle scoring can only read 0% or 100%, leaving the team blind to whether the objective is on track until the quarter is over.
- Scores affected: K1=0, K2=1, K6=2 (PL2 set), K7=2 (PL2 set); per-KR score capped at 1.0 by the K1=0 cap
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II control gaps (baseline: `<M>`/`<N>` closed as of 2026-07-05), with the Type II report issued by `<audit firm>` no later than `<date>`." [proposal — placeholder target] Pair it with a trust outcome so the set measures the objective: "KR PL2.3: Enterprise security reviews passed without a remediation condition: `<baseline>` → `<target>` per quarter." [proposal — placeholder target]

## 4. Outbound dependency notes

Single-team mode produces no AL-XX alignment findings — the taxonomy's both-sides quote rule cannot be met with one team in scope. The cross-team mentions found in Platform's material are recorded here as notes only; they carry no severity and are not findings.

- **Note DN-1 — capacity deferral affecting unnamed counterparty teams — unverified — counterparty not in scope.**
  - "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
  - "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-9551238/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
  - Platform declares its quarter fully committed and defers infra requests to Q4. The requesting teams are not named in this material and are not in scope, so whether any other team's Q3 OKR depends on that deferred work is unverified here.

No other cross-team dependency mention appears in Platform's material: no KR or objective names another team, a shared system, or a "depends on" / "blocked by" relationship.

## 5. Prioritized action list

1. Replace KR PL1.3 with a KR that names its instrument and states a baseline, or move the satisfaction measure to its own objective — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, with AP-04 KR Without Baseline and AP-12 Orphan KR).
2. Reset the uptime KR against the 99.95% trailing-90-day figure quoted in the same document — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Rewrite the SOC 2 KR as a graded control-closure count with an issued-report date — owner: Platform lead (Elena R.) (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Reframe Objective PL1 around the cost delta and move the uptime floor into a standing SLO health-metric section outside the OKRs — owner: Platform lead (Elena R.) (resolves §3 AP-10 BAU Dressed as OKR).
5. Add a trust-outcome KR to Objective PL2 so the set would convince a skeptic the objective happened — owner: Platform lead (Elena R.) (raises §2 K7=2 and K6=2 on the PL2 set).
6. Name the system of record and measurement window for cloud spend per 1,000 transactions and for the pen-test finding register — owner: Platform lead (Elena R.) (raises §2 K5=2 on KR PL1.2 and KR PL2.1, and K1=3 on both).
7. Circulate the Q4 deferral to the teams whose infra requests are being held and confirm none of them has a Q3 commitment riding on it — owner: Platform lead (Elena R.) (closes §4 Note DN-1).
