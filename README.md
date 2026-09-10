# OKR-Ninja

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for Claude Code that audits **OKRs — one team or a whole portfolio** — on two axes:

1. **Goodness** — are the objectives and key results well-formed? (outcome vs. task, baselines, measurability, ambition, vanity metrics, and more)
2. **Alignment** — do the teams' OKRs fit together? (unacknowledged dependencies, metric tug-of-wars, duplicated objectives, timeline mismatches, resource contention)

Every finding is backed by a **verbatim quote and a source ref** (Confluence page title, Jira issue key, or file path + heading/line — the exact format is defined in `references/report-format.md`). No quote, no finding.

## Who it's for, when it runs, and what it's for

**One reader per mode.** Portfolio mode is written for an **exec or portfolio owner** — a VP, chief of staff, or founder with authority across the teams in scope — reading for organizational OKR quality and cross-team alignment. Single-team mode is written for the **lead of the team under review**. The two connect through §6 of the portfolio report: the exec gets a ready-to-paste single-team prompt, and the lead runs it on their own team.

**Target use-case: cross-cycle drift tracking** — comparing a team or a portfolio quarter over quarter for silently dropped KRs, moving goalposts, and recycled objectives. The skill as built assumes something narrower: a **pre-commit draft review**, where the OKR text is still editable so a concrete rewrite is directly actionable. That gap is known and additive, not a contradiction to patch in place — drift tracking needs a per-cycle store plus tracking-continuity dimensions, and it is the roadmap's centre of gravity. A review run mid-quarter or later should convert rewrite recommendations into guardrails and escalations, because the text is no longer editable.

**What the report is for — four jobs, in build order, which is also the tie-break order:**

1. **Input to a planning conversation** *(portfolio mode; built)* — surface the two or three cross-team collisions worth an hour of humans' time. The ~10-line verdict, the ≤10-item action list, and the both-sides evidence rule exist for this reader. Where depth and brevity conflict in portfolio mode, brevity wins.
2. **Punch list a lead works through** *(single-team mode; built, depth parity pending)* — exhaustive scoring and a concrete rewrite for every Critical and Major finding. Here depth wins over brevity.
3. **Coaching artifact** *(unbuilt; arrives with drift tracking)* — quarter-over-quarter comparison only pays off if the reader learns between cycles, so the teaching voice lands with the drift work rather than ahead of it.
4. **Quality gate before OKRs are locked** *(deliberately last)* — gating on roll-up grades requires scores reproducible across model versions, which the scoring calibration set does not yet provide. Until it does, grades route follow-up (§6) and gate nothing.

**Distribution: a portfolio / demo piece.** Spec discipline and eval rigor are the product, which ranks eval and calibration work above new detection features. Two consequences: the rubric's doctrine stays fixed and opinionated — outcome over output, baselines mandatory, sandbagging treated as a defect — and per-org configurability is an explicit non-goal, even though an org running Google-style aspirational 0.7 targets would need AP-06 and K3 relaxed. Fixtures stay fictional for demo safety as much as for hygiene.

## Scope: two modes, one skill

The skill is closed and self-contained. Team count at scope intake selects the mode:

| | **Portfolio mode** (2+ teams) | **Single-team mode** (exactly 1 team) |
|---|---|---|
| Core question | Do these OKRs fit *together*? Are there systemic quality problems? | Are this team's OKRs *deeply* sound? |
| Goodness depth | Screening: rubric scores + top findings per team | Exhaustive: every objective and KR scored, full anti-pattern sweep, a rewrite for every Critical/Major finding |
| Alignment analysis | Yes — cross-team failure modes are a first-class output | No cross-team findings (one team can't supply both sides' quotes); dependency mentions become labeled, unverified notes |
| Report | Six-section portfolio report with heatmap | Single-team report (defined in `references/report-format.md`) |
| Follow-up | §6 recommends single-team re-runs for teams that score badly | — |

Both modes share the same rubric, severity scale, source-ref format, and evidence rules.

## Repository layout

```
OKR-Ninja/
├── SKILL.md                        # Skill entry point: trigger description + procedure
├── references/
│   ├── goodness-rubric.md          # Scoring dimensions (O1–O4, K1–K7), AP-XX anti-patterns, roll-up
│   ├── alignment-taxonomy.md       # AL-XX cross-team failure modes and how to detect them
│   └── report-format.md            # Output contract: severity scale, source-ref format, report templates
├── examples/
│   ├── sample-portfolio.md         # Fixture 1: fictional 4-team portfolio with planted defects + generated answer key
│   └── sample-portfolio-2.md       # Fixture 2: fictional 5-team portfolio covering the catalog modes fixture 1 leaves uncovered
├── evals/
│   ├── keys/                       # Canonical JSON answer keys (the fixtures' answer-key sections are generated from these)
│   ├── prompts/                    # Frozen run-prompt templates (portfolio, single-team)
│   ├── grader/                     # harness.py — deterministic grader/planner/scorecard (stdlib only) + selftest corpus
│   └── runs/                       # Committed eval batches: reports, grades, scorecards
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

- "Sweep the Q3 OKRs for Payments, Growth, Platform, and Data and tell me where they conflict." *(portfolio mode)*
- "Audit our whole portfolio of OKRs in the PLANNING Confluence space — quality and cross-team alignment." *(portfolio mode)*
- "Are any of our teams' OKRs pulling against each other this quarter?" *(portfolio mode)*
- "Here are OKR exports for six squads (attached markdown files) — find duplicated objectives and unowned dependencies." *(portfolio mode)*
- "Review the Payments team's OKRs." *(single-team mode)*
- "Are the Platform squad's KPIs any good?" *(single-team mode)*

Prompts asking to write new OKRs from scratch ("draft OKRs for my team") are out of scope and should not trigger the skill.

## Data sources

**Atlassian MCP (preferred).** If an Atlassian MCP server is connected, the skill searches Jira via JQL and Confluence via CQL to locate each team's OKR pages/issues, and cites Confluence page titles and Jira issue keys in every finding.

**Local files (fallback).** With no MCP connected, point the skill at local exports — markdown, CSV, or spreadsheet files containing the OKRs. Findings then cite file paths with headings and line numbers. `examples/sample-portfolio.md` and `examples/sample-portfolio-2.md` show the expected shape of a markdown export (and double as the eval set — each carries an answer key of planted defects).

## Roadmap

- **Single-team depth parity** — close the gaps left by absorbing single-team review with the existing rubric machinery: tracking-continuity and claimed-vs-actual-tracking dimensions (Jira activity vs stated cadence), a computed /100 headline score, deterministic check scripts (placeholder detection, coverage counts, score caps), and a dedicated single-team fixture with its own answer key (today single-team mode is evaluated via fixture 1's Platform slice).
- **Historical drift tracking** — compare a team's OKRs quarter-over-quarter to surface silently dropped KRs, moving goalposts, and recycled objectives.
- **Scoring calibration set** — a labelled corpus of real-world (anonymized) OKRs with agreed rubric scores, to keep 0–4 scoring consistent across model versions.
- **Eval harness (landed)** — `evals/` holds canonical JSON answer keys, a deterministic grader with self-tests, and the `/okr-eval` command, which runs the skill against each fixture as subagents on your Claude Code subscription (no API tokens) and grades every report: all planted defects found by canonical ID, zero fabricated quotes, no more counted findings beyond the key than its budget. Tiers: `smoke` (1 run per slice, wired into the OPSX verify gate), `candidate` (5 runs per slice, one arm), `baseline` (5 runs per slice at a git ref) and `decision` (5 runs per slice per arm, old skill vs new, with a fixed regression rule). Scorecards live under `evals/runs/`.
- **Known open item** — a recurring extra finding: AP-10 BAU Dressed as OKR reported against Platform Objective PL1 in 7 of 10 fixture-1 runs. It is either a fixture-wording ambiguity (the objective reads "Keep the lights on, cheaper") or over-eager AP-10 detection; it needs one triage decision, then either a fixture edit or a rubric edit. Until then it consumes budget on every fixture-1 run.
- **Still open** — a headless `claude -p` driver for CI, and automated routing tests for the skill description (not observable from subagent output).
- **More fixtures** — larger portfolios (8–12 teams). (Full-catalog defect coverage landed with `examples/sample-portfolio-2.md`, which plants the 13 modes fixture 1 leaves uncovered; both fixtures carry near-miss non-defects to measure false-positive rate.)
