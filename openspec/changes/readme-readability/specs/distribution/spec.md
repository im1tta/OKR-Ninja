## MODIFIED Requirements

### Requirement: Install routes are documented per platform
README SHALL document installation in two sections. A **Quick start** section SHALL appear before README's usage, product-context, development and roadmap sections. It SHALL lead with the one-command install, which fetches `install.py` from `https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py` and runs it in Python's isolated mode (`-I`) — as every documented command that runs a downloaded `install.py` SHALL, so a module file in the user's current or download folder can never shadow the standard library. It SHALL give a pipe form for macOS and Linux (`curl -fsSL <url> | python3 -I -`) and a Windows PowerShell form that downloads into the user's temporary folder and runs the copy only when the download succeeded. It SHALL state that running the same command again updates the skill, and SHALL give the remote `build` that writes the upload file for Cowork and claude.ai, with the note that an uploaded copy is updated by building and uploading again. A later **Installation reference** section SHALL give: a form that downloads `install.py` into a fresh private temporary folder (never a shared one such as `/tmp` itself) for inspection before running it; the options `--release`, `--only` and `--project`, stating that `--release` pins the skill's content while the installer that runs is whichever copy was fetched, together with a fully pinned form that fetches `install.py` at the same tag; and the clone route (`git clone https://github.com/im1tta/OKR-Ninja.git`, then `python3 install.py`) for developers. It SHALL also state, for Claude Code, Cursor, Codex, Cowork and claude.ai, where that platform looks for skills and which route installs OKR-Ninja there: the one-command install for platforms that read skill folders, the `.skill` written by `build` for Cowork and claude.ai, and the `.plugin` written by the same `build` as an alternative for hosts that install Claude plugins. No documented command SHALL write `install.py` into the user's current folder. README SHALL NOT instruct users to symlink the repo checkout into a skills folder, and SHALL NOT contain a placeholder repository URL.

#### Scenario: Quick start comes first
- **WHEN** a reader opens README
- **THEN** the Quick start section, with the macOS/Linux and Windows one-command installs and the Cowork and claude.ai upload route, appears before README's usage, product-context, development and roadmap sections

#### Scenario: Every listed platform has a route
- **WHEN** a reader looks up any of Claude Code, Cursor, Codex, Cowork or claude.ai in README's Installation reference section
- **THEN** they find where that platform looks for skills and the command or upload that installs OKR-Ninja there, and the `.plugin` route is still offered for plugin hosts

#### Scenario: Updating is documented
- **WHEN** a reader looks for how to update an installed copy
- **THEN** the Quick start section tells them to re-run the install command, and to rebuild and re-upload for Cowork and claude.ai

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
