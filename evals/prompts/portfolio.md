You are running an evaluation of the OKR-Ninja skill. Load the skill by reading `{{skill_md}}` and follow its procedure exactly, loading each file under `{{references_dir}}` at the step where SKILL.md tells you to. Do not decide whether the skill applies — it applies.

Task: audit the OKR portfolio in `{{input_path}}` for quality and cross-team alignment. Every team in the file is in scope (portfolio mode).

Rules for this run:

- `{{input_path}}` is the only source of OKR content. Do not read any other file for OKR content, do not open anything under `examples/` or `evals/keys/`, and do not search the repository or its history for related material. No Atlassian connection is available.
- There is no user to ask. Treat the teams enumerated in the file as the confirmed scope, the period as the quarter the file states, and the file's company priorities section as the strategy source.
- This is an eval run: never publish artifacts and never create or modify any registry file. The skill's publish step is skipped for eval runs.
- Do not write the report to any file: the harness captures it from your reply. Return the complete report — exactly the portfolio report defined in the skill's report format, all six sections, with every finding in the finding template (verbatim quote plus source ref on every evidence line) — as raw markdown in your final message, between two marker lines that each appear exactly once, on their own lines: `=====BEGIN OKR-NINJA REPORT=====` immediately before the report's first line and `=====END OKR-NINJA REPORT=====` immediately after its last line. Everything between the markers is graded verbatim, so put nothing there but the report, do not wrap it in a code fence, and do not alter its characters (dashes, quotes, `$`, `<`, `&`) for any tool. Write nothing anywhere except scratch files inside `{{run_dir}}`, and do not modify `{{input_path}}`.
- Source refs use the local-file form from the report format: `<file path> › <nearest heading> › line N`, where line numbers refer to `{{input_path}}` exactly as it is.

When you are done, your final message is the marker block and nothing else — no path, no summary, no commentary outside the markers.
