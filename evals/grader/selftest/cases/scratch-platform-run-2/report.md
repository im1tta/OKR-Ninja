# Platform — Q3 2026 OKR Review (single-team mode)

*Team: Platform · Period: Q3 2026 (as stated by the source page) · Mode: single-team (exactly one team in confirmed scope) · Corpus searched, in full: `input.md` — the Platform team OKR page (Confluence 88221 / PLAT-OKR-Q3) and the Q2 2026 business-review appendix (Confluence 88104 / Q2-REVIEW). No Atlassian connection was available and no other source was consulted.*

## 1. Verdict summary

**Verdict: Usable but not yet trustworthy — one objective is a restated standing duty and two of five KRs cannot be honestly scored as written.**

Roll-up grade: **C (2.3)** for the team; the two objectives split sharply — PL1 **D (1.9)**, PL2 **B (2.8)**.
Findings: **1 Critical, 5 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names a score with no instrument, no baseline, and no measuring system anywhere in the corpus, so it can never be honestly scored.
Second-worst by consequence: **AP-06 Sandbagged Target** — the committed uptime target sits *below* the trailing-90-day actual quoted in the same file, so the KR is passed on the day it is written.
Company-level strategy tracing was **out of scope**: no company/org strategy document was provided, so O4 Strategic Anchoring is scored N/A for both objectives and excluded from the roll-up rather than guessed (gap note in §2).
Recommended first action: re-baseline KR PL1.1 against the quoted 99.95% trailing-90-day actual and replace KR PL1.3 with a measurable instrument or move it out of the OKR set — owner: Platform lead (Elena R.).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 2 | N/A | 2 | 2 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.3)** — PL1 D (1.9), PL2 B (2.8).
- Platform: K1=2 — one KR is a pure done/not-done milestone and one states a target with no baseline.

**O4 gap note (rubric-mandated).** O4 = **N/A** for both objectives, excluded from the roll-up. Search trail: the entire corpus listed in the header was read; it contains one OKR page and one Q2 business-review appendix and no company, portfolio, or org strategy artifact, and neither objective states a parent ("supports Company Bet…"-style link) — so no strategy source exists to trace against and no anchoring was guessed. Consequence to record: **no objective in this set is traceable to a stated company priority**, and the rubric's team-level cap for untraceable strategy does not fire only because the strategy corpus is absent, not because the traces are sound. Supplying the Q3 company priorities page would let O4 be scored on a re-run.

### Per-instance breakdown

Objectives (O1–O4):

- **PL1** — O1=2 · O2=2 · O3=2 · O4=N/A. Drivers: "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 7`). O1=2 — "keep the lights on" is the team's standing state, not a changed end-state; strip it and the remaining "cheaper" names no subject. O2=2 — "keep the lights on" is an idiom two readers gloss differently (uptime? on-call load? all infra?) and the line carries no specific noun subject. O3=2 — the period is inherited unambiguously from "Platform team — Q3 2026" (`input.md › Platform team — Q3 2026 › line 3`), but a "keep the lights on" objective is an open-ended standing journey crammed into one cycle.
- **PL2** — O1=4 · O2=4 · O3=3 · O4=N/A. Text scored: "Earn enterprise trust" (`input.md › Objective PL2: Earn enterprise trust › line 12`). O3=3 — the period is inherited from the page heading "Platform team — Q3 2026" (`input.md › Platform team — Q3 2026 › line 3`) rather than restated in the objective.

Key results (K1–K5):

- **PL1.1** — K1=3 · K2=4 · K3=1 · K4=3 · K5=3. Text: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 8`). K1=3 — metric, target and unit present, baseline absent from the KR but retrievable from the cited corpus: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input.md › Appendix — Q2 2026 business review (extracts) › line 21`); measurement window unstated. K3=1 — target below that quoted baseline (see §3 AP-06). K4=3 — owning team named and the individual is derivable from the same page: "Owner: Elena R." (`input.md › Platform team — Q3 2026 › line 4`). K5=3 — no source named in the KR, but the corpus shows one obvious system of record, the "Datadog SLO monitor" (line 21).
- **PL1.2** — K1=3 · K2=4 · K3=3 · K4=3 · K5=2. Text: "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`input.md › Objective PL1: Keep the lights on, cheaper › line 9`). K1=3 — metric, numeric baseline and target and unit all present; measurement window unstated. K3=3 — a clear stretch off the stated $4.10 baseline, justification and mechanism absent. K4=3 — "Owner: Elena R." (line 4). K5=2 — plausibly measurable but no system of record is named and the denominator "per 1,000 transactions" has more than one candidate reading in this corpus (the appendix uses "transactions" for Payments volume, line 22), so two systems would return different numbers.
- **PL1.3** — K1=1 · K2=2 · K3=2 · K4=3 · K5=1. Text: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`). K1=1 — a qualitative state dressed as a metric: no defined score, no baseline. K2=2 — measures an internal state with no stated causal link to any outcome outside the team. K3=2 — capped: no baseline or prior actual exists anywhere in the searched corpus, so calibration is unverifiable. K4=3 — "Owner: Elena R." (line 4). K5=1 — the measurement requires a survey instrument that does not exist in the corpus and no KR or task builds one.
- **PL2.1** — K1=4 · K2=3 · K3=3 · K4=3 · K5=2. Text: "Close 100% of pen-test findings rated High or above (currently 7 open)." (`input.md › Objective PL2: Earn enterprise trust › line 13`). K2=3 — remediation throughput is a proxy for the objective's trust outcome; the causal link is implied by the objective, not stated. K3=3 — clearing the stated 7-finding backlog is a real stretch, justification absent; committed per the page convention. K4=3 — "Owner: Elena R." (line 4). K5=2 — the population "(currently 7 open)" is stated, but no tracker or report of record is named and the corpus contains none.
- **PL2.2** — K1=0 · K2=1 · K3=2 · K4=3 · K5=2. Text: "Complete the SOC 2 Type II audit." (`input.md › Objective PL2: Earn enterprise trust › line 14`). K1=0 — nothing countable; a pure done/not-done milestone (triggers the rubric's K1=0 cap, so this KR's score is capped at 1.0). K2=1 — a delivery milestone, not a measured result. K3=2 — capped: no baseline or magnitude exists to calibrate, so calibration is unverifiable. K4=3 — "Owner: Elena R." (line 4). K5=2 — verification would rest on the auditor's report, which is named nowhere in the corpus.

KR-set dimensions (K6–K7):

- **PL1 set** — K6=2 · K7=2. K6=2 — "Maintain API uptime at or above 99.9%." and "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (lines 8–9) are both end-state measures and nothing in the set is a leading indicator that predicts either (no error-budget burn, no cost-driver metric). K7=2 — "Improve internal developer satisfaction score to 8/10." (line 10) is an orphan serving a different end-state than "Keep the lights on, cheaper" (line 7); see §3 AP-12.
- **PL2 set** — K6=3 · K7=3. K6=3 — a mix is present (pen-test closure ahead of the audit outcome) but the pairing is never stated in the text. K7=3 — one coverage gap: both KRs measure internal compliance artifacts and nothing measures whether an enterprise customer actually behaves as if it trusts Brightledger.

**Anti-pattern catalog sweep (full AP-01…AP-15).** Fired: AP-02, AP-04, AP-06, AP-09, AP-10, AP-12 (§3). Swept and **not** fired, with reason: AP-01 — the only qualifying KR is "Complete the SOC 2 Type II audit." (line 14), reported under its canonical match AP-02 rather than twice; AP-03 — no cumulative-total metric anywhere in the set; AP-05 — two objectives, no priority labels at all, below the catalog's threshold; AP-07 — no target/baseline ratio above 5; AP-08 — the page states the convention explicitly, "KRs are committed unless marked (aspirational)." (`input.md › Platform team — Q3 2026 › line 5`); AP-11 — "Keep the lights on, cheaper" (line 7) qualifies one operational end-state by cost rather than joining unrelated end-states; AP-13 — the one ratio KR, "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13), states its population, and PL1.2's loose denominator is carried as K5=2 rather than escalated; AP-14 — no KR uses a calendar date as its measure; AP-15 — an accountable individual is named on the page, "Owner: Elena R." (line 4).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the "internal developer satisfaction score" quantifies an internal state with no instrument — the full corpus searched (the PLAT-OKR-Q3 page and the Q2-REVIEW appendix, the only sources available) names no survey, dashboard, or tool that could report it, and no KR or task builds one. The KR can therefore never be honestly scored, and any number claimed at quarter end is unfalsifiable.
- Scores affected: K5=1, K1=1 (and, as a Critical on PL1, the rubric's per-OKR cap of 1.9 applies to Objective PL1)
- Suggested rewrite: "KR PL1.3 (committed): stand up a quarterly Platform Developer Experience pulse (existing `<survey tool>`, n ≥ `<respondents>` across the eng org, first run by `<date>` in Q3); 'I can ship without fighting our infrastructure' agreement score `<baseline from first run>`/10 → 8/10 on the following run." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the target (99.9%) sits below the trailing-90-day actual quoted in the same file (99.95%), and it is a committed KR under the page's convention — so the KR is already met on the day it was written and consumes a quarter's attention while encoding no ambition.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.97%, measured monthly on the same Datadog SLO monitor, with error-budget burn reviewed weekly." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input.md › Objective PL2: Earn enterprise trust › line 14`)
- Why it's a problem: the KR is done/not-done with no numeric scale, so mid-cycle it can only score 0% or 100% and the team gets no steering signal until the audit lands; it is also the catalog's AP-01 shape (a "Complete…" deliverable with no baseline→target pair), reported here under its canonical binary-milestone match.
- Scores affected: K1=0, K2=1 (K1=0 caps this KR's per-KR score at 1.0)
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence requests closed 0/`<N>` → `<N>`/`<N>` with zero auditor-raised exceptions outstanding, and the Type II report received by `<date>` in Q3." [proposal — placeholder target]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Evidence: "Maintain API uptime at or above 99.9%." (`input.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: "Keep the lights on" is the team's standing job stated with no delta, and its lead KR is a "Maintain" of an already-exceeded level — the objective is achieved by default staffing and displaces a real goal from a two-objective quarter.
- Scores affected: O1=2, O2=2, O3=2
- Suggested rewrite: "Objective PL1: Run the platform for measurably less per transaction without customers noticing — KR: cloud spend per 1,000 transactions $4.10 → $3.20; KR: customer-visible incidents `<baseline>` → `<target>`." Move the standing uptime duty out of the OKR set into a health-metric section with a floor of 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) reviewed monthly. [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Why it's a problem: the KR states a target with no "from" and no current value, and none is retrievable — both sources in the corpus were searched (the PLAT-OKR-Q3 page and the Q2-REVIEW appendix) and neither reports a developer-satisfaction figure — so both the ambition and mid-quarter progress are unjudgeable.
- Scores affected: K1=1, K3=2 (calibration unverifiable, capped)
- Suggested rewrite: "KR PL1.3 (committed): internal developer satisfaction `<Q2 actual>`/10 (baseline, per `<named survey instrument>`) → 8/10, same instrument, same population, re-run in the last two weeks of Q3." [proposal — placeholder target]

### [Major] AP-12 Orphan KR — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence: "Keep the lights on, cheaper" (`input.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Why it's a problem: the KR shares no noun or domain with its objective's end-states (uptime and unit cost) and no causal chain from developer satisfaction to either is stated or reachable in two steps — hitting it would not move "Keep the lights on, cheaper", and hitting the other two would not require it.
- Scores affected: K7=2 (PL1 set), K2=2
- Suggested rewrite: replace with a KR that moves the stated objective — "KR PL1.3 (committed): unplanned infrastructure toil `<baseline>` → `<target>` hours per on-call week (source: `<named on-call/ticket system>`)" — and relocate the developer-satisfaction goal to its own Developer Experience objective or to a team health-metric section outside the OKR set. [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`input.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** The requesting teams are not named here and no other team's OKRs are in scope, so whether any team is counting on Platform infra work this quarter cannot be checked from this material.
- "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`input.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** A full-capacity declaration that would need to be reconciled against any other team's OKRs that assume Platform capacity in Q3; no counterparty material is available to reconcile it against.

## 5. Prioritized action list

1. Rewrite KR PL1.3 onto a real instrument with a stated baseline, or drop it from the OKR set this quarter — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, §3 AP-04 KR Without Baseline, §3 AP-12 Orphan KR).
2. Re-baseline KR PL1.1 against the quoted 99.95% trailing-90-day actual and set a target above it — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert KR PL2.2 from a done/not-done audit milestone into a graded evidence-closure count with a date for the report — owner: Platform lead (Elena R.), with the SOC 2 evidence owner (resolves §3 AP-02 Binary KR with No Gradient).
4. Recast Objective PL1 as a cost-and-experience delta and move the standing uptime duty to a health-metric section — owner: Platform lead (Elena R.) (resolves §3 AP-10 BAU Dressed as OKR).
5. Name the system of record for cloud spend per 1,000 transactions and define which transactions form the denominator — owner: Platform lead (Elena R.) with Finance (raises K5 from 2 on KR PL1.2, §2 per-instance breakdown).
6. Name the tracker of record for pen-test findings and state whether the 100% target covers only the 7 currently open High+ findings or any found during Q3 — owner: Platform security lead (raises K5 on KR PL2.1, §2 per-instance breakdown).
7. Add one leading indicator to the PL1 set that predicts the cost outcome mid-quarter (for example a weekly cost-per-transaction run rate) — owner: Platform lead (Elena R.) (raises K6=2 on the PL1 set, §2 per-instance breakdown).
8. Add one customer-side KR to PL2 so "Earn enterprise trust" is evidenced by enterprise behavior and not only by internal compliance artifacts — owner: Platform lead (Elena R.) with the enterprise account team (raises K7=3 on the PL2 set, §2 per-instance breakdown).
9. Supply the Q3 company priorities page and re-run O4 Strategic Anchoring so both objectives can be traced or shown to be orphaned — owner: Platform lead (Elena R.) (resolves the §2 O4 gap note).
10. Reconcile the "fully committed" Q3 capacity declaration with any team counting on held infra requests before mid-quarter — owner: Platform lead (Elena R.) with the eng leadership group (resolves §4 outbound dependency notes).
