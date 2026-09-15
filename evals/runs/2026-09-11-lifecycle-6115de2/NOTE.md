# Lifecycle batch — the artifact-lifecycle contract, executed

Five runs, one per decision path the contract defines, each a fresh subagent running the skill against a
scratch corpus with a publish seam standing in for the artifact surface. Graded by
`python3 evals/grader/harness.py lifecycle-grade --batch-dir evals/runs/2026-09-11-lifecycle-6115de2`
(deterministic, stdlib-only, no model tokens; exits non-zero if any scenario fails).

| scenario | seeded state | what the run did | verdict |
|---|---|---|---|
| `create` | no registry | created one artifact per key and registered both with all five fields | PASS |
| `update` | two live entries | updated both at their registered URLs; URLs, titles and favicons unchanged; timestamps advanced | PASS |
| `recreate` | one dead URL, one live | verified the dead URL, published one replacement, overwrote the entry, reported the re-create and its reason; updated the other in place | PASS |
| `adopt` | a stale entry plus a user-supplied URL | recorded the supplied URL under the key, overwriting the prior entry, and updated that artifact | PASS |
| `fixture-exempt` | same seam, same working folder, **a fixture as the corpus** | published nothing, wrote no registry, and said why | PASS |

The counter-test lives in `evals/runs/2026-09-11-lifecycle-broken-skill/` — the same `update` scenario against a
deliberately broken skill snapshot, which forks both keys and is graded red.

## Provenance notes, stated rather than hidden

- **The corpus's header note was reworded after the four publishing runs executed.** The edit replaced one sentence
  inside line 3 — the "Fictional scratch corpus" note — so the OKR content, its line numbers and every source ref in
  the runs' reports are unchanged. Grading never reads the corpus (it reads the run directory), so no verdict depends
  on it. `batch.json`'s per-scenario `corpus_hashes` were introduced after that edit and therefore record the current
  file; this note is the record of the change itself.
- **`adopt` and `fixture-exempt` were re-run** after their declarations changed (a prior-cycle output seeded into
  `adopt`; deliverables corrected and the prompt made exemption-neutral for `fixture-exempt`). The grader had failed
  the stale `adopt` run rather than reinterpreting it, which is the behaviour to keep.
- The four publishing prompts render byte-identically under the final template, so the template edits made during
  repair changed nothing any of them was asked.
