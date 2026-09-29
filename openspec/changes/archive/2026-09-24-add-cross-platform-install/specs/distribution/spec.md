## Purpose

Defines how OKR-Ninja is shipped to the agent platforms that run it: exactly which files make up the skill, the frontmatter check that keeps it uploadable, the two packages built for upload and plugin hosts, the installer for platforms that read skill folders, and the documented install route per platform.

## ADDED Requirements

### Requirement: The runtime payload is the whole shipment
The skill SHALL ship as exactly its runtime payload: `SKILL.md` plus every regular file under `references/` and `examples/`, at the same relative paths. Hidden files (names beginning with `.`), Windows folder metadata (`Thumbs.db`, `desktop.ini`) and Python bytecode caches SHALL be excluded. A folder under `references/` or `examples/` that cannot be read SHALL stop the build or the install with a non-zero exit rather than be skipped, and the payload SHALL be read in full before anything is written, so an unreadable file stops the run before any folder is created. No other repo content — `CLAUDE.md`, `README.md`, `install.py`, `evals/`, `openspec/`, `.claude/`, `dist/` — SHALL appear in an installed copy or a built package.

#### Scenario: Development files never ship
- **WHEN** the installer or the build runs from a checkout that also holds `CLAUDE.md`, `README.md`, `evals/`, `openspec/`, `.claude/` and a previous `dist/`
- **THEN** every installed copy and every package contains `SKILL.md`, the files under `references/` and the files under `examples/`, and no other file

#### Scenario: OS noise is dropped
- **WHEN** a `.DS_Store` file sits inside `references/` or `examples/`
- **THEN** it appears in no installed copy and in no package

### Requirement: The frontmatter check keeps the skill uploadable
`python3 install.py check` SHALL accept only frontmatter written in the one-line subset of YAML that design D2 defines — one-line plain or quoted values, spaces as the only whitespace, and `metadata` as indented `key: value` lines — and SHALL refuse any other form. For every form it accepts it SHALL apply the constraints that skill uploads enforce. It SHALL print every failure it finds and exit non-zero on any failure (zero when all pass):
- `SKILL.md` is a regular file, not a symlink, and opens with a frontmatter block delimited by `---` lines, written in that subset;
- the block carries no key other than `name`, `description`, `license`, `allowed-tools`, `metadata` and `compatibility`;
- `name` is present, uses only lowercase letters, digits and hyphens, neither starts nor ends with a hyphen, contains no consecutive hyphens, and is at most 64 characters;
- `description` is present, non-empty, at most 1,024 characters, and contains no `<` or `>`;
- `license`, `allowed-tools` and `compatibility`, when present, are one-line strings, `compatibility` at most 500 characters;
- `metadata`, when present, is a map whose keys and values are one-line strings, written as indented `key: value` lines.

The build and the installer SHALL run the same check first and SHALL change nothing when it fails. The OPSX verify gate's structural checks SHALL include this check exiting 0.

#### Scenario: An over-long description blocks packaging and install
- **WHEN** the frontmatter `description` is longer than 1,024 characters
- **THEN** `check` exits non-zero naming the description's length and the 1,024-character limit, and `build` and `install` exit non-zero without writing any file

#### Scenario: The shipped skill passes
- **WHEN** `check` runs against the repo's `SKILL.md`
- **THEN** it exits 0

### Requirement: Built packages for upload and plugin hosts
`python3 install.py build` SHALL write two zip archives into `dist/` at the repo root, or into the directory given with `--out` (an empty `--out` value is refused), replacing any previous copies:
- `okr-ninja.skill` — the payload under one top-level folder named after the skill (`okr-ninja/SKILL.md`, `okr-ninja/references/…`, `okr-ninja/examples/…`), the layout claude.ai and Cowork accept as a skill upload;
- `okr-ninja.plugin` — `.claude-plugin/plugin.json` at the archive root and the payload under `skills/okr-ninja/`. The manifest SHALL be valid JSON whose `name` equals the skill's `name`, whose `version` is a semantic version, and whose `description` is non-empty.

Building twice from an unchanged payload SHALL produce byte-identical archives.

#### Scenario: Skill archive layout
- **WHEN** `build` completes
- **THEN** every entry of `okr-ninja.skill` sits under `okr-ninja/`, and the entries are exactly the payload files

#### Scenario: Plugin archive layout
- **WHEN** `build` completes
- **THEN** `okr-ninja.plugin` holds `.claude-plugin/plugin.json` plus exactly the payload files under `skills/okr-ninja/`, and the manifest parses with `name` `okr-ninja`, a semantic `version` and a non-empty `description`

#### Scenario: Rebuilds are reproducible
- **WHEN** `build` runs twice with no change to the payload
- **THEN** each archive is byte-identical across the two runs

### Requirement: Installer targets
`python3 install.py`, or `python3 install.py install`, SHALL place a copy of the payload at `<home>/.claude/skills/okr-ninja/` and at `<home>/.agents/skills/okr-ninja/`, where `<home>` is the current user's home directory, creating missing parent folders. With `--project DIR` it SHALL use `DIR/.claude/skills/okr-ninja/` and `DIR/.agents/skills/okr-ninja/` instead, and SHALL exit non-zero without changing anything when `DIR` is not an existing directory. An empty `--project` value is not an existing directory. `--only claude` SHALL install only the `.claude` target and `--only agents` only the `.agents` target. The installer SHALL print each path it installed, and SHALL work from a checkout without git metadata, such as a downloaded archive of the repo.

#### Scenario: Default install covers the folder-reading platforms
- **WHEN** a user runs `python3 install.py` with no options
- **THEN** `<home>/.claude/skills/okr-ninja/SKILL.md` and `<home>/.agents/skills/okr-ninja/SKILL.md` both exist, each beside the full payload, and both paths are printed

#### Scenario: Project install
- **WHEN** a user runs `python3 install.py --project DIR` on an existing directory `DIR`
- **THEN** the payload is installed at `DIR/.claude/skills/okr-ninja/` and `DIR/.agents/skills/okr-ninja/`, and nothing under `<home>` changes

#### Scenario: One target only
- **WHEN** a user runs `python3 install.py --only agents`
- **THEN** only `<home>/.agents/skills/okr-ninja/` is written

### Requirement: Replacing an existing install is safe
When a target already exists, the installer SHALL replace it so that it holds exactly the new payload, with no file left over from the previous copy. The previous copy SHALL be moved aside before the new copy is moved into place, so a failure or interruption never leaves a partly deleted copy at the target; if the moved-aside copy cannot be deleted afterwards, the installer SHALL say where it was left. A previous copy its owner cannot read or write is made accessible to its owner before it is inspected or moved aside, and its mode is put back if the install is refused or undone. The installer SHALL delete only the previous copy it moved aside in the same run — never another folder beside the target, including hidden folders left by earlier runs; those were named when they were left. When a target is a symbolic link, the installer SHALL move and remove only the link and SHALL NOT modify or delete anything the link points to; if the new copy then cannot be moved into place, the link is put back. When a target is a real directory that is the checkout the installer runs from, or contains that checkout — judged by file-system identity, so a path differing only in letter case on a case-insensitive disk counts as the same directory — the installer SHALL exit non-zero, name the conflicting target, and change nothing at any target. When a target is a real directory holding a `.git` entry, it is a repository clone rather than an installed copy, and the installer SHALL exit non-zero, name it, and change nothing at any target. When a target exists but is neither a directory nor a symbolic link, the installer SHALL exit non-zero and change nothing at any target.

#### Scenario: Stale files are removed
- **WHEN** a previous install holds a file that the current payload no longer contains
- **THEN** after the install that file no longer exists at the target

#### Scenario: An undeletable previous copy never leaves a broken install
- **WHEN** a file in the previous copy cannot be deleted
- **THEN** the target holds exactly the new payload, and the installer names the folder where the previous copy was left

#### Scenario: A hand-made folder beside the target is never deleted
- **WHEN** a folder that this run did not create — such as `.okr-ninja.my-backup.previous`, `.okr-ninja.20260923.previous`, or a copy an earlier run could not delete — sits beside a target
- **THEN** after the install it and every file in it are unchanged

#### Scenario: A symlinked checkout becomes a copy
- **WHEN** `<home>/.claude/skills/okr-ninja` is a symbolic link to a repo checkout, as the previous README instructed
- **THEN** after the install that path is a real directory holding exactly the payload, and every file in the checkout the link pointed to is unchanged

#### Scenario: Running from inside a target refuses
- **WHEN** the installer runs from a checkout that is itself the real directory `<home>/.claude/skills/okr-ninja`
- **THEN** it exits non-zero naming that target, and neither target changes

#### Scenario: A case variant of the checkout's path still refuses
- **WHEN** on a case-insensitive disk the checkout sits at `<home>/.claude/skills/OKR-Ninja` and the installer runs from it
- **THEN** it exits non-zero naming `<home>/.claude/skills/okr-ninja`, and every file of the checkout is unchanged

#### Scenario: A repository clone at a target is never deleted
- **WHEN** `<home>/.claude/skills/okr-ninja` is a real directory holding `.git`, as a clone copied there per the previous README would
- **THEN** the installer exits non-zero naming it, and every file under it is unchanged

### Requirement: Install routes are documented per platform
README's Installation section SHALL state, for Claude Code, Cursor, Codex, Cowork and claude.ai, where that platform looks for skills and which route installs OKR-Ninja there: the installer for platforms that read skill folders, the `.skill` upload for Cowork and claude.ai, and the `.plugin` as an alternative for hosts that install Claude plugins. It SHALL NOT instruct users to symlink the repo checkout into a skills folder.

#### Scenario: Every listed platform has a route
- **WHEN** a reader looks up any of Claude Code, Cursor, Codex, Cowork or claude.ai in README's Installation section
- **THEN** they find where that platform looks for skills and the command or upload that installs OKR-Ninja there

#### Scenario: No checkout symlink instruction
- **WHEN** README is searched for an instruction to symlink the checkout into a skills folder
- **THEN** there is none
