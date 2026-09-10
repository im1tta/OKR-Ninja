# OKR review — Platform team, Q3 2026 (single-team mode)

## 1. Verdict summary

**Verdict: At risk — Objective PL1 needs rework before the quarter can be trusted.**
Scope: Platform team only (single-team mode); period Q3 2026, as stated on the source page ("Platform team — Q3 2026"). Corpus: one local export (Platform OKR page + Q2 business-review appendix).
Roll-up grade: **C (2.15)** — Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**.
Findings: **1 Critical, 2 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no instrument, no baseline, and no route back to the objective it sits under.
Two of five KRs cannot be honestly scored as written (PL1.3, PL2.2); the two strongest (PL1.2, PL2.1) already carry baseline→target pairs and need no rewrite.
Company-level strategy tracing was **out of scope**: no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored **N/A** and excluded from the roll-up (gap note in §2).
Recommended first action: Platform lead (Elena R.) re-targets PL1.1 against the quoted 99.95% trailing baseline and replaces PL1.3 with an instrumented KR that actually serves PL1 — both before the mid-quarter check-in.

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 2 | 3 | N/A | 2 | 2 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform **C (2.15)** — Objective PL1 **D (1.9)** (capped by the Critical AP-09 finding), Objective PL2 **C (2.4)** (capped by two Major anti-patterns on one OKR).
- Platform: K1=2 — one KR is a bare milestone and one is an undefined "score" (AP-09 Metric Nobody Can Measure, AP-01 Task Masquerading as KR).

**O4 gap note (rubric-mandated).** No company/portfolio strategy artifact exists anywhere in the corpus — the only two sources searched were the Platform OKR page ("Platform team — Q3 2026", `sample-portfolio.md › Platform team — Q3 2026 › line 3`) and the appendix ("Appendix — Q2 2026 business review (extracts)", `sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 18`), neither of which states a company priority or pillar. Per the rubric, O4 is therefore **N/A** for both objectives and excluded from all means; strategic anchoring is unjudged, not judged good. Neither objective states a parent link in its own text.

### Per-instance breakdown

**Objectives**

| Objective | O1 | O2 | O3 | O4 |
|---|---|---|---|---|
| PL1 "Keep the lights on, cheaper" | 3 | 2 | 3 | N/A |
| PL2 "Earn enterprise trust" | 4 | 3 | 3 | N/A |

Spans driving every score ≤ 3:
- PL1 **O1=3** — "Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`): no delivery verbs and a real named change ("cheaper"), but the first half commits to today's state rather than a changed one.
- PL1 **O2=2** — "Keep the lights on, cheaper" (same ref): "the lights" is a metaphor, not a specific noun subject; two readers would gloss its scope differently (uptime only? all infra? incident load?).
- PL1 **O3=3** / PL2 **O3=3** — period is inherited unambiguously from the page, "Platform team — Q3 2026" (`sample-portfolio.md › Platform team — Q3 2026 › line 3`), and is restated in neither objective.
- PL2 **O2=3** — "Earn enterprise trust" (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`): short, memorable and plain, but "trust" is an abstraction the KR set narrows only to compliance.
- PL1 **O4=N/A**, PL2 **O4=N/A** — see the O4 gap note above.

**Key results**

| KR | K1 | K2 | K3 | K4 | K5 | Per-KR score |
|---|---|---|---|---|---|---|
| PL1.1 "Maintain API uptime at or above 99.9%." | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 "Improve internal developer satisfaction score to 8/10." | 1 | 2 | 2 | 3 | 1 | 1.8 |
| PL2.1 "Close 100% of pen-test findings rated High or above (currently 7 open)." | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 "Complete the SOC 2 Type II audit." | 0 | 1 | 2 | 3 | 2 | 1.6 → **1.0** (cap: K1=0) |

Spans driving every score ≤ 3:
- **PL1.1 K1=3** — "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`): metric, target and unit are present; the baseline is absent from the KR but retrievable from the cited appendix, and no measurement window is stated. **K3=1** — sandbag against the quoted baseline (see §3 AP-06). **K4=3** — no per-KR owner; the individual is derivable from the page ("Owner: Elena R.", `sample-portfolio.md › Platform team — Q3 2026 › line 4`). **K5=3** — the KR names no source, but the corpus names exactly one system of record for this metric ("API uptime, trailing 90 days: 99.95% (Datadog SLO monitor).", `sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`).
- **PL1.2 K1=3** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`): baseline, target, unit and denominator are all present; only the measurement window is unstated. **K3=3** — a real ~22% unit-cost stretch against the KR's own quoted baseline, with no stated justification or mechanism. **K4=3** — as PL1.1. **K5=2** — no system of record is named for cloud spend, and a cloud bill and a finance ledger would give different numbers for the same quarter.
- **PL1.3 K1=1** — "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`): a qualitative state dressed as a metric — the "score" itself is never defined, and no baseline is stated. **K2=2** — an internal-team state with no stated causal link to the objective's uptime or cost outcome. **K3=2** — no baseline or trend for this metric exists anywhere in the corpus (both sources searched), so calibration is unverifiable; capped per the rubric. **K4=3** — as PL1.1. **K5=1** — the number would require a survey instrument that no source in the corpus mentions, and no KR or task builds one.
- **PL2.1 K1=3** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`): population, baseline ("currently 7 open") and target are all countable; measurement window unstated. **K2=3** — a security-posture proxy whose link to the objective's outcome is credible but stated only through the objective. **K3=3** — a modest, properly-labelled committed stretch (7 → 0) under the page convention "Commitment: KRs are committed unless marked (aspirational)." (`sample-portfolio.md › Platform team — Q3 2026 › line 5`). **K4=3** — as PL1.1. **K5=2** — no finding register or tracker is named anywhere in the corpus.
- **PL2.2 K1=0** — "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`): a pure done/not-done milestone with nothing countable. **K2=1** — a delivery milestone, not a result anyone outside the team experiences. **K3=2** — nothing to calibrate against; no baseline or prior actual in the corpus, so capped as unverifiable. **K4=3** — as PL1.1. **K5=2** — plausibly evidenced by an auditor's report, but no system or artifact of record is named in the corpus.

**KR sets**

| KR set | K6 | K7 |
|---|---|---|
| PL1 (PL1.1–PL1.3) | 2 | 2 |
| PL2 (PL2.1–PL2.2) | 3 | 3 |

- PL1 **K6=2** — all three KRs are end-state truths ("Maintain API uptime at or above 99.9%.", "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", `sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › lines 8–9`); nothing in the set predicts them, so the set gives no mid-quarter steering signal.
- PL1 **K7=2** — one orphan KR serving a different goal: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) moves neither uptime nor cost (see §3 AP-12 on that instance).
- PL2 **K6=3** — a mix is present but the pairing is left to the reader: "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) plausibly leads "Complete the SOC 2 Type II audit." (line 14), but no text states the link (`sample-portfolio.md › Objective PL2: Earn enterprise trust › lines 13–14`).
- PL2 **K7=3** — one coverage gap: both KRs measure compliance work, and nothing in the set measures whether "Earn enterprise trust" (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`) actually happened — no enterprise adoption, renewal, or security-review outcome.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: the "internal developer satisfaction score" is an internal state with no instrument — no survey, tool, or dashboard for it appears in either source searched (the Platform OKR page, lines 3–16, and the Q2 business-review appendix, lines 18–23), so the 8/10 can never be honestly scored; it also states no current value, leaving both ambition and progress unjudgeable, and its success would move neither half of "Keep the lights on, cheaper" — no chain in two steps connects developer sentiment to API uptime or to cloud spend per 1,000 transactions.
- Scores affected: K1=1, K2=2, K3=2, K5=1, K7=2 (PL1 set); PL1 per-OKR capped at 1.9 by this Critical finding
- Suggested rewrite: replace it under PL1 with a KR that serves the objective — "KR PL1.3: Sev-1 incidents per quarter `<baseline>` → `<target>`, and unplanned on-call pages per week `<baseline>` → `<target>` (source: `<incident tracker of record>`)." [proposal — placeholder target] If developer satisfaction is genuinely a Q3 goal, move it to its own objective with a named instrument and a starting point: "KR: Internal developer survey (n ≥ `<N>`, existing `<survey tool>` instrument, run in the last two weeks of Q3): overall satisfaction `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence (KR): "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence (baseline, other source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the committed target sits *below* the trailing-90-day actual quoted in the same corpus, so the KR is already met on the day the quarter opens and can be scored green by changing nothing. It also spends one of only three PL1 slots on a floor the team is already clearing by 0.05pt.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% trailing 90 days (Q2 review, Datadog SLO monitor) → ≥ 99.97% for Q3, measured on the same Datadog SLO monitor; error-budget burn reported weekly." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a bare completion of a delivery verb — it carries neither a baseline→target pair nor any measure someone outside the team moves, so it counts the team finishing its own work rather than a result; and because it is done-or-not-done, mid-cycle scoring can only ever read 0% or 100%, hiding whether the audit is on track until the quarter ends.
- Scores affected: K1=0, K2=1 (per-KR score capped at 1.0 by K1=0)
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence requests closed 0/`<N>` → `<N>`/`<N>`, tracked weekly in `<audit tracker>`; auditor's Type II report received with zero qualified exceptions by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Holding all non-critical infra requests until Q4." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** The sentence defers infrastructure work other teams may be relying on this quarter, but names no counterparty team and no specific request, and no other team's OKRs were in scope to check against. Its companion sentence, "Q3 is fully committed between SOC 2 evidence collection and the cost work." (same ref), states the capacity position behind the hold.
- No other cross-team dependency mention appears in the team's material: neither objective, none of the five KRs, and no line of the appendix names another team, a shared system, or a depends-on / blocked-by relationship.

## 5. Prioritized action list

1. Replace KR PL1.3 with an instrumented KR that moves PL1's uptime or cost outcome, and re-home developer satisfaction under its own objective with a named survey instrument and baseline — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, incl. AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Re-target KR PL1.1 above the quoted 99.95% trailing-90-day baseline and state the measurement window — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert KR PL2.2 into a weekly-gradable evidence-closure count with an audit-report gate — owner: SOC 2 evidence lead within Platform (resolves §3 AP-01 Task Masquerading as KR / AP-02 Binary KR with No Gradient).
4. Name the system of record for cloud spend per 1,000 transactions and for the pen-test finding register on the OKR page — owner: Platform lead (Elena R.) (lifts K5=2 on PL1.2 and PL2.1, §2).
5. Add one leading indicator to the PL1 set (e.g. weekly cost-per-1,000-transactions run rate) so the quarter is steerable before its final week — owner: Platform lead (Elena R.) (lifts K6=2 on PL1, §2).
6. Add one outcome KR to PL2 that measures enterprise trust itself rather than compliance work — owner: Platform lead (Elena R.) with the enterprise sales counterpart (lifts K7=3 on PL2, §2).
7. Request the company Q3 strategy page and re-score O4 for both objectives — owner: Platform lead (Elena R.) (closes the §2 O4 gap note).
8. Name the counterparty teams behind "Holding all non-critical infra requests until Q4." and confirm the deferral with each — owner: Platform lead (Elena R.) (resolves the §4 dependency note).
