# Full-catalog self-audit sweep — examples/sample-portfolio-2.md

Each row: does the mode fire in the fixture body, and exactly where. Target: the 13 planted modes fire exactly once each; the 14 off-key modes fire zero times. Hardening edits applied during the sweep: C1/C4 enriched to name the workstreams their tagged child objectives serve (kills off-key AL-05 exposure on CR3/CS3/IN1/IN2/DS/AC4 tags); non-defect #8 added (cycle-edge label ambiguity routes to G3/AP-08, not AL-12). Verify-repair edits (cycle 1): CS3.2 softened 45s→12s (the 8s draft was a 5.6x cut — an undeliberate AP-07 near-miss this sweep's first pass missed); C2 gained a third named workstream ("keeping the delivery promises we report to customers") so AC3's "supports C2" tag traces soundly; non-defect #8 reworded to apply the taxonomy's disconfirming check rather than assert what AL-12 requires.

| Mode | Verdict | Where / why not |
|---|---|---|
| AP-01 Task Masquerading as KR | none | Every deliverable-verb KR carries a countable coverage/adoption pair: CR3.1 0/14→14/14, CS3.1 apps 1→3, IN2.1 0/22→22/22, IN2.2 2/9→9/9, AC3.2 0→40, AC4.2 38%→100%, DS1.2 0→6. |
| AP-02 Binary KR | none | No done/not-done KR; all have numeric gradients. |
| AP-03 Vanity Metric | none | No cumulative totals/pageviews; CR2.1 installs are quarterly, attributed, and the referral objective's intended outcome (non-defect #1). |
| AP-04 KR Without Baseline | none | All 31 KRs state an inline baseline. |
| AP-05 Everything Is a P0 | fires once (G1) | Accounts AC1–AC4 uniform "Priority: P0" + notes quote. Other teams have 2–3 objectives, unlabeled — below the ≥4 threshold. |
| AP-06 Sandbagged Target | none | Every target strictly better than its baseline; appendix baselines (retention 71, Sev-1 9, CSAT 78) all sit below the corresponding targets; no "maintain/keep above" phrasing. |
| AP-07 Unmoored Moonshot | fires once (G2) | CR2.1 15x, no mechanism. Full finite-ratio inventory (growth or cut, by factor): CS2.1 4x, CS3.2 3.75x, CR3.2 3.5x, AC2.1 3.5x, CS3.1 3x — every other finite ratio below 3x; all ≤4x. Bounded completions (AC4.2 38%→100%; IN2.2 2/9→9/9, the planted G8 KR) are completion-of-fixed-set, not open-ended growth, and stay under the 5x bar. Zero-baseline launches (DS1.2, DS2.2, CR3.1, IN2.1, AC3.2) carry a mechanism, a bounded denominator, or a pin (non-defect #4). AC3.2 and AC4.2 pinned as non-defects #4/#7. |
| AP-08 Commitment Not Labeled | fires once (G3) | Courier page only; every other page carries the convention line, Accounts labels AC3.2 stretch. |
| AP-09 Metric Nobody Can Measure | none | Every KR names an instrument; DS2.4 names "ops weekly report" (non-defect #3 — its defect is AP-13). |
| AP-10 BAU Dressed as OKR | fires once (G4) | CS1 objective "Continue running…". No other continue/maintain/keep/ongoing objective phrasing. |
| AP-11 Kitchen Sink | fires once (G5) | DS1 only "and"-joined multi-outcome objective; all other objectives are single-theme. |
| AP-12 Orphan KR | fires once (G6) | IN1.3 app-store rating under exec-dashboards objective. All other KRs share domain with their objective (CR2.1 pinned, non-defect #1). |
| AP-13 Ambiguous Denominator | fires once (G7) | DS2.4 "failure rate" population undefined. All other %/ratios define denominators: CS2.2 "of production deploys", AC1.2 "of all new paid accounts created in the quarter", AC4.1 "of invoices issued monthly", CR3.2 "share of events emitted on those flows", DS2.1/AC3.1 define populations inline; CR1.1 crash-free sessions has the single standard Crashlytics reading. |
| AP-14 Date as Target | none | No KR whose only measure is a calendar date; "by end of Q1" on DS2.4 accompanies a metric pair. |
| AP-15 Ownerless KR | fires once (G8) | IN2.2 "Owner: TBD" on the one page using per-KR owners. Other pages use header owners (K4 derivable, not AP-15 — fixture-1 precedent). |
| AL-01 Unacknowledged dependency | none | Every cross-team deliverable appears in its producer's own OKRs: portal (AC3.2), SDK GA (CS3.1), schema validation (IN2.1), instrumentation (CR3.1). Non-defect #5. |
| AL-02 Conflicting metrics | none | No shared metric with opposing directions; no adversarial-mechanism pair. Retention (Courier vs C3) consistent per non-defect #6; cost (CS1.2 vs C4) identical. |
| AL-03 Duplication | none | No two teams pursue the same outcome/surface; the on-time-rate pair routes to AL-08 as root cause (non-defect #2). |
| AL-04 Orphan objective | none | Every objective carries an explicit "supports Cx" link. |
| AL-05 Cascade drift | fires once (A1) | CS2→C2: KRs match neither C2's metric nor any of its three named workstreams. All other tags trace to a workstream the parent's own text names (C1: dispatch adoption + self-serve billing; C2: delivery-promise reporting covers AC3; C4: pipeline consolidation + shared dashboards; C3: driver retention/love). |
| AL-06 Timeline mismatch | none | No dated pair across any dependency edge; cycle edges are condition-based, undated (non-defect #5). |
| AL-07 Resource contention | none | No shared pod/specialist/environment/budget claimed by multiple teams; dependencies are named deliverables in producers' OKRs, not capacity bookings. |
| AL-08 Terminology collision | fires once (A2) | "on-time delivery rate": DS2.1 vs AC3.1 differ in formula, denominator, window, and source. No other metric name is defined by two teams. |
| AL-09 Baseline disagreement | fires once (A3) | CSAT 86 (AC2.2) vs 78 (appendix), same survey and period. All other repeated baselines agree (retention 71 ×3, Sev-1 9 ×2, cost $0.42 ×2). |
| AL-10 Strategy coverage gap | none | C1←Dispatch+AC4; C2←AC1+AC2+AC3 (all three named workstreams) and CS2; C3←CR1/CR2; C4←CS1/CS3/CR3/IN1/IN2. Every named workstream in C1/C2/C4 has an owner. |
| AL-11 Circular dependency | fires once (A4) | CR3.1→CS3.1→IN2.1→CR3.1; each edge verbatim; no other cycle (portal edge is one-way). |
| AL-12 Commitment asymmetry | fires once (A5) | DS2.2 (committed) on AC3.2 (stretch). Cycle edges pinned by non-defect #8 (label absence = G3, not AL-12). |

Result: 13/13 planted modes fire exactly once; 0/14 off-key modes fire. Sweep clean after the two hardening edits.
