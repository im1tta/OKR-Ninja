# Phase 2 — Refine (the one human gate)

Reduce ambiguity before any change is created. Build a clear, shared picture of the **problem to be solved** and the user's **intent**, then get explicit approval. This is the only mandatory checkpoint in the loop — **do not proceed to `/opsx:propose`, create a change, or write code until the user approves.**

## Open by sharing the frame

Restate, in one or two lines: the idea, the problem it solves, and who it's for. Ask the user to confirm or correct. This anchors the conversation before any questions.

## Ask one question at a time

- **One question per turn.** Use the **AskUserQuestion tool** — it renders the choices as clickable options and always adds a free-text "Other," so the user is never boxed in.
- Each question offers **three options**. The **recommended option goes first and is labeled "(Recommended)"** (your "always A" rule, rendered natively). Briefly say *why* it's recommended in its description.
- **Adapt.** Choose each next question from the previous answers — hunt blindspots, don't read a fixed script. Drop questions that earlier answers already settled.
- Keep it to the **fewest questions that remove real ambiguity.** Stop when remaining ambiguity is low or the user signals "that's enough." Don't interrogate.

## Blindspot sweep (skip any already clear)

- **Problem & intent** — what's actually being solved, and the underlying goal behind the request.
- **Scope** — what's explicitly **in** vs **out**, and what to **defer** (this repo favors thin, minimal scope — push non-essential work to "later").
- **Affected surfaces** — SKILL.md triggering/description, the operating procedure steps, `references/` (goodness rubric, alignment taxonomy, report format), the `examples/` fixture and its answer key.
- **Skill routing** (project-specific, easy to miss) — does the change keep the boundary with the sibling `okr-deepdive` skill crisp (OKR-Ninja = multi-team/portfolio + alignment; okr-deepdive = single-team deep dive)? Surface this whenever the description or scope-intake step is touched.
- **Evidence discipline** — does the change preserve the verbatim-quote-with-source requirement everywhere findings are produced? No paraphrase presented as quote.
- **Success criteria** — how we'll know it worked; which planted defects in `examples/sample-portfolio.md` the change should newly catch (or stop false-positive-ing on).
- **Data sources** — impact on Jira/Confluence MCP extraction vs the local-file fallback; changes to the normalized OKR structure (team, objective, KRs, owners, parent link, dependencies).
- **Edge cases & failure modes** — empty/partial OKR sets, a team with no OKRs, unreachable sources, ambiguous team names, N too large for full pairwise comparison.
- **Dependencies & sequencing** — what must exist first; what this unblocks.
- **Rollout** — does the fixture/answer key need updating in the same change; reversibility.

## Converge — Agreed requirements

When questions are answered, write a crisp summary the proposal will be built from:

```
## Agreed requirements
- Problem / intent:
- In scope:
- Out of scope (deferred):
- Affected surfaces:
- Success criteria:
- Key decisions: <the A/B/C choices made, each with the option chosen>
- Constraints (trust/safety/auth/scope):
- Data model impact:
- Open risks (if any):
```

## Approval gate

Ask explicitly, e.g.: **"Approve this to proceed to `/opsx:propose`, or refine further?"** Proceed **only** on explicit approval. If the user wants changes, keep refining and re-summarize. On approval, hand the Agreed-requirements summary back to the orchestrator as the input for Propose.

## Guardrails

- **Do not proceed with any action or task** until all questions are answered **and** the user explicitly approves (the user's standing rule).
- **No application code** in this phase. Capturing the agreed summary is fine; creating the change is the next phase.
- **Recommend, don't decide** — the first option is your recommendation, but the user chooses. Honor an "Other" answer fully.
- If the user prefers plain-text "Option A / B / C" instead of the tool's clickable options, switch to that format — same rule (recommended first, tagged "(Recommended)").
