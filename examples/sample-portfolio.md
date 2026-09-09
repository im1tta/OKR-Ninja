# Brightledger — Q3 2026 OKRs (portfolio export)

> **Fictional test fixture.** Brightledger is an invented B2B SaaS company (invoicing & payments platform, ~200 employees). All teams, people, numbers, and page IDs below are fictional. This file mimics a Confluence export of a company priorities page, four teams' OKR pages, and a Q2 business-review extract, and deliberately contains planted defects — see the answer key at the bottom.

---

## Company Q3 2026 priorities
*Source: Confluence page 88101 (CO-PRIO-Q3) · Owner: Dana W. (CEO) · Last updated 2026-06-25*

- **C1 — Grow self-serve revenue:** mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3.
- **C2 — Become enterprise-ready:** complete SOC 2 Type II and hold enterprise-grade reliability.
- **C3 — Cut fraud losses:** bring chargeback rate under 0.5% after the Q2 incident.
- **C4 — Launch Brightledger Capital:** invoice-financing pilot live with 3 design partners by Sep 30.

---

## Payments team — Q3 2026
*Source: Confluence page 88213 (PAY-OKR-Q3) · Owner: Priya N. · Last updated 2026-07-02*
*Commitment: KRs are committed unless marked (aspirational).*

### Objective P1: Make checkout something customers never think about
- **KR P1.1:** Raise checkout success rate from 91.2% to 95% for card transactions.
- **KR P1.2:** Ship checkout & billing API v2 to GA by Sep 26.
- **KR P1.3:** Reduce median payment authorization latency from 840ms to 500ms.

### Objective P2: Cut fraud losses without drama
- **KR P2.1:** Reduce chargeback rate from 0.9% to 0.45% of transactions.
- **KR P2.2:** Increase step-up verification coverage to 90% of transactions (from 35%).

*Notes: API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup. Fraud work is our top ask from leadership after the Q2 incident (company priority C3).*

---

## Growth team — Q3 2026
*Source: Confluence page 88217 (GRW-OKR-Q3) · Owner: Marcus T. · Last updated 2026-06-28*
*Commitment: KRs are committed unless marked (aspirational).*

### Objective G1: Make the first week with Brightledger magical
- **KR G1.1:** Increase trial-to-paid conversion to 22%.
- **KR G1.2:** Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%.
- **KR G1.3:** Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter.

### Objective G2: Turn our funnel into a machine
- **KR G2.1:** Raise checkout conversion from 58% to 68% for self-serve signups.
- **KR G2.2:** Grow qualified signups from 2,100/mo to 2,800/mo.
- **KR G2.3:** Reach 50,000 monthly blog pageviews. *(aspirational)*

*Notes: self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine.*

---

## Platform team — Q3 2026
*Source: Confluence page 88221 (PLAT-OKR-Q3) · Owner: Elena R. · Last updated 2026-07-05*
*Commitment: KRs are committed unless marked (aspirational).*

### Objective PL1: Keep the lights on, cheaper
- **KR PL1.1:** Maintain API uptime at or above 99.9%.
- **KR PL1.2:** Reduce cloud spend per 1,000 transactions from $4.10 to $3.20.
- **KR PL1.3:** Improve internal developer satisfaction score to 8/10.

### Objective PL2: Earn enterprise trust
- **KR PL2.1:** Close 100% of pen-test findings rated High or above (currently 7 open).
- **KR PL2.2:** Complete the SOC 2 Type II audit.

*Notes: Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4.*

---

## Data team — Q3 2026
*Source: Confluence page 88225 (DATA-OKR-Q3) · Owner: Jonas K. · Last updated 2026-07-01*
*Commitment: KRs are committed unless marked (aspirational).*

### Objective D1: One trustworthy source of truth
- **KR D1.1:** Migrate 100% of product events to unified event schema v2.
- **KR D1.2:** Cut critical-dashboard data latency from 6h to 1h.
- **KR D1.3:** Significantly improve data quality across core tables.

### Objective D2: Own onboarding personalization end-to-end
- **KR D2.1:** Ship personalized onboarding checklists to 100% of new signups.
- **KR D2.2:** Lift new-user activation rate to 35% via onboarding experiments.

*Notes: schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level.*

---

## Appendix — Q2 2026 business review (extracts)
*Source: Confluence page 88104 (Q2-REVIEW) · Last updated 2026-06-20*

- Platform reliability: "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)."
- Payments: "Chargeback rate ended Q2 at 0.9% of transactions; step-up verification covered 35%."
- Growth: "Qualified signups averaged 2,100/mo across Q2."

---
---

## Answer key (planted defects)

**Fourteen planted defects: G1–G7 (goodness) and A1–A7 (alignment).** Every row cites its canonical ID and name from `references/goodness-rubric.md` (AP-XX) or `references/alignment-taxonomy.md` (AL-XX). Locations reference the sections above; a compliant report quotes the exact objective/KR text with a source ref (format in `references/report-format.md`).

### Goodness defects

| # | ID · Anti-pattern | Location | What's wrong |
|---|---|---|---|
| G1 | AP-01 · Task Masquerading as KR *(AP-14 · Date as Target also accepted — either ID, counted once)* | Payments KR P1.2 | "Ship checkout & billing API v2 to GA by Sep 26" is a deliverable/milestone, not a measured outcome (no adoption, error-rate, or usage target). |
| G2 | AP-04 · KR Without Baseline | Growth KR G1.1 | "Increase trial-to-paid conversion to 22%" states a target with no current value, and none is retrievable anywhere in this corpus; ambition and progress are unjudgeable. |
| G3 | AP-03 · Vanity Metric | Growth KR G2.3 | "Reach 50,000 monthly blog pageviews" rises with exposure but indicates none of the funnel outcomes the objective claims (revenue, signups, conversion). |
| G4 | AP-02 · Binary KR with No Gradient | Platform KR PL2.2 | "Complete the SOC 2 Type II audit" is done/not-done; mid-cycle scoring can only be 0% or 100%. |
| G5 | AP-06 · Sandbagged Target | Platform KR PL1.1 + Appendix (Q2 review) | Target of 99.9% uptime sits below the Q2-review trailing actual of 99.95% — the KR is achieved by getting worse. Requires verbatim quotes from **both** documents (cross-source rule in `goodness-rubric.md` Part 5). |
| G6 | AP-09 · Metric Nobody Can Measure | Data KR D1.3 | "Significantly improve data quality across core tables" names no metric, instrument, baseline, or target — it can never be honestly scored. |
| G7 | AP-04 · KR Without Baseline *(AP-09 · Metric Nobody Can Measure also accepted — either ID, counted once)* | Platform KR PL1.3 | "Improve internal developer satisfaction score to 8/10" has no baseline anywhere in the corpus (and the unnamed survey instrument additionally depresses K5). |

### Alignment defects

| # | ID · Failure mode | Location(s) | What's wrong |
|---|---|---|---|
| A1 | AL-02 · Conflicting metrics / adversarial incentives | Payments KR P2.2 ↔ Growth KR G2.1 | Step-up verification on 90% of transactions adds checkout friction while Growth targets checkout conversion 58%→68% — one team's lever predictably damages the other's target, and neither mentions the other team. |
| A2 | AL-01 · Unacknowledged dependency | Data KR D1.1 ↔ Platform OKRs | Data's 100% schema migration "rides on the streaming pipeline migration... handled at the infra level" (Data notes), but nothing in Platform's OKRs or notes mentions the pipeline, and Platform holds "all non-critical infra requests until Q4." |
| A3 | AL-06 · Timeline mismatch | Growth KR G1.3 ↔ Payments KR P1.2 | Growth needs the billing API for self-serve upgrades "by Aug 15"; Payments targets API v2 GA "by Sep 26" — a ~6-week inversion acknowledged by neither KR. |
| A4 | AL-03 · Duplicated / overlapping objectives *(AL-02 also accepted for the incompatible activation targets — either ID, counted once)* | Growth Objective G1 + KR G1.2 ↔ Data Objective D2 + KR D2.2 | Both teams claim new-user onboarding/activation with no cross-reference or division of labor, and target the same activation metric with different numbers (40% vs 35%). This is **one** defect — a report that splits it into two findings double-counts. |
| A5 | AL-07 · Resource contention | Payments notes + Data notes ↔ Platform notes | Payments assumes Platform provisions PCI-scoped infra in July; Data assumes Platform runs the pipeline migration; Platform states Q3 is "fully committed" — two implicit bookings against capacity declared not to exist. |
| A6 | AL-04 · Orphan objective | Data Objective D1 ↔ Company priorities C1–C4 | "One trustworthy source of truth" has no explicit parent link, moves no company-level metric, and no priority on page 88101 mentions data-platform work — all three orphan checks fail. |
| A7 | AL-10 · Strategy coverage gap | Company priority C4 ↔ all four teams | "Launch Brightledger Capital: invoice-financing pilot live with 3 design partners by Sep 30" is a dated company priority that no team's objectives, KRs, or notes mention — the portfolio has a hole. |

### Intentional non-defects (do not report)

Near-misses planted to measure false-positive discipline. Reporting one of these counts against the extra-findings budget in the eval criterion.

1. **Payments KR P2.1** (chargeback 0.9% → 0.45%): an ambitious but legitimate 2x cut — far below AP-07's >5x bar, with the mechanism (P2.2 step-up coverage) stated on the same page.
2. **Growth KR G1.3** ("Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter"): carries a countable adoption outcome (300 upgrades), so neither AP-01 nor AP-14 applies despite "Launch... by". (Its date is load-bearing evidence for A3, which *is* on the key.)
3. **Data KR D2.1** ("Ship personalized onboarding checklists to 100% of new signups"): "Ship" plus a coverage denominator (100% of new signups) is an adoption measure, not a pure milestone — not AP-01.
4. **Payments KR P1.1 vs Growth KR G2.1**: "checkout success rate" (91.2% → 95%, card transactions) and "checkout conversion" (58% → 68%, self-serve signups) are different metrics with different names and populations — not AL-08 and not AL-09.
5. **AP-08 · Committed vs Aspirational Not Labeled does not fire**: every team page states a commitment convention and Growth marks G2.3 aspirational.
6. **Company C3 vs Payments KR P2.1**: "under 0.5%" and "to 0.45%" are consistent targets on the same metric — not AL-02 and not AL-09.

### Triage entries

Recurring findings beyond the key, each classified once so the same debate is not re-had. A **known-red** entry is reported by the grader but excluded from the extra-findings budget until its fix lands; a **fixed** entry no longer affects counting.

1. **T1 · AP-12 on KR PL1.3** — bucket: rubric-gap · status: fixed · decision: Fixed by change fix-baseline-recall-gaps (2026-09-09): goodness rubric Part 5 rule 9 files one finding per KR under the root-cause ID with secondary IDs on the Also line, and the grader credits secondary IDs; a repeated block on one KR counts again from this change on. · rationale: In 3 of 5 baseline single-team runs (2026-09-08-baseline-02f27be) the skill files AP-12 Orphan KR on PL1.3 beside the planted AP-04 KR Without Baseline, arguing that developer satisfaction does not serve 'Keep the lights on, cheaper'. It is the same KR reported under a second ID, not a false detection; the alignment taxonomy already forbids this for AL findings (Part 3 §5) and the goodness rubric has no equivalent. Confirmed by the user on 2026-09-09.

### Modes deliberately not covered

The fixture plants no instance of **AL-05, AL-08, AL-09, AL-11, or AL-12** (nor of anti-patterns AP-05, AP-07, AP-08, AP-10, AP-11, AP-12, AP-13, AP-15). A finding citing any of them is off-key and counts against the extra-findings budget.

### Eval criterion

A passing portfolio review must:

1. surface **all 14 planted defects, cited by canonical ID** (where a row accepts either of two IDs, either passes — counted once), each with correct verbatim quotes and source refs;
2. contain **zero fabricated quotes** — every quoted span must exist character-for-character in this file;
3. raise **no more than 2 findings beyond this key** (the stated budget), with any reported item from the Intentional non-defects list counting against that budget.

### Single-team eval slice (Platform)

Grades **single-team mode** against this same fixture — no separate fixture needed.

**Run:** review the **Platform team** alone, in single-team mode. Input scope: the "Platform team — Q3 2026" section plus the "Appendix — Q2 2026 business review (extracts)" section. The company-priorities section is **not** provided, so the report must state that company-level strategy tracing was out of scope. Content from other teams' sections is outside the slice's input scope.

A passing single-team review must:

1. surface **G4 (AP-02 · Binary KR with No Gradient), G5 (AP-06 · Sandbagged Target), and G7 (AP-04 · KR Without Baseline)**, each cited by canonical ID with verbatim quotes and source refs — G5 quoting **both** the KR and the appendix's trailing actual (the cross-source rule applies unchanged in single-team mode);
2. report **zero AL-XX findings** — Platform's notes tempt a contention/dependency story, but the counterparty is out of scope; cross-team mentions belong under outbound dependency notes, unverified, with no severity;
3. score **O4 as N/A** per the rubric's no-strategy-source rule (no strategy source exists in the slice's input scope), with the rubric's gap note recorded in the score section — not a findings-section entry, and not counted against the budget below;
4. contain **zero fabricated quotes** — every quoted span must exist character-for-character in this file;
5. raise **no more than 1 finding beyond the three in item 1**, with any finding grounded in content outside the slice's input scope counting against that budget.
