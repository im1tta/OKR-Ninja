## Why

README.md is 169 lines and makes a first-time visitor read product strategy (reader personas, four jobs, distribution intent) and a 25-line repository tree before reaching how to install or use the skill. The repo has just gone public with a one-command install, so the README's first screen should answer what OKR-Ninja is, how to install it, and how to use it. Everything else belongs further down.

## What Changes

- **Reorder README.md around a newcomer's path.** The top half becomes: a short pitch (the two axes and the quote-or-no-finding rule), **Quick start** (the macOS/Linux and Windows one-liners, "run it again to update", and the claude.ai/Cowork build-and-upload step), **Usage** (example prompts per mode, and the out-of-scope note for drafting new OKRs), **What you get** (a condensed two-mode table) and **Data sources**.
- **Move the technical and reference material below a divider:** **Installation reference** (per-platform table, `--release`/`--project`/`--only`, the fully pinned form, inspect-first, the `.plugin`, the clone route and checkout commands, and what ships), **Product context**, **Development**, **Roadmap** and **License**.
- **Condense the product context and move it down.** Every decision it records is kept: one reader per mode and the §6 hand-off, drift tracking as the target use-case vs. the pre-commit review built today (and the mid-quarter guardrail note), the four jobs in build order as the tie-break order with their built/unbuilt status, and the distribution intent (a portfolio/demo piece, eval rigor above detection features, fixed opinionated doctrine, no per-org configuration, fictional fixtures).
- **Prune the Roadmap to open items.** Remove the "landed" history entries (eval harness, artifact-lifecycle eval, precision pass), which are already recorded in git and the OpenSpec archive. A new short **Development** section replaces them with a trimmed repo tree, a 3–4 line description of the eval harness and its tiers, and a pointer to CLAUDE.md.
- **Keep every documented command byte-identical.** No command changes; commands only move between sections.
- **Point `openspec/config.yaml`'s project context** at the renamed product-context heading.

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `distribution`: the requirement "Install routes are documented per platform" now lets README split installation in two. A top **Quick start** leads with the one-command install (macOS/Linux and Windows), says that re-running it updates the skill, and gives the claude.ai/Cowork `build`-and-upload route. A later **Installation reference** section carries the remaining routes: the per-platform table, the options and fully pinned form, inspect-first, the `.plugin`, and the clone route. Every existing scenario is kept (a route for every platform, updating documented, `-I` on every command and no write into the current folder, a consistent pinned tag, no symlink instruction, no placeholder URL). They now range over both sections rather than a single "Installation section".

## Non-goals

- No change to the skill payload (`SKILL.md`, `LICENSE`, `references/`, `examples/`), `install.py`, `tests/` or `evals/`, and no version bump. Users get nothing new to install.
- No change to CLAUDE.md's file-ownership table. README remains the only home of the product context and of human install instructions.
- No change to any product decision. The product context is reworded and moved, never revised.
- No new docs files. Nothing is split out of README.
- No change to detection behaviour, so no planted defect is newly caught and no fixture eval applies.

## Impact

- `README.md`: restructured, targeting roughly 110–140 raw lines (blank lines around every fence and list for markdown hygiene included) with Quick start inside the first ~25 lines.
- `openspec/specs/distribution/spec.md`: one modified requirement, via this change's delta.
- `openspec/config.yaml`: the project context names the new product-context heading.
- The gate is the structural checks: `python3 install.py check`, `python3 -m unittest discover -s tests` (whose tests read README.md only as the checkout marker, never its content) and `python3 evals/grader/harness.py check`.
