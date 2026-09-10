---
name: okr-ninja
description: OKR audit for a single team or a whole portfolio — quality ("goodness") review of objectives and key results, cross-team alignment analysis when multiple teams are in scope, and full-depth single-team review when one is. Not for writing new OKRs from scratch. Use whenever someone wants to review, audit, score, critique, or compare the OKRs, goals, targets, or roadmaps of one or more teams, squads, or projects, or check whether teams line up with each other or with company strategy — e.g. "audit all our teams' OKRs", "do our Q3 OKRs line up across squads", "find alignment gaps between Payments and Platform", "review the Payments team's OKRs", "are the Platform squad's KPIs any good", "portfolio OKR review". Trigger even when the user doesn't say "OKR" — any request to assess whether a team's or several teams' goals, targets, or plans are well-formed, consistent, non-overlapping, or strategy-aligned. Portfolio runs detect cross-team dependency gaps, conflicting or duplicated objectives, orphaned goals, and broken strategy traces; single-team runs score every objective and key result in depth — always with verbatim quoted evidence.
---

# OKR-Ninja: OKR Audit — Portfolio & Single-Team

You are auditing OKRs in one of two modes, selected by team count at scope intake (Step 1): **portfolio mode** (2+ teams — breadth: every team screened, alignment checked across the portfolio) or **single-team mode** (exactly one team — depth: every objective and KR scored exhaustively; no cross-team analysis). Both are this skill's job.

**Non-negotiable rule:** every finding must trace to verbatim quoted source text with a source ref (format defined in `references/report-format.md`). No quote, no finding. Paraphrase is never presented as a quote.

## Step 1 — Scope intake

Establish, asking the user only for what you cannot infer:

- **Teams/projects:** If named, use those. If the user says "all", enumerate: Jira projects via `getVisibleJiraProjects`, Confluence spaces/OKR pages via CQL (e.g. `title ~ "OKR" AND type = page`), or team sections/files in the provided local exports. Show the enumerated list and confirm it before proceeding — do not silently audit teams the user didn't expect.
- **Period:** Which quarter/cycle. Default to the current quarter and say so.
- **Sources:** Atlassian MCP (Jira via JQL, Confluence via CQL) when connected; otherwise local files (markdown/CSV/spreadsheet OKR exports). If both exist, ask which is canonical.
- **Strategy doc (optional):** A company/org strategy page, if one exists, enables strategy-trace analysis in Step 4.

Exactly ONE team in confirmed scope selects **single-team mode**; two or more select **portfolio mode**. State the selected mode as part of the scope confirmation.

## Step 2 — Extraction

For each team, pull its OKRs and normalize into a common record:

```yaml
team: <name>
source: <source ref — see references/report-format.md>
objectives:
  - text: "<VERBATIM objective text>"
    owner: <named owner or null>
    parent: "<verbatim text of any stated link to strategy/company goal, or null>"
    krs:
      - text: "<VERBATIM KR text>"
        baseline/target: <as stated, verbatim, or null>
    dependencies: ["<verbatim mention of another team/system>", ...]
```

Rules: preserve exact quotes (typos included); record `null` rather than inventing owners, targets, or parents; capture every cross-team mention (team names, shared systems, "depends on", "blocked by", "with X team") — these feed Step 4. Keep the raw source text available for Step 5.

## Step 3 — Per-team goodness screening

Load `references/goodness-rubric.md` and score each team against it: score each objective on O1–O4, each KR on K1–K5, and each KR-set on K6–K7. **Depth by mode** — portfolio mode supports notable scores with at most 1–2 quoted examples (screening depth, not an exhaustive per-KR critique); single-team mode scores exhaustively: every instance scored, every notable score evidenced, the full AP-XX catalog swept, a concrete rewrite prepared for every Critical or Major finding, and — when a strategy doc is in scope — each objective's stated parent traced against it as O4 evidence (the rubric's O4 rules govern throughout, including its no-strategy-source case). Then compute the team dimension scores using the rubric's aggregation rule — one integer (or N/A) per team for each of the 11 dimensions O1–O4, K1–K7 — and each team's roll-up grade per the rubric; in portfolio mode the report's §6 uses that grade (not the heatmap integers) to decide single-team re-run recommendations.

In portfolio mode, do not switch to exhaustive depth for a struggling team mid-run — a team meeting the criteria in `references/report-format.md` §6 gets a single-team re-run recommendation in the report instead.

## Step 4 — Cross-team alignment analysis (portfolio mode only)

**Single-team mode skips this step's alignment analysis entirely** — one team cannot supply both sides' verbatim quotes, so no AL-XX finding is ever produced. Instead: record every cross-team dependency mention as an **outbound dependency note** (verbatim quote + source ref, labeled unverified, no severity) per the single-team template in `references/report-format.md` — strategy tracing, when a doc was provided, already happened inside Step 3's O4 scoring. Then go to Step 5.

In portfolio mode, load `references/alignment-taxonomy.md` and apply it:

1. **Dependency map:** From the extracted dependency mentions, build the directed team-to-team map. Check each edge for reciprocation — if team A's KR depends on team B, does anything in B's OKRs commit to delivering it? Unreciprocated edges are findings.
2. **Strategy trace:** If a strategy doc is in scope, trace each objective to a stated strategic pillar. Orphaned objectives (no trace) and unstaffed pillars (no team's objective serves them) are findings.
3. **Blocked candidate generation, then checks:** Never compare all pairs of teams or KRs. First group extracted items into candidate sets using the taxonomy's blocking keys; then run the taxonomy's detection checks (conflicts, duplication/overlap, metric incompatibilities, and its other failure modes) only within each candidate set, followed by the taxonomy's disconfirming checks before any finding stands.

Every alignment finding must cite quoted evidence from **both** sides (or from the objective and the strategy doc), and record — per the taxonomy's evidence rules — which detection check fired, which disconfirming checks were run and their results, inference labels on any inferred link, and a CONFIRMED or PLAUSIBLE verdict.

## Step 5 — Verification pass

Before writing the report, re-check every finding against the stored source text:

- Confirm each quote appears verbatim in its cited source. A quote that doesn't match exactly is corrected from the source or the finding is dropped.
- Confirm the finding's claim actually follows from the quotes alone, without unstated assumptions. If the evidence only partially supports it, downgrade the severity, narrow the wording, and (for alignment findings) mark the verdict PLAUSIBLE rather than CONFIRMED; if it doesn't support it, drop it.
- Confirm no finding relies on content you inferred, remembered, or paraphrased rather than extracted.

Silently dropping weak findings is correct behavior, not lost work.

## Step 6 — Report

Load `references/report-format.md` (at this step) and produce the report for the selected mode exactly as that file defines it — the six portfolio sections, or the Single-team report. Section structure, finding templates, the severity scale, the source-ref format, and the re-run criteria all live in that file — do not improvise alternatives here.

## Step 7 — Publish

Skip this step entirely for runs against any of this skill's own fixtures — the files under the `examples/` directory that ships with it — and any eval run — those never publish artifacts or write a registry. Otherwise, publish the report deliverables by following the **"Artifact lifecycle"** section of `references/report-format.md` exactly: the per-portfolio `artifacts.json` registry decides update-vs-create; never create a duplicate artifact for a registered deliverable.

## Execution model: fan-out vs sequential

**When the harness supports subagents/parallel workflows:** fan out — one extractor subagent per team (Step 2); one alignment-checker subagent per blocked candidate set from Step 4 (never one per team pair); and a verifier subagent per finding batch (Step 5) that receives only the finding plus raw source text, so verification is independent of the reasoning that produced the finding. Cap concurrency sensibly (~5 parallel agents) and merge extractor output into the normalized structure before Step 4's blocking runs.

**When it doesn't:** run the same steps sequentially — one team, then one candidate set at a time — writing each team's normalized extraction to a scratch file before moving on so context loss cannot corrupt earlier extractions. The verification pass still runs as a distinct step over the scratch files — never merged into report writing.

## Boundaries

- One team in scope → single-team mode (full-depth goodness, outbound dependency notes, no cross-team findings); two or more → portfolio mode. Both belong to this skill — never refer OKR review elsewhere.
- Writing new OKRs from scratch → out of scope; offer only rewrites grounded in existing quoted text, within report recommendations, with any invented numbers following report-format §3's placeholder convention.
- Never modify Jira issues or Confluence pages — this skill is read-only.
