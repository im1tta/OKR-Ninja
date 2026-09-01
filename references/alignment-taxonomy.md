# Cross-Team Alignment Taxonomy & Detection Methodology

This reference defines the misalignment failure modes OKR-Ninja hunts for across a portfolio of teams, and the procedure for finding them without hallucinating. Load it when running a multi-team sweep. Every finding produced from this taxonomy MUST satisfy the evidence discipline in the final section — an alignment claim without verbatim quotes from **both** sides is not reportable.

Wherever this file says **source ref**, use the single format defined in `references/report-format.md` ("Source references" subsection). Do not invent a different citation format.

All examples use a fictional company, **Meridian** (a B2B SaaS), and fictional teams: **Atlas** (platform/infra), **Bluefin** (payments), **Cormorant** (growth), **Dune** (mobile), **Ember** (data), **Foxtrot** (support).

## Severity

Findings from this taxonomy are rated on the single **Critical / Major / Minor** scale defined in `references/report-format.md` ("Severity scale" section). Do not define or use any other levels. Each failure mode below states its default rating and the conditions that move it. Escalate one level (Minor → Major, Major → Critical) when the affected objective is explicitly marked committed (vs. aspirational), is board- or exec-visible, or sits on the critical path of two or more other findings.

---

## Part 1 — Failure mode taxonomy

### AL-01 — Unacknowledged dependency
- **Definition:** Team A's KR requires deliverable work, capacity, or a decision from Team B, and nothing in Team B's OKRs, committed roadmap, or linked issues acknowledges that work.
- **Example:** Bluefin's KR reads "Launch installment payments in EU by Nov 15," which requires Atlas's new ledger service. Atlas's OKRs for the same period mention only "Reduce infra spend 20%" and "Migrate CI to Buildkite" — the ledger appears nowhere.
- **Detection heuristic:** From each KR, extract named systems, platforms, teams, and verbs implying external work ("integrate with," "once X ships," "using the new," "pending," "requires"). Resolve each mention to an owning team. Then search the owner's OKRs *and* their Jira epics/committed backlog for the deliverable. A dependency with no hit on the owner's side is a candidate. If resolution surfaces two or more teams claiming the same owner's capacity while that owner states a capacity constraint, the contention itself is not an AL-01 — it aggregates into AL-07 Resource contention (see its aggregation rule); AL-01 still applies per edge naming a distinct deliverable absent from the producer's plans — not a pure capacity/provisioning ask, which folds into the AL-07 entirely — cross-referencing the AL-07.
- **Evidence required:** (a) A's KR text quoted verbatim with source ref; (b) the dependency phrase itself quoted; (c) a description of the search performed on B's side (which pages/JQL, what terms) and its empty result — you are proving an absence, so the search scope must be stated explicitly; (d) if B has *any* partially matching item, quote it and explain why it does not cover the need.
- **Severity:** Major by default. Critical if A's KR is committed and B has explicitly deprioritized the area ("ledger v2 deferred to Q1" — quote it). Minor if B's backlog contains the work but unscheduled/unsized.

### AL-02 — Conflicting metrics / adversarial incentives
- **Definition:** Two teams' KRs push the same metric in opposite directions, or optimizing one team's KR predictably degrades the other's (perverse incentive), even when the metrics differ by name.
- **Example:** Cormorant: "Increase trial-to-paid conversion to 9% by removing signup friction (drop mandatory email verification)." Foxtrot: "Reduce fraud-driven support tickets 40%." Removing verification is a known fraud vector — Cormorant's lever damages Foxtrot's target.
- **Detection heuristic:** Build the metric catalog (Part 2). Flag (1) same canonical metric appearing in two teams' KRs with opposing directionality (↑ vs ↓, or the same direction with incompatible targets); (2) known tension pairs where one KR's *stated mechanism* is a documented driver of the other's metric — speed vs. quality, acquisition volume vs. unit economics, feature velocity vs. reliability/error budget, discount-driven revenue vs. margin.
- **Evidence required:** Both KRs verbatim with source refs, the shared/coupled metric named, and one sentence stating the causal mechanism. For perverse-incentive pairs (different metrics), the mechanism must come from the teams' own documents where possible (e.g., a quoted retro or RFC noting the tradeoff); otherwise label the mechanism as analyst inference, not fact.
- **Severity:** Critical when directly opposed targets on the same metric; Major for mechanism-level conflicts; Minor if either KR is aspirational or the coupling is speculative.

### AL-03 — Duplicated / overlapping objectives
- **Definition:** Two teams independently pursue substantially the same outcome, with no cross-reference, shared owner, or division of labor between them.
- **Example:** Dune: "Ship in-app onboarding checklist to lift week-1 activation to 55%." Cormorant: "Redesign onboarding flow to lift week-1 activation to 60%." Neither OKR set mentions the other team; both have separate design tracks for the same surface.
- **Detection heuristic:** Cluster objectives and KRs by target metric + target population/surface (same metric alone is insufficient — see false positives). Within a cluster, check for any mutual reference, shared epic, joint owner, or explicit split ("Dune owns mobile surface, Cormorant owns web"). Absence of all of these → candidate duplicate.
- **Evidence required:** Both objectives/KRs verbatim with source refs; statement that no cross-reference was found, with the searched locations listed.
- **Severity:** Major when the targets are inconsistent (55% vs 60% on the same metric — who is accountable?) or the duplicated work involves conflicting technical approaches to one surface; Minor for plain duplication with compatible targets (waste, not failure).

### AL-04 — Orphan objective
- **Definition:** A team objective with no traceable parent in company or department strategy — nothing above it that it claims to serve, explicitly or by reasonable metric linkage.
- **Example:** Meridian's company OKRs are about enterprise expansion and reliability. Ember's objective "Launch internal ML experimentation platform" cites no parent, moves no company-level metric, and no strategy doc mentions ML platforms.
- **Detection heuristic:** Build the strategy trace (Part 2). For each team objective, look for (a) an explicit parent link/label, (b) a KR metric that is a company-level metric or a documented driver of one, (c) a mention in the department strategy page. Zero of three → orphan candidate.
- **Evidence required:** The objective verbatim with source ref; the company/department objective list quoted or precisely cited; the three-way check's results stated. If the team's page contains its own justification ("this enables 2027 platform strategy"), quote it — it may downgrade the finding.
- **Severity:** Major if the orphan consumes a large stated fraction of team capacity ("3 of our 5 engineers" — quote the capacity claim); Minor by default. If the team is explicitly chartered for exploratory work, quote the charter — it may kill the finding.

### AL-05 — Cascade drift
- **Definition:** A child OKR nominally links to a parent objective, but the child's KRs, if fully achieved, would not plausibly move the parent's metric — the link is decorative.
- **Example:** Parent (company): "Reduce enterprise churn from 8% to 5%." Atlas's linked objective: "Support churn reduction" with KRs "Upgrade Kubernetes to 1.31" and "Complete SOC 2 evidence collection." Neither KR has a stated causal path to churn.
- **Detection heuristic:** For each explicit parent link, ask: do the child KRs measure the parent's metric, a documented driver of it, or a deliverable the parent's own page names as needed? If the child KRs are pure activity/output with no stated mechanism, flag. The tell is a linked objective whose KRs could be achieved in a quarter where the parent metric worsens.
- **Evidence required:** Parent objective and metric verbatim; child objective, its link/claim of support, and all child KRs verbatim; explicit statement of which mechanism check failed. All quotes carry source refs.
- **Severity:** Major when the parent is a committed company OKR relying on this child as a named contributor; Minor otherwise.

### AL-06 — Timeline mismatch
- **Definition:** Dependent milestones are sequenced impossibly or implausibly across teams: the consumer's date precedes (or leaves no integration margin after) the producer's date.
- **Example:** Bluefin: "EU installments GA October 31." Atlas (which *does* acknowledge the dependency): "Ledger service beta available December 1." The consumer ships a month before its dependency exists.
- **Detection heuristic:** On the dependency map, compare dates on every edge: producer's delivery date vs. consumer's need-by date. Flag hard inversions (need-by < delivery) and thin margins (< ~2–4 weeks for integration/testing, judged by the work's nature). Also compare milestone dates against the quarter's boundaries — a KR due after the OKR period ends is its own flag.
- **Evidence required:** Both dated statements verbatim with source refs. Dates must be quoted, not inferred; if one side's date comes from Jira due-date fields rather than OKR text, cite the issue key in the source ref and say so.
- **Severity:** Critical for hard inversions on committed KRs; Major for thin margins or inversions on aspirational KRs; Minor when one date is soft ("targeting late Q4").

### AL-07 — Resource contention
- **Definition:** Multiple teams' plans assume the same shared resource — a platform team's roadmap slots, a specialist (security review, legal, data science), an environment, or a budget — with combined demand exceeding any stated supply, or with no supply stated at all.
- **Example:** Bluefin, Dune, and Cormorant each have a Q4 KR requiring "design support from the Platform Design pod." The pod's own OKR page states "capacity for two partner engagements this quarter."
- **Detection heuristic:** Extract every mention of shared teams/pods/functions/environments across all KRs; group by resource; count distinct claimants per quarter. Two or more claimants → check the resource owner's own OKRs/capacity statements for declared supply and an explicit allocation. Overcommitment or silence → flag. **Aggregation and disambiguation vs. AL-01:** contention is a property of the resource node, not of any single edge — classify only after grouping claimants by resource, never edge-by-edge. When two or more claimants land on one owner whose own pages state a capacity constraint (a countable supply, or a statement that the capacity is committed elsewhere), the contention is a single AL-07 candidate — one finding, if it survives the Part 4 disconfirming checks — quoting every claimant and the owner's capacity statement. Per-edge AL-01 findings are not a substitute: filing the claimant edges as AL-01s loses the portfolio-level fact — combined demand against stated supply — that only the resource-node view captures, and under Part 3 §5 the contention's root cause is AL-07, with AL-01 cross-referenced as secondary. An edge whose ask is the owner's capacity itself (provisioning, roadmap slots, review bandwidth) folds into the aggregate entirely. An edge naming a distinct deliverable absent from the producer's plans — work the producer would have to plan as its own project (a build, a migration) beyond allocating capacity or access — additionally earns its own AL-01 finding for that missing deliverable, cross-referencing the AL-07: the missing acknowledgment and the overbooked quarter are different defects, and the capacity arithmetic itself is reported exactly once, under AL-07. When both readings fit an edge (every provisioning ask names the thing provisioned), the capacity-ask clause wins and the edge folds in. A lone claimant on an unacknowledging owner stays AL-01.
- **Disambiguation example (vs. AL-01):** Bluefin's notes assume "Atlas provisions the isolated payments enclave in July"; Ember's notes assume Atlas runs "the warehouse migration" this quarter; Atlas's own page states "Q3 capacity is fully committed to the compliance push and the cost work." Filing each edge as AL-01 misses the contention. The heuristic reading that catches it: grouping resource mentions puts two claimants on Atlas in the same quarter; Atlas's page, checked for declared supply, yields the fully-committed statement — overcommitment, flagged once at the resource node. Correct output: one AL-07 finding quoting both claimants and Atlas's capacity statement (AL-01 as secondary cross-reference) — Bluefin's provisioning ask is a pure capacity claim and folds in entirely — plus one AL-01 finding for Ember's warehouse migration, a named deliverable appearing nowhere in Atlas's plans, cross-referencing the AL-07. Wrong outputs: per-edge AL-01s standing in for the aggregate, or the same capacity arithmetic double-counted across findings.
- **Evidence required:** Each claimant's KR verbatim with source ref; the resource owner's capacity statement verbatim if one exists, or the searched-and-absent statement if not.
- **Severity:** Major when declared supply is exceeded by committed demands; Minor when demand is plural but supply is undeclared (the finding is "nobody has done this arithmetic").

### AL-08 — Terminology collision
- **Definition:** Two forms: (a) **same name, different definition** — two teams use one metric name ("activation," "active user," "uptime") with different formulas, windows, or populations; (b) **different names, same concept** — one underlying metric travels under two names, hiding overlap or conflict from AL-02/AL-03 detection.
- **Example:** (a) Cormorant defines "activated" as "completed 3 key actions in 7 days"; Dune's page defines it as "opened the app twice in 14 days" — both have KRs on "activation rate." (b) Ember's "data freshness SLA" and Atlas's "pipeline latency p95" are, per Ember's glossary page, the same measurement.
- **Detection heuristic:** For every metric name used by ≥2 teams, hunt each team's pages for a definition (formula, window, population, data source) and diff them. For form (b), compare metric *definitions* (not names) across the catalog; near-identical formulas under different names → merge candidates. Definitions absent on both sides is itself a Minor finding (unverifiable metric).
- **Evidence required:** Both definitions (or both KRs plus the absence of definitions) verbatim with source refs. For form (b), quote the text establishing equivalence — do not assert it from intuition.
- **Severity:** Minor by default (including cosmetic drift where the definitions actually match — usually no finding at all); Major when the colliding metric is used in a cross-team target, an exec rollup, or an AL-02/AL-03 pair (it corrupts the comparison).

### AL-09 — Baseline disagreement
- **Definition:** Two teams (or a team and the company page) state different current values for the same metric, so at least one team's target is calibrated against a wrong starting point.
- **Example:** Company page: "NPS currently 31." Foxtrot's OKR: "Raise NPS from 38 to 45." Same survey, same period, seven-point discrepancy — Foxtrot's +7 target may actually be a +14 ask.
- **Detection heuristic:** In the metric catalog, collect every stated baseline ("from X," "currently Y," "baseline: Z") per canonical metric. Any two baselines for the same metric and period that differ beyond rounding → flag. Check first whether an AL-08 definition split explains the gap (different populations legitimately have different values) — if so, report as AL-08 instead.
- **Evidence required:** Both baseline statements verbatim with source refs and their as-of dates. State whether a definitional explanation was searched for and not found.
- **Severity:** Major when the metric carries a committed target; Minor otherwise.

### AL-10 — Strategy coverage gap
- **Definition:** The inverse of AL-04: a declared company or department priority that no team's OKRs address. The portfolio has a hole, not a weed.
- **Example:** Meridian's company OKRs include "O3: Achieve FedRAMP readiness by year-end." A sweep of all six teams finds no objective, KR, or epic mentioning FedRAMP, compliance milestones, or the named workstreams under O3.
- **Detection heuristic:** Run the strategy trace top-down: for each company/department objective and each named KR under it, search all teams' OKRs and linked epics for coverage. Company objectives with zero contributing children → gap. Partial coverage (2 of 5 parent KRs claimed) is reportable too — name the uncovered KRs.
- **Evidence required:** The company objective verbatim with source ref; the search scope stated (teams swept, terms used); any near-miss quoted and distinguished.
- **Severity:** Critical for committed, dated company objectives with zero coverage; Major for partial coverage of committed objectives; Minor for aspirational ones.

### AL-11 — Circular dependency
- **Definition:** A cycle in the cross-team dependency graph: A waits on B, B waits on C, C waits on A (or a direct A↔B mutual wait). No valid execution order exists as written.
- **Example:** Dune's KR: "Adopt unified auth SDK once Atlas ships it." Atlas: "GA the auth SDK after Bluefin validates it in production." Bluefin: "Migrate to unified auth after mobile (Dune) proves the flow." Three teams, each first in line behind another.
- **Detection heuristic:** Purely structural: build the directed dependency graph (Part 2), run cycle detection. Every cycle found is a candidate; then verify each edge's quote still reads as a genuine blocking relationship, not a soft preference ("ideally after").
- **Evidence required:** One verbatim quote per edge in the cycle, each with source ref. Every edge must be quotable — a cycle with one inferred edge is reported as PLAUSIBLE at best, with the inferred edge labeled.
- **Severity:** Critical when all edges are committed KRs; Major when any edge is soft; downgrade to Minor if any team's text shows awareness plus a resolution plan (quote it).

### AL-12 — Commitment asymmetry
- **Definition:** Two teams describe the same shared outcome with mismatched commitment levels or mismatched ambition: A treats it as a committed KR while B lists it as a stretch/aspirational item, or A's target arithmetic silently assumes B achieves 100% of B's stretch target.
- **Example:** Cormorant (committed): "Drive 4,000 signups from the partner marketplace launch." Bluefin's page lists "Partner marketplace" under "Stretch — only if payments migration lands early." Cormorant's committed number depends on Bluefin's explicitly-maybe deliverable.
- **Detection heuristic:** For every acknowledged cross-team dependency (edges that AL-01 did *not* flag), compare the commitment labels on each side (committed/aspirational, P-labels, "stretch," confidence scores) and compare target arithmetic: does A's number require B's full target rather than B's expected value? Mismatched labels or full-target coupling → flag.
- **Evidence required:** Both sides verbatim including the commitment-level wording, with source refs. For arithmetic coupling, show the numbers from both quotes.
- **Severity:** Major when a committed KR depends on an explicitly stretch item; Minor for label ambiguity where one side simply never states a level.

---

## Part 2 — Cross-team analysis procedure

### Step 1: Normalize per-team inventories
For each of the N teams, extract into a uniform structure (before any comparison):
- Team name, source refs for every page/issue read (format: see `references/report-format.md`), OKR period, commitment labels.
- Objectives (verbatim), KRs (verbatim) with: metric name as written, baseline, target, direction, dates, owner.
- **Dependency mentions:** every named external team, system, platform, shared resource, or "after/once/pending/requires/blocked by" phrase, with its verbatim sentence.
- **Definitions:** any stated metric formulas, glossary entries, capacity statements.
Keep verbatim text attached to every extracted field — downstream findings quote from here, and a field that lost its quote cannot be reported.

### Step 2: Build the two core structures
1. **Dependency map** — directed graph. Nodes: teams (plus shared resources as nodes). Edges: consumer → producer, each edge carrying its verbatim quote, need-by date, and commitment level. Add producer-side acknowledgment status per edge (acknowledged / partially / absent) by searching the producer's inventory.
2. **Strategy trace** — tree from company objectives → department objectives → team objectives, using explicit links first, then metric-linkage inference (marked as inferred). Leaves with no parent = AL-04 candidates; parents with no children = AL-10 candidates; links whose child KRs fail the mechanism check = AL-05 candidates.
Also build a **metric catalog**: canonical metric → every (team, KR, name-as-written, definition, baseline, target, direction) tuple. This is the index for AL-02, AL-03, AL-08, AL-09.

### Step 3: Run checks — know what scales
With N teams there are N(N−1)/2 pairs; naive pairwise reading is fine at N≤4 and wasteful beyond. Classify checks:
- **Per-team vs. strategy (O(N)):** AL-04, AL-05, AL-10. Run against the strategy trace, no pairing needed.
- **Graph-structural (near-linear):** AL-01 (edge acknowledgment), AL-06 (edge date comparison), AL-11 (cycle detection), AL-12 (edge label comparison), AL-07 (resource node fan-in). Run on the dependency map.
- **Pairwise, but blocked first:** AL-02, AL-03, AL-08, AL-09. Never compare all pairs of KRs. Block on a candidate key — same canonical metric (AL-02/AL-09), same metric + same surface/population cluster (AL-03), same metric name across teams or near-identical definitions (AL-08) — and only inspect pairs sharing a block. Report the blocking keys used, so a reviewer knows what could have been missed.
At N ≥ ~8 teams, run Steps 1–2 as independent per-team extraction passes (parallel subagents if available) and merge the inventories; only the merged catalog and graph are analyzed jointly.

### Step 4: False-positive controls (disconfirming checks)
Before promoting any candidate to a finding, actively try to kill it. Every failure mode has at least one disconfirming check; run the ones matching the candidate's AL-ID and record each check and its result (the report block in `references/report-format.md` §4 has a slot for them).
- **Missing mention ≠ unacknowledged (AL-01):** the producer may track the work in Jira without an OKR (deliberate — not everything is an OKR). Search the producer's epics/backlog before claiming absence; a scheduled epic downgrades to Minor or kills the finding.
- **Shared metric ≠ conflict (AL-02):** same metric, same direction, compatible targets is *alignment*. Check directionality, check for an explicit shared/parent OKR covering both, check for a documented split of levers. Only opposing directions or a stated adversarial mechanism survive.
- **Similar objectives ≠ duplication (AL-03):** different populations, surfaces, segments, or geographies are legitimate division of labor. Check for cross-references, shared epics, or a parent objective that assigns lanes. Quote the disambiguating text if found, and drop the finding.
- **No parent link ≠ orphan (AL-04):** run the three-way check (explicit link, metric linkage, strategy-page mention) before flagging; inferred parents count against the finding, not for it.
- **Activity KRs ≠ decorative link (AL-05):** the causal mechanism may be documented outside the child's OKR text. Check the parent objective's own page for a list of named contributing workstreams, the child's linked epic descriptions, and strategy docs for a stated driver relationship (e.g., "SOC 2 completion unblocks our two largest enterprise renewals"). If any source names the child's deliverable as a needed contribution to the parent metric, quote it and kill the finding.
- **Late date ≠ inversion (AL-06):** confirm which milestone the consumer actually needs — beta may suffice for their integration even if GA is later. Prefer the tightest quotable reading.
- **Plural demand ≠ contention (AL-07):** the allocation may live outside OKR pages — capacity allocated in Jira (scheduled epics or assignments covering each claimant) rather than on OKR pages falsifies the finding. Check the resource owner's Jira and any capacity/allocation table linked from their pages; also confirm the claims fall in the same quarter and name the same resource, not similarly-named pods. Fully allocated demand kills the finding; a documented but partial allocation downgrades it.
- **Different wording ≠ different definition (AL-08):** normalize both definitions (formula, window, population, data source) before diffing — verbally different texts often reduce to the same measurement. Check page versions/dates: one definition may be superseded by a newer glossary both teams actually use. Definitions that match once normalized, or a superseded page, kill the finding.
- **Different baselines ≠ disagreement (AL-09):** different as-of dates or (per AL-08) different populations can both be right. Check dates and definitions first.
- **Zero hits ≠ coverage gap (AL-10):** re-search under synonyms and program names (FedRAMP work may live under "compliance," an audit program name, or an epic key) and check the company objective's own page for named owners — a priority explicitly assigned to a function outside the swept team set is an ownership note, not a portfolio hole. Quote any near-miss and say why it does or does not count as coverage.
- **Cycle ≠ deadlock (AL-11):** re-read every edge for hard blocking vs. soft preference ("ideally after," "would benefit from"), and check whether the edges reference different milestones of the same deliverables (A needs B's beta; B needs A's feedback on that beta before GA) — staged milestones can interleave into a valid execution order. A soft edge or a valid interleaving downgrades or kills the cycle.
- **Missing label ≠ mismatch (AL-12):** teams use different labeling vocabularies, and a team that labels nothing has not implicitly marked everything aspirational — find the team's labeling scheme (or its absence) before reading a missing label as a commitment level. Also check whether the consumer's arithmetic already discounts the producer ("assumes 50% of Bluefin's stretch lands") or explicitly hedges the dependence — quoted hedging kills or downgrades the finding.
When a disconfirming check kills a candidate, do not report it; when it merely weakens one, report at reduced severity and say which check weakened it.

---

## Part 3 — Evidence discipline (non-negotiable)

1. **Two-sided quoting.** Every alignment finding involves at least two parties. Quote each party's verbatim text — exact words, no paraphrase inside quotation marks — each with its source ref (see `references/report-format.md`). A finding quoting only one side is incomplete and must not be reported.
2. **Absence claims name their search.** AL-01, AL-03, AL-07, AL-10 assert that something is *missing*. State exactly what was searched (which pages, which JQL/CQL, which terms) and quote the closest near-miss found. "Not found" without a described search is a hallucination risk, not evidence.
3. **Label inference.** Causal mechanisms (AL-02), inferred parent links (AL-04/AL-05), and any unquotable edge (AL-11) must be tagged as analyst inference in the finding. Verdict discipline: **CONFIRMED** only when every load-bearing quote was re-fetched and matched character-for-character against its source in a verification pass; otherwise **PLAUSIBLE**.
4. **Quote-verification pass.** Before final reporting, re-open each cited source and confirm each quote exists verbatim and its surrounding context does not reverse the reading (watch for negations, "we considered but rejected," strikethroughs, outdated page versions — record the page version/last-modified date). Findings that fail verification are dropped or downgraded, never silently patched.
5. **One finding, one failure mode.** If a situation matches multiple categories (a terminology collision masking a metric conflict), report the root-cause category and cross-reference the secondary ID rather than double-counting.
6. **Report format.** Emit each finding as an alignment-finding block per `references/report-format.md` §4, populating the fields §4 defines: severity, the AL-XX taxonomy ID with its canonical failure-mode name, the teams involved, both sides' verbatim quotes with source refs, the detection check that fired, the disconfirming checks run and their results, inference labels on any inferred link, the CONFIRMED/PLAUSIBLE verdict, and the recommended resolution owner (which named team drives the conversation, about what, before when).
