# eval-harness Specification

## Purpose
Defines the deterministic evaluation harness that grades OKR-Ninja runs against machine-readable answer keys without spending model tokens, orchestrates run batches through subagents on the subscription, produces a per-batch scorecard, and compares two skill versions with a fixed regression rule.

## Requirements

### Requirement: Deterministic, token-free grading

The harness SHALL grade a run's report against its fixture key using only deterministic scripts — no model calls — and SHALL emit a per-run grade containing: the status of every key row (found, missed, partial), the matched ID for found rows, extras, duplicates, non-defect violations, off-key findings, quote-class counts with every fabricated span listed, structural check results, run provenance, and a pass/fail verdict against the key's criterion.

#### Scenario: Grading is reproducible

- **WHEN** the same report, sliced input, and key are graded twice
- **THEN** the two grades are identical except for the grading timestamp

#### Scenario: Grader self-tests guard the grader

- **WHEN** the harness's self-test command runs
- **THEN** it grades the bundled mini reports and corrupted keys, and every expected outcome (found, missed, partial, duplicate, near-miss, fabricated, out-of-scope, budget pass/fail) matches, otherwise the command exits non-zero

### Requirement: Findings are recognised only through the mandated report format

The grader SHALL recognise a finding only by the heading forms defined in `references/report-format.md` — a severity in brackets, an AP-XX or AL-XX ID, and the canonical name. Inside a finding's block, a quoted span followed by a source ref on the same line is an **evidence span** when the line is an evidence line (its label contains "evidence" or names a team or section, as the template's `Evidence:` and `<Side> evidence:` lines do) and a **supporting span** on any other labelled line (why, conflict, detection check, disconfirming checks, rewrite). Both are verified against the input and, when located, satisfy anchors; only evidence spans can be fabricated — a supporting span that cannot be located is reported as unverified and never fails the run. A quoted span without a source ref is a mention: it is neither verified nor able to satisfy an anchor.

#### Scenario: Report with no conforming headings

- **WHEN** a report contains no heading in the mandated form
- **THEN** the grade records zero findings parsed, marks every planted row missed, and raises a structural failure naming the cause, rather than passing silently

#### Scenario: Quote without a source ref

- **WHEN** a finding's "Why it's a problem" line quotes a phrase with no source ref
- **THEN** the span is recorded as a mention, is not checked against the input, and does not satisfy any evidence anchor

#### Scenario: Search term quoted on a disconfirming-checks line

- **WHEN** a finding's "Disconfirming checks run" line quotes the search terms it looked for, with a source ref to the page searched, and those terms appear nowhere in the input
- **THEN** each term is recorded as an unverified supporting span in the grade's warnings, and the run is not failed for them

### Requirement: Row matching by accepted ID and evidence anchors

A finding SHALL match a key row only when its ID is in the row's accepted list AND every required evidence anchor of the row is satisfied by an evidence span located on the input line carrying that anchor's marker (item anchors) or inside the named section (section anchors). Optional anchors never block a match. A row SHALL be counted found at most once per run, and the grade SHALL record whether the matched ID is the row's primary (first-listed) ID.

#### Scenario: Cross-source defect quoted from one side only

- **WHEN** a finding cites AP-06 Sandbagged Target with an evidence span on the Platform uptime KR line but no evidence span inside the appendix section
- **THEN** row G5 stays unmatched, the finding is recorded as a partial match naming the unsatisfied anchor, and it counts as an extra

#### Scenario: Same ID at two locations

- **WHEN** a report carries AP-04 findings anchored on Growth KR G1.1 and on Platform KR PL1.3
- **THEN** each matches its own row and neither is an extra

#### Scenario: Accepted alternate ID

- **WHEN** a row accepts AP-01 first and AP-14 second, and the finding cites AP-14 on the row's anchor
- **THEN** the row is found, the grade records the matched ID as AP-14, and the row is not ID-exact

### Requirement: Duplicate findings on a matched anchor

When a second finding's evidence anchors coincide with a row already matched in the same run, the grader SHALL record it as a duplicate of that row, count it against the budget, and list it separately from extras.

#### Scenario: One KR reported under three IDs

- **WHEN** a single-team report carries AP-04, AP-09 and AP-12 findings all anchored on Platform KR PL1.3
- **THEN** one matches row G7, the other two are duplicates of G7, and both duplicates count against the budget

### Requirement: Quote classification after normalisation

Every evidence and supporting span SHALL be classified after normalising Unicode quotation marks and dashes to ASCII, collapsing whitespace, and stripping the span's own surrounding quotation marks and markdown emphasis, as exactly one of: **verbatim** (substring of the run's sliced input), **near-miss** (equal to a substring except for a trailing period, an ellipsis, or emphasis markers), **out-of-scope** (substring of the original fixture but not of the sliced input), or **fabricated** (none of the above); a supporting span that would be fabricated is classified **unverified** instead, and a span of fewer than three words that cannot be located is a **term** (a label or search word, not a quote of source text) and is never fabricated. A span that occurs on several input lines is located by the line its source ref names; when the ref names none of them the span stays unlocated, satisfies no anchor, and is reported as ambiguous. Any fabricated evidence span SHALL fail the run.

#### Scenario: Curly quotes and a trailing period

- **WHEN** an evidence span reproduces an input line with curly quotation marks and an added trailing period
- **THEN** it is classified near-miss, counted, and the run is not failed for it

#### Scenario: Paraphrase presented as a quote

- **WHEN** an evidence span restates a KR in different words
- **THEN** it is classified fabricated and the run fails regardless of every other result

#### Scenario: Absent label word quoted as a term

- **WHEN** an AP-08 finding's evidence line quotes the single word "aspirational" as a label the page never uses
- **THEN** the span is classified term, the run is not failed for it, and it satisfies no anchor

#### Scenario: Repeated line located by its ref

- **WHEN** a finding quotes a commitment-convention line that appears under four teams, with a source ref naming the Accounts page's line
- **THEN** the span is located on the Accounts line and anchors the finding there

#### Scenario: Quote from outside the slice

- **WHEN** a Platform single-team report quotes a line that exists in the full fixture but not in the sliced input
- **THEN** the span is classified out-of-scope and the finding counts against the slice's budget

### Requirement: Extras, violations, and the budget count

A finding matching no row SHALL be an extra. An extra that cites a forbidden ID at an intentional non-defect's location SHALL additionally be flagged a non-defect violation; an extra whose ID is in the fixture's not-covered list SHALL be flagged off-key. The budget count SHALL be the number of extras plus duplicates, excluding findings covered by an active known-red triage entry in the key, which are still reported. The run passes the key criterion only when every planted row is found, no evidence span is fabricated, and the budget count does not exceed the key's budget.

#### Scenario: Known-red entry excludes an extra from the count

- **WHEN** the key holds an active known-red entry for AP-10 anchored on Platform Objective PL1 and a run reports exactly that finding
- **THEN** the finding appears in the grade's extras with the entry's bucket, and the budget count does not include it

#### Scenario: Budget exceeded

- **WHEN** a fixture-1 portfolio run has three counted extras against a budget of two
- **THEN** the run fails the key criterion with the three findings listed

### Requirement: Structural conformance per mode

The grade SHALL check the report's structure for its mode. Portfolio: the six sections in order, a heatmap with exactly the eleven dimension columns, every finding with at least one evidence span, and every AL finding with evidence from at least two sides. Single-team: no heatmap, no AL block, no re-run section, an outbound-dependency-notes section, and — when the slice provides no strategy source — O4 shown as N/A with the rubric's gap note and a statement that strategy tracing was out of scope. An AL block in a single-team report SHALL fail the run.

#### Scenario: Single-team report with an alignment block

- **WHEN** a Platform single-team report contains an AL-07 finding block
- **THEN** the run fails with a structural failure naming the block

#### Scenario: Heatmap with a twelfth column

- **WHEN** a portfolio heatmap carries a column beyond O1–O4 and K1–K7
- **THEN** the structural check fails and the failure names the extra column

### Requirement: Run provenance

Every run record SHALL include the skill snapshot's git SHA and a dirty flag, the model ID the run executed on, the prompt-template hash, the key hash, the slice ID, the arm label, the start time, the wall time, and the token usage when the runner reports it (null otherwise).

#### Scenario: Provenance present in every grade

- **WHEN** any run is graded
- **THEN** its grade carries every provenance field, with null for unreported token usage rather than an omitted key

### Requirement: Batch tiers and execution

The harness SHALL provide two batch tiers executed through subagents inside a Claude Code session on that session's model, with each run following `SKILL.md`'s execution model unchanged and writing only inside its run directory. **Smoke**: one run per slice in scope; passes only when every run passes its key criterion. **Decision**: five runs per slice per arm, with a baseline arm (a snapshot of the skill at a named git commit) and a candidate arm executed in the same batch; a baseline batch MAY carry a single arm. A batch SHALL be resumable: runs whose report already exists are not re-executed.

#### Scenario: Smoke tier with a failing run

- **WHEN** one of three smoke runs exceeds its budget
- **THEN** the batch result is fail and names the run and its counted findings

#### Scenario: Interrupted decision batch

- **WHEN** a decision batch is restarted after seven of thirty runs completed
- **THEN** only the remaining twenty-three runs execute and the scorecard covers all thirty

### Requirement: Verify gate uses the smoke tier

The OPSX verify gate's fixture eval SHALL invoke the smoke tier for the slices whose keys cover the category the change touched, and the gate's fixture-eval result SHALL be the harness's pass/fail rather than an ungraded subagent judgement. Decision batches are not part of the gate.

#### Scenario: Skill-content change reaches the gate

- **WHEN** a change edits `references/alignment-taxonomy.md` and the verify gate runs
- **THEN** the gate runs the smoke tier on the fixture slices covering the touched modes and reports the grader's verdict

### Requirement: Scorecard per batch

For every arm and slice in a batch the scorecard SHALL report: per-row hit count and ID-exact count out of runs; a frequency table of extras and duplicates keyed by ID and anchor, with kind, known-red status and bucket; non-defect violation and off-key counts; quote-class totals; structural pass count; runs passing the key criterion; mean and maximum tokens and wall time. It SHALL carry the batch provenance and, for rows the key flags as overlapping reference worked examples, a leakage caveat.

#### Scenario: Recurring extra is visible

- **WHEN** four of five runs of a slice report AP-12 Orphan KR anchored on Accounts KR AC3.2
- **THEN** the scorecard lists that ID-and-anchor key with a count of four, its kind, and whether a triage entry covers it

#### Scenario: Flaky defect is visible

- **WHEN** row G7 is found in five of five runs but ID-exact in one
- **THEN** the scorecard shows both counts for G7

### Requirement: Regression rule between arms

Given a baseline arm and a candidate arm of equal run count in one batch, the comparator SHALL declare a regression when any of the following holds, and SHALL list each triggered rule with the rows or keys involved: a row's hit count drops by two or more; an extras, duplicates or violation key appears in three or more candidate runs and fewer than three baseline runs; any fabricated evidence span exists in the candidate arm. The comparator SHALL refuse to compare arms whose model IDs differ.

#### Scenario: One-hit drop is not a regression

- **WHEN** a row is found in five baseline runs and four candidate runs
- **THEN** no regression is declared for that row

#### Scenario: New stable extra

- **WHEN** an extra key appears in four candidate runs and one baseline run
- **THEN** a regression is declared naming that key

#### Scenario: Arms on different models

- **WHEN** the baseline arm's runs record a different model ID than the candidate arm's
- **THEN** the comparator exits with an error instead of a comparison

### Requirement: Committed batch artefacts

Every batch directory SHALL contain, per run, the prompt as sent, the report as written, and the grade; and per batch, the scorecard and, when two arms exist, the comparison. Regenerable sliced inputs and skill snapshots SHALL NOT be committed.

#### Scenario: Batch directory after a decision batch

- **WHEN** a decision batch completes
- **THEN** the directory holds thirty prompt, report and grade files, one scorecard, one comparison, and no sliced inputs or skill snapshots

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
