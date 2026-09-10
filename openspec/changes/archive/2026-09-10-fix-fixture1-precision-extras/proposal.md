# Proposal: fix-fixture1-precision-extras

## Why

The archived change `2026-09-09-fix-baseline-recall-gaps` closed the recall half of what the eval harness measured; the **precision half is still open**, and it now fails the gate. The latest smoke batch (`evals/runs/2026-09-10-smoke-9551238`) reports `fixture1-portfolio` at 0/1: every planted defect found by canonical ID, zero fabricated quotes, but **3 counted findings against a budget of 2**, one of them a violation of intentional non-defect N3. The same extras recur at 1–3 of 5 runs across `2026-09-08-baseline-02f27be`, `2026-09-09-candidate-8d1cb12` and `2026-09-09-candidate-opus-8d1cb12` — the "same four or five findings each time" that `add-eval-harness` predicted.

Because the OPSX verify gate grades every skill-content change against these keys, the red is inherited by changes that cannot have caused it. `generalize-fixture-publish-exemption` is stuck at 7/8 tasks on exactly this: its diff reworded a publish exemption and touched no detection path.

Each of the four extras has a *different* cause, and the fix belongs at a different altitude in each case. Triaging them together is what makes one change out of four symptoms.

## What Changes

**Two rubric anchors sharpened** (`references/goodness-rubric.md`, each with the before/after example the repo's editing rule requires):

- **AP-10 · BAU Dressed as OKR** — the detect line's "with no delta" clause is not operational, so BAU-*sounding* phrasing fires the anti-pattern even when the objective names a real change. The test becomes a property of the **objective's own statement**: AP-10 fires when the objective asserts continuation of the standing job and names no change; it does not fire when the objective names a change that at least one of its KRs realizes with a baseline→target pair. This is deliberately *not* a "do its KRs carry deltas" test — see below.
- **AP-01 · Task Masquerading as KR** — the detect line says nothing about a coverage denominator, leaving "Ship X to 100% of Y" undecidable. A **rescue clause** is added, not a new trigger: a delivery-verb KR is not AP-01 when it carries **either** a result measure someone outside the delivering team moves (adoption, usage, error rate) — with or without a baseline, since a missing baseline there is AP-04's business — **or** a baseline→target pair, including a coverage figure that moves from a stated starting point over a countable denominator. It fires only when the KR has *neither*. The disjunction is load-bearing: a single-limb version saying a coverage percentage of the team's own delivery never rescues was measured as a cross-fixture regression (`design.md` D3a) and is forbidden by this change's own `goodness-findings` delta. The trigger verb list is unchanged, so no KR that is silent today starts firing.

**Three fixture wordings corrected** (`examples/sample-portfolio.md`) — each an unplanted true defect or a non-defect whose text does not demonstrate what the key claims:

- **KR D2.1** — "Ship personalized onboarding checklists to 100% of new signups" is filed as non-defect N3 ("an adoption measure"), but 100% rollout coverage is satisfied by a feature flag; the reports flagging it are right and the key is wrong. Reworded so the KR keeps its delivery-verb near-miss character while its measure is one shipping alone does not satisfy — a support-ticket rate new signups move (see `design.md` D4a for why the adoption form D4 first proposed was dropped). N3's rationale is rewritten to match.
- **KR D1.1** — "Migrate 100% of product events to unified event schema v2" is a true AP-01 the key never planted, so it taxes the budget on every run that catches it. Reworded to an outcome the data's consumers experience, with the schema-v2 migration as the stated mechanism so answer-key row **A2** (AL-01, the unacknowledged pipeline dependency) keeps its evidence.
- **KR D2.2** — "Lift new-user activation rate to 35% via onboarding experiments" states no baseline: a true unplanted AP-04. Gains the same 31% baseline Growth states for the same metric, which leaves row **A4** (AL-03) intact and makes its 40%-vs-35% collision sharper, not weaker.

**Key and docs** (`evals/keys/sample-portfolio.json`, then `render-key --all`):

- N3's text rewritten against the new D2.1; a new intentional non-defect forbidding **AP-10 at Objective PL1**.
- Four triage entries (bucket, decision, rationale, status) recording each disposition, per `CLAUDE.md`.
- Row A2's note updated where it quotes D1.1's old "100%" phrasing.
- `README.md`'s "Known open item" bullet retires — AP-10 @ PL1 is the decision it was waiting for.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `goodness-findings`: adds requirements fixing the decision boundary of two anti-pattern detect rules — AP-10 against the objective's own statement, AP-01's rescue clause for delivery-verb KRs — so two independent readers reach the same verdict on the cases that currently split.
- `eval-fixtures`: fixture 1 must plant no defect its key does not declare, and each intentional non-defect's text must actually demonstrate the property its rationale claims; the four dispositions are recorded as triage entries.

## Impact

- `references/goodness-rubric.md` — AP-01 and AP-10 entries: detect line plus a before/after example each.
- `examples/sample-portfolio.md` — three KR lines in the Data team section (D1.1, D2.1, D2.2), plus the regenerated `## Answer key` section.
- `evals/keys/sample-portfolio.json` — N3 text, one new non-defect row, four triage entries, A2's note.
- `README.md` — the "Known open item" roadmap bullet.
- `examples/sample-portfolio-2.md` — KR AC3.2, one line, plus its regenerated `## Answer key` section; `evals/keys/sample-portfolio-2.json` — triage entry T1.
- `evals/grader/selftest/cases/non-defect-violation/report.md` and its generator constant in `evals/grader/selftest/gen_cases.py` — one quoted span, kept in step so a regeneration cannot silently re-break the case. The selftest's frozen key points at the **live** fixture, so this case's report quotes D2.1's replaced text and its anchor stops resolving. The case's purpose is unchanged; only the quote is refreshed. (Discovered during apply — the selftest corpus is coupled to fixture 1's text, which this change is the first to exercise.)
- Not touched: `SKILL.md`, `references/alignment-taxonomy.md`, `references/report-format.md`, `evals/grader/harness.py`, `evals/prompts/`. (`examples/sample-portfolio-2.md` and its key **are** touched — see the scope-widening note under Non-goals.)

**Planted defects newly caught: none.** This change is precision-only — it stops false positives and removes unplanted true defects. The proposal rule's disclosure requirement is satisfied vacuously, and the eval exists here to prove nothing regressed. The **recall guard is the acceptance test**: if any planted defect's hit count drops against the committed batches, the AP-01 or AP-10 edit is too tight and the change is wrong.

**Cross-fixture hazard, checked.** AP-10 is planted in fixture 2 as row **G4** — Core Systems Objective CS1, "Continue running the platform smoothly for every team" — whose KRs *do* carry real deltas (`Sev-1 incidents 9 → ≤ 4`, `Cloud cost per completed delivery $0.42 → $0.30`). A naive "does the KR set carry a delta?" test would have silently destroyed that planted defect. Testing the **objective statement** separates the two correctly: CS1 names no change and still fires; PL1's "Keep the lights on, **cheaper**" names one that KR PL1.2 realizes ($4.10 → $3.20) and stops firing. AP-01 and AP-04 are fixture 1's territory (fixture 2's key lists both under "not covered"), so `fixture2-portfolio` runs as the regression control.

## Non-goals

- **Scope widened during apply, with the owner's approval (2026-09-10).** The acceptance batch left `fixture2-portfolio` at 4/5 on `AP-12@KR AC3.2` ×3 — an unplanted true defect of exactly the class this change fixes on fixture 1. Fixture 2's KR AC3.2 is reworded and the disposition recorded as triage entry T1 in its key. `AL-05@Objective CR2` (×2) and `AL-10@KR DS2.2` (×1) are analysed in `design.md` D5a and deliberately left: both sit inside the budget, and the CR2 fix would require naming a mechanism on the Courier page, which would destroy planted defect **G2** (AP-07, whose detection requires no mechanism anywhere on that page).
- Not raising any budget, adding a known-red triage entry to absorb an extra, or otherwise loosening the criterion to reach green. Every disposition here changes the thing that was actually wrong.
- Not renumbering, renaming, or adding an AP-XX or AL-XX ID.
- Not touching `SKILL.md`, the alignment taxonomy, the report format, or the harness.
- Not touching fixture 2's planted rows, its other non-defects, or any AL-XX detection heuristic.
- Not attempting the roadmap work (single-team depth parity, drift tracking, the calibration set) or the deferred artifact-lifecycle behavioral eval.
- Not re-running or re-grading the committed batches under `evals/runs/`: they remain valid records of the key they were graded against, and this change makes them a *non-comparable* baseline for fixture 1 by design.
