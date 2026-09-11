## Context

See `proposal.md` — Why. The constraint that shapes everything here is that **KR CR2.1 and the Courier page around it are load-bearing three times over**:

| Depends on | What it requires of the Courier page |
|---|---|
| **G2** · AP-07 Unmoored Moonshot at CR2.1 | The 15x target has **no mechanism, intermediate milestone, or resourcing signal anywhere on the page**. AP-07's detect line is literally "Target/baseline ratio > 5 with no accompanying 'how' anywhere on the page." |
| **G3** · AP-08 at Courier set level | Cites "the 15x CR2.1" as the evidence that targets vary wildly in stretch while the page carries no commitment convention. |
| **N1** · intentional non-defect | Forbids AP-03 and AP-12 at CR2.1, on the rationale that "installs are the referral objective CR2's intended outcome" — which requires CR2 to stay an objective whose intended outcome *is* installs. |

`2026-09-10-candidate-repair2`'s run-5 supplies the other half of the picture — the detection's own disconfirming check, run and recorded:

> the AL-05 control `activity KRs ≠ decorative link` — **the company page under C3 names no contributing workstreams beyond the retention metric itself**, and Courier's notes offer only "referral growth is our big swing this quarter." with no stated install→retention mechanism (result: stands)

Two clauses, two pages. The second clause must stay true or G2 dies. The first is on page 91050, where nothing in the key has a stake.

## Goals / Non-Goals

**Goals:**

- Make the AL-05 mechanism check return *no flag* at Courier CR2 by satisfying a branch it already offers, rather than by suppressing the finding.
- Leave the Courier page byte-for-byte unchanged.
- Leave a guard behind, so the correction cannot be silently undone.

**Non-Goals:**

- Not making CR2 a *good* objective. It stays a near-miss — an acquisition-only KR under a retention priority — because that is what N9 measures.
- Not touching C2's text. A1's crispness comes from C2 naming three workstreams that CS2's KRs all miss; nothing here may dilute that contrast.
- Not re-deriving whether to plant the row. The spec settles it and the proposal's Non-goals restate it.

## Decisions

### D1. Edit the parent's page, not the child's — the lever D5a did not weigh

AL-05's heuristic is a three-branch disjunction:

> do the child KRs measure **the parent's metric**, **a documented driver of it**, or **a deliverable the parent's own page names as needed**?

`2026-09-10-fix-fixture1-precision-extras` § D5a weighed three levers and rejected all three, but all three edit the child's side: state the mechanism on the Courier page (kills G2), re-point CR2 at another priority (no C1–C4 is moved by referral installs), plant the row (recall asymmetry). Branch two is satisfiable **from the parent's page**, where the key holds nothing — and where AP-07, which is scoped to "the page" that carries the target, does not look.

This asymmetry is what the spec delta generalizes: for a cross-page defect, pick the side that is free.

**Alternatives considered:**

- **Drop or re-point `(supports C3)`.** AL-05 fires only on an explicit parent link, so removal kills it — and immediately trips **AL-04 Orphan objective**, whose three-way check (explicit link / company metric or documented driver / department-strategy mention) then returns zero of three. AL-04 sits in fixture 2's `not_covered` list, so the finding is off-key and costs budget on every run that makes it. That trades an unplanted in-catalog defect for an unplanted off-key one. Re-pointing has no target: C1 is ARR via enterprise dispatch and self-serve billing, C2 enterprise churn, C4 unit cost.
- **Add a second KR under CR2 measuring referred-driver retention.** It would satisfy branch one directly, but it is precisely AP-07's own published remedy — the anti-pattern's "After" is "KR (aspirational): ARR $2M → $3.5M via enterprise tier launch; **leading KR**: 25 enterprise pilots signed" — so a companion KR under the 15x target is the single most likely thing to be read as the missing "how". It also puts a second retention metric on the same page as CR1.2, inviting an AL-08 duplicate against planted row A2.
- **Known-red triage entry.** Excluded from the budget is not absent from the extras, and the spec closes this route for unplanted true defects ("never by raising a budget"). Forbidden outright for `skill-error`; this is `fixture-ambiguous`, so it is merely wrong rather than invalid.

### D2. The wording: a documented driver, never a "how"

```
- **C3 — Make drivers love the app:** driver-app weekly retention from 71% to 80%
  across FY27, driven by in-app reliability and by driver-to-driver referral growth
  — our FY26 cohort review found drivers who join through a referral retain far
  better than drivers we acquire through paid channels.
```

Three properties, each deliberate:

1. **It names a workstream, in C2's established voice.** C2 reads "driven primarily by onboarding time-to-value, the support escalation backlog, and keeping the delivery promises we report to customers." C3 now reads the same way. The fixture keeps sounding like one company's Confluence page rather than a page written for a grader.
2. **It says why referrals matter, never how 45,000 is reached.** A mechanism in AP-07's sense answers "how do you get from 3,000 to 45,000" — a program, a spend, a milestone, a headcount. "Referred drivers retain better" answers a different question and gives CR2.1's target no more support than it had. The retention claim is also unquantified and retrospective (an FY26 cohort review), so it cannot be mistaken for a target or a baseline.
3. **It preserves N6's quote.** `driver-app weekly retention from 71% to 80% across FY27` survives character-for-character, as does the C3 label, so CR1.2's "Q1 step toward the FY27 80% goal in C3" stays consistent and N6 stands.

### D3. N9 guards the corrected state; T2 records why

**N9** forbids AL-05 at `Objective CR2`. It is legitimate only because of D2: after the edit the fixture text genuinely exhibits the property N9's rationale asserts (C3 names the driver), which is the bar `An intentional non-defect demonstrates the property its rationale claims` sets. It costs nothing in budget terms — an extra already counts — and buys a named violation instead of an anonymous extra if C3's wording ever regresses.

Its near-miss character is intact and worth having: CR2 still links to a retention priority while measuring only installs, so a reviewer who skips the parent page will still flag it. That is a false positive the rubric should not produce, which is exactly what the non-defect list is for.

**T2** (`fixture-ambiguous`, `fixed`) records the disposition, the per-batch run counts, and each rejected lever with the row it would have cost — the record the spec delta's second new scenario requires.

### D4. Verification is a 5-run candidate batch on `fixture2-portfolio` only

The change touches fixture 2's content and nothing else — no rubric, no taxonomy, no procedure — so `verify-gate.md`'s slice-scoping rule points at `fixture2-portfolio` alone; fixture 1's two slices read a file this change does not open. Smoke (1 run) cannot distinguish "fixed" from "the 1-in-5 did not fire", so the tier is **candidate**: 5 runs, working tree only, read against the key's absolute criterion.

Pass requires all three of:

- `AL-05@Objective CR2` absent from the extras in 5/5;
- rows **G2**, **G3** and **A1** found by canonical ID in 5/5 (with all ten others);
- zero fabricated quotes, counted findings ≤ 2 per run.

If G2 drops in any run, D2's wording is the suspect and the repair is to weaken the causal claim on C3, not to widen a row. If `AL-05@Objective CR2` survives, the repair is stronger parent-page text — and N9 does not ship until it is genuinely dead, because a non-defect the reports keep violating with sound reasoning is a key defect by the spec's own rule.

**Result — batch `2026-09-11-candidate-cbdeba3` (5 runs, `claude-opus-5[1m]`, skill `cbdeba3`): 5/5 pass.** All thirteen rows found id-exact in every run (G1–G8, A1–A5 each 5/5); zero fabricated, near-miss and out-of-scope quotes; structure clean in 5/5. `AL-05@Objective CR2` does not appear in any run. Counted findings beyond the key were 0/0/0/0/2 against a budget of 2 — run 5's two are `AL-01@KR IN2.2` and `AL-10@KR DS1.2`, both single-run, both seen in earlier batches, and neither touching CR2 or C3.

R1 is refuted from the reasoning side, not merely the aggregate. Run 1 ran its AP-07 search across both pages and recorded the distinction this design turns on: *"Search scope: the Courier section (lines 35–49) plus the company priorities section (lines 7–13), which names referral growth as a C3 driver but commits no lever to Courier."* The new sentence was read, weighed, correctly classified as a driver rather than a how — and G2 stood.

## Risks / Trade-offs

- **[R1 — primary] The C3 sentence is read as the "how" AP-07 requires to be absent, and G2 drops.** → Mitigated by D2: the claim is retrospective, unquantified, about *why referrals matter for retention* rather than *how installs grow 15x*, and it sits on page 91050 while AP-07's detect line is scoped to the page carrying the target (91116). Measured directly — G2 must be 5/5, and it has been 5/5 in the last three batches, so a drop is unambiguous.
- **[R2] AL-05's secondary tell — "KRs achievable in a quarter where the parent metric worsens" — still technically holds at CR2, so a run could flag it anyway.** → The tell is a supporting signal in the heuristic, not an independent trigger; the primary question is the three-branch check, and run-5's transcript shows the model consults the parent page for named workstreams exactly as branch two describes. The batch settles it; a survivor means stronger C3 text, never a widened row or a known-red entry.
- **[R3] N9 outlives the reasoning behind it.** → Its text names the property it depends on (C3 naming the driver), so a reader who finds that property gone knows the row is stale rather than wrong; T2 carries the same reasoning independently.
- **[R4 — retired] Two selftest cases grade frozen fixture-2 reports that list `AL-05@Objective CR2` as an extra, so a key edit might move their expectations.** → It cannot: `harness.py:1533` resolves a case's key as `cdir/case["key"]`, then `selftest/keys/`, then the live `evals/keys/`, and `evals/grader/selftest/keys/sample-portfolio-2.json` exists — a frozen snapshot holding N1–N8 and no triage entries. N9 and T2 are invisible to the corpus, which is insulated from key evolution by construction. The consequence worth stating is the opposite of a risk and of a guard: **`selftest` does not exercise N9 at all.** N9's standing checks are `harness.py check` (its anchor must resolve to exactly one body line) and every future graded batch; nothing in the zero-token tier would notice if it stopped matching.
- **[Trade-off] Fixture 2's company priorities page grows a sentence of narrative that no key row plants a defect in.** → Accepted. C2 already carries the same kind of sentence, the strategy trace needs parent pages with real content for AL-04/AL-05/AL-10 to be decidable at all, and the alternative is a fixture that taxes correct answers.

## Migration Plan

None — fixture and key content only, no schema or interface. Rollback is `git revert`; no committed run batch is invalidated, since each batch records the `key_hash` it was graded under and the frozen selftest inputs are independent copies.
