# Brightledger — Q3 2026 OKRs (portfolio export)

> **Fictional test fixture.** Brightledger is an invented B2B SaaS company (invoicing & payments platform, ~200 employees). All teams, people, numbers, and page IDs below are fictional. This file mimics a Confluence export of a company priorities page, four teams' OKR pages, and a Q2 business-review extract.

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
