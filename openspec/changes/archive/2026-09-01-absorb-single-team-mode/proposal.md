# Proposal: Absorb single-team mode (closed skill, no okr-deepdive dependency)

## Why

OKR-Ninja currently depends on an external sibling skill, `okr-deepdive`, in seven files: the frontmatter description routes every single-team ask to it, the procedure stops and recommends it, and report §6's best outcome is a prompt for a skill this repo neither ships nor controls. The repo owner has decided the skill must be **closed and self-contained** — installable and fully useful on its own — and that single-team OKR review becomes a first-class mode of this skill rather than a referral.

## What Changes

- **BREAKING (routing):** the frontmatter `description` claims BOTH portfolio and single-team OKR review. Single-team prompts ("review the Payments team's OKRs") now trigger this skill instead of being excluded. The "not for writing new OKRs from scratch" exclusion stays.
- **Mode switch in scope intake (SKILL.md Step 1):** exactly 1 team in scope → **single-team mode**; 2+ teams → **portfolio mode** (existing behavior, unchanged). Replaces the "stop and recommend `okr-deepdive`" rule.
- **Single-team mode reuses existing machinery at full depth:** exhaustive O1–O4/K1–K7 scoring of every objective/KR (portfolio mode's screening depth stays as-is), full AP-XX sweep, a concrete rewrite for every Critical/Major finding, strategy trace vs a company strategy doc when provided. AL-XX cross-team analysis does **not** run — one team cannot supply both sides' verbatim quotes; outbound dependency mentions are captured as clearly-labeled notes, not findings.
- **Report contract (references/report-format.md):** a new single-team report template (same severity scale, source-ref format, evidence invariant). Portfolio report §6 "Suggested deep dives" is rewritten from "run `okr-deepdive`" to an internal mode-switch recommendation — "re-run this skill on team X alone" — keeping the same computed criteria (roll-up grade at/below the needs-rework threshold, or any Critical finding).
- **okr-deepdive naming removed repo-wide** (SKILL.md, CLAUDE.md, README.md, references/goodness-rubric.md, references/report-format.md, openspec/config.yaml, .claude/skills/openspec-loop/phases/refine.md). `openspec/changes/archive/` is historical record and is not touched.
- **Repo rules flipped:** CLAUDE.md's purpose line, the editing rule that mandated the okr-deepdive disambiguation, and routing-test step 4 (a single-team prompt must now trigger the skill). README's "How it relates to okr-deepdive" section becomes a two-mode scope section.
- **Eval:** a single-team-mode eval slice appended to one existing fixture's answer key — running one already-planted team alone must find exactly that team's goodness defects, zero alignment findings, zero fabricated quotes.
- **README Roadmap** gains the follow-up project: depth-parity gaps vs the retired companion (tracking-continuity and claimed-vs-actual dimensions, a computed /100 headline score, deterministic check scripts, a dedicated single-team fixture).

## Capabilities

### New Capabilities

- `review-modes`: the two review modes (portfolio vs single-team), the team-count mode switch at scope intake, single-team mode's depth/exclusion behavior (full-depth goodness, no AL-XX analysis, outbound-dependency notes, optional strategy trace), the single-team report template, the §6 internal mode-switch recommendation, and the closed-skill invariant (no reference to external OKR skills anywhere outside `openspec/changes/archive/`).

### Modified Capabilities

- `eval-fixtures`: one fixture's answer key gains a single-team-mode eval slice (scoped team, expected defect IDs, zero-alignment-findings requirement, extra-findings budget) so the new mode has eval coverage without a new fixture file.

## Impact

- **Files edited:** `SKILL.md` (description + Steps 1/3/4/6 + Boundaries; stays ≤~150 lines), `references/report-format.md` (§6 rewrite + new single-team template section), `references/goodness-rubric.md` (line ~144 threshold wording repointed from okr-deepdive to the internal mode switch), `CLAUDE.md`, `README.md`, `openspec/config.yaml`, `.claude/skills/openspec-loop/phases/refine.md`, one fixture under `examples/` (answer-key addition only).
- **Detection behavior:** no new detection paths; no planted defect in `examples/sample-portfolio.md` is newly caught by this change. The single-team eval slice re-scopes already-planted goodness defects to a one-team run.
- **Frozen surfaces untouched:** AP-XX/AL-XX catalogs and IDs, severity scale definitions, source-ref format, evidence invariant, artifact-lifecycle registry contract (single-team reports already fit `team-report/<team>`).
- **Environment note (outside repo):** while the external okr-deepdive skill remains installed, both descriptions claim single-team prompts and router behavior is ambiguous until the companion is uninstalled/retired. Not addressable by repo content.

## Non-goals

- No new rubric dimensions, anti-patterns, or failure modes (tracking-continuity and claimed-vs-actual parity gaps are documented Roadmap follow-ups, not built now).
- No port of the okr-deepdive pipeline: no D1–D9 rubric, no /100 headline score, no Python scripts, no .docx output, no per-stage subagent files.
- No new fixture file; no changes to planted defects, answer-key budgets, or non-defect lists beyond the appended single-team slice.
- No edits to the installed okr-deepdive plugin or any file outside this repo.
- No changes to the artifact-lifecycle contract or the OPSX toolchain beyond the two workflow-context lines already listed.
