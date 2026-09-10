You are running an evaluation of the OKR-Ninja skill. Load the skill by reading `{{skill_md}}` and follow its procedure exactly, loading each file under `{{references_dir}}` at the step where SKILL.md tells you to. Do not decide whether the skill applies — it applies.

Task: review the {{team}} team's OKRs alone, in depth. Exactly one team is in scope, so this is a single-team-mode run.

Rules for this run:

- `{{input_path}}` is the only source of OKR content. It contains the {{team}} team's OKR page and a business-review appendix, nothing else. Do not read any other file for OKR content, do not open anything under `examples/` or `evals/keys/`, and do not search the repository or its history for related material. No Atlassian connection is available.
- There is no user to ask. Treat {{team}} as the confirmed scope and the period as the quarter the file states. No company strategy document is provided: state in the report that company-level strategy tracing was out of scope and apply the rubric's rules for that case.
- This is an eval run: never publish artifacts and never create or modify any registry file. The skill's publish step is skipped for eval runs.
- Write the complete report — exactly the single-team report defined in the skill's report format, with every finding in the finding template (verbatim quote plus source ref on every evidence line) and the score table with all eleven dimension columns — as markdown to `{{report_path}}`. Write nothing else anywhere except scratch files inside `{{run_dir}}`, and do not modify `{{input_path}}`.
- Source refs use the local-file form from the report format: `<file path> › <nearest heading> › line N`, where line numbers refer to `{{input_path}}` exactly as it is.

When you are done, reply with only the path of the written report.
