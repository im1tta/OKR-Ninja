# Tasks — artifact-lifecycle-contract

## 1. Contract in report-format.md

- [x] 1.1 Add a top-level "Artifact lifecycle" section to `references/report-format.md` (after §6) containing: the per-portfolio `artifacts.json` registry as source of truth, a concrete JSON example with keys `portfolio-dashboard` / `team-report/<team>` and fields `url`, `title`, `favicon`, `last_published`, `cycle_date`; verify the section and example exist and field names match the spec.
- [x] 1.2 In the same section, write the ordered publish decision procedure (adopt user-supplied URL → read registry → verify registered URL → update in place / re-create + overwrite entry + report / create + register), the never-silently-fork rule, the title/favicon stability rule, the single-run-per-folder assumption, the local dated append-only history rule, and the fixture/eval never-publish exemption; verify each spec requirement maps to explicit contract text.

## 2. Procedure step in SKILL.md

- [x] 2.1 Add "Step 7 — Publish" to `SKILL.md` (≤8 lines) that skips publishing for fixture/eval runs and otherwise defers to the "Artifact lifecycle" section of `references/report-format.md` by name; verify SKILL.md stays under 150 lines and duplicates no contract detail.

## 3. Verify-gate extension

- [x] 3.1 Add two structural-check bullets to `.claude/skills/openspec-loop/phases/verify-gate.md`: (a) `references/report-format.md` contains the "Artifact lifecycle" contract section, (b) SKILL.md's publish step references it; verify by reading the updated gate text.
- [x] 3.2 Add a "future work" note in `verify-gate.md` recording the deferred behavioral eval (pre-seeded registry, grade update-vs-create); verify the note names the deferred test explicitly.

## 4. Consistency check

- [x] 4.1 Cross-check CLAUDE.md file-ownership rules still hold (contract only in report-format.md; no severity/rubric/taxonomy content touched) and that all cross-file references resolve; verify with a grep for "Artifact lifecycle" showing exactly one defining home plus pointers.
