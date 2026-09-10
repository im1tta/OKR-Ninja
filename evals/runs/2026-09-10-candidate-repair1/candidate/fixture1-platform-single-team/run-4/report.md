# OKR-Ninja — Single-team review: Platform, Q3 2026

*Mode: single-team (exactly one team in confirmed scope — Platform). Period: Q3 2026, as stated by the source page. Source: `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md` (Platform OKR page + Q2 2026 business-review appendix). No Atlassian source available; no other corpus consulted.*

## 1. Verdict summary

**Verdict: At risk — the set is not trustworthy as written.** Platform roll-up: **C (2.15)** — Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**.
Findings: **1 Critical, 2 Major, 0 Minor** across 2 objectives and 5 key results.
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names a score with no instrument, no baseline, and no system of record anywhere in the two sources in scope, so the KR can never be honestly graded.
Two of five KRs cannot be scored on progress at all: one is a done/not-done milestone ("Complete the SOC 2 Type II audit."), one is unmeasurable as written.
The one committed reliability number is a **sandbag**: the target 99.9% sits below the 99.95% trailing-90-day actual quoted in the team's own Q2 review.
The cost KR ("from $4.10 to $3.20") is the set's healthiest: metric, baseline, target, and unit all present.
**Company-level strategy tracing was out of scope for this run** — no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored **N/A** for both objectives and excluded from the roll-up, per the rubric's no-strategy-source rule. This is a corpus gap, not a pass: nothing in scope shows either objective connects to a stated company priority.
Recommended first action: rewrite KR PL1.3 against a named survey instrument with a baseline, or drop it from the OKR set (resolves §3 AP-09).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 2 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (weighted 2.35, capped at 1.9 by the confirmed Critical AP-09), Objective PL2 **C (2.4)** (weighted 2.62, capped at 2.4 by two Major anti-patterns on the OKR). No team-level cap applied: 2 of 5 KRs carry K1 ≤ 1 (not "more than half"), and the strategy-trace cap requires a strategy corpus, which is absent.

- Platform: K5=1 — two KRs name no system of record and one has none in principle (AP-09 Metric Nobody Can Measure).

**O4 gap note (rubric-mandated):** O4 = **N/A** for PL1 and PL2. No strategy source exists in the corpus. Sources searched: the Platform OKR page (Confluence 88221, PLAT-OKR-Q3) and the Q2 2026 business-review appendix (Confluence 88104, Q2-REVIEW) — the only two sources in this file and the only material in scope; no Atlassian connection was available and no strategy document was provided. Neither objective states a parent priority, so the link is not guessed: O4 is excluded from the roll-up rather than scored 0.

### Per-instance breakdown

Objectives:

| Instance | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 2 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

Key results:

| Instance | K1 | K2 | K3 | K4 | K5 | Per-KR |
|---|---|---|---|---|---|---|
| PL1.1 uptime | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 cloud spend | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 developer satisfaction | 1 | 3 | 2 | 3 | 0 | 1.0 (capped: K5=0) |
| PL2.1 pen-test findings | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 SOC 2 audit | 0 | 1 | 2 | 3 | 2 | 1.0 (capped: K1=0) |

KR sets: PL1 — K6=2, K7=2. PL2 — K6=3, K7=3.

Spans driving each score ≤ 3 (per the rubric's "scores name their spans" rule):

- O1=3 (PL1) — "Keep the lights on, cheaper" (`…/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 7`): outcome-framed with no delivery verb, but half the statement ("Keep the lights on") is continuation of standing duty rather than a changed end-state; only ", cheaper" names a change.
- O2=2 (PL1) — "Keep the lights on, cheaper" (line 7): "the lights" is a metaphor, not a specific noun subject, and two readers gloss it differently — the KR set itself reads it two ways, covering both externally-facing "API uptime" (line 8) and "internal developer satisfaction" (line 10).
- O2=3 (PL2) — "Earn enterprise trust" (`… › ### Objective PL2: Earn enterprise trust › line 12`): memorable and short, but "trust" is left unqualified (trust enough to do what?), so two readers could set different bars.
- O3=3 (both) — no period is restated in either objective; the cycle is inherited unambiguously from "## Platform team — Q3 2026" (line 3) and "*Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05*" (line 4).
- K1=3 (PL1.1) — "Maintain API uptime at or above 99.9%." (line 8): metric, target, and unit present; baseline absent from the KR but retrievable from the cited appendix; measurement window unstated.
- K1=3 (PL1.2) — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9): baseline, target, unit, and denominator all present; measurement window unstated.
- K1=1 (PL1.3) — "Improve internal developer satisfaction score to 8/10." (line 10): a qualitative state dressed as a metric, with no defined score.
- K1=3 (PL2.1) — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13): baseline (7 open) → target (0 open) over a defined population; window unstated.
- K1=0 (PL2.2) — "Complete the SOC 2 Type II audit." (line 14): a pure done/not-done milestone; nothing countable.
- K2=3 (PL1.3) — "Improve internal developer satisfaction score to 8/10." (line 10): it is a state internal developers experience, but no causal link to the objective is stated.
- K2=3 (PL2.1) — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13): a risk-state proxy whose link to enterprise trust is credible but not stated in the text.
- K2=1 (PL2.2) — "Complete the SOC 2 Type II audit." (line 14): a delivery milestone; the only failure mode is not finishing.
- K3=1 (PL1.1) — target "at or above 99.9%" (line 8) sits below the quoted trailing actual "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21) — sandbag; see §3 AP-06.
- K3=3 (PL1.2) — "from $4.10 to $3.20." (line 9): a stretch of roughly a fifth of unit cost, committed by the page convention, with no justification given.
- K3=2 (PL1.3) — no baseline or prior actual for any developer-satisfaction score exists in either source in scope; calibration is unverifiable (rubric cap).
- K3=3 (PL2.1) — "(currently 7 open)" (line 13) gives the baseline; clearing all 7 in a quarter is a stated, committed stretch with no justification.
- K3=2 (PL2.2) — no baseline or prior audit actual anywhere in scope; calibration unverifiable (rubric cap).
- K4=3 (all five KRs) — no per-KR owner is stated; the accountable individual is derivable from the same page: "Owner: Elena R." (line 4).
- K5=3 (PL1.1) — the system of record is not named in the KR but is identifiable from the corpus: "(Datadog SLO monitor)" (line 21).
- K5=2 (PL1.2) — "cloud spend per 1,000 transactions" (line 9) names no dashboard; cloud billing and finance reporting would plausibly give different numbers.
- K5=0 (PL1.3) — "internal developer satisfaction score" (line 10) names no survey, tool, or scale; nothing in either source in scope reports such a score.
- K5=2 (PL2.1) — "pen-test findings rated High or above" (line 13) names no tracker of record.
- K5=2 (PL2.2) — "the SOC 2 Type II audit" (line 14): the auditor's report is a plausible record, but no tracker or report is named.
- K6=2 (PL1 set) — all three KRs are end-of-quarter truths ("Maintain API uptime at or above 99.9%.", "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", "Improve internal developer satisfaction score to 8/10." — lines 8–10); none is a leading indicator that predicts another, so there is no mid-cycle steering signal.
- K7=2 (PL1 set) — "Improve internal developer satisfaction score to 8/10." (line 10) measures a different domain from the objective's stated end-state, and the uptime KR's sandbagged target means hitting it demonstrates nothing about "Keep the lights on" (line 7).
- K6=3 (PL2 set) — a mix exists but the pairing is loose: "(currently 7 open)" (line 13) gives a mid-cycle signal, while the other KR is a single event, "Complete the SOC 2 Type II audit." (line 14).
- K7=3 (PL2 set) — one coverage gap: both KRs measure compliance work, and nothing measures anything an enterprise customer does or experiences, so hitting both would not convince a skeptic that "Earn enterprise trust" (line 12) happened.

**Checked and not filed** (recorded so the absence is not read as an oversight): AP-08 Committed vs Aspirational Not Labeled does not fire — the page states a convention: "*Commitment: KRs are committed unless marked (aspirational).*" (line 5). AP-05 Everything Is a P0 does not fire — two objectives, no priority labels. AP-10 BAU Dressed as OKR does not fire on PL1 — the objective names a change (", cheaper") and KR PL1.2 realizes that change with a baseline→target pair ("from $4.10 to $3.20."). AP-01 Task Masquerading as KR does not fire on PL2.1 — "(currently 7 open)" supplies a starting point over a countable denominator, so the KR is progress-measurable all quarter. AP-13 Ambiguous Denominator does not fire on PL1.2 — the denominator ("per 1,000 transactions") and the population of PL2.1 ("pen-test findings rated High or above") are both stated. AP-15 Ownerless KR does not fire — "Owner: Elena R." is on the page (K4=3).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-04 KR Without Baseline
- Why it's a problem: no survey, scale definition, cadence, or system of record for a "developer satisfaction score" exists anywhere in the material in scope — the Platform OKR page (Confluence 88221) and the Q2 2026 business review (Confluence 88104), both searched in full — so the number can never be honestly produced or disputed; and with no current value stated or retrievable, "to 8/10" cannot be judged as either ambition or progress.
- Scores affected: K5=0, K1=1, K3=2 (unverifiable-calibration cap), K7=2
- Suggested rewrite: "KR PL1.3 (committed): Internal developer satisfaction among the `<N>` engineers outside Platform who ship on the platform, measured by a quarterly 5-question survey on `<named survey instrument>` (1–10 scale, response rate ≥ 60%), run in week 2 and week 12 of Q3: `<baseline from the week-2 run>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ## Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target sits below the team's own quoted trailing-90-day actual, so the KR is already met on the day the quarter opens and the team could let reliability degrade by half a nine and still score 100%; it encodes no improvement and no defence of the current level.
- Scores affected: K3=1, K7=2
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% (Q2 trailing-90-day actual, per the Datadog SLO monitor) → 99.98%, monthly and quarter-to-date on that same monitor, with no single month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb with no metric and no baseline→target pair — no starting point, and no measure that anyone outside Platform moves — so it restates the work instead of measuring a result; and because it is a single done/not-done event, it can only ever score 0% or 100%, hiding every week of slipped evidence collection until the quarter ends.
- Scores affected: K1=0, K2=1, K6=3, K7=3
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II controls with a complete audit-period evidence sample accepted by the auditor: 0/`<N>` → `<N>`/`<N>`, tracked weekly in `<audit tracker>`, with zero unremediated exceptions and the Type II report issued by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- **unverified — counterparty not in scope** — Platform states it will hold other teams' infrastructure work for the quarter: "Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-candidate-repair1/candidate/fixture1-platform-single-team/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 16`). The same note gives the reason: "Q3 is fully committed between SOC 2 evidence collection and the cost work." (same source ref, line 16). No requesting team is named, and no other team's OKRs are in scope, so whether any team is counting on Platform infra work this quarter cannot be checked here — this is recorded as a note, not a finding, and carries no severity. It would be the input to a cross-team dependency check in a portfolio-mode run.

## 5. Prioritized action list

1. Rewrite KR PL1.3 against a named survey instrument with a week-2 baseline run, or move developer satisfaction to a health metric outside the OKR set — owner: Platform lead (Elena R., page owner) (resolves §3 AP-09 Metric Nobody Can Measure, and its Also: AP-04 KR Without Baseline).
2. Reset the uptime KR above the quoted 99.95% trailing baseline and name the Datadog SLO monitor in the KR text — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a controls-evidenced ratio with a weekly tracker so mid-quarter slippage is visible — owner: Platform lead (Elena R.), with the SOC 2 audit coordinator (resolves §3 AP-01 Task Masquerading as KR, and its Also: AP-02 Binary KR with No Gradient).
4. Add one enterprise-side outcome KR to PL2 (for example security-review cycles cleared or enterprise deals unblocked) so the objective is provable by something other than compliance work — owner: Platform lead (Elena R.) (resolves §2 K7=3 for the PL2 set).
5. Name the system of record for cloud spend per 1,000 transactions and for the pen-test finding tracker in the KR text — owner: Platform lead (Elena R.) (resolves §2 K5=2 on PL1.2 and PL2.1).
6. Add a leading indicator to PL1 that predicts the cost and uptime results mid-quarter — owner: Platform lead (Elena R.) (resolves §2 K6=2 for the PL1 set).
7. Obtain the company or portfolio strategy document and re-run the O4 Strategic Anchoring trace for both objectives, which this run could not perform — owner: Platform lead (Elena R.) with the OKR process owner (resolves §2 O4 gap note).
8. Raise the "Holding all non-critical infra requests until Q4." note with the teams that depend on Platform infra before mid-quarter — owner: Platform lead (Elena R.) (resolves §4 outbound dependency note).
