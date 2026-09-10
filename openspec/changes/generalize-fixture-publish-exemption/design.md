## Context

See `proposal.md` — Why. The relevant constraint is structural: three files state the exemption, and `CLAUDE.md`'s one-owner rule says a topic has exactly one owning file. `references/report-format.md` owns the Artifact lifecycle contract; `SKILL.md` Step 7 points at it; the spec states the requirement the gate checks. All three currently name `examples/sample-portfolio.md`, so the same sentence drifted in three places at once when fixture 2 landed.

This is the second instance of one root cause in this branch. The first — the verify gate's fixture scope restated in four places across three planning- and archive-side files (`openspec/config.yaml` twice, the loop skill's `SKILL.md`, and `phases/refine.md`) — was fixed by making those statements point at the gate instead of paraphrasing it. The same reasoning applies here, with one difference: the exemption cannot be reduced to a pointer in all three places, because the spec must state a checkable requirement. So the fix is to make the *scope* immune to new fixtures rather than to remove the restatement.

## Goals / Non-Goals

**Goals:**

- Express the exemption so that adding a fixture cannot narrow it.
- Keep the three statements textually consistent, so a future reader cannot find two different scopes and have to guess which governs.
- Leave every already-exempt run behaving exactly as before.

**Non-Goals:**

- Any change to what a publishing run does (registry schema, decision procedure, recovery paths) — see `proposal.md` — Non-goals.
- Collapsing the three statements into one. The spec states the requirement, report-format owns the contract text, and SKILL.md points at it; that division is `CLAUDE.md`'s rule and stays.

## Decisions

**Scope by what the corpus is, not by filename or path.** "Any of this skill's own fixtures" rather than "`examples/sample-portfolio.md` or `examples/sample-portfolio-2.md`."

*Alternative considered — enumerate both fixtures.* Rejected: it is the current bug with one more name in it. Fixture 3 strands it again, and the failure is silent — a run publishes instead of erroring, so nothing surfaces the omission.

*Alternative considered — rely on the trailing "or any eval" and change nothing.* Rejected: it makes hermeticity depend on how the run was phrased. The harness prompts do say "never publish," so `/okr-eval` is safe either way — but a hand-typed run against a fixture says no such thing, and the guarantee would hold for the automated path and not the ad-hoc one.

**The test is file identity, not a resolvable path.** A bare `examples/` is a relative path that equally matches an `examples/` folder inside a user's working directory — and `README.md` invites users to point the skill at local exports, so that collision is reachable, where the old single-filename text could not collide this way.

*Alternative considered — anchor the path to "this skill's `examples/` directory".* Written, then rejected on review. `README.md` documents four install modes, and in three of them (copy, project-level, plugin) the installed skill's `examples/` and a working checkout's `examples/` are different directories — so the anchored wording made this change fail at its own motivating case, classifying a hand-typed run against a checkout fixture as the user's own corpus and publishing it. Worse, an agent cannot resolve which `examples/` is "this skill's" from anything `SKILL.md` or `references/report-format.md` tell it: the prompt's path resolves against the working directory, the skill's own path against wherever it was installed, and no loaded text compares them.

The exemption therefore turns on the corpus being one of the skill's shipped fixture files — exempt wherever that copy is read from — and never on the path it occupies. That is decidable from what the agent already has in front of it, and it puts the user's own exports outside the exemption no matter what they name the folder.

**Keep "or any eval run" alongside the fixture scope.** The two cover different things: a fixture run outside the harness, and a harness run whose corpus is a scratch portfolio rather than a file under `examples/`. Dropping either leaves a hole.

**One scope phrase in all three files.** A future grep for the exemption returns three statements that agree on scope. The spec states the user's-own-exports boundary normatively; `references/report-format.md` phrases the same boundary for the running skill, since it owns the contract text; `SKILL.md` carries the scope phrase and points at that section. Divergent phrasings are how the original defect stayed invisible, and a first draft of this change reproduced it — the elaborating sentence went into `report-format.md` only and widened the trigger from a fixture to the directory, which the non-author verify caught.

## Risks / Trade-offs

**"One of this skill's own fixtures" is judged by the agent rather than computed** → Accepted deliberately. The shipped fixtures are few, named in `CLAUDE.md`'s file map, and carry their own answer-key sections, so the judgement is easy in every case that arises; the alternative — a path comparison — was tried and is strictly worse, because it is undecidable from the loaded text and misclassifies the common developer case (see Decisions).

The residual failure is a demonstration run against a file someone parked in the skill's `examples/` declining to publish → fail-safe and recoverable by asking for a publish, where the inverse — a fixture run writing to a real registry — is not.

**Two earlier drafts of this change were caught by the non-author verify** → recorded here so the reasoning is not re-derived: draft 1 put an elaborating sentence in `references/report-format.md` only, which widened its trigger from a fixture to the directory and left the three statements disagreeing; draft 2 anchored the path, which broke the motivating case as described above. Both failures came from describing the exemption by *where* the file sits.

## Migration Plan

None. No state, no registry format change, no rollback path needed — the change only widens a prohibition, so any run that was exempt before remains exempt and no existing `artifacts.json` is read or written differently.
