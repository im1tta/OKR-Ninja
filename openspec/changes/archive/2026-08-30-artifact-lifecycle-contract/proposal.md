# Proposal — artifact-lifecycle-contract

## Why

In the predecessor project (MDPI OKR & KPI Review), review runs published their dashboards and reports as Claude artifacts with no rule for locating the existing artifact: some runs updated it in place, others created a duplicate. The output history became inconsistent and hard to trust. OKR-Ninja currently has no artifact-publishing contract at all, so it would inherit the same drift.

## What Changes

- Add a deterministic **artifact-lifecycle contract** to `references/report-format.md`: a per-portfolio `artifacts.json` registry in the review working folder is the single source of truth mapping each deliverable to its living artifact URL.
- One **living artifact per deliverable type** (`portfolio-dashboard`; `team-report/<team>` when produced), updated in place every run; a new artifact is created only for a genuinely new deliverable (and its URL immediately registered).
- Registry entry fields: stable key, artifact URL, title, favicon, last-published timestamp, cycle date. Title and favicon stay stable across republishes.
- **Self-healing rules**: verify the registered URL before updating; if the artifact is gone, re-create, overwrite the entry, and report the re-create (and why) in the run summary; adopt a user-supplied artifact URL into the registry; never silently fork a second artifact when a registry entry exists.
- **History stays local**: dated, append-only cycle outputs remain the audit trail; the artifact is only the living view.
- Add a **publishing step to SKILL.md** (after Step 6 — Report) that references the registry contract in `references/report-format.md`.
- **Fixture exemption**: eval runs against `examples/sample-portfolio.md` never publish artifacts or write a registry.
- Extend the OPSX **verify-gate structural checks**: the contract sections must exist in `references/report-format.md`, and SKILL.md's publishing step must reference the registry.
- Note (not build) the deferred **behavioral eval**: a pre-seeded-registry test grading update-vs-create behavior.

## Capabilities

### New Capabilities
- `artifact-lifecycle`: how OKR-Ninja publishes and re-publishes its report deliverables as artifacts — registry as source of truth, update-in-place semantics, self-healing recovery, local append-only history, and the fixture publishing exemption.

### Modified Capabilities

(none — no existing spec directories; this is the first capability spec in the repo)

## Non-goals

- No changes to detection behavior, the rubric, the taxonomy, or the report's six sections — no planted defects are newly caught by this change.
- No changes to the predecessor MDPI project; its format is superseded, not migrated.
- No okr-deepdive changes; it may adopt the same registry schema later in its own repo.
- No behavioral eval implementation (pre-seeded registry update-vs-create test) — recorded as deferred future work only.
- No writing to Confluence/Jira; the skill stays read-only against sources.

## Impact

- `references/report-format.md` — gains the artifact-lifecycle contract (registry schema, update semantics, self-healing, fixture exemption).
- `SKILL.md` — gains a short publishing step referencing the contract; must stay under ~150 lines.
- `.claude/skills/openspec-loop/phases/verify-gate.md` — structural checks extended.
- No code, build, or fixture changes.
