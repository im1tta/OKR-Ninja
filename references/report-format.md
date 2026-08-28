# Report format — output contract for a portfolio review

This file is the only source of truth for how the final report is structured, for the **severity scale**, and for the **source-ref format**. Rubric dimensions and anti-patterns (AP-XX) are defined in `references/goodness-rubric.md`; alignment failure modes (AL-XX) in `references/alignment-taxonomy.md` — refer to them by ID and canonical name, never redefine them here.

## Severity scale

One scale, three levels, used everywhere in this repo:

- **Critical** — the finding invalidates the OKR or the plan as written: the KR cannot be honestly measured or scored, a committed outcome is impossible as sequenced, or two teams are actively working against each other. Blocks trust in the quarter until fixed.
- **Major** — materially undermines the OKR's usefulness or the portfolio's coherence: failure, waste, or contention is likely without a correction or a conversation that has not visibly happened.
- **Minor** — polish and hygiene: weakens clarity, traceability, or calibration; cheap to fix, low immediate risk. Fix opportunistically.

These are the only severity definitions in the repo. `references/goodness-rubric.md` assigns one of these names to each AP-XX anti-pattern, and `references/alignment-taxonomy.md` to each AL-XX failure mode; both point here rather than redefining the scale.

## Source references

One format everywhere. A **source ref** is:

```
<file path, Confluence page title, or Jira issue key> › <nearest heading, or issue field>
```

plus `› line N` when the source is a local file. Examples:

- `exports/growth-q3.md › Objective G2: Turn our funnel into a machine › line 41`
- `Payments Q3 OKRs › Objective P2: Cut fraud losses without drama`
- `PLAT-1204 › Description`

This subsection is the only definition of the source-ref format; `SKILL.md`, `references/goodness-rubric.md`, and `references/alignment-taxonomy.md` point here ("Source references") for the format instead of describing it.

## Evidence invariant

Every finding — goodness or alignment — must include at least one **verbatim quote** with its **source ref**. Alignment findings quote **both** sides. A claim that cannot be quoted is not reported.

The report has six sections, in this order.

---

## 1. Executive summary

Rules:
- **Verdict first.** Line 1 is the overall portfolio verdict, not throat-clearing.
- Maximum ~10 lines total.
- Must state: number of teams reviewed, number of findings by severity (Critical / Major / Minor), the single worst alignment risk (by AL-ID + canonical name), and the single most common goodness anti-pattern (by AP-ID + canonical name).
- No finding appears here that is not detailed later in the report.

> **Example (fictional):**
>
> **Verdict: At risk.** 4 teams reviewed; 2 Critical, 5 Major, 3 Minor findings.
> The portfolio's biggest threat is AL-02 Conflicting metrics / adversarial incentives: Payments is adding checkout friction to cut chargebacks while Growth targets +10pt checkout conversion — neither team acknowledges the other.
> The most common quality issue is AP-01 Task Masquerading as KR (3 of 4 teams ship outputs instead of measuring outcomes).
> Platform is implicitly committed to work by two other teams that its own OKRs do not reflect (AL-07 Resource contention).
> Recommended first action: joint Payments/Growth session to reconcile the checkout funnel targets before mid-quarter.

## 2. Portfolio heatmap

Spec:
- A markdown table: **one row per team**, and **exactly these 11 dimension columns**, in this order: **O1, O2, O3, O4, K1, K2, K3, K4, K5, K6, K7**. No other scored columns.
- Cell values are integer **team dimension scores 0–4**, computed per the "Team dimension score" aggregation rule in `references/goodness-rubric.md` (mean of scored instances, rounded down; a dimension with zero scored instances shows **N/A**).
- Below the table, a **legend** mapping the codes to their short names exactly as defined in `references/goodness-rubric.md`: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency.
- Also below the table: one line listing each team's **roll-up grade** from `references/goodness-rubric.md`'s Roll-Up section (letter + numeric), and one line per team of at most 15 words explaining its lowest score. Order rows worst roll-up grade first.

> **Example (fictional):**
>
> | Team | O1 | O2 | O3 | O4 | K1 | K2 | K3 | K4 | K5 | K6 | K7 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | Platform | 1 | 2 | 3 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 |
> | Growth | 2 | 3 | 3 | N/A | 1 | 2 | 2 | 3 | 2 | 2 | 3 |
>
> Legend: O1 Outcome Orientation · O2 Inspiring but Concrete · O3 Time-Bound · O4 Strategic Anchoring · K1 Measurability · K2 Outcome vs Output · K3 Ambition Calibration · K4 Ownership Clarity · K5 Verifiability of Metric Source · K6 Leading/Lagging Mix · K7 Set Coherence & Sufficiency (per `references/goodness-rubric.md`).
> Roll-up grades (per `references/goodness-rubric.md` Roll-Up): Platform D (1.9) · Growth C (2.3).
> - Platform: K3=1 — uptime target sits below the quoted trailing baseline (AP-06 Sandbagged Target).
> - Growth: K1=1 — two of four KRs state targets with no baseline (AP-04 KR Without Baseline).

## 3. Per-team goodness findings

One block per finding, grouped by team, ordered by severity. The heading carries three of the required fields: the severity, the **AP-ID with its canonical anti-pattern name** exactly as spelled in `references/goodness-rubric.md`, and the team.

```
### [<Severity>] AP-XX <Canonical anti-pattern name> — <Team>
- Evidence: "<verbatim quote>" (<source ref>)
- Why it's a problem: <1–2 sentences, tied to the anti-pattern as defined in goodness-rubric.md>
- Scores affected: <dimension codes and scores this finding drove, e.g. K2=1, K1=0>
- Suggested rewrite: <concrete replacement objective/KR text>
```

Required fields: **Severity · AP-ID + canonical name · Team · Verbatim quote + source ref · Why it's a problem · Scores affected · Suggested rewrite.** The quote must satisfy the evidence rules in `references/goodness-rubric.md` Part 5. The rewrite must be concrete replacement text, not advice about writing one.

**Proposed-number convention** (defined here once; applies to every rewrite and recommendation in this report, §3 and §4 alike): a rewrite is OKR-Ninja's **proposal**, never presented as sourced. Any number not quoted verbatim from the corpus appears either as a `<placeholder>` or carries the tag `[proposal — placeholder target]`. Real figures quoted from the corpus may be reused as-is with their source ref.

> **Example (fictional):**
>
> ### [Major] AP-01 Task Masquerading as KR — Payments
> - Evidence: "KR2: Ship checkout API v2 to GA" (Payments Q3 OKRs › Objective 2)
> - Why it's a problem: shipping is an output; the KR succeeds even if nobody adopts the API. No outcome is measured.
> - Scores affected: K2=1, K1=0
> - Suggested rewrite: "KR2: `<target>`% of new checkout sessions run on API v2 by `<date>`, with error rate ≤ `<threshold>`" [proposal — placeholder target]

## 4. Alignment findings

One block per finding, ordered by severity. Alignment findings always cite **both** (or all) involved teams, each with its own verbatim quote and source ref.

```
### [<Severity>] AL-XX <Canonical failure-mode name>: <Team A> ↔ <Team B>
- <Team A> evidence: "<verbatim quote>" (<source ref>)
- <Team B> evidence: "<verbatim quote>" (<source ref>)
- Conflict: <1–2 sentences describing the collision>
- Detection check that fired: <the heuristic from alignment-taxonomy.md that produced the candidate>
- Disconfirming checks run: <each false-positive control that was run, with its result>
- Inference labels: <every inferred link or mechanism labeled "analyst inference"; or "none — all load-bearing text quoted">
- Verdict: CONFIRMED | PLAUSIBLE
- Recommended resolution owner: <team or role who should convene/decide, and the concrete next step>
```

Required fields: **Severity · AL-ID + canonical name · Teams involved · both sides' verbatim quotes + source refs · Detection check that fired · Disconfirming checks run (and their results) · Inference labels on any inferred link · Verdict (CONFIRMED or PLAUSIBLE) · Recommended resolution owner.** Verdict discipline is defined in `references/alignment-taxonomy.md`: CONFIRMED only after every load-bearing quote passed the quote-verification pass; otherwise PLAUSIBLE.

The failure-mode name must match the AL-XX canonical name in `references/alignment-taxonomy.md`. A finding with evidence from only one side is downgraded to a per-team finding or dropped.

> **Example (fictional):**
>
> ### [Critical] AL-02 Conflicting metrics / adversarial incentives: Payments ↔ Growth
> - Payments evidence: "Increase step-up verification coverage to 90% of transactions" (Payments Q3 OKRs › Objective P2)
> - Growth evidence: "Raise checkout conversion from 58% to 68%" (Growth Q3 OKRs › Objective G2)
> - Conflict: step-up verification adds checkout friction; the two KRs push the same funnel in opposite directions and neither KR mentions the other team.
> - Detection check that fired: metric-catalog blocking — same funnel surface, mechanism-level opposition (AL-02 heuristic).
> - Disconfirming checks run: shared/parent OKR covering both — none found; documented split of levers — none found; directionality — confirmed opposed.
> - Inference labels: the friction→conversion mechanism is analyst inference (no team document states the tradeoff).
> - Verdict: CONFIRMED (both quotes re-verified character-for-character against their pages)
> - Recommended resolution owner: VP Product to convene both leads; agree a shared guardrail pair (`<fraud-rate ceiling>` + `<conversion floor>`) within 2 weeks [proposal — placeholder target].

## 5. Prioritized action list

Rules:
- Numbered list, at most 10 items, ordered by (severity, then breadth of impact).
- Each item: one sentence, starts with a verb, names an owner, and references the finding(s) it resolves by section anchor and ID.
- Alignment actions outrank goodness actions at equal severity (they block multiple teams).

> **Example (fictional):**
>
> 1. Convene Payments + Growth to set a joint fraud/conversion guardrail pair — owner: VP Product (resolves §4 AL-02 Conflicting metrics / adversarial incentives).
> 2. Rewrite Platform's uptime KR against the quoted 99.95% trailing baseline — owner: Platform lead (resolves §3 AP-06 Sandbagged Target).

## 6. Suggested deep dives

Rules:
- Recommend an `okr-deepdive` run for a team when **either**: (a) the team's **roll-up grade** — the letter produced by `references/goodness-rubric.md`'s Roll-Up section — is at or below the rubric's stated "needs rework" threshold, or (b) the team has **any Critical finding** (goodness or alignment).
- **The rubric roll-up is the governing computation for deep-dive routing.** The heatmap's per-dimension integers (§2) are display aggregates and never gate a recommendation.
- One line per team: the team name, the reason (grade and/or finding IDs), and a ready-to-paste prompt.
- If no team qualifies, say so explicitly in one line.

> **Example (fictional):**
>
> - **Platform** (roll-up D (1.9), at/below the needs-rework threshold; AP-06 Sandbagged Target + inbound AL-01 Unacknowledged dependency): run `okr-deepdive` — "Deep dive the Platform team's Q3 OKRs from Confluence space PLAT."
