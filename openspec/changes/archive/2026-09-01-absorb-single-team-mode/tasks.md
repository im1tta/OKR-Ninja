# Tasks — absorb-single-team-mode

## 1. Report contract (references/report-format.md)

- [x] 1.1 Rewrite §6 from "Suggested deep dives" to "Suggested single-team re-runs": same computed criteria and governing roll-up wording, recommendation text becomes "re-run this skill on <team> alone", ready-to-paste prompt must carry team, period, that team's known source location(s), and the strategy doc if in scope; update the fictional example to match. Verify: no "okr-deepdive" in the file; example prompt names team, period, source, strategy context.
- [x] 1.2 Add a "Single-team report" section defining the single-team template per spec `review-modes`: verdict-first summary; one-team score table (same 11 columns + roll-up line, stated by reference to §2 conventions); AP-XX findings reusing §3's template verbatim by reference; mandatory "Outbound dependency notes" section (verbatim quote + source ref, unverified label, no severity, explicit "none found" line when empty); prioritized action list by reference to §5; explicit exclusions (no heatmap, no AL-XX blocks, no §6). Verify: section present; defines by reference, not by copying §1–§5 content (one-owning-file rule).

## 2. Rubric threshold wording (references/goodness-rubric.md)

- [x] 2.1 Repoint line ~144's needs-rework threshold text from "route teams to the okr-deepdive skill" to the internal single-team-mode re-run via report-format §6, keeping the threshold itself (D or below) and the "roll-up governs routing" rule byte-for-byte in meaning. Verify: no "okr-deepdive" in the file; threshold definition and governing-computation language unchanged otherwise. (No rubric dimension/anti-pattern content changes, so no new example is required.)

## 3. Procedure and description (SKILL.md)

- [x] 3.1 Rewrite the frontmatter description to claim BOTH portfolio and single-team OKR review per design D8: add single-team trigger examples (e.g. "review the Payments team's OKRs"), keep the writing-new-OKRs-from-scratch exclusion, remove all okr-deepdive naming. Verify: description mentions no other skill; contains both a single-team and a portfolio example prompt.
- [x] 3.2 Step 1: replace the "exactly ONE team → stop and recommend okr-deepdive" rule with the mode switch (1 team → single-team mode, 2+ → portfolio mode, announced with scope confirmation); update the intro paragraph (line 8) to describe both modes. Verify: single-team requests are handled, not referred out.
- [x] 3.3 Step 3: add the depth clause — screening depth in portfolio mode (unchanged text), exhaustive scoring + evidence for every notable score + mandatory Critical/Major rewrites in single-team mode; drop the "do not deep-dive here" referral (line 46) in favor of mode language. Verify: both depths described; no referral remains.
- [x] 3.4 Step 4: add the mode gate — in single-team mode AL-XX analysis is skipped, outbound dependency mentions become labeled notes, strategy doc (when provided) feeds O4 evidence; portfolio behavior untouched. Verify: gate present; AL taxonomy semantics not restated in SKILL.md.
- [x] 3.5 Step 6 + Boundaries: point report production at the mode's template in report-format.md; rewrite Boundaries (line 84) to drop the okr-deepdive route and state the two modes + retained exclusions (no OKRs from scratch, read-only). Verify: no "okr-deepdive" anywhere in SKILL.md; `wc -l` ≤ ~150.

## 4. Eval slice (examples/sample-portfolio.md)

- [x] 4.1 Append the "Single-team eval slice (Platform)" subsection to fixture 1's answer key per spec `eval-fixtures`: input scope (Platform section + Q2 appendix, no priorities page), expected G4/G5/G7 by canonical ID (G5 requiring both-document quotes), zero AL-XX findings, zero fabricated quotes, extra-findings budget 1, out-of-scope-content rule. Verify: slice present at the key's end; portfolio eval criterion, defect rows, budgets, and non-defect list above it are byte-identical to before.

## 5. Repo rules and docs (CLAUDE.md, README.md)

- [x] 5.1 CLAUDE.md: rewrite the purpose line (repo owns single-team AND multi-team review); replace the description-editing rule (b/c clauses about okr-deepdive) with the closed-skill routing rule (must claim both modes, must keep the from-scratch exclusion, must not name external skills); flip testing step 4 to the three-case routing check (single-team prompt triggers, portfolio prompt triggers, write-new-OKRs prompt does not); sweep remaining mentions (file-map row notes, testing step 1 wording if needed). Verify: no "okr-deepdive" in the file; testing section states the three-case check.
- [x] 5.2 README.md: replace "How it relates to okr-deepdive" with a two-mode Scope section (portfolio mode + single-team mode, mode switch by team count); update usage examples to include a single-team prompt; update the routing line (70); add the Roadmap follow-up item for depth-parity gaps (tracking-continuity and claimed-vs-actual dimensions, computed /100 headline score, deterministic check scripts, dedicated single-team fixture). Verify: no "okr-deepdive" in the file; Roadmap lists the parity follow-up.

## 6. Workflow context (openspec/config.yaml, loop refine phase)

- [x] 6.1 openspec/config.yaml: replace the sibling-boundary context bullet (lines 18–20) with the closed-skill posture (two modes, one skill; description must claim both and exclude from-scratch writing). Verify: no "okr-deepdive" in the file; `openspec validate --strict` (or `openspec doctor`) still parses config.
- [x] 6.2 .claude/skills/openspec-loop/phases/refine.md: rewrite the skill-routing blindspot (line 21) to guard the two-mode boundary (mode switch semantics + description claiming both modes) instead of the sibling boundary. Verify: no "okr-deepdive" in the file.

## 7. Change-complete verification

- [x] 7.1 Repo-wide sweep: `grep -ri "okr-deepdive"` from repo root — excluding `.git`, `openspec/changes/archive/`, and this change's own artifacts under `openspec/changes/absorb-single-team-mode/` (they document the removal and move into the archive at completion) — returns zero matches; the same sweep for "deep dive"/"deep-dive" surfaces no external-skill referrals. Verify: sweep output clean outside the change's own artifacts.
- [x] 7.2 Run the verify gate (structural checks + fixture evals scoped per `.claude/skills/openspec-loop/phases/verify-gate.md`). Result: structural checks green (frontmatter parses, 88 lines, all referenced paths resolve, lifecycle contract intact); independent refute-mode spec verification green after one repair cycle (4 violations fixed: O4/no-strategy-doc spec-vs-rubric contradiction, §6 fixture-universe leak, stale H1, task 7.1 wording); routing sanity 6/6; single-team slice green (G4/G5/G7 by ID, zero AL-XX, O4 N/A + gap note, 1 extra finding within budget, quotes verified); fixture 2 green (13/13, zero extras, quotes verified). Fixture 1: 13/14 in two independent runs — every touched-category behavior correct; the sole miss both times is A1 (AL-02 mechanism-level conflict), an untouched, pre-existing detection weakness (runs apply only metric-identity blocking, never the heuristic's mechanism-pair clause) — surfaced per the gate's honesty rule and filed as follow-up work outside this change's scope (AL-XX detection changes are a design non-goal).
