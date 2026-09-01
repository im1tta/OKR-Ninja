# Design — strengthen-al02-mechanism-pair-generation

## Context

See `proposal.md` — Why. Current state: AL-02's Detection heuristic already *names* mechanism pairs (clause 2: "known tension pairs where one KR's stated mechanism is a documented driver of the other's metric"), but the only generation machinery the procedure gives runs on metric identity — Part 2 Step 3 lists AL-02's blocking key as "same canonical metric (AL-02/AL-09)". Clause (2) is therefore a classifier with no candidate stream: both failed eval runs built the metric catalog, blocked on metric identity, found no shared metric between Payments P2.2 and Growth G2.1, and never compared them. Constraints: `references/alignment-taxonomy.md` is the only file allowed to hold AL-XX detection heuristics (CLAUDE.md ownership table); AL-XX IDs and canonical names are frozen; severity names point to `references/report-format.md`; Part 3 evidence discipline must not change; SKILL.md must not change (its Step 4 defers to "the taxonomy's blocking keys" generically, which is exactly why fixing the taxonomy suffices).

## Goals / Non-Goals

**Goals:**
- Clause (2) becomes a real generation step: a named blocking key that mechanically produces mechanism-pair candidates, so a run's method notes can report it among the "blocking keys used" (Step 3 already requires reporting them).
- The generation/disconfirmation boundary is explicit, with per-candidate kills — a correctly killed lookalike pair cannot take a surface's mechanism pairs down with it.
- A worked in-file example encodes both behaviors in the Meridian universe.

**Non-Goals:**
- No re-tuning of AL-02 severity mapping or evidence requirements; no changes to other failure modes' keys; no fixture edits (see proposal Non-goals).

## Decisions

- **D1 — Fix at the taxonomy layer only.** The observed failure is fully explained by the taxonomy's own Step 3 text; SKILL.md already defers to the taxonomy's blocking keys. Alternative (adding a SKILL.md procedure step) rejected: duplicates taxonomy content into a file barred from holding it, and SKILL.md sits near its ~150-line cap.
- **D2 — A named key ("surface-lever key"), not softer prose.** Generation guidance must be mechanical and auditable. Naming both keys (metric-identity key, surface-lever key) lets Step 3 reference them, lets method notes report which keys ran, and gives the verify gate something checkable. Alternative ("also consider mechanism conflicts" advisory sentence) rejected: that is what clause (2) already was, and two independent runs ignored it.
- **D3 — Key definition = same surface + stated lever of the friction/quality/risk/cost family.** The blocking condition is deliberately narrower than "any two KRs on one surface" (which would explode the candidate set): one side must *state a lever* that is a control on the surface (verification steps, review gates, rate limits, stricter thresholds, price changes), the other must target that surface's throughput/conversion/volume/latency metric. The classic tension-pair list (speed vs. quality, acquisition vs. unit economics, velocity vs. reliability, discounts vs. margin) stays as recognized shapes of the same key, not a third key.
- **D4 — Generation requires a stated lever, not a documented mechanism.** The lever must appear in the KR's own text (P2.2 states "step-up verification coverage"); whether the causal path to the other metric is documented in the corpus governs labeling (analyst inference) and severity under the *unchanged* Evidence required rules. Requiring in-corpus documentation at generation time would re-suppress exactly the A1 class, since fixture 1 documents no friction–conversion tradeoff.
- **D5 — Per-candidate kills stated at both sites.** The rule ("disconfirmation kills candidates one at a time, never a surface") lands in the AL-02 entry and in Step 4's "Shared metric ≠ conflict" bullet, because the failed runs' wholesale-dismissal behavior is a disconfirmation-stage error and Step 4 is where disconfirmation is specified. Wording kept short at both sites to avoid duplication drift.
- **D6 — Example embeds the near-miss trap.** The new AL-02 example mirrors the fixture's structure without copying it (Meridian teams, different numbers/metrics): a challenge-coverage lever vs. a checkout-completion target (invisible to metric-identity blocking) *plus* a lookalike-metric pair correctly killed — so the example teaches generation and non-suppression together. Fixture 1 stays untouched: A1 is already planted and keyed, which also satisfies the config's "fixture update when detection behavior changes" tasks rule vacuously (the covering defect and answer-key row already exist; adding a second planted AL-02 would change defect counts and budgets for no coverage gain).

## Risks / Trade-offs

- [Surface-lever key over-generates candidates, pressuring the fixture's 2-extra-findings budget] → The key requires a *stated* control-type lever plus a same-surface metric target, and every candidate still passes the existing disconfirming checks (shared parent OKR, documented lever split, opposing-direction test). Non-defect #4 remains killed because it has no control lever on either side — both KRs push the same surface in the same direction.
- [Longer heuristic text gets skimmed by runs] → Keys are bolded, numbered, and one sentence each; the example carries the operational detail.
- [Fresh-agent eval is stochastic; one green run may not prove the fix] → Verify gate honesty rule applies: report the run(s) as evidence, not proof; the fixture-1 eval in this change's verify step must show A1 caught, non-defect #4 absent, 13 others still found, within budget.

## Migration Plan

Docs-only change to one reference file; no consumers to migrate. Rollback = revert the commit. Archive syncs the delta into `openspec/specs/alignment-detection/spec.md`.
