## Why

`references/report-format.md`'s "Artifact lifecycle" section defines the per-portfolio `artifacts.json` registry as the single source of truth for update-vs-create — adopt / read / verify / act / refresh, a re-create path for a dead URL, and a "never silently fork" rule. It is fully specified, structurally checked, and **has never once executed**: every eval run is publish-exempt by design, so no run under `evals/runs/` has ever published an artifact or written a registry. The only enforcement today is "the section exists", which cannot distinguish a skill that updates in place from one that forks a new artifact every cycle. `.claude/skills/openspec-loop/phases/verify-gate.md` records the gap as deferred future work; this change closes it.

## What Changes

- **Narrow the fixture/eval exemption so an eval can execute the contract at all.** Today the exemption's second arm — "and any eval run" — blocks this eval by construction. The exemption is restated in terms of the **real artifact surface**: runs against the skill's own fixtures stay fully exempt (unchanged), and no eval run may ever publish to or read from the real artifact surface or touch a registry outside its own run directory. What is added: an eval run whose prompt supplies a **publish seam** (a local command standing in for the artifact surface) and a working folder inside its run directory executes the decision procedure unchanged, publishing through that seam. A run against a fixture stays exempt even when a seam is supplied.
- **A scratch, non-fixture eval corpus** at `evals/corpora/tidewell-q3.md` — a fictional two-team portfolio. It sits outside `examples/` and is named by no answer key, so the contract's file-based test classifies it as publishable, exactly as a user's own OKR export is.
- **A publish seam**, `evals/lifecycle/publish_seam.py` (stdlib): `read` (verify a URL), `publish` (create), `update` (update in place), backed by a per-run JSON store with an append-only ledger of every operation and the deliverable key it was for.
- **Five graded scenarios** in `evals/lifecycle/scenarios.json`, the only hand-edited source of truth for this eval: **create** (empty registry), **update** (live entries pre-seeded), **re-create** (dead URL pre-seeded), **adopt** (user-supplied URL over a stale entry), and **fixture-exempt** (the same seam and working folder, but a fixture as the corpus — it must publish nothing). Never-fork, verify-before-act, registry/artifact agreement and append-only local history are asserted across the publishing four.
- **Two harness subcommands** — `lifecycle-plan` and `lifecycle-grade` — grading the run's `artifacts.json`, the seam ledger, the run summary and the working folder together. Python 3 standard library only, deterministic, zero model tokens, non-zero exit on failure. `check` validates the scenario file; `selftest` gains a compliant case and one case per contract violation.
- **A frozen run-prompt template** at `evals/prompts/lifecycle.md`, alongside the existing portfolio and single-team templates.
- **Gate wiring:** verify-gate.md's "Future work (deferred)" note is replaced by a **conditional lifecycle tier** — the gate runs the lifecycle eval when a change touches the publish path (SKILL.md's Step 7, report-format's "Artifact lifecycle" section, the seam, the corpus, or the scenario file) and skips it otherwise. `.claude/commands/okr-eval.md` gains the `lifecycle` tier.
- **Doc maps updated:** CLAUDE.md's file-ownership table and README's repository layout gain the corpus, the seam and the scenario file.

## Capabilities

### New Capabilities

None. The behaviour belongs to two capabilities that already exist.

### Modified Capabilities

- `artifact-lifecycle`: the "Fixture and eval runs never publish" requirement is restated in terms of the real artifact surface, with the publish-seam carve-out for eval runs; a new requirement makes the contract behaviourally enforced (a graded eval covering create, update, re-create, adopt, the fixture-exempt counter-case, never-fork and append-only history) rather than only structurally.
- `eval-harness`: a new lifecycle tier — the scratch corpus, the seam, the scenario file, deterministic grading of registry/ledger/summary, and the conditional verify-gate wiring.

## Non-goals

- **Real publishing to claude.ai.** The seam covers every decision the contract specifies; the real Artifact tool's own semantics (that a redeploy keeps the URL, that a favicon persists) remain the tool's contract, not this eval's.
- **Scorecard / `compare` integration.** Lifecycle grades stand alone; they do not join `scorecard.json`, the regression rule, or decision batches.
- **Grading review quality on the scratch corpus.** The corpus plants no AP-XX/AL-XX defects and no answer key claims it; only lifecycle behaviour is graded.
- **Any change to the two fixtures, their keys, the rubric, or the taxonomy.** This change touches no detection behaviour, so it plants no new defects and changes no fixture's answer key — the smoke tier's expected results are unchanged.
- **Cross-cycle drift tracking.** The append-only history assertion checks only that a prior cycle's file survives untouched; comparing cycles remains unbuilt.

## Impact

- **Contract:** `references/report-format.md` (the exemption paragraph only, which the change splits into "Fixture exemption" and "Eval runs and the publish seam") and `SKILL.md` Step 7, which must carry the same scope while still pointing at report-format rather than restating the contract.
- **Harness:** `evals/grader/harness.py` (new subcommands, `check` extension), its selftest corpus, and new files under `evals/corpora/`, `evals/lifecycle/`, `evals/prompts/`.
- **Workflow:** `.claude/skills/openspec-loop/phases/verify-gate.md`, `.claude/commands/okr-eval.md`, `CLAUDE.md`, `README.md`. `.gitignore` is unchanged: a run's working folder and seam store are graded evidence and are committed; only the skill snapshot is regenerable, and it is already ignored.
- **Not affected:** the rubric, the taxonomy, both fixtures, both answer keys, and every existing batch under `evals/runs/`.
