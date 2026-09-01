# Design: add-second-eval-fixture

## Context

See `proposal.md` — Why. Fixture 1 (`examples/sample-portfolio.md`, Brightledger, 4 teams, 14 defects) stays untouched. The hard design problem is planting 13 specific modes densely **without accidentally planting anything else**: every fixture-1-covered mode (AP-01/02/03/04/06/09/14, AL-01/02/03/04/06/07/10) is *off-key* in fixture 2, so an accidental instance burns the 2-finding budget and makes the fixture ungradable.

## Goals / Non-Goals

**Goals:**
- One clean, separable planted defect per uncovered mode; every defect quotable (two-sided where the mode requires it).
- Every non-defect line authored defensively against the full catalog (all 27 modes, not just the 13 planted).

**Non-Goals:**
- No new detection content; no severity redefinitions; the fixture asserts nothing normative — the references stay the only owners of their topics.

## Decisions

### D1 — Universe: Coppervale, Q1 2027

(Applied note: the driver-app team is named **Courier** — the design draft said "Mobile", but that bare word appears in `references/`, failing the name-independence grep.)

Fictional B2B field-service & delivery-operations SaaS (~300 employees), quarter Q1 2027. Distinct from Brightledger (fixture 1) and Meridian/Atlas/Bluefin/Cormorant/Dune/Ember/Foxtrot (taxonomy worked examples) — grep-verifiably absent from `references/` and fixture 1. Five teams: **Dispatch** (routing product), **Courier** (driver app), **Core Systems** (infra), **Insights** (analytics), **Accounts** (billing & customer success). File structure mirrors fixture 1: fictional-fixture banner → company priorities page (C1–C4) → five team pages (source line, owner, commitment-convention line except where AP-08 is planted, objectives/KRs, notes) → appendix (Q4 2026 business-review extracts) → answer key → intentional non-defects → modes deliberately not covered → eval criterion (budget 2).

### D2 — Defect placement map

| # | Mode | Placement | Construction |
|---|---|---|---|
| G1 | AP-05 Everything Is a P0 | Accounts | 4 objectives, each labeled "Priority: P0"; no ranking anywhere. |
| G2 | AP-07 Unmoored Moonshot | Courier KR | Driver referral installs 3k → 45k in-quarter (15x); no mechanism, milestone, or resourcing anywhere on the page. |
| G3 | AP-08 Committed vs Aspirational Not Labeled | Courier (page level) | Courier is the ONLY page omitting the commitment-convention line; targets vary wildly in stretch (crash-free 99.2→99.6 next to the 15x moonshot), zero labels. Key notes AP-07 = KR-level, AP-08 = set-level; counted separately. |
| G4 | AP-10 BAU Dressed as OKR | Core Systems objective | "Continue running the platform smoothly…" — standing duty as objective; its KRs stay measurable with real deltas so nothing else fires. |
| G5 | AP-11 Objective as Kitchen Sink | Dispatch objective | ≥2 "and"-joined unrelated outcomes (enterprise dispatcher experience AND new-region expansion); KRs cluster into unrelated groups, each individually clean. |
| G6 | AP-12 Orphan KR | Insights KR | Objective about execs trusting dashboards; orphan KR "App-store rating 4.1 → 4.6" — measurable outcome (so not AP-01) but zero causal chain / shared nouns with the objective. |
| G7 | AP-13 Ambiguous Denominator | Dispatch KR | "Reduce the failure rate from 6% to 3%" — baseline present (so not AP-04) but the population is undefined with multiple plausible readings (delivery attempts? unique shipments? route legs?) and nothing on the page disambiguates. |
| G8 | AP-15 Ownerless KR | Insights KR | Insights lists per-KR owners; one KR's field reads "Owner: TBD". Other teams use page-header owners only (K4=3 territory, not AP-15). |
| A1 | AL-05 Cascade drift | Core Systems ↔ C2 | C2: enterprise churn 8%→5%, "driven primarily by onboarding time-to-value and escalation backlog." Core objective tagged "supports C2" with KRs (deploy frequency, change-failure rate, CI time) that are coherent with their own objective (no AP-12) but match neither named driver nor the churn metric — the link is decorative. |
| A2 | AL-08 Terminology collision | Dispatch ↔ Accounts | Both pages state inline definitions of "on-time delivery rate" that differ in formula, window, AND population; both carry KRs on it. The baseline gap between them is definitionally explained → non-defects list pins "not AL-09". |
| A3 | AL-09 Baseline disagreement | Accounts ↔ Appendix | Appendix Q4 review: "CSAT ended Q4 2026 at 78 (quarterly relationship survey)"; Accounts KR: "CSAT 86 → 90 (quarterly relationship survey)". Same instrument, same period notation, no definitional split findable → true AL-09, distinct metric from A2's. |
| A4 | AL-11 Circular dependency | Courier → Core Systems → Insights → Courier | Courier instruments driver-app events *once Core GAs telemetry SDK v1*; Core GAs the SDK *after Insights validates event schema v3 in production*; Insights validates v3 *after Courier instruments the new event stream*. Each edge verbatim on the consumer's page; each deliverable appears in its producer's own OKRs (so no AL-01); edges are condition-based with no dates (so no AL-06). |
| A5 | AL-12 Commitment asymmetry | Dispatch ↔ Accounts | Dispatch committed KR: 600 enterprise trials via the partner portal launch. Accounts lists the portal KR "(stretch — only if the billing migration lands early)". Dependency acknowledged on both sides (not AL-01), undated (not AL-06). |

### D3 — Anti-collision rules (authoring discipline)

1. **Every clean KR is fully armored:** inline metric + numeric baseline → target + unit/window + named source system, target above baseline and safely below the catalog's >5x moonshot bar (largest clean finite ratio ≤4x, counting cuts by factor as fixture 1's non-defect #1 does; bounded completion-to-full-coverage KRs of the form x/N → N/N over a fixed denominator sit outside the ratio inventory — completing a fixed set cannot read as open-ended growth — but stay under 5x or get pinned), owner resolvable, in-quarter. That simultaneously blocks AP-01/02/03/04/06/07/13/14 and K-dimension noise. (Applied note: relaxed from an over-strict "below 2x" draft during verify-repair — fixture 1's own clean KRs exceed 2x; the ≤4x line is the enforced bound.)
2. **All cross-team mentions are acknowledged by the producer's own OKRs** (blocks AL-01), **undated on dependency edges** (blocks AL-06), and **name no shared pod/specialist/environment** (blocks AL-07).
3. **Every objective traces to a C-priority** via an explicit "supports Cx" tag or one-step metric link (blocks AL-04), and **every C1–C4 has real team coverage** — including both named C2 drivers, covered by Accounts objectives (blocks AL-10 while sharpening A1).
4. **No metric other than "on-time delivery rate" appears in two teams' KRs; no baseline for one metric appears in two places except the planted CSAT pair** (blocks AL-02/AL-03 and keeps A2/A3 unique).
5. Where a planted mode intrinsically resembles an off-key one (AL-08 vs AL-09; AP-13 vs AP-04), the near-miss is pinned in the intentional non-defects list — the list is a false-positive test, mirroring fixture 1's.

### D4 — Answer key conventions

Same table format and ID conventions as fixture 1 (`G#`/`A#` rows citing "AP-XX/AL-XX · canonical name" exactly as the owning file spells them). One row per mode — 13 rows, stated total 13. Budget: max 2 findings beyond the key, non-defect reports count against it. "Modes deliberately not covered" lists all 14 fixture-1-covered modes (AP-01/02/03/04/06/09/14; AL-01/02/03/04/06/07/10) — citing any of them is off-key here.

### D5 — Doc updates (minimal wording)

- **CLAUDE.md**: `examples/` file-map row covers both fixtures; "Testing changes" steps say to grade against the fixture(s) whose answer keys cover the touched modes.
- **README.md**: layout tree + one usage line for fixture 2; roadmap "More fixtures" trimmed to what remains (8–12-team scale portfolios).
- **verify-gate.md**: "fixture eval" wording generalizes to "the fixture(s) under `examples/` whose answer keys cover the touched category."

## Risks / Trade-offs

- [Accidental unplanned defect burns the budget] → D3 armoring rules + a dedicated self-audit task: sweep the drafted fixture against all 27 modes before finalizing, fixing or promoting anything found.
- [A planted defect is arguably two IDs] → contained by design separation (D2 constructions isolate the triggering evidence) and, where residual (AP-07/AP-08 co-location), an explicit counted-separately note in the key.
- [Leakage: scenario shapes echo taxonomy worked examples] → different domain per mode than the taxonomy's example (cycle = telemetry/schema, not auth SDK; AL-12 = partner portal, not marketplace signups... adjusted where shapes drifted close).
- [Verify-gate eval variance: a fresh subagent may near-miss one mode] → borderline results surfaced per the gate's honesty rule, not silently counted; fixture text sharpened rather than key loosened.

## Migration Plan

Pure addition + doc wording; revert = delete the new file and revert three doc edits. No sequencing constraints.
