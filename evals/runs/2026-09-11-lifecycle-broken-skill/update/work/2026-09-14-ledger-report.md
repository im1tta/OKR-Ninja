# Ledger — Q3 2026 OKR review (Tidewell portfolio slice)

*OKR-Ninja portfolio-mode audit · cycle date 2026-09-14 · period Q3 2026 · team owner Amara O.*
*This page is the Ledger slice of the Tidewell Q3 2026 portfolio review — the same run, filtered to Ledger. It is **not** a single-team-mode review: the scores below are portfolio screening depth, and the alignment findings are the portfolio run's AL-XX blocks, which quote both sides. Section numbers refer to the full portfolio report.*
*Source in scope: `evals/corpora/tidewell-q3.md` (local export; no Atlassian connection available). Strategy source: the file's "Company Q3 2026 priorities" section (T1–T3).*

---

## Heatmap row (§2)

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ledger | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **Ledger B (2.76)** — the mean of objective L1 at B (3.37) and objective L2 at C (2.16), where L2 sits under the rubric's ≥2-Major-anti-patterns cap. For comparison, the portfolio's other team scored Onboarding C (2.4).

- Ledger: K1=2 — L2.2 is a ship-by-date milestone and L2.1 states no baseline (AP-01, AP-04).

Ledger raised no Critical finding and its roll-up grade is above the rubric's needs-rework threshold, so §6 of the portfolio report recommends **no** single-team-mode re-run for this team.

## Goodness findings (§3)

### [Major] AP-10 BAU Dressed as OKR — Ledger
- Evidence: "Billing stays boring as we scale" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 25)
- Evidence (the objective's full KR set, enumerated as the absence search): "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26); "Ship the new payout ledger service to production by Sep 18. *(aspirational)*" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Why it's a problem: the objective asserts continuation of Ledger's standing job — billing keeps working the way it works today — and names no change at all: no direction, no reduction, no improvement that differs from today, which is AP-10 path (a). Neither KR rescues it, and under path (a) KR deltas never could: one holds a rate at a floor and the other ships a service, so the quarter can be scored "achieved" by the team doing exactly its existing job.
- Scores affected: O1=3, K6=1, K7=2
- Suggested rewrite: "Objective L2: Billing survives clinic growth without clinics noticing — KR: failed billing runs per 1,000 clinic-months `<baseline>` → `<target>`, held while active clinic count rises from `<current>` to `<target>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Ledger
- Evidence: "Ship the new payout ledger service to production by Sep 18. *(aspirational)*" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and carries neither of AP-01's two rescues — no baseline→target pair and no measure that anyone outside Ledger moves — so it is satisfied by the deploy itself, whether or not a single clinic payout ever runs through the service. Mid-cycle it can only be scored 0% or 100%, which is AP-02: there is no gradient to steer by between now and Sep 18.
- Scores affected: K1=0, K2=1, K6=1, K7=2
- Suggested rewrite: "KR L2.2 (aspirational): Clinic payout volume served by the new payout ledger service 0% → `<target>`% by Sep 18, with billing run success rate on that volume at or above 99.7% (source: `<billing dashboard>`)." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Ledger
- Evidence: "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26)
- Why it's a problem: the KR states a floor with no starting point, and no current or prior value for billing run success exists anywhere in the corpus — searched: the whole file in scope (company priorities section lines 7–12, the Ledger page and its notes lines 16–29, the Onboarding page and its notes lines 33–42) for "success rate", "billing run", "99." and any prior-period actual; the only number attached to billing reliability is this KR's own 99.7%. Because of that absence this is filed as AP-04 and **not** as AP-06 Sandbagged Target: calling a floor a sandbag would require a baseline that is not quotable, which the rubric's evidence discipline forbids (Part 5, rule 5).
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR L2.1: Billing run success rate `<Q2 actual>`% → at or above 99.7% in every weekly billing run through Q3 (source: `<billing dashboard>`)." [proposal — placeholder target]

## Alignment findings naming Ledger (§4)

All four of the portfolio run's alignment findings involve Ledger. Each quotes both sides, as the taxonomy requires; the counterparty quotes are reproduced here unchanged.

### [Major] AL-08 Terminology collision: Ledger ↔ Company Q3 2026 priorities
- Company priorities evidence: "cut the average clinic's days-to-collect from 31 to under 20" (`evals/corpora/tidewell-q3.md` › Company Q3 2026 priorities › line 10)
- Ledger evidence: "Reduce median days-to-collect from 31 to 19 across active clinics." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 21)
- Conflict: the company's headline T1 number is an average and Ledger's committed KR moves the median, under one metric name and one shared baseline of 31. On a right-skewed collection distribution — the normal shape for receivables — the median can reach 19 while the average stays above 20, so Ledger's KR can be fully achieved in a quarter where the priority it serves fails.
- Detection check that fired: AL-08 form (a) — one metric name ("days-to-collect") used on two pages with different formulas, found by diffing the definitions attached to a metric name used by ≥2 parties.
- Disconfirming checks run: *normalize before diffing* — mean and median are definitionally different statistics and do not reduce to the same measurement, so the difference survives normalization; *superseded page* — the company page reads "Last updated 2026-06-22" and the Ledger page "Last updated 2026-07-01", and the corpus contains no glossary reconciling them, so the later page did not adopt an agreed definition; *AL-09 Baseline disagreement checked first* (as the taxonomy requires) and killed — both sides state 31, so a baseline split does not explain the gap; *different populations* — "the average clinic" and "across active clinics" describe the same clinic population, not two segments.
- Inference labels: none — all load-bearing text is quoted, and mean-vs-median divergence is a definitional property of the two statistics rather than an inferred mechanism.
- Verdict: CONFIRMED (both quotes re-read character-for-character against the file in the verification pass)
- Severity note: raised from AL-08's Minor default to **Major** on the taxonomy's "used in an exec rollup" condition — the metric is company priority T1, owned by the CEO. The Severity-section escalation clause is deliberately not applied a second time to that same fact.
- Recommended resolution owner: Rosalind K. (CEO, owner of the T1 priority) to decide with Amara O. which statistic T1 is scored on, and restate both the priority line and KR L1.1 in that one statistic — before the next cycle checkpoint, since the quarter's headline number is at stake.

### [Major] AL-06 Timeline mismatch: Ledger ↔ Onboarding
- Ledger evidence: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29)
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: the consumer's stated need-by for the connector is July; the producer's only committed date for that same connector is Aug 29 — up to a month later, with no integration margin quoted on either side before Ledger's own end-of-quarter target on KR L1.2. Both KRs are committed under the pages' stated convention ("KRs are committed unless marked (aspirational)").
- Detection check that fired: AL-06 edge-date comparison on the dependency map — producer delivery date against consumer need-by date on the single Ledger → Onboarding edge.
- Disconfirming checks run: *late date ≠ inversion, tightest quotable reading* — "by Aug 29" is an outer bound that does not exclude the rebuild landing earlier, so the inversion is possible rather than certain; this check is what moved the finding down from AL-06's Critical anchor (hard inversion on committed KRs) to Major. *Producer awareness* — Onboarding does acknowledge the edge: "O1.3 is the connector Ledger's reconciliation work depends on; sequencing agreed with Amara in the June planning review." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 42) — which rules out AL-01 on the connector itself and weakens this finding further, but the corpus attaches no date to that agreed sequencing, so it does not reconcile July with Aug 29.
- Inference labels: that Aug 29 is the earliest reliable availability of the rebuild is **analyst inference** — the corpus gives one date for a KR that bundles the rebuild and the migration, and states no separate rebuild date.
- Verdict: PLAUSIBLE — every quote was re-verified character-for-character, but one load-bearing step (reading Aug 29 as the rebuild's availability) is inferred rather than quoted, which keeps it below the taxonomy's bar for CONFIRMED.
- Recommended resolution owner: Nadia F. to state the connector rebuild's own availability date separately from the Aug 29 migration date, and Amara O. to re-baseline or re-plan KR L1.2 against whatever that date turns out to be, within two weeks of this review.

### [Minor] AL-01 Unacknowledged dependency: Ledger ↔ Onboarding
- Ledger evidence: "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22)
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: Ledger's target spans all transactions, while the only cutover anyone commits to covers "100% of new clinics". Nothing in the corpus commits any team to moving existing clinics onto the rebuilt connector, so the population that supplies most of a Q3 transaction base has no owner for that move.
- Detection check that fired: AL-01 evidence rule (d) — the producer has a *partially* matching item, which must be quoted and distinguished from the need rather than treated as coverage.
- Disconfirming checks run: *missing mention ≠ unacknowledged* — search performed over the entire corpus (the only source in scope; no Jira or Confluence connection is available in this run): Onboarding's three KRs (lines 38–40) and its notes (line 42), plus Ledger's own notes (line 29), for "existing", "migrat", "backfill", "all clinics" and "active clinics" — the only migration commitment found is O1.3's "100% of new clinics", quoted above. *AL-12 Commitment asymmetry* checked and killed — both sides are committed under each page's stated convention, so there is no label mismatch to report. *Consumer's own framing* — Ledger's stated assumption is narrower than the gap: it quotes only that "the clinic bank-link rework lands", which O1.3's rebuild clause does cover; this is what holds the finding at Minor.
- Inference labels: that existing clinics' transactions must run on the rebuilt connector for Ledger to reach 85% is **analyst inference** — no document states what share of transactions comes from new versus existing clinics.
- Verdict: PLAUSIBLE
- Recommended resolution owner: Amara O. to confirm with Nadia F. whether 85% of transactions is reachable on new-clinic volume alone, and if it is not, to get an existing-clinic migration into one named team's Q3 plan before the connector cuts over.

### [Minor] AL-02 Conflicting metrics / adversarial incentives: Onboarding ↔ Ledger
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Ledger evidence: "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26)
- Conflict: Onboarding commits to replacing and cutting over a component on the clinic payment path inside the same quarter in which Ledger commits to no degradation of that path's success rate. The change and the guardrail sit on one surface, and neither page acknowledges the other team's stake in it — the cutover's risk lands on a number Ledger alone is scored against.
- Detection check that fired: AL-02 surface-lever key (2) — both KRs touch the clinic payment/billing surface, Onboarding's stated lever is a rebuild-and-cutover (feature velocity) and Ledger's KR targets that surface's reliability metric: the "feature velocity vs. reliability/error budget" shape the key names. Key (1) metric-identity generated nothing here — the two KRs share no metric name.
- Disconfirming checks run: *shared or parent OKR covering both* — none found in the corpus; *documented split of levers* — none found; *directionality* — the metrics differ, so this is a mechanism-level candidate rather than a directly opposed pair, which caps it below AL-02's Critical anchor; *documented mechanism* — no Tidewell document states a cutover-versus-reliability tradeoff, so the coupling is speculative, which holds the finding at AL-02's Minor floor.
- Inference labels: the cutover → billing-run-reliability mechanism is **analyst inference** (no document in the corpus states the tradeoff).
- Verdict: PLAUSIBLE
- Recommended resolution owner: Amara O. and Nadia F. to agree a cutover guardrail — the billing-run success floor at which the connector migration pauses — and record it on both pages before Aug 29.

## Actions naming Ledger (§5)

Numbering is the portfolio report's, so the items can be matched back to it. Item 4 of that list is Onboarding-only and is omitted here.

1. Decide which statistic T1 is scored on — mean or median days-to-collect — and restate both the priority line and KR L1.1 in it; owner: Rosalind K. with Amara O. (resolves §4 AL-08 Terminology collision).
2. Publish the connector rebuild's own availability date, separate from the Aug 29 migration date, and re-plan KR L1.2 against it; owner: Nadia F. with Amara O. (resolves §4 AL-06 Timeline mismatch).
3. Rewrite KR L2.2 so it measures payout volume served by the new service rather than the deploy date; owner: Amara O. (resolves §3 AP-01 Task Masquerading as KR / AP-02 Binary KR with No Gradient — Ledger).
5. Add the Q2 actual for billing run success rate as KR L2.1's baseline and name its dashboard; owner: Amara O. (resolves §3 AP-04 KR Without Baseline — Ledger).
6. Reframe objective L2 around a change Ledger will pay for — reliability held against rising clinic count — rather than around billing continuing to work; owner: Amara O. (resolves §3 AP-10 BAU Dressed as OKR — Ledger).
7. Confirm whether 85% of transactions is reachable on new-clinic volume alone, and place any existing-clinic migration in a named team's plan; owner: Amara O. with Nadia F. (resolves §4 AL-01 Unacknowledged dependency).
8. Agree and record a billing-run success floor that pauses the connector cutover; owner: Amara O. with Nadia F. (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
