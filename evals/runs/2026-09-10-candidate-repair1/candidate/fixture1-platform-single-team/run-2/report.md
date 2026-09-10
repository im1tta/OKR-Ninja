# OKR-Ninja — Single-team review: Platform, Q3 2026

*Scope confirmed at intake: exactly one team (Platform) → **single-team mode** (full-depth goodness scoring; no cross-team AL-XX findings). Period: Q3 2026, as stated by the source page. Source (canonical, and the only corpus): `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` — the Platform OKR page (lines 3–16) plus the Q2 2026 business-review appendix (lines 18–23). No Atlassian connection available; no strategy document provided.*

## 1. Verdict summary

**Verdict: Needs rework before the quarter can be trusted.** Roll-up grade **C (2.15)**, but Objective PL1 alone grades **D (1.9)** and carries the review's only Critical finding.
Findings: **1 Critical, 2 Major, 0 Minor** across 2 objectives and 5 key results (every objective and KR scored exhaustively).
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10" names no instrument, no scale definition, and no baseline anywhere in the corpus, so it can never be honestly scored.
Also material: the uptime KR targets 99.9% while the same file's Q2 review quotes a trailing-90-day actual of 99.95% (AP-06 Sandbagged Target), and the SOC 2 KR is a pure completion milestone with no gradient (AP-01 Task Masquerading as KR · AP-02 Binary KR with No Gradient).
Two KRs are genuinely sound and should be left alone: PL1.2 (real baseline→target on cost per transaction) and PL2.1 (100% of a stated 7-finding base set).
**Company-level strategy tracing was out of scope for this run:** no company or org strategy document was provided, and none exists in the corpus, so O4 Strategic Anchoring is scored **N/A** for both objectives and excluded from the roll-up per the rubric — no strategic anchoring was guessed.
Recommended first action: the Platform lead either names a real instrument, population, and baseline for the developer-satisfaction KR or drops it from PL1 this week (resolves §3 AP-09).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (weighted mean 2.47, capped at 1.9 by the confirmed Critical anti-pattern AP-09); Objective PL2 **C (2.4)** (weighted mean 2.54, capped at 2.4 by two Major anti-patterns on one OKR). Neither team-level cap applies: 2 of 5 KRs carry K1 ≤ 1 (not more than half), and the strategy-trace cap requires a strategy corpus, which is absent.

- Platform: K1=2, K5=2 — the developer-satisfaction and SOC 2 KRs name no measurable metric or source.

**O4 = N/A — mandated gap note:** no strategy source exists anywhere in the corpus. Search trail: the entire provided corpus is the single file above (23 lines, both sections read in full); a case-insensitive search for `strategy|strategic|company|pillar|bet|priorit` returns no match, and no Atlassian source was connected. Per `references/goodness-rubric.md` O4, both objectives are scored N/A and excluded from the roll-up mean rather than guessed. **Gap:** neither objective states a link to any company or portfolio priority, so nothing in this quarter's Platform plan can be traced up. Recording this here, in the score section, is the rubric's requirement — it is deliberately not filed as a §3 finding block.

### Per-instance breakdown (dimensions whose scores vary)

**Objective PL1 — O1=3, O2=3, O3=3, O4=N/A**
- O1=3 — "Objective PL1: Keep the lights on, cheaper" (`…/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 7). Outcome-framed with no delivery verbs and no named solution, but half of it ("Keep the lights on") asserts the status quo rather than a changed end-state, so it falls short of the 4 anchor.
- O2=3 — same span, line 7. Memorable, under 15 words, no metric embedded; but "the lights" is a metaphor rather than a specific noun subject, leaving the covered systems unnamed.
- O3=3 — period inherited unambiguously from the page heading "## Platform team — Q3 2026" (`…/input/sample-portfolio.md` › ## Platform team — Q3 2026 › line 3) rather than restated in the objective.
- **Not AP-10 BAU Dressed as OKR** (checked and cleared): the objective does assert continuation, but it also names a change — "cheaper" — and KR PL1.2 realizes exactly that change with a baseline→target pair ("from $4.10 to $3.20", line 9), which is the rubric's stated exclusion.

**KR PL1.1 — K1=3, K2=4, K3=1, K4=3, K5=3**
- K1=3 — "**KR PL1.1:** Maintain API uptime at or above 99.9%." (line 8): metric, target, and unit present; the baseline is missing from the KR but retrievable from the cited appendix (line 21), and no measurement window is stated.
- K2=4 — API uptime is a result experienced outside the team.
- K3=1 — sandbag; see §3 AP-06 Sandbagged Target for both quoted ends.
- K4=3 — no per-KR owner; owning team named in the page heading (line 3) and an individual is derivable from the same source: "Owner: Elena R." (line 4).
- K5=3 — the KR names no source, but "Datadog SLO monitor" (line 21) is the single obvious system of record for this metric elsewhere in the corpus.

**KR PL1.2 — K1=3, K2=4, K3=3, K4=3, K5=2**
- K1=3 — "**KR PL1.2:** Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9): named metric, numeric baseline, numeric target, unit — only the measurement window is unstated.
- K3=3 — a properly-labeled committed KR at a modest (~22%) stretch with no justification stated; the commitment label comes from "*Commitment: KRs are committed unless marked (aspirational).*" (line 5).
- K4=3 — as PL1.1.
- K5=2 — plausibly measurable, but no source is named and no cloud-cost or transaction-count system of record appears anywhere in the corpus (search trail: the only measurement system named in the whole file is the Datadog SLO monitor, line 21), so cloud-billing and finance figures could differ.

**KR PL1.3 — K1=1, K2=4, K3=2, K4=3, K5=0 → per-KR score capped at 1.0 (K5=0)**
- See §3 AP-09 Metric Nobody Can Measure for the quoted evidence and search trail. K3=2 applies the rubric's unverifiable-calibration cap (no baseline or trend exists anywhere); K4=3 as PL1.1.

**KR set PL1 — K6=2, K7=2**
- K6=2 — all three KRs are lagging/outcome measures ("Maintain API uptime at or above 99.9%.", line 8; "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", line 9; "Improve internal developer satisfaction score to 8/10.", line 10); none is a leading indicator that predicts another, so the set gives no mid-cycle steering signal.
- K7=2 — one orphan KR that serves a different goal: "Improve internal developer satisfaction score to 8/10." (line 10) touches neither reliability nor cost (see §3, `Also:` AP-12 Orphan KR).

**Objective PL2 — O1=4, O2=4, O3=3, O4=N/A**
- O1=4 / O2=4 — "Objective PL2: Earn enterprise trust" (line 12): a changed end-state for customers, reachable by more than one route, stated as a plain three-word line with a specific audience and no metric embedded.
- O3=3 — period inherited from the page heading (line 3), not restated.

**KR PL2.1 — K1=3, K2=3, K3=3, K4=3, K5=2**
- K1=3 — "**KR PL2.1:** Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13): metric, target, and an explicit baseline ("currently 7 open") over a stated base set; only the window is unstated.
- K2=3 — a proxy output whose causal link to the objective's outcome is credible but stated only via the objective, not on the KR.
- K3=3 — a committed KR at a real stretch (7 open → none) with no justification stated.
- K4=3 — as PL1.1.
- K5=2 — plausibly measurable, but the pen-test report or tracker of record is unnamed and appears nowhere in the corpus (same search trail as PL1.2), so two readers could count "open" differently.
- **Not AP-01 and not AP-13** (checked and cleared): the KR carries a baseline→target pair over a countable denominator, and "(currently 7 open)" pins the population, so neither the task-masquerade trigger nor the ambiguous-denominator trigger fires.

**KR PL2.2 — K1=0, K2=1, K3=2, K4=3, K5=3 → per-KR score capped at 1.0 (K1=0)**
- See §3 AP-01 Task Masquerading as KR. K3=2 applies the unverifiable-calibration cap (no baseline or trend); K4=3 as PL1.1; K5=3 because the external Type II audit report is an unambiguous single record of completion, even though the KR names no metric.

**KR set PL2 — K6=2, K7=2**
- K6=2 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) is a leading security proxy, and "Complete the SOC 2 Type II audit." (line 14) is a binary milestone; the set contains no lagging *outcome* KR for the proxy to predict.
- K7=2 — multiple coverage gaps against "Earn enterprise trust" (line 12): both KRs measure compliance artifacts, and nothing measures anything an enterprise customer does (deals unblocked, renewals, security-review pass rate).

**Set-level anti-patterns checked and cleared (whole page as the instance):**
- **Not AP-08 Committed vs Aspirational Not Labeled** — the page states a convention: "*Commitment: KRs are committed unless marked (aspirational).*" (line 5).
- **Not AP-05 Everything Is a P0** — two objectives, no uniform P0/must-hit labels; the threshold (≥4 uniformly labeled objectives, or >5 unranked objectives) is not met.
- **Not AP-15 Ownerless KR** — K4=3 for every KR: "Owner: Elena R." (line 4) is derivable from the same source.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "**KR PL1.3:** Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 10)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: the KR quantifies an internal state with no instrument — no survey, scale definition, respondent population, or system of record for a "developer satisfaction score" exists anywhere in the corpus (search trail: the whole 23-line file was read; the only measurement system named anywhere is "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." at line 21, and "satisfaction" occurs exactly once, at line 10), so the 8/10 can never be honestly scored; it also states no starting point, and its success would not move "Objective PL1: Keep the lights on, cheaper" (line 7) — developer sentiment shares no metric, noun, or ≤2-step causal chain with uptime or cloud cost.
- Scores affected: K5=0, K1=1, K3=2 (unverifiable-calibration cap), K7=2 (orphan KR in the set); per-KR score capped at 1.0 by K5=0, and Objective PL1 capped at 1.9 (D) by this Critical finding.
- Suggested rewrite: drop it from PL1 and, if developer experience is still a Q3 goal, give it its own objective with a real instrument — "KR PL1.3 (replacement, stays under PL1): Sev-1 incidents on platform-owned services `<baseline>`/quarter → `<target>`/quarter, measured on the Datadog SLO monitor." [proposal — placeholder target] and "KR (new objective, e.g. 'Internal teams ship without waiting on us'): Internal developer satisfaction, quarterly platform survey of the `<N>` engineers outside Platform (n ≥ `<respondents>`, run in `<named survey tool>`): mean `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "**KR PL1.1:** Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ## Appendix — Q2 2026 business review (extracts) › line 21, Confluence page 88104 (Q2-REVIEW))
- Why it's a problem: the target sits below the quoted trailing-90-day actual — 99.9% is 0.05 points *under* the 99.95% the team is already delivering — so the KR is passed by doing nothing new and encodes no ambition; the "Maintain" framing is the rubric's exact detection cue for a target the baseline already exceeds.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, per Datadog SLO monitor) → 99.98%, measured monthly on the Datadog SLO monitor; error budget breach in any month scores the KR at 0." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "**KR PL2.2:** Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and carries neither of the two things that would spare it — no baseline→target pair and no measure anyone outside Platform moves — so it records that the team finished a task rather than that enterprises trust the product; and because it is a single done/not-done event with no numeric scale, mid-cycle scoring can only be 0% or 100%, hiding whether the quarter's evidence work is on track until it is too late to correct.
- Scores affected: K1=0, K2=1, K6=2, K7=2; per-KR score capped at 1.0 by K1=0, and Objective PL2 capped at 2.4 (C) by two Major anti-patterns on one OKR.
- Suggested rewrite: "KR PL2.2: SOC 2 Type II in-scope controls with evidence accepted by the auditor `<baseline>`/`<N>` → `<N>`/`<N>`, tracked weekly in `<compliance tracker>`; Type II report received from `<auditor>` by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 16) — **unverified — counterparty not in scope.** Platform declares a freeze on inbound infra requests for the quarter, but names no requesting team and no request, so whether another team's Q3 plan depends on work now deferred to Q4 cannot be checked from Platform's material alone. Note only: no severity, and no AL-XX finding is produced, because a one-team scope cannot supply the counterparty's verbatim quote.

## 5. Prioritized action list

1. Replace or relocate the developer-satisfaction KR — name the survey instrument, respondent population, and baseline, or drop it from PL1 — owner: Elena R., Platform lead (resolves §3 AP-09 Metric Nobody Can Measure, and its `Also:` AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Reset the uptime target above the quoted 99.95% trailing baseline and name the measurement window — owner: Elena R., Platform lead (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a control-evidence gradient with a dated report milestone — owner: Platform compliance DRI (resolves §3 AP-01 Task Masquerading as KR and its `Also:` AP-02 Binary KR with No Gradient).
4. Add one enterprise-behaviour KR to PL2 (e.g. security reviews passed, or enterprise deals unblocked) so compliance artifacts are not the only proof of trust — owner: Elena R. with the enterprise sales lead (resolves §2 K7=2 for KR set PL2).
5. Add a leading indicator to PL1 that predicts uptime and cost mid-quarter — owner: Elena R., Platform lead (resolves §2 K6=2 for KR set PL1).
6. Name the metric source on each KR (cloud-cost dashboard, pen-test tracker) as the Datadog SLO monitor is already named for uptime — owner: Elena R., Platform lead (resolves §2 K5=2 for PL1.2 and PL2.1).
7. Circulate the Q4 infra-request freeze to the teams that file those requests and confirm none of their Q3 KRs depend on the deferred work — owner: Elena R., Platform lead (resolves §4 outbound dependency note).
8. State the company priority each objective serves once a strategy document exists, so O4 can be scored instead of marked N/A — owner: Elena R. with the exec sponsor (resolves §2 O4 gap note).
