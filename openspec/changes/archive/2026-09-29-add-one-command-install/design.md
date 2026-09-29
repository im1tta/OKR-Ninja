## Context

`install.py` (stdlib only, Python 3.8+) reads the runtime payload from the checkout it sits in, validates `SKILL.md`'s frontmatter, and then installs the payload into `.claude/skills` and `.agents/skills` or builds the `.skill` and `.plugin` archives. Its payload reader already returns `{relative path: bytes}` and every writer consumes that map, so the source of the bytes is the only thing a remote mode changes. The frontmatter reader is strict by design (D2 of `openspec/changes/archive/2026-09-24-add-cross-platform-install/design.md`, "cross-platform D2" below) and already accepts a `metadata` map. The replacement-safety rules (cross-platform D6) stay as they are. See proposal.md for motivation; the requirements are in `specs/distribution/spec.md`.

Constraints: no third-party packages; `install.py` stays a single self-contained file, since the one-liner fetches only that file; the repo has no releases or tags yet; GitHub is unreachable from the development sandbox, so every behaviour must be testable offline. A pre-implementation review (four lenses, each finding checked by a skeptic) shaped D1, D4, D5, D11, D13 and the release order below.

## Goals / Non-Goals

**Goals:**
- One command that both installs and updates, needing only Python and a way to fetch one file.
- Remote runs no less safe than checkout runs: same check, same payload filter, same replacement rules, nothing written until the payload is fully read and checked, and no way for an archive to choose which folder gets replaced.
- A version that every installed copy and upload carries, so a user can see what they have and what an update replaced.

**Non-Goals:**
- Verifying archive checksums or signatures. HTTPS to GitHub is the trust anchor; a user who wants more inspects `install.py` and pins both the installer and the release (D11).
- Resuming or caching downloads, proxies beyond what `urllib` already honours (`HTTPS_PROXY`), or GitHub Enterprise hosts.
- Detecting that an update is available without running the command.
- Bounding the zip central directory's entry count. The 100 MB download cap already bounds it, and a hostile archive needs a user-chosen `--repo` fork or `--source` file.

## Decisions

### D1. Remote mode is chosen by where the script is, and a checkout must look like one
Remote mode is the default. The installer reads its own checkout only when three things hold. First, `__file__` names a real file: not absent (`python3 -c`), not starting with `<` (`python3 -` sets `<stdin>`, and a file literally named `<stdin>` in the current folder must not count), and `sys.argv[0]` is not `-` or `-c`. Second, that file's folder holds both `SKILL.md` and `README.md`, and on POSIX is not world-writable, so a shared folder such as Linux's `/tmp`, where any local user can plant files, is never taken for a checkout. Third, none of `--release`, `--repo` or `--source` is given.

`README.md` is the checkout marker because installed copies and unpacked `.skill` uploads now carry `SKILL.md`, `LICENSE`, `references/` and `examples/`. Those four no longer tell a checkout from a copy, while a clone or a GitHub source archive always has `README.md`. A checkout run prints the folder it reads, so a surprise is visible.

The detection is one pure function of (`__file__`, `argv[0]`, the file system), unit-tested directly and by subprocess runs with no remote options: piped from inside a checkout, and a lone copy beside an installed skill.

Whenever `__file__` is a real file, in either mode, its folder is passed to the existing "target is or contains the checkout" guard. A copy saved inside `~/.claude/skills/okr-ninja/` therefore cannot delete itself.

*Alternative:* an explicit `--remote` flag. Rejected because it lengthens the one-liner, and forgetting it would silently install whatever checkout the user stands in.

### D2. "Latest" comes from the `/releases/latest` redirect, not the REST API
`https://github.com/OWNER/NAME/releases/latest` redirects to `/releases/tag/<tag>` for the newest published release. This is GitHub's documented link form, and it never selects drafts or pre-releases. The installer follows it and accepts a final URL on `github.com` whose path matches `/<owner>/<name>/releases/tag/<tag>` for any owner and name. The owner and name are deliberately not compared, because GitHub's rename and case redirects may change them. Any other final URL, or a 404, means there is no published release. The tag is percent-decoded and must match the tag rule. An explicit `--release` value is checked against the same rule before any request.

*Alternative:* `api.github.com/repos/…/releases/latest`. Rejected: it allows only 60 unauthenticated requests per hour per IP, which a shared office NAT exhausts, and it adds a third host and JSON parsing.

### D3. Zip archives from GitHub's archive route
The archive URL is `https://github.com/OWNER/NAME/archive/refs/tags/<tag>.zip`, which redirects to `codeload.github.com`. Zip rather than tar, because `zipfile` reads from memory with random access and behaves the same from 3.8 to 3.13, whereas `tarfile`'s safety filters exist only from 3.12. GitHub's zips are `git archive` output: a directory entry for every folder, a zip comment holding the commit, `create_system` 0 with mode 0 for ordinary files, and `create_system` 3 with mode `0o120777` for symlinks (verified locally). `--source` accepts the same shape. So `git archive --format=zip --prefix=OKR-Ninja-0.2.0/` from a commit is a faithful stand-in, and the test suite builds its archives exactly that way (D13).

### D4. Hosts, schemes and failures are handled on every hop
A single opener factory builds `urllib`'s opener with a redirect handler that checks each redirect target before following it. The first URL is checked the same way. The rule is scheme `https`, host exactly `github.com` or `codeload.github.com`, no user-info, default port. Anything else raises a refusal naming the URL.

Requests carry a `User-Agent` naming the installer and a 60-second timeout. The response is read in chunks with a running total. A declared `Content-Length` above 100 MB is refused up front, and the stream stops past 100 MB either way.

Every failure while opening or reading, whether `HTTPError`, `URLError`, `OSError`, `http.client.HTTPException` or `ValueError`, becomes a refusal naming the URL and the cause. The opener factory is also the test seam: tests add a fake HTTPS handler behind the real redirect handler, so redirect checking runs for real in-process.

`http.client` returns a short body silently when a connection closes before the declared `Content-Length`, so `download` compares the bytes received with that length (unless the response is chunked) and refuses a short read naming the URL, rather than letting it surface later as an unreadable zip.

Python before 3.11 does not follow 308 redirects. GitHub uses 302 for both routes, and a 308 would fail loudly as an HTTP error.

### D5. Read, never extract
The downloaded bytes, or a `--source` file already checked to be a regular file of at most 100 MB, are opened with `zipfile.ZipFile(io.BytesIO(…))`. Every entry name is validated on `ZipInfo.orig_filename`, the stored name, because `filename` has already had a NUL truncation applied and, on Windows, separator rewriting. An entry is refused when its name:
- is absolute;
- contains an empty, `.` or `..` segment (a trailing `/` on a directory entry is allowed);
- contains a backslash, a NUL or a drive letter;
- duplicates another entry's stored name;
- shares its local header with another central-directory record. Python 3.12 and later read such an entry with only an `Overlapped entries` warning, which would print the stored name unescaped; 3.9 reads it silently. `git archive` never writes one.

An entry is also refused when its central-directory extra field, or its local header's, carries an Info-ZIP Unicode Path field (0x7075), found by walking the `<HH` headers as `zipfile` does. `zipfile` reads only the central copy, but streaming readers read the local one. Python 3.12 and later set `filename` from that field after the name as stored has been read, so an entry could pass these checks under one name and be selected under another. `git archive` never writes the field, so refusing it outright costs nothing and gives the same answer on every interpreter. `filename` is then never read: selection, the payload's relative paths and every message use `orig_filename`. A relative path is the stored name minus the one top-level folder, so it is unique because stored names are.

Next, exactly one top-level folder is required. Directory entries are ignored, and an entry counts as a symlink only when `(external_attr >> 16) & 0o170000 == 0o120000`.

Payload entries are selected by the checkout reader's rules:
- `SKILL.md`, `LICENSE`, and files under `references/` and `examples/`;
- skipped when any component is hidden or `__pycache__`, when the file is Windows metadata or bytecode, or when it is a symlink under the two folders;
- refused when `SKILL.md` or `LICENSE` is a symlink.

Payload path components must also be portable: no Unicode control characters (category `Cc`: C0, DEL and C1), no code point the running interpreter's Unicode database leaves unassigned (category `Cn`), none of `< > : " | ? *`, no trailing `.` or space, and no Windows device names. Payload paths are compared under canonical caseless matching (NFD, case fold, NFD again: case folding can un-normalise a string, so NFC-then-casefold misses pairs such as `ΐ` and `Ϊ́` that APFS merges), which refuses both equal paths and file-versus-folder prefix clashes (APFS and NTFS would otherwise merge them). The key can only be as current as the interpreter's Unicode: macOS's `/usr/bin/python3` 3.9 has Unicode 13, and APFS on Darwin 23 merges pairs added later, such as U+A7C0 and U+A7C1. A new case pair always involves a newly assigned character, so refusing unassigned code points makes an older interpreter refuse exactly what it cannot compare.

Payload entries must be stored or deflated. GitHub archives use nothing else, and deflate is the only method `zipfile` decompresses with a bounded output (`max_length`); bzip2 and LZMA decompress a whole compressed chunk at once, so a few kilobytes can expand to gigabytes before the declared size truncates them. The declared uncompressed sizes of payload entries must then total at most 20 MB before anything is decompressed; for stored and deflated entries that sum is a true upper bound, and each entry is read through `ZipFile.open()` in chunks. Any exception at all while listing or reading the archive becomes a named refusal (a `Refusal` raised inside the loop passes through unchanged), and so does any warning `zipfile` raises while reading, which is turned into an exception there, because corrupt archives raise types no fixed list anticipates (`LZMAError`, `OverflowError` for out-of-range zip64 offsets). Archive-derived names are always printed escaped: with `ascii()` in refusals, and in `build`'s payload listing whenever a name is not printable ASCII. Frontmatter values (`name`, `version`, keys) are quoted with `ascii()` in check errors, and an exception's own text in a refusal is escaped the same way, since `zipfile` repeats entry names in it through `%r`. As a last line, everything printed, argparse's usage errors included, passes through one filter that escapes control and format characters (Unicode categories `C*`, `Zl`, `Zp`) while leaving ordinary non-ASCII text such as a user's home path readable, and stdout and stderr are set to `backslashreplace`, so no terminal encoding can turn a refusal into a traceback.

`SKILL.md` bytes are decoded as UTF-8 with universal newlines, exactly as `Path.read_text` does for a checkout. The result is the same `{relative path: bytes}` map a checkout produces, handed to the existing check, `build` and `install` code. That is what gives the spec's "same rules as a checkout run" guarantee.

### D6. The version lives in `SKILL.md`'s `metadata.version`
It is the one place that travels with every folder install, every `.skill` upload and every `.plugin`, so an installed copy can always report its version. `check` requires it to be a semantic version (the semver.org core, no leading zeros, optional dot-separated pre-release and build identifiers). `build` writes it into `plugin.json`, and the `PLUGIN_VERSION` constant goes away. It is written quoted (`version: "0.2.0"`) so no YAML reader takes it for a number.

*Alternatives:* a `VERSION` file (an extra payload file that uploads do not surface), a committed `plugin.json` (absent from folder installs), and the git tag alone (absent from every installed copy).

### D7. A release's version must match its tag, and its name must be ours
The version is compared with the tag after stripping one leading `v` (`tag[1:] if tag.startswith("v")`). This catches the one release mistake that would otherwise ship silently: tagging without bumping. When the tag was resolved as "latest", the resolved tag is the one compared.

A remote payload's frontmatter `name` must also be `okr-ninja` (the `SKILL_NAME` constant), because target folder names come from `name`. Without the check, a `--source` file or a `--repo` fork naming `other-skill` would replace `~/.claude/skills/other-skill`. A fork that renames its skill edits `SKILL_NAME` and `DEFAULT_REPO` in its own `install.py`, which its own raw URL then serves. A checkout run keeps taking the name from its own trusted `SKILL.md`, as today.

### D8. `LICENSE` joins the payload
MIT requires the notice to accompany copies, and every installed folder and `.skill` is a copy that users may pass on. So `LICENSE` ships next to `SKILL.md`, the same pattern Anthropic's published skills use, and a checkout or archive without it is refused. The notice reads `Copyright (c) 2026 Difan Lin`, from the repository's git author name. This is an assumption the owner can edit without touching any requirement.

### D9. Install output reads the previous copy before the swap, defensively
Before `copy_into`, the installer checks `<target>/SKILL.md`. If `os.stat` (following a link) says it is a regular file, the installer reads at most 64 KB of it with universal newlines and extracts `metadata.version` with the same frontmatter reader. Any other file type, any error, or no version gives `unversioned`, and no target at all gives `new install`.

The printed line is `installed okr-ninja 0.3.0 (<n> files) -> <target> (was 0.2.0 | new install | was unversioned)`. A same-version run still replaces the copy: it repairs a damaged install, and "same command updates" should never mean "silently does nothing".

### D10. Remote `build` writes into the current directory
A piped run has no checkout, so the default of `dist/` beside the script has no meaning. The current directory is what a claude.ai or Cowork user expects to find the upload in, and `--out` works as before. It is resolved only when `build` needs it, so `install` and `check` run from a folder that has since been deleted, and `build` there refuses with a message suggesting `--out`.

### D11. Documented forms run isolated and never write into the current folder
Under `python3 -` or `py file.py`, Python puts the current folder first on `sys.path`. A `json.py` or `zipfile.py` there would then shadow the standard library, which the review reproduced on 3.9 and 3.12. Every documented form therefore passes `-I` (isolated mode, available since 3.4). `-I` still honours `HTTPS_PROXY` and `SSL_CERT_FILE`.

The documented forms:
- **macOS / Linux:** `curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py | python3 -I -`, with arguments after the `-`.
- **Windows PowerShell:** `$f = Join-Path $env:TEMP 'okr-ninja-install.py'; curl.exe -fsSLo $f <url>; if ($LASTEXITCODE -eq 0) { py -I $f }`. It writes only into the per-user temp folder, runs only after a successful download, and D1 makes the lone copy remote.
- **Inspect first:** `d=$(mktemp -d) && curl -fsSLo "$d/install.py" <url> && less "$d/install.py"`, then `python3 -I "$d/install.py"`. A fresh private folder, not a private file inside the shared temp root: on Linux `mktemp` without `-d` puts the file in world-writable `/tmp`, where another user could plant a fake checkout beside it (D1 also refuses such folders).
- **Fully pinned:** fetch `install.py` from the tag's raw URL and pass the same `--release`. `--release` alone pins the skill content, not the installer that runs.

`install.py` stays pure ASCII, a property the tests assert, so even a re-encoding pipe cannot corrupt it.

### D12. Certificate failures get a platform-appropriate fix
A TLS verification failure (`ssl.SSLCertVerificationError`, possibly wrapped in `URLError`) is reported with a fix that depends on the platform:
- **macOS**, when `ssl.get_default_verify_paths().openssl_cafile` does not exist (python.org builds before `Install Certificates.command` has been run): run that command.
- **Everywhere else:** point `SSL_CERT_FILE` at the system or corporate CA bundle.

### D13. An offline `unittest` suite in `tests/`, wired into the gate
`tests/test_install.py` imports `install.py` for in-process tests. These cover the detection function, the version rule, name and tag rules, the archive reader over crafted and `git archive`-built zips, the redirect handler, and full `main([...])` runs through the opener seam, where a fake HTTPS handler serves the 302s and zip bytes behind the real redirect handler. The in-process runs cover:
- the latest release moving from v0.2.0 to v0.3.0 between two runs;
- a pinned `--release` with the exact URL sequence asserted;
- a resolved tag whose archive disagrees with it;
- a break mid-download.

It also runs the script as a subprocess in the documented form, `python3 -I - < install.py …`. That covers piped `--source` install and update into a scratch `HOME`, from a scratch folder holding a `json.py` that raises on import. It also covers the two no-option detection cases, with `HTTPS_PROXY` pointed at a closed local port, so a request fails fast and is named in stderr. Finally it covers a remote `build` into a scratch folder.

Test archives come from `git archive --format=zip --prefix=…/` over a temporary repo that commits the working tree's payload, so the suite exercises uncommitted changes in GitHub's real zip shape. A frozen v0.2.0-shaped archive is installed by the current code to guard "main must install every published release". Static checks assert pure ASCII, `ast.parse(..., feature_version=(3, 8))`, and the absence of 3.9+ APIs, because only 3.9 and 3.12 are available to run the suite; 3.8 runtime behaviour itself stays untested.

The suite runs with `python3 -m unittest discover -s tests` and is added to the verify gate's structural checks and CLAUDE.md's testing steps. `.gitignore` gains `__pycache__/`.

*Alternative:* ad-hoc scratch scripts recorded only in tasks, as the previous change did. Rejected because the one-liner always runs `main`'s installer, so a regression there reaches every user immediately.

## Risks / Trade-offs

- [A breaking installer change on `main` reaches every one-liner user before any release] → The committed suite runs in the verify gate. It includes the frozen-release test, and CLAUDE.md's Releasing section names compatibility with every published release as a standing constraint.
- [No real download is tested before the first release exists, and GitHub is blocked in the sandbox] → Everything past the socket is exercised offline, the redirect logic included, through the opener seam and `git archive`-built zips. The release order below smokes the real chain on a pre-release before it becomes "latest".
- [GitHub changes the `/releases/latest` redirect or the codeload host] → The failure is loud (a named URL, exit 1, nothing written), and `--release TAG` keeps working, because the archive route does not use the redirect.
- [Trust: `curl | python3` runs whatever `main` serves] → README offers the inspect-first form and the fully pinned form, and HTTPS host pinning means only GitHub serves the code. `--release` alone pins only the skill content, and README says so.
- [A copy in a shared folder another user filled with a fake checkout] → D1 refuses world-writable folders on POSIX, and the documented forms download into a fresh private folder.
- [A copy downloaded next to an unrelated checkout that has both `SKILL.md` and `README.md` runs in local mode] → It prints the folder it reads. A non-OKR-Ninja checkout still fails the payload reader (no `LICENSE`, `references/` or `examples/`). The documented forms never put the copy in the current folder.
- [The portable-name rule may refuse a future release that adds a file with a `:` or a trailing dot] → Such a file would already break Windows checkouts, so the rule costs nothing a release could legitimately need.

## Migration Plan

1. Merge. `main` then carries `metadata.version: "0.2.0"`, `LICENSE` and the remote-capable installer, and checkout installs keep working unchanged.
2. The owner makes the repo public, since the raw and archive URLs need unauthenticated access, and then creates the release as a pre-release pinned to the merge commit: `gh release create v0.2.0 --target <merge-sha> --prerelease --generate-notes`.
3. Smoke test the pinned chain into one scratch home, twice: `h=$(mktemp -d)`, then run `HOME="$h" sh -c 'curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py | python3 -I - --release v0.2.0'` two times. The first run should report `new install` and the second `was 0.2.0`, for both targets.
4. Promote the release, `gh release edit v0.2.0 --prerelease=false --latest`, then smoke the unpinned one-liner the same way.
5. Every later release follows CLAUDE.md's Releasing section, which repeats steps 2–4.

Rollback: delete the bad release (`gh release delete vX.Y.Z --cleanup-tag`) so "latest" falls back to the previous one. A broken installer on `main` is reverted by an ordinary commit. Existing installs are untouched by either step.
