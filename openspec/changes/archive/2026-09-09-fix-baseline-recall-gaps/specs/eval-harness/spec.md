## ADDED Requirements

### Requirement: Secondary IDs credit key rows

The grader SHALL parse a goodness finding block's `Also:` line for AP-IDs and treat them as the finding's secondary IDs; an ID mentioned anywhere else in the block is not a secondary ID. When matching key rows, a finding SHALL satisfy a row whose accepted list contains its primary ID or any of its secondary IDs, provided the row's required evidence anchors are satisfied by the finding's located spans. The grade SHALL record which ID matched, and `id_exact` SHALL be true only when the primary ID is the row's first accepted ID. Each row is claimed at most once, and a finding that claims a row through a secondary ID is neither a duplicate nor an extra.

#### Scenario: Missing baseline folded under an orphan-KR block

- **WHEN** a fixture 1 report files Platform KR PL1.3 once, headed AP-12 Orphan KR, with an `Also:` line naming AP-04 KR Without Baseline and the KR text quoted with its source ref
- **THEN** row G7 is found with the matched ID recorded as AP-04 and `id_exact` false, and the block counts as neither a duplicate nor an extra

#### Scenario: Secondary ID without the row's anchor

- **WHEN** a block's `Also:` line names AP-04 but none of the block's located spans lies on KR PL1.3's line
- **THEN** row G7 stays unmatched, recorded as partial at most

#### Scenario: Prose mention is not a secondary ID

- **WHEN** a block's "Why it's a problem" line mentions "AP-04" in prose and the block has no `Also:` line
- **THEN** no secondary ID is recorded and the mention credits no row

### Requirement: Cross-batch comparison

`compare` SHALL accept a `--baseline-batch <dir>` option naming another batch whose single arm serves as the baseline arm. The comparison SHALL then apply the unchanged regression rule, record both batch identifiers and creation times, refuse arms on different models exactly as a paired comparison does, and mark the result **unpaired** in `comparison.json` and in the printed verdict; a paired batch remains the default and the release-grade check.

#### Scenario: Candidate-only batch compared with an earlier baseline

- **WHEN** a batch holds only a candidate arm and `compare` is given the directory of the 2026-09-08 baseline batch
- **THEN** the comparison uses that batch's baseline arm, marks the result unpaired, and exits 1 only when the regression rule fires
