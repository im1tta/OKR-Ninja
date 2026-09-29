## 1. Rewrite README.md

- [x] 1.1 Snapshot the current README (`git show HEAD:README.md`) as the baseline for the checks in section 3.
- [x] 1.2 Write the top half (design D1, D2, D5): pitch, `## Quick start`, `## Usage`, `## What you get`, `## Data sources`. Verify that Quick start begins within the first ~25 lines, that the single-team and portfolio prompts both appear, and that the draft-new-OKRs exclusion is present.
- [x] 1.3 Write the reference half (design D1–D4): the divider, then `## Installation reference`, `## Product context`, `## Development`, `## Roadmap` and `## License`. Verify that no "landed" roadmap entry remains and that CLAUDE.md is pointed to.
- [x] 1.4 Verify the README is roughly 110–140 raw lines, blank lines around fences and lists included (`wc -l README.md`), and renders cleanly: headings are in order, tables are well-formed and fences are balanced.

## 2. Keep references in step

- [x] 2.1 Update `openspec/config.yaml` so the project context cites the new `## Product context` heading. Verify with `grep -n "Product context" openspec/config.yaml`, and confirm no file outside `openspec/changes/archive/` and `evals/runs/` still cites the old heading.

## 3. Verify against the baseline

- [x] 3.1 Extract every fenced code block from the baseline and from the new README. Verify that each baseline command appears byte-identical in the new README.
- [x] 3.2 Check each scenario of the modified distribution requirement against the new README. Every platform has a route, updating is documented, `-I` appears on every command, no command writes into the current folder, the pinned tag matches, there is no symlink instruction and no `your-org`.
- [ ] 3.3 Check each product-context claim from the baseline against the new `## Product context`. Every claim must be present, even if reworded: the personas, the §6 hand-off, drift tracking vs. pre-commit review, the mid-quarter note, all four jobs with their status and tie-break, and the distribution intent.
- [x] 3.4 Run `python3 install.py check`, `python3 -m unittest discover -s tests`, `python3 evals/grader/harness.py check` and `openspec validate readme-readability --strict`. All must pass.
