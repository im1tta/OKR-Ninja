# artifact-lifecycle Specification

## Purpose

Defines how OKR-Ninja publishes its report deliverables as artifacts deterministically: a per-portfolio registry is the source of truth, each deliverable has one living artifact updated in place, recovery from registry/reality mismatches is prescribed and reported, fixture runs never publish, and no eval run touches the real artifact surface — though one given a publish seam executes the whole procedure against it, which is how the contract is tested.

## Requirements

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

A run against **any of this skill's own fixtures** — the files under the `examples/` directory that ships with the skill — SHALL NOT publish or update artifacts and SHALL NOT create or modify a registry file. The exemption SHALL be expressed as this scope rather than as a list of fixture filenames, so that adding a fixture never narrows it. It SHALL turn on the corpus being one of those fixture files — exempt whether read from an installed skill, a symlink, or a working checkout — and never on the path the corpus occupies, so that a user's own OKR exports are outside it even when they sit in a folder named `examples/`.

No **eval run** SHALL touch the real artifact surface: it SHALL NOT publish, update, or read artifacts there, and SHALL NOT create or modify any registry file outside its own run directory. An eval run against a non-fixture corpus MAY execute the publish decision procedure against a supplied publish seam, as the "Eval runs execute the contract through a publish seam" requirement defines; a run against a fixture stays exempt whether or not a seam is supplied.

`SKILL.md`'s publish step and the two exemption paragraphs of `references/report-format.md` — **"Fixture exemption"** (the fixture arm) and **"Eval runs and the publish seam"** (the eval arm) — SHALL state this same scope, with `SKILL.md` pointing at the "Artifact lifecycle" section rather than restating the contract.

#### Scenario: Fixture eval stays hermetic

- **WHEN** the skill is run against any of this skill's own fixtures for evaluation
- **THEN** no artifact is published or updated and no `artifacts.json` is written

#### Scenario: A fixture run is exempt even when a seam is supplied

- **WHEN** an eval run supplies a publish seam and a working folder but its corpus is one of the skill's own fixtures
- **THEN** the run publishes nothing through the seam and writes no registry, because the fixture arm of the exemption is unconditional

#### Scenario: A manual run against a fixture not named anywhere

- **WHEN** a user runs the skill by hand against one of its fixtures with a prompt that never says "eval" — e.g. "review the OKRs in `examples/sample-portfolio-2.md`" typed in a working checkout to demo the skill or spot-check a change without the harness, while the skill itself was installed elsewhere by copy or as a plugin
- **THEN** the run is still exempt and publishes nothing, because the exemption turns on the corpus being one of the skill's fixtures rather than on the run being labelled an eval or on which copy of the fixture was read

#### Scenario: A newly added fixture is covered on arrival

- **WHEN** a third fixture is added under the skill's `examples/` directory and the skill is run against it before any other file mentions it
- **THEN** it is exempt from publishing with no edit to `SKILL.md`, `references/report-format.md`, or this spec

#### Scenario: A user's own exports are not exempt for sitting in an `examples/` folder

- **WHEN** a user points the skill at their own OKR exports, which happen to be held in a subdirectory they named `examples/`
- **THEN** the run publishes per the registry procedure as normal, because the exemption names the skill's own fixture files and not any path ending in `examples/`

#### Scenario: An eval run never reaches the real artifact surface

- **WHEN** any eval run reaches its publish step, with or without a seam
- **THEN** it publishes, updates and reads nothing on the real artifact surface and writes no registry file outside its own run directory

### Requirement: Eval runs execute the contract through a publish seam

An eval run whose prompt supplies a **publish seam** — a local command standing in for the artifact surface — together with a review working folder inside the run's own directory SHALL follow the publish decision procedure unchanged, publishing through that seam and writing that working folder's `artifacts.json`. Every decision the contract specifies SHALL be made exactly as it would against the real artifact surface: adopt a user-supplied URL, read the registry, verify the registered URL through the seam, update in place or re-create or create-and-register, refresh the timestamps, report any create performed while an entry existed, and never fork a second artifact for a registered key. The seam SHALL be the only publish target such a run uses.

#### Scenario: Seam run updates the registered artifact

- **WHEN** an eval run is given a seam, a working folder, and a registry whose entry names a URL the seam reports reachable
- **THEN** the run updates that URL through the seam, leaves the entry's URL, title and favicon unchanged, refreshes its `last_published` and `cycle_date`, and creates no artifact

#### Scenario: Seam run re-creates a dead artifact and says so

- **WHEN** the registry names a URL the seam reports unreachable
- **THEN** the run publishes a replacement through the seam, overwrites the entry with the new URL, and states in its run summary that a re-create happened and why

#### Scenario: Seam run adopts a user-supplied URL

- **WHEN** the run's prompt supplies an artifact URL for a deliverable whose key already holds a different entry
- **THEN** the run records the supplied URL under that key, overwriting the prior entry, and updates that artifact rather than creating one

### Requirement: Verify gate checks the contract structurally
The project quality gate SHALL fail when the artifact-lifecycle contract sections are absent from `references/report-format.md` or when SKILL.md's publishing step does not reference the registry contract.

#### Scenario: Contract section removed
- **WHEN** the structural checks run and `references/report-format.md` lacks the artifact-lifecycle contract or SKILL.md's publishing step no longer references it
- **THEN** the gate reports red
