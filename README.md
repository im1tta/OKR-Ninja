# OKR-Ninja

OKR-Ninja audits OKRs, for one team or a whole portfolio. It is an [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for Claude Code, Cursor, Codex, Cowork and claude.ai, and it checks two axes:

1. **Goodness.** Are the objectives and key results well-formed? It checks outcome vs. task, baselines, measurability, ambition, vanity metrics and more.
2. **Alignment.** Do the teams' OKRs fit together? It looks for unacknowledged dependencies, metric tug-of-wars, duplicated objectives, timeline mismatches and resource contention.

Every finding quotes the OKR text word for word and gives its source ref: a Confluence page title, a Jira issue key, or a file path with heading and line (exact format in [`references/report-format.md`](references/report-format.md)). No quote, no finding.

## Quick start

One command installs OKR-Ninja for Claude Code, Cursor and Codex. It needs Python 3.8 or later and nothing else: no clone, no git. Run it, then start a new session and check that `okr-ninja` appears in the skills list. Run the same command again to update.

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py | python3 -I -
```

**Windows (PowerShell):**

```powershell
$f = Join-Path $env:TEMP 'okr-ninja-install.py'; curl.exe -fsSLo $f https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py; if ($LASTEXITCODE -eq 0) { py -I $f }
```

**claude.ai and Cowork** load skills only from uploads. The `build` command below writes the upload file, `okr-ninja.skill`, into the current folder. Upload it under Skills in your claude.ai settings. Skills on your account also reach Cowork and signed-in Claude Code sessions. An uploaded copy does not update itself: to update it, run `build` again and upload the new file.

```bash
curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py | python3 -I - build
```

## Usage

A prompt about one team and a prompt about several teams should both trigger OKR-Ninja. Prompts asking to write new OKRs from scratch ("draft OKRs for my team") are out of scope and should not trigger it. The skill's first step, scope intake, confirms which teams are in scope, and that team count selects the mode: two or more teams get portfolio mode, exactly one gets single-team mode. For example:

- "Sweep the Q3 OKRs for Payments, Growth, Platform, and Data and tell me where they conflict." *(portfolio mode)*
- "Audit our whole portfolio of OKRs in the PLANNING Confluence space — quality and cross-team alignment." *(portfolio mode)*
- "Are any of our teams' OKRs pulling against each other this quarter?" *(portfolio mode)*
- "Here are OKR exports for six squads (attached markdown files) — find duplicated objectives and unowned dependencies." *(portfolio mode)*
- "Review the Payments team's OKRs." *(single-team mode)*
- "Are the Platform squad's KPIs any good?" *(single-team mode)*

## What you get

| | **Portfolio mode** (2+ teams) | **Single-team mode** (exactly 1 team) |
|---|---|---|
| Core question | Do these OKRs fit *together*? Are there systemic quality problems? | Are this team's OKRs *deeply* sound? |
| Goodness depth | Screening: rubric scores and top findings per team | Exhaustive: every objective and KR scored, a full anti-pattern sweep, a rewrite for every Critical or Major finding |
| Alignment analysis | Yes: cross-team failure modes are a first-class output | No cross-team findings (one team can't supply both sides' quotes); dependency mentions become labeled, unverified notes |
| Follow-up | §6 of the report recommends single-team re-runs for teams that score badly | None |

Portfolio mode writes a six-section report with a heatmap. Single-team mode writes a five-section report for its one team, with no heatmap and no cross-team findings. Both reports are defined in [`references/report-format.md`](references/report-format.md), and both modes share the same rubric, severity scale, source-ref format and evidence rules. The skill is closed and self-contained: it never hands any part of a review to another skill.

## Data sources

- **Atlassian MCP (preferred).** If an Atlassian MCP server is connected, the skill searches Jira via JQL and Confluence via CQL to locate each team's OKR pages and issues, and cites Confluence page titles and Jira issue keys in every finding.
- **Local files (fallback).** With no MCP connected, point the skill at local exports: markdown, CSV or spreadsheet files containing the OKRs. Findings then cite file paths with headings and line numbers. [`examples/sample-portfolio.md`](examples/sample-portfolio.md) and [`examples/sample-portfolio-2.md`](examples/sample-portfolio-2.md) show the expected shape of a markdown export.

---
**Reference.** You can stop here if you only want to use the skill. The rest covers install details, product context, development and the roadmap.

## Installation reference

| Platform | Where it looks for skills | Install route |
|---|---|---|
| Claude Code | `~/.claude/skills/`, a project's `.claude/skills/`, plugins, and skills uploaded to your claude.ai account | [The one-command install](#quick-start) |
| Cursor | `~/.agents/skills/`, `~/.cursor/skills/`, `~/.claude/skills/` and `~/.codex/skills/`, plus the same folders inside a project | [The one-command install](#quick-start) |
| Codex | `~/.agents/skills/` and a project's `.agents/skills/` | [The one-command install](#quick-start) |
| Cowork | Skills uploaded to your claude.ai account, and plugins (not a project folder's `.claude/skills/`) | [Upload `okr-ninja.skill`](#quick-start), or install `okr-ninja.plugin` |
| claude.ai | Skills uploaded to your account | [Upload `okr-ninja.skill`](#quick-start) |

- **What the installer does.** It downloads the newest published release of this repo from GitHub, reads the skill out of the release archive in memory, and copies it into `~/.claude/skills/okr-ninja/` and `~/.agents/skills/okr-ninja/`. It prints the version it installed and the version it replaced, and nothing else on your machine changes. `-I` runs Python in isolated mode, so no file in your current folder can stand in for part of Python's standard library.
- **What ships.** Only the skill, as a standard Agent Skill folder: `SKILL.md`, `LICENSE`, `references/` and `examples/`. One copy works on every platform in the table; they differ only in where they look for it. `README.md`, `CLAUDE.md`, `install.py`, `tests/`, `evals/`, `openspec/` and `.claude/` never reach an installed copy or a package. The same `build` that writes `okr-ninja.skill` also writes `okr-ninja.plugin`, an optional Claude plugin containing only the skill, for hosts that install Claude plugins, such as Cowork.
- **Options.** Arguments go after the `-` on macOS and Linux (`… | python3 -I - --only agents`), or after `$f` on Windows.
  - `--release TAG` installs that release instead of the latest one, for example `--release v0.2.0`. It pins the skill, not the installer, which is whichever `install.py` you fetched. For a fully pinned install, fetch the installer from the same tag: `curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/v0.2.0/install.py | python3 -I - --release v0.2.0`.
  - `--project DIR` installs into `DIR/.claude/skills/` and `DIR/.agents/skills/` instead, so the skill is available only in that project.
  - `--only claude` or `--only agents` installs just one of the two. Cursor reads both folders, so if Cursor is the only tool you use, `--only agents` stops it listing the skill twice.

**Inspect before running.** Download the installer into a fresh private folder, read it, then run it from the same terminal:

```bash
d=$(mktemp -d) && curl -fsSLo "$d/install.py" https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py && less "$d/install.py"
```

```bash
python3 -I "${d:?run the download step first, in this same terminal}/install.py"
```

**From a clone (developers).** A checkout installs itself, with no download:

```bash
git clone https://github.com/im1tta/OKR-Ninja.git
cd OKR-Ninja
python3 install.py
```

In a checkout, `python3 install.py build` writes both packages into `dist/`, which is git-ignored. `python3 install.py check` validates the frontmatter against the rules skill uploads enforce (for example, a description of at most 1,024 characters) and requires a semantic `metadata.version`. `build` and `install` run the same check first and stop if it fails. On Windows, run `py install.py` wherever this section says `python3 install.py`. Re-running the installer replaces the previous copy. A symlinked install made per an older version of this README becomes a copy, and the checkout it pointed at is left alone.

## Product context

- **Readers.** Portfolio mode is written for an **exec or portfolio owner** (a VP, chief of staff or founder with authority across the teams) judging organizational OKR quality and cross-team alignment. Single-team mode is written for the **lead of the team under review**. §6 of the portfolio report links them: the exec gets a ready-to-paste single-team prompt for the lead to run.
- **Target vs. today.** Today's build assumes a **pre-commit draft review**: the text is still editable, so a concrete rewrite is directly actionable. The target is **cross-cycle drift tracking** of a team or portfolio: silently dropped KRs, moving goalposts, recycled objectives. The gap is known and additive, not a contradiction to patch: drift tracking needs a per-cycle store and tracking-continuity dimensions, and is the roadmap's centre of gravity. Mid-quarter or later, a review should turn rewrites into guardrails and escalations, as the text is locked.
- **Four jobs, in build order, which is also the tie-break order.**
  1. **Input to a planning conversation** *(portfolio; built)*: the two or three cross-team collisions worth an hour of people's time. The ~10-line verdict, ≤10-item action list and both-sides evidence rule serve it; brevity wins.
  2. **Punch list a lead works through** *(single-team; built, depth parity pending)*: exhaustive scoring and a rewrite for every Critical and Major finding; depth wins.
  3. **Coaching artifact** *(unbuilt)*: lands with drift tracking, since comparing quarters pays off only if the reader learns between cycles.
  4. **Quality gate before OKRs are locked** *(deliberately last)*: needs roll-up scores reproducible across model versions, which the calibration set cannot yet provide. Until then, grades route follow-up (§6) and gate nothing.
- **Distribution: a portfolio / demo piece.** Spec discipline and eval rigor are the product, so eval and calibration work outranks new detection features. The doctrine stays fixed and opinionated (outcome over output, baselines mandatory, sandbagging a defect). Per-org configurability is an explicit non-goal, even though Google-style aspirational 0.7 targets would need AP-06 Sandbagged Target and K3 Ambition Calibration relaxed. Fixtures stay fictional, for demo safety as much as hygiene.

## Development

Agents developing this repo start with [CLAUDE.md](CLAUDE.md): file ownership, editing rules and test steps. Changes go through the OpenSpec (OPSX) workflow: propose, apply, verify, archive (see "Change workflow (OPSX)" in CLAUDE.md).

```
OKR-Ninja/
├── SKILL.md      # Skill entry point: trigger description, version and review procedure (kept lean)
├── references/   # Scoring rubric, alignment failure modes, report format (loaded on demand)
├── examples/     # Two fictional portfolios with planted defects and near-miss non-defects; the eval set
├── evals/        # Eval harness: JSON answer keys, grader, lifecycle eval, committed runs
├── install.py    # Installer, package builder (.skill, .plugin) and frontmatter check; stdlib only
├── tests/        # Offline unittest suite for install.py
├── openspec/     # OpenSpec (OPSX) change-of-record scaffold
├── .claude/      # OPSX commands and skills, and the /okr-eval command
├── LICENSE       # MIT; ships with every installed copy and package
└── CLAUDE.md     # Instructions for agents developing this repo
```

**Evals.** `/okr-eval` runs the skill as subagents on your Claude Code subscription (no API tokens) and grades the results deterministically. The report tiers (`smoke`, `candidate`, `baseline`, `decision`) grade each fixture report against its JSON answer key: every planted defect found by canonical ID, no fabricated quote, extra findings within the key's budget. `lifecycle` checks the publish contract instead, against a non-fixture corpus. Details are in [`.claude/commands/okr-eval.md`](.claude/commands/okr-eval.md); results live under `evals/runs/`.

## Roadmap

- **Single-team depth parity.** Close the gaps left by absorbing single-team review with the existing rubric machinery: tracking-continuity and claimed-vs-actual-tracking dimensions (Jira activity vs. stated cadence), a computed /100 headline score, deterministic check scripts (placeholder detection, coverage counts, score caps), and a dedicated single-team fixture with its own answer key. Today single-team mode is evaluated via fixture 1's Platform slice.
- **Historical drift tracking.** Compare a team's OKRs quarter over quarter to surface silently dropped KRs, moving goalposts and recycled objectives.
- **Scoring calibration set.** A labelled corpus of real-world (anonymized) OKRs with agreed rubric scores, to keep 0–4 scoring consistent across model versions.
- **CI driver and routing tests.** A headless `claude -p` driver for CI, and automated routing tests for the skill description (not observable from subagent output).
- **Larger fixtures.** Portfolios of 8–12 teams.

## License

MIT. See [LICENSE](LICENSE). The notice ships inside every installed copy and package.
