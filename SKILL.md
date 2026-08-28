---
name: okr-ninja
description: Portfolio-wide OKR audit and cross-team alignment analysis across MULTIPLE teams, squads, or projects. NOT for a single team — any single-team question, including whether ONE team aligns with company strategy, routes to the okr-deepdive skill; only multi-team analysis belongs here. Not for writing new OKRs from scratch. Use whenever someone wants to review, audit, score, or compare the OKRs, goals, targets, or roadmaps of more than one team at once, or check whether teams line up with each other or with company strategy — e.g. "audit all our teams' OKRs", "do our Q3 OKRs line up across squads", "find alignment gaps between Payments and Platform", "portfolio OKR review". Trigger even when the user doesn't say "OKR" — any request to assess whether multiple teams' goals, targets, or plans are consistent, non-overlapping, and strategy-aligned. Detects cross-team dependency gaps, conflicting or duplicated objectives, orphaned goals, and broken strategy traces, with verbatim quoted evidence.
---

# OKR-Ninja: Portfolio OKR Audit & Cross-Team Alignment

You are auditing OKRs across a **portfolio of teams**. Your job is breadth (every team screened, alignment checked across the portfolio), not depth on any single team — depth is `okr-deepdive`'s job; hand off to it when warranted. Any single-team question — including whether ONE team aligns with company strategy — routes to `okr-deepdive`; only multi-team analysis belongs here.

**Non-negotiable rule:** every finding must trace to verbatim quoted source text with a source ref (format defined in `references/report-format.md`). No quote, no finding. Paraphrase is never presented as a quote.

## Step 1 — Scope intake

Establish, asking the user only for what you cannot infer:

- **Teams/projects:** If named, use those. If the user says "all", enumerate: Jira projects via `getVisibleJiraProjects`, Confluence spaces/OKR pages via CQL (e.g. `title ~ "OKR" AND type = page`), or team sections/files in the provided local exports. Show the enumerated list and confirm it before proceeding — do not silently audit teams the user didn't expect.
- **Period:** Which quarter/cycle. Default to the current quarter and say so.
- **Sources:** Atlassian MCP (Jira via JQL, Confluence via CQL) when connected; otherwise local files (markdown/CSV/spreadsheet OKR exports). If both exist, ask which is canonical.
- **Strategy doc (optional):** A company/org strategy page, if one exists, enables strategy-trace analysis in Step 4.

If exactly ONE team is in scope — even for a strategy-alignment question — stop and recommend `okr-deepdive` instead.

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

Load `references/goodness-rubric.md` and score each team against it: score each objective on O1–O4, each KR on K1–K5, and each KR-set on K6–K7, supporting notable scores with at most 1–2 quoted examples — screening depth, not an exhaustive per-KR critique. Then compute each team's **team dimension scores** using the rubric's aggregation rule, yielding one integer (or N/A) per team for each of the 11 dimensions O1–O4, K1–K7 — exactly the 11 columns of the portfolio heatmap. Also compute each team's roll-up grade per the rubric; the report's §6 uses that grade (not the heatmap integers) to decide deep-dive handoffs.

Do not deep-dive a struggling team here — a team meeting the handoff criteria in `references/report-format.md` §6 gets an `okr-deepdive` recommendation in the report instead.

## Step 4 — Cross-team alignment analysis

Load `references/alignment-taxonomy.md` and apply it:

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

Load `references/report-format.md` (at this step) and produce the six sections it defines, exactly as it defines them. Section structure, finding templates, the severity scale, the source-ref format, and the deep-dive handoff criteria all live in that file — do not improvise alternatives here.

## Execution model: fan-out vs sequential

**When the harness supports subagents/parallel workflows:** fan out — one extractor subagent per team (Step 2); one alignment-checker subagent per blocked candidate set from Step 4 (never one per team pair); and a verifier subagent per finding batch (Step 5) that receives only the finding plus raw source text, so verification is independent of the reasoning that produced the finding. Cap concurrency sensibly (~5 parallel agents) and merge extractor output into the normalized structure before Step 4's blocking runs.

**When it doesn't:** run the same steps sequentially — one team, then one candidate set at a time — writing each team's normalized extraction to a scratch file before moving on so context loss cannot corrupt earlier extractions. The verification pass still runs as a distinct step over the scratch files — never merged into report writing.

## Boundaries

- Any single-team question — a deep dive, a score, or whether ONE team aligns with company strategy → `okr-deepdive`. Only multi-team analysis belongs here.
- Writing new OKRs from scratch → out of scope; offer only rewrites grounded in existing quoted text, within report recommendations, with any invented numbers following report-format §3's placeholder convention.
- Never modify Jira issues or Confluence pages — this skill is read-only.
