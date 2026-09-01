# OKR-Ninja

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for Claude Code that audits a **portfolio of OKRs across multiple teams** on two axes:

1. **Goodness** — are the objectives and key results well-formed? (outcome vs. task, baselines, measurability, ambition, vanity metrics, and more)
2. **Alignment** — do the teams' OKRs fit together? (unacknowledged dependencies, metric tug-of-wars, duplicated objectives, timeline mismatches, resource contention)

Every finding is backed by a **verbatim quote and a source ref** (Confluence page title, Jira issue key, or file path + heading/line — the exact format is defined in `references/report-format.md`). No quote, no finding.

## How it relates to `okr-deepdive`

OKR-Ninja is the wide-angle lens; its sibling skill `okr-deepdive` is the microscope. They are designed to hand off to each other, and keeping their trigger descriptions from overlapping is an explicit maintenance rule — see the routing sanity-check in `CLAUDE.md`'s "Testing changes."

| | **OKR-Ninja** (this repo) | **okr-deepdive** (sibling skill) |
|---|---|---|
| Scope | Portfolio: 2+ teams/projects at once | ONE team or project |
| Core question | Do these OKRs fit *together*? Are there systemic quality problems? | Are this team's OKRs *deeply* sound? |
| Alignment analysis | Yes — cross-team failure modes are a first-class output | No cross-team alignment; single-team strategy check only |
| Depth per team | Rubric scores + top findings per team | Full pipeline: gap register, rewrites, adversarial critique |
| Hands off to | `okr-deepdive` for teams that score badly | OKR-Ninja when the ask turns multi-team |

If you ask for a review of a single named team, the router should pick `okr-deepdive`, not this skill.

## Repository layout

```
OKR-Ninja/
├── SKILL.md                        # Skill entry point: trigger description + procedure
├── references/
│   ├── goodness-rubric.md          # Scoring dimensions (O1–O4, K1–K7), AP-XX anti-patterns, roll-up
│   ├── alignment-taxonomy.md       # AL-XX cross-team failure modes and how to detect them
│   └── report-format.md            # Output contract: severity scale, source-ref format, report templates
├── examples/
│   ├── sample-portfolio.md         # Fixture 1: fictional 4-team portfolio with planted defects + answer key
│   └── sample-portfolio-2.md       # Fixture 2: fictional 5-team portfolio covering the catalog modes fixture 1 leaves uncovered
├── openspec/                       # OpenSpec (OPSX) change-of-record scaffold
├── .claude/                        # OPSX commands (commands/opsx/*) and skills (skills/openspec-*)
├── README.md                       # This file
├── CLAUDE.md                       # Instructions for agents developing this repo
└── .gitignore
```

`SKILL.md` stays lean; the reference files are loaded on demand (progressive disclosure). Changes to this repo go through the OPSX workflow — see `CLAUDE.md`'s "Change workflow (OPSX)."

## Installation

**Option A — copy or symlink into your personal skills directory:**

```bash
git clone https://github.com/your-org/OKR-Ninja.git
ln -s "$(pwd)/OKR-Ninja" ~/.claude/skills/okr-ninja
# or: cp -R OKR-Ninja ~/.claude/skills/okr-ninja
```

**Option B — project-level install:** place the directory at `.claude/skills/okr-ninja` inside a repo to make it available only in that project.

**Option C — plugin marketplace:** if your organization distributes skills through a Claude Code plugin marketplace, add this repo as a skill entry in the plugin's manifest and install the plugin as usual.

Restart Claude Code (or start a new session) and confirm the skill appears in the skills listing.

## Usage

Example prompts that should trigger OKR-Ninja:

- "Sweep the Q3 OKRs for Payments, Growth, Platform, and Data and tell me where they conflict."
- "Audit our whole portfolio of OKRs in the PLANNING Confluence space — quality and cross-team alignment."
- "Are any of our teams' OKRs pulling against each other this quarter?"
- "Here are OKR exports for six squads (attached markdown files) — find duplicated objectives and unowned dependencies."

Prompts about a single team ("review the Payments team's OKRs") should route to `okr-deepdive` instead.

## Data sources

**Atlassian MCP (preferred).** If an Atlassian MCP server is connected, the skill searches Jira via JQL and Confluence via CQL to locate each team's OKR pages/issues, and cites Confluence page titles and Jira issue keys in every finding.

**Local files (fallback).** With no MCP connected, point the skill at local exports — markdown, CSV, or spreadsheet files containing the OKRs. Findings then cite file paths with headings and line numbers. `examples/sample-portfolio.md` and `examples/sample-portfolio-2.md` show the expected shape of a markdown export (and double as the eval set — each carries an answer key of planted defects).

## Roadmap

- **Historical drift tracking** — compare a team's OKRs quarter-over-quarter to surface silently dropped KRs, moving goalposts, and recycled objectives.
- **Scoring calibration set** — a labelled corpus of real-world (anonymized) OKRs with agreed rubric scores, to keep 0–4 scoring consistent across model versions.
- **CI eval harness** — automated evals (via skill-creator's eval tooling) that run the skill against each fixture under `examples/` and assert its eval criterion — all planted defects found by ID, zero fabricated quotes, no more findings beyond the answer key than its stated budget — so regressions fail CI. (The OPSX verify gate already runs a scoped version of this fixture eval on every skill-content change; docs-only changes skip it.)
- **More fixtures** — larger portfolios (8–12 teams). (Full-catalog defect coverage landed with `examples/sample-portfolio-2.md`, which plants the 13 modes fixture 1 leaves uncovered; both fixtures carry near-miss non-defects to measure false-positive rate.)
