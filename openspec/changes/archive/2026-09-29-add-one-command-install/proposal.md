## Why

The repo is about to go public at `github.com/im1tta/OKR-Ninja`, but a stranger who finds it cannot get the skill without cloning it first, cannot tell which version they have, and gets updates only by pulling a clone and re-running the installer; claude.ai and Cowork users additionally need git and a checkout just to build the upload file. The repo also carries no license — a public repo without one grants nobody the right to use or share the skill — and its README clones from a placeholder `your-org` URL.

## What Changes

- **Remote mode in `install.py`.** Remote mode is the default. The installer reads a local checkout only when it runs from a file whose folder holds both `SKILL.md` and `README.md` and no remote option is given. Piped with `curl -fsSL …/install.py | python3 -I -`, or downloaded on its own, it runs remotely:
  - it resolves the newest published GitHub Release of `im1tta/OKR-Ninja` and downloads that tag's source archive over HTTPS, from GitHub hosts only;
  - it reads the runtime payload out of the archive in memory, never extracting it, and refuses unsafe or colliding entry names, decompression bombs, a payload named anything other than `okr-ninja`, and a version that disagrees with the tag;
  - it then runs the requested command exactly as a checkout run does: `install` (the default), `build` or `check`.

  Re-running the same command is the update. New options: `--release TAG` pins a release; `--repo OWNER/NAME` points a fork at its own releases; `--source ZIP` reads a local archive instead of downloading, for offline use and tests. `--project`, `--only` and `--out` behave as today, and a remote `build` writes into the current folder by default. Every documented command runs Python in isolated mode (`-I`), so files in the user's current folder cannot shadow the standard library.
- **One version, in the skill.** `SKILL.md`'s frontmatter gains `metadata.version` (semantic version, first value `0.2.0`), the single source of the skill's version. `check` requires it; `build` writes it into the `.plugin` manifest instead of the hard-coded `0.1.0`; a remote run refuses an archive whose version disagrees with the release tag it came from; `install` reports the version it installed and the version it replaced.
- **MIT license.** A root `LICENSE` (MIT), `license: MIT` in the frontmatter, and `LICENSE` added to the runtime payload so every installed copy and package carries the notice the license requires.
- **README.** The Installation section leads with the one-command install and update (macOS/Linux pipe form, Windows download-then-run form, and a download-and-inspect-first form), the remote `build` for claude.ai and Cowork, and keeps the clone + `install.py` route for developers; the placeholder clone URL becomes the real one; the layout lists `LICENSE` and `tests/`.
- **CLAUDE.md.** A short "Releasing" procedure: bump `metadata.version` under a stated semver policy, merge, create the release as a pre-release, smoke it with `--release`, then promote it to latest. Also file-map rows for `LICENSE` and `tests/`, and the `install.py` row names `LICENSE` in the payload and remote mode.
- **`tests/test_install.py`.** A standard-library `unittest` suite that runs offline and covers remote-mode detection, archive reading and every refusal, version/tag agreement, redirect and host rules through a fake HTTPS handler, end-to-end piped install and update into a scratch home, remote build, and a frozen-release compatibility case. It is added to the OPSX verify gate's structural checks and CLAUDE.md's testing steps, and `.gitignore` gains `__pycache__/`. It guards `main`, because the one-liner always fetches `main`'s installer.
- **Housekeeping.** `install.py`'s docstring points at the archived `add-cross-platform-install` design and the synced `openspec/specs/distribution/spec.md` instead of the moved change folder.

This change touches no detection behavior — no procedure step, rubric, taxonomy, report format, fixture or key; the frontmatter edit adds `license` and `metadata.version` and leaves `description` untouched — so it newly catches no planted defect in either fixture.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `distribution`: the runtime payload gains `LICENSE`; the frontmatter check requires a semantic `metadata.version`; the plugin manifest's version comes from it; install output reports old and new versions; README's install routes lead with the isolated one-command install and update, and keep the `.skill` and `.plugin` routes. New requirements cover remote install from a published release, reading archives without extracting them, a release's version agreeing with its tag, and an offline installer test suite in the verify gate.

## Impact

- `install.py` — remote mode, version handling, `LICENSE` in the payload, docstring and help text.
- `.gitignore` — `__pycache__/`, `*.pyc`.
- `.claude/skills/openspec-loop/phases/verify-gate.md` — the structural checks gain the installer test suite. The path is write-protected in the development sandbox and needs the owner's approval.
- `SKILL.md` — frontmatter only: `license: MIT` and `metadata.version: "0.2.0"`. `description` and the procedure body are unchanged, so the closed-skill routing rules are untouched.
- `LICENSE`, `tests/test_install.py` — new.
- `README.md`, `CLAUDE.md` — as listed above.
- `openspec/specs/distribution/spec.md` — updated from the delta at archive time.
- Users: the documented install becomes one command with no clone; an install made by an earlier `install.py` is replaced by the next run and reported as "was unversioned". The one-liner has nothing to fetch until the owner publishes the first release (`v0.2.0`) after merge.
- No change to `evals/`: keys, prompts, harness and committed batches are untouched; the harness snapshots `SKILL.md` and `references/` by `git archive`, which the frontmatter addition does not affect.

## Non-goals

- No Claude Code plugin marketplace (`.claude-plugin/marketplace.json`); no auto-update or update-available notifications.
- No CI workflow, no release assets built by CI, and no tagging or publishing of a release as part of this change — the owner cuts `v0.2.0` after merge.
- No scrubbing of absolute paths in committed eval records and no git-history rewrite.
- No support for tar archives, GitHub Enterprise hosts, or checksum/signature verification of release archives.
- No change to what the skill does: procedure, rubric, taxonomy, report format, fixtures and keys are out of scope.
