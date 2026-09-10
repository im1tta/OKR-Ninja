# Platform — Q3 2026 OKR review (single-team mode)

Scope: Platform team only (one team in confirmed scope → single-team mode). Period: Q3 2026, as stated by the source page. Source in scope: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` (Platform OKR page plus the Q2 2026 business-review appendix). No Atlassian source and no company strategy document were available.

## 1. Verdict summary

**Verdict: not trustworthy as written — one of the two objectives cannot be honestly scored at quarter end.**
Roll-up: **C (2.15)** — Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**.
Findings: **1 Critical, 2 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no survey, no scale of record and no current value, so it can never be honestly scored.
Two more Major defects sit on the measurement layer: the uptime KR targets less than the quoted trailing actual (AP-06 Sandbagged Target), and the SOC 2 KR is a completion event with no gradient (AP-01 Task Masquerading as KR · AP-02 Binary KR with No Gradient).
What is working: the page carries a commitment convention and a named owner, the cost KR states a real baseline→target pair, and the pen-test KR states its starting point — none of those fire an anti-pattern.
**Company-level strategy tracing was out of scope for this run**: no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored N/A, excluded from the roll-up, and recorded as a gap note in §2 (per `references/goodness-rubric.md`).
Recommended first action: rewrite KR PL1.3 against a named survey instrument with a stated baseline — or move it off PL1 — before the quarter's mid-point review.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 2 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 D (1.9, capped by a Critical anti-pattern), Objective PL2 C (2.4, capped by two Major anti-patterns). No team-level cap applied: 2 of 5 KRs carry K1 ≤ 1 (not more than half), and the strategy-trace cap requires a strategy corpus, which this run did not have.
- Platform: K5=1 — only one KR's metric has a named system of record; one names a metric no instrument could report.

**O4 gap note (mandated by the rubric, recorded here and never as a finding block):** O4 = **N/A** — no strategy source exists in the corpus, so O4 is scored N/A and excluded from the roll-up rather than guessed. Neither objective states a link to a named company priority, and no company priority is quotable to trace them to. Search trail: the only source in scope was the single file named above; it contains a Platform OKR section and a Q2 business-review appendix and no strategy, pillar, or company-priority text (searched for "strategy", "strategic", "company bet", "company priority/priorities", "pillar", "north star" — no match anywhere in the file). Strategic anchoring for both objectives is therefore unverified, not confirmed.

### Per-instance breakdown

Objectives:

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 2 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

- PL1 O1=3 — "Keep the lights on, cheaper" (`.../input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 7): an end-state with no deliverable and no delivery verb, but only the "cheaper" half names a change; "Keep the lights on" asserts today's state continuing.
- PL1 O2=2 — same span, line 7: "the lights" is one abstraction two readers would gloss differently (uptime only? on-call load? every service the team runs?), and the objective names no specific noun subject.
- PL1 O3=3 — the objective states no period itself; it is inherited unambiguously from "## Platform team — Q3 2026" (line 3) and "# Brightledger — Q3 2026 OKRs (portfolio export)" (line 1).
- PL2 O1=4 — "Earn enterprise trust" (line 12).
- PL2 O2=3 — "Earn enterprise trust" (line 12) is short and plain, but "trust" is a single abstraction the KR set silently narrows to security compliance; two readers would not agree on what counts.
- PL2 O3=3 — period inherited from "## Platform team — Q3 2026" (line 3), not restated in the objective.
- PL1 and PL2 O4=N/A — see the gap note above.

Key results (K1–K5; per-KR score = mean of K1..K5, caps applied after):

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." | 1 | 4 | 2 | 3 | 0 | 1.0 (capped from 2.0; K5=0) |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." | 3 | 2 | 3 | 3 | 2 | 2.6 |
| PL2.2 "Complete the SOC 2 Type II audit." | 0 | 1 | 2 | 3 | 2 | 1.0 (capped from 1.6; K1=0) |

- PL1.1 K1=3 — "Maintain API uptime at or above 99.9%." (line 8): metric, target and unit present; the baseline is missing from the KR but retrievable from the corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`.../input/sample-portfolio.md` › ## Appendix — Q2 2026 business review (extracts) › line 21) — and no measurement window is stated.
- PL1.1 K3=1 — sandbag: the target sits below the quoted trailing actual; see §3 AP-06.
- PL1.1 K4=3 — no per-KR owner; the accountable individual is derivable from the page field "Owner: Elena R." (line 4) and the team from "## Platform team — Q3 2026" (line 3). Same basis for all five KRs.
- PL1.1 K5=3 — the KR names no source, but the corpus names one obvious system of record for this exact metric: "(Datadog SLO monitor)" (line 21).
- PL1.2 K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9): metric, baseline, target and unit all present; measurement window unstated.
- PL1.2 K3=3 — a real stretch (the stated $4.10 → $3.20 unit-cost move) with no justification of the lever on the page; labeled committed by "Commitment: KRs are committed unless marked (aspirational)." (line 5).
- PL1.2 K5=2 — plausibly measurable, but no source is named for either half of the ratio: cloud billing, the finance ledger, and the transaction counter would each give a different number. Search trail: the only measurement system named anywhere in the file is the Datadog SLO monitor (line 21), which reports uptime, not spend.
- PL1.3 K1=1 — "Improve internal developer satisfaction score to 8/10." (line 10): a qualitative state dressed as a metric — the "score" is defined nowhere — and no current value is stated or retrievable.
- PL1.3 K3=2 — capped at 2 because no baseline or trend for this metric exists anywhere in the corpus; calibration is unverifiable, and the deficiency stands regardless of intent.
- PL1.3 K5=0 — the metric is defined only in someone's head; see §3 AP-09.
- PL2.1 K1=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13): metric, starting point and target present; the window is unstated, and the KR does not say whether findings opened during the quarter join the denominator.
- PL2.1 K2=2 — remediation throughput with no outcome link stated in the KR: closing the 7 findings is work completed, not a result an enterprise customer experiences.
- PL2.1 K3=3 — a properly-labeled committed KR (line 5 convention) at a modest, honest stretch from the stated "currently 7 open".
- PL2.1 K5=2 — plausibly measurable but the source is unnamed: the pen-test report and a security backlog would give different open counts, and neither is named in the corpus.
- PL2.2 K1=0 — "Complete the SOC 2 Type II audit." (line 14): a pure done/not-done milestone with nothing countable.
- PL2.2 K2=1 — a delivery milestone whose only failure mode is not finishing.
- PL2.2 K3=2 — capped at 2: no baseline or trend exists for audit completion, so calibration is unverifiable.
- PL2.2 K5=2 — no audit firm, report, or tracker is named anywhere in the corpus, so "complete" has no single system of record.

Set-level dimensions:

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 2 | 3 |

- PL1 K6=2 — all three KRs are end-state truths ("Maintain API uptime at or above 99.9%.", line 8; "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", line 9; "Improve internal developer satisfaction score to 8/10.", line 10) with no leading indicator that predicts any of them mid-cycle.
- PL1 K7=2 — one KR serves a different goal than the objective: "Improve internal developer satisfaction score to 8/10." (line 10) measures developer experience, while "Keep the lights on, cheaper" (line 7) is about uptime and cost, each already covered by its own KR.
- PL2 K6=2 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) and "Complete the SOC 2 Type II audit." (line 14) are both compliance milestones; neither is an outcome KR the other predicts, so the set gives no steering signal on trust itself.
- PL2 K7=3 — one coverage gap: nothing in the set measures anything an enterprise customer actually does, so hitting both KRs would not by itself convince a skeptic that "Earn enterprise trust" (line 12) happened.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 10)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: no survey, tool, scale, or population is defined for an "internal developer satisfaction score", and the corpus names no instrument that could report one — the only measurement system named anywhere in the file is the Datadog SLO monitor for uptime (line 21) — so the KR can never be honestly scored; it also states no current value, so 8/10 cannot be judged as ambition or progress, and its success would not show that "Keep the lights on, cheaper" (line 7) happened.
- Scores affected: K1=1, K3=2 (capped, calibration unverifiable), K5=0, K7=2 for the PL1 set; the KR score is capped at 1.0 (K5=0) and Objective PL1 at 1.9 (Critical cap).
- Suggested rewrite: "KR PL1.3 (moved under a developer-experience objective, e.g. 'Internal teams ship without waiting on Platform'): Developer satisfaction with the internal platform — one 1–10 question asked quarterly of the `<N>` engineers outside Platform in `<named survey tool>`, response rate ≥ `<threshold>`% — `<baseline>`/10 → 8/10." If the KR must stay under PL1, replace it instead with one that serves that objective: "KR PL1.3: Sev-1 incidents per quarter `<baseline>` → `<target>` (source: `<incident tracker>`)." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ## Appendix — Q2 2026 business review (extracts) › line 21)
- Why it's a problem: the committed target of 99.9% sits below the quoted trailing-90-day actual of 99.95%, so the KR is already met on the day it was written and can be "hit" while reliability degrades — it encodes no ambition and gives the quarter no signal.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, measured monthly on the same Datadog SLO monitor, with no single month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable — it opens with "Complete", names no metric, and gives no starting point or countable denominator — so nothing about it is progress-measurable during the quarter and mid-cycle scoring can only read 0% or 100%. A team three weeks from its audit report and a team that has collected no evidence look identical.
- Scores affected: K1=0, K2=1, K5=2; the KR score is capped at 1.0 (K1=0) and Objective PL2 at 2.4 (two Major anti-patterns on one OKR).
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence requests closed `<baseline>`/`<total>` → `<total>`/`<total>`, tracked weekly in `<audit tracker>`; observation window opens by `<date>` and the Type II report is received from `<audit firm>` by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- **unverified — counterparty not in scope** — "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 16). Platform declares its capacity fully consumed and defers infra requests that other teams would raise; whether any other team's Q3 plan depends on that deferred work cannot be checked with one team in scope.

Search trail for this section: Platform's own material (lines 3–16) names no other team and contains no "depends on", "blocked by", or "with `<team>`" phrasing; the appendix (lines 18–23) mentions Payments and Growth, but those lines are business-review extracts, not statements of a Platform dependency, and those teams' OKRs are outside this run's scope.

## 5. Prioritized action list

1. Rewrite KR PL1.3 against a named survey instrument with a stated baseline, or move it under a developer-experience objective — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, incl. AP-04 KR Without Baseline and AP-12 Orphan KR).
2. Reset the uptime target above the quoted 99.95% trailing baseline and state its measurement window — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a graded evidence-closure measure with a named tracker and dates — owner: Platform lead (Elena R.), with the SOC 2 program owner (resolves §3 AP-01 Task Masquerading as KR · AP-02 Binary KR with No Gradient).
4. Name the system of record for cloud spend per 1,000 transactions and for open pen-test findings on the OKR page — owner: Platform lead (Elena R.) (addresses §2 K5=1, the team's lowest dimension).
5. Add one leading indicator to each objective's KR set so the quarter is steerable before its final week — owner: Platform lead (Elena R.) (addresses §2 K6=2 on both sets).
6. Confirm with the teams that raise infra requests which of them the Q4 deferral actually blocks — owner: Platform lead (Elena R.) (addresses the §4 outbound dependency note).
7. Add an explicit link from each objective to a named company priority once a strategy page exists, and re-run this review with it in scope — owner: Platform lead (Elena R.) (addresses the §2 O4 gap note).
