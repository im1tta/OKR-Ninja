# Ledger team — Q3 2026 OKR report

*Cycle date: 2026-09-14 · Period: Q3 2026 · Owner: Amara O. · Source: Confluence page 41108 (LEDG-OKR-Q3), exported at `evals/corpora/tidewell-q3.md`*

> **This page is the Ledger slice of the Tidewell Q3 2026 portfolio review** — the same run, filtered to Ledger: its heatmap row, its goodness findings, every alignment finding in which Ledger is a party, and the actions that name it. It is not a single-team-mode review: scoring here is portfolio screening depth, and the alignment findings below draw their second side from Onboarding and the company priorities page. For the cross-team picture, the other team's findings, and the full action list, see the portfolio review for the same cycle.

---

## Score row

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ledger | 3 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 2 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grade (per `references/goodness-rubric.md` Roll-Up): **B (2.76)** — the mean of Objective L1 (3.27) and Objective L2 (2.25). The gap between the two objectives is the story of this page: L1 is a well-formed outcome set, L2 is not.

- Ledger: K1=2 — "Ship the new payout ledger service to production by Sep 18" counts nothing.

Findings on this page: 1 Critical, 4 Major, 1 Minor.

## Goodness findings

### [Major] AP-10 BAU Dressed as OKR — Ledger
- Evidence: "Objective L2: Billing stays boring as we scale" (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 25)
- Evidence (the objective's full KR set, enumerated as the search for a named change): "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26) and "Ship the new payout ledger service to production by Sep 18." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27)
- Why it's a problem: "stays" asserts continuation of Ledger's standing job and the objective names no change — no direction, reduction, or improvement that differs from today — so it fires under AP-10's path (a); neither KR supplies a delta that could rescue it (one holds a rate, the other ships a service), and under the rubric a KR delta could not rescue a path-(a) objective in any case. The objective is outcome-shaped rather than a task list, which is why O1 is not floored, but it commits the team to nothing changing.
- Scores affected: O1=3, K6=1, K7=2
- Suggested rewrite: "Objective L2: Billing survives clinic growth without new failure modes — KR: billing run success rate `<Q2 actual>`% → 99.9% while monthly billing runs grow `<baseline>` → `<target>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Ledger
- Evidence: "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 26)
- Why it's a problem: the KR states a floor with no starting point, so neither ambition nor progress can be judged — 99.7% may be a stretch or already true. The corpus was searched for a current value (both team pages and the company priorities section); the nearest statement is "no degradation of billing reliability as clinic count rises" (`evals/corpora/tidewell-q3.md` › Company Q3 2026 priorities › line 12), which carries no number. Because no baseline is quotable, AP-06 Sandbagged Target is deliberately **not** filed — a sandbag can be neither confirmed nor excluded here — and K3 takes the rubric's unverifiable-calibration cap instead.
- Scores affected: K1=2, K3=2 (capped, calibration unverifiable), K5=2
- Suggested rewrite: "KR L2.1: Billing run success rate `<Q2 actual>`% → 99.9% through Q3, measured on `<named billing-run monitor>`, with no month below `<floor>`%." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Ledger
- Evidence: "Ship the new payout ledger service to production by Sep 18." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 27), labeled "(aspirational)" on the same line
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR opens with a delivery verb and carries neither of AP-01's two rescues — no result measure that anyone outside Ledger moves (no adoption, usage, or error figure) and no baseline→target pair — so it measures Ledger's own delivery, and the only way to fail it is to be late. It is also binary: until Sep 18 it scores 0%, after it 100%, with no mid-cycle gradient.
- Scores affected: K1=0, K2=1, K3=2, K5=2 (KR score capped at 1.0 by the rubric's K1=0 cap), K6=1
- Suggested rewrite: "KR L2.2 (aspirational): Monthly payout value settled through the new payout ledger service 0% → `<target>`% by Sep 30, with billing run success rate held at or above `<Q2 actual>`%." [proposal — placeholder target]

## Alignment findings naming Ledger

### [Critical] AL-06 Timeline mismatch: Ledger ↔ Onboarding
- Ledger evidence: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29)
- Ledger evidence (the dependent KR and its commitment level): "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22), governed by "KRs are committed unless marked (aspirational)" (`evals/corpora/tidewell-q3.md` › Ledger team — Q3 2026 › line 18) — L1.2 carries no aspirational marker.
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: the consumer needs the connector in July; the producer's only quoted date for it is Aug 29 — a hard inversion of roughly six weeks on a committed KR, leaving about one month of Q3 for a 23-point move in auto-reconciled share that the note says depends on it.
- Detection check that fired: AL-06 dependency-map edge date comparison — producer's delivery date (Aug 29) against the consumer's quoted need-by (July).
- Disconfirming checks run: "Late date ≠ inversion" — searched Onboarding's page for an earlier partial milestone (beta, pilot, staged rollout) that Ledger could integrate against; Onboarding states one date only, Aug 29, covering both the rebuild and the move of 100% of new clinics, so the tightest quotable reading is still Aug 29; not killed. Awareness/resolution check — found and weighed Onboarding's "O1.3 is the connector Ledger's reconciliation work depends on; sequencing agreed with Amara in the June planning review." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 42); this weakens any "nobody noticed" reading, but the note states no dates and does not reconcile July with Aug 29, so it downgrades nothing. AL-01 acknowledgment check — the connector rebuild **is** acknowledged on the producer side, so no AL-01 is filed for the rebuild itself.
- Inference labels: none — all load-bearing text quoted; the six-week gap is arithmetic on two quoted dates.
- Verdict: CONFIRMED (both dated statements re-verified character-for-character against the source, and the pages' last-updated stamps — Ledger 2026-07-01, Onboarding 2026-06-30 — were checked for supersession).
- Recommended resolution owner: Amara O. (Ledger) and Nadia F. (Onboarding) to agree within one week either a dated partial connector milestone Ledger can reconcile against in July, or a restated L1.2 target calibrated to an Aug 29 start — and to write the agreed dates onto both pages rather than leaving them in a planning review.

### [Major] AL-08 Terminology collision: Ledger ↔ Company Q3 2026 priorities (T1)
- Company priorities evidence: "cut the average clinic's days-to-collect from 31 to under 20" (`evals/corpora/tidewell-q3.md` › Company Q3 2026 priorities › line 10)
- Ledger evidence: "Reduce median days-to-collect from 31 to 19 across active clinics." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 21)
- Conflict: one metric name, two statistics — the company's top priority is stated as an **average** and the only KR serving it moves a **median**, with both pages claiming 31 as today's value. Ledger can hit a 19 median and report T1 delivered while the average the CEO page tracks sits above 20.
- Detection check that fired: AL-08 form (a) — a metric name used on two pages ("days-to-collect"), definitions hunted on each page and diffed; blocking key: same canonical metric.
- Disconfirming checks run: "Different wording ≠ different definition" — normalized both readings; average and median are different statistics of one distribution and do not reduce to the same measurement, so not killed. Page-version check — company page "Last updated 2026-06-22" versus Ledger page "Last updated 2026-07-01"; the later page is a team OKR page, not a glossary, and claims no redefinition, so supersession does not explain the split. AL-09 check — the two stated baselines do not differ, so the root cause is definitional and AL-09 Baseline disagreement is not double-counted here. Population check — "the average clinic" versus "across active clinics" also differ; recorded as part of the same collision rather than a separate finding.
- Inference labels: that both figures cannot normally describe the same right-skewed collections distribution — so at least one "31" is measuring something other than what its page says — is analyst inference; the average/median divergence itself is quoted on both sides.
- Verdict: CONFIRMED (both quotes re-verified character-for-character; escalated to Major, over AL-08's Minor default, because the colliding metric is the company's own exec-level T1 measure).
- Recommended resolution owner: Rosalind K. (owner of page 41002) with Amara O. to publish one definition of days-to-collect — statistic, clinic population, as-of date — and restate T1 and KR L1.1 against it before the mid-quarter check-in.

### [Major] AL-01 Unacknowledged dependency: Ledger ↔ Onboarding
- Ledger evidence: "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 22), with its stated dependency "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md` › Objective L2: Billing stays boring as we scale › line 29)
- Onboarding evidence (the partially matching item): "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 40)
- Conflict: the populations do not meet. Ledger's target spans "transactions" with no population limit; Onboarding's only rollout commitment covers "new clinics." Nothing in scope commits anyone to moving existing clinics onto the rebuilt connector, so the acknowledged dependency is covered only for the newest slice of the book.
- Detection check that fired: AL-01 dependency-edge resolution — the deliverable named in Ledger's dependency phrase was resolved to the owning team's plans and matched only partially, which AL-01's evidence rule (d) requires be quoted and explained rather than treated as coverage.
- Disconfirming checks run: "Missing mention ≠ unacknowledged" — could **not** be completed: no Atlassian source is connected for this run, so Onboarding's epics and backlog were not searchable; the absence claim is therefore bounded to the two OKR pages and the company priorities section, and the verdict is held at PLAUSIBLE for that reason. Corpus search for existing-clinic coverage — terms "existing clinic", "migrat", "backfill", "all clinics" across the whole file returned zero hits; the only clinic-population wording attached to the connector is "new clinics" on line 40, quoted above as the near-miss.
- Inference labels: that Ledger needs existing clinics on the rebuilt connector to reach 85% of all transactions is **analyst inference** — the corpus states no transaction mix between new and existing clinics, and no team page says which population L1.2's denominator covers.
- Verdict: PLAUSIBLE
- Recommended resolution owner: Amara O. to state before the next planning checkpoint which clinic population L1.2's "of transactions" denominator covers, and Nadia F. to confirm whether existing-clinic migration is inside O1.3's scope or unowned this quarter.

### [Minor] AL-08 Terminology collision: Ledger ↔ Onboarding
- Ledger evidence: "Cut billing support tickets per 100 clinics from 14 to 8 per month." (`evals/corpora/tidewell-q3.md` › Objective L1: Clinics get paid without chasing anyone › line 23)
- Onboarding evidence: "Reduce onboarding support contacts per new clinic from 3.1 to 1.5." (`evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 39)
- Conflict: two committed reduction targets sit on adjacent per-clinic support volumes under two names — "tickets" and "contacts" — with no stated formula, queue, or boundary between them. A new clinic's billing question in its first month plausibly lands in both counters, and neither page says which team's number it moves.
- Detection check that fired: AL-08 form (b) blocking — near-identical measurements travelling under different names, both per-clinic-normalized support volume, surfaced by the metric catalog.
- Disconfirming checks run: definition diff — searched both pages for a formula, window, or population for each metric; Onboarding names a source only ("Support-contact counts come from the Zendesk weekly export." — `evals/corpora/tidewell-q3.md` › Objective O1: A new clinic's first month runs itself › line 42), Ledger names none for tickets, so the two definitions could not be normalized and no documented split of populations exists. Surface check — "billing" and "onboarding" name different surfaces, which argues against a true collision; this check weakened the finding and is why it is filed Minor rather than Major and PLAUSIBLE rather than CONFIRMED.
- Inference labels: the equivalence of "tickets" and "contacts", and the double-count scenario, are both **analyst inference** — no text in the corpus establishes either.
- Verdict: PLAUSIBLE
- Recommended resolution owner: Amara O. and Nadia F. to add a one-line definition (queue, population, source system) beside each metric on their own pages this cycle, and to name which counter owns a first-month billing contact.

## Actions naming Ledger

Numbering is kept from the portfolio review's §5 so the two pages can be read side by side; item 4 (Onboarding's KR O1.3 rewrite) is the one action that does not name Ledger.

1. Agree a dated partial connector milestone for July, or restate KR L1.2 against an Aug 29 start — owner: Amara O. with Nadia F. (resolves §4 AL-06 Timeline mismatch).
2. Publish one definition of days-to-collect (statistic, population, as-of date) and restate T1 and KR L1.1 against it — owner: Rosalind K. with Amara O. (resolves §4 AL-08 Terminology collision: Ledger ↔ Company Q3 2026 priorities).
3. State which clinic population L1.2's "of transactions" covers and whether existing-clinic migration sits inside O1.3 — owner: Amara O. with Nadia F. (resolves §4 AL-01 Unacknowledged dependency).
5. Recast Objective L2 as a change the team must pay for rather than a continuation of billing's standing state — owner: Amara O. (resolves §3 AP-10 BAU Dressed as OKR).
6. Retrieve and publish the Q2 billing run success actual, then restate KR L2.1 as a baseline→target pair — owner: Amara O. (resolves §3 AP-04 KR Without Baseline — Ledger).
7. Rewrite KR L2.2 as payout volume settled through the new service, keeping its aspirational label — owner: Amara O. (resolves §3 AP-01 Task Masquerading as KR — Ledger, and its AP-02 Binary KR with No Gradient).
8. Add one-line definitions beside both support metrics and assign first-month billing contacts to one counter — owner: Nadia F. with Amara O. (resolves §4 AL-08 Terminology collision: Ledger ↔ Onboarding).
