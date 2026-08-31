## 1. Taxonomy edits (references/alignment-taxonomy.md)

- [x] 1.1 Extend AL-07's detection heuristic with the aggregation/precedence rule: ≥2 claimants on one resource owner whose pages state a capacity constraint → one aggregated AL-07 finding that takes precedence over per-edge AL-01 for those edges (AL-01 cross-referenced as secondary per Part 3 §5). Verify: the rule text appears in the AL-07 entry and names both the ≥2-claimants trigger and the stated-capacity trigger.
- [x] 1.2 Add the matching in-file example to AL-07: scenario narrative (Meridian teams, e.g. Bluefin + Ember claiming Atlas capacity Atlas declares committed) showing per-edge AL-01 classification missing the contention, plus the heuristic reading that catches it. Verify: example present in AL-07, fictional-only content.
- [x] 1.3 Add a one-sentence redirect in AL-01's detection heuristic pointing multi-claimant/stated-capacity cases to "AL-07 Resource contention" by canonical name, without duplicating AL-07's definition. Verify: AL-01 entry contains the redirect and no severity/template/definition duplication.
- [x] 1.4 Sanity-check no editing-rule violations: no IDs renamed/renumbered, severity names only Critical/Major/Minor pointing to report-format.md, no template content added. Verify: grep for new severity definitions or ID changes returns nothing unexpected.

## 2. Fixture eval (alignment category)

- [x] 2.1 Re-run the alignment-category fixture eval against `examples/sample-portfolio.md`: a fresh-context evaluator using the updated taxonomy classifies the A-row defects. Verify: A5 reported as AL-07 aggregating Payments + Data against Platform's "fully committed" statement; no standalone AL-01 for those edges; previously-caught alignment defects still found; nothing from the intentional non-defects list reported and the answer key's finding budget not exceeded.
