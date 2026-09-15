# Tidewell — Q3 2026 OKR portfolio review

*Cycle date: 2026-09-14 · Mode: **portfolio** (2 teams in scope) · Period: Q3 2026*

**Scope confirmed at intake.** Teams: **Ledger**, **Onboarding** — every team enumerated in the export. Two teams in confirmed scope select portfolio mode (breadth: every team screened, alignment checked across the portfolio).
**Source (canonical, single):** `evals/corpora/tidewell-q3.md` — full path `/Users/difan/orca/workspaces/OKR_Reviewer/The-artifact-lifecycle-behavioural-eval/evals/corpora/tidewell-q3.md`. No Atlassian connection was available; the export's own page references ("Confluence page 41108 (LEDG-OKR-Q3)", "Confluence page 41117 (ONBD-OKR-Q3)") were not opened and are not cited as sources.
**Strategy source in scope:** the export's "Company Q3 2026 priorities" section ("Confluence page 41002 (TW-PRIO-Q3)", "Last updated 2026-06-22"), enabling the strategy trace in §4 and O4 scoring in §2.
**Source-ref form used throughout:** `<file path> › <nearest heading> › line N`, line numbers as they stand in the export above.

---

## 1. Executive summary

**Verdict: Sound, with one sequencing risk.** 2 teams reviewed; 0 Critical, 5 Major, 1 Minor findings.
The portfolio's single worst alignment risk is **AL-06 Timeline mismatch**: Ledger's committed reconciliation KR assumes the bank-link connector "lands from Onboarding in July", while Onboarding's only stated date for that connector is "by Aug 29" — an inversion on two committed KRs, softened (not removed) by Onboarding's quoted acknowledgment of the dependency.
The most common goodness anti-pattern is **AP-01 Task Masquerading as KR** — both teams (2 of 2) carry one delivery KR that is finished by shipping rather than by moving a measure.
Every other defect sits in one place: Ledger's Objective L2, whose two KRs between them state no baseline, no measurement source, and no countable result.
Both teams trace cleanly to company priorities T1/T2/T3, and all three priorities are covered — no orphan objectives, no coverage gaps, no baseline disagreements, no duplicated objectives.
Recommended first action: Amara O. and Nadia F. confirm the connector's actual landing date and re-baseline L1.2's 85% target against the weeks left in Q3.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ledger | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |
| Onboarding | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Ledger B (2.86) · Onboarding B (3.09).
- Ledger: K1=2: "Ship the new payout ledger service to production by Sep 18." — nothing countable (AP-01).
- Onboarding: K1=2: "move 100% of new clinics onto it by Aug 29." states no starting point.

## 3. Per-team goodness findings

### [Major] AP-10 BAU Dressed as OKR — Ledger
- Evidence: "Objective L2: Billing stays boring as we scale" (`evals/corpora/tidewell-q3.md` › Ledger team — Q3 2026 › line 25)
- Evidence (the objective's KRs, enumerated in full): "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26); "Ship the new payout ledger service to production by Sep 18." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Why it's a problem: the objective asserts continuation of the team's standing job — billing "stays" as it is — and names no direction, reduction or improvement, so it fires on path (a), where deltas beneath it could not rescue it in any case. Read instead as naming a change ("as we scale"), it fires on path (b): neither KR realizes that change with a baseline→target pair — L2.1 is a hold with no starting point and L2.2 is a delivery date — so the adjective is never paid for.
- Scores affected: O1=3, K7=3
- Suggested rewrite: "Objective L2: Billing survives the growth curve — clinics never notice we got bigger. KR L2.1: Failed billing runs per 1,000 runs `<Q2 actual>` → `<target>`, weekly through Q3, while monthly billing-run volume rises `<current>` → `<projected>` (source: `<billing reliability dashboard>`)." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Ledger
- Evidence: "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26)
- Why it's a problem: the KR states a floor with no "from" value, so neither its ambition nor mid-quarter progress can be judged — and the absence cuts both ways: without a current value the "at or above" phrasing cannot be tested for sandbagging either, so calibration is simply unverifiable. Search performed for a starting point: the whole export (the "Company Q3 2026 priorities" section, both team pages, both Notes lines), terms "success rate", "billing run", "baseline", "currently", "prior", "Q2", "actual" — the only occurrence anywhere is the KR itself at line 26; no dashboard or prior-period figure is cited for it.
- Scores affected: K1=2, K3=2 (capped: calibration unverifiable with no baseline in the corpus)
- Suggested rewrite: "KR L2.1: Billing run success rate `<Q2 actual>`% → 99.9%, measured weekly through Q3 with no single week below 99.7% (source: `<billing reliability dashboard>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Ledger
- Evidence: "Ship the new payout ledger service to production by Sep 18." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Evidence (commitment label on the same KR): "(aspirational)" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with "Ship", carries no result measure that anyone outside the delivering team moves and no baseline→target pair, so it is scored by the delivery date alone — the service can reach production on Sep 18 with no payout running through it. Mid-cycle it can only read 0% or 100% (AP-02); the honest aspirational label sets expectations but does not make the KR measurable.
- Scores affected: K1=0, K2=1, K6=2
- Suggested rewrite: "KR L2.2 (aspirational): Monthly payout volume served by the new payout ledger service 0% → `<target>`% by Sep 30, with billing run success rate on that path no lower than on the legacy path (source: `<billing reliability dashboard>`)." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Onboarding
- Evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Why it's a problem: the KR opens with a build verb and its only figure is a bare completion target — "100% of new clinics" has no stated starting point, so it counts a rollout the team finishes by shipping rather than a result a clinic produces. The rubric's exclusion does not rescue it: a coverage figure lifts a delivery-verb KR out of AP-01 only when it moves from a stated starting point over a countable denominator, and neither the starting point nor the size of the "new clinics" population appears anywhere in the export.
- Scores affected: K1=2, K2=1, K3=2
- Suggested rewrite: "KR O1.3: New clinics completing bank-link setup on the rebuilt connector 0 → `<target>` of the `<new clinics onboarded in Q3>` onboarded this quarter, with bank-link setup contacts per new clinic `<baseline>` → `<target>` (source: `<onboarding funnel dashboard>`; contact counts from the Zendesk weekly export)." [proposal — placeholder target]

## 4. Alignment findings

*Blocking keys run before any pairwise check, so a reviewer knows what could have been missed: (1) metric-identity on the metric catalog — no canonical metric appears in both teams' KRs, so this key generated no AL-02/AL-03/AL-08/AL-09 candidate; (2) surface-lever — no KR states a friction, quality, risk or cost control on a surface whose throughput, conversion, volume or latency the other team targets, so this key generated nothing either; (3) metric + population cluster (AL-03) — Ledger's "Cut billing support tickets per 100 clinics from 14 to 8 per month." and Onboarding's "Reduce onboarding support contacts per new clinic from 3.1 to 1.5." cluster on support-contact volume but were killed by the "similar objectives ≠ duplication" control: different populations (active clinics vs new clinics), different surfaces (billing vs onboarding), same direction, compatible targets — division of labor, not duplication. Graph checks: one dependency edge (Ledger → Onboarding, the bank-link connector), so AL-11 cycle detection found no cycle and AL-07 found no resource node with two or more claimants. Strategy trace: all three company priorities have a contributing child and every objective has a parent — no AL-04 and no AL-10 (T1 ← Objective L1, T2 ← Objective O1, T3 ← Objective L2). AL-09 baseline check: the only metric stated on two pages is days-to-collect, and both pages give the same starting value ("from 31 to under 20." / "from 31 to 19 across active clinics.") — no disagreement.*

### [Major] AL-06 Timeline mismatch: Ledger ↔ Onboarding
- Ledger evidence: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29), against the KR it gates: "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22)
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: the consumer's need-by date precedes the producer's only stated date by about a month — Ledger plans on the rework landing "in July", Onboarding commits to "by Aug 29" — leaving Ledger's 23-point reconciliation climb roughly the final four weeks of the quarter and no integration margin.
- Detection check that fired: AL-06 edge-date comparison on the dependency map — producer delivery date vs consumer need-by date on the single Ledger → Onboarding connector edge.
- Disconfirming checks run: (1) "Late date ≠ inversion — confirm which milestone the consumer actually needs": Ledger needs the "rework" to land, while Aug 29 attaches to Onboarding's combined "Rebuild … and move 100% of new clinics onto it" KR; no separate, earlier date for the rebuild alone exists anywhere in the export, so the tightest quotable reading is still an inversion — but the rebuild may in fact land sooner, which weakens the finding. (2) AL-01 acknowledgment check on the same edge: not an unacknowledged dependency — Onboarding's page names it, "O1.3 is the connector Ledger's reconciliation work depends on; sequencing agreed with Amara in the June planning review." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 42) — quoted awareness plus an agreed sequence weakens it further, though the agreed sequence itself is stated nowhere and the two dates as written still invert. Result: the default rating for a hard inversion on committed KRs (Critical) is reduced one level by these two checks.
- Inference labels: none — all load-bearing text quoted. Both KRs' committed status is read from each page's own stated convention, "Commitment: KRs are committed unless marked (aspirational)." (`evals/corpora/tidewell-q3.md` › Ledger team — Q3 2026 › line 18; `evals/corpora/tidewell-q3.md` › Onboarding team — Q3 2026 › line 35), and neither KR carries the marker.
- Verdict: CONFIRMED (every load-bearing quote re-verified character-for-character against lines 18, 22, 29, 35, 40 and 42 of the export; page versions recorded — Ledger "Last updated 2026-07-01", Onboarding "Last updated 2026-06-30", neither superseded within the file)
- Recommended resolution owner: Amara O. (Ledger) to convene with Nadia F. (Onboarding) inside the next week — agree a connector-availability milestone that is dated separately from the 100%-migration date, and restate L1.2's target against the date actually available for the remainder of Q3; carry the split milestone into Q4 planning.

### [Minor] AL-12 Commitment asymmetry: Ledger ↔ Onboarding
- Ledger evidence: "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22), with its stated assumption: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29)
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: Ledger's committed number rides on the producer's full target with nothing held back — and the two targets do not name the same population: Ledger's 85% is "of transactions", while the only committed rollout on Onboarding's side moves "100% of new clinics". Nothing on either page commits the rebuilt connector to clinics already onboarded, so part of Ledger's denominator may never be served by the deliverable its own note depends on.
- Detection check that fired: AL-12 edge comparison on an acknowledged dependency (the edge AL-01 did not flag) — commitment labels on each side, plus target arithmetic: full-target coupling with no discount.
- Disconfirming checks run: (1) "Missing label ≠ mismatch": both pages state a labeling scheme, "Commitment: KRs are committed unless marked (aspirational)." (`evals/corpora/tidewell-q3.md` › Ledger team — Q3 2026 › line 18; `evals/corpora/tidewell-q3.md` › Onboarding team — Q3 2026 › line 35), and both KRs are unmarked and therefore committed — there is no label mismatch, which is exactly why this is not the Major "committed depends on an explicitly stretch item" shape and is rated Minor. (2) Consumer-discount check: Ledger's note surfaces the assumption but quotes no discount, fallback or hedge — no "assumes X% of" arithmetic and no plan for clinics outside the rollout — so the check does not kill the finding.
- Inference labels: that "of transactions" spans a wider population than "new clinics" is **analyst inference** — neither page defines the transaction population or the size of either set.
- Verdict: PLAUSIBLE (all quotes re-verified character-for-character, but the population gap rests on the labeled inference above rather than on a quoted definition)
- Recommended resolution owner: Amara O. (Ledger) to state L1.2's transaction population and whether already-onboarded clinics need the rebuilt connector, with Nadia F. (Onboarding) confirming whether O1.3's rollout covers them — before the Q3 close review, and written into both pages for Q4.

## 5. Prioritized action list

1. Convene Nadia F. to confirm the connector's actual landing date and re-baseline L1.2's 85% target against the weeks left in Q3 — owner: Amara O., Ledger lead (resolves §4 AL-06 Timeline mismatch).
2. Rewrite Objective L2 so it names the change the quarter is buying instead of committing the team to continuity — owner: Amara O., Ledger lead (resolves §3 AP-10 BAU Dressed as OKR).
3. Restate L2.1 with a quoted starting value from the billing reliability source of record before the Q3 close — owner: Amara O., Ledger lead (resolves §3 AP-04 KR Without Baseline).
4. Replace L2.2's ship-by-date with a payout-volume adoption measure on the new ledger service — owner: Amara O., Ledger lead (resolves §3 AP-01 Task Masquerading as KR — Ledger, with AP-02 Binary KR with No Gradient).
5. Replace O1.3's bare 100% with a stated starting point over a named clinic population — owner: Nadia F., Onboarding lead (resolves §3 AP-01 Task Masquerading as KR — Onboarding).
6. Define the transaction population behind L1.2 and whether existing clinics need the rebuilt connector — owner: Amara O., Ledger lead, with Nadia F. (resolves §4 AL-12 Commitment asymmetry).

## 6. Suggested single-team re-runs

No team qualifies: both roll-up grades — Ledger B (2.86), Onboarding B (3.09) — sit above the rubric's needs-rework threshold (D or below), and neither team carries a Critical finding of either kind.
