## MODIFIED Requirements

### Requirement: The runtime payload is the whole shipment
The skill SHALL ship as exactly its runtime payload: `SKILL.md` and `LICENSE` plus every regular file under `references/` and `examples/`, at the same relative paths. Hidden files (names beginning with `.`), Windows folder metadata (`Thumbs.db`, `desktop.ini`) and Python bytecode caches SHALL be excluded. A folder under `references/` or `examples/` that cannot be read SHALL stop the build or the install with a non-zero exit rather than be skipped, and the payload SHALL be read in full before anything is written, so an unreadable file stops the run before any folder is created. No other repo content — `CLAUDE.md`, `README.md`, `install.py`, `tests/`, `evals/`, `openspec/`, `.claude/`, `dist/` — SHALL appear in an installed copy or a built package.

#### Scenario: Development files never ship
- **WHEN** the installer or the build runs from a checkout that also holds `CLAUDE.md`, `README.md`, `tests/`, `evals/`, `openspec/`, `.claude/` and a previous `dist/`
- **THEN** every installed copy and every package contains `SKILL.md`, `LICENSE`, the files under `references/` and the files under `examples/`, and no other file

#### Scenario: OS noise is dropped
- **WHEN** a `.DS_Store` file sits inside `references/` or `examples/`
- **THEN** it appears in no installed copy and in no package

#### Scenario: A checkout without its license refuses
- **WHEN** the installer or the build runs from a checkout whose `LICENSE` is missing
- **THEN** it exits non-zero naming `LICENSE`, and writes no file

### Requirement: The frontmatter check keeps the skill uploadable
`python3 install.py check` SHALL accept only frontmatter written in the one-line subset of YAML that design D2 of the archived `add-cross-platform-install` change defines — one-line plain or quoted values, spaces as the only whitespace, and `metadata` as indented `key: value` lines — and SHALL refuse any other form. For every form it accepts it SHALL apply the constraints that skill uploads enforce, and SHALL additionally require the skill's version. It SHALL print every failure it finds and exit non-zero on any failure (zero when all pass):
- `SKILL.md` is a regular file, not a symlink, and opens with a frontmatter block delimited by `---` lines, written in that subset;
- the block carries no key other than `name`, `description`, `license`, `allowed-tools`, `metadata` and `compatibility`;
- `name` is present, uses only lowercase letters, digits and hyphens, neither starts nor ends with a hyphen, contains no consecutive hyphens, and is at most 64 characters;
- `description` is present, non-empty, at most 1,024 characters, and contains no `<` or `>`;
- `license`, `allowed-tools` and `compatibility`, when present, are one-line strings, `compatibility` at most 500 characters;
- `metadata`, when present, is a map whose keys and values are one-line strings, written as indented `key: value` lines;
- `metadata` is present and holds a `version` whose value is a semantic version: `MAJOR.MINOR.PATCH` in decimal without leading zeros, optionally followed by a `-` pre-release and/or a `+` build suffix of letters, digits, dots and hyphens.

On success `check` SHALL print the skill's name and version. The build and the installer SHALL run the same check first and SHALL change nothing when it fails. The OPSX verify gate's structural checks SHALL include this check exiting 0.

#### Scenario: An over-long description blocks packaging and install
- **WHEN** the frontmatter `description` is longer than 1,024 characters
- **THEN** `check` exits non-zero naming the description's length and the 1,024-character limit, and `build` and `install` exit non-zero without writing any file

#### Scenario: A missing or malformed version fails the check
- **WHEN** the frontmatter has no `metadata.version`, or its value is `0.2`, `v0.2.0` or `01.2.0`
- **THEN** `check` exits non-zero naming `metadata.version`, and `build` and `install` exit non-zero without writing any file

#### Scenario: The shipped skill passes
- **WHEN** `check` runs against the repo's `SKILL.md`
- **THEN** it exits 0 and prints the name `okr-ninja` and the version in `metadata.version`

### Requirement: Built packages for upload and plugin hosts
`python3 install.py build` SHALL write two zip archives — into `dist/` at the repo root when run from a checkout, into the current working directory when run in remote mode, or into the directory given with `--out` (an empty `--out` value is refused) — replacing any previous copies:
- `okr-ninja.skill` — the payload under one top-level folder named after the skill (`okr-ninja/SKILL.md`, `okr-ninja/LICENSE`, `okr-ninja/references/…`, `okr-ninja/examples/…`), the layout claude.ai and Cowork accept as a skill upload;
- `okr-ninja.plugin` — `.claude-plugin/plugin.json` at the archive root and the payload under `skills/okr-ninja/`. The manifest SHALL be valid JSON whose `name` equals the skill's `name`, whose `version` equals `SKILL.md`'s `metadata.version`, and whose `description` is non-empty.

Building twice from an unchanged payload SHALL produce byte-identical archives.

#### Scenario: Skill archive layout
- **WHEN** `build` completes
- **THEN** every entry of `okr-ninja.skill` sits under `okr-ninja/`, and the entries are exactly the payload files

#### Scenario: Plugin archive layout
- **WHEN** `build` completes
- **THEN** `okr-ninja.plugin` holds `.claude-plugin/plugin.json` plus exactly the payload files under `skills/okr-ninja/`, and the manifest parses with `name` `okr-ninja`, `version` equal to `SKILL.md`'s `metadata.version`, and a non-empty `description`

#### Scenario: Rebuilds are reproducible
- **WHEN** `build` runs twice with no change to the payload
- **THEN** each archive is byte-identical across the two runs

### Requirement: Installer targets
`python3 install.py`, or `python3 install.py install`, SHALL place a copy of the payload at `<home>/.claude/skills/okr-ninja/` and at `<home>/.agents/skills/okr-ninja/`, where `<home>` is the current user's home directory, creating missing parent folders. With `--project DIR` it SHALL use `DIR/.claude/skills/okr-ninja/` and `DIR/.agents/skills/okr-ninja/` instead, and SHALL exit non-zero without changing anything when `DIR` is not an existing directory. An empty `--project` value is not an existing directory. `--only claude` SHALL install only the `.claude` target and `--only agents` only the `.agents` target. The installer SHALL print each path it installed together with the version it installed there and what it replaced: the previous copy's `metadata.version`, `new install` when nothing was there, or `unversioned` when the previous copy's `SKILL.md` has no readable version. It SHALL work from a checkout without git metadata, such as a downloaded archive of the repo.

#### Scenario: Default install covers the folder-reading platforms
- **WHEN** a user runs `python3 install.py` with no options
- **THEN** `<home>/.claude/skills/okr-ninja/SKILL.md` and `<home>/.agents/skills/okr-ninja/SKILL.md` both exist, each beside the full payload, and both paths are printed

#### Scenario: Project install
- **WHEN** a user runs `python3 install.py --project DIR` on an existing directory `DIR`
- **THEN** the payload is installed at `DIR/.claude/skills/okr-ninja/` and `DIR/.agents/skills/okr-ninja/`, and nothing under `<home>` changes

#### Scenario: One target only
- **WHEN** a user runs `python3 install.py --only agents`
- **THEN** only `<home>/.agents/skills/okr-ninja/` is written

#### Scenario: Install output reports the version change
- **WHEN** a target holds a copy whose `metadata.version` is `0.2.0` and the installer installs a payload whose version is `0.3.0`, while the other target is empty
- **THEN** the output names `0.3.0` for both targets, `0.2.0` as what the first replaced, and `new install` for the second

#### Scenario: An install from before versioning
- **WHEN** a target holds a copy whose `SKILL.md` has no `metadata.version`
- **THEN** the installer replaces it and reports it replaced an `unversioned` copy

### Requirement: Install routes are documented per platform
README's Installation section SHALL lead with the one-command install, which fetches `install.py` from `https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py` and runs it in Python's isolated mode (`-I`) — as every documented command that runs a downloaded `install.py` SHALL, so a module file in the user's current or download folder can never shadow the standard library: a pipe form for macOS and Linux (`curl -fsSL <url> | python3 -I -`) and a Windows PowerShell form that downloads into the user's temporary folder and runs the copy only when the download succeeded. It SHALL state that running the same command again updates the skill. It SHALL also give: a form that downloads `install.py` into a fresh private temporary folder (never a shared one such as `/tmp` itself) for inspection before running it; the options `--release`, `--only` and `--project`, stating that `--release` pins the skill's content while the installer that runs is whichever copy was fetched, together with a fully pinned form that fetches `install.py` at the same tag; the remote `build` that writes the upload file for Cowork and claude.ai, with the note that an uploaded copy is updated by building and uploading again; and the clone route (`git clone https://github.com/im1tta/OKR-Ninja.git`, then `python3 install.py`) for developers. It SHALL state, for Claude Code, Cursor, Codex, Cowork and claude.ai, where that platform looks for skills and which route installs OKR-Ninja there: the one-command install for platforms that read skill folders, the `.skill` written by `build` for Cowork and claude.ai, and the `.plugin` written by the same `build` as an alternative for hosts that install Claude plugins. No documented command SHALL write `install.py` into the user's current folder. It SHALL NOT instruct users to symlink the repo checkout into a skills folder, and SHALL NOT contain a placeholder repository URL.

#### Scenario: Every listed platform has a route
- **WHEN** a reader looks up any of Claude Code, Cursor, Codex, Cowork or claude.ai in README's Installation section
- **THEN** they find where that platform looks for skills and the command or upload that installs OKR-Ninja there, and the `.plugin` route is still offered for plugin hosts

#### Scenario: Updating is documented
- **WHEN** a reader looks for how to update an installed copy
- **THEN** the Installation section tells them to re-run the install command, and to rebuild and re-upload for Cowork and claude.ai

#### Scenario: Documented commands run isolated and never write into the current folder
- **WHEN** README's one-command install, update, pinned, inspect-first and remote `build` commands are read
- **THEN** every command that runs a downloaded `install.py` passes `-I` to Python, and none writes `install.py` into the current folder

#### Scenario: A fully pinned form is consistent
- **WHEN** README shows the fully pinned form
- **THEN** the tag in its `raw.githubusercontent.com` URL equals its `--release` value

#### Scenario: No checkout symlink instruction
- **WHEN** README is searched for an instruction to symlink the checkout into a skills folder
- **THEN** there is none

#### Scenario: No placeholder URL
- **WHEN** README is searched for `your-org`
- **THEN** there is no match, and every clone or download URL names `im1tta/OKR-Ninja`

## ADDED Requirements

### Requirement: Remote install from a published release
`install.py` SHALL read the payload from its own checkout only when all of these hold: it runs from a file on disk (not from standard input, `python3 -c` or any other source whose file name starts with `<`), that file's folder holds both `SKILL.md` and `README.md` (a checkout or a downloaded archive of the repo, as opposed to an installed copy or an unpacked `.skill`, which carry no `README.md`), that folder is not writable by other users (on POSIX, not world-writable, so a shared folder such as `/tmp` never counts), and none of `--release`, `--repo` or `--source` is given. In every other case it SHALL run in remote mode. A checkout run SHALL print the checkout folder it reads and make no network request. In remote mode it SHALL:
- take the repository from `--repo OWNER/NAME`, defaulting to `im1tta/OKR-Ninja`, and refuse before any request a value whose `OWNER` is not 1 to 39 letters, digits and hyphens starting with a letter or digit, or whose `NAME` is not 1 to 100 letters, digits, `.`, `_` and `-`, or is `.` or `..`;
- take the release from `--release TAG`; an absent `--release` or the value `latest` means the repository's latest published release (GitHub never reports a draft or a pre-release as the latest), and when there is none the installer SHALL exit non-zero naming the repository; any other value SHALL be refused before any request unless it consists only of letters, digits, `.`, `_`, `+` and `-` and is not `.` or `..`;
- download that tag's source archive as a zip, where every request and every redirect uses `https` and a host that is `github.com` or `codeload.github.com`; a request or redirect with any other scheme or host SHALL stop the run before anything is written;
- with `--source PATH`, read that local file instead and make no network request; the file SHALL be a regular file of at most 100 MB, and `--source` together with `--release latest` SHALL be refused, naming both options;
- refuse, writing nothing, a payload whose frontmatter `name` is not `okr-ninja`, so an archive can never choose which skills folder is replaced;
- print the repository and tag, or the local archive path, and the version it is about to use;
- then run the requested command — `install` (the default), `build` or `check` — on the archive's payload with the same frontmatter check, targets, options and replacement-safety rules as a run from a checkout. Whenever the installer runs from a file on disk, in either mode, the folder holding that file counts as the checkout for the rule that refuses a target which is, or contains, the checkout.

A network, TLS or HTTP failure, including a connection that breaks during a download or a response that ends before its declared `Content-Length`, SHALL exit non-zero with a message naming the URL and the cause, and SHALL write nothing; a certificate-verification failure SHALL also say how to make the missing CA certificates available on that platform.

#### Scenario: The same command installs and updates
- **WHEN** a user runs the one-command install into an empty home, the repository then publishes a newer release, and the user runs the same command again
- **THEN** the first run installs the first release's payload, the second replaces it with the newer payload, and the second run reports the old and the new version

#### Scenario: A pinned release
- **WHEN** a user runs the installer in remote mode with `--release v0.2.0` while a newer release exists
- **THEN** the payload of tag `v0.2.0` is installed, and the latest-release address is never requested

#### Scenario: No published release
- **WHEN** the repository has no published release and no `--release` is given
- **THEN** the installer exits non-zero naming the repository, and writes nothing

#### Scenario: A redirect away from GitHub is refused
- **WHEN** a download is redirected to a host other than `github.com` or `codeload.github.com`, or to an `http` URL
- **THEN** the installer exits non-zero naming the refused URL, and writes nothing

#### Scenario: Unsafe repository or tag values are refused before any request
- **WHEN** the installer runs with `--repo ../x`, `--repo a/b/c` or `--release 'v1/../x'`
- **THEN** it exits non-zero naming the value, makes no request, and writes nothing

#### Scenario: A local archive needs no network
- **WHEN** the installer runs with `--source` pointing at a zip of the repo
- **THEN** it makes no network request and installs that archive's payload

#### Scenario: An archive naming another skill is refused
- **WHEN** a `--source` archive's `SKILL.md` has `name: other-skill` and `<home>/.claude/skills/other-skill` exists
- **THEN** the installer exits non-zero naming `other-skill`, and that folder is unchanged

#### Scenario: A checkout run stays local
- **WHEN** the installer runs from a checkout that holds `SKILL.md` and `README.md` and none of `--release`, `--repo` or `--source` is given
- **THEN** it prints the checkout folder, installs the checkout's payload and makes no network request

#### Scenario: A piped run inside a checkout is remote
- **WHEN** `install.py` is piped into `python3 -I -` with a checkout as the current folder and no options
- **THEN** it reads nothing from that checkout and requests the latest-release address of `im1tta/OKR-Ninja`

#### Scenario: A checkout in a world-writable folder is never read
- **WHEN** a copy of `install.py` runs from a world-writable folder (such as Linux's `/tmp`) that another user has filled with `SKILL.md`, `README.md`, `LICENSE`, `references/` and `examples/`
- **THEN** it runs in remote mode, and nothing from that folder is installed

#### Scenario: A copy beside an installed skill is remote
- **WHEN** a lone `install.py` sits in a folder that holds an installed copy or an unpacked `.skill` (`SKILL.md`, `LICENSE`, `references/`, `examples/`, no `README.md`)
- **THEN** it runs in remote mode and does not install that folder's payload

#### Scenario: Remote build for upload platforms
- **WHEN** a user runs the installer in remote mode with the `build` command and no `--out`
- **THEN** `okr-ninja.skill` and `okr-ninja.plugin` built from the release's payload are written into the current working directory

#### Scenario: A deleted current folder
- **WHEN** a remote run starts in a current folder that no longer exists
- **THEN** `install` and `check` still complete, and `build` without `--out` exits non-zero saying the current folder no longer exists and suggesting `--out`, writing nothing

### Requirement: Release archives are read, never extracted
In remote mode the installer SHALL read the payload from the archive into memory and SHALL NOT extract the archive to disk; the only files it writes are those its command writes from a checkout. The archive SHALL hold exactly one top-level folder. Directory entries (names ending in `/`) SHALL be ignored, and an entry is a symbolic link only when its Unix mode says so; any other entry is a regular file. The payload SHALL be that folder's `SKILL.md` and `LICENSE` plus the files under its `references/` and `examples/`, filtered as a checkout's payload is (in both readers): an entry is skipped when any component of its path, the file name included, is hidden (starts with `.`) or is `__pycache__`, when it is Windows folder metadata or Python bytecode, or when it is a symbolic link under `references/` or `examples/`. Entries outside the payload SHALL be ignored. `SKILL.md` text from an archive SHALL be read with the same newline handling as a checkout's, so CRLF line ends pass the check. Archive-derived names and frontmatter values SHALL be printed in escaped form wherever the installer prints them, including `build`'s payload listing and `check`'s errors; no output the installer prints SHALL carry a raw control or format character (such as U+202E), and output SHALL never fail because the terminal cannot encode a character. The installer SHALL exit non-zero, naming the problem and writing nothing, when:
- the file is not a readable zip, or does not hold exactly one top-level folder, or any error of any kind occurs while listing or reading it, including an encrypted entry, a failed checksum, a truncated file or an out-of-range offset;
- a payload entry is compressed with any method other than stored or deflate (the only methods a GitHub archive uses, and the only ones whose decompression the installer can bound);
- any entry's name as stored is absolute, contains an empty, `.` or `..` segment (other than the trailing `/` of a directory entry), a backslash, a NUL character or a drive letter;
- two entries share a name, or two central-directory records point at one local header (Python 3.12 and later read such an entry with only a warning; a GitHub archive never has one);
- any entry carries an Info-ZIP Unicode Path extra field (0x7075), in its central-directory record or its local header, which some zip readers, Python 3.12 and later among them, use in place of the name as stored; a GitHub archive never carries one, and every check and every written path uses the name as stored;
- any payload path component contains a Unicode control character (C0, DEL or C1, U+0080 to U+009F), a code point the running Python's Unicode database does not assign (its case folding is unknown there, so a case pair a newer file system merges would go unseen), or one of `< > : " | ? *`, ends in `.` or a space, or is a Windows reserved device name (`CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`, with or without an extension, in any letter case);
- two payload paths are equal under canonical caseless matching (Unicode NFD, case folding, NFD again), or one payload file's path so compared equals a folder on another payload file's path;
- `SKILL.md` or `LICENSE` is missing or is a symbolic link, or `references/` or `examples/` holds no payload file;
- the downloaded archive exceeds 100 MB, or the payload entries' declared uncompressed sizes add up to more than 20 MB (checked before any entry is decompressed).

#### Scenario: Only the payload is taken from a release
- **WHEN** a release archive also holds `CLAUDE.md`, `README.md`, `install.py`, `tests/`, `evals/`, `openspec/`, `.claude/` and `references/.cache/x.md`
- **THEN** every installed copy and package contains exactly `SKILL.md`, `LICENSE` and the non-hidden files under `references/` and `examples/`

#### Scenario: An archive shaped like GitHub's is read
- **WHEN** the archive is produced by `git archive --format=zip --prefix=OKR-Ninja-0.2.0/` from a commit of the repo, with its directory entries, zip comment and a symbolic link under `references/`
- **THEN** the payload read from it equals the payload read from that commit's checkout

#### Scenario: A traversal entry is refused
- **WHEN** an archive holds an entry named `OKR-Ninja-0.2.0/references/../../escape.md` or `/etc/passwd`
- **THEN** the installer exits non-zero naming the entry, and writes nothing

#### Scenario: Colliding payload paths are refused
- **WHEN** an archive's top-level folder holds both `references/Rubric.md` and `references/rubric.md`, or both `references/a` and `references/a/b.md`, or `references/./x.md`
- **THEN** the installer exits non-zero naming the entries, and writes nothing

#### Scenario: Unsafe payload names are refused
- **WHEN** a payload entry's name contains an escape character, a DEL, a C1 control such as U+009B, a `:`, a trailing `.`, or is `references/NUL.md`
- **THEN** the installer exits non-zero naming it in escaped form, and writes nothing

#### Scenario: Two records for one entry's data are refused
- **WHEN** a second central-directory record, named inside the payload or outside it, points at the local header of a payload entry
- **THEN** the installer exits non-zero naming both entries in escaped form, on every supported Python version, prints no Python warning, and writes nothing

#### Scenario: An entry that renames itself is refused
- **WHEN** any entry, inside the payload or not, carries a Unicode Path extra field (0x7075) that Python can parse, whatever name it gives
- **THEN** the installer exits non-zero naming the entry as stored, on every supported Python version, and writes nothing
- **AND** a 0x7075 field that Python 3.12 or later cannot parse makes the archive unreadable there, which is refused as such, and nothing is written

#### Scenario: A symlinked SKILL.md is refused
- **WHEN** the archive's `SKILL.md` entry is a symbolic link
- **THEN** the installer exits non-zero naming it, and writes nothing

#### Scenario: A decompression bomb is refused before it is decompressed
- **WHEN** a payload entry declares an uncompressed size above 20 MB, or is compressed with bzip2 or LZMA, or an archive's content is corrupt or truncated
- **THEN** the installer exits non-zero with a named refusal rather than a traceback, and writes nothing

### Requirement: A release's version agrees with its tag
When the payload comes from a release tag, the archive's `SKILL.md` `metadata.version` SHALL equal the tag with at most one leading `v` removed; otherwise the run SHALL exit non-zero naming both values and write nothing. With `--source` and no `--release`, no tag comparison is made; with `--source` and `--release TAG`, the version SHALL be compared against `TAG`. When the tag was resolved as the latest release, the comparison SHALL use that resolved tag.

#### Scenario: A mismatched release is refused
- **WHEN** tag `v0.3.0`'s archive carries `metadata.version` `0.2.0`
- **THEN** the installer exits non-zero naming `v0.3.0` and `0.2.0`, and writes nothing

#### Scenario: A matching release is accepted
- **WHEN** tag `v0.2.0`'s archive carries `metadata.version` `0.2.0`
- **THEN** the run proceeds with the requested command

### Requirement: The installer is tested offline on every change
The repo SHALL carry a standard-library test suite for `install.py` that runs without network access, in which every scenario of this capability that concerns the installer maps to at least one test, and the OPSX verify gate's structural checks SHALL include that suite passing. The suite SHALL include a check that `install.py` parses under Python 3.8's grammar and uses no standard-library API newer than 3.8, and that `install.py` is pure ASCII.

#### Scenario: The gate runs the suite
- **WHEN** the verify gate's structural checks run
- **THEN** they include the installer test suite, and a failing test turns the gate red
