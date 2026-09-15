# eval-harness (delta)

## MODIFIED Requirements

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
