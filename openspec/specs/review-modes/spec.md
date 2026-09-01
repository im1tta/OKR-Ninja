# review-modes Specification

## Purpose

Defines OKR-Ninja's two review modes — portfolio (2+ teams) and single-team (exactly 1 team) — including how the mode is selected at scope intake, what single-team mode runs at full depth, what it must not produce, the single-team report contract, the portfolio report's internal mode-switch recommendation, and the closed-skill invariant that no repo file references an external OKR skill.

## Requirements

### Requirement: Mode is selected by team count at scope intake

The skill SHALL select its review mode during scope intake from the number of teams in confirmed scope: exactly one team selects **single-team mode**; two or more teams select **portfolio mode**. The skill SHALL state the selected mode to the user before extraction begins. The skill SHALL NOT decline single-team requests or refer them to any other skill.

#### Scenario: Single team in scope

- **WHEN** the confirmed scope contains exactly one team (e.g. "review the Payments team's OKRs")
- **THEN** the skill proceeds in single-team mode, announces it, and runs the review itself rather than recommending another skill

#### Scenario: Multiple teams in scope

- **WHEN** the confirmed scope contains two or more teams
- **THEN** the skill proceeds in portfolio mode with the existing portfolio procedure (screening-depth goodness, cross-team alignment analysis, portfolio report)

### Requirement: Single-team mode applies the goodness machinery at full depth

In single-team mode the skill SHALL score every objective on O1–O4, every KR on K1–K5, and every KR-set on K6–K7 using the 0–4 anchors, aggregation rule, and roll-up grade defined in `references/goodness-rubric.md` — exhaustively (every instance scored and supportable, not the portfolio mode's 1–2-example screening) — and SHALL sweep the full AP-XX anti-pattern catalog. Every Critical or Major finding SHALL include a concrete rewrite (replacement objective/KR text following the report's proposed-number convention). The evidence invariant is unchanged: every finding carries a verbatim quote and source ref, and the pre-report verification pass runs.

#### Scenario: Full-depth scoring of one team

- **WHEN** single-team mode reviews a team with 2 objectives and 6 KRs
- **THEN** the report's score section reflects all 8 objective-dimension scores (2×O1–O4) and all 30+ KR/set-dimension scores (6×K1–K5, plus K6–K7 per KR-set), each low score traceable to quoted evidence, with no objective or KR left unscored

#### Scenario: Critical finding without a rewrite is non-compliant

- **WHEN** a single-team report contains a Critical or Major AP-XX finding with no concrete replacement text
- **THEN** the report violates this specification

### Requirement: Single-team mode produces no cross-team alignment findings

In single-team mode the skill SHALL NOT run AL-XX detection and SHALL NOT report any finding tagged with an AL-XX failure mode: with one team in scope, the taxonomy's requirement of verbatim quotes from both sides cannot be met. Cross-team dependency mentions found in the team's material SHALL be captured in a clearly-labeled **outbound dependency notes** section — each note a verbatim quote plus source ref, explicitly marked as unverified against the counterparty and carrying no severity — and SHALL NOT be presented as findings.

#### Scenario: Dependency mention becomes a note, not a finding

- **WHEN** the reviewed team's KR states "depends on the streaming pipeline migration owned by Platform" and only that team is in scope
- **THEN** the report records it under outbound dependency notes with the verbatim quote and source ref, marked unverified, and no AL-XX finding is created

#### Scenario: AL-tagged finding in a single-team report

- **WHEN** a single-team report contains any finding citing an AL-XX ID
- **THEN** the report violates this specification

### Requirement: Strategy tracing in single-team mode feeds O4, not AL findings

When the user provides a company strategy doc in single-team mode, the skill SHALL trace each objective's stated parent link against that doc during scoring and use the result as quoted evidence for O4 Strategic Anchoring scores (and any applicable AP-XX finding). Absence of a strategy doc SHALL NOT block the run: O4 then follows `references/goodness-rubric.md`'s own rules for the team's corpus — including its no-strategy-source case (O4 = N/A, excluded from roll-up, with the rubric's mandated gap note recorded in the report's score section, not as a findings-section entry) — and the report notes that company-level tracing was out of scope. Strategy tracing in single-team mode SHALL NOT produce AL-XX findings (portfolio-semantic conclusions such as unstaffed pillars require the full portfolio).

#### Scenario: Strategy doc provided

- **WHEN** single-team mode runs with a strategy doc and an objective has no stated link to any pillar in it
- **THEN** the missing trace is reflected in that objective's O4 score with quoted evidence, and no AL-XX finding is produced

#### Scenario: No strategy doc and no strategy source in the corpus

- **WHEN** single-team mode runs without a strategy doc and the team's own material contains no strategy source
- **THEN** the review completes with O4 = N/A per the rubric's no-strategy-source rule, the rubric's gap note recorded in the score section rather than as a findings-section entry, and the report states that company-level strategy tracing was out of scope

### Requirement: Single-team report follows the single-team template

`references/report-format.md` SHALL define a single-team report template, and single-team mode SHALL produce exactly its sections. The template SHALL include: a verdict-first summary; the team's eleven dimension scores (O1–O4, K1–K7) with roll-up grade (letter + numeric); AP-XX findings using the same finding template, severity scale, source-ref format, and proposed-number convention as the portfolio report; outbound dependency notes; and a prioritized action list. It SHALL NOT include a multi-team heatmap, AL-XX finding blocks, or a deep-dive/mode-switch recommendation section.

#### Scenario: Report sections for a single-team run

- **WHEN** single-team mode completes a review
- **THEN** the report contains the verdict summary, the 11-dimension score table with roll-up grade, severity-ordered AP-XX findings each with verbatim quote + source ref, outbound dependency notes (or an explicit "none found" line), and a prioritized action list — and contains no portfolio heatmap and no AL-XX blocks

### Requirement: Portfolio report recommends the skill's own single-team mode

The portfolio report's §6 SHALL recommend a **single-team-mode run of this skill** (not any external skill) for each team meeting the existing criteria — roll-up grade at or below the needs-rework threshold, or any Critical finding — with the rubric roll-up remaining the governing computation. Each recommendation SHALL include a ready-to-paste prompt that carries the scope context already established: the team, the period, the team's source location(s) as known from intake (Confluence space/page, Jira project key(s), or file paths), and the strategy doc if one was in scope.

#### Scenario: Team at the needs-rework threshold

- **WHEN** a portfolio run computes a team's roll-up grade at or below the needs-rework threshold
- **THEN** §6 recommends re-running the skill on that team alone, with a prompt naming the team, period, that team's known source location(s), and the strategy doc when one was provided — and no external skill is named

#### Scenario: No team qualifies

- **WHEN** no team meets either criterion
- **THEN** §6 states that explicitly in one line, unchanged from existing behavior

### Requirement: The repo is closed — no external OKR-skill references

No file in the repo outside `openspec/changes/archive/` SHALL reference `okr-deepdive` or defer any OKR-review behavior to an external skill. The frontmatter `description` SHALL claim both portfolio-wide and single-team OKR review, SHALL retain the exclusion for writing new OKRs from scratch, and SHALL NOT name any other skill as a handoff. Repo guidance (CLAUDE.md testing steps, README, workflow context files) SHALL describe the two-mode routing: a single-team prompt and a portfolio prompt both trigger this skill.

#### Scenario: Repo-wide reference sweep

- **WHEN** the repo is searched for "okr-deepdive" (any casing) outside `openspec/changes/archive/`
- **THEN** there are zero matches

#### Scenario: Routing claims in the description

- **WHEN** the frontmatter description is read
- **THEN** it claims single-team review and portfolio review, contains no reference to another OKR skill, and still excludes writing new OKRs from scratch
