# Coppervale — Q1 2027 OKRs (portfolio export)

> **Fictional test fixture #2.** Coppervale is an invented B2B field-service & delivery-operations SaaS (~300 employees). All teams, people, numbers, and page IDs below are fictional. This file mimics a Confluence export of a company priorities page, five teams' OKR pages, and a Q4 business-review extract.

---

## Company Q1 2027 priorities
*Source: Confluence page 91050 (CO-PRIO-Q1FY27) · Owner: Noor E. (CEO) · Last updated 2026-12-18*

- **C1 — Win mid-market logistics:** grow ARR from $14M to $17.5M run-rate by end of Q1, led by enterprise dispatch adoption and frictionless self-serve billing.
- **C2 — Keep enterprise customers for life:** reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers.
- **C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80% across FY27.
- **C4 — Run lean:** cloud cost per completed delivery from $0.42 to $0.30 — consolidate our duplicated data and telemetry pipelines and run weekly ops reviews from shared dashboards.

---

## Dispatch team — Q1 2027
*Source: Confluence page 91112 (DSP-OKR-Q1) · Owner: Mei L. · Last updated 2027-01-04*
*Commitment: KRs are committed unless marked (stretch).*

### Objective DS1: Delight enterprise dispatchers and expand Coppervale into two new regions *(supports C1)*
- **KR DS1.1:** Enterprise dispatcher NPS 24 → 40 (quarterly in-product survey, Delighted dashboard "Dispatcher NPS").
- **KR DS1.2:** Signed pilot customers in DE and FR: 0 → 6 (CRM "Intl Pilots" view).

### Objective DS2: Enterprise teams run their whole day in Coppervale dispatch *(supports C1)*
- **KR DS2.1:** On-time delivery rate — jobs completed within the promised window as a share of all completed jobs, measured weekly in the Ops Console — 91% → 95%.
- **KR DS2.2:** 600 enterprise trial starts via the partner portal launch (0 → 600, CRM campaign "Portal Trials").
- **KR DS2.3:** Median time to build a full-day route plan 14 min → 6 min (Ops Console telemetry).
- **KR DS2.4:** Reduce the failure rate from 6% to 3% by end of Q1 (ops weekly report).

*Notes: DS2.2 assumes the partner portal launch — Accounts owns the portal build this quarter. On-time delivery is measured per our Ops Console methodology (see KR DS2.1).*

---

## Courier team (driver app) — Q1 2027
*Source: Confluence page 91116 (COUR-OKR-Q1) · Owner: Tomás R. · Last updated 2027-01-06*

### Objective CR1: Drivers finish every shift without fighting the app *(supports C3)*
- **KR CR1.1:** Crash-free sessions 99.2% → 99.6% (Firebase Crashlytics).
- **KR CR1.2:** Driver-app weekly retention 71% → 78% (Amplitude cohort "Driver Weekly Retention"; Q1 step toward the FY27 80% goal in C3).

### Objective CR2: Every driver in the region hears about Coppervale from another driver *(supports C3)*
- **KR CR2.1:** Driver referral installs 3,000 → 45,000 this quarter (App Store + Play attributed installs).

### Objective CR3: Every driver action is visible to the teams that need it *(supports C4)*
- **KR CR3.1:** Instrument all 14 core driver flows with telemetry SDK v1 (0/14 → 14/14, flow coverage checklist) once Core Systems GAs the SDK.
- **KR CR3.2:** Event loss rate on instrumented flows — lost events as a share of events emitted on those flows — 2.1% → 0.6% (Grafana "Courier Events" board).

*Notes: referral growth is our big swing this quarter. SDK timing per Core Systems' plan.*

---

## Core Systems team — Q1 2027
*Source: Confluence page 91120 (CORE-OKR-Q1) · Owner: Adaeze O. · Last updated 2027-01-05*
*Commitment: KRs are committed unless marked (stretch).*

### Objective CS1: Continue running the platform smoothly for every team *(supports C4)*
- **KR CS1.1:** Sev-1 incidents per quarter 9 (Q4 actual, incident review) → ≤ 4.
- **KR CS1.2:** Cloud cost per completed delivery $0.42 → $0.30 (Cost Explorer dashboard "Unit Cost").

### Objective CS2: Ship with confidence *(supports C2 — enterprise churn)*
- **KR CS2.1:** Deploy frequency 2/week → 8/week (Buildkite deploy log).
- **KR CS2.2:** Change-failure rate 18% → 8% of production deploys (incident review tags).
- **KR CS2.3:** CI pipeline p95 42 min → 15 min (Buildkite analytics).

### Objective CS3: One telemetry pipeline every product team trusts *(supports C4)*
- **KR CS3.1:** GA telemetry SDK v1 after Insights validates event schema v3 in production, with internal apps live on it 1 → 3 (SDK adoption dashboard).
- **KR CS3.2:** Telemetry ingestion p95 latency 45s → 12s (Grafana "Pipeline Health").

*Notes: SDK v1 is code-complete; GA is gated on schema v3 validation (Insights). The cost work is our C4 commitment.*

---

## Insights team — Q1 2027
*Source: Confluence page 91124 (INS-OKR-Q1) · Owner: Halima D. · Last updated 2027-01-07*
*Commitment: KRs are committed unless marked (stretch). Owners listed per KR.*

### Objective IN1: Execs run Monday mornings from our dashboards *(supports C4)*
- **KR IN1.1:** Weekly active leadership viewers of the exec suite 14 → 35 (Looker usage stats). Owner: Halima D.
- **KR IN1.2:** Core dashboard load p95 9s → 3s (Looker performance panel). Owner: Vik M.
- **KR IN1.3:** Driver-app App Store rating 4.1 → 4.6 (App Store Connect). Owner: Vik M.

### Objective IN2: Every product event lands in one trusted schema *(supports C4)*
- **KR IN2.1:** Validate event schema v3 in production — 22 of 22 v3 event types passing conformance checks (0/22 → 22/22, schema CI suite) — after Courier instruments the new driver-app event stream. Owner: Halima D.
- **KR IN2.2:** Product squads onboarded to v3 event conventions 2/9 → 9/9 (onboarding tracker). Owner: TBD.

*Notes: schema v3 validation is sequenced behind Courier's instrumentation of the new event stream; the conformance suite is ready.*

---

## Accounts team (billing & customer success) — Q1 2027
*Source: Confluence page 91128 (ACC-OKR-Q1) · Owner: Georg B. · Last updated 2027-01-08*
*Commitment: KRs are committed unless marked (stretch).*

### Objective AC1 (Priority: P0): New customers reach first value in days, not weeks *(supports C2 — onboarding time-to-value)*
- **KR AC1.1:** Median onboarding time-to-value (signup → first completed delivery) 19 days → 7 days (Mode report "TTV").
- **KR AC1.2:** New paid accounts completing guided setup within 14 days: 54% → 80% of all new paid accounts created in the quarter (Onboarding tracker).

### Objective AC2 (Priority: P0): Support answers arrive before customers ask twice *(supports C2 — escalation backlog)*
- **KR AC2.1:** Open escalation backlog 210 → 60 tickets (Zendesk view "Escalations — Open").
- **KR AC2.2:** Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline).

### Objective AC3 (Priority: P0): Customers trust the delivery promises we report *(supports C2)*
- **KR AC3.1:** On-time delivery rate — deliveries scanned at the destination inside the promised window as a share of all scheduled deliveries including cancellations, monthly, from the Billing warehouse — 78% → 85%.
- **KR AC3.2:** Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM) *(stretch — only if the billing migration lands early)*.

### Objective AC4 (Priority: P0): Billing runs itself *(supports C1)*
- **KR AC4.1:** Invoices requiring manual correction 4.2% → 1.5% of invoices issued monthly (Billing QA dashboard).
- **KR AC4.2:** Billing-system migration covering 38% → 100% of the 6,400 self-serve accounts (migration tracker).

*Notes: every one of these is P0 for us this quarter — we're not choosing. Portal timing depends on how fast the billing migration goes (see AC3.2).*

---

## Appendix — Q4 2026 business review (extracts)
*Source: Confluence page 91031 (Q4-REVIEW) · Last updated 2026-12-15*

- Customer health: "Customer CSAT ended Q4 2026 at 78 (quarterly relationship survey, n = 412)."
- Driver app: "Driver-app weekly retention averaged 71% across Q4 (Amplitude)."
- Reliability: "Sev-1 incidents in Q4: 9 (incident review)."
