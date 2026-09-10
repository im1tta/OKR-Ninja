# artifact-lifecycle Specification (delta)

## MODIFIED Requirements

### Requirement: Fixture and eval runs never publish

A run against **any of this skill's own fixtures** — the files under the `examples/` directory that ships with the skill — or any eval run, SHALL NOT publish or update artifacts and SHALL NOT create or modify a registry file. The exemption SHALL be expressed as this scope rather than as a list of fixture filenames, so that adding a fixture never narrows it. It SHALL turn on the corpus being one of those fixture files — exempt whether read from an installed skill, a symlink, or a working checkout — and never on the path the corpus occupies, so that a user's own OKR exports are outside it even when they sit in a folder named `examples/`. `SKILL.md`'s publish step and `references/report-format.md`'s "Fixture/eval exemption" SHALL state this same scope, with `SKILL.md` pointing at the report-format section rather than restating the contract.

#### Scenario: Fixture eval stays hermetic

- **WHEN** the skill is run against any of this skill's own fixtures for evaluation
- **THEN** no artifact is published or updated and no `artifacts.json` is written

#### Scenario: A manual run against a fixture not named anywhere

- **WHEN** a user runs the skill by hand against one of its fixtures with a prompt that never says "eval" — e.g. "review the OKRs in `examples/sample-portfolio-2.md`" typed in a working checkout to demo the skill or spot-check a change without the harness, while the skill itself was installed elsewhere by copy or as a plugin
- **THEN** the run is still exempt and publishes nothing, because the exemption turns on the corpus being one of the skill's fixtures rather than on the run being labelled an eval or on which copy of the fixture was read

#### Scenario: A newly added fixture is covered on arrival

- **WHEN** a third fixture is added under the skill's `examples/` directory and the skill is run against it before any other file mentions it
- **THEN** it is exempt from publishing with no edit to `SKILL.md`, `references/report-format.md`, or this spec

#### Scenario: A user's own exports are not exempt for sitting in an `examples/` folder

- **WHEN** a user points the skill at their own OKR exports, which happen to be held in a subdirectory they named `examples/`
- **THEN** the run publishes per the registry procedure as normal, because the exemption names the skill's own fixture files and not any path ending in `examples/`
