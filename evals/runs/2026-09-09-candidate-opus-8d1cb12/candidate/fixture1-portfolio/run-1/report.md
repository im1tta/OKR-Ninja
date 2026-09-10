# Brightledger — Q3 2026 OKR Portfolio Review

*Mode: portfolio (4 teams in scope: Payments, Growth, Platform, Data) · Period: Q3 2026 · Source: `sample-portfolio.md` · Strategy source: "Company Q3 2026 priorities" (Confluence page 88101 / CO-PRIO-Q3)*

## 1. Executive summary

**Verdict: At risk.** 4 teams reviewed; 5 Critical, 8 Major, 1 Minor findings.
The portfolio's biggest threat is AL-10 Strategy coverage gap: company priority C4 ("invoice-financing pilot live with 3 design partners by Sep 30.") has zero coverage in any of the four teams' OKRs — a dated company commitment with nobody working on it.
Two further Critical alignment risks sit inside the checkout funnel: Growth's Aug 15 self-serve upgrade date depends on a billing API that Payments does not GA until Sep 26 (AL-06 Timeline mismatch), and Payments' step-up-verification push works directly against Growth's checkout-conversion target (AL-02 Conflicting metrics / adversarial incentives).
Platform is the most over-subscribed node: its own page declares Q3 fully committed while Payments and Data both assume Platform work (AL-07 Resource contention).
The most common quality issue is AP-04 KR Without Baseline (3 instances across Growth, Platform, and Data), and two KRs — Platform's developer-satisfaction score and Data's "data quality" KR — cannot be measured at all (AP-09 Metric Nobody Can Measure).
Recommended first action: name an owner and a team for company priority C4 this week, before the Sep 30 date makes the pilot unreachable.

## 2. Portfolio heatmap

| Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| Data | 2 | 3 | 3 | 1 | 1 | 2 | 2 | 3 | 1 | 2 | 3 |
| Growth | 4 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 2 |
| Payments | 4 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 3 | 3 |

Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).

Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform C (2.15) · Data C (2.25) · Growth C (2.59) · Payments B (3.12).

- Platform: K5=2 — "developer satisfaction score" names no instrument anywhere in the corpus (AP-09).
- Data: K1=1 — "Significantly improve data quality" states no metric, baseline, or target (AP-09).
- Growth: K1=2 — three KRs state a target with no baseline (AP-04).
- Payments: K1=2 — "Ship checkout & billing API v2 to GA" has nothing countable (AP-01).

## 3. Per-team goodness findings

### [Critical] AP-09 Metric Nobody Can Measure — Platform
- Evidence: "Improve internal developer satisfaction score to 8/10." (`sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 59)
- Also: AP-04 KR Without Baseline · AP-12 Orphan KR
- Why it's a problem: no survey, instrument, or dashboard for a "developer satisfaction score" exists anywhere in the searched corpus (all four team pages, the company priorities page, and the Q2 business-review appendix), so the 8/10 can never be honestly scored; the KR also states no current value, and its success would not move an objective about uptime and cost.
- Scores affected: K5=0, K1=1, K3=2, K2=2, K7=2 (PL1 set)
- Suggested rewrite: "KR PL1.3: Quarterly engineering survey (n ≥ `<respondents>`, run on `<named survey tool>`): developer satisfaction `<baseline>`/10 → 8/10." — and move it under a developer-experience objective rather than "Keep the lights on, cheaper". [proposal — placeholder target]

### [Major] AP-06 Sandbagged Target — Platform
- Evidence: "Maintain API uptime at or above 99.9%." (`sample-portfolio.md` › Objective PL1: Keep the lights on, cheaper › line 57)
- Evidence (prior actual, same corpus): "API uptime, trailing 90 days: 99.95% (Datadog SLO monitor)." (`sample-portfolio.md` › Appendix — Q2 2026 business review (extracts) › line 89)
- Also: AP-10 BAU Dressed as OKR
- Why it's a problem: the target sits below the trailing-90-day actual the same document reports, so the KR is achieved by changing nothing; "Maintain" also presents a standing operational duty as a quarterly goal, displacing a real reliability commitment.
- Scores affected: K3=1, K6=2 (PL1 set)
- Suggested rewrite: "KR PL1.1: API uptime 99.95% (Q2 trailing-90-day actual, Datadog SLO monitor) → 99.98%, measured monthly; error-budget burn ≤ `<budget>`% per month." [proposal — placeholder target]

### [Major] AP-02 Binary KR with No Gradient — Platform
- Evidence: "Complete the SOC 2 Type II audit." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 63)
- Also: AP-01 Task Masquerading as KR
- Why it's a problem: the KR can only score 0% or 100%, so it gives no mid-quarter steering signal on a commitment the company has declared ("complete SOC 2 Type II and hold enterprise-grade reliability.", `sample-portfolio.md` › Company Q3 2026 priorities › line 11); as written it also measures completing a piece of work rather than any result.
- Scores affected: K1=0, K2=1, K6=2 (PL2 set)
- Suggested rewrite: "KR PL2.2: Close 100% of the `<N>` open SOC 2 Type II evidence requests (baseline: `<M>`/`<N>` closed), auditor's report received by `<date>`." [proposal — placeholder target]

### [Critical] AP-09 Metric Nobody Can Measure — Data
- Evidence: "Significantly improve data quality across core tables." (`sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 76)
- Why it's a problem: "data quality" names no score, no formula, and no system of record — a search of all four team pages, the company priorities page, and the Q2 business-review appendix found no data-quality instrument — and "Significantly" supplies no magnitude, so the KR can never be honestly scored or falsified.
- Scores affected: K1=0, K5=0, K3=2, K2=2
- Suggested rewrite: "KR D1.3: Core-table data-quality pass rate (rows failing the `<named test suite>` freshness/null/uniqueness checks, weekly, from `<dashboard>`): `<baseline>`% → `<target>`%." [proposal — placeholder target]

### [Major] AP-03 Vanity Metric — Growth
- Evidence: "Reach 50,000 monthly blog pageviews." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 46)
- Also: AP-04 KR Without Baseline
- Why it's a problem: pageviews rise with publishing volume and paid spend without indicating that the funnel converts anyone, and with no starting value stated (none appears anywhere in the corpus) neither the ambition nor the progress of the 50,000 can be judged.
- Scores affected: K2=2, K1=2, K3=2, K7=2 (G2 set)
- Suggested rewrite: "KR G2.3 (aspirational): Blog-sourced qualified signups `<baseline>`/mo → `<target>`/mo, attributed in `<analytics system>`." [proposal — placeholder target]

### [Major] AP-04 KR Without Baseline — Growth
- Evidence: "Increase trial-to-paid conversion to 22%." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 39)
- Why it's a problem: no current trial-to-paid value is stated in the KR and none appears anywhere in the corpus (searched Growth's page, the company priorities page, and the Q2 business-review appendix, which reports signups but not conversion), so 22% could be a stretch or already achieved and nobody can tell which.
- Scores affected: K1=2, K3=2
- Suggested rewrite: "KR G1.1: Trial-to-paid conversion `<baseline>`% (Q2 actual, per `<funnel dashboard>`) → 22%, measured on trials started in the quarter." [proposal — placeholder target]

### [Major] AP-01 Task Masquerading as KR — Payments
- Evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Why it's a problem: shipping to GA is a deliverable with a date, not a result — the KR succeeds in full even if no traffic, no partner team, and no customer ever uses API v2, and its only failure mode is lateness.
- Scores affected: K1=0, K2=1, K7=3 (P1 set)
- Suggested rewrite: "KR P1.2: `<target>`% of checkout and billing calls served by API v2 by `<date>` (baseline 0%), with v2 error rate ≤ `<threshold>`% and Growth's self-serve upgrade flow live on it." [proposal — placeholder target]

## 4. Alignment findings

### [Critical] AL-10 Strategy coverage gap: Company priorities ↔ Payments / Growth / Platform / Data
- Company evidence: "invoice-financing pilot live with 3 design partners by Sep 30." (`sample-portfolio.md` › Company Q3 2026 priorities › line 13)
- Portfolio evidence (near-miss — the only related hit in any team section): "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40) — this is invoice *sending* inside onboarding activation, not invoice *financing*, and it serves self-serve growth, so it is not coverage of C4.
- Conflict: C4 is a dated company priority with a hard Sep 30 date and no contributing objective, KR, or note in any of the four teams' OKRs — the portfolio has a hole where a launch is supposed to be.
- Detection check that fired: AL-10 top-down strategy trace — for each company objective, search all teams' OKRs for coverage; C4 returned zero contributing children.
- Disconfirming checks run: re-searched all four team sections (lines 17–83) under synonyms and program names — terms searched (unquoted, case-insensitive): capital → 0 hits, financ → 0 hits, design partner → 0 hits, pilot → 0 hits, lending → 0 hits, underwrit → 0 hits, Sep 30 → 0 hits, invoice → 1 hit (the Growth activation definition quoted above, distinguished as a near-miss); checked C4's own line and page for an owner assigned to a function outside the swept team set — none is named, the priorities page lists only "Owner: Dana W. (CEO)" for the page as a whole.
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 13 and 40)
- Recommended resolution owner: Dana W. (CEO) to assign C4 to a named team with a contributing objective, or formally drop it from the Q3 priorities, within 1 week — the Sep 30 date leaves no room to decide later.

### [Critical] AL-06 Timeline mismatch: Growth ↔ Payments
- Growth evidence: "Launch self-serve plan upgrades by Aug 15 and drive 300 upgrades through the new flow this quarter." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 41), with the dependency stated as "self-serve upgrades (G1.3) will use the new billing API — Marcus synced with Priya in June, should be fine." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 48)
- Payments evidence: "Ship checkout & billing API v2 to GA by Sep 26." (`sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 23)
- Conflict: Growth's committed launch date for the flow that consumes the new billing API is Aug 15, six weeks *before* the producer's own GA date of Sep 26 — the consumer ships before its dependency exists, and the quarter ends four days after GA, leaving no margin for the 300 upgrades either.
- Detection check that fired: AL-06 dependency-map date comparison — producer's delivery date (Sep 26) versus consumer's need-by date (Aug 15) on the Growth → Payments edge; hard inversion.
- Disconfirming checks run: the AL-06 control *late date is not necessarily an inversion* — searched the whole file for an earlier consumable milestone of the billing API (terms: beta, preview, early access, sandbox): 0 hits, so no pre-GA milestone is quotable that Growth could integrate against; commitment levels checked on both sides — both pages state "Commitment: KRs are committed unless marked (aspirational)." (lines 36 and 19) and neither KR carries an aspirational label, so both are committed; checked Growth's note for a hedge that would downgrade the finding — "should be fine" records confidence, not a discounted plan or an alternative path.
- Inference labels: none — all load-bearing text quoted. (Growth's note names "the new billing API"; P1.2 is the only billing-API deliverable in the corpus.)
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 41, 48 and 23)
- Recommended resolution owner: Priya N. (Payments) and Marcus T. (Growth) to agree before end of July either a dated pre-GA milestone Growth can build on or a revised G1.3 launch date after Sep 26 — and to restate the 300-upgrade target against whichever date survives.

### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
- Payments evidence: "Increase step-up verification coverage to 90% of transactions (from 35%)." (`sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 28)
- Growth evidence: "Raise checkout conversion from 58% to 68% for self-serve signups." (`sample-portfolio.md` › Objective G2: Turn our funnel into a machine › line 44)
- Conflict: step-up verification is a friction control applied at checkout, and Payments plans to take it from 35% to 90% of transactions in the same quarter Growth commits to a 10-point lift in checkout conversion on that same surface; each team's lever predictably degrades the other's number, and neither page mentions the other team.
- Detection check that fired: AL-02 surface-lever blocking key (2) — both KRs sit on the checkout surface, step-up verification coverage is a stated friction/risk control there, and Growth targets that surface's conversion metric. (Metric-identity key (1) generated nothing between them — no shared canonical metric.)
- Disconfirming checks run: shared or parent OKR covering both — none found (searched both team sections and the company priorities page; the two objectives trace to different priorities, C3 and C1); documented split of levers — none found (no text on either page assigns checkout-friction ownership or exempts self-serve signups from step-up); directionality — confirmed opposed at the mechanism level. Separately, the lookalike pair "Raise checkout success rate from 91.2% to 95% for card transactions." (`sample-portfolio.md` › Objective P1: Make checkout something customers never think about › line 22) against the same Growth KR was generated and **killed**: different definitions and populations (card-transaction authorization success vs self-serve signup checkout conversion), same direction, and no control lever on either side — that kill does not touch this candidate.
- Inference labels: the step-up-verification → checkout-conversion mechanism is **analyst inference** — no Brightledger document in the corpus states the tradeoff.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 28 and 44)
- Recommended resolution owner: VP Product to convene Priya N. and Marcus T. within 2 weeks and agree a guardrail pair — a risk-based step-up policy with a stated conversion floor (`<conversion floor>`%) and a chargeback ceiling (`<chargeback ceiling>`%) — instead of two independently committed numbers. [proposal — placeholder target]
- Severity note: AL-02 rates mechanism-level conflicts Major; escalated one level to Critical because both KRs are committed under their pages' stated convention ("Commitment: KRs are committed unless marked (aspirational).", lines 19 and 36) and the fraud side is exec-visible after the Q2 incident.

### [Major] AL-07 Resource contention: Payments + Data ↔ Platform
- Payments evidence (claimant 1): "API v2 GA depends on the new PCI-scoped infra — assuming Platform provisions this in July as discussed in standup." (`sample-portfolio.md` › Objective P2: Cut fraud losses without drama › line 30)
- Data evidence (claimant 2): "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82)
- Platform evidence (resource owner's capacity statement): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65)
- Conflict: two teams' committed KRs assume Platform capacity in Q3 — PCI-scoped infra provisioning in July and the streaming pipeline migration — while Platform's own page declares that quarter fully committed to two other workstreams and is holding infra requests to Q4; nobody has done the arithmetic, and both claimants recorded their assumption in a note rather than in an agreement.
- Detection check that fired: AL-07 resource-node fan-in — grouped every shared-resource mention by owner, found two distinct claimants on Platform in the same quarter, then checked the owner's page for declared supply and found the fully-committed statement. Classified at the resource node, not edge-by-edge: Payments' ask is provisioning (the owner's capacity itself) and so folds into this aggregate entirely; Data's edge additionally names a distinct deliverable and is filed separately below as AL-01, cross-referencing this finding. The capacity arithmetic is reported here once and nowhere else.
- Disconfirming checks run: the AL-07 control *plural demand is not necessarily contention* — searched Platform's section (lines 52–66) for an allocation covering either claimant; terms searched: stream → 0 hits, pipeline → 0 hits, schema → 0 hits, event → 0 hits, migrat → 0 hits, data → 0 hits, PCI → 0 hits, provision → 0 hits, enclave → 0 hits, and no capacity or allocation table is linked from the page; no Jira or backlog source exists in this corpus, so no scheduled-epic allocation could be found to falsify the finding and that limit is stated rather than assumed away; confirmed both claims fall in the same quarter (Q3 2026, per all four page headings) and name the same resource owner.
- Inference labels: Data's phrase "the infra level" is resolved to the Platform team by **analyst inference** — Platform is the only infrastructure-owning team in the confirmed scope, but Data's text never names it.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 30, 82 and 65)
- Recommended resolution owner: Elena R. (Platform) to publish a Q3 capacity allocation naming what she will and will not do for Payments and Data, and to take the resulting descope decision to Dana W. before end of July.

### [Major] AL-01 Unacknowledged dependency: Data ↔ Platform
- Data evidence: "schema v2 rollout rides on the streaming pipeline migration; we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 82), supporting the committed KR "Migrate 100% of product events to unified event schema v2." (`sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 74)
- Platform evidence (closest partial match on the producer's side): "Q3 is fully committed between SOC 2 evidence collection and the cost work. Holding all non-critical infra requests until Q4." (`sample-portfolio.md` › Objective PL2: Earn enterprise trust › line 65) — a general hold, not an acknowledgment: it never mentions the streaming pipeline, and neither Platform objective nor any of its five KRs does either.
- Conflict: the streaming pipeline migration is a distinct deliverable Platform would have to plan and staff as its own project, Data has explicitly excluded it from its own 3-engineer-month scope, and it appears nowhere in Platform's OKRs — so a committed 100% Data KR rests on work no team has committed to doing. Cross-reference: this edge also lands on the over-subscribed Platform node reported once above as AL-07 Resource contention; the capacity arithmetic is not repeated here.
- Detection check that fired: AL-01 dependency-edge acknowledgment — extracted "rides on" as an external-work phrase, resolved "the infra level" to Platform, searched the producer's OKRs for the deliverable, and found no hit.
- Disconfirming checks run: the AL-01 control *a missing mention is not necessarily an unacknowledged dependency* — searched Platform's whole section (lines 52–66) for the deliverable; terms searched: stream, pipeline, schema, event, warehouse, migrat, data — 0 hits for each; no Jira or backlog source exists in this corpus, so no scheduled-but-unwritten epic could be produced to downgrade the finding; quoted Platform's closest partial match above and explained why it does not cover the need. Not escalated to Critical: the Q4 hold is a general statement about "non-critical infra requests" and never deprioritizes this area by name.
- Inference labels: the resolution of "the infra level" to the Platform team is **analyst inference** — Data's text names no team.
- Verdict: CONFIRMED (all three quotes re-verified character-for-character against lines 82, 74 and 65)
- Recommended resolution owner: Jonas K. (Data) and Elena R. (Platform) to decide before end of July whether Platform commits the pipeline migration as a Q3 KR or Data rescopes D1.1 to the events the current pipeline already supports.

### [Major] AL-03 Duplicated / overlapping objectives: Growth ↔ Data
- Growth evidence: "Lift new-user activation rate (first invoice sent within 7 days) from 31% to 40%." (`sample-portfolio.md` › Objective G1: Make the first week with Brightledger magical › line 40)
- Data evidence: "Lift new-user activation rate to 35% via onboarding experiments." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 80)
- Conflict: both teams commit to lifting the same named metric on the same population in the same quarter, to two different numbers (40% and 35%), with two separate onboarding workstreams — Growth's self-serve flow work and Data's "Ship personalized onboarding checklists to 100% of new signups." (`sample-portfolio.md` › Objective D2: Own onboarding personalization end-to-end › line 79) — and neither page references the other team or divides the surface. If both land, nobody can say who moved the number or which target was the commitment.
- Detection check that fired: AL-03 clustering by target metric + target population — "new-user activation rate" for new signups appears in two teams' KRs; the cluster then failed every division-of-labor check.
- Disconfirming checks run: the AL-03 control *similar objectives are not necessarily duplication* — searched Growth's section (lines 34–49) for any reference to Data (terms: data, Jonas, D2): 0 hits, and Data's section (lines 69–83) for any reference to Growth (terms: growth, Marcus, G1): 0 hits; searched both for an explicit lane split (mobile/web, segment, geography) — none stated; checked for a shared parent objective assigning lanes — none, as neither objective states a parent at all; confirmed the populations are the same ("new-user" / "new signups") rather than legitimately different segments.
- Inference labels: none — all load-bearing text quoted. Secondary cross-reference: AL-08 Terminology collision also applies — Growth defines activation as "first invoice sent within 7 days" (line 40) while Data's KR carries no definition at all — reported here as the secondary ID rather than as its own finding, because the duplication is the root cause and the definitional gap corrupts the same comparison.
- Verdict: CONFIRMED (both quotes re-verified character-for-character against lines 40 and 80)
- Recommended resolution owner: Marcus T. (Growth) to convene Jonas K. (Data) within 2 weeks: agree one owner, one activation definition (Growth's 7-day first-invoice formula is the only one written down), and one target, with the other team's KR restated as a contributing driver.

### [Minor] AL-04 Orphan objective: Data ↔ Company priorities
- Data evidence: "Objective D1: One trustworthy source of truth" (`sample-portfolio.md` › Objective D1: One trustworthy source of truth › line 73), whose KRs are "Migrate 100% of product events to unified event schema v2." (line 74), "Cut critical-dashboard data latency from 6h to 1h." (line 75), and "Significantly improve data quality across core tables." (line 76)
- Company evidence: the full Q3 priority list — "mid-market self-serve ARR from $8.4M to $11M run-rate by end of Q3." / "complete SOC 2 Type II and hold enterprise-grade reliability." / "bring chargeback rate under 0.5% after the Q2 incident." / "invoice-financing pilot live with 3 design partners by Sep 30." (`sample-portfolio.md` › Company Q3 2026 priorities › lines 10–13)
- Conflict: D1 claims no parent, none of its three KR metrics is a company-level metric or a documented driver of one, and no company priority mentions data, schema, dashboards, or data quality — so half the Data team's quarter serves nothing the company has said it is trying to do.
- Detection check that fired: AL-04 three-way check on the strategy trace — (a) explicit parent link: absent from D1's text and Data's notes; (b) KR metric that is a company metric or documented driver: none of schema-migration completeness, dashboard latency, or data quality appears in C1–C4; (c) mention in a strategy page: none. Zero of three.
- Disconfirming checks run: the AL-04 control *no parent link is not necessarily an orphan* — ran the full three-way check above before flagging rather than inferring a parent; searched Data's own page for a self-justification that could downgrade or kill the finding and found only "we've sized our part at 3 engineer-months and expect the pipeline itself to be handled at the infra level." (line 82), which states scope, not strategic rationale; checked for an exploratory-work charter for the Data team — none stated in the corpus. Held at Minor because no fraction of team capacity is claimed for D1 (3 engineer-months is an absolute sizing, not a stated share of the team).
- Inference labels: none — all load-bearing text quoted.
- Verdict: CONFIRMED (all quotes re-verified character-for-character against lines 73–76 and 10–13)
- Recommended resolution owner: Jonas K. (Data) with Dana W. (CEO) to either state D1's parent priority explicitly on the OKR page or re-cut the objective around the driver it actually serves, before the mid-quarter check-in.

## 5. Prioritized action list

1. Assign company priority C4 to a named team with a contributing objective, or drop it from the Q3 list — owner: Dana W. (CEO) (resolves §4 AL-10 Strategy coverage gap).
2. Resequence Growth's Aug 15 upgrade launch against Payments' Sep 26 GA, or publish a dated pre-GA milestone Growth can integrate on — owner: Priya N. (Payments) with Marcus T. (Growth) (resolves §4 AL-06 Timeline mismatch).
3. Convene Payments and Growth to replace the two independent checkout numbers with a guardrail pair (conversion floor + chargeback ceiling) — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
4. Rewrite Platform's developer-satisfaction KR against a named survey instrument with a stated baseline, or drop it from PL1 — owner: Elena R. (Platform) (resolves §3 AP-09 Metric Nobody Can Measure — Platform).
5. Replace Data's "data quality" KR with a defined pass rate on a named test suite and dashboard — owner: Jonas K. (Data) (resolves §3 AP-09 Metric Nobody Can Measure — Data).
6. Publish a Q3 Platform capacity allocation stating what Payments and Data will and will not get, and escalate the resulting descope — owner: Elena R. (Platform) (resolves §4 AL-07 Resource contention).
7. Decide whether Platform commits the streaming pipeline migration as a Q3 KR or Data rescopes D1.1 — owner: Elena R. (Platform) with Jonas K. (Data) (resolves §4 AL-01 Unacknowledged dependency).
8. Agree a single owner, definition, and target for new-user activation rate across Growth and Data — owner: Marcus T. (Growth) (resolves §4 AL-03 Duplicated / overlapping objectives).
9. Restate Platform's uptime KR against the quoted 99.95% trailing baseline — owner: Elena R. (Platform) (resolves §3 AP-06 Sandbagged Target).
10. Rewrite the four remaining Major goodness defects into measurable form — Payments P1.2, Growth G1.1 and G2.3, Platform PL2.2 — owner: each team's OKR page owner, by the mid-quarter check-in (resolves §3 AP-01 Task Masquerading as KR, AP-04 KR Without Baseline, AP-03 Vanity Metric, AP-02 Binary KR with No Gradient).

## 6. Suggested single-team re-runs

All four teams qualify — Platform and Data on Critical goodness findings, Payments and Growth on Critical alignment findings — listed worst roll-up grade first.

- **Platform** (roll-up C (2.15); Critical AP-09 Metric Nobody Can Measure, plus AL-07 Resource contention and inbound AL-01 Unacknowledged dependency): re-run single-team mode — "Review the Platform team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Platform team — Q3 2026' (Confluence page 88221, PLAT-OKR-Q3, owner Elena R.); strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Data** (roll-up C (2.25); Critical AP-09 Metric Nobody Can Measure, plus AL-01 Unacknowledged dependency, AL-03 Duplicated / overlapping objectives, AL-04 Orphan objective): re-run single-team mode — "Review the Data team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Data team — Q3 2026' (Confluence page 88225, DATA-OKR-Q3, owner Jonas K.); strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Growth** (roll-up C (2.59); Critical AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Growth team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Growth team — Q3 2026' (Confluence page 88217, GRW-OKR-Q3, owner Marcus T.); strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."
- **Payments** (roll-up B (3.12), above the needs-rework threshold, but qualifies on Critical AL-02 Conflicting metrics / adversarial incentives and AL-06 Timeline mismatch): re-run single-team mode — "Review the Payments team's Q3 2026 OKRs alone, in depth. Source: `sample-portfolio.md`, section 'Payments team — Q3 2026' (Confluence page 88213, PAY-OKR-Q3, owner Priya N.); strategy doc: 'Company Q3 2026 priorities' (Confluence page 88101, CO-PRIO-Q3) in the same file."

Company priority C4 (§4 AL-10) has no team to re-run against — it needs an owner assigned before any team-level review can cover it.
