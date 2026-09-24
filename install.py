#!/usr/bin/env python3
"""Install, package or check the OKR-Ninja skill (Python 3.8+ standard library only).

Commands
  install   (default) copy the skill into ~/.claude/skills/<name> (Claude Code; Cursor reads it
            too) and ~/.agents/skills/<name> (Codex, Cursor and other .agents-standard tools)
              --project DIR       install into DIR/.claude/skills and DIR/.agents/skills instead
              --only claude|agents  install one of the two targets
  build     write dist/<name>.skill (the skill upload for claude.ai and Cowork) and
            dist/<name>.plugin (a Claude plugin); --out DIR writes elsewhere
  check     validate SKILL.md's frontmatter against the rules skill uploads enforce

Only the runtime payload ships: SKILL.md plus the files under references/ and examples/.

Design: openspec/changes/add-cross-platform-install/design.md
Contract: openspec/changes/add-cross-platform-install/specs/distribution/spec.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
PAYLOAD_DIRS = ("references", "examples")
PLUGIN_VERSION = "0.1.0"
COMMANDS = ("install", "build", "check")

# Limits and keys enforced by skill uploads (the Agent Skills spec, as skill-creator's
# quick_validate.py implements it).
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
NAME_MAX = 64
DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500
OS_NOISE = {"thumbs.db", "desktop.ini"}  # Windows folder metadata, compared lowercased

ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644 << 16

# Plain YAML scalars that PyYAML's implicit resolvers (YAML 1.1, as skill uploads parse them)
# read as something other than a string: bool, float, int, merge, null, timestamp, value.
YAML_NON_STRING = re.compile(
    r"^(?:yes|Yes|YES|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF"
    r"|[-+]?(?:[0-9][0-9_]*)\.[0-9_]*(?:[eE][-+][0-9]+)?|\.[0-9_]+(?:[eE][-+][0-9]+)?"
    r"|[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\.[0-9_]*|[-+]?\.(?:inf|Inf|INF)|\.(?:nan|NaN|NAN)"
    r"|[-+]?0b[0-1_]+|[-+]?0[0-7_]+|[-+]?(?:0|[1-9][0-9_]*)|[-+]?0x[0-9a-fA-F_]+"
    r"|[-+]?[1-9][0-9_]*(?::[0-5]?[0-9])+"
    r"|<<|~|null|Null|NULL|="
    r"|[0-9]{4}-[0-9]{2}-[0-9]{2}"
    r"|[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}(?:[Tt]|[ \t]+)[0-9]{1,2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]*)?"
    r"(?:[ \t]*(?:Z|[-+][0-9]{1,2}(?::[0-9]{2})?))?)$"
)

YAML_LINE_BREAKS = (0x85, 0x2028, 0x2029)  # YAML reads these as line ends inside a value


class Refusal(Exception):
    """A problem the user must fix; printed without a traceback, exit status 1."""


# ---------------------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------------------

def yaml_printable(ch):
    """True for characters PyYAML's reader accepts; it rejects everything else."""
    o = ord(ch)
    return (o in (0x09, 0x0A, 0x0D, 0x85) or 0x20 <= o <= 0x7E or 0xA0 <= o <= 0xD7FF
            or 0xE000 <= o <= 0xFFFD or 0x10000 <= o <= 0x10FFFF)


def read_frontmatter(text):
    """Return (fields, errors). fields maps each top-level key to
    {"raw", "line", "continued", "children"}, children being the (line number, text) of the
    indented or list lines below the key.

    Strict by design (D2): it reads the one-line subset of YAML that skill frontmatter uses,
    the way an upload's validator and YAML parser read it, and refuses what it cannot
    classify rather than guessing. It is not a YAML parser.
    """
    if text.startswith(chr(0xFEFF)):
        return {}, ["SKILL.md starts with a byte-order mark; uploads expect it to open with '---'"]
    lines = text.split("\n")
    if lines[0] != "---":
        return {}, ["SKILL.md must open with a frontmatter block: a first line '---'"]
    # The validator's `^---\n(.*?)\n---` cannot close on the line right after the opener, and
    # a second '---' there is YAML's own document-start marker.
    close = next((i for i in range(2, len(lines)) if lines[i].startswith("---")), None)
    if close is None:
        return {}, ["the frontmatter block is not closed by a line '---'"]
    start = 2 if lines[1] == "---" else 1

    fields, errors, current = {}, [], None
    for n, line in enumerate(lines[start:close], start=start + 1):
        odd = sorted({f"U+{ord(c):04X}" for c in line
                      if not yaml_printable(c) or ord(c) in YAML_LINE_BREAKS})
        if odd:
            errors.append(f"line {n}: contains control or line-break characters YAML cannot read "
                          f"in a one-line value ({', '.join(odd)})")
            continue
        if "\t" in line:
            errors.append(f"line {n}: contains a tab; write the frontmatter with spaces only")
            continue
        # YAML's whitespace here is the space alone (tabs are refused above); Python's strip()
        # would also drop no-break and other Unicode spaces that YAML keeps.
        if not line.strip(" ") or line.lstrip(" ").startswith("#"):
            continue
        if line[0] == " " or line.startswith("- "):
            if current is None:
                errors.append(f"line {n}: indented text before any key")
            else:
                fields[current]["continued"] = True
                fields[current]["children"].append((n, line))
            continue
        m = re.match(r"^([^\s:#][^:]*):(?: +(.*))?$", line)
        if not m:
            errors.append(f"line {n}: expected 'key: value'")
            current = None
            continue
        key = m.group(1)
        if key in fields:
            errors.append(f"line {n}: duplicate key '{key}'")
        fields[key] = {"raw": (m.group(2) or "").rstrip(" "), "line": n, "continued": False,
                       "children": []}
        current = key
    return fields, errors


def scalar(field, key, comments_allowed=False):
    """Return (value, error) for a one-line scalar field."""
    raw, where = field["raw"], f"line {field['line']}"
    if field["continued"]:
        if raw:
            return None, f"{where}: '{key}' has a value on its line and indented lines below it"
        return None, f"{where}: '{key}' must be written on one line"
    if comments_allowed and raw[:1] not in ("'", '"') and " #" in raw:
        raw = raw[:raw.index(" #")].rstrip(" ")  # YAML drops a trailing comment
    if not raw:
        return None, f"{where}: '{key}' is empty"
    if raw[0] in "|>":
        return None, f"{where}: '{key}' uses a block scalar; write it on one line"
    if raw[0] == "'":
        inner = raw[1:-1] if len(raw) > 1 and raw.endswith("'") else None
        if inner is None or "'" in inner.replace("''", ""):
            return None, f"{where}: '{key}' has an unbalanced single quote"
        return inner.replace("''", "'"), None
    if raw[0] == '"':
        inner = raw[1:-1] if len(raw) > 1 and raw.endswith('"') else None
        if inner is None or '"' in inner:
            return None, f"{where}: '{key}' has an unbalanced double quote"
        if "\\" in inner:
            return None, f"{where}: '{key}' uses a backslash escape; use a plain or single-quoted value"
        return inner, None
    if raw[0] in ",[]{}#&*!%@`" or (raw[0] in "-?:" and (len(raw) == 1 or raw[1] == " ")):
        return None, f"{where}: '{key}' starts with a YAML indicator ({raw[0]!r}); quote the value"
    if ": " in raw or raw.endswith(":"):
        return None, f"{where}: '{key}' contains ': ', which YAML reads as a mapping; rephrase or quote it"
    if " #" in raw:
        return None, f"{where}: '{key}' contains ' #', which YAML reads as a comment; rephrase or quote it"
    if YAML_NON_STRING.match(raw):
        return None, f"{where}: YAML reads '{key}' as a non-string ({raw}); quote it"
    return raw, None


def check_metadata(field):
    """`metadata` is a map of string keys to string values (Agent Skills spec): accept only
    indented `key: value` lines at one indentation, each key and value a one-line string."""
    where = f"line {field['line']}"
    if field["raw"]:
        if field["continued"]:
            return [f"{where}: 'metadata' has a value on its line and indented lines below it"]
        return [f"{where}: 'metadata' must be a map: indented 'key: value' lines below it"]
    errors, indent = [], None
    for n, line in field["children"]:
        m = re.match(r"^( +)([^ ][^:]*):(?: +(.*))?$", line)
        if not m:
            errors.append(f"line {n}: 'metadata' holds only indented 'key: value' lines")
            continue
        if indent is None:
            indent = m.group(1)
        elif m.group(1) != indent:
            errors.append(f"line {n}: 'metadata' entries must share one indentation")
            continue
        key = {"raw": m.group(2), "line": n, "continued": False}
        _, error = scalar(key, f"metadata key {m.group(2)!r}")
        if error:
            errors.append(error)
            continue
        entry = {"raw": (m.group(3) or "").rstrip(" "), "line": n, "continued": False}
        _, error = scalar(entry, f"metadata.{m.group(2)}", comments_allowed=True)
        if error:
            errors.append(error)
    return errors


def check_skill(root=ROOT):
    """Validate SKILL.md's frontmatter. Returns (name, description, errors)."""
    path = root / "SKILL.md"
    if path.is_symlink():
        return None, None, [f"{path} is a symlink; the payload is never read through symlinks"]
    try:
        # Universal newlines, exactly as the upload validator reads it: CRLF files pass.
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return None, None, [f"cannot read {path}: {e}"]
    fields, errors = read_frontmatter(text)
    if not fields and errors:
        return None, None, errors
    extra = sorted(set(fields) - ALLOWED_KEYS)
    if extra:
        errors.append(f"unexpected frontmatter key(s): {', '.join(extra)} "
                      f"(allowed: {', '.join(sorted(ALLOWED_KEYS))})")
    for key, field in fields.items():
        if key in ("name", "description") or key not in ALLOWED_KEYS:
            continue
        if key == "metadata":
            errors.extend(check_metadata(field))
            continue
        if not field["raw"] and not field["continued"]:
            continue  # an empty value reads as null, which the validator accepts for these keys
        value, error = scalar(field, key, comments_allowed=True)
        if error:
            errors.append(error)
        elif key == "compatibility" and len(value) > COMPATIBILITY_MAX:
            errors.append(f"compatibility is {len(value):,} characters; the limit is {COMPATIBILITY_MAX}")

    name = description = None
    for key in ("name", "description"):
        if key not in fields:
            errors.append(f"missing '{key}' in the frontmatter")
            continue
        value, error = scalar(fields[key], key)
        if error:
            errors.append(error)
        elif key == "name":
            name = value.strip()
        else:
            description = value.strip()

    if name is not None:
        if not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"name '{name}' must use only lowercase letters, digits and hyphens")
        elif name.startswith("-") or name.endswith("-") or "--" in name:
            errors.append(f"name '{name}' cannot start or end with a hyphen or contain '--'")
        if len(name) > NAME_MAX:
            errors.append(f"name is {len(name)} characters; the limit is {NAME_MAX}")
    if description is not None:
        if not description:
            errors.append("description is empty")
        if "<" in description or ">" in description:
            errors.append("description contains an angle bracket (< or >), which uploads reject")
        if len(description) > DESCRIPTION_MAX:
            errors.append(f"description is {len(description):,} characters; "
                          f"the limit is {DESCRIPTION_MAX:,}")
    return name, description, errors


def checked_skill(root=ROOT):
    """Run the check; raise Refusal listing every failure, else return (name, description)."""
    name, description, errors = check_skill(root)
    if errors:
        raise Refusal("SKILL.md fails the upload check:\n" + "\n".join(f"  - {e}" for e in errors))
    return name, description


# ---------------------------------------------------------------------------------------
# Payload
# ---------------------------------------------------------------------------------------

def payload_files(root=ROOT):
    """The runtime payload as sorted POSIX-relative paths: SKILL.md, references/, examples/.

    Regular files only; hidden names, __pycache__, *.pyc and Windows folder metadata are
    skipped, symlinks are never followed (so nothing outside the checkout can ship), and an
    unreadable folder stops the run instead of being skipped (design D3).
    """
    skill_md = root / "SKILL.md"
    if skill_md.is_symlink() or not skill_md.is_file():
        raise Refusal(f"{skill_md} must be a regular file; the payload is never read through symlinks")

    def unreadable(err):
        raise Refusal(f"cannot read {err.filename}: {err.strerror}; nothing was built or installed")

    files = ["SKILL.md"]
    for top in PAYLOAD_DIRS:
        base = root / top
        if base.is_symlink():
            raise Refusal(f"{top}/ is a symlink; the payload is never read through symlinks")
        if not base.is_dir():
            raise Refusal(f"{top}/ is missing from {root}; is this an OKR-Ninja checkout?")
        for dirpath, dirnames, filenames in os.walk(base, onerror=unreadable):
            here = Path(dirpath)
            dirnames[:] = sorted(d for d in dirnames
                                 if not d.startswith(".") and d != "__pycache__"
                                 and not (here / d).is_symlink())
            for f in sorted(filenames):
                p = here / f
                if (f.startswith(".") or f.lower() in OS_NOISE or f.endswith(".pyc")
                        or p.is_symlink() or not p.is_file()):
                    continue
                files.append(p.relative_to(root).as_posix())
    return sorted(files)


def read_payload(root=ROOT):
    """Read the whole payload before anything is written, so an unreadable file stops the
    run before a folder is created (design D3). Returns {relative path: bytes}."""
    data = {}
    for f in payload_files(root):
        try:
            data[f] = (root / PurePosixPath(f)).read_bytes()
        except OSError as e:
            raise Refusal(f"cannot read {root / PurePosixPath(f)}: {e.strerror or e}; "
                          f"nothing was built or installed")
    return data


def current_umask():
    umask = os.umask(0)
    os.umask(umask)
    return umask


# ---------------------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------------------

def write_zip(dest, entries):
    """Write a reproducible zip (sorted entries, fixed timestamps and modes) via a temp file."""
    fd, tmp = tempfile.mkstemp(prefix=f".{dest.name}.", suffix=".tmp", dir=dest.parent)
    os.close(fd)
    try:
        with zipfile.ZipFile(tmp, "w") as zf:
            for arcname, data in sorted(entries):
                info = zipfile.ZipInfo(arcname, date_time=ZIP_EPOCH)
                info.create_system = 3
                info.external_attr = FILE_MODE
                zf.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        os.chmod(tmp, 0o666 & ~current_umask())  # mkstemp creates 0600; a package is an ordinary file
        os.replace(tmp, dest)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def first_sentence(text):
    head = text.split(". ", 1)[0].rstrip(".")
    return head + "."


def cmd_build(args):
    name, description = checked_skill()
    data = read_payload()
    if args.out is not None and not args.out:
        raise Refusal("--out '': not a directory; nothing was built")
    out = Path(args.out).expanduser() if args.out is not None else ROOT / "dist"
    if out.exists() and not out.is_dir():
        raise Refusal(f"--out {out}: exists and is not a directory")
    out.mkdir(parents=True, exist_ok=True)

    skill = out / f"{name}.skill"
    write_zip(skill, [(f"{name}/{f}", b) for f, b in data.items()])

    manifest = {"name": name, "version": PLUGIN_VERSION, "description": first_sentence(description)}
    plugin = out / f"{name}.plugin"
    write_zip(plugin, [(".claude-plugin/plugin.json",
                        (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))]
              + [(f"skills/{name}/{f}", b) for f, b in data.items()])

    print(f"payload ({len(data)} files):")
    for f in data:
        print(f"  {f}")
    print(f"wrote {skill}  (upload under Skills in claude.ai settings; Cowork uses the same account skills)")
    print(f"wrote {plugin}  (Claude plugin, version {PLUGIN_VERSION})")
    return 0


# ---------------------------------------------------------------------------------------
# install
# ---------------------------------------------------------------------------------------

def is_junction(path):
    """A Windows directory junction, which is a link to be unlinked, never deleted through."""
    if hasattr(os.path, "isjunction"):  # Python 3.12+
        return os.path.isjunction(path)
    if os.name != "nt":
        return False
    try:
        st = os.lstat(path)
    except OSError:
        return False
    return (bool(getattr(st, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT)
            and getattr(st, "st_reparse_tag", None) == stat.IO_REPARSE_TAG_MOUNT_POINT)


def is_link(path):
    return path.is_symlink() or is_junction(path)


def same_file(a, b):
    try:
        return os.path.samefile(a, b)
    except OSError:
        return False


def holds_git(target):
    """Whether target holds .git. A previous copy its owner cannot list is opened up just long
    enough to look (POSIX), and its mode is put back, so a refusal still changes nothing."""
    try:
        return (target / ".git").exists() or (target / ".git").is_symlink()
    except PermissionError:
        if os.name == "nt":
            raise
    mode = stat.S_IMODE(target.stat().st_mode)
    os.chmod(target, mode | stat.S_IRUSR | stat.S_IXUSR)
    try:
        return (target / ".git").exists() or (target / ".git").is_symlink()
    finally:
        os.chmod(target, mode)


def refuse_target(target, source):
    """Return why target cannot be replaced safely, or None (spec: Replacing an existing install is safe)."""
    if is_link(target):
        return None  # only the link itself is moved and removed; whatever it points to is left alone
    if target.exists():
        if not target.is_dir():
            return f"{target} exists and is not a directory or a symlink"
        # File-system identity, never path strings: on a case-insensitive disk ".../OKR-Ninja"
        # and ".../okr-ninja" are one directory while comparing unequal (design D6).
        if any(same_file(target, p) for p in (source, *source.parents)):
            return (f"{target} is the checkout this installer runs from, or contains it; "
                    f"replacing it would delete the source. Run install.py from another checkout, "
                    f"or skip that target with --only")
        try:
            clone = holds_git(target)
        except OSError as e:
            return f"cannot look inside {target} to check it is not a repository clone: {e.strerror or e}"
        if clone:
            return (f"{target} holds .git, so it is a repository clone, not an installed copy; "
                    f"move it out of the skills folder, then re-run")
        return None
    for parent in target.parents:
        if parent.exists() or parent.is_symlink():
            if not parent.is_dir():
                return f"{parent} is not a directory, so {target} cannot be created"
            return None
    return None


def remove_tree(root, _active=None, _top=None):
    """Delete a folder this installer owns (a moved-aside previous copy), design D6.

    Only deleting calls are retried. On POSIX only folders inside the top folder are made
    writable, never a file, so a file hard-linked from elsewhere keeps its mode; on Windows
    the read-only attribute of the path being deleted is cleared. A folder that cannot be
    listed is made listable and deleted whole; anything else is re-raised.
    """
    root = os.path.abspath(root)
    top = root if _top is None else _top
    if _top is None and os.name != "nt" and not os.path.islink(root):
        os.chmod(root, stat.S_IRWXU)  # this run's own moved-aside copy: it may be unlistable
    active = set() if _active is None else _active  # folders being deleted whole, never re-entered
    active.add(root)

    def retry(func, path, excinfo):
        err = excinfo[1] if isinstance(excinfo, tuple) else excinfo
        try:
            os.lstat(path)
        except FileNotFoundError:
            return  # already deleted, e.g. as part of a folder deleted whole below
        except OSError:
            pass  # cannot even stat it: let the handling below decide
        if func in (os.unlink, os.remove, os.rmdir):
            if os.name == "nt":
                if os.chmod in os.supports_follow_symlinks:
                    os.chmod(path, stat.S_IWRITE, follow_symlinks=False)
                else:
                    os.chmod(path, stat.S_IWRITE)
            elif os.path.abspath(path) != top:
                os.chmod(os.path.dirname(path), stat.S_IRWXU)
            else:
                raise err
            func(path)
        elif (os.path.isdir(path) and not os.path.islink(path)
              and os.path.abspath(path) not in active):
            # A folder that could not be listed. Python 3.12+ also lands here, reporting
            # os.scandir, when a deletion inside the folder failed; the active set turns that
            # into a re-raise instead of endless recursion.
            os.chmod(path, stat.S_IRWXU)
            remove_tree(path, active, top)
        else:
            raise err

    if sys.version_info >= (3, 12):
        shutil.rmtree(root, onexc=retry)
    else:
        shutil.rmtree(root, onerror=retry)


def remove_aside(aside):
    """Delete the previous copy this run moved aside: a link is removed itself, a folder whole."""
    if is_junction(aside):
        os.rmdir(aside)  # removes the junction, never what it points to
    elif aside.is_symlink():
        aside.unlink()
    else:
        remove_tree(aside)


def copy_into(target, data):
    """Install data ({relative path: bytes}) at target via a staging copy and a two-rename swap
    (design D6). Returns a warning naming a previous copy that could not be deleted, else None."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}.", suffix=".staging", dir=target.parent))
    aside = old_mode = None
    try:
        os.chmod(staging, 0o777 & ~current_umask())  # mkdtemp creates 0700
        for f, b in data.items():
            dst = staging / PurePosixPath(f)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(b)
        if is_link(target) or target.exists():
            if not is_link(target) and os.name != "nt":
                mode = stat.S_IMODE(target.stat().st_mode)
                if not mode & stat.S_IWUSR:  # macOS will not move a folder its owner cannot write
                    os.chmod(target, mode | stat.S_IWUSR)
                    old_mode = mode
            aside = Path(tempfile.mkdtemp(prefix=f".{target.name}.", suffix=".previous", dir=target.parent))
            aside.rmdir()  # reserve a unique name, then move the previous copy (or link) onto it
            os.rename(target, aside)
        os.rename(staging, target)
    except BaseException as exc:
        shutil.rmtree(staging, ignore_errors=True)
        if aside is not None and not os.path.lexists(target) and os.path.lexists(aside):
            try:
                os.rename(aside, target)  # put the previous copy or link back
            except OSError:
                raise OSError(f"{exc}; the previous copy was left at {aside}") from exc
        if old_mode is not None and os.path.lexists(target) and not is_link(target):
            try:
                os.chmod(target, old_mode)
            except OSError:
                pass
        raise
    if aside is not None:
        try:
            remove_aside(aside)
        except OSError as e:
            return (f"the new copy is installed, but the previous copy could not be deleted; "
                    f"delete it yourself: {aside} ({e.strerror or e})")
    return None


def cmd_install(args):
    name, _ = checked_skill()
    data = read_payload()
    if args.project is not None:
        project = os.path.expanduser(args.project)
        if not os.path.isdir(project):  # os.path.isdir("") is False, unlike Path("").is_dir()
            raise Refusal(f"--project {args.project!r}: not an existing directory; nothing was installed")
        base = Path(project)
    else:
        base = Path.home()
    kinds = [args.only] if args.only else ["claude", "agents"]
    targets = [base / f".{kind}" / "skills" / name for kind in kinds]

    problems = [p for p in (refuse_target(t, ROOT) for t in targets) if p]
    if problems:
        raise Refusal("nothing was installed:\n" + "\n".join(f"  - {p}" for p in problems))
    done, warnings = [], []
    for t in targets:
        try:
            warning = copy_into(t, data)
        except OSError as e:
            already = ", ".join(map(str, done)) if done else "none"
            raise Refusal(f"could not install {t}: {e}\n  already installed: {already}\n"
                          f"  fix the cause and re-run; the installer replaces whatever it finds")
        done.append(t)
        print(f"installed {name} ({len(data)} files) -> {t}")
        if warning:
            warnings.append(warning)
    for w in warnings:
        print(f"install.py install: warning: {w}", file=sys.stderr)
    return 0


def cmd_check(args):
    name, description, errors = check_skill()
    if errors:
        print("SKILL.md fails the upload check:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"ok: {name}, description {len(description):,}/{DESCRIPTION_MAX:,} characters")
    return 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in COMMANDS + ("-h", "--help"):
        argv.insert(0, "install")
    parser = argparse.ArgumentParser(
        prog="install.py",
        description="Install, package or check the OKR-Ninja skill. With no command, installs it.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("install", help="copy the skill into the .claude and .agents skills folders (default)")
    p.add_argument("--project", metavar="DIR", help="install into DIR/.claude/skills and DIR/.agents/skills")
    p.add_argument("--only", choices=("claude", "agents"), help="install only one of the two targets")
    p = sub.add_parser("build", help="write the .skill upload and the .plugin package")
    p.add_argument("--out", metavar="DIR", help="output folder (default: dist/ in the checkout)")
    sub.add_parser("check", help="validate SKILL.md's frontmatter for skill uploads")
    args = parser.parse_args(argv)
    try:
        return {"install": cmd_install, "build": cmd_build, "check": cmd_check}[args.command](args)
    except (Refusal, OSError) as e:
        print(f"install.py {args.command}: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
