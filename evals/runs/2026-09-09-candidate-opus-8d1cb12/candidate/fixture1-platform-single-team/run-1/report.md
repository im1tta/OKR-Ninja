# OKR-Ninja — Single-team review: Platform, Q3 2026

*Mode: single-team (exactly one team in confirmed scope). Source of record: `input/sample-portfolio.md` (the Platform OKR page, lines 3–16, and the Q2 2026 business-review appendix, lines 18–23). No Atlassian source connected; no strategy document provided. All source refs below are `<file path> › <nearest heading> › line N` against that file.*

## 1. Verdict summary

**Verdict: At risk — one of the two objectives (PL1) is not trustworthy as written.** Roll-up grade **C (2.15)** for the team; per-objective, **PL1 D (1.9)** and **PL2 C (2.4)**.
Findings: **1 Critical, 3 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, and no survey, dashboard, or prior score exists anywhere in the two sources searched, so the KR can never be honestly scored.
Second-worst: the reliability KR is a sandbag — the OKR page targets "at or above 99.9%" while the appendix already reports 99.95% trailing 90 days, so the KR is met on the day it is written.
The strong material is real and should be protected: "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." is a complete baseline→target outcome KR, "Earn enterprise trust" is a genuine end-state objective, and the page carries an explicit commitment convention (line 5), so no AP-08 Committed vs Aspirational Not Labeled finding arises.
**Company-level strategy tracing was out of scope for this run: no company/org strategy document was provided or found in the corpus.** O4 Strategic Anchoring is therefore scored N/A and excluded from the roll-up (see the gap note in §2); no objective is credited or penalised for strategic anchoring.
Recommended first action: replace KR PL1.3 with a measurable developer-satisfaction KR built on a named instrument, or drop it from Q3 (§3, AP-09).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — PL1 D (1.9, capped by a Critical anti-pattern), PL2 C (2.4, capped by two Major anti-patterns on one OKR).

- Platform: K5=1 — three of five KRs name no system of record; one names none that exists.

**O4 gap note (rubric-mandated):** O4 shows **N/A** because no strategy source exists in the corpus. Search trail: the entire file `input/sample-portfolio.md` (lines 1–23) was searched for a company/org strategy artifact, strategic pillar, company bet, or stated priority; the only non-OKR content is the Q2 business-review appendix, which reports outcomes, not strategy. Neither objective states a parent goal: no `supports…`, `parent`, or company-goal text appears anywhere in lines 3–16. The gap is real — it is recorded here, not as a finding — and O4 is excluded from the roll-up rather than guessed.

### Per-instance breakdown

**Objective PL1** — "Objective PL1: Keep the lights on, cheaper" (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- O1=2 — "Keep the lights on" is a standing state, not a change in the world; only "cheaper" carries a delta, so half the objective describes the team's default duty.
- O2=2 — "the lights" is figurative: which systems, and at what service level, two readers would gloss differently (the page pins it to API uptime only in KR PL1.1, line 8).
- O3=3 — period is inherited unambiguously from "## Platform team — Q3 2026" (line 3) but is not restated in the objective text.
- O4=N/A — no strategy source in corpus (gap note above).
- K6=2 (set) — "Maintain API uptime at or above 99.9%." (line 8), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) and "Improve internal developer satisfaction score to 8/10." (line 10) are all end-state outcome readings; no leading indicator (workload migration, toil, reserved-capacity coverage) is stated that would predict any of them mid-cycle.
- K7=2 (set) — "Improve internal developer satisfaction score to 8/10." (line 10) measures an end-state the objective does not state; hitting it would not show that the platform stayed up or got cheaper.

**KR PL1.1** — "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- K1=3 — metric, target and unit present; no baseline on the OKR page, but retrievable from the corpus: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`). Measurement window unstated on the KR.
- K2=4 — "Maintain API uptime at or above 99.9%." measures availability as customers experience it.
- K3=1 — sandbag: "at or above 99.9%" sits below the quoted 99.95% actual (line 21). See §3 AP-06.
- K4=3 — owning team named in the page heading (line 3) and an individual is derivable from the same source: "Owner: Elena R." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 4`); no per-KR accountable individual.
- K5=3 — the KR names no source, but the corpus names a single obvious system of record for this metric: "(Datadog SLO monitor)" (line 21).

**KR PL1.2** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`)
- K1=3 — metric, unit, baseline "$4.10" and target "$3.20" all present; only the measurement window is unstated.
- K2=4 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." is a unit-economics result, normalised by a defined denominator.
- K3=3 — a clear stretch (a 22% cut against the stated $4.10 baseline), committed by the page convention "KRs are committed unless marked (aspirational)." (`input/sample-portfolio.md › Platform team — Q3 2026 › line 5`), but no justification or mechanism is stated.
- K4=3 — as PL1.1: "Owner: Elena R." (line 4), no per-KR individual.
- K5=2 — plausibly measurable, but no system of record is named for either cloud spend or the transaction denominator, and a billing export versus a finance ledger would give different numbers. No finding filed: the measurement is possible today with systems any team of this kind has.
- **Strength — no finding.** This KR is the model the other four should follow.

**KR PL1.3** — "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- K1=2 — target "8/10" with no baseline; search trail: lines 1–23 of the file contain no current developer-satisfaction value and no prior survey result (the appendix reports only uptime, chargeback rate and signups).
- K2=4 — internal developers sit outside the Platform team, so their satisfaction is an outcome, not an output.
- K3=2 — capped at the rubric's unverifiable ceiling: with no baseline or prior actual anywhere in the corpus, calibration of "8/10" cannot be judged.
- K4=3 — as PL1.1: "Owner: Elena R." (line 4).
- K5=0 — no instrument, survey, cadence, population or scale definition exists in the corpus for "internal developer satisfaction score"; the only measurement system named anywhere is the "Datadog SLO monitor" (line 21). Per the roll-up caps, this KR's score is capped at 1.0. See §3 AP-09.

**Objective PL2** — "Objective PL2: Earn enterprise trust" (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`)
- O1=4 — "Earn enterprise trust" states a changed end-state with no delivery verb; it could be reached by routes other than the two the team has chosen.
- O2=4 — "Earn enterprise trust" is a three-word, plain-language one-liner with a specific audience and no metric embedded.
- O3=3 — period inherited unambiguously from "## Platform team — Q3 2026" (line 3), not restated.
- O4=N/A — no strategy source in corpus (gap note above).
- K6=3 — a mix exists but the pairing is loose: "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) steers mid-cycle toward the lagging "Complete the SOC 2 Type II audit." (line 14), but no text states that link.
- K7=3 — one coverage gap: both KRs are compliance artefacts; nothing measures anything an enterprise customer or prospect experiences or decides, so a skeptic could see both hit and still doubt "Earn enterprise trust".

**KR PL2.1** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`)
- K1=3 — metric, target "100%" and an explicit baseline "(currently 7 open)"; the denominator is pinned to findings "rated High or above", only the measurement window is unstated.
- K2=3 — a proxy for security posture with a credible link to the stated objective, not a customer-experienced outcome in itself.
- K3=3 — committed by the page convention (line 5) at a modest, honest stretch: seven open items closed within the cycle.
- K4=3 — as above: "Owner: Elena R." (line 4).
- K5=2 — plausibly measurable, but the KR names no pen-test report, tracker or issue project of record; search trail: no tracker, tool or dashboard for pen-test findings appears anywhere in lines 1–23.
- **Strength — no finding.** The parenthetical baseline is what keeps this KR out of AP-04, and "rated High or above" is what keeps it out of AP-13.

**KR PL2.2** — "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- K1=0 — nothing countable: a pure done/not-done milestone with no metric, baseline or scale. Per the roll-up caps, this KR's score is capped at 1.0.
- K2=1 — a delivery milestone standing in for a result; "Complete the SOC 2 Type II audit." succeeds even if no enterprise customer changes its posture.
- K3=2 — capped at the rubric's unverifiable ceiling: no baseline, prior audit, or control count anywhere in the corpus, so ambition cannot be judged.
- K4=3 — as above: "Owner: Elena R." (line 4).
- K5=2 — verifiable only at the end and only by an artefact that is never named (no auditor, evidence tracker, or report is identified in the corpus).

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Evidence (search trail for the absence claim): the only measurement system named anywhere in the corpus is "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`); lines 1–23 of the file were searched for a survey, instrument, dashboard, score definition, or prior satisfaction value and contain none.
- Also: AP-04 KR Without Baseline
- Why it's a problem: "internal developer satisfaction score" quantifies an internal state with no instrument, population, scale definition or cadence anywhere in the corpus, so the number can never be honestly produced or disputed at quarter end; and with no current value stated, the "8/10" target cannot be read as ambition or as progress.
- Scores affected: K5=0, K1=2, K3=2 (unverifiable cap), K7=2 (PL1 set)
- Suggested rewrite: "KR PL1.3: Platform developer-experience survey, run in weeks 1 and 12 of Q3 to all `<n>` engineers outside Platform via `<survey tool>`, question 'How satisfied are you with the internal platform? (1–10)': `<week-1 baseline>`/10 → 8/10, with response rate ≥ `<threshold>`%." [proposal — placeholder target] If the survey cannot be stood up inside the quarter, drop PL1.3 from the Q3 set rather than carry an unscoreable KR.

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Objective PL1: Keep the lights on, cheaper" (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Why it's a problem: "Keep the lights on" names the team's standing operational duty with no delta — it is achieved by default staffing, and its lead KR asks only to "Maintain" a level already exceeded — so the objective occupies an OKR slot that a real change should hold; only the "cheaper" clause states a change worth committing to.
- Scores affected: O1=2, O2=2, K7=2
- Suggested rewrite: "Objective PL1: Serve Q3's traffic on a materially cheaper platform without customers noticing the difference." [proposal] Keep "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." as the lead KR, and move the availability commitment out of the OKR set into a standing health-metric/guardrail section, stated as a floor: "Guardrail (not an OKR): API uptime ≥ 99.95%, monthly, Datadog SLO monitor." (the 99.95% and the monitor are reused verbatim from `input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target "at or above 99.9%" sits below the 99.95% the team's own business review reports for the trailing 90 days, so the KR is satisfied on the day it is written and can be met while reliability degrades by roughly a factor of two; it encodes no ambition and gives the quarter no reliability signal.
- Scores affected: K3=1, K1=3
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, measured monthly on the same monitor, with no month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is the activity itself — an audit completed — with no metric, baseline or target, so it measures schedule rather than any result an enterprise customer would recognise; and because it can only score 0% or 100%, weeks 1–11 of the quarter produce no evidence of whether the commitment is on track.
- Scores affected: K1=0, K2=1, K3=2 (unverifiable cap), K6=3, K7=3
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence accepted by the auditor: 0/`<total in-scope controls>` → `<total in-scope controls>`/`<total in-scope controls>`, tracked weekly in `<evidence tracker>`; Type II report received by `<date>` with 0 unresolved exceptions." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** The team's material states a capacity decision that other teams' plans may be relying on, but names no team, system, or request, and nothing here says whether any counterparty knows. Full context quoted: "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (same source ref). No severity is assigned and this is not a finding.
- Search trail: lines 3–16 (the Platform team's own material) contain no `depends on`, `blocked by`, `with <team>`, shared-system, or named-team mention other than the page's own heading "## Platform team — Q3 2026" (line 3). The appendix names Payments and Growth (lines 22–23), but only as Q2 results for those teams — not as Platform dependencies — and those teams are outside this run's scope.

## 5. Prioritized action list

1. Replace KR PL1.3 with the survey-based rewrite, or drop it from Q3 if no instrument can be stood up this cycle — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, AP-04 KR Without Baseline).
2. Reset the uptime KR against the quoted 99.95% trailing-90-day baseline, or move it out of the OKR set as a guardrail — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Rewrite Objective PL1 around the cost change and relocate the standing availability duty to a health-metric section — owner: Platform lead (Elena R.) (resolves §3 AP-10 BAU Dressed as OKR).
4. Convert KR PL2.2 into a graded evidence-completion measure with a named tracker so progress is visible before week 12 — owner: Platform lead (Elena R.), with the compliance/audit owner (resolves §3 AP-01 Task Masquerading as KR, AP-02 Binary KR with No Gradient).
5. Add one KR to Objective PL2 that measures an enterprise-customer-visible result (for example security-questionnaire turnaround or enterprise deals unblocked) — owner: Platform lead (Elena R.) (resolves the K7=3 coverage gap recorded in §2).
6. Name the system of record on each remaining KR — cloud spend and its transaction denominator, and the pen-test finding tracker — owner: Platform lead (Elena R.) (resolves the K5=2 scores recorded in §2 for PL1.2, PL2.1 and PL2.2).
7. State a measurement window on every KR (monthly, weekly, or end-of-quarter) so K1 stops losing a point across the whole set — owner: Platform lead (Elena R.) (resolves the K1=3 ceilings recorded in §2).
8. Circulate the Q3 capacity decision quoted in §4 to the teams whose plans assume Platform infra work, and record their acknowledgement — owner: Platform lead (Elena R.) (resolves the unverified dependency note in §4).
9. Attach a company-strategy reference to both objectives at the next planning checkpoint so O4 can be scored instead of excluded — owner: Platform lead (Elena R.) (resolves the O4 N/A gap note in §2).
