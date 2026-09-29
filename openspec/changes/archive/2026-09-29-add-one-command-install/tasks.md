## 1. License and version in the skill

- [x] 1.1 Add a root `LICENSE` with the standard MIT text, `Copyright (c) 2026 Difan Lin` (design D8). Verify with `head -3 LICENSE`.
- [x] 1.2 Add `license: MIT` and a `metadata:` map holding `version: "0.2.0"` to `SKILL.md`'s frontmatter (design D6). Verify: `git diff SKILL.md` shows only added frontmatter lines; the `description` line is byte-identical to `HEAD`; the body is untouched; the file stays under ~150 lines.
- [x] 1.3 Add `__pycache__/` and `*.pyc` to `.gitignore`. Verify `git check-ignore -q __pycache__/x.pyc`.

## 2. Installer: version, license, output

- [x] 2.1 Split the frontmatter check so it validates `SKILL.md` text from any source, and add the `metadata.version` rule: present, and semver per design D6. On success, `check` prints the name and version. Verify:
  - `python3 install.py check` exits 0 and prints `okr-ninja` and `0.2.0`;
  - in scratch checkouts under `$TMPDIR`, no `metadata`, `version: "0.2"`, `version: "v0.2.0"` and `version: "01.2.0"` each exit 1 naming `metadata.version`;
  - `1.0.0-rc.1+build.5` passes.
- [x] 2.2 Add `LICENSE` to the checkout payload (required, never read through a symlink) and drop `PLUGIN_VERSION`, so `build` writes `metadata.version` into `plugin.json`. Verify with `python3 install.py build --out $TMPDIR/b1`:
  - both archives hold `LICENSE`, and the manifest's `version` is `0.2.0`;
  - a second build into `$TMPDIR/b2` is byte-identical under `cmp`;
  - a scratch checkout without `LICENSE` exits 1 naming it and writes nothing.
- [x] 2.3 Make `install` read each target's previous version defensively before the swap (design D9: regular file only, at most 64 KB, universal newlines, never raises). It prints the installed version plus `was X`, `new install` or `was unversioned`. Verify in the test suite:
  - a first install prints `new install` for both targets, and a second prints `was 0.2.0`;
  - a target with a frontmatter-less `SKILL.md` prints `was unversioned`;
  - a CRLF `SKILL.md` still reports its version;
  - a `SKILL.md` symlinked to `/dev/zero` gives `was unversioned` and a normal replacement.
- [x] 2.4 Update the docstring and help text:
  - the payload line names `LICENSE`;
  - the Commands block lists `--release`, `--repo` and `--source`, the remote-mode trigger, and the one-liner;
  - `--out`'s help says "default: dist/ in the checkout, or the current folder in remote mode";
  - pointers go only to paths that will not move: the archived cross-platform design and `openspec/specs/distribution/spec.md`;
  - in-code design references are qualified ("cross-platform D6", "one-command D5").

  Verify: `grep -n "plus the files under references/ and examples/" install.py` finds nothing; every path named in the docstring exists; `python3 install.py build --help` shows the new `--out` text.

## 3. Installer: remote mode

- [x] 3.1 Implement the detection function (design D1): local only for a real `__file__` not starting with `<`, `argv[0]` not `-` or `-c`, `SKILL.md` and `README.md` beside the file, and no `--release`, `--repo` or `--source`. Details:
  - a checkout run prints the folder it reads;
  - whenever `__file__` is a real file, its folder feeds the checkout-containment guard in both modes;
  - add `--release`, `--repo` and `--source` to every command;
  - validate `--repo` per the spec: `OWNER` of 1–39 letters, digits and hyphens starting with a letter or digit; `NAME` of 1–100 characters from `[A-Za-z0-9._-]`, not `.` or `..`;
  - validate a non-`latest` `--release` against the tag rule, before any request;
  - refuse `--source` with `--release latest`;
  - require `--source` to be a regular file of at most 100 MB.

  Verify in the test suite.
- [x] 3.2 Implement the opener factory and fetch layer (design D4, D12), and verify each in the test suite with a fake HTTPS handler behind the real redirect handler:
  - https-only redirect checking on `github.com` and `codeload.github.com`;
  - `User-Agent`, a 60-second timeout, and the 100 MB cap applied to both `Content-Length` and the stream;
  - every open or read failure mapped to a refusal naming the URL;
  - the platform-specific certificate advice.
- [x] 3.3 Implement latest-release resolution (design D2: any owner and name in a `/releases/tag/<tag>` final path, 404 or any other final path means no release) and the archive URL for a tag (design D3). Verify in the test suite:
  - a 302 to `/releases/tag/v0.2.0`, and a 301 rename followed by that 302, both yield `v0.2.0`;
  - `/releases` and a 404 exit 1 naming the repository;
  - a percent-encoded tag is decoded and a malformed one is refused.
- [x] 3.4 Implement the archive reader (design D5):
  - validate names on `orig_filename`, refusing empty, `.` and `..` segments, backslashes, NUL, drive letters and duplicates;
  - require one top-level folder, ignore directory entries, and apply the symlink rule;
  - filter the payload exactly as the checkout reader does, hidden components at any depth included;
  - apply the portable-name rule, the NFC-plus-casefold collision rule (file-versus-folder prefixes included) and the declared-size cap before decompressing, then read in chunks;
  - turn every `zipfile`/`zlib` failure into a named refusal;
  - decode `SKILL.md` with universal newlines;
  - print names with `ascii()`.

  Verify in the test suite with crafted zips covering every refusal and scenario in the spec's archive requirement, and with `git archive`-built zips.
- [x] 3.5 Implement the tag/version agreement, the `name: okr-ninja` rule for remote payloads (design D7) and the current-directory default for remote `build` (design D10). Wire remote payloads into `check`, `build` and `install`, and print the repository, tag (or archive path) and version before acting. Verify end to end in the test suite.
- [x] 3.6 Keep `install.py` pure ASCII, grammar-compatible with 3.8 and free of 3.9+ standard-library APIs (design D11, D13). Verify by test.

## 4. Tests

- [x] 4.1 Create `tests/test_install.py` (stdlib `unittest`, offline, design D13). Every installer-related scenario in the delta spec maps to at least one test, named after the scenario where practical. It includes:
  - the pure detection-function tests;
  - the two subprocess detection tests with no remote options (piped from inside a checkout; a lone copy beside an installed skill), each with `HTTPS_PROXY`/`https_proxy` pointed at `http://127.0.0.1:9` and `NO_PROXY`/`no_proxy` cleared, asserting exit 1, the latest-release URL in stderr, and an unchanged scratch `HOME`;
  - the in-process `main([...])` runs through the opener seam: latest moving from v0.2.0 to v0.3.0 across two runs; a pinned `--release` with the exact URL sequence; a resolved tag whose archive disagrees; a break mid-download;
  - the piped `python3 -I - < install.py --source …` install-then-update from a scratch folder holding a `json.py` that raises on import;
  - a remote `build` whose archives match a checkout build byte for byte for the same payload;
  - a `--source` archive with `name: other-skill` that leaves `<home>/.claude/skills/other-skill` unchanged by checksum;
  - `install.py` copied into a folder that is `<home>/.claude/skills/okr-ninja` and run with `--source`, which exits 1 with the folder unchanged;
  - the frozen v0.2.0-shaped archive installed by the current code;
  - the static checks: ASCII, 3.8 grammar, and no 3.9+ APIs.

  Verify: `python3 -m unittest discover -s tests -v` passes on `/usr/bin/python3` (3.9) and `/opt/homebrew/bin/python3.12`, and afterwards `git status --short` shows no `__pycache__`.

## 5. Docs and gate

- [x] 5.1 Rewrite README's Installation section per the modified requirement "Install routes are documented per platform":
  - lead with the isolated one-liner: the macOS/Linux pipe form, the Windows PowerShell temp-file form gated on the download's exit code, and re-running as the update;
  - add the inspect-first form using `mktemp -d`, the options, the note that `--release` pins the skill and not the installer, and the fully pinned form;
  - keep the remote `build` for Cowork and claude.ai with the re-upload note, the `.plugin` route for plugin hosts, the platform table, and the clone route with the real URL;
  - add a short License section, and add `LICENSE` and `tests/` to Repository layout.

  Verify:
  - `grep -n "your-org" README.md` and `grep -n "o install.py" README.md` find nothing;
  - every documented `python3`/`py` command that runs a downloaded `install.py` carries `-I` (the clone route runs the checkout's own file and needs none);
  - `grep -n "okr-ninja.plugin" README.md` matches in the Installation section;
  - each of Claude Code, Cursor, Codex, Cowork and claude.ai appears there;
  - `grep -n "ln -s" README.md` finds nothing;
  - the pinned form's URL tag equals its `--release` value.
- [x] 5.2 Update `CLAUDE.md`:
  - **File map:** the `install.py` row names `LICENSE` in the payload and the remote mode; new rows cover `LICENSE` (with the version living in `SKILL.md`'s `metadata.version`) and `tests/`.
  - **Testing step 1:** gains `python3 -m unittest discover -s tests`, run on every change because it is offline and takes seconds.
  - **Change-workflow paragraph:** mentions it.
  - **New "Releasing" section:**
    - bump `metadata.version`, using semver: patch for wording and fixture or answer-key corrections, minor for rubric, taxonomy, procedure, report-format or `description` changes, major for a breaking report or install contract;
    - run the checks, then merge;
    - `gh release create vX.Y.Z --target <merge-sha> --prerelease --generate-notes`;
    - smoke `curl … | python3 -I - --release vX.Y.Z` into a scratch home;
    - `gh release edit vX.Y.Z --prerelease=false --latest`;
    - smoke the unpinned one-liner;
    - note that merged skill changes reach one-liner users only when a release is cut;
    - note that `main`'s installer must stay able to install every published release, adding a frozen-shape test whenever a release changes the payload's shape.

  Verify with `grep -n "Releasing\|LICENSE\|tests/\|unittest" CLAUDE.md`.
- [x] 5.3 Add "`python3 -m unittest discover -s tests` passes" to the structural checks in `.claude/skills/openspec-loop/phases/verify-gate.md`. The path is write-protected in the sandbox, so make the edit through the editor tool with the owner's approval; if approval is refused, record the gap here and in the final report. Verify with `grep -n "unittest" .claude/skills/openspec-loop/phases/verify-gate.md`.

## 6. Verify

- [x] 6.1 `python3 install.py check` and `python3 evals/grader/harness.py check` both exit 0, and `python3 -m unittest discover -s tests` passes on both interpreters.
- [x] 6.2 `openspec validate add-one-command-install --strict` passes.
- [x] 6.3 Checkout-route regression against a scratch `HOME` on both interpreters:
  - the default install writes both targets with exactly the payload, now including `LICENSE`;
  - `--only agents`, `--project DIR`, a missing `--project`, a symlinked target pointing at a scratch checkout (the checkout unchanged by checksum), a target holding `.git`, and running from inside a target all behave as the `distribution` spec requires.
- [x] 6.4 `git status --short` shows no change under `references/`, `examples/` or `evals/`, `SKILL.md`'s diff is added frontmatter lines only, and no `__pycache__` appears. Record here that the fixture eval is skipped, because no procedure, rubric, taxonomy, report-format or description text changed, and that the routing review is not needed, because `description` is unchanged. **Done 2026-09-25:** no change under `references/`, `examples/` or `evals/`; `SKILL.md`'s diff is `+license: MIT`, `+metadata:`, `+  version: "0.2.0"`. Fixture eval skipped (no procedure, rubric, taxonomy, report-format or description text changed); lifecycle eval skipped (publish path untouched); routing review not needed (`description` byte-identical). 6.3 is covered by the suite's replacement-safety and installer-target classes, which pass on 3.9.6 and 3.12.14.
- [x] 6.5 Independent refute-mode verification by fresh subagents that did not write the change, briefed with design.md:
  - spec conformance of `install.py`, the tests and the docs against the delta spec, including a check that every installer scenario maps to a test;
  - an adversarial security pass on the remote path (archive parsing, redirects, trigger detection, what gets written where).

  Green only if no cited, reproducible violation remains. **Done 2026-09-29:** green after five repair cycles and six gate runs (sections 7-15). The last full four-lens run is in section 13. The owner then chose a targeted non-author check of cycle 5, recorded in section 15.
- [x] 6.6 At archive time, add this change's archived design path to the pointers in `install.py`'s docstring and `tests/test_install.py`'s header, then confirm with a grep that every path named in either exists and that neither names `openspec/changes/add-one-command-install`.

## 7. Repair cycle 1 (independent refute-mode verification, 2026-09-25)

The first gate pass was RED: five non-author lenses (spec conformance, security, test adequacy by mutation, platform, coherence) reported 27 findings, each reproduced by a separate skeptic; 3 more were refuted. The critical one: on Linux the inspect-first form's `mktemp` file lands in world-writable `/tmp`, where another user can plant `SKILL.md` + `README.md` and turn the run into a checkout run that installs their skill under any name.

- [x] 7.1 C1 (critical): the inspect-first form downloads into `mktemp -d` (README, spec, design D11), and `checkout_root` never takes a world-writable folder for a checkout (spec, design D1). Verify by test: a fake checkout in a `0o1777` folder runs remote and installs nothing from it.
- [x] 7.2 W1: bzip2 and LZMA payload entries are refused before any decompression (a 6.5 KB archive drove 1–2 GB of RAM). Verify by test for both methods.
- [x] 7.3 W2: any exception while listing or reading an archive becomes a named refusal (`LZMAError`, zip64 `OverflowError`), and an empty exception message falls back to its type name. Verify by test (bad LZMA properties, zip64 offset 2**64-1, an entry running past the end).
- [x] 7.4 W3: C1 controls (U+0080–U+009F) and DEL are refused in payload names (Unicode category `Cc`), and `build` prints archive-derived names escaped. Verify by test (U+0085, U+009B, 0x7F; `build` stdout is ASCII for a non-ASCII payload name).
- [x] 7.5 W4: a response that ends before its declared `Content-Length` is refused naming the URL. Verify by test with a real `http.client.HTTPResponse` over a fake socket.
- [x] 7.6 Test adequacy: adopt the mutation-verified suite additions (writes into the system temp folder are caught; folder-before-file case collision; drive-letter needles and a `C:/` top folder; network failure causes asserted; truncated entry; `references/__pycache__/notes.md`; `0o120755` symlink; duplicate names printed escaped; dangling-link and linked-`SKILL.md` previous versions; a codeload tag page; `Path.readlink` and dict-union static checks). Verify each added test passes on the real code.
- [x] 7.7 Docs: CLAUDE.md Releasing (installer changes reach users on merge; the smoke uses one home twice), the `install.py` file-map row, the top-level `--help` description, `openspec/config.yaml`'s payload wording, README's opening line, and design Migration step 3. Verify by grep.

## 8. Repair cycle 2 (gate re-run, 2026-09-25)

The gate re-run confirmed all 27 cycle-1 findings resolved (each re-reproduced against the repaired code, mutants killed on 3.9 and 3.12) and reported 7 new findings, each reproduced by a skeptic; 7 more were refuted.

- [x] 8.1 W1: the collision key uses canonical caseless matching (NFD, casefold, NFD); spec and D5 say so. Verify by test with `references/\u0390.md` + `references/\u03aa\u0301.md`.
- [x] 8.2 W2/W3: frontmatter-derived values are quoted with `ascii()` in check errors; everything printed passes an escape filter for control and format characters; stdout and stderr use `backslashreplace`; an install's `OSError` text is escaped. Verify by tests: `check --source` with a U+202E `name` prints ASCII-escaped output and exits 1; a latin-1 stdout gives no traceback.
- [x] 8.3 W4: remote `build` resolves the current folder lazily and refuses with a named message when it no longer exists; `install` and `check` from a deleted folder still work. Verify by subprocess test.
- [x] 8.4 S1: a file named `__pycache__` is skipped by both the archive and the checkout reader. Verify by test.
- [x] 8.5 S2: the re-raise test reaches the read loop (so deleting `except Refusal: raise` fails it). Verify by mutation.

## 9. Final gate run (2026-09-26): RED; the loop's two repair cycles are spent, so this is held for the owner

The final run confirmed all 34 earlier findings resolved: each was re-reproduced against the current code, and 39 mutants were killed on 3.9 and 3.12. Fuzzing ran 21,000 crafted archives with no traceback, and the redirect tricks all failed. The run reported 3 new findings, each reproduced by a skeptic, and refuted 1. The spec-conformance lens stalled and did not finish, so it must be re-run.

- [x] 9.1 W (security): on Python 3.12+, a zip entry's Info-ZIP Unicode Path extra field (0x7075) replaces `ZipInfo.filename` after `read_archive` validated `orig_filename`. An archive from `--source` or a `--repo` fork can therefore install a name the rules refuse (`references/x\..\..\evil.md`), collapse `references//x.md` onto another payload file, or pull a non-payload entry into the payload. GitHub's own archives never carry 0x7075. Fix: refuse any entry whose extra field carries 0x7075, scanning `info.extra` so the result is the same on every interpreter; use `orig_filename` for selection and the written path; refuse a repeated relative path before `selected[rel] = info`. Verify by a test that appends a 0x7075 entry.
- [x] 9.2 W: a non-ASCII `metadata` key from an archive prints raw in `check` errors (`'metadata.ключ'`), while top-level keys are quoted with `ascii()` (design D5). Fix: escape the key label once in `check_metadata` before both `scalar()` calls. Verify by test.
- [x] 9.3 S: four cycle-2 escaping sites have no test. The mutants that revert them survive: an install's `OSError` text, unexpected top-level keys, the `metadata.version` value, and a duplicate key. Fix: add the tests from the finding, including an ENAMETOOLONG write of a 256×`é` entry name, and confirm each mutant is killed.
- [x] 9.4 Re-run the spec-conformance lens of the final gate, which stalled. **Done 2026-09-27** in the cycle-3 gate run (section 11), split into two lenses that both finished.

## 10. Repair cycle 3 (owner-authorised by `/opsx:apply`, 2026-09-26)

- **9.1 done.** `read_archive` refuses any entry whose extra field carries 0x7075, walking the headers as `zipfile` does (`extra_ids`), and never reads `ZipInfo.filename`: selection, relative paths and messages use `orig_filename`. The requested guard against a repeated relative path is not added as code, because it cannot fire: a relative path is the stored name minus the one top-level folder, and stored names are already refused when repeated (`test_duplicate_entries_are_refused`). Spec and D5 now name the field. Tests: `test_a_unicode_path_extra_field_is_refused` covers four renames: past the rules, non-payload into the payload, onto another payload file, and the same name. Each is refused by `read_archive` and by `install --source` with nothing written, and on 3.12+ the test first asserts that `zipfile` really renames the entry. `test_other_extra_fields_are_read_as_git_archive_writes_them` shows that git's 0x5455 timestamp field still reads, and that 0x7075 is found when it is not the first field.
- **9.2 done.** `check_metadata` escapes the key once (`label`) before both `scalar()` calls, and the key label is no longer quoted twice. Test: `test_a_non_ascii_metadata_key_is_escaped`.
- **9.3 done.** Four new tests: `test_an_install_write_error_names_the_file_escaped` (the ENAMETOOLONG write of a 256×`é` name, whose output is ASCII and leaves no target or staging folder), `test_an_unexpected_non_ascii_key_is_escaped`, `test_a_non_ascii_version_is_escaped` and `test_a_duplicate_non_ascii_key_is_escaped`.
- **Checks.** The suite passes with 165 tests on 3.9.6 and 3.12.14. `scratch/mutate.py` kills all 21 mutants on both interpreters, 7 of them new: the 0x7075 check removed, only the first extra header walked, the raw metadata label, the raw `OSError` file name, raw unexpected keys, the raw version, and the raw duplicate key.

## 11. Gate run after repair cycle 3 (2026-09-27): RED, held for the owner

Four non-author lenses ran, each followed by a skeptic: spec conformance for the MODIFIED requirements, spec conformance for the ADDED requirements, adversarial security, and fix confirmation.

- **Fix confirmation:** 9.1–9.3 are resolved. The lens built its own 0x7075 attack zips and confirmed that 3.12 renames them, and that install, check and build refuse them on both interpreters with nothing written. It found no read of `ZipInfo.filename`. The escaping mutants fail the suite on both interpreters.
- **MODIFIED requirements:** fully conformant. No sentence or scenario was silently dropped from the main spec.
- **Result:** 4 findings were confirmed and 3 refuted.
  - Refuted: the rebuild-reproducibility tests depend on timing; deeply nested names use quadratic memory with no spec'd bound; Windows device-name forms outside the spec's list.

- [x] 11.1 W (security): on Python 3.9, which ships Unicode 13, the collision key misses case pairs assigned in Unicode 14 or later, such as U+A7C0/U+A7C1, U+2C2F/U+2C5F and the Vithkuqi letters. APFS on Darwin 23 merges these pairs. The result is a silent overwrite: `note-Ꟁ.md` and `note-ꟁ.md` install as one file with the second file's bytes, the run reports 6 files, and 5 are on disk. 3.12 refuses the same archive. `/usr/bin/python3` 3.9 is what the macOS one-liner runs. Fix: `unportable` refuses a code point the running interpreter treats as unassigned (category `Cn`), and the spec's refusal list and D5 say so. Verify by test with that pair on both interpreters.
- [x] 11.2 W: the catch-all refusals print zipfile's exception text raw (`cause(e)`, install.py:657 and :757). That text repeats the entry name through `%r`: `Bad CRC-32 for file '…/résumé.md'`, and `File <ZipInfo filename='…/рубрика.md' …> is encrypted`. Fix: escape non-ASCII in `cause()`. Verify by giving the checksum and encryption tests non-ASCII entry names, so `assertArchiveRefused`'s ASCII check covers this path.
- [x] 11.3 S: on 3.12, a 0x7075 field that zipfile cannot parse makes `ZipFile()` raise before the named check. The refusal says the zip is unreadable and does not name the entry, while 3.9 names it. The two cases are an empty field and invalid UTF-8 with a matching CRC. Safety holds: exit 1 and nothing written. Fix: narrow the scenario, because the unreadable-zip bullet already covers a malformed field. Add a malformed-field case asserting exit 1 and nothing written.
- [x] 11.4 S: argparse's `unrecognized arguments` error echoes raw argv (U+202E, ESC) and bypasses `shown()`, against the unqualified clause "no output the installer prints SHALL carry a raw control or format character". Fix: an `ArgumentParser` subclass whose messages pass through `shown()`. Verify by extending `test_unknown_command_arguments_do_not_traceback` with a U+202E argument.

## 12. Repair cycle 4 (owner-authorised, 2026-09-27)

- **11.1 done.** `unportable` refuses a code point that the running interpreter's Unicode database leaves unassigned (`Cn`). The message names that Unicode version. A new case pair always involves a newly assigned character, so an older Python refuses exactly the pairs it cannot fold. Spec refusal list and D5 updated. Tests:
  - `test_a_code_point_this_python_does_not_assign_is_refused` (U+0378, unassigned in every Unicode so far);
  - `test_a_case_pair_newer_than_this_pythons_unicode_is_refused` (`note-\ua7c0.md` + `note-\ua7c1.md`: refused as a collision on 3.12 and as an unknown character on 3.9, with nothing written on either).
- **11.2 done.** `cause()` escapes non-ASCII, the same way every other archive-derived name is escaped. D5 updated. The checksum and encryption tests now use non-ASCII entry names (`résumé.md`, `рубрика.md`), so `assertArchiveRefused`'s ASCII check covers both catch-alls. `assertArchiveRefused` moved to `InstallerCase` so every class can use it.
- **11.3 done.** The scenario is narrowed: a field Python can parse is refused by name on every interpreter; a field 3.12+ cannot parse makes the archive unreadable there, which is refused as such. `read_archive` also silences zipfile's warning about an empty field, which is then refused by name. Test: `test_a_unicode_path_field_python_cannot_parse_is_refused` (an empty field, a non-UTF-8 name, an empty name). On every interpreter it asserts exit 1, nothing written and no warning, and below 3.12 that the entry is named.
- **11.4 done.** A `Parser` subclass passes everything argparse prints through `shown()`. D5 updated. Test: `test_usage_errors_print_the_command_line_escaped`.
- **Checks.** The suite passes with 169 tests on 3.9.6 and 3.12.14. The 4 new mutants are killed on 3.12, and 3 of them on 3.9. The fourth, removing the warning filter, survives on 3.9 only, because 3.9's zipfile never warns, so the mutant makes no difference there. `openspec validate --strict`, `install.py check` (okr-ninja 0.2.0) and `harness.py check` all pass, and `install.py` is pure ASCII.

## 13. Gate run after repair cycle 4 (2026-09-28): RED, held for the owner

Four non-author lenses ran, each followed by a skeptic. Two lenses were re-run after API failures.

- **MODIFIED requirements:** no findings.
- **Fix confirmation:** no findings. 11.1–11.4 are confirmed fixed on both interpreters. A full sweep of U+0020..U+10FFFF on APFS found 0 merged pairs that the key plus the `Cn` rule misses: on 3.9, 2,439 merges; on 3.12, 2,479.
- **Security:** one finding, the same one the ADDED-requirements lens reported.
- **Result:** 2 distinct findings confirmed.

- [x] 13.1 W: on Python 3.12, when two central-directory records share one local header, zipfile's `open()` warns `Overlapped entries: '<name>' (possible zip bomb)` and carries on. The warning goes to stderr through the warnings module, so the stored name prints with raw non-ASCII letters (`résumé.md`). It bypasses `ascii()`, `cause()` and `shown()`, and the install still exits 0. The read loop at install.py:755 has no warnings filter. This breaks spec.md:178 ("Archive-derived names … SHALL be printed in escaped form wherever the installer prints them"). Fix: refuse, on every interpreter, two records that share a `header_offset` (a GitHub archive never has them), and turn any zipfile warning during reading into a named refusal. Verify with an aliasing record over a non-ASCII payload name: exit 1, ASCII stderr, no warning, nothing written.
- [x] 13.2 S: the 0x7075 bullet says "any entry carries" the field, but `read_archive` scans only the central-directory extra (D5 scopes it that way). An entry whose local header alone carries 0x7075 is installed under its stored name. This has no safety impact: the installer never reads the local extra, and CPython reads 0x7075 only from the central directory. Fix: scan each entry's local-header extra too, or narrow the bullet to the central directory to match D5. Add a local-header-only test case.

## 14. Repair cycle 5 (owner-authorised, 2026-09-28; the owner chose a targeted check afterwards)

- **13.1 done.** `read_archive` refuses two central-directory records that share a `header_offset`, naming both, on every interpreter. The read loop also runs with zipfile warnings turned into errors, so any warning becomes a named refusal through the catch-all, escaped by `cause()`. Spec: the "two entries share a name" bullet gains shared local headers, and a new scenario reads "Two records for one entry's data are refused". D5 is updated to match. Tests:
  - `test_entries_that_share_one_local_header_are_refused`: an aliasing record over `references/résumé.md`, named outside the payload and inside it; asserts exit 1, ASCII output, no warning and nothing written;
  - `test_a_zipfile_warning_while_reading_is_a_named_refusal`;
  - `alias_entry` is a new test helper.
- **13.2 done.** `local_extra` reads each entry's local-header extra field from the archive bytes, and the 0x7075 check scans it as well as the central copy. The spec bullet and D5 say so. Test: `test_a_unicode_path_field_in_the_local_header_alone_is_refused`. It clears only the central copy's field ID and asserts that no interpreter renames the entry, and that the archive is refused naming the entry.
- **Checks.** The suite passes with 172 tests on 3.9.6 and 3.12.14. `scratch/mutate.py` covers 28 mutants, 3 of them new: the shared-header check removed, the read-warning filter removed, the central extra scanned alone. All 28 are killed on 3.12. On 3.9, 27 are killed; `no-warning-filter` survives, as expected, because 3.9's zipfile never warns. `openspec validate --strict`, `install.py check` (okr-ninja 0.2.0) and `harness.py check` pass, `install.py` is pure ASCII, and nothing changed under `references/`, `examples/` or `evals/`.

## 15. Targeted check of repair cycle 5 (2026-09-29): GREEN

Two non-author lenses covered cycle 5, each followed by a skeptic.

**Fix confirmation: no findings.**
- It reproduced both original problems on copies of the code with the fix reverted:
  - 3.12 printed the `Overlapped entries` warning raw and installed;
  - a zip whose Unicode Path field (0x7075) sat only in the entry's local header installed.
- On the current code, `install`, `check` and `build` refuse both on 3.9 and 3.12: exit 1, ASCII output, no warning, nothing written.
- Each cycle-5 revert fails the suite on both interpreters.
- A real `git archive` zip with a symlink, a hidden file and a non-ASCII name still installs byte-for-byte like a checkout.

**Security: two findings.**
- One suggestion was confirmed: C5-1, fixed here. The shared-header test used ASCII alias names, so a message that printed the second name raw, or dropped it, still passed.
- The aliases are now `evals/\u00ff.md` and `references/c\u00f3pia.md`, and the test asserts both escaped names. Both mutants now fail on 3.9 and 3.12.
- One suggestion was refuted: C5-2. Overlapping entries at *different* offsets fall outside the spec bullet and D5's scope. 3.12 refuses them through `BadZipFile`; 3.9 reads each entry's own header.

Pointers updated at archive time (6.6). `install.py`'s docstring and the test header now name this change's archived design, beside the cross-platform one.

