# OKR Goodness Rubric

Scoring reference for OKR-Ninja. Consult this while scoring; do not paraphrase it into reports. Every score and finding must satisfy the Evidence Discipline rules at the end of this file.

## How to Use

1. Extract each OKR verbatim (objective text + each KR text + owner + timeframe + any committed/aspirational label) with source refs (format: see `references/report-format.md`, "Source references") before scoring anything.
2. Score every dimension below on the 0–4 scale using the anchors. Pick the anchor whose description matches; do not interpolate feelings — if the text sits between anchors, take the **lower** score.
3. Check the anti-pattern catalog against each objective and KR. Anti-patterns and dimension scores are reported separately but usually co-occur (an anti-pattern is the *named cause* of a low score).
4. Roll up per the Roll-Up section. Apply caps mechanically.
5. If information is absent (no owner listed, no baseline stated), score what the text says, not what you assume the team "probably meant." Absence scores low; it is not "unknown."

## The 0–4 Scale (general shape)

- **4** — Exemplary. A reviewer could execute/measure from the text alone.
- **3** — Sound. One small, explicitly identifiable gap.
- **2** — Usable but flawed. Needs rewriting to be trustworthy.
- **1** — Seriously deficient. The dimension's core property is mostly absent.
- **0** — Property absent entirely, or actively inverted.

---

## Part 1 — Objective Dimensions (score per objective)

### O1. Outcome Orientation
Is the objective a change in the world, or a list of work?

- **4** — States a changed end-state for customers/business/system ("Customers trust checkout enough to store cards"). No delivery verbs. You could achieve it by a route other than the one the team has in mind.
- **3** — Outcome-framed but names one solution ("Reduce churn by relaunching onboarding") — the outcome survives if the named solution is dropped.
- **2** — Mixed: an outcome clause plus deliverables joined by "by shipping/via/through," where deleting the deliverables leaves the outcome vague.
- **1** — A project name or deliverable with outcome garnish ("Ship the new billing platform to improve reliability").
- **0** — Pure task list or project title ("Migrate to Postgres 16"; "Complete Phases 1–3").

Detection cue: verbs. *Ship, launch, migrate, complete, implement, roll out, deliver* → pull toward 0–1. *Customers can, users trust, revenue from, no team waits* → pull toward 3–4.

### O2. Inspiring but Concrete
Would a team member repeat it unprompted, and would two people agree on what it means?

- **4** — Memorable one-liner (< ~15 words), plain language, a specific noun subject, no metric in it (metrics belong in KRs).
- **3** — Clear and specific but bureaucratic phrasing, or slightly long (15–25 words).
- **2** — Contains one abstraction that two readers would gloss differently ("operational excellence," "best-in-class," "world-class," "delight").
- **1** — Strung-together abstractions; or a metric target pasted in as the objective.
- **0** — Content-free ("Improve the business"; "Excellence in everything we do") or unintelligible jargon.

### O3. Time-Bound
- **4** — Explicit period (e.g., "by end of Q3 FY26" or the OKR doc's stated cycle) AND the objective is plausibly achievable-or-failable within it.
- **3** — Period inherited unambiguously from the document (page titled "Q3 2026 OKRs") though not restated.
- **2** — Period ambiguous (doc mixes quarters; "this year" on a quarterly page) or objective is an open-ended journey ("continuously improve…") crammed into a cycle.
- **1** — Conflicting dates in the same OKR (objective says H2, KRs say Q3).
- **0** — No timeframe anywhere in text or source context.

### O4. Strategic Anchoring
- **4** — Explicitly links to a named company/portfolio priority in the text ("supports Company Bet #2: Self-serve growth") and the link is logically sound.
- **3** — No explicit link, but an obvious one-step chain to a strategy artifact found in the same source corpus.
- **2** — Link asserted but non-sequitur, or plausible only with unstated assumptions.
- **1** — Anchored to a stale or superseded strategy (references a priority the current strategy doc dropped).
- **0** — No connection findable; or contradicts a stated company priority. (Contradictions also feed the alignment analysis — see `references/alignment-taxonomy.md`.)

If no strategy source exists in the corpus, score O4 as **N/A** (exclude from roll-up) and record a gap finding — do not guess.

---

## Part 2 — Key Result Dimensions

K1–K5 are scored **per KR**. K6 and K7 are scored **once per KR set**.

### K1. Measurability (baseline AND target)
- **4** — Named metric + numeric baseline + numeric target + unit + measurement window ("Checkout conversion 2.1% → 3.0%, weekly avg, Q3").
- **3** — Metric, target, unit present; baseline missing but retrievable from a cited source, or window unstated.
- **2** — Target without baseline ("Reach 95% uptime" — from what?), or direction without magnitude ("Increase NPS significantly").
- **1** — Qualitative dressed as a metric ("Improve quality score" with no defined score), or ambiguous denominator ("Reduce errors 50%" — of what population?).
- **0** — Nothing countable; pure prose or a pure done/not-done milestone.

### K2. Outcome vs Output
- **4** — Measures a result someone outside the team experiences (revenue, latency, retention, adoption, incidents).
- **3** — Proxy output with a stated, credible causal link to an outcome ("Cut p95 build time 40m → 15m to unblock daily releases").
- **2** — Activity volume ("Run 20 experiments"; "Hold 12 customer interviews") with no stated outcome link.
- **1** — Delivery milestone with a date as the "metric" ("Launch v2 by June 15").
- **0** — Effort accounting ("Spend 30% of sprint capacity on tech debt").

### K3. Ambition Calibration (sandbag / moonshot detection)
Compare target against baseline, stated trend, or prior-period actuals when present in the corpus.

- **4** — Target ~20–100% beyond trend-extrapolation or an explicitly justified stretch; labeled committed vs aspirational consistently with its size.
- **3** — Clearly a stretch but justification absent; a properly-labeled committed KR at modest stretch; **or** a >5x moonshot backed by a stated mechanism (a named lever, intermediate milestone, or resourcing signal) and labeled aspirational — extreme but honest ambition.
- **2** — Target ≈ trend extrapolation: achievable by doing nothing new. Effort-free, though not below baseline — one notch above an outright sandbag.
- **1** — **Sandbag**: target at or below current baseline/last period's actual ("Maintain 99% uptime" when baseline is 99.2%). Or **unmoored moonshot**: >5x with no mechanism, no milestones, no resourcing signal.
- **0** — Target already achieved per the same document, or mathematically guaranteed (target below a floor the system enforces).

If no baseline/trend exists anywhere, cap K3 at 2 and note that calibration is unverifiable — the deficiency is real even if intent was good.

### K4. Ownership Clarity
- **4** — One named accountable individual (a person, not a team) in the OKR source itself.
- **3** — Owning team named, individual derivable from the same source (e.g., team lead listed on the page).
- **2** — Team named only, in a multi-team document where the KR spans teams.
- **1** — Shared ownership ("Eng + Marketing") with no tiebreaker, or owner is a person who appears nowhere else in the corpus.
- **0** — No owner stated anywhere.

### K5. Verifiability of Metric Source
- **4** — Names the system/dashboard/query of record ("per Looker dash 'Checkout Funnel'"; "Datadog SLO monitor #142").
- **3** — Metric is a standard one with an obvious single system of record in this org (found elsewhere in corpus).
- **2** — Plausibly measurable but source unnamed and multiple candidate systems would give different numbers.
- **1** — Requires data collection that doesn't exist yet, with no KR/task to build it.
- **0** — Unmeasurable in principle as written ("Increase team happiness by 30%") or the metric is defined only in someone's head.

### K6. Leading/Lagging Mix (per KR set)
- **4** — Set contains ≥1 lagging outcome KR and ≥1 leading indicator that predicts it; the causal pairing is evident from the text.
- **3** — Mix present but pairing loose.
- **2** — All lagging (only end-of-quarter truths — no steering signal mid-cycle) or all leading (proxies with nothing they predict).
- **1** — KRs are heterogeneous milestones with no indicator logic at all.
- **0** — Single KR, or KRs that restate each other.

### K7. Set Coherence & Sufficiency (per KR set)
- **4** — 2–5 KRs; jointly, hitting all of them would convince a skeptic the objective happened; no KR is unrelated to the objective.
- **3** — One coverage gap (a facet of the objective no KR touches).
- **2** — Multiple gaps, or one orphan KR that serves a different goal.
- **1** — KRs mostly measure a different objective than the one stated; or >7 KRs (an unfocused metrics dump).
- **0** — No KRs, or KRs contradict the objective.

---

## Part 3 — Roll-Up

All arithmetic on 0–4 numeric scores; convert to letters last. Exclude N/A dimensions from means.

**Per-KR score** = mean(K1..K5) for that KR.

**Per-OKR score** = 0.35 × mean(O1..O4) + 0.45 × mean(all per-KR scores) + 0.20 × mean(K6, K7).

**Caps (apply after the weighted mean, in order):**
1. Any KR with K1 = 0 or K5 = 0 → that KR's score capped at 1.0.
2. Any **Critical** anti-pattern confirmed on an OKR → per-OKR score capped at 1.9 (max D).
3. ≥2 **Major** anti-patterns on one OKR → capped at 2.4 (max C).
4. O1 = 0 (objective is a task list) → per-OKR score capped at 2.0.

**Letter grades:** A ≥ 3.5 · B 2.75–3.49 · C 2.0–2.74 · D 1.0–1.99 · F < 1.0.

**Per-team score** = mean of its per-OKR scores, with caps:
- More than half the team's KRs carry K1 ≤ 1 → team capped at C.
- Any team with 0 OKRs traceable to strategy (all O4 ≤ 1, strategy corpus present) → team capped at C.

Report the numeric score alongside the letter (e.g., "B (3.1)") so portfolio comparisons stay ordinal.

**Needs-rework threshold:** a per-team roll-up grade of **D or below** means the team's OKR set needs rework before its quarter can be trusted. `references/report-format.md` §6 uses this threshold (together with any Critical finding) to route teams to the okr-deepdive skill; the roll-up grade computed here — not the heatmap integers below — governs that routing.

### Team dimension scores (for the portfolio heatmap)

Team dimension score = arithmetic mean of all scored instances of that dimension across the team's OKRs (objectives for O1–O4; KRs for K1–K5; KR-sets for K6–K7), rounded DOWN to an integer; N/A instances excluded; a dimension with zero scored instances shows N/A.

These eleven integers (O1 O2 O3 O4 K1 K2 K3 K4 K5 K6 K7) populate the portfolio heatmap defined in `references/report-format.md`. They are display aggregates only — deep-dive routing is governed by the per-team roll-up grade above, never by heatmap cells.

---

## Part 4 — Anti-Pattern Catalog

Each anti-pattern carries a severity — **Critical**, **Major**, or **Minor** — as defined in `references/report-format.md` ("Severity scale"). This file assigns severities; it does not define them.

Cite by ID and canonical name. A finding must quote the triggering text verbatim (see Part 5). Every **After** line below is an OKR-Ninja-style proposal, and invented numbers in it carry the placeholder tag per the convention in `references/report-format.md` §3.

### AP-01 · Task Masquerading as KR — **Major**
- **Definition:** A KR that is a deliverable or activity, not a measurable result.
- **Detect:** KR begins with ship/launch/implement/migrate/complete/build/write; no metric, no baseline→target pair.
- **Before:** "KR: Launch the new referral flow."
- **After:** "KR: Referral-driven signups 120/mo → 400/mo by end of Q3 (source: Amplitude 'Referral Signups')." [proposal — placeholder target]

### AP-02 · Binary KR with No Gradient — **Major**
- **Definition:** Done/not-done KR; scoring mid-cycle can only be 0% or 100%.
- **Detect:** Yes/no phrasing ("SOC 2 achieved"), single event, no numeric scale.
- **Before:** "KR: Achieve SOC 2 Type II."
- **After:** "KR: Close 100% of the 34 open SOC 2 audit findings (baseline: 0/34 closed), audit report received by Sep 15." [proposal — placeholder target]

### AP-03 · Vanity Metric — **Major**
- **Definition:** Metric that rises with exposure/spend but doesn't indicate the outcome the objective claims.
- **Detect:** Cumulative totals (total signups ever, page views, downloads, followers) attached to objectives about value, retention, or quality.
- **Before:** "KR: Reach 1M total registered users."
- **After:** "KR: Weekly active users completing ≥1 core action: 42k → 70k." [proposal — placeholder target]

### AP-04 · KR Without Baseline — **Major**
- **Definition:** Target stated with no starting point; ambition and progress are both unjudgeable.
- **Detect:** "Reach/achieve/hit X" with no "from," no current value, and none retrievable in the corpus.
- **Before:** "KR: Achieve 40% margin."
- **After:** "KR: Gross margin 33% (Q2 actual, per Finance dash) → 40%." [proposal — placeholder target]

### AP-05 · Everything Is a P0 — **Major**
- **Definition:** All objectives/KRs marked top priority (or none prioritized), so the set encodes no trade-off.
- **Detect:** Uniform "P0/critical/must-hit" labels across ≥4 objectives; or a team with >5 objectives, all unranked.
- **Before:** "P0: O1…P0: O2…P0: O3…P0: O4…P0: O5."
- **After:** "P0: O1. P1: O2, O3. Dropped to backlog: O4, O5."

### AP-06 · Sandbagged Target — **Major**
- **Definition:** Target at/below current baseline, trend, or last period's actual.
- **Detect:** Compare target to any baseline/prior actual in the corpus; flag "maintain," "keep," "stay above" where baseline already exceeds target.
- **Before:** "KR: Maintain NPS above 40" (Q2 report in same space: "NPS: 47").
- **After:** "KR: NPS 47 → 55, quarterly survey (n ≥ 300)." [proposal — placeholder target]

### AP-07 · Unmoored Moonshot — **Major**
- **Definition:** >5x stretch with no mechanism, intermediate milestone, or resourcing signal — functions as decoration, not a goal. (Maps to K3 = 1, the same anchor tier as AP-06.)
- **Detect:** Target/baseline ratio > 5 with no accompanying "how" anywhere on the page.
- **Before:** "KR: Grow ARR $2M → $20M this quarter."
- **After:** "KR (aspirational): ARR $2M → $3.5M via enterprise tier launch; leading KR: 25 enterprise pilots signed (0 → 25)." [proposal — placeholder target]

### AP-08 · Committed vs Aspirational Not Labeled — **Minor**
- **Definition:** Set mixes must-hits and stretch bets with no labels, corrupting expected-attainment and sandbag/moonshot judgments.
- **Detect:** No "committed/aspirational" (or ~0.7-target convention) markers anywhere in the doc while targets vary wildly in stretch.
- **Before:** "KR1: 99.95% uptime. KR2: 10x referral traffic."
- **After:** "KR1 (committed): 99.95% uptime. KR2 (aspirational): referral traffic 5k → 50k sessions/wk." [proposal — placeholder target]

### AP-09 · Metric Nobody Can Measure — **Critical**
- **Definition:** No system of record exists or could report the number as defined; the KR can never be honestly scored.
- **Detect:** Metric names no source; corpus shows no dashboard/tool for it; or it quantifies an internal state ("developer joy up 30%") with no instrument.
- **Before:** "KR: Increase engineering morale by 25%."
- **After:** "KR: Quarterly eng survey (n ≥ 40, existing Culture Amp instrument): eNPS 12 → 25." [proposal — placeholder target]

### AP-10 · BAU Dressed as OKR — **Major**
- **Definition:** Routine operational duty presented as a goal; achieved by default staffing, displaces real goals.
- **Detect:** "Continue," "maintain," "keep supporting," "ongoing"; describes the team's standing job with no delta.
- **Before:** "O: Continue supporting production systems reliably."
- **After:** "O: Cut operational toil so the team ships again — KR: pages/on-call week 22 → 8." [proposal — placeholder target] (Or move the standing duty to a health-metric section outside the OKRs.)

### AP-11 · Objective as Kitchen Sink — **Minor**
- **Definition:** One objective bundling multiple unrelated end-states joined by "and."
- **Detect:** ≥2 "and"-joined outcome clauses with disjoint nouns/audiences; KRs cluster into unrelated groups.
- **Before:** "O: Delight enterprise customers and modernize our data platform and grow the team."
- **After:** "O1 (ranked first): Enterprise customers renew without an escalation because the product earns it. O2: Analysts answer their own questions on the new data platform, unaided." (Keep only the top two, ranked; headcount growth moves to the hiring plan — it is an input, not an outcome.)

### AP-12 · Orphan KR — **Major**
- **Definition:** KR whose success would not move its stated objective.
- **Detect:** No causal chain in ≤2 steps from KR metric to objective outcome; KR shares no nouns/domain with objective.
- **Before:** "O: Customers trust our billing accuracy. KR: Publish 6 engineering blog posts."
- **After:** "KR: Billing dispute tickets 140/mo → 45/mo." [proposal — placeholder target]

### AP-13 · Ambiguous Denominator — **Critical**
- **Definition:** A percentage/ratio whose population is undefined, so any number can be claimed.
- **Detect:** "% of errors/users/requests/tickets" where the base set has multiple plausible readings and none is specified.
- **Before:** "KR: Reduce errors by 50%."
- **After:** "KR: 5xx responses on /checkout, 7-day rolling: 0.8% of requests → 0.4% (Datadog monitor #77)." [proposal — placeholder target]

### AP-14 · Date as Target — **Major**
- **Definition:** The "measure" is a calendar date for a deliverable; a schedule commitment, not a result. (Milestone-chain variant of AP-01: *every* KR in the set is one.)
- **Detect:** KR of the form "X by <date>" where X is a deliverable and the only failure mode is lateness.
- **Before:** "KR: Data warehouse migration complete by Aug 31."
- **After:** "KR: 100% of the 61 production report queries served from the new warehouse (0/61 → 61/61) with p95 query time ≤ prior system." [proposal — placeholder target]

### AP-15 · Ownerless KR — **Major**
- **Definition:** No accountable individual or team attached; corollary of K4 ≤ 1.
- **Detect:** Owner field blank/absent; or owner is a group with no lead named anywhere in corpus.
- **Before:** "KR: Churn 3.2% → 2.4%. Owner: —"
- **After:** "KR: Logo churn 3.2% → 2.4% monthly. Owner: <named individual> (Growth)."

---

## Part 5 — Evidence Discipline

Non-negotiable. A score or anti-pattern finding that violates these rules must be discarded, not softened.

1. **Verbatim or nothing.** A finding may cite an anti-pattern only if it quotes the exact OKR text that triggers it, character-for-character as extracted, in quotation marks, with its source ref (format defined in `references/report-format.md`, "Source references"). Paraphrase presented as quotation is itself a Critical reporting defect.
2. **Scores name their spans.** Every dimension score ≤ 3 must list the specific quoted span(s) that drove it (e.g., `O1=1 — "Ship the new billing platform" [Billing Q3 OKRs › Team Goals]`). A 4 needs the quoted text being scored, not additional justification.
3. **Cross-source claims quote both ends.** Sandbagging (AP-06), stale strategy (O4=1), and baseline-retrievability (K1=3) claims require verbatim quotes from *both* documents with both source refs.
4. **Absence claims state the search.** "No baseline anywhere" or "no owner in corpus" must record what was searched (sources enumerated) — absence-of-evidence findings without a search trail are discarded.
5. **No inferred numbers.** Never compute or "recall" a baseline, trend, or prior actual that is not quoted from a source. If calibration inputs are missing, use the K3 unverifiable cap; do not estimate.
6. **Quote minimally.** Quote the triggering span, not whole pages — enough that a reader can verify the finding without opening the source, and no more.
7. **Verify before reporting.** Before a finding enters the report, re-open the source and confirm the quoted span exists verbatim. A quote that fails re-verification drops the finding entirely.
8. **Rewrites are labeled as proposals.** Before→after rewrites must mark the "after" as OKR-Ninja's proposal, never presented as if sourced. Invented numbers in a proposal use a `<placeholder>` or the tag "[proposal — placeholder target]" — the convention is defined once in `references/report-format.md` §3.

**Finding format:** goodness findings use the template and required fields defined in `references/report-format.md` §3 (Severity · AP-ID + canonical anti-pattern name · Team · Verbatim quote + source ref · Why it's a problem · Scores affected · Suggested rewrite). This file defines the evidence rules only; no finding template lives here.
