# Coppervale — Q1 2027 OKRs (portfolio export)

> **Fictional test fixture #2.** Coppervale is an invented B2B field-service & delivery-operations SaaS (~300 employees). All teams, people, numbers, and page IDs below are fictional. This file mimics a Confluence export of a company priorities page, five teams' OKR pages, and a Q4 business-review extract, and deliberately contains planted defects — see the answer key at the bottom. It complements `examples/sample-portfolio.md` (fixture 1): its answer key covers the catalog modes fixture 1 leaves uncovered.

---

## Company Q1 2027 priorities
*Source: Confluence page 91050 (CO-PRIO-Q1FY27) · Owner: Noor E. (CEO) · Last updated 2026-12-18*

- **C1 — Win mid-market logistics:** grow ARR from $14M to $17.5M run-rate by end of Q1, led by enterprise dispatch adoption and frictionless self-serve billing.
- **C2 — Keep enterprise customers for life:** reduce enterprise logo churn from 8% to 5% across FY27, driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers.
- **C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80% across FY27, driven by in-app reliability and by driver-to-driver referral growth — our FY26 cohort review found drivers who join through a referral retain far better than drivers we acquire through paid channels.
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
- **KR AC3.2:** Partner portal live for the first 40 partner accounts, 0 → 40 (Partner CRM), giving those partners the same on-time delivery reporting AC3.1 measures *(stretch — only if the billing migration lands early)*.

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

---
---

## Answer key (planted defects)

**Thirteen planted defects: G1–G8 (goodness) and A1–A5 (alignment).** Every row cites its canonical ID and name from `references/goodness-rubric.md` (AP-XX) or `references/alignment-taxonomy.md` (AL-XX). Locations reference the sections above; a compliant report quotes the exact objective/KR text with a source ref (format in `references/report-format.md`).

### Goodness defects

| # | ID · Anti-pattern | Location | What's wrong |
|---|---|---|---|
| G1 | AP-05 · Everything Is a P0 | Accounts, all four objectives | AC1–AC4 uniformly labeled "Priority: P0", reinforced by the notes ("every one of these is P0 for us this quarter — we're not choosing") — the set encodes no trade-off. |
| G2 | AP-07 · Unmoored Moonshot | Courier KR CR2.1 | "Driver referral installs 3,000 → 45,000 this quarter" is a 15x stretch with no mechanism, intermediate milestone, or resourcing signal anywhere on the page ("big swing" states no how). |
| G3 | AP-08 · Committed vs Aspirational Not Labeled | Courier page (set level) | Courier is the only page with no commitment-convention line and no labels, while targets vary wildly in stretch (crash-free 99.2% → 99.6% beside the 15x CR2.1). Counted separately from G2: G2 is the KR-level defect, G3 the set-level labeling defect. |
| G4 | AP-10 · BAU Dressed as OKR | Core Systems Objective CS1 | "Continue running the platform smoothly for every team" is a standing operational duty framed as a goal — achieved by default staffing. |
| G5 | AP-11 · Objective as Kitchen Sink | Dispatch Objective DS1 | "Delight enterprise dispatchers and expand Coppervale into two new regions" joins two unrelated end-states with disjoint audiences; its KRs (dispatcher NPS vs DE/FR pilots) cluster into unrelated groups. |
| G6 | AP-12 · Orphan KR | Insights KR IN1.3 | "Driver-app App Store rating 4.1 → 4.6" has no causal chain to "Execs run Monday mornings from our dashboards" and shares no nouns or domain with it. |
| G7 | AP-13 · Ambiguous Denominator | Dispatch KR DS2.4 | "Reduce the failure rate from 6% to 3%" never defines the population — failures of delivery attempts, unique shipments, route plans, or something else — and nothing on the page disambiguates; any number can be claimed. |
| G8 | AP-15 · Ownerless KR | Insights KR IN2.2 | The page's own convention assigns per-KR owners, and this KR's reads "Owner: TBD" — no accountable individual, and none derivable for it elsewhere in the corpus. |

### Alignment defects

| # | ID · Failure mode | Location(s) | What's wrong |
|---|---|---|---|
| A1 | AL-05 · Cascade drift | Core Systems Objective CS2 ↔ Company C2 | CS2 explicitly claims "supports C2 — enterprise churn", but its KRs (deploy frequency, change-failure rate, CI time) measure neither churn nor any workstream C2 names (onboarding time-to-value, escalation backlog, delivery-promise reporting) — the link is decorative; all three KRs could land in a quarter where churn worsens. |
| A2 | AL-08 · Terminology collision | Dispatch KR DS2.1 ↔ Accounts KR AC3.1 | Both teams carry KRs on "On-time delivery rate" under materially different definitions — completed-within-window / completed jobs, weekly, Ops Console vs scanned-at-destination / all scheduled deliveries including cancellations, monthly, Billing warehouse. Same name, different measurement. |
| A3 | AL-09 · Baseline disagreement | Accounts KR AC2.2 ↔ Appendix (Q4 review) | Accounts states "Customer CSAT 86 → 90 (quarterly relationship survey; Q4 2026 baseline)" while the Q4 review states "Customer CSAT ended Q4 2026 at 78" from the same survey and period — an eight-point discrepancy with no definitional split findable, so the +4 target may be a +12 ask. |
| A4 | AL-11 · Circular dependency | Courier KR CR3.1 → Core Systems KR CS3.1 → Insights KR IN2.1 → Courier | Courier instruments "once Core Systems GAs the SDK"; Core GAs "after Insights validates event schema v3 in production"; Insights validates "after Courier instruments the new driver-app event stream". Three teams, each first in line behind another — no valid execution order as written; every edge is quotable. |
| A5 | AL-12 · Commitment asymmetry | Dispatch KR DS2.2 ↔ Accounts KR AC3.2 | Dispatch's committed "600 enterprise trial starts via the partner portal launch" depends on the portal that Accounts lists as "(stretch — only if the billing migration lands early)" — a committed number built on an explicitly-maybe deliverable. |

### Intentional non-defects (do not report)

Near-misses planted to measure false-positive discipline. Reporting one of these counts against the extra-findings budget in the eval criterion.

1. **Courier KR CR2.1 is G2 (AP-07) only** — quarterly attributed installs are not a cumulative vanity total (not AP-03), and installs are the referral objective CR2's intended outcome (not AP-12).
2. **Dispatch KR DS2.1 vs Accounts KR AC3.1 baselines (91% vs 78%)**: the gap is fully explained by the A2 definitional split — not AL-09; report the collision once, as AL-08.
3. **Dispatch KR DS2.4**: the baseline is present (6%) so not AP-04, and a source exists ("ops weekly report") so not AP-09 — the defect is the undefined denominator (AP-13, G7).
4. **Accounts KR AC3.2** (partner portal 0 → 40): a zero-baseline launch that is explicitly labeled stretch and gated on a named mechanism (the billing migration) — not AP-07; its stretch label is load-bearing evidence for A5.
5. **The A4 cycle edges are not AL-01 and not AL-06**: each depended-on deliverable appears in its producer's own OKRs (SDK in CS3.1, validation in IN2.1, instrumentation in CR3.1), and no edge carries a date to invert.
6. **Courier KR CR1.2 (retention to 78%) vs Company C3 (to 80%)**: consistent — the KR states it is the "Q1 step toward the FY27 80% goal in C3", not a conflicting target.
7. **Accounts KR AC4.2** (billing migration 38% → 100%): bounded completion of an in-flight migration with a countable coverage denominator — neither AP-07 (not open-ended growth) nor AP-01/AP-14 (not a dateline milestone).
8. **The A4 cycle edges are not reported as AL-12**: Courier's page states no labeling scheme at all, and the taxonomy's own disconfirming check applies — a team that labels nothing has not implicitly marked everything aspirational. The scheme's absence is already reported as G3 (AP-08); per the taxonomy's one-finding-one-failure-mode rule, reporting the same absence again as per-edge label ambiguity double-counts one root cause.
9. **Courier Objective CR2 (supports C3) vs Company C3**: CR2's only KR measures referral installs, but C3 names driver-to-driver referral growth as a documented driver of driver-app weekly retention — so AL-05's mechanism check passes on its second branch (child KRs measure "a documented driver of" the parent metric) and the parent link is not decorative. The near-miss is real and the reading is wrong: report AL-05 once, at A1 (CS2 ↔ C2), where the child's KRs measure neither the parent metric nor any workstream C2 names.

### Triage entries

Recurring findings beyond the key, each classified once so the same debate is not re-had. A **known-red** entry is reported by the grader but excluded from the extra-findings budget until its fix lands; a **fixed** entry no longer affects counting.

1. **T1 · AP-12 on KR AC3.2** — bucket: fixture-ambiguous · status: fixed · decision: Fixed by change fix-fixture1-precision-extras (2026-09-10, scope widened to fixture 2 with the owner's approval): "Partner portal live for the first 40 partner accounts, 0 → 40" stated no causal chain to its objective, "Customers trust the delivery promises we report", so AP-12 Orphan KR was a defensible reading the key never planted — the same unplanted-true-defect class this change fixed on fixture 1. AC3.2 now names the delivery reporting it gives those partners, which is the objective's own subject. Everything the key depends on is preserved: the portal, 0 → 40, the stretch label and the billing-migration gate, all load-bearing for row A5 (AL-12) and non-defect N4 (AP-07). Not planted as a defect row: it appeared in 3 runs of 5, and a key row must be found in every run. · rationale: Extra in 3 of 5 runs of 2026-09-10-candidate-repair1, where it was the finding that pushed one run to 3 counted findings against a budget of 2. Absent from the pre-change batches, but no valid comparison to them exists — the harness refuses it because those arms ran on claude-opus-5 and this one on claude-opus-5[1m] — so it is triaged on its merits rather than attributed to any change.
2. **T2 · AL-05 on Objective CR2** — bucket: fixture-ambiguous · status: fixed · decision: Fixed by change fix-fixture2-unplanted-cascade-drift (2026-09-11) on the parent's side of the link: Courier Objective CR2 declares "(supports C3)" while its only KR measures referral installs, an acquisition measure that moves no retention rate — the same shape as planted row A1, one page over, and a defensible AL-05 the key never planted. Company priority C3 now names driver-to-driver referral growth as a documented retention driver, alongside in-app reliability, so AL-05's mechanism check passes on its documented-driver branch. The Courier page is left unedited, which is the point: the three levers rejected before all edit it or cost a row — stating the install-to-retention mechanism on the Courier page deletes G2 (AP-07 requires no "how" anywhere on that page); dropping or re-pointing "(supports C3)" leaves CR2 at zero of AL-04's three checks, an off-key finding for this fixture, and no priority C1-C4 is moved by referral installs; adding a companion retention KR under CR2 is AP-07's own published remedy and would read as the missing "how", besides inviting an AL-08 duplicate against CR1.2. Not planted as a defect row: the absolute criterion requires every planted row in every run, and this fires intermittently. Guarded instead by non-defect N9, which is valid only while C3 carries the documented driver its rationale names. · rationale: Extra in 5 of 5 runs of 2026-09-10-candidate-5beed03, 2 of 5 of 2026-09-10-candidate-repair1, 1 of 5 of 2026-09-10-candidate-repair2, 1 of 1 of 2026-09-10-smoke-verify, and 1 of 5 of 2026-09-09-candidate-opus-8d1cb12 — persistent across skill states rather than a flake, and analysed but left in place by 2026-09-10-fix-fixture1-precision-extras (design.md section D5a), whose three rejected levers all edited the child's side of the link.

### Modes deliberately not covered

The fixture plants no instance of **AL-01, AL-02, AL-03, AL-04, AL-06, AL-07, or AL-10** (nor of anti-patterns AP-01, AP-02, AP-03, AP-04, AP-06, AP-09, AP-14) — those are fixture 1's territory (`examples/sample-portfolio.md`). A finding citing any of them is off-key and counts against the extra-findings budget.

### Eval criterion

A passing portfolio review must:

1. surface **all 13 planted defects, cited by canonical ID**, each with correct verbatim quotes and source refs;
2. contain **zero fabricated quotes** — every quoted span must exist character-for-character in this file;
3. raise **no more than 2 findings beyond this key** (the stated budget), with any reported item from the Intentional non-defects list counting against that budget.
