# OKR-Ninja — Single-team review: Platform (Brightledger), Q3 2026

**Mode:** single-team (exactly one team in confirmed scope → depth, no cross-team alignment analysis).
**Team:** Platform. **Period:** Q3 2026, as stated by the source page.
**Source (canonical, and the only one):** `/Users/difan/Archive/A_02_Cursor/OKR_Reviewer/.claude/worktrees/loving-hypatia-0d8d0c/evals/runs/2026-09-09-candidate-opus-8d1cb12/candidate/fixture1-platform-single-team/input/sample-portfolio.md` — the Platform OKR page (lines 3–16, "Confluence page 88221 (PLAT-OKR-Q3)") and the Q2 2026 business-review appendix (lines 18–23, "Confluence page 88104 (Q2-REVIEW)"). No Atlassian connection was available for this run.
**Strategy doc:** none provided.
Source refs below abbreviate that file as `sample-portfolio.md`; line numbers refer to it exactly as it stands.

---

## 1. Verdict summary

**Verdict: Needs rework — Objective PL1 is not trustworthy as written; Objective PL2 is usable but under-measured.** Roll-up grade **C (2.2)** (Objective PL1 **D (1.9)**, Objective PL2 **C (2.4)**).
Findings: **1 Critical, 3 Major, 0 Minor.**
Worst finding: **AP-09 Metric Nobody Can Measure** — "Improve internal developer satisfaction score to 8/10." names a score for which no instrument, baseline, or system of record exists anywhere in the corpus, so the KR can never be honestly scored.
Most consequential correction: the availability KR is a sandbag — its committed 99.9% target sits **below** the 99.95% trailing-90-day actual quoted in the same export (AP-06 Sandbagged Target).
Two of the five KRs cannot be scored as written (K1 ≤ 1): PL1.3 and PL2.2, the latter a pure done/not-done milestone.
What is working: the page names an owner and states a commitment convention, and KR PL1.2 is a complete baseline→target metric — the set's defects are concentrated, not pervasive.
**Company-level strategy tracing was out of scope for this run:** no company or portfolio strategy document was provided, so O4 Strategic Anchoring is scored **N/A** for both objectives and excluded from the roll-up, with the mandated gap note recorded in §2.
Recommended first action: rebaseline KR PL1.1 against the quoted 99.95% actual and set a target above it — owner: Platform lead (Elena R.).

---

## 2. Score table

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 2 | N/A | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Platform C (2.2)** — mean of Objective PL1 **D (1.9)** (weighted 2.42, capped at 1.9 by the confirmed Critical anti-pattern AP-09) and Objective PL2 **C (2.4)** (weighted 2.62, capped at 2.4 by two Major anti-patterns on one OKR). No team-level cap applied: only 2 of 5 KRs carry K1 ≤ 1, and the strategy-trace cap requires a strategy corpus, which is absent.
- Platform: K1=2 — two of five KRs state no measurable baseline→target pair (AP-09, AP-01).

**O4 gap note (recorded here, per the rubric's no-strategy-source rule — not as a finding):** O4 = **N/A** for both objectives and excluded from the roll-up. Search performed: the whole of `sample-portfolio.md` — the Platform OKR page (lines 3–16) and the Q2 2026 business-review appendix (lines 18–23), which reports only "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor).", "Chargeback rate ended Q2 at 0.9% of transactions; step-up verification covered 35%." and "Qualified signups averaged 2,100/mo across Q2." — plus the run's stated constraint that no Atlassian source and no strategy document were available. No company or portfolio strategy artifact exists in the corpus, and neither objective states a parent priority, so strategic anchoring could be neither confirmed nor refuted and is not guessed. **This is a real gap:** whether "Keep the lights on, cheaper" and "Earn enterprise trust" are the right two bets for Q3 is unverifiable from this material.

### Per-instance breakdown (single-team mode scores exhaustively; every score ≤ 3 names its driving span)

**Objective PL1 — "Keep the lights on, cheaper"** (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)

- **O1 = 2** — "Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`). "Keep the lights on" is the standing operational duty, not a changed end-state; only "cheaper" carries a delta, and deleting it leaves no outcome at all.
- **O2 = 3** — "Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`). Memorable, plain, well under 15 words and metric-free, but the metaphor supplies no specific noun subject — "the lights" is not a system, service, or audience.
- **O3 = 2** — "Keep the lights on, cheaper" (line 7) read against "## Platform team — Q3 2026" (`sample-portfolio.md › Platform team — Q3 2026 › line 3`). The quarter is inherited unambiguously from the page, but the objective is an open-ended standing state crammed into a cycle: it cannot be failed at the end of Q3.
- **O4 = N/A** — see the gap note above.

**KR PL1.1 — "Maintain API uptime at or above 99.9%."** (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`) — per-KR score **2.8**

- **K1 = 3** — "Maintain API uptime at or above 99.9%." (line 8). Metric, target and unit are present and the baseline is retrievable from a cited source in the corpus — "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`) — but the KR states neither the baseline nor its measurement window.
- **K2 = 4** — "Maintain API uptime at or above 99.9%." (line 8). Availability is experienced by everyone outside the team who calls the API.
- **K3 = 1** — "Maintain API uptime at or above 99.9%." (line 8) against "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (line 21). Sandbag: the target is below the quoted actual. See §3 AP-06.
- **K4 = 3** — "Owner: Elena R." (`sample-portfolio.md › Platform team — Q3 2026 › line 4`). An individual is derivable from the same source, but no owner is attached to the KR itself.
- **K5 = 3** — "Maintain API uptime at or above 99.9%." (line 8) with "(Datadog SLO monitor)" (line 21). A standard metric with an obvious single system of record found elsewhere in the corpus; the KR itself does not name it.

**KR PL1.2 — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20."** (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`) — per-KR score **3.0**

- **K1 = 3** — "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9). Named metric, numeric baseline, numeric target and unit are all present; the measurement window is unstated (monthly? quarter-end? trailing average?).
- **K2 = 4** — "from $4.10 to $3.20" (line 9). Unit cost per transaction is a business result, not team activity.
- **K3 = 3** — "from $4.10 to $3.20" (line 9), i.e. a 22% reduction, and "Commitment: KRs are committed unless marked (aspirational)." (`sample-portfolio.md › Platform team — Q3 2026 › line 5`). Clearly a stretch and properly labelled committed, but no mechanism or justification is stated anywhere on the page; no prior-period cost trend exists in the corpus to test it against.
- **K4 = 3** — "Owner: Elena R." (line 4). As PL1.1.
- **K5 = 2** — "cloud spend per 1,000 transactions" (line 9). Plausibly measurable but no system of record is named, and both the numerator (cloud bill: which accounts, which shared services?) and the denominator (transaction count) have several plausible sources that would give different numbers.

**KR PL1.3 — "Improve internal developer satisfaction score to 8/10."** (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`) — per-KR score **2.2**

- **K1 = 1** — "Improve internal developer satisfaction score to 8/10." (line 10). A qualitative state dressed as a metric: no defined score, no baseline, and no population; see §3 AP-09.
- **K2 = 4** — "internal developer satisfaction" (line 10). Internal developers are outside the Platform team, so this measures a result someone else experiences.
- **K3 = 2** — "to 8/10." (line 10). No baseline, prior actual, or trend exists anywhere in the corpus (searched: lines 3–16 and the appendix, lines 18–23), so calibration is unverifiable — capped at 2 per the rubric.
- **K4 = 3** — "Owner: Elena R." (line 4). As PL1.1.
- **K5 = 1** — "internal developer satisfaction score" (line 10). The number requires a survey that does not exist in the corpus, and no KR or task in the set builds one.

**KR set PL1** — K6 and K7 scored once for the set

- **K6 = 2** — "Maintain API uptime at or above 99.9%." (line 8) · "Reduce cloud spend per 1,000 transactions from $4.10 to $3.20." (line 9) · "Improve internal developer satisfaction score to 8/10." (line 10). Three independent end-state truths; none is a leading indicator that predicts another, so the set gives no steering signal about which lever to pull mid-quarter.
- **K7 = 2** — "Keep the lights on, cheaper" (line 7) against "Improve internal developer satisfaction score to 8/10." (line 10). One orphan KR serving a different goal: hitting the satisfaction target would move neither availability nor cost. Toil/incident load — the other half of "Keep the lights on" — is also untouched.

**Objective PL2 — "Earn enterprise trust"** (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`)

- **O1 = 4** — "Earn enterprise trust" (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 12`). A changed end-state for a named audience, no delivery verbs, and achievable by routes other than the two the team has picked.
- **O2 = 3** — "Earn enterprise trust" (line 12). Short, memorable and metric-free, but "trust" is left to the reader: security trust, reliability trust and commercial trust would each imply different KRs.
- **O3 = 3** — "Earn enterprise trust" (line 12) read against "## Platform team — Q3 2026" (line 3). The period is inherited unambiguously from the page though not restated in the objective, and the objective is plausibly failable within it.
- **O4 = N/A** — see the gap note above.

**KR PL2.1 — "Close 100% of pen-test findings rated High or above (currently 7 open)."** (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 13`) — per-KR score **2.8**

- **K1 = 3** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13). Metric, baseline ("currently 7 open") and target (100%) are all present with a defined severity population; the measurement window is unstated, and the KR does not say whether findings raised later in the quarter join the denominator.
- **K2 = 3** — "Close 100% of pen-test findings rated High or above" (line 13) under "Earn enterprise trust" (line 12). Remediation of a known risk set is a credible proxy for the trust outcome, but the causal link is left implicit by the KR itself.
- **K3 = 3** — "(currently 7 open)" → "100%" (line 13). A genuine, bounded commitment; no mechanism, sequencing or prior closure-rate is stated to justify it, and no prior-period actual exists in the corpus to calibrate against.
- **K4 = 3** — "Owner: Elena R." (line 4). As PL1.1.
- **K5 = 2** — "pen-test findings rated High or above" (line 13). No tracker, report, or dashboard of record is named; the pen-test vendor's report and an internal issue tracker would plausibly disagree on the count.

**KR PL2.2 — "Complete the SOC 2 Type II audit."** (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`) — per-KR score **1.6 → capped at 1.0** (K1 = 0 cap)

- **K1 = 0** — "Complete the SOC 2 Type II audit." (line 14). Nothing countable: a pure done/not-done milestone with no metric, baseline, target or unit. See §3 AP-01.
- **K2 = 1** — "Complete the SOC 2 Type II audit." (line 14). A delivery milestone; its only failure mode is lateness.
- **K3 = 2** — "Complete the SOC 2 Type II audit." (line 14). No baseline, target magnitude or trend exists, so calibration is unverifiable — capped at 2 per the rubric.
- **K4 = 3** — "Owner: Elena R." (line 4). As PL1.1.
- **K5 = 2** — "Complete the SOC 2 Type II audit." (line 14). Completion is plausibly evidenced by the auditor's report, but no GRC tool, evidence tracker or report is named, and "Complete" is not defined (report received? observation window closed? findings remediated?).

**KR set PL2** — K6 and K7 scored once for the set

- **K6 = 3** — "Close 100% of pen-test findings rated High or above (currently 7 open)." (line 13) · "Complete the SOC 2 Type II audit." (line 14). A mix exists — the 7→0 remediation count moves mid-quarter and plausibly predicts the audit outcome — but the pairing is loose and nowhere stated.
- **K7 = 3** — "Earn enterprise trust" (line 12) against both KRs (lines 13–14). Two related, non-orphan KRs, but one coverage gap: nothing measures the trust outcome itself (enterprise deals unblocked, security-review turnaround, renewals), so a skeptic could see both KRs hit and still ask whether enterprises trust Brightledger.

---

## 3. Findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 10`)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: the "internal developer satisfaction score" quantifies an internal state with no instrument — no survey, tool, or dashboard for it appears anywhere in the corpus (searched: the Platform OKR page, lines 3–16, and the Q2 2026 business-review appendix, lines 18–23, which reports only uptime, chargeback rate and qualified signups), so 8/10 can never be honestly scored and no one can dispute a claimed number; the KR also states no current value, leaving both ambition and progress unjudgeable, and its success would move neither half of "Keep the lights on, cheaper".
- Scores affected: K1=1, K5=1, K3=2, K7=2
- Suggested rewrite: "KR PL1.3 (committed): Internal developer satisfaction among the `<n>` product engineers who consume platform services, quarterly survey run in `<named survey tool>`, n ≥ `<minimum responses>`: `<baseline>`/10 → 8/10." [proposal — placeholder target] — and, because satisfaction serves neither availability nor cost, move that KR under an objective it actually measures and replace it under PL1 with a KR on the objective's own terms: "KR PL1.3 (committed): Pages per on-call week `<baseline>` → `<target>`, source `<named paging system>`." [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 8`)
- Evidence: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md › Appendix — Q2 2026 business review (extracts) › line 21`)
- Why it's a problem: the target sits below the trailing-90-day actual quoted in the same export, so the KR was already achieved the day it was written and encodes no delta — and under the page's own convention, "Commitment: KRs are committed unless marked (aspirational)." (`sample-portfolio.md › Platform team — Q3 2026 › line 5`), it consumes a committed slot that could hold a real goal.
- Scores affected: K3=1
- Suggested rewrite: "KR PL1.1 (committed): API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.97%, measured monthly on the same Datadog SLO monitor, with monthly error budget consumed ≤ `<threshold>`%." [proposal — placeholder target; the 99.95% baseline is quoted from line 21]

### [Major] AP-10 BAU Dressed as OKR — Platform
- Evidence: "Keep the lights on, cheaper" (`sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 7`)
- Why it's a problem: "Keep the lights on" is the standing operational duty of a platform team — it is achieved by default staffing and describes no change, so as written the objective can be met by doing exactly what the team already does; that vacuum is why the KR set reads as a maintenance target, an unrelated cost target and an uninstrumented satisfaction score rather than one coherent bet.
- Scores affected: O1=2, O3=2, K7=2
- Suggested rewrite: "Objective PL1: Platform costs less per transaction and wakes fewer people up." — with the standing availability commitment moved out of the OKR set into an SLO/health-metric section that the team reports but does not score as a goal, and the KR set becoming: "KR PL1.1 (committed): Cloud spend per 1,000 transactions $4.10 → $3.20." (figures quoted from `sample-portfolio.md › Objective PL1: Keep the lights on, cheaper › line 9`) and "KR PL1.2 (committed): Pages per on-call week `<baseline>` → `<target>`, source `<named paging system>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 14`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a deliverable, not a result — it opens with "Complete" and carries no metric, no baseline and no target, so it tracks the team's activity rather than anything an enterprise customer experiences; and because it is done/not-done, it can only ever score 0% or 100%, giving the team no mid-quarter signal that the audit is slipping until it has already slipped.
- Scores affected: K1=0, K2=1, K5=2 (per-KR score capped at 1.0 by the K1=0 rule)
- Suggested rewrite: "KR PL2.2 (committed): SOC 2 Type II evidence requests closed `<0>`/`<N>` → `<N>`/`<N>`, tracked weekly in `<named GRC tool>`; observation window opened by `<date>` and the auditor's Type II report received before quarter end with zero qualified exceptions." [proposal — placeholder target]

---

## 4. Outbound dependency notes

Notes carry no severity and are not findings. Single-team mode produces no AL-XX alignment findings: with one team in scope, the taxonomy's both-sides quote rule cannot be met.

- "Holding all non-critical infra requests until Q4." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** Platform declares it is deferring other teams' non-critical infrastructure requests for the quarter, but no requesting team is named here and no other team's OKRs are in scope, so which Q3 plans this defers, and whether any of them depend on that work, cannot be checked from this material.
- "Q3 is fully committed between SOC 2 evidence collection and the cost work." (`sample-portfolio.md › Objective PL2: Earn enterprise trust › line 16`) — **unverified — counterparty not in scope.** A full-capacity declaration that other teams may be planning against; no counterparty commitment is quotable with one team in scope.

No Platform objective or key result states a dependency on another team's delivery: the only cross-team-relevant text in the team's material is the note quoted above.

---

## 5. Prioritized action list

1. Replace the developer-satisfaction KR with a named, instrumented survey metric — or move it off Objective PL1 entirely — before the quarter is scored, owner: Platform lead (Elena R.) (resolves §3 AP-09 Metric Nobody Can Measure).
2. Rebaseline KR PL1.1 on the quoted 99.95% trailing-90-day actual and commit to a target above it, owner: Platform lead (Elena R.) (resolves §3 AP-06 Sandbagged Target).
3. Recast Objective PL1 as a cost-and-toil change and move the standing availability commitment into an SLO/health-metric section outside the OKRs, owner: Platform lead (Elena R.) (resolves §3 AP-10 BAU Dressed as OKR).
4. Convert the SOC 2 KR into a graded evidence-closure count with a dated observation-window milestone, owner: Platform SOC 2 / compliance workstream lead (resolves §3 AP-01 Task Masquerading as KR).
5. Name the system of record for cloud spend per 1,000 transactions and for pen-test finding closure, and state each KR's measurement window, owner: Platform lead (Elena R.) (resolves the K5=2 and K1=3 score notes on PL1.2 and PL2.1 in §2).
6. Obtain the Q3 company-priorities document and re-score O4 for both objectives, owner: Platform lead (Elena R.) (resolves the §2 O4 gap note — strategy tracing was out of scope this run).
7. Add one leading indicator to Objective PL1 that predicts the cost outcome mid-quarter, owner: Platform lead (Elena R.) (resolves the §2 K6=2 score note on the PL1 KR set).
