## ADDED Requirements

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
