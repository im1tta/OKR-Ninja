## Purpose

Defines how OKR-Ninja publishes its report deliverables as artifacts deterministically: a per-portfolio registry is the source of truth, each deliverable has one living artifact updated in place, recovery from registry/reality mismatches is prescribed and reported, and fixture/eval runs never publish.

## ADDED Requirements

### Requirement: Per-portfolio artifact registry is the source of truth
The skill SHALL maintain an `artifacts.json` registry at the root of the review working folder, one registry per portfolio. Every publish decision (update vs. create) SHALL be driven by this registry, not by artifact listing, title matching, or agent judgment. Each registry entry SHALL record: a stable deliverable key, the artifact URL, the artifact title, the favicon, the last-published timestamp, and the cycle date of the last publish.

#### Scenario: Existing entry drives an update
- **WHEN** a review run finishes its report and the registry has an entry for the deliverable's key
- **THEN** the run updates the artifact at the registered URL in place, keeping title and favicon unchanged, and refreshes the entry's timestamp and cycle date

#### Scenario: Missing entry drives a create-and-register
- **WHEN** a review run produces a deliverable whose key has no registry entry (including when no registry file exists yet)
- **THEN** the run creates a new artifact and immediately writes its key, URL, title, favicon, timestamp, and cycle date to the registry before the run ends

### Requirement: One living artifact per deliverable type
The skill SHALL publish exactly one living artifact per deliverable key — `portfolio-dashboard` for the portfolio report, and `team-report/<team>` for any per-team output it produces — updated in place on every run. The skill SHALL NOT create a second artifact for a key that already has a registry entry, except through the self-healing re-create path.

#### Scenario: Repeat run does not fork
- **WHEN** a second review cycle runs against the same portfolio working folder
- **THEN** the run republishes to the registered URLs and creates no new artifacts for already-registered keys

### Requirement: Self-healing on registry/reality mismatch
Before updating, the skill SHALL verify the registered URL still points to a reachable artifact the user owns. If it does not, the skill SHALL create a replacement artifact, overwrite the registry entry, and state in the run summary that a re-create happened and why. If the user supplies an artifact URL for a deliverable, the skill SHALL adopt it into the registry instead of creating a new artifact. The skill SHALL NOT silently create a duplicate when a registry entry exists: any create performed while an entry existed MUST be reported in the run summary.

#### Scenario: Dead registered URL
- **WHEN** the registry names a URL whose artifact no longer exists or cannot be updated
- **THEN** the run creates a replacement, overwrites the entry with the new URL, and reports the re-create and its reason in the run summary

#### Scenario: User supplies the artifact URL
- **WHEN** the user provides an existing artifact URL for a deliverable (with or without a registry present)
- **THEN** the run records that URL under the deliverable's key and updates that artifact rather than creating a new one

### Requirement: Local cycle outputs are the append-only history
Run outputs written to the working folder SHALL be dated and append-only — a run SHALL NOT overwrite a prior cycle's local outputs. The living artifact is only the current view; cross-cycle comparisons derive from the local cycle files.

#### Scenario: New cycle preserves prior local outputs
- **WHEN** a new review cycle writes its outputs to the working folder
- **THEN** prior cycles' dated files remain unmodified and the new outputs are written under the new cycle's date

### Requirement: Fixture and eval runs never publish
A run against the test fixture (`examples/sample-portfolio.md`) or any eval run SHALL NOT publish or update artifacts and SHALL NOT create or modify a registry file.

#### Scenario: Fixture eval stays hermetic
- **WHEN** the skill is run against `examples/sample-portfolio.md` for evaluation
- **THEN** no artifact is published or updated and no `artifacts.json` is written

### Requirement: Verify gate checks the contract structurally
The project quality gate SHALL fail when the artifact-lifecycle contract sections are absent from `references/report-format.md` or when SKILL.md's publishing step does not reference the registry contract.

#### Scenario: Contract section removed
- **WHEN** the structural checks run and `references/report-format.md` lacks the artifact-lifecycle contract or SKILL.md's publishing step no longer references it
- **THEN** the gate reports red
