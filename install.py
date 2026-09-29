#!/usr/bin/env python3
"""Install, package or check the OKR-Ninja skill (Python 3.8+ standard library only).

One command installs or updates it, with no clone (the same command again is the update):
  curl -fsSL https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py | python3 -I -

Commands
  install   (default) copy the skill into ~/.claude/skills/<name> (Claude Code; Cursor reads it
            too) and ~/.agents/skills/<name> (Codex, Cursor and other .agents-standard tools)
              --project DIR       install into DIR/.claude/skills and DIR/.agents/skills instead
              --only claude|agents  install one of the two targets
  build     write <name>.skill (the skill upload for claude.ai and Cowork) and <name>.plugin
            (a Claude plugin) into dist/ in the checkout, or into the current folder in remote
            mode; --out DIR writes elsewhere
  check     validate SKILL.md's frontmatter against the rules skill uploads enforce, plus its
            metadata.version

Where the skill comes from
  A checkout: when this file sits in a folder holding SKILL.md and README.md (a clone or a
  downloaded archive of the repo) and no option below is given.
  Remote mode, in every other case (piped into python3, or a copy downloaded on its own): the
  newest published GitHub Release of im1tta/OKR-Ninja, read from its source archive in memory.
              --release TAG       use that release instead of the latest one
              --repo OWNER/NAME   use a fork's releases
              --source ZIP        read a local zip of the repo instead of downloading

Only the runtime payload ships: SKILL.md and LICENSE plus the files under references/ and
examples/.

Design: openspec/changes/archive/2026-09-24-add-cross-platform-install/design.md (cross-platform D*)
        openspec/changes/archive/2026-09-29-add-one-command-install/design.md (one-command D*)
Contract: openspec/specs/distribution/spec.md
"""
from __future__ import annotations

import argparse
import http.client
import io
import json
import os
import re
import shutil
import stat
import struct
import sys
import tempfile
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import warnings
import zipfile
import zlib
from pathlib import Path, PurePosixPath

try:
    import ssl
except ImportError:  # a Python built without TLS; any download then fails with a named URL
    ssl = None

SCRIPT_FILE = globals().get("__file__")  # "<stdin>" when piped, absent under python3 -c
SKILL_NAME = "okr-ninja"
DEFAULT_REPO = "im1tta/OKR-Ninja"
PAYLOAD_DIRS = ("references", "examples")
COMMANDS = ("install", "build", "check")

# Remote mode (one-command D2-D5): only these hosts, over https, within these sizes.
ALLOWED_HOSTS = ("github.com", "codeload.github.com")
MAX_DOWNLOAD = 100 * 1024 * 1024
MAX_PAYLOAD = 20 * 1024 * 1024
TIMEOUT = 60
USER_AGENT = "okr-ninja-installer"
_extra_handlers = ()  # test seam: extra urllib handlers for make_opener()

SEMVER = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
                    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?")
REPO_RE = re.compile(r"([A-Za-z0-9][A-Za-z0-9-]{0,38})/([A-Za-z0-9._-]{1,100})")
TAG_RE = re.compile(r"[A-Za-z0-9._+-]+")
RESERVED_NAME = re.compile(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(\..*)?")

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


def shown(text):
    """Text safe to print: control and format characters (such as U+202E) escaped, newlines
    kept, ordinary non-ASCII text such as a user's home path left readable (one-command D5)."""
    return "".join(c if c == "\n" or not (unicodedata.category(c)[0] == "C"
                                          or unicodedata.category(c) in ("Zl", "Zp"))
                   else ascii(c)[1:-1] for c in str(text))


def say(text, stream=None):
    print(shown(text), file=stream or sys.stdout)


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

    Strict by design (cross-platform D2): it reads the one-line subset of YAML that skill
    frontmatter uses, the way an upload's validator and YAML parser read it, and refuses what it
    cannot classify rather than guessing. It is not a YAML parser.
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
            errors.append(f"line {n}: duplicate key {ascii(key)}")
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
    indented `key: value` lines at one indentation, each key and value a one-line string.
    Returns (errors, {key: value} for the entries that pass)."""
    where = f"line {field['line']}"
    if field["raw"]:
        if field["continued"]:
            return [f"{where}: 'metadata' has a value on its line and indented lines below it"], {}
        return [f"{where}: 'metadata' must be a map: indented 'key: value' lines below it"], {}
    errors, values, indent = [], {}, None
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
        raw_key = m.group(2)
        label = raw_key if raw_key.isascii() and raw_key.isprintable() else ascii(raw_key)[1:-1]
        key = {"raw": raw_key, "line": n, "continued": False}
        name, error = scalar(key, f"metadata key {label}")
        if error:
            errors.append(error)
            continue
        entry = {"raw": (m.group(3) or "").rstrip(" "), "line": n, "continued": False}
        value, error = scalar(entry, f"metadata.{label}", comments_allowed=True)
        if error:
            errors.append(error)
        else:
            values[name] = value
    return errors, values


def check_skill(root):
    """Validate a checkout's SKILL.md. Returns (name, description, version, errors)."""
    path = root / "SKILL.md"
    if path.is_symlink():
        return None, None, None, [f"{path} is a symlink; the payload is never read through symlinks"]
    try:
        # Universal newlines, exactly as the upload validator reads it: CRLF files pass.
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return None, None, None, [f"cannot read {path}: {e}"]
    return check_skill_text(text)


def check_skill_text(text):
    """Validate SKILL.md text from any source (read with universal newlines) against the
    upload rules plus metadata.version. Returns (name, description, version, errors)."""
    fields, errors = read_frontmatter(text)
    if not fields and errors:
        return None, None, None, errors
    metadata = {}
    extra = sorted(set(fields) - ALLOWED_KEYS)
    if extra:
        errors.append(f"unexpected frontmatter key(s): {', '.join(ascii(k) for k in extra)} "
                      f"(allowed: {', '.join(sorted(ALLOWED_KEYS))})")
    for key, field in fields.items():
        if key in ("name", "description") or key not in ALLOWED_KEYS:
            continue
        if key == "metadata":
            meta_errors, metadata = check_metadata(field)
            errors.extend(meta_errors)
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
            errors.append(f"name {ascii(name)} must use only lowercase letters, digits and hyphens")
        elif name.startswith("-") or name.endswith("-") or "--" in name:
            errors.append(f"name {ascii(name)} cannot start or end with a hyphen or contain '--'")
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

    # Not an upload rule: the skill's single version (one-command D6).
    version = metadata.get("version")
    if "metadata" not in fields or ("version" not in metadata and not any(
            re.match(r"^ +version:", line) for _, line in fields["metadata"]["children"])):
        errors.append("metadata.version is missing; add a 'metadata:' map holding "
                      "'  version: \"X.Y.Z\"' to the frontmatter")
    elif version is not None and not SEMVER.fullmatch(version):
        errors.append(f"metadata.version {ascii(version)} is not a semantic version "
                      f"(MAJOR.MINOR.PATCH such as 0.2.0, no leading zeros)")
    if version is not None and not SEMVER.fullmatch(version):
        version = None
    return name, description, version, errors


def version_in(text):
    """The semantic metadata.version in SKILL.md text, or None. Never raises."""
    try:
        fields, _ = read_frontmatter(text)
        field = fields.get("metadata")
        if field is None:
            return None
        version = check_metadata(field)[1].get("version")
    except Exception:
        return None
    return version if version is not None and SEMVER.fullmatch(version) else None


def refuse_on_errors(errors, header):
    if errors:
        raise Refusal(header + ":\n" + "\n".join(f"  - {e}" for e in errors))


# ---------------------------------------------------------------------------------------
# Payload
# ---------------------------------------------------------------------------------------

def payload_files(root):
    """The runtime payload as sorted POSIX-relative paths: SKILL.md, LICENSE, references/,
    examples/.

    Regular files only; hidden names, __pycache__, *.pyc and Windows folder metadata are
    skipped, symlinks are never followed (so nothing outside the checkout can ship), and an
    unreadable folder stops the run instead of being skipped (cross-platform D3).
    """
    for top_file in ("SKILL.md", "LICENSE"):
        path = root / top_file
        if path.is_symlink():
            raise Refusal(f"{path} is a symlink; the payload is never read through symlinks")
        if not path.is_file():
            raise Refusal(f"{top_file} is missing from {root}; is this an OKR-Ninja checkout?")

    def unreadable(err):
        raise Refusal(f"cannot read {err.filename}: {err.strerror}; nothing was built or installed")

    files = ["LICENSE", "SKILL.md"]
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
                if (f.startswith(".") or f == "__pycache__" or f.lower() in OS_NOISE or f.endswith(".pyc")
                        or p.is_symlink() or not p.is_file()):
                    continue
                files.append(p.relative_to(root).as_posix())
    return sorted(files)


def read_payload(root):
    """Read the whole payload before anything is written, so an unreadable file stops the
    run before a folder is created (cross-platform D3). Returns {relative path: bytes}."""
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
# Where the payload comes from: a checkout, or a release archive (remote mode)
# ---------------------------------------------------------------------------------------

def checkout_root(file_attr, argv0):
    """The checkout folder this installer reads, or None for remote mode (one-command D1).

    Local only when the script is a real file (not piped: python3 - sets "<stdin>", and
    python3 -c sets no __file__) whose folder holds SKILL.md and README.md and, on POSIX, is not
    world-writable. Installed copies and unpacked .skill uploads carry SKILL.md but no README.md,
    so they never count as checkouts; nor does a shared folder such as /tmp.
    """
    if not isinstance(file_attr, str) or not file_attr or file_attr.startswith("<"):
        return None
    if argv0 in ("-", "-c"):
        return None
    try:
        path = Path(file_attr)
        if not path.is_file():
            return None
        root = path.resolve().parent
        if os.name != "nt" and os.stat(root).st_mode & stat.S_IWOTH:
            return None  # a shared folder such as /tmp: anyone could have planted a checkout there
        if (root / "SKILL.md").is_file() and (root / "README.md").is_file():
            return root
    except OSError:
        return None
    return None


def script_dir(file_attr):
    """The folder of the running script when it is a real file, else None. It is the checkout
    for the rule that refuses a target which is, or contains, where the installer runs from."""
    if not isinstance(file_attr, str) or not file_attr or file_attr.startswith("<"):
        return None
    try:
        path = Path(file_attr)
        return path.resolve().parent if path.is_file() else None
    except OSError:
        return None


def check_repo(repo):
    m = REPO_RE.fullmatch(repo)
    if not m or m.group(2) in (".", ".."):
        raise Refusal(f"--repo {ascii(repo)}: expected OWNER/NAME, the owner 1-39 letters, digits "
                      f"and hyphens, the name 1-100 letters, digits, '.', '_' and '-'")
    return repo


def check_tag(tag, option="--release"):
    if not TAG_RE.fullmatch(tag) or tag in (".", ".."):
        raise Refusal(f"{option} {ascii(tag)}: a release tag uses only letters, digits, "
                      f"'.', '_', '+' and '-'")
    return tag


def check_url(url):
    """Refuse anything but https on github.com or codeload.github.com (one-command D4)."""
    try:
        parts = urllib.parse.urlsplit(url)
        port = parts.port
    except ValueError:
        parts, port = None, -1
    if (parts is None or parts.scheme != "https" or (parts.hostname or "") not in ALLOWED_HOSTS
            or "@" in parts.netloc or port not in (None, 443)):
        raise Refusal(f"refusing to fetch {ascii(url)}: only https URLs on "
                      f"{' and '.join(ALLOWED_HOSTS)} are allowed; nothing was written")
    return url


class PinnedRedirects(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an allowed https URL."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def make_opener(*extra_handlers):
    return urllib.request.build_opener(PinnedRedirects(), *extra_handlers)


class HttpStatus(Refusal):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


def cert_advice():
    """How to make CA certificates available on this platform (one-command D12)."""
    if sys.platform == "darwin" and ssl is not None:
        cafile = ssl.get_default_verify_paths().openssl_cafile
        if not cafile or not os.path.exists(cafile):
            return ("this Python has no CA certificates: run 'Install Certificates.command' in the "
                    f"Python {sys.version_info[0]}.{sys.version_info[1]} folder under "
                    f"/Applications, then re-run")
    return "point SSL_CERT_FILE at your system's or organisation's CA bundle (a .pem file), then re-run"


def describe_failure(url, err):
    reason = err.reason if isinstance(err, urllib.error.URLError) else err
    if ((ssl is not None and isinstance(reason, ssl.SSLCertVerificationError))
            or "CERTIFICATE_VERIFY_FAILED" in str(reason)):
        return f"cannot verify the TLS certificate for {url} ({reason}); {cert_advice()}"
    return f"cannot download {url}: {cause(reason)}; nothing was written"


def open_url(url, opener):
    check_url(url)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        return opener.open(request, timeout=TIMEOUT)
    except urllib.error.HTTPError as e:
        where = e.filename or url
        e.close()
        raise HttpStatus(f"cannot download {where}: HTTP {e.code} {e.reason}; nothing was written",
                         e.code)
    except (urllib.error.URLError, OSError, http.client.HTTPException, ValueError) as e:
        raise Refusal(describe_failure(url, e))


def download(url, opener):
    """GET url through the pinned opener into memory, at most MAX_DOWNLOAD bytes."""
    response = open_url(url, opener)
    chunks, total = [], 0
    try:
        with response:
            headers = response.headers
            length = headers.get("Content-Length") if headers else None
            declared = int(length) if length and length.strip().isdigit() else None
            chunked = "chunked" in ((headers.get("Transfer-Encoding") if headers else None) or "").lower()
            if declared is not None and declared > MAX_DOWNLOAD:
                raise Refusal(f"{url} is {declared:,} bytes; the limit is {MAX_DOWNLOAD:,}")
            while True:
                chunk = response.read(1 << 20)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_DOWNLOAD:
                    raise Refusal(f"{url} exceeds {MAX_DOWNLOAD:,} bytes; nothing was written")
                chunks.append(chunk)
            # http.client returns a short body silently when the connection closes early.
            if declared is not None and not chunked and total != declared:
                raise Refusal(f"cannot download {url}: the connection closed after {total:,} of "
                              f"{declared:,} bytes; nothing was written")
    except (OSError, http.client.HTTPException, ValueError) as e:
        raise Refusal(describe_failure(url, e))
    return b"".join(chunks)


def resolve_latest(repo, opener):
    """The tag of the repository's latest published release, from GitHub's /releases/latest
    redirect (one-command D2). Drafts and pre-releases are never "latest"."""
    url = f"https://github.com/{repo}/releases/latest"
    missing = (f"found no published release of {repo} at {url}; publish one, or name a tag "
               f"with --release")
    try:
        response = open_url(url, opener)
    except HttpStatus as e:
        if e.code == 404:
            raise Refusal(missing)
        raise
    with response:
        final = response.geturl() or url
    parts = urllib.parse.urlsplit(final)
    m = re.fullmatch(r"/[^/]+/[^/]+/releases/tag/([^/?#]+)/?", parts.path)
    if parts.hostname != "github.com" or not m:
        raise Refusal(f"{missing} (it led to {ascii(final)})")
    return check_tag(urllib.parse.unquote(m.group(1)), option="the latest release's tag")


def archive_url(repo, tag):
    return f"https://github.com/{repo}/archive/refs/tags/{urllib.parse.quote(tag, safe='')}.zip"


def bad_entry_name(name):
    """Why a stored zip entry name is unsafe anywhere in the archive, or None."""
    if not name:
        return "has an empty name"
    if "\x00" in name:
        return "contains a NUL character"
    if "\\" in name:
        return "contains a backslash"
    if name.startswith("/"):
        return "is an absolute path"
    if re.match(r"[A-Za-z]:", name):
        return "starts with a drive letter"
    segments = (name[:-1] if name.endswith("/") else name).split("/")
    if any(seg in ("", ".", "..") for seg in segments):
        return "has an empty, '.' or '..' segment"
    return None


def unportable(component):
    """Why a payload path component cannot be written on every platform, or None."""
    if any(unicodedata.category(c) == "Cc" for c in component):  # C0, DEL and C1
        return "contains a control character"
    if any(unicodedata.category(c) == "Cn" for c in component):
        # Case folding needs to know the character: an older Python (3.9 has Unicode 13) would
        # miss a case pair that a newer file system merges.
        return (f"contains a character this Python's Unicode {unicodedata.unidata_version} "
                f"does not know; a newer Python can read it")
    if any(c in '<>:"|?*' for c in component):
        return 'contains one of < > : " | ? *'
    if component.endswith((".", " ")):
        return "ends in '.' or a space"
    if RESERVED_NAME.fullmatch(component):
        return "is a Windows reserved device name"
    return None


BOUNDED_METHODS = (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)  # zipfile bounds only these reads
UNICODE_PATH_EXTRA = 0x7075  # Info-ZIP Unicode Path: Python 3.12+ renames an entry from it


def extra_ids(extra):
    """The header IDs in a zip entry's extra field, walked as zipfile walks it."""
    ids = []
    while len(extra) >= 4:
        tp, ln = struct.unpack("<HH", extra[:4])
        ids.append(tp)
        extra = extra[4 + ln:]
    return ids


def local_extra(blob, info):
    """The extra field of an entry's local header (zipfile reads only the central directory's
    copy), or b"" when no local header sits at the entry's offset."""
    at = info.header_offset
    if at < 0 or blob[at:at + 4] != b"PK\x03\x04" or len(blob) < at + 30:
        return b""
    nlen, xlen = struct.unpack_from("<HH", blob, at + 26)
    return blob[at + 30 + nlen:at + 30 + nlen + xlen]


def cause(err):
    """An exception's text for a refusal. zipfile's messages repeat entry names through %r,
    which keeps non-ASCII letters, so the text is escaped as every archive-derived name is."""
    return (str(err) or type(err).__name__).encode("ascii", "backslashreplace").decode("ascii")


def read_archive(blob):
    """Read the payload of a GitHub source archive (zip) into memory, never extracting it
    (one-command D5). Returns ({relative path: bytes}, SKILL.md text)."""
    try:
        with warnings.catch_warnings():  # 3.12+ warns on an empty 0x7075 field; it is refused below
            warnings.simplefilter("ignore")
            zf = zipfile.ZipFile(io.BytesIO(blob))
        infos = zf.infolist()
    except Exception as e:  # corrupt archives raise types no fixed list anticipates
        raise Refusal(f"the archive is not a readable zip ({cause(e)}); nothing was written")

    # Every check and every written path uses the name as stored (orig_filename): the
    # interpreter-dependent `filename` is never read.
    stored, headers, tops = set(), {}, set()
    for info in infos:
        raw = info.orig_filename
        problem = bad_entry_name(raw)
        if problem:
            raise Refusal(f"archive entry {ascii(raw)} {problem}; nothing was written")
        if (UNICODE_PATH_EXTRA in extra_ids(info.extra)
                or UNICODE_PATH_EXTRA in extra_ids(local_extra(blob, info))):
            raise Refusal(f"archive entry {ascii(raw)} carries a Unicode Path extra field (0x7075), "
                          f"which some readers use in place of its checked name; a repo archive "
                          f"never has one; nothing was written")
        if raw in stored:
            raise Refusal(f"archive entry {ascii(raw)} appears twice; nothing was written")
        stored.add(raw)
        if info.header_offset in headers:  # 3.12+ reads such entries with only a warning
            raise Refusal(f"archive entries {ascii(headers[info.header_offset])} and {ascii(raw)} "
                          f"share one local header; a repo archive never does; nothing was written")
        headers[info.header_offset] = raw
        if "/" not in raw.rstrip("/") and not raw.endswith("/"):
            raise Refusal(f"archive entry {ascii(raw)} sits beside the top-level folder; a repo "
                          f"archive holds exactly one top-level folder")
        tops.add(raw.split("/", 1)[0])
    if len(tops) != 1:
        raise Refusal(f"the archive holds {len(tops)} top-level folders, not one; nothing was written")
    top = tops.pop() + "/"

    selected = {}
    for info in infos:
        if info.orig_filename.endswith("/"):
            continue  # directory entry
        rel = info.orig_filename[len(top):]  # unique: every stored name is
        parts = rel.split("/")
        is_symlink = (info.external_attr >> 16) & 0o170000 == 0o120000
        if rel in ("SKILL.md", "LICENSE"):
            if is_symlink:
                raise Refusal(f"{rel} in the archive is a symbolic link; the payload is never "
                              f"read through symlinks")
        elif parts[0] in PAYLOAD_DIRS and len(parts) > 1:
            if (any(p.startswith(".") or p == "__pycache__" for p in parts[1:])
                    or parts[-1].lower() in OS_NOISE
                    or parts[-1].endswith(".pyc") or is_symlink):
                continue  # filtered exactly as a checkout's payload is
        else:
            continue  # not payload: CLAUDE.md, evals/, install.py, ...
        for part in parts:
            problem = unportable(part)
            if problem:
                raise Refusal(f"archive entry {ascii(info.orig_filename)}: {ascii(part)} {problem}")
        selected[rel] = info

    # Paths that one file system would merge (letter case, Unicode form, file vs folder).
    files, folders = {}, {}
    for rel in sorted(selected):
        # Canonical caseless matching (NFD, casefold, NFD): casefold can un-normalise a string.
        keys = [unicodedata.normalize("NFD", unicodedata.normalize("NFD", p).casefold())
                for p in rel.split("/")]
        key = "/".join(keys)
        clash = files.get(key) or folders.get(key)
        if clash:
            raise Refusal(f"archive entries {ascii(clash)} and {ascii(rel)} collide on a "
                          f"case-insensitive disk; nothing was written")
        files[key] = rel
        for i in range(1, len(keys)):
            folder = "/".join(keys[:i])
            if folder in files:
                raise Refusal(f"archive entries {ascii(files[folder])} and {ascii(rel)} collide "
                              f"(a file and a folder of the same name); nothing was written")
            folders.setdefault(folder, rel)

    for required in ("SKILL.md", "LICENSE"):
        if required not in selected:
            raise Refusal(f"the archive has no {required} in {ascii(top)}; is it an OKR-Ninja archive?")
    for d in PAYLOAD_DIRS:
        if not any(rel.startswith(d + "/") for rel in selected):
            raise Refusal(f"the archive's {d}/ holds no payload file; is it an OKR-Ninja archive?")
    for rel, info in sorted(selected.items()):
        if info.compress_type not in BOUNDED_METHODS:
            raise Refusal(f"archive entry {ascii(info.orig_filename)} uses compression method "
                          f"{info.compress_type}; a repo archive uses only stored or deflate, "
                          f"whose size the installer can bound; nothing was written")
    declared = sum(info.file_size for info in selected.values())
    if declared > MAX_PAYLOAD:
        raise Refusal(f"the archive's payload declares {declared:,} bytes; the limit is "
                      f"{MAX_PAYLOAD:,}")

    data, total = {}, 0
    with warnings.catch_warnings():  # any zipfile warning while reading becomes a refusal
        warnings.simplefilter("error")
        for rel, info in sorted(selected.items()):
            chunks = []
            try:
                with zf.open(info) as f:
                    while True:
                        chunk = f.read(1 << 16)
                        if not chunk:
                            break
                        total += len(chunk)
                        if total > MAX_PAYLOAD:
                            raise Refusal(f"the archive's payload exceeds {MAX_PAYLOAD:,} bytes")
                        chunks.append(chunk)
            except Refusal:
                raise
            except Exception as e:  # LZMAError, OverflowError on zip64 offsets, EOFError, ...
                raise Refusal(f"cannot read {ascii(info.orig_filename)} from the archive "
                              f"({cause(e)}); nothing was written")
            data[rel] = b"".join(chunks)
    try:
        # Universal newlines, exactly as a checkout's SKILL.md is read: CRLF passes.
        text = io.TextIOWrapper(io.BytesIO(data["SKILL.md"]), encoding="utf-8", newline=None).read()
    except UnicodeDecodeError as e:
        raise Refusal(f"SKILL.md in the archive is not UTF-8 ({e})")
    return data, text


def read_source(path):
    """The bytes of a --source archive: a regular file of at most MAX_DOWNLOAD bytes."""
    where = Path(os.path.expanduser(path)) if path else Path("")
    try:
        st = os.stat(where) if path else None
    except OSError as e:
        raise Refusal(f"--source {ascii(path)}: {e.strerror or e}")
    if st is None or not stat.S_ISREG(st.st_mode):
        raise Refusal(f"--source {ascii(path)}: not a regular file")
    if st.st_size > MAX_DOWNLOAD:
        raise Refusal(f"--source {ascii(path)} is {st.st_size:,} bytes; the limit is {MAX_DOWNLOAD:,}")
    try:
        with open(where, "rb") as f:
            blob = f.read(MAX_DOWNLOAD + 1)
    except OSError as e:
        raise Refusal(f"--source {ascii(path)}: {e.strerror or e}")
    if len(blob) > MAX_DOWNLOAD:
        raise Refusal(f"--source {ascii(path)} exceeds {MAX_DOWNLOAD:,} bytes")
    return blob


class Payload:
    """The skill to act on: files (None until needed), frontmatter results, and provenance."""

    def __init__(self, data, name, description, version, errors, origin, header, out_dir, guard):
        self.data, self.name, self.description, self.version = data, name, description, version
        self.errors, self.origin, self.header = errors, origin, header
        self.out_dir, self.guard = out_dir, guard


def load_payload(args, need_files):
    """Read and check the skill from the checkout or, in remote mode, from a release archive.
    Writes nothing. Frontmatter problems are returned in .errors, not raised."""
    remote_opts = any(v is not None for v in (args.release, args.repo, args.source))
    argv0 = sys.argv[0] if sys.argv else ""
    root = None if remote_opts else checkout_root(SCRIPT_FILE, argv0)
    guard = script_dir(SCRIPT_FILE) if argv0 not in ("-", "-c") else None
    if root is not None:
        say(f"reading the checkout at {root}")
        name, description, version, errors = check_skill(root)
        data = read_payload(root) if need_files and not errors else None
        return Payload(data, name, description, version, errors, str(root),
                       "SKILL.md fails the upload check", root / "dist", guard)

    repo = check_repo(args.repo) if args.repo is not None else DEFAULT_REPO
    release = args.release
    if release is not None and release != "latest":
        check_tag(release)
    if args.source is not None:
        if release == "latest":
            raise Refusal("--source and --release latest cannot be combined: a local archive "
                          "has no latest release to compare against")
        blob = read_source(args.source)
        tag, origin = release, args.source
    else:
        opener = make_opener(*_extra_handlers)
        tag = release if release not in (None, "latest") else resolve_latest(repo, opener)
        say(f"downloading {repo} {tag} from github.com")
        blob = download(archive_url(repo, tag), opener)
        origin = f"{repo} {tag}"
    data, text = read_archive(blob)
    name, description, version, errors = check_skill_text(text)
    if name is not None and name != SKILL_NAME:
        errors.append(f"the archive's skill is named {ascii(name)}, not '{SKILL_NAME}'; a downloaded "
                      f"skill never chooses which skills folder is replaced")
    if tag is not None and version is not None:
        expected = tag[1:] if tag.startswith("v") else tag
        if version != expected:
            errors.append(f"release {tag} carries metadata.version {version}; a release's version "
                          f"must equal its tag")
    return Payload(data, name, description, version, errors, origin,
                   f"the skill from {origin} fails the check", None, guard)


def current_folder():
    """Where a remote build writes by default (one-command D10), resolved only when needed."""
    try:
        return Path.cwd()
    except OSError:
        raise Refusal("the current folder no longer exists; cd to an existing folder or pass "
                      "--out DIR; nothing was built")


def announce(payload):
    say(f"using {payload.name} {payload.version} from {payload.origin}")


def previous_version(target):
    """What an install at target replaces: 'was X.Y.Z', 'new install' or 'was unversioned'.
    Reads at most 64 KB of a regular SKILL.md; never raises (one-command D9)."""
    try:
        if not (is_link(target) or target.exists()):
            return "new install"
        path = target / "SKILL.md"
        if not stat.S_ISREG(os.stat(path).st_mode):
            return "was unversioned"
        with open(path, "r", encoding="utf-8", errors="replace", newline=None) as f:
            text = f.read(64 * 1024)
    except (OSError, ValueError):
        return "was unversioned"
    version = version_in(text)
    return f"was {version}" if version else "was unversioned"


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
    if args.out is not None and not args.out:
        raise Refusal("--out '': not a directory; nothing was built")
    payload = load_payload(args, need_files=True)
    refuse_on_errors(payload.errors, payload.header)
    announce(payload)
    name, data = payload.name, payload.data
    out = (Path(args.out).expanduser() if args.out is not None
           else payload.out_dir if payload.out_dir is not None else current_folder())
    if out.exists() and not out.is_dir():
        raise Refusal(f"--out {out}: exists and is not a directory")
    out.mkdir(parents=True, exist_ok=True)

    skill = out / f"{name}.skill"
    write_zip(skill, [(f"{name}/{f}", b) for f, b in data.items()])

    manifest = {"name": name, "version": payload.version,
                "description": first_sentence(payload.description)}
    plugin = out / f"{name}.plugin"
    write_zip(plugin, [(".claude-plugin/plugin.json",
                        (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))]
              + [(f"skills/{name}/{f}", b) for f, b in data.items()])

    print(f"payload ({len(data)} files):")
    for f in data:
        print(f"  {f if f.isascii() and f.isprintable() else ascii(f)}")
    say(f"wrote {skill}  (upload under Skills in claude.ai settings; Cowork uses the same account skills)")
    say(f"wrote {plugin}  (Claude plugin, version {payload.version})")
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
    """Return why target cannot be replaced safely, or None (spec: Replacing an existing install
    is safe). source is the folder the installer runs from, or None when it runs from no file."""
    if is_link(target):
        return None  # only the link itself is moved and removed; whatever it points to is left alone
    if target.exists():
        if not target.is_dir():
            return f"{target} exists and is not a directory or a symlink"
        # File-system identity, never path strings: on a case-insensitive disk ".../OKR-Ninja"
        # and ".../okr-ninja" are one directory while comparing unequal (cross-platform D6).
        if source is not None and any(same_file(target, p) for p in (source, *source.parents)):
            return (f"{target} is the folder this installer runs from, or contains it; "
                    f"replacing it would delete the running copy. Run install.py from another "
                    f"folder, or skip that target with --only")
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
    """Delete a folder this installer owns (a moved-aside previous copy), cross-platform D6.

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
    (cross-platform D6). Returns a warning naming a previous copy that could not be deleted, else None."""
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
    if args.project is not None:
        project = os.path.expanduser(args.project)
        if not os.path.isdir(project):  # os.path.isdir("") is False, unlike Path("").is_dir()
            raise Refusal(f"--project {args.project!r}: not an existing directory; nothing was installed")
        base = Path(project)
    else:
        base = Path.home()
    payload = load_payload(args, need_files=True)
    refuse_on_errors(payload.errors, payload.header)
    announce(payload)
    name, data = payload.name, payload.data
    kinds = [args.only] if args.only else ["claude", "agents"]
    targets = [base / f".{kind}" / "skills" / name for kind in kinds]

    problems = [p for p in (refuse_target(t, payload.guard) for t in targets) if p]
    if problems:
        raise Refusal("nothing was installed:\n" + "\n".join(f"  - {p}" for p in problems))
    done, warnings = [], []
    for t in targets:
        replaced = previous_version(t)
        try:
            warning = copy_into(t, data)
        except OSError as e:
            already = ", ".join(map(str, done)) if done else "none"
            why = (f"{e.strerror}: {ascii(e.filename)}" if e.strerror and e.filename is not None
                   else str(e))
            raise Refusal(f"could not install {t}: {why}\n  already installed: {already}\n"
                          f"  fix the cause and re-run; the installer replaces whatever it finds")
        done.append(t)
        say(f"installed {name} {payload.version} ({len(data)} files) -> {t} ({replaced})")
        if warning:
            warnings.append(warning)
    for w in warnings:
        say(f"install.py install: warning: {w}", sys.stderr)
    return 0


def cmd_check(args):
    payload = load_payload(args, need_files=False)
    if payload.errors:
        say(f"{payload.header}:")
        for e in payload.errors:
            say(f"  - {e}")
        return 1
    announce(payload)
    say(f"ok: {payload.name} {payload.version}, description "
          f"{len(payload.description):,}/{DESCRIPTION_MAX:,} characters")
    return 0


class Parser(argparse.ArgumentParser):
    """argparse, with everything it prints (usage errors echo the command line) passed
    through the same filter as the installer's own messages."""

    def _print_message(self, message, file=None):
        if message:
            (file or sys.stderr).write(shown(message))


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):  # no terminal encoding turns a message into a traceback
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(errors="backslashreplace")
            except (ValueError, OSError):
                pass
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in COMMANDS + ("-h", "--help"):
        argv.insert(0, "install")
    parser = Parser(
        prog="install.py",
        description="Install, package or check the OKR-Ninja skill. With no command, installs it. "
                    "Reads the checkout this file sits in or, when there is none (piped into "
                    "python3, or downloaded on its own) or --release, --repo or --source is "
                    "given, a published release of " + DEFAULT_REPO + " (the newest unless "
                    "--release names one) or a local --source zip. See 'install.py install "
                    "--help' for the options.")
    remote = argparse.ArgumentParser(add_help=False)
    group = remote.add_argument_group("remote mode (one-command install and update)")
    group.add_argument("--release", metavar="TAG",
                       help="use this release instead of the latest one ('latest' is the default)")
    group.add_argument("--repo", metavar="OWNER/NAME",
                       help=f"use a fork's releases (default: {DEFAULT_REPO})")
    group.add_argument("--source", metavar="ZIP",
                       help="read this local zip of the repo instead of downloading")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("install", parents=[remote],
                       help="copy the skill into the .claude and .agents skills folders (default)")
    p.add_argument("--project", metavar="DIR", help="install into DIR/.claude/skills and DIR/.agents/skills")
    p.add_argument("--only", choices=("claude", "agents"), help="install only one of the two targets")
    p = sub.add_parser("build", parents=[remote], help="write the .skill upload and the .plugin package")
    p.add_argument("--out", metavar="DIR",
                   help="output folder (default: dist/ in the checkout, or the current folder in "
                        "remote mode)")
    sub.add_parser("check", parents=[remote],
                   help="validate SKILL.md's frontmatter for skill uploads, and its metadata.version")
    args = parser.parse_args(argv)
    try:
        return {"install": cmd_install, "build": cmd_build, "check": cmd_check}[args.command](args)
    except (Refusal, OSError) as e:
        say(f"install.py {args.command}: {e}", sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
