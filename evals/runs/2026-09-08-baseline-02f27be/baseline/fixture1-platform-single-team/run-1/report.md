# OKR-Ninja — Single-team report: Platform, Q3 2026

Scope (confirmed at intake): **Platform team only → single-team mode.** Period: Q3 2026 (as stated by the source). Source: local export `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md` (Platform OKR page, Confluence page 88221 export, plus Q2 2026 business-review extracts, page 88104). No Atlassian connection; no company strategy document provided. Eval run — nothing published, no registry written.

---

## 1. Verdict summary

**Verdict: At risk — roll-up grade C (2.46).** Above the rubric's needs-rework threshold (D), but three of the team's five KRs carry a Major defect and both objectives are score-capped by them.
Findings: **0 Critical · 4 Major · 0 Minor.**
Worst finding: **AP-06 Sandbagged Target** — the committed uptime KR targets "at or above 99.9%" while the Q2 review quotes a trailing-90-day actual of 99.95%, so the team's headline reliability commitment is met on day one with no change in behaviour.
Close behind: **AP-02 Binary KR with No Gradient** — "Complete the SOC 2 Type II audit." can only score 0% or 100%, on the very workstream the page says is consuming the quarter.
The developer-satisfaction KR has no baseline (AP-04 KR Without Baseline) and does not serve its objective (AP-12 Orphan KR).
Company-level strategy tracing was **out of scope** for this run (no strategy source in the corpus): O4 Strategic Anchoring is N/A for both objectives and excluded from the roll-up, with the gap recorded in §2.
Recommended first action: rewrite KR PL1.1 against the quoted 99.95% baseline (or move uptime out of the OKRs as a standing guardrail) and convert KR PL2.2 into a gradient measure of SOC 2 evidence/exception closure — owner: Platform lead (Elena R., page owner).

---

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.46)**.
- Platform: K1=2: PL2.2 scores K1=0, a done/not-done SOC 2 milestone (AP-02 Binary KR with No Gradient).

**O4 — N/A, gap note (rubric's no-strategy-source rule):** no strategy source exists in the corpus, so O4 is scored N/A for both objectives and excluded from the roll-up rather than guessed. Neither objective states a parent: "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`) and "Earn enterprise trust" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`) carry no link to any company priority. Search trail: the entire source file (lines 1–23) — the Platform OKR page (page 88221, lines 3–16) and the Q2 business-review extracts (page 88104, lines 18–23); no strategy, pillar, priority, or company-goal text appears in either, and the appendix is a business review, not a strategy artifact. Company-level strategy tracing was out of scope for this run.

### Per-instance breakdown (exhaustive)

| Instance | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 | per-KR mean (K1–K5) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" (objective) | 3 | 3 | 3 | N/A | – | – | – | – | – | 2 | 2 | – |
| PL1.1 uptime | – | – | – | – | 3 | 4 | 1 | 3 | 3 | – | – | 2.8 |
| PL1.2 cloud spend | – | – | – | – | 3 | 4 | 3 | 3 | 2 | – | – | 3.0 |
| PL1.3 developer satisfaction | – | – | – | – | 2 | 4 | 2 | 3 | 2 | – | – | 2.6 |
| PL2 "Earn enterprise trust" (objective) | 4 | 3 | 3 | N/A | – | – | – | – | – | 2 | 3 | – |
| PL2.1 pen-test findings | – | – | – | – | 3 | 3 | 3 | 3 | 2 | – | – | 2.8 |
| PL2.2 SOC 2 | – | – | – | – | 0 | 1 | 2 | 3 | 2 | – | – | 1.6 → **1.0** (cap: K1=0) |

Team dimension integers (mean of scored instances, rounded down): O1 floor(3.5)=3 · O2 3 · O3 3 · O4 N/A · K1 floor(2.2)=2 · K2 floor(3.2)=3 · K3 floor(2.2)=2 · K4 3 · K5 floor(2.2)=2 · K6 2 · K7 floor(2.5)=2.

Roll-up arithmetic (rubric Part 3):
- PL1: 0.35 × mean(O1..O3)=3.00 + 0.45 × mean(per-KR)=2.80 + 0.20 × mean(K6,K7)=2.00 → 1.05 + 1.26 + 0.40 = **2.71**; cap 3 applies (three Major anti-patterns on one OKR: AP-06, AP-04, AP-12) → **2.40 (C)**.
- PL2: 0.35 × mean(O1..O3)=3.33 + 0.45 × mean(per-KR)=1.90 (PL2.2 capped at 1.0 by cap 1, K1=0) + 0.20 × mean(K6,K7)=2.50 → 1.17 + 0.86 + 0.50 = **2.52 (C)**; one Major anti-pattern (AP-02) → no further cap.
- Team = mean(2.40, 2.52) = **2.46 → C**. Team caps: K1 ≤ 1 on 1 of 5 KRs (PL2.2) — below the more-than-half threshold, no cap; strategy corpus absent — strategy cap not applicable.

### Score rationale — quoted spans for every score ≤ 3 (rubric Part 5, rule 2)

All source refs below point at `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md`; each is written in full.

**PL1 (objective)** — "Keep the lights on, cheaper" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- O1=3 — "Keep the lights on" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): a standing-duty clause with no changed end-state; only "cheaper" carries a delta. No delivery verbs, so not lower.
- O2=3 — "the lights" (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): an idiom with no specific noun subject (the API? all infrastructure?); otherwise short, memorable, metric-free.
- O3=3 — period inherited unambiguously from the page heading "Platform team — Q3 2026" (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 3`), not restated in the objective.
- O4=N/A — see gap note above.
- K6=2 (set) — "Maintain API uptime at or above 99.9%." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`… › line 9`), "Improve internal developer satisfaction score to 8/10." (`… › line 10`): all three are lagging end-of-period measures; nothing in the set predicts them mid-cycle.
- K7=2 (set) — one orphan KR: "Improve internal developer satisfaction score to 8/10." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) serves a developer-experience goal, not "Keep the lights on, cheaper" (see §3 AP-12).

**PL1.1** — "Maintain API uptime at or above 99.9%." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- K1=3 — metric, target and unit present; baseline absent from the KR but retrievable from the same corpus: Platform reliability: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`…/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`); measurement window unstated.
- K2=4 — "API uptime": a result customers experience.
- K3=1 — "at or above 99.9%" (line 8) versus the quoted trailing actual "99.95%" (line 21): target at or below last period's actual — sandbag (see §3 AP-06).
- K4=3 — team named in "Platform team — Q3 2026" (`… › line 3`) and page-level "Owner: Elena R." (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 4`); no per-KR owner. (Applies identically to every KR below.)
- K5=3 — the KR names no source, but the corpus names the system of record for this exact metric: "(Datadog SLO monitor)" (`… › line 21`).

**PL1.2** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`)
- K1=3 — metric, numeric baseline, numeric target, unit and denominator all present; measurement window unstated (monthly average? quarter exit rate?).
- K2=4 — unit cost per transaction is a business result.
- K3=3 — "from $4.10 to $3.20" is a ~22% cut; committed by the page rule "Commitment: KRs are committed unless marked (aspirational)." (`…/input/sample-portfolio.md › Platform team — Q3 2026 › line 5`); no justification of the stretch is stated.
- K4=3 — as PL1.1.
- K5=2 — no cost system or transaction-count source named; billing console, finance ledger and a cost tool would give different numbers.

**PL1.3** — "Improve internal developer satisfaction score to 8/10." (`…/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- K1=2 — "to 8/10": target without baseline (see §3 AP-04).
- K2=4 — internal developers, outside the Platform team, experience the result.
- K3=2 — unverifiable cap: no baseline or trend exists anywhere (searched the Platform page, lines 3–16, and the appendix, lines 18–23); calibration cannot be judged.
- K4=3 — as PL1.1.
- K5=2 — "score" implies an instrument, but none is named; a survey, an ad-hoc poll or a developer-experience tool would each give a different number.

**PL2 (objective)** — "Earn enterprise trust" (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`)
- O1=4 — "Earn enterprise trust": a changed end-state, no delivery verbs, reachable by more than one route.
- O2=3 — "trust" (`… › line 12`): one ungrounded abstraction — trust in what respect is left to the KRs (SOC 2, pen-test), which do supply it; otherwise short and memorable.
- O3=3 — inherited from "Platform team — Q3 2026" (`… › line 3`), not restated.
- O4=N/A — see gap note above.
- K6=2 (set) — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`… › line 13`) and "Complete the SOC 2 Type II audit." (`… › line 14`) are both inputs to trust; no lagging measure of trust itself is in the set.
- K7=3 (set) — one coverage gap: no KR measures trust as enterprise customers experience it (security reviews passed, enterprise deals unblocked); the two KRs cover posture and attestation only.

**PL2.1** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`)
- K1=3 — metric, baseline "(currently 7 open)", target (100% closed = 0 open) and population stated; measurement window unstated.
- K2=3 — closing findings is the team's own output with a credible link to the stated outcome (enterprise trust); trust itself is not measured.
- K3=3 — 7 → 0 High-or-above findings, committed by default; justification absent.
- K4=3 — as PL1.1.
- K5=2 — the pen-test report/tracker of record is not named.

**PL2.2** — "Complete the SOC 2 Type II audit." (`…/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- K1=0 — pure done/not-done milestone; nothing countable (see §3 AP-02).
- K2=1 — a delivery milestone stands in for the metric; no outcome measured.
- K3=2 — unverifiable cap: no scale, baseline or trend to calibrate against.
- K4=3 — as PL1.1.
- K5=2 — the auditor's report is the implicit system of record; not named.

---

## 3. Findings

All four findings are Major; within the tie they are ordered by impact on the team's scores.

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence: Platform reliability: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Evidence: "Commitment: KRs are committed unless marked (aspirational)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Platform team — Q3 2026 › line 5`)
- Why it's a problem: the target (99.9%) sits below the trailing-90-day actual the Q2 review quotes for the same metric (99.95%), so this committed KR is already met with no change in behaviour — the target at/below last period's actual that AP-06 defines. "Maintain" also matches the AP-10 BAU Dressed as OKR cue; the defect is reported once, here, as the specific sandbag.
- Scores affected: K3=1 (PL1.1); K1=3 (baseline retrievable only from the appendix); contributes to the ≥2-Major cap on PL1 (2.71 → 2.40).
- Suggested rewrite: "KR PL1.1 (committed): API uptime, trailing 90 days, 99.95% (Q2 actual, Datadog SLO monitor) → `<target above 99.95%>` [proposal — placeholder target], scored monthly on the Datadog SLO monitor." If 99.9% is a contractual floor and no improvement is intended, remove it from the OKRs and track it as a standing health guardrail instead.

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Evidence: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
- Why it's a problem: a done/not-done KR can only score 0% or 100% mid-cycle, so the workstream the page says is consuming the quarter has no steering signal until the audit ends. It also begins with "Complete" and carries no metric — the AP-01 Task Masquerading as KR cue — but that is the same binary-milestone defect, reported once here.
- Scores affected: K1=0, K2=1 (PL2.2); per-KR score capped at 1.0 (rubric cap 1), dragging PL2's KR mean to 1.90.
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II auditor evidence requests closed 0/`<N>` → `<N>`/`<N>`; control exceptions in the auditor's draft report `<baseline>` → 0; final Type II report received by `<date within Q3 2026>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: "to 8/10" states a target with no "from" — neither ambition nor progress can be judged. Absence search: the Platform OKR page (lines 3–16) and the Q2 business-review extracts (lines 18–23) contain no developer-satisfaction value; the appendix quotes uptime, chargeback, step-up coverage and signups only. No measuring instrument is named either, so the KR also cannot say where the 8/10 would be read from.
- Scores affected: K1=2, K3=2 (unverifiable cap), K5=2 (PL1.3); contributes to the ≥2-Major cap on PL1.
- Suggested rewrite: "KR PL1.3: Internal developer satisfaction, quarterly survey on `<named instrument>` (n ≥ `<n>`): `<last survey score>`/10 → 8/10." [proposal — placeholder baseline] If no prior survey exists, the KR must say so explicitly and the first Q3 survey becomes the stated baseline.

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence: "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Evidence: "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`)
- Why it's a problem: developer satisfaction shares no noun or domain with "Keep the lights on" (service continuity) or "cheaper" (unit cost), and no causal chain of ≤2 steps runs from a higher satisfaction score to either outcome — hitting 8/10 would not show the objective happened. The page's own note that non-critical infra requests are being held until Q4 makes the fit weaker still (analyst inference: those requests are the most plausible lever on developer satisfaction, and the page defers them).
- Scores affected: K7=2 (PL1 set); contributes to the ≥2-Major cap on PL1 (2.71 → 2.40).
- Suggested rewrite: replace the KR under PL1 with a leading reliability indicator that pairs with PL1.1 — "KR PL1.3: API SLO error-budget breaches per Datadog SLO monitor: `<Q2 count>` → 0 in Q3 2026." [proposal — placeholder target] — and, if developer satisfaction matters to the team this quarter, carry it (with the baseline and instrument from the AP-04 rewrite) under a separate developer-experience objective rather than under "Keep the lights on, cheaper".

---

## 4. Outbound dependency notes

No outbound dependency mentions found.

Search trail: the Platform OKR page (lines 3–16) names no other team, shared system, or depends-on / blocked-by / with-<team> phrasing; the appendix lines for Payments (line 22) and Growth (line 23) are Q2 business-review extracts about those teams, not Platform dependency mentions, and those teams are out of scope. Context for a future portfolio run (not a dependency mention; no severity): "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-08-baseline-02f27be/baseline/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) is an inbound-capacity statement whose counterparties are unnamed — unverified — counterparty not in scope.

---

## 5. Prioritized action list

1. Rewrite KR PL1.1 with the quoted 99.95% trailing-90-day baseline and a target above it, or move uptime out of the OKRs as a standing guardrail — owner: Platform lead (Elena R., page owner) (resolves §3 AP-06 Sandbagged Target).
2. Replace KR PL2.2 with a gradient measure of SOC 2 evidence requests closed and draft-report exceptions, with the final-report date as a secondary milestone — owner: Platform lead with the SOC 2 evidence-collection owner (resolves §3 AP-02 Binary KR with No Gradient).
3. State the current developer-satisfaction score and the named survey instrument, or declare that the Q3 survey is the first measurement — owner: Platform lead (resolves §3 AP-04 KR Without Baseline).
4. Move the developer-satisfaction KR out from under PL1 and replace it with a leading reliability indicator on the Datadog SLO monitor — owner: Platform on-call/SRE lead (resolves §3 AP-12 Orphan KR; lifts K6 and K7 for the PL1 set).
5. Name the system of record on KR PL1.2 (cost dashboard and transaction-count source) and KR PL2.1 (pen-test findings tracker), and state a measurement window on each KR — owner: Platform lead (addresses §2 K5=2 and K1=3 rationale for PL1.2 and PL2.1).
6. Attach a stated parent company priority to PL1 and PL2 once a strategy source is available, so O4 can be scored — owner: Platform lead (addresses §2 O4 gap note).
