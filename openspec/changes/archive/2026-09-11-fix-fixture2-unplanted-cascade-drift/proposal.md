## Why

`examples/sample-portfolio-2.md` contains two instances of AL-05 Cascade drift and its key plants one. The planted row is **A1** (Core Systems Objective CS2 ↔ Company C2). The unplanted one is Courier Objective CR2 ↔ Company C3: CR2 declares *(supports C3)*, C3's only metric is driver-app weekly retention, and CR2's only KR — "Driver referral installs 3,000 → 45,000 this quarter" — is an acquisition measure that moves no retention rate. It is the same shape as A1 and it is a defensible detection. It is also persistent and skill-state-dependent rather than a flake: **5 of 5** runs in `2026-09-10-candidate-5beed03`, 2 of 5 in `2026-09-10-candidate-repair1`, 1 of 5 in `2026-09-10-candidate-repair2`, 1 of 1 in `2026-09-10-smoke-verify`, and 1 of 5 back in `2026-09-09-candidate-opus-8d1cb12`. Every run that catches it correctly pays extras budget for being right.

That is exactly what `openspec/specs/eval-fixtures/spec.md` forbade on 2026-09-10: "A fixture plants no defect its key does not declare." The change that wrote that requirement analysed this very instance (`openspec/changes/archive/2026-09-10-fix-fixture1-precision-extras/design.md` § D5a) and deliberately left it, because every lever it weighed cost a planted defect: naming the install→retention link on the Courier page destroys **G2** (AP-07 Unmoored Moonshot, which requires that page to state no "how"), no company priority C1–C4 is moved by referral installs, and planting the row is barred by the recall asymmetry. The lever D5a did not weigh is the one AL-05's own heuristic offers: the *parent's* page.

## What Changes

- **Company priority C3 names its second contributing workstream.** C3 gains driver-to-driver referral growth as a documented retention driver, in the `driven primarily by …` style C2 already uses. AL-05's mechanism check asks whether the child KRs measure "the parent's metric, **a documented driver of it**, or a deliverable the parent's own page names as needed" — the edit satisfies that second branch on the parent's page, where AP-07 does not look.
- **Intentional non-defect N9** is added to `evals/keys/sample-portfolio-2.json`: AL-05 is forbidden at `Objective CR2`. CR2 remains a genuine near-miss after the edit — an acquisition-only KR under a retention priority — so the row measures false-positive discipline, and a future edit that strips the documented driver from C3 surfaces as a named violation rather than being absorbed by the budget.
- **Triage entry T2** records the disposition (bucket `fixture-ambiguous`, status `fixed`), the run-count evidence, and why the three rejected levers were rejected.
- The fixture's generated `## Answer key` section is regenerated with `render-key --all`.
- **No skill-content change.** No edit to `SKILL.md`, `references/goodness-rubric.md`, or `references/alignment-taxonomy.md`; no budget raised, no row widened, no key row added. Not breaking.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `eval-fixtures`: the "A fixture plants no defect its key does not declare" requirement gains the rule this instance exposes — when an unplanted defect arises from a link between two fixture pages and the child's text is load-bearing for another key row, the repair lands on the other side of the link rather than on the child.

## Impact

- `examples/sample-portfolio-2.md` — the C3 bullet on the company priorities page (one line), plus the regenerated `## Answer key` section. The Courier page is not touched.
- `evals/keys/sample-portfolio-2.json` — one `non_defects` entry, one `triage` entry. `budget` stays 2; `defects`, `criterion`, `not_covered` and `slices` are unchanged.
- `openspec/specs/eval-fixtures/spec.md` — the one requirement restated from the delta at archive time.
- No change to `evals/grader/harness.py`, and none to the selftest corpus. The grader's key-resolution precedence (`harness.py:1533`) prefers `evals/grader/selftest/keys/` over the live `evals/keys/`, and that frozen fixture-2 snapshot carries N1–N8 with no triage entries — so N9 and T2 are invisible to `selftest`, as are the frozen `input.md` copies to the C3 edit. The corpus is insulated from key evolution by design; `selftest` exits 0 and its 39 cases are untouched.

Detection behavior is untouched, so the change should **newly catch no planted defect** in either fixture — the proposal rule's disclosure requirement is satisfied vacuously. The fixture eval exists here to prove a precision gain (`AL-05@Objective CR2` absent from the extras) with no recall loss: rows **G2**, **G3** and **A1** in particular must still be found in every run.

## Non-goals

- Not planting AL-05@CR2 as a key row. It fires in 1–2 runs of 5; the absolute criterion requires every planted row in every run, so a row would convert a bounded precision cost into an unbounded recall failure. The spec already settles this and the reasoning is not reopened.
- Not raising fixture 2's extras budget, widening any row's accepted IDs, or recording a `known-red` triage entry — all three tolerate the defect instead of fixing it.
- Not editing the Courier page in any way: not CR2's objective statement, not CR2.1, not the notes line. G2, G3 and non-defect N1 all depend on that page as written.
- Not re-pointing or removing CR2's `(supports C3)` link — removal trips AL-04 Orphan objective, which is in fixture 2's not-covered list and would cost budget off-key.
- Not auditing the rest of fixture 2 (or fixture 1) for further unplanted instances; `AL-01@KR IN2.2` appeared in 1 run of 5 and is below every recurrence threshold this repo uses.
- Not touching the in-flight `generalize-fixture-publish-exemption` change, which is unrelated and awaiting its own smoke tier.
