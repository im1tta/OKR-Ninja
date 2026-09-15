# Ledger — Q3 2026 OKR Review (Tidewell portfolio slice)

*Cycle date: 2026-09-14 · This page is the Ledger slice of the Tidewell Q3 2026 portfolio review — Ledger's heatmap row, the goodness findings on its OKRs, the alignment findings that name it, and the actions it owns. It is not a single-team-mode deep dive: the scores and findings below are the portfolio run's screening-depth output, produced with Onboarding in scope.*
*Source: `evals/corpora/tidewell-q3.md` (Ledger team page: Confluence page 41108, LEDG-OKR-Q3, Owner: Amara O.) · Strategy source: "Company Q3 2026 priorities" (T1–T3), same file.*

---

## Score row

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ledger | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Ledger B (2.9)** — Objective L1 scores 3.4 (B); Objective L2 scores 2.4 (C, capped by two or more Major anti-patterns on one OKR).

- Ledger: K1=2 — L2.2 states no metric and L2.1 no baseline (AP-01, AP-04).

Objective L1 "Clinics get paid without chasing anyone" is the strongest OKR in the portfolio: three KRs, each with a named metric, a quoted baseline and a quoted target, and a named system of record for the headline one. Every finding below sits on Objective L2 or on Ledger's cross-team dependency.

## Goodness findings

### [Major] AP-10 BAU Dressed as OKR — Ledger
- Evidence: "Objective L2: Billing stays boring as we scale" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 25)
- Why it's a problem: the objective asserts that the team's standing duty continues — billing keeps working — and names no change at all, and neither of its two KRs pays for one with a baseline→target pair ("Hold billing run success rate at or above 99.7% through Q3." holds a level; "Ship the new payout ledger service to production by Sep 18. (aspirational)" is a delivery date), so the objective is achievable by default staffing while occupying a slot a real goal could hold.
- Scores affected: K3=2 (L2.1, L2.2), K7=2
- Suggested rewrite: "Objective L2: Billing survives clinic growth without a human rescuing it — KR: manual interventions per billing run `<baseline>` → `<target>` per month, from `<billing ops log>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Ledger
- Evidence: "KR L2.1: Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26)
- Why it's a problem: the KR states a floor with no starting point, so neither its ambition nor its progress can be judged — it is unknowable from this corpus whether 99.7% is a stretch or already the trailing rate. Search performed for a baseline: every line of `evals/corpora/tidewell-q3.md` — the company priorities section (lines 10–12), both team pages (lines 16–29, 33–42) and both notes lines (29, 42); the closest near-miss is the company priority "T3 — Hold the platform steady while we grow: no degradation of billing reliability as clinic count rises." (`evals/corpora/tidewell-q3.md` › Company Q3 2026 priorities › line 12), which states no number either. No prior-period actual is quotable, so calibration is unverifiable and K3 takes the rubric's cap rather than a sandbag score.
- Scores affected: K1=2, K3=2, K5=2
- Suggested rewrite: "KR L2.1: Billing run success rate `<Q2 actual, per the finance dashboard (page 41310)>`% → `<target>`%, measured weekly through Q3." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Ledger
- Evidence: "KR L2.2: Ship the new payout ledger service to production by Sep 18. (aspirational)" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and carries neither a result measure anyone outside Ledger moves nor a baseline→target pair, so it succeeds the moment the service reaches production even if no payout ever runs through it; and with no numeric scale, mid-cycle scoring can only read 0% or 100%.
- Scores affected: K1=0, K2=1, K5=2 (K1=0 caps this KR at 1.0 per the rubric's roll-up caps)
- Suggested rewrite: "KR L2.2 (aspirational): Payout volume settled through the new payout ledger service 0% → `<target>`% by Sep 18, with payout failure rate no worse than `<current rate>`, from `<the finance dashboard (page 41310)>`." [proposal — placeholder target]

## Alignment findings naming Ledger

### [Major] AL-06 Timeline mismatch: Ledger ↔ Onboarding
- Ledger evidence: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29)
- Ledger evidence (the dependent KR, and its commitment level): "KR L1.2: Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22); "Commitment: KRs are committed unless marked (aspirational)." (`evals/corpora/tidewell-q3.md` › Ledger team — Q3 2026 › line 18)
- Onboarding evidence: "KR O1.3: Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Onboarding evidence (producer-side acknowledgment): "O1.3 is the connector Ledger's reconciliation work depends on; sequencing agreed with Amara in the June planning review." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 42)
- Conflict: the consumer's need-by date ("in July") precedes the only date the producer commits to for that connector ("by Aug 29"), so a committed KR is calibrated on an arrival the producing team's own committed KR does not promise; at the quoted dates Ledger has roughly the last month of the quarter to move auto-reconciliation from 62% to 85%.
- Detection check that fired: AL-06 edge date comparison on the dependency map — producer's delivery date vs. consumer's need-by date, both quoted from OKR text.
- Disconfirming checks run: (1) "Late date ≠ inversion" — **weakens the finding**: Ledger needs the connector to "land", while Aug 29 attaches to the compound "Rebuild ... and move 100% of new clinics onto it", so Aug 29 is a ceiling on the rebuild rather than a quotable availability date; no earlier rebuild date exists anywhere in the corpus, so the inversion holds only on the tightest quotable reading and the finding is reported Major rather than Critical. (2) AL-01 acknowledgment search over Onboarding's page (lines 33–42, terms: "connector", "bank-link", "Ledger", "reconciliation") — **kills AL-01**: the producer acknowledges the dependency in KR O1.3 and its notes, so this is a date mismatch, not a missing commitment. (3) AL-12 label comparison — no asymmetry: both pages state "KRs are committed unless marked (aspirational)" and neither L1.2 nor O1.3 carries an aspirational marker, so both sides are committed. (4) Quarter-boundary check — both dates fall inside Q3 2026; no KR is due after the period ends.
- Inference labels: the four-to-eight week exposure implied by July vs. Aug 29 is arithmetic on the two quoted dates, not a quoted claim — analyst inference. Whether the rebuild could land before the Aug 29 migration completes is unknown from the corpus and is not assumed either way.
- Verdict: CONFIRMED (every load-bearing quote re-opened and matched character-for-character against `evals/corpora/tidewell-q3.md` in the Step 5 verification pass)
- Recommended resolution owner: Nadia F. (Onboarding) to publish a connector-available milestone date distinct from the Aug 29 migration date, and to confirm with Amara O. (Ledger) which clinic population the rebuilt connector covers, before the mid-quarter check-in; if the connector cannot land before August, Amara O. re-times or re-scopes the 85% target on KR L1.2.

### [Major] AL-08 Terminology collision: Company priorities ↔ Ledger
- Company priorities evidence: "T1 — Get clinics paid faster: cut the average clinic's days-to-collect from 31 to under 20." (`evals/corpora/tidewell-q3.md` › Company Q3 2026 priorities › line 10)
- Ledger evidence: "KR L1.1: Reduce median days-to-collect from 31 to 19 across active clinics." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 21)
- Conflict: one metric name, two different statistics — the company tracks "the average clinic's days-to-collect" while Ledger commits to the "median" — and both attach the same baseline of 31, which cannot be true of both statistics unless the distribution is symmetric. Ledger can deliver a median of 19 while the average the CEO's page reports stays above 20, so the company priority can fail with its only contributing KR fully green.
- Detection check that fired: AL-08 form (a), same name / different definition — the metric name "days-to-collect" is used by two parties, and diffing their stated formulas and populations ("the average clinic" vs. "median ... across active clinics") returns a genuine split.
- Disconfirming checks run: (1) "Different wording ≠ different definition" — **does not kill**: average and median are distinct statistics that do not normalize to one measurement, and "the average clinic" and "active clinics" name different populations. (2) Page-version check — company page "Last updated 2026-06-22", Ledger page "Last updated 2026-07-01" (lines 8 and 17); neither supersedes the other, and no glossary page exists in the corpus. (3) AL-09 baseline check — both sides state 31, so this is not a baseline disagreement; the collision is definitional. (4) Data-source check — Ledger names one ("Days-to-collect is measured from the finance dashboard (page 41310)." — line 29); the company page names none, so no shared system of record settles which statistic is authoritative.
- Inference labels: the claim that a median can improve while an average does not is a property of the two statistics, labeled analyst inference — no Tidewell document states this tradeoff.
- Verdict: CONFIRMED (both quotes re-opened and matched character-for-character against `evals/corpora/tidewell-q3.md`)
- Recommended resolution owner: Rosalind K. (CEO, owner of the priorities page) to settle one statistic and one population for days-to-collect, and to have T1 and KR L1.1 restated against it — with the finance dashboard (page 41310) named as the system of record on both pages — within two weeks.

## Actions naming Ledger

Numbering is the portfolio review's; items 1 and 2 are alignment actions Ledger participates in but does not own.

1. Publish a connector-available date distinct from the Aug 29 migration date and reconcile it against Ledger's July assumption — owner: Nadia F., Onboarding; Ledger counterpart: Amara O., who re-times or re-scopes KR L1.2's 85% target if the date moves (resolves §4 AL-06 Timeline mismatch).
2. Settle one days-to-collect statistic and population across the company page and KR L1.1 — owner: Rosalind K., CEO; Ledger restates KR L1.1 against the agreed definition (resolves §4 AL-08 Terminology collision).
4. Rewrite KR L2.2 as a payout-volume-through-the-new-service measure instead of a ship date — owner: Amara O., Ledger (resolves §3 AP-01 Task Masquerading as KR — Ledger, and its Also: AP-02 Binary KR with No Gradient).
5. Add the quoted trailing baseline and the finance dashboard (page 41310) as system of record to KR L2.1 — owner: Amara O., Ledger (resolves §3 AP-04 KR Without Baseline — Ledger).
6. Reframe Objective L2 around a change at least one KR pays for with a baseline→target pair, or move the standing reliability duty to a health-metric section — owner: Amara O., Ledger (resolves §3 AP-10 BAU Dressed as OKR — Ledger).

*(Item 3 of the portfolio action list is owned by Onboarding and does not name Ledger.)*

## Re-run status

Ledger does not qualify for a single-team-mode re-run: its roll-up grade is B (2.9), above the rubric's D needs-rework threshold, and it carries no Critical finding.
