# OKR-Ninja — Single-team review: Platform (Q3 2026)

Mode: **single-team** (exactly one team in confirmed scope: Platform). Period: Q3 2026, as stated by the source page. Corpus: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` (Platform OKR page, lines 3–16; Q2 2026 business-review appendix, lines 18–23). No Atlassian source was connected.

## 1. Verdict summary

**Verdict: At risk.** Platform's Q3 set is C (2.15) overall, but one KR cannot be honestly scored at all and the flagship reliability KR is set below the number the company already reports.

- Roll-up grade: **C (2.15)** — Objective PL1 D (1.9), Objective PL2 C (2.4).
- Findings: **1 Critical, 2 Major, 0 Minor** (3 finding blocks over 2 objectives and 5 KRs, all scored exhaustively).
- Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, no baseline, and no system of record anywhere in the corpus, so it can never be honestly scored.
- Close behind: **AP-06 Sandbagged Target** on the uptime KR — its 99.9% target sits below the 99.95% trailing baseline quoted in the same file.
- **Company-level strategy tracing was out of scope:** no company or org strategy document was provided in this corpus, so O4 Strategic Anchoring is scored **N/A** for both objectives and excluded from the roll-up, with the gap recorded in §2 (per `references/goodness-rubric.md` O4).
- Recommended first action: re-baseline the uptime KR against the quoted 99.95% figure before the quarter's mid-point (see §5, item 1).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (capped by a Critical anti-pattern), Objective PL2 **C (2.4)** (capped by two Major anti-patterns on one OKR).
- Platform: K5=1 — one KR names no instrument at all and two others leave the system of record unstated.

**O4 gap note (N/A):** no company/org strategy source exists in this corpus — the only non-OKR material is the Q2 business review, which reports outcomes and names no strategic pillar — its Platform line reads in full: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ## Appendix — Q2 2026 business review (extracts) › line 21`). Sources searched: the Platform OKR page (lines 3–16) and the appendix (lines 18–23); no other source was in scope and no Atlassian connection was available. O4 is therefore N/A for PL1 and PL2 and excluded from every mean, and no strategic-anchoring score is guessed.

**Per-instance breakdown** (dimensions whose scores vary):

| Instance | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" (line 7) | 3 | 3 | 3 | N/A |
| PL2 "Earn enterprise trust" (line 12) | 4 | 4 | 3 | N/A |

| Instance | K1 | K2 | K3 | K4 | K5 | per-KR |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." (line 8) | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." (line 10) | 1 | 3 | 2 | 3 | 0 | 1.0 (capped, K5=0) |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 "Complete the SOC 2 Type II audit." (line 14) | 0 | 1 | 2 | 3 | 2 | 1.0 (capped, K1=0) |

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 2 | 2 |

Score notes (each names the quoted span that drove it, per `references/goodness-rubric.md` Part 5 rule 2):
- **O1=3, O2=3, O3=3 (PL1)** — "Keep the lights on, cheaper" (line 7) is outcome-framed with no delivery verb, but "Keep the lights on" states continuation of today's state rather than a changed end-state, and the idiom carries no specific noun subject; the period is inherited unambiguously from "## Platform team — Q3 2026" (line 3) rather than restated.
- **O1=4, O2=4, O3=3 (PL2)** — "Earn enterprise trust" (line 12) is a changed end-state achievable by more than one route, memorable, under 15 words, metric-free; period inherited from the page heading (line 3).
- **K3=1 (PL1.1)** — "Maintain API uptime at or above 99.9%." (line 8) against "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21); see §3.
- **K1=3, K5=2 (PL1.2)** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) carries metric, baseline, target and unit but no measurement window, and names no billing or finance system of record.
- **K1=1, K5=0, K3=2 (PL1.3)** — "Improve internal developer satisfaction score to 8/10." (line 10); see §3. K3 is capped at 2 because no baseline or prior actual for this score exists anywhere in the searched sources — calibration is unverifiable.
- **K1=3, K5=2, K3=3 (PL2.1)** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) states its population and its starting point (7 open), so the percentage is countable; but no tracker or report of record is named and no measurement window is given.
- **K1=0, K2=1, K3=2 (PL2.2)** — "Complete the SOC 2 Type II audit." (line 14); see §3.
- **K4=3 for all five KRs** — no KR names an accountable individual, but the page names one for the whole set: "Owner: Elena R." (line 4), so the individual is derivable from the same source.
- **K6=2, K7=2 (PL1)** — the set contains only end-state truths ("Maintain API uptime at or above 99.9%.", "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", lines 8–9) with no leading indicator that predicts either, and "Improve internal developer satisfaction score to 8/10." (line 10) serves a different goal than "Keep the lights on, cheaper" (see §3).
- **K6=2, K7=2 (PL2)** — "Close 100% of pen-test findings rated High or above (currently 7 open)." and "Complete the SOC 2 Type II audit." (lines 13–14) are both compliance proxies; nothing in the set measures the trust the objective claims ("Earn enterprise trust", line 12) — no enterprise deal, security-review, or renewal outcome — so a skeptic could see both KRs hit and still not see trust earned.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: the "internal developer satisfaction score" names no survey, instrument, or dashboard, and no such system appears anywhere in the searched corpus (the Platform OKR page, lines 3–16, and the Q2 business review appendix, lines 18–23, which reports only uptime, chargebacks and signups), so the 8/10 can never be honestly scored; it also states no current value, so the target is unjudgeable as either ambition or progress, and a developer-satisfaction number would not move "Keep the lights on, cheaper" (line 7) — the objective's end-states are uptime and unit cost, which this KR shares no noun or measurement with.
- Scores affected: K1=1, K3=2, K5=0, K7=2 (PL1 set)
- Suggested rewrite: "KR PL1.3: Retire from PL1. Track instead under a developer-experience objective as: internal developer platform satisfaction `<baseline>`/10 → 8/10, quarterly survey of `<n>` internal engineers on the `<named survey instrument>`, reported from `<survey dashboard>`. If PL1 needs a third KR, measure the objective's own end-state instead: Sev-1 incidents affecting the public API `<baseline>` → `<target>` per quarter (source: `<incident tracker>`)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ## Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target (99.9%) is below the trailing-90-day actual the company already reports (99.95%), so the KR is achieved by letting reliability drift and encodes no ambition; "at or above" also makes the ceiling invisible, so a full quarter of regression still scores green.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (trailing 90 days, Datadog SLO monitor) → 99.98% monthly, measured on the same Datadog SLO monitor, with no month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is the delivery of an audit, not a result anyone outside the team moves — it carries neither an outside-moved measure nor a baseline→target pair, so nothing is countable; and because it is done-or-not-done, mid-quarter scoring can only read 0% or 100%, which hides whether the evidence work is on track until the quarter is over.
- Scores affected: K1=0, K2=1, K6=2 (PL2 set)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence controls closed 0/`<total controls>` → `<total controls>`/`<total controls>` (source: `<GRC tracker>`), observation window closed by `<date>`, and the auditor's Type II report received with `<n>` or fewer exceptions." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** Platform states it is deferring infra work other teams may be relying on this quarter; no requesting team is named in Platform's material, and no other team's OKRs are in scope, so whether any team's Q3 plan depends on that work cannot be checked here.
- "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** A stated capacity ceiling with no headroom for cross-team asks; the counterparties it would affect are outside this review.

No cross-team commitment made *to* Platform, and no dependency Platform declares *on* another team, appears anywhere in the Platform page (lines 3–16).

## 5. Prioritized action list

1. Re-baseline the uptime KR on the quoted 99.95% trailing-90-day figure and set a target above it — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
2. Replace the developer-satisfaction KR with an instrumented metric on a named survey and move it off PL1, or swap in a reliability/cost KR that PL1 actually claims — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, incl. AP-04 KR Without Baseline and AP-12 Orphan KR).
3. Convert the SOC 2 KR into a countable evidence-closure track with a named tracker so mid-quarter progress is visible — owner: Platform security/compliance owner (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Add one leading indicator to each KR set — a mid-cycle signal that predicts uptime/unit cost for PL1 and enterprise trust for PL2 — owner: Platform lead (Elena R.) (resolves §2 K6=2 on both sets).
5. Name the system of record and the measurement window on every KR (cloud-spend billing source, pen-test tracker, uptime monitor) — owner: Platform lead (Elena R.) (resolves §2 K5=1).
6. Add one KR to PL2 that measures the trust itself — e.g. enterprise security reviews passed without escalation — owner: Platform lead (Elena R.) with the enterprise sales sponsor (resolves §2 K7=2 on PL2).
7. Obtain the company/org strategy page for the next review so O4 Strategic Anchoring can be scored instead of recorded as a gap — owner: Platform lead (Elena R.) (resolves §2 O4 gap note).
