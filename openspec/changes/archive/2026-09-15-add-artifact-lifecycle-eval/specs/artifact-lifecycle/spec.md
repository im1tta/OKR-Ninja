## MODIFIED Requirements

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

## ADDED Requirements

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
