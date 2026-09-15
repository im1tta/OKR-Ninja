# Tidewell — Q3 2026 OKR portfolio review

*Cycle date: 2026-09-14 · Mode: portfolio (2 teams in scope: Ledger, Onboarding) · Period: Q3 2026*
*Source corpus: `evals/corpora/tidewell-q3.md` (Confluence exports for pages 41002, 41108, 41117). Strategy source: "Company Q3 2026 priorities" (page 41002). No Atlassian connection was available; the export is the only source read.*

## 1. Executive summary

**Verdict: At risk.** 2 teams reviewed; 1 Critical, 6 Major, 0 Minor findings.
The portfolio's biggest threat is AL-06 Timeline mismatch: Ledger's committed reconciliation KR assumes the bank-link connector "lands from Onboarding in July", while Onboarding's own committed KR dates that connector "by Aug 29" — a two-month inversion inside a single quarter, with neither page noting the gap.
The most common quality issue is AP-01 Task Masquerading as KR (both teams have one: Ledger's payout-ledger ship date and Onboarding's connector rollout).
Two further alignment risks: the rebuilt connector is committed only for "new clinics" while Ledger's reconciliation target spans "transactions" portfolio-wide (AL-01 Unacknowledged dependency), and the company priority and Ledger state days-to-collect as an *average* and a *median* respectively off the same baseline of 31 (AL-08 Terminology collision).
Goodness is otherwise sound: the customer-facing objectives (L1, O1) are outcome-shaped and traceable to company priorities; the weakness is concentrated in Ledger's Objective L2, a standing-duty objective (AP-10 BAU Dressed as OKR) whose two KRs carry no baseline and no gradient.
Recommended first action: Amara O. and Nadia F. reconcile the connector date and its clinic population before the Aug 29 milestone, and restate L1.2's assumption to match whatever they agree.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ledger | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 |
| Onboarding | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Ledger C (2.7) · Onboarding B (3.1).
- Ledger: K1=2 — Objective L2's two KRs state no baseline and no countable target (AP-04, AP-01).
- Onboarding: K1=2 — O1.3's "100% of new clinics" target states no starting point (AP-01).

## 3. Per-team goodness findings

### [Major] AP-10 BAU Dressed as OKR — Ledger
- Evidence: "Objective L2: Billing stays boring as we scale" (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 25`)
- Evidence (the objective's full KR set, showing no change is named or paid for): "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 26`); "Ship the new payout ledger service to production by Sep 18. *(aspirational)*" (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 27`)
- Why it's a problem: the objective asserts that the team's standing job continues — billing *stays* as it already is — and names no change at all, which is AP-10's path (a); the KR set confirms it, since neither KR carries a baseline→target pair that would pay for a change. A quarter of ordinary operations satisfies it.
- Scores affected: O1=3, O3=2, K6=1, K7=2
- Suggested rewrite: "Objective L2: Growth stops showing up in billing — KR: failed billing runs per 1,000 runs `<baseline>` → `<target>` while active clinics grow from `<baseline>` to `<target>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Ledger
- Evidence: "Ship the new payout ledger service to production by Sep 18. *(aspirational)*" (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 27`)
- Also: AP-02 Binary KR with No Gradient
- Why it's a problem: the KR is a delivery verb with a date and neither AP-01 exclusion applies — no result measure anyone outside Ledger moves, and no baseline→target pair — so the only failure mode is lateness; and because the service is in production or it is not, mid-cycle scoring can only read 0% or 100%.
- Scores affected: K1=0, K2=1, K5=2
- Suggested rewrite: "KR L2.2 (aspirational): Payout volume settled through the new payout ledger service 0% → `<target>`% by Sep 18, at a billing run success rate no lower than the legacy path's." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Ledger
- Evidence: "Hold billing run success rate at or above 99.7% through Q3." (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 26`)
- Why it's a problem: the KR states a floor with no current value, so neither ambition nor progress can be judged — 99.7% could be a stretch or already-cleared ground, and the corpus does not say which. Search performed for a current value: the whole export (`evals/corpora/tidewell-q3.md`, all three sections — company priorities, Ledger, Onboarding) for "success", "reliab", "uptime" and "99."; the only hits are this KR (line 26) and the company priority at line 12, neither of which states an actual. No sandbag claim is made here, because none can be quoted.
- Scores affected: K1=2, K3=2 (calibration unverifiable per the rubric's K3 no-baseline cap), K5=2
- Suggested rewrite: "KR L2.1: Billing run success rate `<Q2 actual>` → 99.8%, weekly through Q3, from `<named billing dashboard of record>`." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Onboarding
- Evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md › Objective O1: A new clinic's first month runs itself › line 40`)
- Why it's a problem: "Rebuild" is a build verb and the KR carries neither AP-01 exclusion — "100% of new clinics" states no starting point, so the figure counts the rollout Onboarding finishes by shipping rather than anything a clinic does, and no outside-moved result measure (adoption, error rate, time saved) is attached. It also hides the KR that Ledger actually depends on (see §4 AL-06, AL-01).
- Scores affected: K1=2, K2=1, K5=2
- Suggested rewrite: "KR O1.3: New clinics whose first payment reconciles through the rebuilt bank-link connector `<baseline>` → 100% of the quarter's new clinics, weekly from `<onboarding dashboard of record>`; connector live for Ledger's reconciliation by `<agreed date>`." [proposal — placeholder target]

## 4. Alignment findings

Blocking keys used before any pair was inspected (per `references/alignment-taxonomy.md` Part 2 Step 3), so a reviewer knows what could have been missed: dependency-map edges (Ledger → Onboarding, the bank-link connector, the only edge in the corpus); strategy trace (3 company priorities × 3 team objectives); metric-identity key (days-to-collect; support contacts/tickets); surface-lever key (new-clinic onboarding surface; billing/collection surface). Two candidates were generated and killed: Ledger's "Cut billing support tickets per 100 clinics from 14 to 8 per month." (line 23) against Onboarding's "Reduce onboarding support contacts per new clinic from 3.1 to 1.5." (line 39) — same direction, different populations and denominators, and no text in the corpus establishes the two counts as one metric (AL-02 and AL-08 form (b) both killed); and Ledger L1 against Onboarding O1 for AL-03, killed by both pages' explicit cross-references (lines 29 and 42) and disjoint populations (active clinics vs new clinics). The surface-lever key generated nothing: no KR in either team states a friction, quality, risk or cost control as its lever.

### [Critical] AL-06 Timeline mismatch: Ledger ↔ Onboarding
- Ledger evidence: "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 29`), supporting the committed KR "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md › Objective L1: Clinics get paid without chasing anyone › line 22`)
- Onboarding evidence: "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md › Objective O1: A new clinic's first month runs itself › line 40`)
- Conflict: the consumer's need-by date (July) precedes the producer's only stated delivery date (Aug 29) by roughly two months, leaving Ledger about a month of Q3 to move auto-reconciliation 62% → 85% on a connector it assumed it would have for the whole quarter. Both KRs are committed: both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 18 and 35) and neither L1.2 nor O1.3 carries an aspirational label.
- Detection check that fired: dependency-map edge date comparison (AL-06 heuristic) — producer delivery date vs consumer need-by date on the single Ledger → Onboarding edge.
- Disconfirming checks run: "late date ≠ inversion", i.e. does an earlier milestone suffice for the consumer — searched the whole export for any connector milestone other than Aug 29 (terms "connector", "bank-link", lines 29, 40, 42); none exists, so the tightest quotable reading is the only one. Near-miss quoted and weighed: "sequencing agreed with Amara in the June planning review" (`evals/corpora/tidewell-q3.md › Objective O1: A new clinic's first month runs itself › line 42`) — it evidences a conversation but states no date and does not reconcile July with Aug 29, so it does not kill the finding; period-boundary check — both dates fall inside Q3, so the inversion is internal to the quarter, not a spillover.
- Inference labels: none — all load-bearing text quoted; the ~1-month residual runway is arithmetic on the two quoted dates and the stated quarter.
- Verdict: CONFIRMED (every quote above re-fetched and matched character-for-character against `evals/corpora/tidewell-q3.md` in the verification pass)
- Recommended resolution owner: Nadia F. (Onboarding) convenes with Amara O. (Ledger) to agree one connector-availability date and restate it on both pages — either Onboarding pulls availability into July or Ledger re-bases L1.2's 85% to the shorter runway — before the Aug 29 milestone.

### [Major] AL-01 Unacknowledged dependency: Ledger ↔ Onboarding
- Ledger evidence: "Raise auto-reconciled payment share from 62% to 85% of transactions." (`evals/corpora/tidewell-q3.md › Objective L1: Clinics get paid without chasing anyone › line 22`), with its dependency phrase "L1.2 assumes the clinic bank-link rework lands from Onboarding in July — Nadia's team owns the connector." (`evals/corpora/tidewell-q3.md › Objective L2: Billing stays boring as we scale › line 29`)
- Onboarding evidence (partial match, quoted per AL-01 evidence rule (d)): "Rebuild the clinic bank-link connector and move 100% of new clinics onto it by Aug 29." (`evals/corpora/tidewell-q3.md › Objective O1: A new clinic's first month runs itself › line 40`)
- Conflict: Onboarding commits to moving "new clinics" onto the rebuilt connector; Ledger's target is a share "of transactions", and its sibling KR scopes the team's work "across active clinics" (`evals/corpora/tidewell-q3.md › Objective L1: Clinics get paid without chasing anyone › line 21`). Nothing in Onboarding's OKRs commits to moving already-active clinics onto the new connector, so the deliverable as committed covers a narrower population than the consumer's metric.
- Detection check that fired: AL-01 edge acknowledgment with a partially matching producer item — the producer acknowledges the connector but not the population the consumer's KR spans.
- Disconfirming checks run: "missing mention ≠ unacknowledged" — searched the entire export (the only source; no Jira/Confluence access this run) for any commitment covering existing or active clinics on the new connector, terms "connector", "bank-link", "migrat", "existing", "active clinic"; hits are lines 21, 29, 40 and 42 only, and none commits Onboarding to migrating active clinics. Producer awareness quoted and weighed: "O1.3 is the connector Ledger's reconciliation work depends on; sequencing agreed with Amara in the June planning review." (`evals/corpora/tidewell-q3.md › Objective O1: A new clinic's first month runs itself › line 42`) — it acknowledges the dependency's existence but not this scope, so it weakens rather than kills the finding; severity was held at Major (not raised) on that basis, and no deprioritization statement exists that would raise it to Critical.
- Inference labels: analyst inference — that Ledger's 62% → 85% "of transactions" needs already-active clinics on the new connector. The corpus never states which clinic population feeds the auto-reconciled share, and no denominator definition is given; the inference rests only on the sibling KR's "across active clinics" wording.
- Verdict: PLAUSIBLE (quotes verified verbatim, but the population link above is inferred, not quoted)
- Recommended resolution owner: Amara O. (Ledger) states L1.2's denominator — which clinics' transactions — and, with Nadia F., decides whether active-clinic migration is in Onboarding's Q3 scope or Ledger's; resolve in the same conversation as AL-06 above, before Aug 29.

### [Major] AL-08 Terminology collision: Ledger ↔ Company priorities
- Company priorities evidence: "cut the average clinic's days-to-collect from 31 to under 20." (`evals/corpora/tidewell-q3.md › Company Q3 2026 priorities › line 10`)
- Ledger evidence: "Reduce median days-to-collect from 31 to 19 across active clinics." (`evals/corpora/tidewell-q3.md › Objective L1: Clinics get paid without chasing anyone › line 21`)
- Conflict: one metric name, two statistics — the company priority tracks the *average* clinic's days-to-collect while Ledger commits to the *median* — yet both cite the same baseline of 31. At most one of the two labels can be right about that number, and hitting a median of 19 does not guarantee an average under 20 on a right-skewed collection distribution, so the company's T1 could read as missed while Ledger's KR reads as hit.
- Detection check that fired: AL-08 form (a) — same metric name used by two parties, definitions diffed (statistic, population, source) and found to differ.
- Disconfirming checks run: "different wording ≠ different definition" — normalized both sides: Ledger names its population and source ("across active clinics"; "Days-to-collect is measured from the finance dashboard (page 41310)." — line 29), the company page names neither statistic definition nor source beyond "average", so the texts cannot be normalized to the same measurement. Page-version check: the priorities page is "Last updated 2026-06-22" (line 8) and Ledger's is "Last updated 2026-07-01" (line 17), so the later page is Ledger's and no superseding glossary exists in the corpus. Severity raised from the default Minor to Major because the colliding metric carries a company-level committed target (T1).
- Inference labels: analyst inference — that median and average diverge on this distribution; no Tidewell document states the distribution's shape, and no reconciliation of the two labels exists in the corpus.
- Verdict: CONFIRMED (both quotes re-fetched and matched character-for-character; the definitional difference is in the quoted words themselves)
- Recommended resolution owner: Rosalind K. (CEO, owner of page 41002) and Amara O. agree one definition of days-to-collect — statistic, clinic population and source dashboard — and restate both T1 and L1.1 against it at the next portfolio check-in.

## 5. Prioritized action list

1. Agree one bank-link connector availability date and write it on both pages — owner: Nadia F. with Amara O. (resolves §4 AL-06 Timeline mismatch).
2. Decide who moves already-active clinics onto the rebuilt connector, and state L1.2's denominator — owner: Amara O. with Nadia F. (resolves §4 AL-01 Unacknowledged dependency).
3. Settle whether days-to-collect is a median or an average, and restate T1 and L1.1 against it — owner: Rosalind K. with Amara O. (resolves §4 AL-08 Terminology collision).
4. Rewrite Objective L2 so it names a change and pay for it with one baseline→target KR — owner: Amara O. (resolves §3 AP-10 BAU Dressed as OKR).
5. Replace O1.3's rollout percentage with a starting point and a clinic-side result measure — owner: Nadia F. (resolves §3 AP-01 Task Masquerading as KR — Onboarding).
6. Replace L2.2's ship date with payout volume moved onto the new service — owner: Amara O. (resolves §3 AP-01 Task Masquerading as KR — Ledger, and its AP-02 Binary KR with No Gradient).
7. Add the quoted current value and a named dashboard to L2.1's success-rate floor — owner: Amara O. (resolves §3 AP-04 KR Without Baseline).

## 6. Suggested single-team re-runs

- **Ledger** (roll-up C (2.7) — above the needs-rework threshold — but qualifies on criterion (b): the Critical §4 AL-06 Timeline mismatch lands on its committed KR L1.2, alongside AP-10, AP-01/AP-02 and AP-04): re-run single-team mode — "Review the Ledger team's Q3 2026 OKRs alone, in depth. Source: `evals/corpora/tidewell-q3.md`, section 'Ledger team — Q3 2026' (Confluence page 41108, LEDG-OKR-Q3, owner Amara O.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 41002, TW-PRIO-Q3)."
- **Onboarding** (roll-up B (3.1) — above the needs-rework threshold — but qualifies on criterion (b): the same Critical §4 AL-06 Timeline mismatch lands on its committed KR O1.3, which also carries AP-01): re-run single-team mode — "Review the Onboarding team's Q3 2026 OKRs alone, in depth. Source: `evals/corpora/tidewell-q3.md`, section 'Onboarding team — Q3 2026' (Confluence page 41117, ONBD-OKR-Q3, owner Nadia F.); strategy doc: the 'Company Q3 2026 priorities' section of the same file (Confluence page 41002, TW-PRIO-Q3)."
