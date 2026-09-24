## Why

OKR-Ninja reaches an agent only through a hand-made copy or symlink, and the README's install options name a single folder that Codex never reads. Cowork and claude.ai cannot run it at all: they load skills only from account uploads or plugins, and an uploaded skill is rejected when its frontmatter `description` exceeds 1,024 characters — OKR-Ninja's is 1,146. The owner uses Cowork, where the skill is therefore unusable today (tested: Cowork ignores a project folder's `.claude/skills/`).

## What Changes

- **SKILL.md frontmatter `description`** shortened from 1,146 to at most 1,024 characters, with the key use case first. It still claims both modes, keeps the writing-new-OKRs-from-scratch exclusion, and names no other skill. The procedure body is untouched.
- **New root-level `install.py`** (Python standard library only, runs on macOS, Linux and Windows) with three commands:
  - `install` (the default) copies the runtime payload — `SKILL.md`, `references/`, `examples/` — into `~/.claude/skills/okr-ninja/` and `~/.agents/skills/okr-ninja/`; `--project DIR` targets that project's `.claude/skills/` and `.agents/skills/` instead; `--only claude|agents` picks one. An existing install is replaced cleanly; a symlinked install is replaced by removing the link only, never what it points to.
  - `build` writes `dist/okr-ninja.skill` (the upload format for claude.ai and Cowork) and `dist/okr-ninja.plugin` (a Claude plugin), both holding only the runtime payload and both byte-reproducible.
  - `check` validates the frontmatter the way skill uploads do: kebab-case `name`, `description` present, at most 1,024 characters, no angle brackets, only permitted keys.
- **`.gitignore`** gains `dist/`: packages are built on demand, never committed.
- **README** Installation section replaced: a platform table (where Claude Code, Cursor, Codex, Cowork and claude.ai look for skills) and three routes — `install.py` for the folder-reading platforms, the `.skill` upload for Cowork and claude.ai, the `.plugin` as an option. The old "symlink the whole checkout" instruction is dropped: it exposed `CLAUDE.md`, `evals/` and the repo's own `.claude/` to every session using the skill. Repository layout lists `install.py` and `dist/`.
- **CLAUDE.md**: file-map rows for `install.py` and `dist/`; the frontmatter-description editing rule gains a fourth condition — stay within 1,024 characters; testing step 1 gains `python3 install.py check`.
- **Verify gate** (`.claude/skills/openspec-loop/phases/verify-gate.md`): the structural checks gain `python3 install.py check` exits 0.
- **`openspec/config.yaml`** context: "no build" is corrected — the skill stays markdown-only, while `install.py` packages it.

This change touches no detection behavior — no procedure step, rubric, taxonomy, report format, fixture or key — so it newly catches no planted defect in either fixture. The description edit is routing text only; the smoke tier still runs on all three slices because CLAUDE.md requires it for any description change.

## Capabilities

### New Capabilities

- `distribution`: what gets shipped (the runtime payload), the frontmatter check that keeps the skill uploadable, the two built packages, the installer's targets and its replacement safety rules, and the documented install route per platform.

### Modified Capabilities

None. `review-modes`' "The repo is closed" requirement (the description claims both modes, keeps the write-new exclusion, names no other skill) is unchanged and must still hold after the shortening.

## Impact

- `SKILL.md` — frontmatter `description` only.
- `install.py` — new.
- `.gitignore`, `README.md`, `CLAUDE.md`, `.claude/skills/openspec-loop/phases/verify-gate.md`, `openspec/config.yaml` — as listed above.
- `openspec/specs/distribution/spec.md` — created from the delta at archive time.
- Existing installs: a copy made per the old README is replaced by `install.py`; a symlink made per the old README is replaced by a copy, leaving the checkout it pointed at untouched.
- Uploaded copies on claude.ai or Cowork do not update themselves: after a skill change the owner rebuilds and re-uploads.
- No change to `evals/` — keys, prompts, harness and committed batches are untouched.

## Non-goals

- No plugin marketplace (`.claude-plugin/marketplace.json`) and no committed packages; `dist/` stays out of git.
- No automated routing test: routing is checked by a fresh subagent's review during verify, then by the owner in Cowork after upload.
- No PowerShell or bash installer, and no symlink install mode.
- No GitHub Release publishing, and no Cursor- or Codex-specific plugin formats.
- No change to what the skill does: procedure, rubric, taxonomy, report format and fixtures are out of scope.
