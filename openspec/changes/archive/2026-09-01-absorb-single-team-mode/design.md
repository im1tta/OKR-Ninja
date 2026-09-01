# Design — absorb-single-team-mode

## Context

See `proposal.md` — Why. Current state that shapes the approach:

- `SKILL.md` (87 lines) is a 7-step portfolio procedure; okr-deepdive appears in its description and at 4 body points (lines 8, 21, 46, 84). The ~150-line budget leaves ~60 lines of headroom.
- `references/report-format.md` owns all templates/severities/source-refs; §6 "Suggested deep dives" recommends the external skill. `references/goodness-rubric.md:144` defines the needs-rework threshold *in terms of* okr-deepdive routing.
- The AP-XX catalog (15 entries, frozen IDs) plus O4 Strategic Anchoring already cover everything single-team depth needs — including strategy tracing — without touching the AL taxonomy.
- Fixture 1 (Brightledger) plants three Platform goodness defects (G4 AP-02, G5 AP-06 cross-source, G7 AP-04) and no Platform-internal non-defect traps: a clean single-team eval slice.
- Repo conventions this change must obey: one owning file per topic, frozen IDs, one severity scale, evidence invariant, fictional fixtures.

## Goals / Non-Goals

**Goals:**
- Single-team mode lands as a *branch of the existing procedure*, not a second procedure — minimal new text, no duplicated machinery.
- Every okr-deepdive reference outside `openspec/changes/archive/` is removed in the same change (no half-closed intermediate state).
- The mode has eval coverage the verify gate can run immediately.

**Non-Goals (design-level; proposal lists scope non-goals):**
- No changes to AL-XX detection semantics, blocking keys, or verdict discipline.
- No new report machinery beyond one template section; no per-mode severity or source-ref variants.

## Decisions

**D1 — Mode switch lives in Step 1 as a scope outcome, not a user flag.**
Team count in *confirmed scope* decides the mode (1 → single-team, 2+ → portfolio), announced with the scope confirmation. Alternatives: a user-facing mode argument (rejected: users say "review team X", they don't pick modes); a separate skill file per mode (rejected: splits ownership, re-creates the routing problem we're deleting).

**D2 — Single-team depth = same rubric, exhaustive application; the *only* lever is coverage.**
Portfolio Step 3 screens (1–2 quoted examples per notable score); single-team mode scores every instance and evidences every notable score, plus mandatory rewrites for Critical/Major. No D1–D9 port, no /100 score (refinement decision; parity gaps go to the Roadmap). This keeps one vocabulary and zero new reference surface.

**D3 — AL-XX is fully off in single-team mode — including strategy-related modes.**
Even though a strategy doc could supply "both sides" for orphan-objective reasoning, single-team strategy tracing feeds **O4 Strategic Anchoring** (a goodness dimension) instead of AL-04, and portfolio-semantic modes (e.g. coverage gaps) are impossible with one team. Alternative — allow an AL-04/AL-10 subset in single-team mode (rejected: forks the taxonomy's applicability rules by mode, complicates the eval, and O4 already expresses the defect with quoted evidence at the right severity via scores/actions).

**D4 — Outbound dependency mentions become a dedicated no-severity notes section.**
They are quoted verbatim with source refs but explicitly labeled unverified-against-counterparty and are not findings. This preserves the evidence invariant (no one-sided AL claims) without discarding signal the user will want. The section is mandatory in the template (with an explicit "none found" line when empty) so its absence is detectable by the eval.

**D5 — report-format.md gains one "Single-team report" section; §6 is renamed and repointed.**
The single-team template reuses §1's verdict-first rule, §2's score-table conventions (one team, same 11 columns + roll-up line), §3's finding template verbatim, and §5's action-list rules — stated by reference, not copied (one-owning-file rule). §6 becomes "Suggested single-team re-runs": same computed criteria (unchanged governing roll-up), recommendation text now "re-run this skill on <team> alone", and the ready-to-paste prompt **must carry known scope context** (team, period, that team's sources from intake, strategy doc if in scope) so the follow-up run re-asks nothing.

**D6 — Eval slice rides fixture 1 (Platform) instead of a new fixture.**
Platform has 3 separable goodness defects including the cross-source AP-06 (proves single-team mode still applies Part 5's cross-source rule) and tempting alignment bait nearby (its "fully committed" note underlies A5) — a run that resists producing AL findings there demonstrates the mode boundary. Slice inputs exclude the company-priorities page so strategy tracing is exercised via its documented "out of scope" path deterministically. Budget 1 extra finding (proportionate to portfolio's 2-per-14). Alternative — dedicated single-team fixture (deferred to Roadmap; a slice gives coverage now at ~15 lines).

**D7 — SKILL.md edits fold into existing steps to hold the line budget.**
Step 1 gains the mode switch (replacing the recommend-okr-deepdive rule); Step 3 gains one depth clause ("screening in portfolio mode; exhaustive in single-team mode + rewrites"); Step 4 gains a mode gate line (skipped in single-team mode; outbound notes instead; strategy doc → O4); Step 6 points at the mode's template; Boundaries rewritten. Estimated net +12–18 lines → ~100–105 total, within budget.

**D8 — Description rewrite pattern.**
Claim both modes in one sentence each with trigger examples for both ("review the Payments team's OKRs" joins the portfolio examples); keep the writing-new-OKRs exclusion; drop all sibling naming. Length stays within one frontmatter paragraph comparable to today's.

## Risks / Trade-offs

- [Routing collision while the external okr-deepdive remains installed — both descriptions claim single-team prompts] → Documented in proposal Impact and README's migration note; resolution is uninstalling the companion (user's environment, outside repo control). No repo mitigation possible without re-introducing the exclusion this change removes.
- [Description grows too broad and fires on non-OKR prompts] → Keep the existing "goals/targets/roadmaps" vocabulary and the from-scratch exclusion; routing sanity check in CLAUDE.md testing now asserts three cases (single-team triggers, portfolio triggers, write-new-OKRs does not).
- [Single-team run against the shared fixture file can see other teams' sections] → The eval slice defines input scope explicitly (Platform section + appendix); findings grounded outside it count against the budget, making scope discipline itself part of the eval.
- [SKILL.md creep past ~150 lines over time with two modes] → D7 folds branching into existing steps; verify gate's structural check on line count remains the backstop.
- [Exhaustive scoring inflates single-team report length] → The template's verdict-first + score-table conventions cap prose; findings remain severity-ordered blocks, scores live in the table not paragraphs.

## Migration Plan

Single change, docs-only repo — apply edits, run verify gate (structural checks + fixture evals + routing check), archive. Rollback = `git revert` of the change commit; no data or external-state migration. The openspec `config.yaml` context line and loop `refine.md` blindspot update land in the same change so the OPSX workflow never gives stale sibling-boundary guidance to a future change.

## Open Questions

None — refinement resolved mode semantics, depth engine, eval approach, and deferred parity gaps to the Roadmap.
