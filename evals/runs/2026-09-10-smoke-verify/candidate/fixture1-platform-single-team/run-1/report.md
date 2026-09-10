# OKR-Ninja — Single-team review: Platform, Q3 2026

Mode: single-team (exactly one team in confirmed scope: Platform). Period: Q3 2026, as stated by the source page heading "Platform team — Q3 2026" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ## Platform team — Q3 2026 › line 3). Sources reviewed: that file only — the Platform OKR page section (lines 3–16, Confluence page 88221 (PLAT-OKR-Q3)) and the Q2 2026 business review appendix (lines 18–23, Confluence page 88104 (Q2-REVIEW)). No Atlassian connection was available and no company strategy document was provided.

## 1. Verdict summary

**Verdict: At risk — the set is usable, but one key result cannot be honestly scored and one target is already met.**

- Roll-up grade: **C (2.15)** — Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**.
- Findings: **3** — 1 Critical, 2 Major, 0 Minor. Three further anti-patterns apply to those same instances and are recorded on the blocks' `Also:` lines (AP-12 Orphan KR, AP-04 KR Without Baseline, AP-02 Binary KR with No Gradient); per the one-finding-per-instance rule they are not separate blocks.
- Worst finding: **AP-09 Metric Nobody Can Measure** on KR PL1.3 — "Improve internal developer satisfaction score to 8/10." names a score that no instrument in the corpus can produce, so the KR can never be honestly scored.
- Company-level strategy tracing was **out of scope** for this run: no strategy document was provided and no strategy source exists in the corpus, so O4 Strategic Anchoring is scored N/A and excluded from the roll-up (gap note in §2).
- Recommended first action: give KR PL1.3 a named instrument and a baseline — or move it out of the OKR set this quarter (§3, AP-09).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): Platform **C (2.15)** — PL1 D (1.9, capped by a Critical anti-pattern), PL2 C (2.4, capped by two Major anti-patterns on one OKR).
- Platform: K1=2 — one KR states no countable target and one states no defined score (AP-01 Task Masquerading as KR, AP-09 Metric Nobody Can Measure).

**O4 = N/A — mandated gap note.** No strategy source exists in the corpus. The search covered both sections of the only file in scope: the Platform OKR page (lines 3–16) and the Q2 2026 business review appendix (lines 18–23); neither objective states a parent — "Keep the lights on, cheaper" (…/input/sample-portfolio.md › ### Objective PL1: Keep the lights on, cheaper › line 7) and "Earn enterprise trust" (…/input/sample-portfolio.md › ### Objective PL2: Earn enterprise trust › line 12) carry no link to a company or portfolio priority, and no strategy page was provided. Per the rubric, O4 is scored N/A, excluded from every mean, and recorded here as a gap rather than as a finding: strategic anchoring for both objectives is unjudged, not judged good.

### Per-instance breakdown

Source refs below are shortened to `line N`; all refer to `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md`, whose nearest headings are "## Platform team — Q3 2026" (lines 4–5), "### Objective PL1: Keep the lights on, cheaper" (lines 7–10), "### Objective PL2: Earn enterprise trust" (lines 12–16) and "## Appendix — Q2 2026 business review (extracts)" (lines 19–23).

**Objective PL1 — "Keep the lights on, cheaper" (line 7): O1=3, O2=3, O3=3, O4=N/A**
- O1=3 — "Keep the lights on, cheaper" (line 7): outcome-framed with no delivery verb, but half of it states continuation of the standing job rather than a changed end-state; the only change named is "cheaper", which KR PL1.2 pays for with a stated baseline→target pair, "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9).
- O2=3 — "Keep the lights on, cheaper" (line 7): memorable, plain, under 15 words and metric-free, but "the lights" is an idiom rather than a specific noun subject, so two readers could scope it to the API alone or to all infrastructure.
- O3=3 — period is not restated in the objective; it is inherited unambiguously from "Platform team — Q3 2026" (line 3), and both KR sets are failable within it.
- O4=N/A — see the gap note above.

**Objective PL2 — "Earn enterprise trust" (line 12): O1=4, O2=3, O3=3, O4=N/A**
- O1=4 — "Earn enterprise trust" (line 12): a changed end-state for customers, no delivery verb, reachable by more than one route.
- O2=3 — "Earn enterprise trust" (line 12): short, memorable and specific in its audience, but "trust" is one abstraction two readers would evidence differently (compliance artifacts vs. renewal behaviour).
- O3=3 — inherited from "Platform team — Q3 2026" (line 3), not restated.
- O4=N/A — see the gap note above.

**KR PL1.1 — "Maintain API uptime at or above 99.9%." (line 8): K1=3, K2=4, K3=1, K4=3, K5=3 → 2.8**
- K1=3 — metric, target and unit are present in "Maintain API uptime at or above 99.9%." (line 8); the baseline is absent from the KR but retrievable from the corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21) — and no measurement window is stated.
- K2=4 — "Maintain API uptime at or above 99.9%." (line 8) measures availability as API consumers experience it.
- K3=1 — sandbag: the target in "Maintain API uptime at or above 99.9%." (line 8) sits below the most recent quoted actual, "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21). See §3, AP-06.
- K4=3 — no per-KR owner; the owning team is named in "Platform team — Q3 2026" (line 3) and an individual is derivable from the same page, "Owner: Elena R." (line 4).
- K5=3 — the KR names no source, but the corpus names the single system of record for this exact metric: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21).

**KR PL1.2 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9): K1=3, K2=4, K3=3, K4=3, K5=2 → 3.0**
- K1=3 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) states metric, baseline, target, unit and an explicit denominator; only the measurement window is unstated.
- K2=4 — unit cost per 1,000 transactions is a business result, not an activity count.
- K3=3 — clearly a stretch against the stated baseline in "from $4.10 to $3.20." (line 9), but no mechanism or justification for the reduction appears on the page; the KR is committed by default under "Commitment: KRs are committed unless marked (aspirational)." (line 5).
- K4=3 — as PL1.1: team named (line 3), individual derivable from "Owner: Elena R." (line 4).
- K5=2 — plausibly measurable, but "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) names no system of record, and none appears anywhere in the corpus; a cloud bill and a finance view would give different numbers.

**KR PL1.3 — "Improve internal developer satisfaction score to 8/10." (line 10): K1=1, K2=3, K3=2, K4=3, K5=1 → 2.0**
- K1=1 — "Improve internal developer satisfaction score to 8/10." (line 10) is qualitative dressed as a metric: the "score" is never defined and no starting value is stated.
- K2=3 — the KR states a satisfaction result rather than an activity count, but "internal developer satisfaction score" (line 10) names no population and no link to an outcome outside the team.
- K3=2 — capped: no baseline or trend for this score exists anywhere in the corpus (searched: Platform OKR page lines 3–16; Q2 business review appendix lines 18–23), so calibration is unverifiable.
- K4=3 — as PL1.1: team named (line 3), individual derivable from "Owner: Elena R." (line 4).
- K5=1 — "Improve internal developer satisfaction score to 8/10." (line 10) requires data collection that does not exist yet, and no KR or task in the set builds it. See §3, AP-09.

**KR PL2.1 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13): K1=3, K2=3, K3=3, K4=3, K5=2 → 2.8**
- K1=3 — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) states the metric, a starting point and a countable denominator; the measurement window is unstated.
- K2=3 — remediation coverage is a proxy output whose link to the objective "Earn enterprise trust" (line 12) is credible but stated only by placement; nothing measures the trust itself.
- K3=3 — clearing all of "(currently 7 open)" (line 13) is a real stretch beyond the stated baseline, but no justification or mechanism is stated; committed by default under "Commitment: KRs are committed unless marked (aspirational)." (line 5).
- K4=3 — as PL1.1: team named (line 3), individual derivable from "Owner: Elena R." (line 4).
- K5=2 — no tracker or system of record for pen-test findings is named in "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) or anywhere else in the corpus.

**KR PL2.2 — "Complete the SOC 2 Type II audit." (line 14): K1=0, K2=1, K3=2, K4=3, K5=2 → 1.6, capped at 1.0 (K1=0)**
- K1=0 — "Complete the SOC 2 Type II audit." (line 14) is a pure done/not-done milestone: nothing countable.
- K2=1 — the same span is a delivery milestone standing in for a measure.
- K3=2 — capped: no baseline or trend exists for it anywhere in the corpus (searched: lines 3–16 and lines 18–23), so calibration is unverifiable.
- K4=3 — as PL1.1: team named (line 3), individual derivable from "Owner: Elena R." (line 4).
- K5=2 — "Complete the SOC 2 Type II audit." (line 14) names no system of record for the completion evidence.

**KR-set dimensions**
- PL1 K6=2 — all three KRs are period-end truths with no leading indicator that predicts any of them: "Maintain API uptime at or above 99.9%." (line 8), "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9), "Improve internal developer satisfaction score to 8/10." (line 10).
- PL1 K7=2 — one orphan KR serving a different goal: "Improve internal developer satisfaction score to 8/10." (line 10) sits under "Keep the lights on, cheaper" (line 7) and shares no metric domain with its siblings (line 8, line 9). See §3, AP-09/AP-12.
- PL2 K6=3 — a mix is present but the pairing is loose and never stated: "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) gives a mid-cycle signal, "Complete the SOC 2 Type II audit." (line 14) is the period-end truth.
- PL2 K7=2 — two coverage gaps against "Earn enterprise trust" (line 12): both KRs measure compliance artifacts ("Close 100% of pen-test findings rated High or above (currently 7 open)." line 13; "Complete the SOC 2 Type II audit." line 14) and nothing measures trust as enterprise customers would show it, nor the reliability commitments enterprises buy on.

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 10)
- Evidence (objective this KR sits under): "Keep the lights on, cheaper" (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 7)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: the "developer satisfaction score" is never defined and no instrument that could report it exists in the corpus — the search covered both sources in scope, the Platform OKR page (lines 3–16) and the Q2 2026 business review appendix (lines 18–23), and the only named measurement instrument anywhere is "(Datadog SLO monitor)" (line 21) — so the KR can never be honestly scored, and no starting value is stated or retrievable, leaving the "8/10" unjudgeable as either ambition or progress. It also shares no metric domain with its sibling KRs, "Maintain API uptime at or above 99.9%." (line 8) and "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9), so hitting it would not move the objective those siblings define.
- Scores affected: K5=1, K1=1, K3=2, K7=2
- Suggested rewrite: "KR (new objective — Platform's internal customers can build without waiting): Internal developer satisfaction with the platform, quarterly survey of engineers outside the Platform team (n ≥ `<respondents>`, run on `<named survey tool>`, instrument live by `<date>`): `<baseline>`/10 → 8/10." [proposal — placeholder target] — moving it out of "Keep the lights on, cheaper", whose remaining two KRs measure uptime and unit cost.

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ## Appendix — Q2 2026 business review (extracts) › line 21)
- Evidence (commitment convention): "Commitment: KRs are committed unless marked (aspirational)." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ## Platform team — Q3 2026 › line 5)
- Why it's a problem: the target sits below the most recent measured actual quoted in the same corpus, so this committed KR requires no improvement on the last number the team reported — "maintain … at or above" is exactly the phrasing that hides a target already cleared. A quarter of real reliability work would score identically to a quarter of none.
- Scores affected: K3=1, K1=3
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, per Datadog SLO monitor) → 99.98%, measured monthly on that same Datadog SLO monitor." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb carrying neither a result measure nor a baseline→target pair — the two things that would keep a "complete…" KR out of this anti-pattern — so it restates the work instead of measuring a result. It also scores 0% until the audit lands and 100% after, giving no mid-cycle signal; its sibling shows the contrast by stating a starting point, "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13).
- Scores affected: K1=0, K2=1
- Suggested rewrite: "KR PL2.2: SOC 2 Type II evidence tasks closed 0/`<N>` → `<N>`/`<N>` by `<date>`, tracked in `<compliance tracker>`, with the Type II report received before quarter end." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/evals/runs/2026-09-10-smoke-verify/candidate/fixture1-platform-single-team/input/sample-portfolio.md` › ### Objective PL2: Earn enterprise trust › line 16) — **unverified — counterparty not in scope.** The note withdraws infra capacity that other teams may be planning against this quarter, but no counterparty team is named anywhere in the Platform section (lines 3–16), and with one team in scope the other side's OKRs cannot be quoted. No severity is assigned and this is not a finding.

No other cross-team dependency mention appears in Platform's material; the team names in the appendix (lines 22–23) belong to other teams' Q2 results, not to Platform's OKRs.

## 5. Prioritized action list

1. Define an instrument and a baseline for the developer-satisfaction score, or drop it from this quarter's set — owner: Platform lead (Elena R., line 4) (resolves §3 AP-09 Metric Nobody Can Measure, with AP-04 KR Without Baseline).
2. Move the developer-satisfaction KR out of Objective PL1 and under an objective its metric actually serves — owner: Platform lead (resolves §3 AP-09's `Also:` AP-12 Orphan KR; lifts §2 PL1 K7=2).
3. Rebaseline the uptime KR on the quoted 99.95% trailing actual and set a target above it — owner: Platform reliability/on-call lead (resolves §3 AP-06 Sandbagged Target).
4. Convert the SOC 2 KR into a graded evidence-closure count with a dated report milestone — owner: Platform compliance owner (resolves §3 AP-01 Task Masquerading as KR, with AP-02 Binary KR with No Gradient).
5. Name the system of record on the OKR page for cloud spend and for pen-test findings — owner: Platform lead (resolves §2 K5=2 on KR PL1.2 and KR PL2.1).
6. Add one leading indicator to Objective PL1 that predicts the cost and uptime outcomes mid-quarter — owner: Platform lead (resolves §2 PL1 K6=2).
7. Add a customer-side trust measure to Objective PL2 so the objective is not evidenced by compliance artifacts alone — owner: Platform lead with the enterprise account owner (resolves §2 PL2 K7=2).
8. Record each objective's parent company priority on the OKR page, and supply the strategy document at the next review so O4 can be scored — owner: Platform lead (resolves §2's O4 = N/A gap note).
9. Circulate the "Holding all non-critical infra requests until Q4." note to the teams planning against Platform this quarter and confirm what it blocks — owner: Platform lead (resolves §4 outbound dependency note).
