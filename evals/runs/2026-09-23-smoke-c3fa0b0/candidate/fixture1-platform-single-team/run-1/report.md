# OKR-Ninja single-team review — Platform team, Q3 2026

## 1. Verdict summary

**Verdict: Needs targeted fixes — roll-up C (2.4).** Three of Platform's five committed KRs need rewriting before the quarter can be tracked on them. PL1.2 and PL2.1 are sound.
- Scope: single-team mode, Platform team, Q3 2026. Source: `/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md` (Platform page, lines 3–16; Q2 2026 business review extract, lines 18–23).
- Findings: 0 Critical · 3 Major · 0 Minor. There is also 1 outbound dependency note (unverified, no severity).
- Worst finding: AP-01 Task Masquerading as KR (with AP-02 Binary KR with No Gradient). The SOC 2 KR is a done/not-done task and has the set's only K1=0.
- Also Major: AP-12 Orphan KR (with AP-04 KR Without Baseline) on developer satisfaction, which sits under a cost-and-uptime objective and has no starting value. And AP-06 Sandbagged Target: the committed 99.9% uptime target is below the Q2 actual of 99.95%.
- Company-level strategy tracing was out of scope. No strategy document was provided, so O4 Strategic Anchoring is N/A and excluded from the roll-up.
- Recommended first action: replace the SOC 2 KR with a graded version that shows progress during the quarter (§5, item 1).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

O4 N/A — gap note: the corpus contains no company or org strategy source, and neither objective states a link to any company goal. Searched: the Platform page (lines 3–16) and the Q2 2026 business review extract (lines 18–23). O4 is left out of the roll-up rather than guessed. Company-level strategy tracing was out of scope for this run.

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): Platform C (2.4) — PL1 C (2.4; 2.71 before the ≥2-Major cap) · PL2 C (2.4; 2.52 before the ≥2-Major cap). No team-level cap was triggered.
- Platform: K1=2 — the SOC 2 audit KR is done/not-done, scoring K1=0 (AP-01).

Per-instance breakdown (every score ≤ 3 names its span):

**Objectives**
- PL1 → O1 3 · O2 3 · O3 3 · O4 N/A — "Keep the lights on, cheaper" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7): "cheaper" names a change, but "Keep the lights on" restates the team's standing duty (O1 3). The idiom also stands where a specific noun subject belongs (O2 3). The standing-duty wording is a matter of style, not an ongoing-duty objective in disguise, because PL1.2 delivers the "cheaper" change with "from $4.10 to $3.20" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9).
- PL2 → O1 4 · O2 3 · O3 3 · O4 N/A — "Earn enterprise trust" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12): a changed end-state with no delivery verb (O1 4). Whose trust, and trust in what, is left to the KRs (O2 3).
- Both objectives, O3 3: the period comes from "Platform team — Q3 2026" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 3), and neither objective restates it.

**Key results** — all five are committed per "KRs are committed unless marked (aspirational)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 5). All five score K4 3: "Owner: Elena R." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 4) names the page owner, and no KR names an owner of its own.
- PL1.1 → K1 3 · K2 4 · K3 1 · K4 3 · K5 3 (KR score 2.8) — "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8) states no baseline or window. The baseline and the system of record appear only in "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21) (K1 3, K5 3). The target is below that actual (K3 1, §3 AP-06).
- PL1.2 → K1 3 · K2 4 · K3 3 · K4 3 · K5 2 (3.0) — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9): baseline, target and unit are stated, but not the averaging window (K1 3). It is a committed cut with no stated trend or mechanism (K3 3). Lines 3–16 and 18–23 name no system for spend or transaction counts (K5 2).
- PL1.3 → K1 2 · K2 4 · K3 2 · K4 3 · K5 2 (2.6) — "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10): a target with no baseline (K1 2). There is no baseline or trend anywhere, so calibration can't be verified and K3 is capped at 2. The corpus names no survey instrument or population (K5 2). See §3 AP-12.
- PL2.1 → K1 3 · K2 3 · K3 3 · K4 3 · K5 2 (2.8) — "Close 100% of pen-test findings rated High or above (currently 7 open)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13): baseline and target are stated, but not the window (K1 3). It is a remediation proxy, and only its objective links it to trust (K2 3). It commits to full closure at a modest stretch, with no trend given (K3 3). No tracker or report is named for closure status (K5 2).
- PL2.2 → K1 0 · K2 1 · K3 2 · K4 3 · K5 2 (1.6, capped at 1.0 by K1=0) — "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14): a done/not-done milestone (K1 0, K2 1). With no baseline, calibration can't be verified (K3 2). The KR doesn't say what counts as proof of completion (K5 2). See §3 AP-01.

**KR sets**
- PL1 → K6 2 · K7 2 — PL1.1–PL1.3 (quoted above) all read outcomes, and none is a leading indicator that predicts another (K6 2). PL1.3 is an orphan (K7 2, §3 AP-12).
- PL2 → K6 2 · K7 3 — PL2.1 and PL2.2 (quoted above) are both proxies, with no lagging trust outcome for them to predict (K6 2). No KR measures whether enterprise customers' trust actually changed, which leaves one coverage gap under "Earn enterprise trust" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12) (K7 3).

## 3. Findings

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: KR PL2.2 opens with a delivery verb and has no metric, no baseline→target pair and no result that anyone outside the team moves, so it restates the work instead of measuring a result (AP-01). It is also a single done/not-done event, so mid-quarter it can only score 0% or 100% (AP-02).
- Scores affected: K1=0 (per-KR score capped at 1.0), K2=1, K3=2 (PL2.2)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II controls with evidence accepted by the auditor `<baseline>`/`<total>` → `<total>`/`<total>`, with the Type II report issued without exceptions by `<date>`." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Keep the lights on, cheaper" (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7)
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10)
- Also: AP-04 KR Without Baseline
- Why it's a problem: KR PL1.3 measures internal developer satisfaction, which shares no noun or domain with an objective about keeping the platform running at lower cost, and nothing on the page ties a higher score to uptime or unit cost, so hitting 8/10 would not show that PL1 was achieved (AP-12). It also states no starting value, and none appears anywhere in the corpus (searched the Platform page, lines 3–16, and the Q2 2026 business review extract, lines 18–23), so the committed 8/10 can be judged neither as ambition nor as progress (AP-04).
- Scores affected: K7=2 (PL1 set), K1=2, K3=2 (PL1.3)
- Suggested rewrite: PL1 keeps PL1.1 and PL1.2, which cover both halves of its objective; PL1.3 leaves PL1 and, if the team keeps it, returns under an objective it serves as "KR: Internal developer satisfaction score, `<survey instrument>` (n ≥ `<n>`), `<baseline>`/10 → 8/10 by end of Q3 2026." [proposal — placeholder target] (8/10 reused from /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10)

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21)
- Why it's a problem: KR PL1.1 commits to 99.9% while the Q2 2026 business review already reports 99.95% for the same metric, so the target is below last period's actual and is met even if uptime slips. It sets no ambition and would not flag a decline.
- Scores affected: K3=1 (PL1.1)
- Suggested rewrite: "KR PL1.1: API uptime, trailing 90 days on the Datadog SLO monitor, 99.95% (Q2 2026 actual) → 99.97% by end of Q3 2026." [proposal — placeholder target] (99.95% reused from /Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21)

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (/Users/difan/Archive/A_04_Repos/OKR_Ninja/evals/runs/2026-09-23-smoke-c3fa0b0/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16) — **unverified — counterparty not in scope.** The page does not say who raises these requests or which ones are on hold.

## 5. Prioritized action list

1. Replace PL2.2 with a graded KR that counts SOC 2 Type II controls accepted by the auditor on the way to an issued report — owner: Platform OKR owner (Elena R.) (resolves §3 AP-01 Task Masquerading as KR, AP-02 Binary KR with No Gradient).
2. Move PL1.3 out of PL1 and, if it stays in the plan, restate it with a survey baseline under an objective it serves — owner: Platform OKR owner (Elena R.) (resolves §3 AP-12 Orphan KR, AP-04 KR Without Baseline).
3. Raise PL1.1's committed target above the 99.95% trailing-90-day uptime reported in the Q2 review, measured on the Datadog SLO monitor — owner: Platform OKR owner (Elena R.) (resolves §3 AP-06 Sandbagged Target).
4. Link PL1 and PL2 to the company priority each serves, and supply that strategy doc for a re-run so O4 Strategic Anchoring can be scored — owner: Platform OKR owner (Elena R.) (resolves §2 O4 gap note).
