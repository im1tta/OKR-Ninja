# Single-team OKR review — Platform, Q3 2026

*Mode: single-team (exactly one team in confirmed scope: Platform). Period: Q3 2026, as stated by the source page. Corpus in scope (enumerated, both in one local export file): the Platform team OKR page (Confluence 88221, PLAT-OKR-Q3) and the Q2 2026 business-review appendix (Confluence 88104, Q2-REVIEW). No Atlassian connection was available; no strategy document was provided. Source refs below use the local-file form and cite `/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md`.*

## 1. Verdict summary

**Verdict: Needs rework on two of five KRs; the objectives themselves are sound.**
Roll-up grade: **C (2.15)** — Objective PL1 D (1.9, capped by a Critical finding), Objective PL2 C (2.4, capped by two Major findings on one OKR).
Findings: **1 Critical, 2 Major, 0 Minor** across 2 objectives and 5 key results.
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names no survey, instrument, or dashboard anywhere in the corpus, so the KR can never be honestly scored.
Also material: the uptime KR targets 99.9% against a quoted trailing-90-day actual of 99.95% (AP-06 Sandbagged Target), and the SOC 2 KR is a delivery milestone with no gradient (AP-01 Task Masquerading as KR · AP-02 Binary KR with No Gradient).
What holds up: both objectives are outcome-framed rather than task lists, the page states a commitment convention, the cost KR carries a real baseline→target pair, and a named page owner makes every KR attributable.
**Company-level strategy tracing was out of scope for this run** — no company or portfolio strategy source was provided, so O4 Strategic Anchoring is scored N/A and excluded from the roll-up, with the gap recorded in §2.
Recommended first action: replace KR PL1.3 with a measurable KR naming its instrument and baseline (or move developer satisfaction to an objective it actually serves) — owner: Platform lead (Elena R.).

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | N/A | 2 | 3 | 2 | 3 | 1 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.15)** — Objective PL1 **D (1.9)** (weighted 2.35, capped at 1.9 by the Critical AP-09 finding); Objective PL2 **C (2.4)** (weighted 2.64, capped at 2.4 by two Major anti-patterns on one OKR).
- Platform: K5=1 — two KRs name no system of record and one has no instrument at all (AP-09 Metric Nobody Can Measure).

**O4 = N/A — mandated gap note.** No strategy source exists in the corpus: the two sources in scope are the Platform OKR page and the Q2 2026 business-review appendix, and neither states a company priority, bet, or pillar. Neither objective claims a link of its own — "Keep the lights on, cheaper" (line 7) and "Earn enterprise trust" (line 12) both stand alone — so O4 is scored N/A for both objectives and excluded from the roll-up rather than guessed. Company-level strategy tracing should be re-run once a strategy page is supplied.

### Per-instance breakdown

**Objectives** (O1–O4; O4 N/A for both — see gap note above)

| Objective | O1 | O2 | O3 | O4 | Quoted spans driving scores ≤ 3 |
|---|---|---|---|---|---|
| PL1 | 3 | 2 | 3 | N/A | O1=3 — "Keep the lights on, cheaper" (line 7) is outcome-framed with no delivery verb, but half of it asserts the status quo rather than a changed end-state. O2=2 — "Keep the lights on" is an idiom two readers would gloss differently (API uptime only? all infra? on-call load?) and names no specific noun subject. O3=3 — no period in the objective text; inherited unambiguously from "Brightledger — Q3 2026 OKRs (portfolio export)" (line 1) and "Platform team — Q3 2026" (line 3). |
| PL2 | 4 | 4 | 3 | N/A | O3=3 — "Earn enterprise trust" (line 12) states no period; inherited unambiguously from "Platform team — Q3 2026" (line 3). O1=4 and O2=4 need no driver: the scored text is "Earn enterprise trust" — a memorable three-word end-state for customers, no delivery verb, no metric embedded. |

**Key results** (K1–K5, and the per-KR mean after caps)

| KR | Verbatim text (source ref) | K1 | K2 | K3 | K4 | K5 | Per-KR |
|---|---|---|---|---|---|---|---|
| PL1.1 | "Maintain API uptime at or above 99.9%." (line 8) | 3 | 4 | 1 | 3 | 3 | 2.8 |
| PL1.2 | "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) | 3 | 4 | 3 | 3 | 2 | 3.0 |
| PL1.3 | "Improve internal developer satisfaction score to 8/10." (line 10) | 1 | 4 | 2 | 3 | 0 | **1.0** (capped: K5=0) |
| PL2.1 | "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) | 3 | 3 | 3 | 3 | 2 | 2.8 |
| PL2.2 | "Complete the SOC 2 Type II audit." (line 14) | 0 | 1 | 2 | 3 | 2 | **1.0** (capped: K1=0) |

Quoted spans driving each score ≤ 3:
- **PL1.1** — K1=3: "Maintain API uptime at or above 99.9%." states metric, target, and unit but no baseline and no measurement window; the baseline is retrievable from the same corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21). K3=1: target sits below that quoted actual — see §3 AP-06. K4=3: no per-KR owner; the individual is derivable from the page — "Owner: Elena R." (line 4). K5=3: the KR names no source, but "(Datadog SLO monitor)" (line 21) is the single obvious system of record for this metric elsewhere in the corpus.
- **PL1.2** — K1=3: "from $4.10 to $3.20" gives baseline, target, and unit, but no measurement window is stated. K3=3: a ~22% reduction is clearly a stretch against the stated baseline, but no mechanism or justification accompanies it; the page says only "the cost work" (line 16). K4=3: derivable from "Owner: Elena R." (line 4). K5=2: "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." names no billing, finance, or transaction-count system, and candidate systems would give different numbers.
- **PL1.3** — K1=1: "Improve internal developer satisfaction score to 8/10." is a qualitative judgement dressed as a metric — no defined score. K3=2: no baseline or prior actual for this metric exists anywhere in the two sources searched, so calibration is unverifiable (rubric cap). K4=3: derivable from "Owner: Elena R." (line 4). K5=0: the "developer satisfaction score" is defined only in someone's head — see §3 AP-09.
- **PL2.1** — K1=3: "Close 100% of pen-test findings rated High or above (currently 7 open)." gives a countable denominator and a starting point, but no measurement window. K2=3: closing findings is a proxy for the security posture the objective is about, and the causal link to "Earn enterprise trust" (line 12) is not stated in the KR. K3=3: a full burn-down from "(currently 7 open)" is a stretch, but no justification or mechanism accompanies it. K4=3: derivable from "Owner: Elena R." (line 4). K5=2: no pen-test tracker, report, or ticket queue is named here or anywhere in the corpus.
- **PL2.2** — K1=0: "Complete the SOC 2 Type II audit." is a pure done/not-done milestone; nothing countable. K2=1: a delivery milestone, not a result anyone outside Platform experiences. K3=2: no baseline or trend exists for it anywhere, so calibration is unverifiable (rubric cap). K4=3: derivable from "Owner: Elena R." (line 4). K5=2: no auditor, report, or evidence system is named; the page mentions only "SOC 2 evidence collection" (line 16).

**KR sets** (K6–K7)

| Set | K6 | K7 | Quoted spans driving scores ≤ 3 |
|---|---|---|---|
| PL1 | 2 | 2 | K6=2 — all three KRs are end-state measures ("Maintain API uptime at or above 99.9%.", line 8; "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.", line 9; "Improve internal developer satisfaction score to 8/10.", line 10); none is a leading indicator that predicts another, so there is no mid-cycle steering signal. K7=2 — the objective's two facets are covered (uptime by PL1.1, cost by PL1.2), but "Improve internal developer satisfaction score to 8/10." (line 10) serves a different goal than "Keep the lights on, cheaper" (line 7) — see §3 AP-09 / AP-12. |
| PL2 | 2 | 3 | K6=2 — the only lagging member, "Complete the SOC 2 Type II audit." (line 14), is a done/not-done event rather than a lagging outcome, so the mix with "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) is nominal and no pairing logic is stated. K7=3 — one coverage gap: both KRs measure security-compliance inputs; nothing measures an enterprise-side result of "Earn enterprise trust" (line 12), such as enterprise security reviews cleared or enterprise deals unblocked. |

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10)
- Evidence (objective the KR sits under): "Keep the lights on, cheaper" (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7)
- Also: AP-12 Orphan KR · AP-04 KR Without Baseline
- Why it's a problem: the "developer satisfaction score" names no survey, instrument, cadence, or population, and both sources in scope were searched for one — the Platform OKR page (Confluence 88221, lines 3–16) and the Q2 2026 business-review appendix (Confluence 88104, lines 18–23) — where the only measurement system named anywhere is "(Datadog SLO monitor)" (line 21) for uptime, so the 8/10 can never be honestly scored or disputed. It also states no current value, leaving ambition and progress unjudgeable; and its success would move neither uptime nor cost, the two end-states its objective names, so it is an orphan under PL1.
- Scores affected: K5=0, K1=1, K3=2, K7=2 (PL1 set), per-KR score capped at 1.0, PL1 roll-up capped at 1.9
- Suggested rewrite: under PL1, replace it with a KR that moves the objective — "KR PL1.3: Sev-1 incidents affecting the public API `<baseline>` → `<target>` per quarter, measured on `<Datadog incident monitor>`." [proposal — placeholder target] — and, if developer satisfaction is still worth a goal, move it to its own internal-developer-experience objective as "KR: Internal developer satisfaction with Platform services, quarterly engineering survey (n ≥ `<40>`, instrument: `<named survey tool>`): `<baseline>`/10 → 8/10." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8)
- Evidence (baseline, second source): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21)
- Why it's a problem: the 99.9% target is below the trailing-90-day actual quoted in the same corpus, so the KR is already satisfied on day one of the quarter and can be scored 100% with no change in behaviour; "Maintain" encodes a floor the team is already above, not an improvement, and it consumes one of only three slots under the reliability half of PL1.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, per Datadog SLO monitor) → `<99.98>`%, measured monthly on the same Datadog SLO monitor, with no single calendar month below 99.95%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and carries neither a baseline→target pair nor any measure someone outside Platform moves, so it restates the deliverable instead of measuring a result; and as a single done/not-done event it can only score 0% or 100%, leaving no mid-quarter signal on the work the page says consumes the quarter — "Q3 is fully committed between SOC 2 evidence collection and the cost work." (line 16).
- Scores affected: K1=0, K2=1, K6=2 (PL2 set), per-KR score capped at 1.0, PL2 roll-up capped at 2.4 (with AP-02, two Major anti-patterns on one OKR)
- Suggested rewrite: "KR PL2.2: SOC 2 Type II controls with a complete accepted evidence set across the observation window: 0/`<34>` → `<34>`/`<34>`, tracked weekly in `<evidence tracker>`; Type II report received from `<auditor>` by `<date>`." [proposal — placeholder target]

## 4. Outbound dependency notes

- "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (/Users/difan/orca/workspaces/OKR_Reviewer/barnacle/evals/runs/2026-09-11-smoke-cbdeba3/candidate/fixture1-platform-single-team/input/sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16) — **unverified — counterparty not in scope.** Platform states it is deferring infra requests that originate outside the team, but names no requesting team and no specific request. Whether any other team's Q3 plan depends on work inside that deferral cannot be checked with one team in scope; it needs confirmation from the requesting teams (or a portfolio-mode run) before anyone treats the Q4 hold as safe. No severity is assigned: this is a note, not a finding.

## 5. Prioritized action list

1. Replace KR PL1.3 with a KR that moves uptime or cost, and re-home developer satisfaction under its own objective with a named survey instrument and a baseline — owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure, incl. AP-12 Orphan KR and AP-04 KR Without Baseline).
2. Reset the uptime KR against the quoted 99.95% trailing-90-day actual so the target requires improvement, not maintenance — owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Convert the SOC 2 KR into a weekly-trackable control/evidence burn-down with the report date as a secondary condition — owner: SOC 2 evidence lead within Platform (resolves §3 AP-01 Task Masquerading as KR and AP-02 Binary KR with No Gradient).
4. Name the system of record and measurement window for cloud spend per 1,000 transactions and for the pen-test findings count, on the OKR page itself — owner: Platform lead (Elena R.) (raises K5=1 and the K1=3 window gaps recorded in §2).
5. Add one leading indicator to each objective's KR set so mid-quarter progress is steerable, not only end-of-quarter truth — owner: Platform lead (Elena R.) (raises K6=2 on both sets recorded in §2).
6. Add one enterprise-side result measure under PL2 so the objective is evidenced by customer outcomes, not only compliance artifacts — owner: Platform lead (Elena R.) with the enterprise account owner (closes the K7=3 coverage gap recorded in §2).
7. Confirm with the teams whose infra requests are being held to Q4 that none of them is load-bearing for a Q3 commitment — owner: Platform lead (Elena R.) (resolves the §4 outbound dependency note).
8. Supply the company Q3 strategy page and re-run this review so O4 Strategic Anchoring can be scored instead of N/A — owner: Platform lead (Elena R.) with the OKR program owner (closes the §2 O4 gap note).
