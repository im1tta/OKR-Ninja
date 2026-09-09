# OKR-Ninja single-team report — Platform, Q3 2026

**Scope (confirmed at intake):** **single-team mode** — exactly one team in scope. Team: Platform. Period: Q3 2026, the quarter the source states ("Platform team — Q3 2026", /Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 3). Source: that local export only — the Platform OKR page (lines 3–16; "Source: Confluence page 88221 (PLAT-OKR-Q3)", line 4) plus the Q2 2026 business-review appendix (lines 18–23), which is used solely for stated baselines. Atlassian: not connected. Strategy doc: none provided. Eval run: nothing published, no registry file created or modified (Step 7 skipped).

Source refs use the local-file form `<file path> › <nearest heading> › line N`; line numbers refer to the input file exactly as it is. Every number in a rewrite that is not quoted from the corpus is a `<placeholder>` or carries the tag [proposal — placeholder target].

---

## 1. Verdict summary

**Verdict: At risk — roll-up C (2.15).** Platform's two objectives are outcome-shaped, but three of its five key results cannot be trusted as written.
- 1 team, 2 objectives, 5 KRs reviewed exhaustively (every instance scored, full AP-01–AP-15 catalog swept): **1 Critical, 2 Major, 0 Minor** findings (three blocks, carrying seven anti-pattern IDs in total).
- Worst finding: **AP-09 Metric Nobody Can Measure** on KR PL1.3 — "Improve internal developer satisfaction score to 8/10." names no instrument, states no baseline, and does not serve its objective.
- Other findings: KR PL1.1's 99.9% uptime target sits below the 99.95% Q2 actual quoted in the same export (AP-10 BAU Dressed as OKR, with AP-06 Sandbagged Target), and KR PL2.2 is a done/not-done task (AP-01 Task Masquerading as KR, with AP-02 Binary KR with No Gradient).
- The team grade C (2.15) sits above the rubric's needs-rework threshold (D or below), but Objective PL1 alone rolls up to D (1.9) under the Critical cap; no leading indicator exists in either KR set (K6=2 twice).
- **Company-level strategy tracing was out of scope:** no strategy document was provided, so O4 Strategic Anchoring is N/A for both objectives (excluded from the roll-up) and the rubric's gap note is recorded in §2.
- Recommended first action: rewrite KR PL1.3 against a named survey instrument with a stated baseline, and either tie it explicitly to the cost work as a guardrail or move it under its own objective (§3 AP-09).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15).
- Platform: K5=2 — PL1.3's satisfaction score has no named instrument (AP-09 Metric Nobody Can Measure).

**O4 = N/A — rubric gap note (recorded here, not as a finding):** no strategy source exists in the corpus. Searched: the Platform OKR page (lines 3–16) and the Q2 business-review appendix (lines 18–23) — no strategy, priority, pillar, or supports-style parent text anywhere; neither "Objective PL1: Keep the lights on, cheaper" (line 7) nor "Objective PL2: Earn enterprise trust" (line 12) states a parent (extraction records `parent: null` for both). Company-level strategy tracing was out of scope for this run; O4 is excluded from every mean per the rubric, and no anchoring was guessed.

### Per-instance breakdown (single-team depth)

Objectives (O1–O4):

| Instance | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

Key results (K1–K5, per-KR score = mean, caps applied):

| Instance | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 uptime | 3 | 4 | 1 | 3 | 3 | 2.80 |
| PL1.2 cloud spend | 3 | 4 | 3 | 3 | 2 | 3.00 |
| PL1.3 developer satisfaction | 1 | 4 | 2 | 3 | 0 | 2.00 → **1.00** (K5=0 cap) |
| PL2.1 pen-test findings | 4 | 3 | 3 | 3 | 2 | 3.00 |
| PL2.2 SOC 2 audit | 0 | 1 | 2 | 3 | 3 | 1.80 → **1.00** (K1=0 cap) |

KR sets (K6–K7):

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 2 | 3 |

Roll-up arithmetic (rubric Part 3; O4 excluded):
- PL1: 0.35 × mean(O1..O3 = 3, 3, 3) 3.00 + 0.45 × mean(2.80, 3.00, 1.00) 2.27 + 0.20 × mean(K6 2, K7 2) 2.00 = 2.47 → Critical anti-pattern confirmed (AP-09) → **capped at 1.9 → D (1.9)** (the ≥2-Major cap at 2.4 is moot).
- PL2: 0.35 × mean(O1..O3 = 4, 3, 3) 3.33 + 0.45 × mean(3.00, 1.00) 2.00 + 0.20 × mean(K6 2, K7 3) 2.50 = 2.57 → ≥2 Major anti-patterns on one OKR (AP-01, AP-02) → **capped at 2.4 → C (2.4)**.
- Team: mean(1.9, 2.4) = **2.15 → C**. Team caps: K1 ≤ 1 on 2 of 5 KRs (not more than half) → no cap; the strategy cap does not apply (no strategy corpus).
- Team dimension scores (mean of scored instances, rounded down): O1 (3, 4) → 3 · O2 (3, 3) → 3 · O3 (3, 3) → 3 · O4 → N/A · K1 (3, 3, 1, 4, 0) 2.2 → 2 · K2 (4, 4, 4, 3, 1) 3.2 → 3 · K3 (1, 3, 2, 3, 2) 2.2 → 2 · K4 (3 × 5) → 3 · K5 (3, 2, 0, 2, 3) 2.0 → 2 · K6 (2, 2) → 2 · K7 (2, 3) 2.5 → 2.

### Score evidence (every score ≤ 3 names the span that drove it)

Objectives:
- PL1 O1=3 — "Keep the lights on, cheaper" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7): a state, not a task list, with no delivery verbs; the one gap is that "Keep the lights on" describes a standing condition — only "cheaper" is a change in the world.
- PL1 O2=3 — "Keep the lights on, cheaper" (same ref, line 7): memorable, plain, no metric; the gap is the idiom "the lights" standing in for a specific noun subject.
- PL1 O3=3 — "Platform team — Q3 2026" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 3): the period is inherited unambiguously from the page heading but not restated in the objective.
- PL1 O4=N/A — gap note above.
- PL2 O1=4 — "Earn enterprise trust" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12): a changed end-state, no delivery verbs, achievable by more than one route.
- PL2 O2=3 — "Earn enterprise trust" (same ref, line 12): three plain words, no metric; the gap is that "trust" is left unconcretized — what an enterprise does when it trusts Brightledger is not said.
- PL2 O3=3 — "Platform team — Q3 2026" (line 3 ref above): inherited, not restated.
- PL2 O4=N/A — gap note above.

Key results:
- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8): metric, target and unit present; no baseline on the page, but one is retrievable from the same export — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21); the KR states no measurement window.
- PL1.1 K2=4 — "Maintain API uptime at or above 99.9%." (line 8 ref above): uptime is a result experienced outside the team.
- PL1.1 K3=1 — "Maintain API uptime at or above 99.9%." (line 8) against "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21): target at or below last period's actual — sandbag anchor.
- PL1.1 K4=3 — the KR line "Maintain API uptime at or above 99.9%." (line 8) carries no owner; the individual is derivable from the page header "Owner: Elena R." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 4).
- PL1.1 K5=3 — no source named in the KR; a single obvious system of record is found elsewhere in the corpus: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21).
- PL1.2 K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9): metric, numeric baseline, numeric target and unit; the measurement window (monthly average, quarter-exit month, or quarter total) is unstated.
- PL1.2 K2=4 — same quote (line 9): unit cost is a business result.
- PL1.2 K3=3 — same quote (line 9): a 22% reduction, committed by the page default "KRs are committed unless marked (aspirational)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 5); no trend or justification anywhere in the corpus, so the stretch is unexplained.
- PL1.2 K4=3 — no owner on the KR line (line 9); "Owner: Elena R." (line 4) makes the individual derivable.
- PL1.2 K5=2 — same quote (line 9): no source named, and the cloud bill, a FinOps tool and the finance ledger — plus whichever system supplies the transaction count — would give different unit costs; the corpus names no cost system (searched lines 3–23: the only instrument named anywhere is the Datadog SLO monitor on line 21).
- PL1.3 K1=1, K2=4, K3=2 (no baseline or trend anywhere → unverifiable cap), K4=3 (as above), K5=0 — "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10): a qualitative state dressed as a metric — the "score" is defined nowhere in the corpus, has no baseline, and no instrument; see §3 AP-09.
- PL2.1 K1=4 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13): named metric, numeric baseline (7 open), numeric target (100% closed), unit, and the population pinned by the parenthetical; a closure count is a cycle-end stock, so no averaging window is needed.
- PL2.1 K2=3 — same quote (line 13): remediation is a proxy output; its link to the outcome is stated only through the objective "Earn enterprise trust" (line 12).
- PL2.1 K3=3 — same quote (line 13): 7 → 0 in one quarter, committed by default (line 5); a full-coverage but modest stretch with no trend to compare.
- PL2.1 K4=3 — no owner on the KR line (line 13); "Owner: Elena R." (line 4).
- PL2.1 K5=2 — same quote (line 13): no source named; the pen-test vendor's report and an internal tracker, and closure read as fixed versus re-tested, would give different counts; none named in the corpus.
- PL2.2 K1=0, K2=1, K3=2 (no scale → unverifiable cap), K4=3 (as above) — "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14): a pure done/not-done milestone with no date; see §3 AP-01.
- PL2.2 K5=3 — same quote (line 14): the auditor's issued report is the single obvious system of record, and the audit is confirmed in progress by "Q3 is fully committed between SOC 2 evidence collection and the cost work." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16).

KR sets:
- PL1 K6=2 — "Maintain API uptime at or above 99.9%." (line 8), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9), "Improve internal developer satisfaction score to 8/10." (line 10): all three are end-of-quarter truths; nothing in the set predicts them mid-cycle.
- PL1 K7=2 — the first two KRs cover both clauses of "Keep the lights on, cheaper" (line 7); "Improve internal developer satisfaction score to 8/10." (line 10) is an orphan serving a different goal (see §3 AP-09, Also AP-12).
- PL2 K6=2 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) and "Complete the SOC 2 Type II audit." (line 14) are both leading proxies (security work); no KR measures the trust they are meant to produce.
- PL2 K7=3 — one coverage gap under "Earn enterprise trust" (line 12): no KR shows an enterprise actually extending trust (security reviews passed, deals unblocked, renewals).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10)
- Evidence: "Keep the lights on, cheaper" (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: The KR quantifies an internal state with no instrument — no survey, dashboard, or tool for a developer satisfaction score is named on the OKR page or anywhere else in the corpus (searched lines 3–16 and 18–23; the only instrument named in the export is the Datadog SLO monitor for uptime on line 21), so who is asked, what is asked, and when is defined only in someone's head and the number can never be honestly scored (AP-09). It states no current value and none is retrievable — "satisfaction" and "score" appear nowhere else in the export — so neither ambition nor progress can be judged (AP-04). And no causal chain of two steps or fewer runs from a satisfaction score to "Keep the lights on, cheaper": the KR shares no nouns with its objective, so reaching 8/10 would not show the lights stayed on or got cheaper (AP-12).
- Scores affected: K5=0, K1=1, K3=2 (unverifiable cap), K7=2 (set PL1); per-KR score capped at 1.0; Critical cap → PL1 per-OKR 1.9 (D)
- Suggested rewrite: "KR PL1.3 (guardrail on the cost work): Internal developer satisfaction with the platform — `<named survey instrument, e.g. the existing engineering pulse survey>`, question 'How satisfied are you with the platform?' answered 1–10, one wave per quarter, n ≥ `<n>` engineers from product teams — `<baseline>`/10 (last wave) → 8/10, and never below `<floor>`/10 in any wave while cloud spend per 1,000 transactions falls from $4.10 to $3.20." [proposal — placeholder target] If developer experience is meant as a goal in its own right rather than a guardrail on PL1, move the same KR under its own objective — "Product engineers build on the platform without waiting on us" [proposal] — instead of leaving it under PL1.

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21)
- Also: AP-06 Sandbagged Target
- Why it's a problem: "Maintain" describes the team's standing duty with no delta — the KR is met by default staffing and takes a KR slot from a real goal (AP-10); and its 99.9% target sits below the 99.95% trailing-90-day actual the same export quotes for Q2, so the target is already achieved as written — a sandbag (AP-06).
- Scores affected: K3=1, K1=3 (baseline off-page but retrievable), K6=2 (set PL1)
- Suggested rewrite: "KR PL1.1: API uptime, trailing 90 days per the Datadog SLO monitor: 99.95% (Q2 actual) → `<target above 99.95%>`, held while cloud spend per 1,000 transactions falls from $4.10 to $3.20." [proposal — placeholder target] If 99.9% is a contractual floor rather than a goal, move it to a health-metric line outside the OKRs and replace the KR with: "KR PL1.1: Customer-facing Sev-1/Sev-2 incidents per quarter: `<Q2 count>` → `<target>` (Datadog incident records)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: The KR begins with "Complete" and carries no metric and no baseline→target pair — it is an activity, not a measured result, and it succeeds even if the audit surfaces exceptions that keep enterprise buyers away (AP-01). It is done/not-done, so a mid-quarter check can only read 0% or 100%, giving the team no steering signal (AP-02).
- Scores affected: K1=0, K2=1, K3=2 (unverifiable cap), K6=2 (set PL2); per-KR score capped at 1.0; two Major anti-patterns on one OKR → PL2 per-OKR capped at 2.4 (C)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II — auditor evidence requests delivered 0/`<n>` → `<n>`/`<n>` (tracked weekly in `<evidence tracker>`), fieldwork closed with `<0>` exceptions, and the final report received and shared with `<k>` enterprise prospects by `<date within Q3>`." [proposal — placeholder target]

## 4. Outbound dependency notes

Single-team mode produces no AL-XX findings; the notes below carry no severity.

- "Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16) — **unverified — counterparty not in scope.** This is an inbound-request freeze: other teams' infrastructure requests to Platform are deferred for the quarter, but no requesting team is named, so which teams (if any) have Q3 commitments that depend on Platform cannot be established from Platform's material alone. A portfolio-mode run is the place to check this edge.

No other cross-team mention exists on the Platform page: no team name, shared system, or depends-on / blocked-by / with-team phrase appears on lines 3–16 (searched). The appendix's Payments and Growth lines (lines 22–23) are Q2 business-review extracts about other teams, not Platform dependency mentions, and are out of scope for this review.

## 5. Prioritized action list

1. Rewrite KR PL1.3 against a named survey instrument with a stated baseline and an explicit guardrail link to the cost work (or move it under its own developer-experience objective) — owner: Elena R., Platform page owner (resolves §3 AP-09 Metric Nobody Can Measure, including AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Re-baseline KR PL1.1 at the quoted 99.95% Q2 actual with a target above it, or move the 99.9% floor to a health-metric line and replace the KR with an incident-count delta — owner: Platform SRE/on-call lead (resolves §3 AP-10 BAU Dressed as OKR, including AP-06 Sandbagged Target).
3. Replace KR PL2.2 with a graded SOC 2 KR — evidence requests delivered, exceptions, and report in enterprise prospects' hands by a Q3 date — owner: Platform security/compliance lead (resolves §3 AP-01 Task Masquerading as KR, including AP-02 Binary KR with No Gradient).
4. Add one leading indicator to each KR set (e.g. an error-budget or incident signal for PL1, evidence-request velocity for PL2) so both sets can be steered mid-quarter — owner: Elena R. (addresses §2 K6=2 on both sets; no finding block).
5. Name the system of record and measurement window for KR PL1.2 (which cost source, which transaction count, monthly or quarter-exit) and for KR PL2.1 (pen-test report versus tracker; closure defined as re-tested) — owner: Platform FinOps owner and security lead respectively (addresses §2 K5=2 and K1=3 on PL1.2, K5=2 on PL2.1; no finding block).
6. Record a stated parent for each objective once a company priorities document exists, so O4 Strategic Anchoring can be scored on the next run — owner: Elena R. (addresses the §2 O4 N/A gap note).
