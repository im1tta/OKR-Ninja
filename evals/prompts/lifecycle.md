You are running an evaluation of the OKR-Ninja skill. Load the skill by reading `{{skill_md}}` and follow its procedure exactly, loading each file under `{{references_dir}}` at the step where SKILL.md tells you to. Do not decide whether the skill applies — it applies.

Task: audit the OKR portfolio in `{{corpus_path}}` for quality and cross-team alignment — every team in the file is in scope, so this is a portfolio-mode run — and then {{task_tail}}

Rules for this run:

- `{{corpus_path}}` is the only source of OKR content. Do not read any other file for OKR content, {{corpus_scope_note}} and do not search the repository or its history for related material. No Atlassian connection is available.{{corpus_note}}
- There is no user to ask. Treat the teams enumerated in the file as the confirmed scope, the period as the quarter the file states, and the file's company priorities section as the strategy source.
{{exemption_note}}
  - Review working folder: `{{work_dir}}`.
  - The artifact surface in this environment is one local command. Use it and nothing else to verify, create, or update an artifact — there is no other artifact tool here, and it offers no way to list artifacts:
    - verify a URL — `python3 {{seam}} read --store {{store}} --url <url>` (exit 0 with the artifact's title and favicon when it is reachable; exit 3 when it is dead)
    - create — `python3 {{seam}} publish --store {{store}} --key <deliverable key> --title <title> --favicon <emoji> --file <path>` (prints the new URL)
    - update in place — `python3 {{seam}} update --store {{store}} --key <deliverable key> --url <url> --file <path>` (keeps the URL; add `--title`/`--favicon` only if they should change)
  - The cycle date for this run is **{{cycle_date}}**.
{{deliverables_header}}
{{deliverables_block}}
{{supplied_block}}- Write each deliverable as markdown into the working folder under the file name given above{{publish_clause}}, and do not rewrite it afterwards. Report content follows the skill's report format — the deliverable named as the portfolio report is the full six-section portfolio report, with every finding in the finding template (verbatim quote plus source ref on every evidence line).
- Source refs use the local-file form from the report format: `<file path> › <nearest heading> › line N`, where line numbers refer to `{{corpus_path}}` exactly as it is.
- Write a short run summary to `{{summary_path}}`: {{summary_ask}}
- Write nothing outside `{{run_dir}}`, do not modify `{{corpus_path}}`, and do not touch any file under `evals/` other than your own run directory and the seam store named above.

When you are done, reply with only the path of the written run summary.
