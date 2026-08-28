# CLAUDE.md — for agents developing this repo

This repo is an Agent Skill ("okr-ninja") that audits multi-team OKR portfolios for quality ("goodness") and cross-team alignment. It complements the sibling skill `okr-deepdive`, which owns single-team deep dives; this repo owns everything multi-team.

## File map and ownership (no duplication between files)

| File | Owns | Must NOT contain |
|---|---|---|
| `SKILL.md` | Trigger description (frontmatter) + the step-by-step review procedure, pointers to references | Rubric dimension definitions, alignment failure-mode definitions, output templates, severity definitions |
| `references/goodness-rubric.md` | The ONLY home of rubric dimensions (O1–O4, K1–K7), 0–4 scoring anchors, team-dimension aggregation and roll-up rules, and the AP-XX anti-pattern catalog | Alignment content, report/finding templates, severity-scale definitions |
| `references/alignment-taxonomy.md` | The ONLY home of AL-XX cross-team failure modes and their detection heuristics | Goodness/rubric content, report/finding templates, severity-scale definitions |
| `references/report-format.md` | The ONLY home of output/finding templates, the Critical/Major/Minor severity scale, and the source-ref format | Rubric or taxonomy definitions (it references them by ID and canonical name only) |
| `examples/sample-portfolio.md` | Test fixture: fictional company priorities + 4-team portfolio with planted defects; the answer key, intentional non-defects list, and eval criterion live at the bottom | Real company data |
| `README.md` | Human-facing overview, install, usage | Procedure details agents follow |
| `openspec/` + `.claude/` | OPSX change-of-record scaffold, commands, and skills (see Change workflow below) | Skill content |

If a rubric dimension needs explaining, it goes in `references/goodness-rubric.md` and everywhere else refers to it by name. Same rule for failure modes (`references/alignment-taxonomy.md`), and for templates, severities, and source-ref formats (`references/report-format.md`).

## Editing rules

- **Keep `SKILL.md` under ~150 lines.** If an edit pushes it past that, move detail into the appropriate `references/` file instead.
- **Every rubric or taxonomy change needs a matching example in the same file.** For a goodness anti-pattern: a bad OKR (before) and its concretely rewritten form (after) — actual replacement text, not advice about writing one. For an alignment failure mode: a scenario narrative plus the detection heuristic that catches it may stand in for an after-state. A new anti-pattern or failure mode without its example does not merge.
- **One severity scale: Critical / Major / Minor**, defined only in `references/report-format.md`. Anti-patterns and failure modes assign severities using those names and point there for definitions. Never define severity levels anywhere else.
- **AP-XX and AL-XX IDs are frozen.** Never renumber or rename an existing ID; new entries append at the end of their catalog. Every cross-file mention uses "AP-XX <canonical name>" / "AL-XX <canonical name>" exactly as the owning file spells it.
- **Frontmatter `description` edits must keep the `okr-deepdive` disambiguation intact.** The description must continue to (a) claim multi-team/portfolio/alignment work, (b) explicitly exclude single-team deep dives, and (c) name `okr-deepdive` as the handoff for those. Never let the two descriptions overlap enough that the skill router could pick either for the same prompt.
- Findings-must-quote-evidence is a core invariant. Do not add any procedure step or template field that lets a finding exist without a verbatim quote + source ref (format in `references/report-format.md`).
- Fictional content in examples must stay clearly fictional (invented company/team names, no real people).

## Change workflow (OPSX)

This repo uses OpenSpec (OPSX) as its change-of-record system. Any non-trivial change goes through `/opsx:propose` → apply → verify → archive (or the combined `/opsx:loop`). The verify step runs the quality gate defined in `.claude/skills/openspec-loop/phases/verify-gate.md`: structural checks over the repo files plus the fixture eval against the answer key in `examples/sample-portfolio.md`. The OPSX scaffold lives in `openspec/`; the commands and skills live under `.claude/commands/opsx/` and `.claude/skills/openspec-*`.

## Testing changes

1. Run the skill against the fixture: ask Claude Code (with this skill installed) to "audit the OKR portfolio in `examples/sample-portfolio.md` for quality and cross-team alignment."
2. Grade the output against the **answer key at the bottom of `examples/sample-portfolio.md`** (section `## Answer key (planted defects)`) using the fixture's eval criterion: all planted defects found by ID, zero fabricated quotes, and no more findings beyond the key than its stated budget. The key's `## Intentional non-defects` list enumerates near-misses that must not be reported.
3. If you changed the rubric or taxonomy, verify the affected dimension/failure mode still catches its corresponding planted defect(s).
4. If you changed the `description`, sanity-check routing: a single-team prompt ("review the Payments team's OKRs") must NOT trigger this skill, and a portfolio prompt must.
5. When adding a new anti-pattern or failure mode, also plant a matching defect in the fixture, add its ID'd row to the answer key, and update the key's stated defect count — the fixture doubles as the eval set.
6. The OPSX verify gate (see Change workflow) automates the structural checks and, for skill-content changes, a fixture eval scoped to the touched category; the full-fixture run and the routing sanity-check (steps 1–4) remain the manual pre-merge test.
