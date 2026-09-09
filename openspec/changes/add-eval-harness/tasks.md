## 1. Canonical keys and generated answer-key sections

- [x] 1.1 Author `evals/keys/sample-portfolio.json` by transcribing the current markdown key (14 defects, 6 non-defects, not-covered list, budget 2, criterion, Platform slice) with accepted IDs primary-first and evidence anchors per design D3; verify `python3 -m json.tool` parses it and a row-by-row comparison shows the same 14 + 6 IDs and notes as the markdown tables
- [x] 1.2 Author `evals/keys/sample-portfolio-2.json` the same way (13 defects, 8 non-defects, not-covered list, budget 2, criterion); verify parse plus the same 13 + 8 row comparison
- [x] 1.3 Add `reference_overlap` flags to fixture-1 rows G1, G5 and A1 pointing at the `references/report-format.md` examples, and decide A2 and A5 per design D14 by reading the §1 and §6 examples; verify every flag's pointer resolves to a line of `references/report-format.md` containing the quoted example text
- [x] 1.4 Implement `harness.py check` (key schema, anchor resolution to exactly one line or heading, full-catalog coverage AP-01–AP-15 and AL-01–AL-12 across keys, triage rules incl. no `skill-error` + `known-red` and rationale required); verify it exits 0 on both keys and exits 1 on the recovered corrupted key with the row and marker named
- [x] 1.5 Implement `harness.py render-key` and regenerate both fixtures' `## Answer key` sections per design D4; verify the diff preserves every ID, quote and note (formatting-only), `check` reports fresh afterwards, and a one-character manual edit below the heading makes `check` fail

## 2. Grader

- [x] 2.1 Implement the slicer inside `plan` (strip the answer-key section; keep the H1 plus listed H2 sections for a slice); verify the fixture-1 portfolio input contains no "Answer key" text and the Platform slice contains exactly the H1, the Platform section and the Appendix section
- [x] 2.2 Implement the finding parser with dash/arrow/quote normalisation and the evidence-versus-mention split per design D6; verify parsed finding counts on the nine scratch reports equal their mandated-heading counts (17/18/16, 15/17/14, 6/6/7)
- [x] 2.3 Implement quote classification (verbatim, near-miss, out-of-scope, fabricated, plus the `key-leak` flag); verify with one selftest mini per class that each span lands in its expected class and only fabricated fails the run
- [x] 2.4 Implement row matching, duplicates, extras, non-defect violations, off-key flags, known-red exclusion and the pass verdict per design D7; verify with selftest minis covering accepted-alternate ID, same ID at two locations, cross-source partial match (G5), one KR under three IDs, known-red exclusion, and budget exceeded
- [x] 2.5 Implement structural checks per mode; verify a portfolio mini with a twelfth heatmap column fails naming the column, a single-team mini with an AL block fails naming the block, and a compliant single-team mini passes with O4 N/A and the out-of-scope statement
- [x] 2.6 Implement `grade` output with full provenance (skill SHA and dirty flag, model, prompt hash, key hash, slice, arm, start, wall time, tokens or null); verify grade.json carries every field for a run with `run.json` tokens and for one without
- [x] 2.7 Assemble `evals/grader/selftest/` (recovered minis and corrupted key, the new minis from 2.3–2.5, the nine scratch reports with source-ref paths rewritten to selftest input copies, each with `expected.json`); verify `harness.py selftest` exits 0 and that flipping one expected value makes it exit 1

## 3. Batch orchestration

- [x] 3.1 Write `evals/prompts/portfolio.md` and `evals/prompts/single-team.md` with placeholders and the frozen preamble per design D10; verify rendering for each slice yields the batch's paths and the template hash is identical across two renders
- [x] 3.2 Implement `plan` (batch directory and `batch.json`, baseline snapshot via `git archive`, candidate snapshot from the working tree with SHA and dirty flag, prompts, resume skip); verify a second `plan` on the same batch creates nothing new and lists only pending runs, and that a run whose report is missing is reported as not produced
- [x] 3.3 Implement `aggregate` producing `scorecard.json` and a printed markdown table (rows with hit and ID-exact counts and caveats, extras frequency by ID and anchor with kind and exclusion, violations, quote classes, structure, cost, mixed-model warning); verify on a synthetic batch assembled from selftest grades that every count equals a hand-computed value
- [x] 3.4 Implement `compare` with the regression rule and model-mismatch refusal per design D11; verify with synthetic scorecards that a one-hit drop yields no regression, an extra in four candidate runs versus one baseline run yields a named regression, and differing model IDs exit with an error
- [x] 3.5 Write `.claude/commands/okr-eval.md` (smoke, baseline, decision; plan, Agent runs at most five concurrent, `run.json` after each, grade, aggregate, compare, print) per design D8; verify `/okr-eval smoke fixture2-portfolio` runs end to end and produces a grade and a scorecard in the batch directory

## 4. Baseline batch

- [x] 4.1 Run `/okr-eval baseline` against `main` (5 runs per slice, 15 runs, single arm); verify all 15 reports exist, every grade carries provenance, and the scorecard prints without a mixed-model warning
- [x] 4.2 From the baseline scorecard, draft triage proposals for every extra or duplicate key present in three or more runs (bucket plus rationale, no status) and present them to the user one at a time for confirmation; verify only confirmed entries carry `known-red`, no `skill-error` entry does, and `check` passes on the updated keys
- [x] 4.3 Regenerate both answer-key sections after triage and commit `evals/runs/<batch>/` with prompts, reports, `run.json`, grades and scorecard; verify `git ls-files evals/runs` lists no `input/` or `skill/` paths

## 5. Gate wiring and documentation

- [x] 5.1 Update the fixture-eval bullet in `.claude/skills/openspec-loop/phases/verify-gate.md` per design D12; verify the bullet invokes `/okr-eval smoke`, keeps the fixture-selection language, the docs-only skip and the honesty rules, and every path it mentions resolves
- [x] 5.2 Update `CLAUDE.md` (file-map row for `evals/` naming the JSON keys as the answer keys' owner, and testing steps pointing at `/okr-eval`, `harness.py check` and `selftest`); verify `git diff --stat` shows `SKILL.md` and `references/` untouched and the file map still lists one owner per topic
- [x] 5.3 Update the README roadmap line for the CI eval harness and add `evals/runs/**/input/` and `evals/runs/**/skill/` to `.gitignore`; verify `git status --ignored` shows those directories ignored and `evals/scratch/` still ignored
- [ ] 5.4 Final verification: run `harness.py check`, `harness.py selftest`, `openspec validate add-eval-harness --strict`, and `/okr-eval smoke` on both portfolio slices and the Platform slice; verify all exit green and the scorecard's excluded findings are exactly the confirmed triage entries
