# Tasks: add-second-eval-fixture

## 1. Author the fixture body

- [x] 1.1 Write `examples/sample-portfolio-2.md` header + company priorities page (Coppervale, Q1 2027, C1–C4 per design D1/D2, including C2's two named drivers) and verify no company/team/person name from it appears in `references/` or `examples/sample-portfolio.md` (grep for each invented proper noun).
- [x] 1.2 Write the five team pages (Dispatch, Courier, Core Systems, Insights, Accounts) planting all 13 defects exactly per design D2 — commitment-convention line on every page except Courier, per-KR owners only on Insights — and verify each of the 13 modes has its triggering text present and quotable (line-check each D2 row against the draft). (Driver-app team named "Courier" instead of design's "Mobile" — the bare word "mobile" appears in `references/`, failing the name-independence grep.)
- [x] 1.3 Write the appendix (Q4 2026 business-review extracts) carrying the AL-09 counter-baseline and any baseline a clean KR cites externally, and verify every two-sided defect (A1, A2, A3, A4 edges, A5) has verbatim quotable text on both sides.

## 2. Self-audit against the full catalog

- [x] 2.1 Sweep the drafted fixture body against all 15 AP modes and all 12 AL modes (design D3 rules 1–4): confirm each of the 13 planted modes fires exactly once, and fix any line where an off-key mode (AP-01/02/03/04/06/09/14, AL-01/02/03/04/06/07/10) is triggerable — verify by recording a 27-row pass/fail sweep note in the change dir (`audit-sweep.md`). (Two hardening edits applied: C1/C4 name their workstreams; non-defect #8 pins cycle-edge label ambiguity to G3.)
- [x] 2.2 Verify defensively-armored properties hold: every clean KR has baseline→target+unit+source+owner-resolvable, all dependency edges undated and producer-acknowledged, every objective traces to a C-priority, all four C-priorities covered, only the two designed metric collisions exist (D3) — corrections applied to the draft.

## 3. Answer key and eval sections

- [x] 3.1 Append the answer key (13 rows, G1–G8/A1–A5, canonical "AP-XX/AL-XX · name" spelling per the owning reference files), the intentional non-defects list (including the pinned "not AL-09" and "not AP-04" near-misses per D3.5 and the AP-07/AP-08 counted-separately note), the modes-deliberately-not-covered list (the 14 fixture-1 modes), and the eval criterion (all 13 by canonical ID, zero fabricated quotes, budget 2) — verify every quoted span in the key exists character-for-character in the fixture body and every canonical name matches the owning file's spelling exactly.

## 4. Doc updates

- [x] 4.1 Update `CLAUDE.md` (examples/ file-map row + "Testing changes" steps reference both fixtures, grading against the fixture(s) covering the touched modes) and verify no other CLAUDE.md content changed.
- [x] 4.2 Update `README.md` (repository layout tree, one usage line for fixture 2, roadmap "More fixtures" item trimmed to remaining scale-fixture work) and verify links/paths resolve.
- [x] 4.3 Update `.claude/skills/openspec-loop/phases/verify-gate.md` fixture-eval wording to run the fixture(s) under `examples/` whose answer keys cover the touched category, and verify the gate's other rules are untouched.

## 5. Validation

- [x] 5.1 Run `openspec validate --change add-second-eval-fixture` (strict if available) and verify it passes.
- [x] 5.2 Verify fixture 1 is byte-identical (`git diff --stat examples/sample-portfolio.md` empty) and structural checks hold: SKILL.md untouched and under ~150 lines, every referenced path resolves, no reference-file content duplicated into the fixture.
