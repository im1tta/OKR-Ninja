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

Every run record SHALL include the skill snapshot's git SHA and a dirty flag, the model ID the run executed on, the prompt-template hash, the key hash, the slice ID, the arm label, the start time, the wall time, and the token usage when the runner reports it (null otherwise). The model ID SHALL be the one the run's transcript records for its assistant turns; a model ID supplied by the orchestrator that disagrees with the transcript SHALL be rejected rather than recorded. A run whose report was not produced SHALL record a named not-produced reason, and the grade SHALL carry that reason.

#### Scenario: Provenance present in every grade

- **WHEN** any run is graded
- **THEN** its grade carries every provenance field, with null for unreported token usage rather than an omitted key

#### Scenario: Orchestrator model disagrees with the transcript

- **WHEN** capture is given a model ID and the transcript's assistant turns record a different one, or record none
- **THEN** capture fails loudly, writes no report, and the run record names the reason as a model mismatch

### Requirement: Batch tiers and execution

The harness SHALL provide two batch tiers executed through subagents inside a Claude Code session, with each run following `SKILL.md`'s execution model unchanged. A run SHALL return its complete report as the runner's final message, between two exact marker lines that each appear once, and SHALL write nothing outside its run directory (scratch files inside it are allowed). The harness SHALL capture the report byte-exact from the runner's transcript — the last assistant message carrying text, where a message is the API message (its transcript lines grouped by message id) and its text items are concatenated with nothing inserted — and write it as the run's report itself; a marker line matches exactly, with a trailing carriage return as the only tolerated variation; the captured report is the text strictly between the marker lines, kept as emitted, with a final newline added only when it lacks one, and a block with no report text yields no report; the runner never writes the report file, and text from a completion notification is never used as the report because notifications escape it. A batch executes on one model, chosen per batch (the session's model or an override), and the model is recorded per run from the transcript. When capture cannot yield a report — the agent errored, the transcript is unreadable or malformed, the final message carries no text, the markers are missing, more than one marker block exists, the block is empty, or the model cross-check fails — the run SHALL have no report and SHALL record the corresponding named reason without crashing; an orchestrator-reported agent error takes precedence over every transcript-level reason. Capture SHALL remove any earlier report and grade from the run directory whenever it runs, so a resumed batch never grades a stale file; the harness never retries a run inside a batch. **Smoke**: one run per slice in scope; passes only when every run passes its key criterion. **Decision**: five runs per slice per arm, with a baseline arm (a snapshot of the skill at a named git commit) and a candidate arm executed in the same batch; a baseline batch MAY carry a single arm. A batch SHALL be resumable: runs whose report already exists are not re-executed.

#### Scenario: Smoke tier with a failing run

- **WHEN** one of three smoke runs exceeds its budget
- **THEN** the batch result is fail and names the run and its counted findings

#### Scenario: Interrupted decision batch

- **WHEN** a decision batch is restarted after seven of thirty runs completed
- **THEN** only the remaining twenty-three runs execute and the scorecard covers all thirty

#### Scenario: A runner whose Write is refused still produces a graded run

- **WHEN** a runner's attempt to write a report file is refused by the environment and it returns the complete report between the marker lines as its final message
- **THEN** capture writes that report byte-exact to the run directory, the run is graded normally, and the grade does not count the refusal against the runner

#### Scenario: Report text is preserved character for character

- **WHEN** the returned report contains `<`, `&`, em-dashes, `$` or any other character the transport could escape
- **THEN** the captured report is byte-identical to the text of the runner's final message between the markers

#### Scenario: Notification text is never used as the report

- **WHEN** the orchestrator receives a completion notification whose result text is an escaped rendering of the runner's reply
- **THEN** the report is captured from the transcript file only; nothing from the notification is written as the report

#### Scenario: Chatter outside the markers is ignored

- **WHEN** the final message carries a preamble before the begin marker or commentary after the end marker
- **THEN** only the text between the markers becomes the report

#### Scenario: Final message split across transcript lines

- **WHEN** the final assistant message's text arrives as two transcript lines sharing one message id, the begin marker in the first and the end marker in the second
- **THEN** the two text items are concatenated and the report between the markers is captured byte-exact

#### Scenario: Transcript cannot be read

- **WHEN** the transcript path is a directory or a file the harness may not read, and a stale report exists in the run directory
- **THEN** capture records the reason as transcript-unreadable, writes no report, removes the stale report, and does not crash

#### Scenario: Malformed transcript line

- **WHEN** a transcript line is valid JSON but a relied-on field has an unexpected shape, and a stale report exists in the run directory
- **THEN** capture records the reason as transcript-unreadable in the run record, writes no report, and leaves no stale report or grade behind

#### Scenario: Final message without markers

- **WHEN** the final message carries text but no marker block, two marker blocks, or a block with nothing in it
- **THEN** no report is written and the run records the reason (markers missing, multiple blocks, or empty report) so the scorecard can distinguish it from a runner that did not finish

### Requirement: Verify gate uses the smoke tier

The OPSX verify gate's fixture eval SHALL invoke the smoke tier for the slices whose keys cover the category the change touched, and the gate's fixture-eval result SHALL be the harness's pass/fail rather than an ungraded subagent judgement. Decision batches are not part of the gate.

#### Scenario: Skill-content change reaches the gate

- **WHEN** a change edits `references/alignment-taxonomy.md` and the verify gate runs
- **THEN** the gate runs the smoke tier on the fixture slices covering the touched modes and reports the grader's verdict

### Requirement: Scorecard per batch

For every arm and slice in a batch the scorecard SHALL report: per-row hit count and ID-exact count out of runs; a frequency table of extras and duplicates keyed by ID and anchor, with kind, known-red status and bucket; non-defect violation and off-key counts; quote-class totals; structural pass count; runs passing the key criterion; mean and maximum tokens and wall time; and, for runs without a report, a count per not-produced reason, so a capture or transport failure is distinguishable from a runner that returned no report. It SHALL carry the batch provenance and, for rows the key flags as overlapping reference worked examples, a leakage caveat.

#### Scenario: Recurring extra is visible

- **WHEN** four of five runs of a slice report AP-12 Orphan KR anchored on Accounts KR AC3.2
- **THEN** the scorecard lists that ID-and-anchor key with a count of four, its kind, and whether a triage entry covers it

#### Scenario: Flaky defect is visible

- **WHEN** row G7 is found in five of five runs but ID-exact in one
- **THEN** the scorecard shows both counts for G7

#### Scenario: Not-produced reasons are visible

- **WHEN** one run of a slice has no report because its markers were missing and another because the agent errored
- **THEN** the scorecard shows the slice with two runs not produced, one per reason, and the printed table names both reasons

### Requirement: Regression rule between arms

Given a baseline arm and a candidate arm of equal run count in one batch, the comparator SHALL declare a regression when any of the following holds, and SHALL list each triggered rule with the rows or keys involved: a row's hit count drops by two or more; an extras, duplicates or violation key appears in three or more candidate runs and fewer than three baseline runs; any fabricated evidence span exists in the candidate arm. The comparator SHALL refuse to compare arms whose model IDs differ. When the compared arms ran on different prompt-template hashes, the comparator SHALL print a warning and record it in the comparison rather than refuse, because the prompt template is transport, not skill content.

#### Scenario: One-hit drop is not a regression

- **WHEN** a row is found in five baseline runs and four candidate runs
- **THEN** no regression is declared for that row

#### Scenario: New stable extra

- **WHEN** an extra key appears in four candidate runs and one baseline run
- **THEN** a regression is declared naming that key

#### Scenario: Arms on different models

- **WHEN** the baseline arm's runs record a different model ID than the candidate arm's
- **THEN** the comparator exits with an error instead of a comparison

#### Scenario: Arms on different prompt templates

- **WHEN** the baseline arm's batch and the candidate arm's batch record different prompt-template hashes for a mode
- **THEN** the comparison proceeds, prints a warning naming the mode, and records the warning in the comparison file

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

### Requirement: Lifecycle eval corpus sits outside the fixture set

The lifecycle eval SHALL run against a scratch portfolio corpus that is not one of the skill's own fixtures: it SHALL live outside the `examples/` directory, SHALL be named by no answer key under `evals/keys/`, and SHALL plant no catalog defect that any key claims. The corpus SHALL be fictional — invented company and team names, no real people — and SHALL be reviewable in portfolio mode. The harness SHALL fail its `check` command when the corpus is missing or when a fixture path is used as the lifecycle corpus.

#### Scenario: Corpus classifies as publishable

- **WHEN** the skill is run against the lifecycle corpus with a seam supplied
- **THEN** the run is outside the fixture exemption and publishes through the seam, because the corpus is not one of the skill's own fixture files

#### Scenario: Fixture path rejected as corpus

- **WHEN** the scenario file names a file under `examples/` as the lifecycle corpus
- **THEN** `check` reports the scenario file invalid and exits non-zero

### Requirement: Publish seam records every publish decision

The harness SHALL provide a publish seam that stands in for the artifact surface and exposes exactly three operations: **verify** a URL (reporting reachable or dead), **create** a new artifact for a named deliverable key (returning a fresh URL), and **update** an existing artifact at a given URL in place (returning the same URL). The seam SHALL keep its state per run inside that run's directory, SHALL record every operation in an append-only ledger carrying the operation, the URL and the order in which it occurred — a create or an update additionally carrying the deliverable key, the title and the favicon, and a verify its result — and SHALL fail an update against a URL it does not hold. The seam SHALL NOT reach the network and SHALL NOT expose a listing operation, so that no run can substitute artifact listing for a registry lookup.

#### Scenario: Create and update are distinguishable after the fact

- **WHEN** a run creates one artifact and later updates it
- **THEN** the ledger holds a create followed by an update, both naming the same deliverable key, and the store holds exactly one artifact

#### Scenario: Update against a dead URL fails

- **WHEN** a run calls update with a URL the seam does not hold
- **THEN** the seam exits non-zero without recording an update, so the run must take the re-create path

### Requirement: Lifecycle scenarios are declared once and graded deterministically

The lifecycle scenarios SHALL be declared in a single machine-readable file that is the only hand-edited source of truth for the eval: for each scenario, the seeded registry state, the seeded seam state, any seeded prior-cycle output, the deliverable keys in scope, the cycle date, the user-supplied URL when the scenario has one, and the assertions to grade. The harness SHALL grade a lifecycle run from that scenario's declaration and from run-directory contents alone — the written `artifacts.json`, the seam ledger and store, the run summary, and the working folder's files — using only the Python 3 standard library, spending no model tokens, and producing the same grade for the same run directory on every invocation. Grading SHALL be joint: a run passes only when the registry, the ledger, the summary and the working folder are all consistent with the scenario's assertions. The grade command SHALL exit non-zero when any graded run fails.

#### Scenario: Registry and ledger must agree

- **WHEN** a run's registry shows an unchanged URL but the ledger shows a create for that key
- **THEN** the run fails, naming the fork, rather than passing on the registry alone

#### Scenario: Same run directory grades identically

- **WHEN** the same lifecycle run directory is graded twice
- **THEN** the two grades are identical except for the grading timestamp

### Requirement: The lifecycle scenarios cover the contract's decision paths

The eval SHALL cover, one scenario per path: **create** — an empty registry yields one artifact per deliverable key, each registered with its URL, title, favicon, last-published timestamp and cycle date; **update** — a registry whose entries the seam reports reachable yields an update in place per key, with URL, title and favicon unchanged and timestamp and cycle date advanced; **re-create** — a registry naming a dead URL yields exactly one replacement artifact for that key, the entry overwritten with the new URL, and a run summary stating the re-create and its reason; **adopt** — a user-supplied URL is recorded under its deliverable key, overwriting any prior entry, and that artifact is updated rather than a new one created. A fifth scenario, **fixture-exempt**, SHALL supply the same seam and working folder but name one of the skill's own fixtures as its corpus, and SHALL assert that the run publishes nothing, writes no registry file anywhere in its run directory, and says in its run summary that the publish step was skipped — so the hermetic guarantee for fixture runs is executed rather than only asserted. Its prompt SHALL NOT state whether the run is exempt, because that is the decision under test.

Every publishing scenario SHALL additionally assert: that no artifact was created for a key that already had a registry entry, except the single re-create, which SHALL be reported in the run summary **and name the deliverable it re-created**; that the registered URL was verified through the seam **before** the run acted on that key; that the registry entry describes the artifact it points at, so a run that renames the living artifact or registers a URL the seam does not hold is caught; and that any prior cycle's local output in the working folder is left byte-identical.

#### Scenario: A second create for a registered key fails the run

- **WHEN** a run creates a new artifact for a deliverable key whose registry entry the seam reported reachable
- **THEN** the run fails the never-fork assertion, naming the key and the offending ledger entry

#### Scenario: An unreported re-create fails the run

- **WHEN** a run takes the re-create path correctly but its run summary states no re-create or gives no reason
- **THEN** the run fails, naming the missing statement

#### Scenario: Overwritten prior cycle output fails the run

- **WHEN** a run rewrites the prior cycle's dated output file in the working folder
- **THEN** the run fails the append-only history assertion, naming the modified file

#### Scenario: A renamed living artifact fails the run

- **WHEN** a run updates the registered URL in place but renames that artifact through the seam, leaving the registry entry's title as registered
- **THEN** the run fails, naming the title the registry claims and the title the artifact now carries

#### Scenario: An unverified update fails the run

- **WHEN** a run updates a registered URL without verifying it through the seam first
- **THEN** the run fails, naming the key and the URL it acted on unverified

#### Scenario: A fixture corpus with a seam supplied publishes nothing

- **WHEN** the fixture-exempt scenario runs and the report is produced
- **THEN** the seam ledger holds no create and no update, no `artifacts.json` exists anywhere in the run directory, and the run summary says the publish step was skipped

#### Scenario: A fixture run that publishes fails

- **WHEN** a run against the fixture-exempt scenario publishes through the seam or writes a registry
- **THEN** the run fails, naming the publish and the registry file, because the fixture arm of the exemption is unconditional

### Requirement: Verify gate uses the lifecycle tier for publish-path changes

The OPSX verify gate SHALL run the lifecycle eval when a change touches the publish path — `SKILL.md`'s publish step, `references/report-format.md`'s "Artifact lifecycle" section, the seam, the lifecycle corpus, or the scenario file — and SHALL skip it otherwise. The gate's lifecycle result SHALL be the harness's pass/fail rather than an ungraded subagent judgement, and the gate SHALL NOT be green when any lifecycle scenario fails.

#### Scenario: Contract edit reaches the gate

- **WHEN** a change edits the "Artifact lifecycle" section of `references/report-format.md` and the verify gate runs
- **THEN** the gate runs the lifecycle eval and reports the grader's verdict

#### Scenario: Rubric-only change skips the tier

- **WHEN** a change edits only a scoring anchor in `references/goodness-rubric.md`
- **THEN** the gate skips the lifecycle tier and says so, because no publish-path file was touched
