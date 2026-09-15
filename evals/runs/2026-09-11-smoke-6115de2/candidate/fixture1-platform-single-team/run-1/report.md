# OKR-Ninja — Single-team review: Platform, Q3 2026

*Mode: single-team (exactly one team in confirmed scope — Platform). Period: Q3 2026, as stated by the source page. Source of record: `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md` (Platform team OKR page + Q2 2026 business-review appendix). No Atlassian connection available; no other source consulted.*

## 1. Verdict summary

**Verdict: Needs rework before the quarter can be trusted.** Platform's roll-up grade is **C (2.15)**, but that average hides a Critical measurement defect and one objective that grades **D (1.9)**.
1 team reviewed; **1 Critical, 2 Major, 0 Minor** findings.
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, no baseline and no system of record, so it can never be honestly scored.
Two of five KRs cannot be scored as written (K1=1 and K1=0), and the flagship reliability KR is calibrated *below* the team's own quoted trailing baseline (AP-06 Sandbagged Target).
Objective PL2's key results measure compliance artifacts rather than the enterprise trust the objective claims, and one of them is a pure done/not-done milestone.
The team's commitment convention is stated explicitly ("KRs are committed unless marked (aspirational)."), so labeling hygiene is *not* a defect here.
**Company-level strategy tracing was out of scope for this run:** no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored N/A per the rubric and excluded from the roll-up (see §2).
**Recommended first action:** rewrite KR PL1.3 against a real instrument and reset the uptime target above the quoted 99.95% baseline — owner: Platform lead (Elena R.), before the Q3 mid-cycle check-in.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (weighted 2.47, capped at 1.9 by a confirmed Critical anti-pattern); Objective PL2 **C (2.4)** (weighted 2.42, capped at 2.4 by ≥2 Major anti-patterns on one OKR).
- Platform: K5=1 — one KR names no instrument that could ever report it (AP-09 Metric Nobody Can Measure).

**O4 gap note (rubric-mandated):** no company/portfolio strategy source exists in the corpus — the only two documents available are the Platform OKR page and the Q2 2026 business-review appendix, and neither states a company priority, pillar, or bet. O4 is therefore **N/A** for both objectives and excluded from the roll-up means; neither objective's strategic anchoring was guessed. Search trail: every line of `sample-portfolio.md` was read; no strategy page, Confluence space, or Jira project was available (no Atlassian connection), and no other file was in scope for this run.

### Per-instance breakdown

Objective dimensions:

| Instance | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

Key-result dimensions (K1–K5 per KR; per-KR score = mean(K1..K5), with the rubric's K1=0/K5=0 cap applied):

| Instance | K1 | K2 | K3 | K4 | K5 | Per-KR |
|---|---|---|---|---|---|---|
| PL1.1 uptime | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 cloud spend | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 developer satisfaction | 1 | 3 | 2 | 3 | 0 | 1.0 (capped, K5=0) |
| PL2.1 pen-test findings | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 SOC 2 audit | 0 | 1 | 2 | 3 | 2 | 1.0 (capped, K1=0) |

KR-set dimensions:

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 2 | 2 |

**Quoted spans driving every score ≤ 3** (rubric Part 5, rule 2):

- **PL1 O1=3** — "Objective PL1: Keep the lights on, cheaper" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`). No delivery verb, and "cheaper" is a real change in the world, but "Keep the lights on" describes holding a state rather than reaching a new end-state, so it sits below the 4 anchor.
- **PL1 O2=3** — "Objective PL1: Keep the lights on, cheaper" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`). Memorable and short, but the subject is an idiom ("the lights") rather than a specific noun, so it lands between the 4 and 3 anchors and takes the lower.
- **PL1 O3=3 / PL2 O3=3** — "## Platform team — Q3 2026" (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 3`). The period is inherited unambiguously from the page heading and never restated on either objective.
- **PL2 O2=3** — "Objective PL2: Earn enterprise trust" (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`). Short and plain, but "enterprise trust" is an abstraction two readers would gloss differently (security posture? audit paperwork? incident record?).
- **PL1.1 K1=3, K5=3** — "Maintain API uptime at or above 99.9%." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`). Metric, target and unit are present but the KR states no baseline and no measurement window; both are retrievable from the cited corpus line "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`…/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`), which also supplies the single obvious system of record the KR itself fails to name.
- **PL1.1 K3=1** — see §3, AP-06 Sandbagged Target.
- **PL1.2 K1=3** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`). Baseline, target and unit are all stated; only the measurement window is missing.
- **PL1.2 K3=3** — same quote. A 22% unit-cost reduction inside one quarter is clearly a stretch, but no justification, lever, or trend is stated anywhere in the corpus.
- **PL1.2 K5=2** — same quote. Plausibly measurable, but no billing dashboard, finance report, or query of record is named, and "per 1,000 transactions" could be computed from more than one transaction ledger.
- **PL1.3 K1=1, K3=2, K5=0** — see §3, AP-09 Metric Nobody Can Measure.
- **PL1.3 K2=3** — "Improve internal developer satisfaction score to 8/10." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`). Satisfaction of internal developers is experienced outside the Platform team, but it is a proxy with no stated causal link to anything the objective claims.
- **PL1.1/PL1.2/PL1.3/PL2.1/PL2.2 K4=3** — "*Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05*" (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 4`). No KR names its own accountable individual; a single page owner, "Owner: Elena R.", is derivable from the same source for all five.
- **PL2.1 K1=3, K2=3, K3=3, K5=2** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`). The parenthetical supplies both a starting point and a countable denominator, so measurability is sound apart from an unstated window; closure of security findings is a credible proxy for the objective rather than a result enterprises themselves experience; and no tracker or report of record is named, so two systems could disagree on the count.
- **PL2.2 K1=0, K2=1, K3=2, K5=2** — see §3, AP-01 Task Masquerading as KR.
- **PL1 K6=2** — "Maintain API uptime at or above 99.9%." · "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." · "Improve internal developer satisfaction score to 8/10." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › lines 8, 9, 10`). All three are end-state truths; nothing in the set is a leading indicator that predicts another, so the set offers no mid-cycle steering signal.
- **PL1 K7=2** — same three quotes against "Objective PL1: Keep the lights on, cheaper" (line 7). Uptime covers "lights on" and cloud spend covers "cheaper", but the developer-satisfaction KR serves a different goal entirely (see AP-12 on the §3 block for PL1.3) — one orphan KR in the set.
- **PL2 K6=2** — "Close 100% of pen-test findings rated High or above (currently 7 open)." · "Complete the SOC 2 Type II audit." (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › lines 13, 14`). Both are end-of-period compliance truths; neither predicts the other and neither gives a steering signal about trust mid-quarter.
- **PL2 K7=2** — same two quotes against "Objective PL2: Earn enterprise trust" (line 12). Hitting both would prove the audit closed and the findings were remediated, not that enterprises trust Brightledger: nothing in the set measures an enterprise-facing outcome (deals unblocked, security-review turnaround, enterprise renewal), and one of the two KRs carries no gradient at all.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: no "internal developer satisfaction score" is defined anywhere in the corpus — no survey, instrument, cadence, population, or system of record — so the 8/10 quantifies an internal state that nothing could honestly report at quarter end; on top of that the KR states no current value, and its success would not move an objective about uptime and cloud cost. Search trail for the absence claims: both documents in scope were read in full — the Platform OKR page (lines 3–16) and the Q2 2026 business-review appendix (lines 18–23); the appendix names a system of record only for uptime ("Datadog SLO monitor"), and no satisfaction survey, baseline, or tool appears in either; no Atlassian source was available.
- Scores affected: K1=1, K5=0, K3=2 (unverifiable-calibration cap), K7=2 (orphan KR in the PL1 set), per-KR score capped at 1.0, PL1 capped at D (1.9)
- Suggested rewrite: move the measure onto a real instrument and onto the objective it actually serves — "KR PL1.3: Platform-caused developer downtime — engineer-hours blocked on infra incidents and failed builds, from `<CI/incident dashboard>`, weekly — `<baseline>` → `<target>` hours/week, so the cost work does not come out of other teams' throughput." If the team wants to keep a satisfaction measure, it needs its own objective and an instrument that exists: "KR: Internal developer survey (quarterly, n ≥ `<respondents>`, `<named survey tool>`): satisfaction `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target, 99.9%, sits *below* the team's own quoted trailing-90-day actual of 99.95%, so the KR can be hit while reliability degrades by roughly 0.05 percentage points — it encodes permission to get worse rather than an ambition, which is exactly the "maintain … at or above" pattern the anti-pattern names. Because both ends of the comparison are quoted from different documents, the claim rests on no inferred number.
- Scores affected: K3=1, K6=2 (the set's only reliability signal carries no ambition), PL1 roll-up
- Suggested rewrite: "KR PL1.1: API uptime (Datadog SLO monitor, trailing 90 days) 99.95% → `<target ≥ 99.97>`%, with the error budget for the quarter stated explicitly and breached-budget freezes agreed in advance." [proposal — placeholder target] If holding 99.95% while the cost work lands is genuinely the intent, say so as a guardrail rather than as a key result: "Guardrail (not a KR): uptime does not fall below 99.95% (Datadog SLO monitor) while cloud spend per 1,000 transactions is reduced."

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb plus a deliverable with neither a baseline→target pair nor any measure someone outside Platform moves, so it restates the work instead of measuring a result; and because it is a single done/not-done event, mid-cycle scoring can only ever read 0% or 100%, which tells the quarter nothing until it is over. Its sibling KR shows the contrast: "Close 100% of pen-test findings rated High or above (currently 7 open)." (same page, line 13) states a starting point over a countable population and is progress-measurable all quarter.
- Scores affected: K1=0, K2=1, K6=2, K7=2, per-KR score capped at 1.0, PL2 capped at C (2.4)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence collection `<0>`/`<N>` → `<N>`/`<N>` controls evidenced and accepted by the auditor, Type II report received by `<date>`; enterprise deals blocked on a missing SOC 2 report `<baseline>` → 0." [proposal — placeholder target] To close the coverage gap the PL2 set leaves (K7=2), add an enterprise-facing outcome KR: "KR PL2.3: Enterprise security reviews cleared without escalation `<baseline>` → `<target>` per quarter, median turnaround `<baseline>` → `<target>` days." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Notes: Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/runs/2026-09-11-smoke-6115de2/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** Platform declares its quarter fully allocated and defers non-critical infrastructure requests to Q4; any other team whose Q3 plan assumes Platform capacity is affected, but no counterparty's OKRs are in scope for this run, so no cross-team finding is made and no severity is assigned.

No other cross-team dependency mention appears in Platform's own material. (The appendix's Payments and Growth lines are business-review extracts, not Platform dependencies, and are not treated as such here.)

## 5. Prioritized action list

1. Replace KR PL1.3 with a measure that has an existing instrument and serves an objective it can actually move — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, incl. AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Reset the uptime KR against the quoted 99.95% trailing baseline, or demote it to an explicit guardrail — owner: Platform lead (Elena R.) with the SRE on-call owner (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a graded evidence-closure measure with a received-report date — owner: Platform compliance/SOC 2 workstream lead (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Add one enterprise-facing outcome KR to Objective PL2 so the set can prove trust rather than paperwork — owner: Platform lead (Elena R.) (resolves §2 PL2 K7=2, K6=2).
5. Name the system of record and measurement window on every KR — the cloud-spend billing source, the pen-test findings tracker, the SOC 2 report — owner: Platform lead (Elena R.) (resolves §2 K5=1, PL1.2 K5=2, PL2.1 K5=2, PL2.2 K5=2).
6. Name a per-KR accountable individual rather than relying on the single page owner — owner: Platform lead (Elena R.) (resolves §2 K4=3 across all five KRs).
7. Raise the Q3 capacity note with the teams it affects, since Platform has declared non-critical infra requests deferred to Q4 — owner: Platform lead (Elena R.) (resolves §4 outbound dependency note; unverified, counterparty not in scope).
8. Obtain the company/portfolio strategy document and re-run this review so O4 Strategic Anchoring can be scored rather than left N/A — owner: Platform lead (Elena R.) (resolves §2 O4 gap note).

---

*Scope and method notes: single-team mode was selected because exactly one team (Platform) was in confirmed scope; per `SKILL.md` Step 4, no cross-team alignment analysis was performed and no AL-XX finding appears in this report. Every quote above was re-verified character-for-character against the source file before the report was written. Company-level strategy tracing was out of scope — no strategy document was provided — so O4 is N/A with the rubric's gap note recorded in §2. Intentional non-defects checked and deliberately not filed: AP-08 Committed vs Aspirational Not Labeled does not fire, because the page states a commitment convention — "Commitment: KRs are committed unless marked (aspirational)." (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 5`); AP-10 BAU Dressed as OKR does not fire on "Objective PL1: Keep the lights on, cheaper" (line 7), because the objective names a change ("cheaper") and a KR pays for it with a baseline→target pair — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9); AP-04 KR Without Baseline does not fire on "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13), whose parenthetical states the starting point over a countable population, which also keeps AP-01 and AP-13 silent there; AP-05 Everything Is a P0 does not fire — two objectives, no uniform priority labels. This is an eval run: no artifact was published and no registry file was created or modified.*
