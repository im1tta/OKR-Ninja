"""Offline tests for install.py (standard library only).

Run from the repo root:  python3 -m unittest discover -s tests -v

The contract is the `distribution` capability: openspec/specs/distribution/spec.md (design D1-D13
in openspec/changes/archive/2026-09-29-add-one-command-install/design.md, building on
openspec/changes/archive/2026-09-24-add-cross-platform-install/design.md). Tests are named after the spec scenario they cover where practical
(`test_scenario_...`); every installer scenario maps to at least one test.

Nothing here touches the network:
- in-process remote runs go through install.py's opener seam (`_extra_handlers`): a fake HTTPS
  handler sits in front of the real redirect handler, so redirect pinning runs for real;
- every subprocess run points HTTPS_PROXY at a closed local port, so a stray request fails fast;
- release archives are built the way GitHub builds them, with `git archive --format=zip` over a
  temporary repo that commits the working tree's payload, or crafted with `zipfile` directly.

Every run that could install gets a scratch HOME (and USERPROFILE) and is checked to write
nothing outside it. /usr/bin/python3 on macOS writes stdlib bytecode caches under
$HOME/Library/Caches/com.apple.python even with -I; home snapshots ignore exactly that path.
"""
import ast
import collections
import contextlib
import email.message
import hashlib
import http.client
import importlib.util
import io
import json
import os
import re
import shutil
import ssl
import stat
import struct
import subprocess
import sys
import tempfile
import threading
import tokenize
import unicodedata
import unittest
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import warnings
import zlib
import zipfile
from pathlib import Path
from unittest import mock

sys.dont_write_bytecode = True

# ---------------------------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_PY = REPO_ROOT / "install.py"

HAS_GIT = shutil.which("git") is not None
POSIX = os.name == "posix"
IS_ROOT = POSIX and hasattr(os, "geteuid") and os.geteuid() == 0
needs_git = unittest.skipUnless(HAS_GIT, "git is not installed")
posix_only = unittest.skipUnless(POSIX, "POSIX only")
needs_permissions = unittest.skipUnless(POSIX and not IS_ROOT, "needs POSIX permissions and a non-root user")

SKILL = "okr-ninja"
SLUG = "im1tta/OKR-Ninja"
MB = 1024 * 1024
CLOSED_PROXY = "http://127.0.0.1:9"
PROXY_VARS = ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy",
              "NO_PROXY", "no_proxy")
MACOS_PY_CACHE = "Library/Caches/com.apple.python"

FILE, DIR, LINK = "file", "dir", "link"

MINI_DESCRIPTION = ("Audits OKRs for one team or a whole portfolio, checking goal quality and "
                    "cross-team alignment. Fictional test copy.")

MIT_LICENSE = """MIT License

Copyright (c) 2026 Test Author

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def latest_url(repo=SLUG):
    return "https://github.com/%s/releases/latest" % repo


def tag_page_url(tag, repo=SLUG):
    return "https://github.com/%s/releases/tag/%s" % (repo, tag)


def archive_url(tag, repo=SLUG):
    return "https://github.com/%s/archive/refs/tags/%s.zip" % (repo, tag)


def codeload_url(tag, repo=SLUG):
    return "https://codeload.github.com/%s/zip/refs/tags/%s" % (repo, tag)


# ---------------------------------------------------------------------------------------------
# Loading install.py and scratch space
# ---------------------------------------------------------------------------------------------

_module = None


def installer():
    """Import install.py by path as `okr_install` (once)."""
    global _module
    if _module is None:
        spec = importlib.util.spec_from_file_location("okr_install", str(INSTALL_PY))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["okr_install"] = mod
        try:
            spec.loader.exec_module(mod)
        except BaseException:
            sys.modules.pop("okr_install", None)
            raise
        _module = mod
    return _module


_scratch = None


def scratch_root():
    global _scratch
    if _scratch is None or not os.path.isdir(_scratch):
        _scratch = os.path.realpath(tempfile.mkdtemp(prefix="okr-install-tests-"))
        _releases.clear()  # release fixtures live under the scratch root
    return _scratch


def force_rmtree(path):
    """Delete a scratch tree even after a test locked parts of it (modes, BSD file flags)."""
    path = str(path)
    if not os.path.lexists(path):
        return
    for dirpath, dirnames, filenames in os.walk(path):
        for p in [dirpath] + [os.path.join(dirpath, n) for n in dirnames + filenames]:
            if os.path.islink(p):
                continue
            if hasattr(os, "chflags"):
                try:
                    os.chflags(p, 0)
                except OSError:
                    pass
            if os.path.isdir(p):
                try:
                    os.chmod(p, 0o700)
                except OSError:
                    pass
    shutil.rmtree(path, ignore_errors=True)


def tearDownModule():
    global _scratch
    if _scratch:
        force_rmtree(_scratch)
    _scratch = None
    _releases.clear()


def call_with_timeout(fn, timeout=30):
    """Run fn in a daemon thread; fail instead of hanging the suite."""
    box = {}

    def run():
        try:
            box["value"] = fn()
        except BaseException as e:  # re-raised in the caller
            box["error"] = e

    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(timeout)
    if t.is_alive():
        raise AssertionError("did not return within %ss" % timeout)
    if "error" in box:
        raise box["error"]
    return box["value"]


def case_insensitive(directory):
    probe = Path(directory, "CaseProbe")
    probe.write_text("x")
    try:
        return Path(directory, "caseprobe").exists()
    finally:
        probe.unlink()


# ---------------------------------------------------------------------------------------------
# Trees, snapshots and payloads
# ---------------------------------------------------------------------------------------------

def is_payload_noise(rel):
    parts = rel.split("/")
    return (any(p.startswith(".") or p == "__pycache__" for p in parts)
            or parts[-1].lower() in ("thumbs.db", "desktop.ini") or parts[-1].endswith(".pyc"))


def expected_payload(root):
    """The payload a checkout at root must yield, computed independently of install.py."""
    root = Path(root)
    data = {"SKILL.md": (root / "SKILL.md").read_bytes(), "LICENSE": (root / "LICENSE").read_bytes()}
    for top in ("references", "examples"):
        for dirpath, dirnames, filenames in os.walk(str(root / top)):
            dirnames[:] = [d for d in dirnames if not os.path.islink(os.path.join(dirpath, d))]
            for f in filenames:
                p = Path(dirpath, f)
                rel = p.relative_to(root).as_posix()
                if p.is_symlink() or not p.is_file() or is_payload_noise(rel):
                    continue
                data[rel] = p.read_bytes()
    return data


def payload_of(files):
    """The payload a {relative path: bytes} tree yields."""
    out = {}
    for rel, data in files.items():
        if data is None:
            continue
        top = rel.split("/")[0]
        if rel in ("SKILL.md", "LICENSE") or (top in ("references", "examples") and "/" in rel
                                               and not is_payload_noise(rel)):
            out[rel] = data
    return out


def is_python_cache(rel):
    return rel in ("Library", "Library/Caches") or rel == MACOS_PY_CACHE or rel.startswith(MACOS_PY_CACHE + "/")


def snapshot(root, home=False):
    """{relative path: description} of everything under root (None when root is absent).
    Files are hashed, links recorded by target; nothing is followed."""
    root = str(root)
    if not os.path.lexists(root):
        return None
    snap = {}
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir.replace(os.sep, "/") + "/"
        keep = []
        for n in sorted(dirnames):
            rel = rel_dir + n
            if home and is_python_cache(rel):
                continue
            p = os.path.join(dirpath, n)
            if os.path.islink(p):
                snap[rel] = ("link", os.readlink(p))
            else:
                snap[rel] = ("dir", stat.S_IMODE(os.lstat(p).st_mode))
                keep.append(n)
        dirnames[:] = keep
        for n in sorted(filenames):
            rel = rel_dir + n
            if home and is_python_cache(rel):
                continue
            p = os.path.join(dirpath, n)
            st = os.lstat(p)
            if stat.S_ISLNK(st.st_mode):
                snap[rel] = ("link", os.readlink(p))
            elif not stat.S_ISREG(st.st_mode):
                snap[rel] = ("special", stat.S_IFMT(st.st_mode))
            else:
                try:
                    digest = hashlib.sha256(Path(p).read_bytes()).hexdigest()
                except OSError:
                    digest = "unreadable"
                snap[rel] = ("file", digest, stat.S_IMODE(st.st_mode))
    return snap


def home_snapshot(home):
    return snapshot(home, home=True)


def names(value, text):
    """Whether text names value as given, or in its repr()/ascii() form."""
    return any(form in text for form in (value, repr(value)[1:-1], ascii(value)[1:-1]))


def write_files(root, files):
    root = Path(root)
    for rel, data in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
    return root


# ---------------------------------------------------------------------------------------------
# SKILL.md text
# ---------------------------------------------------------------------------------------------

KEEP = object()
DROP = object()


def mini_skill_md(version="0.2.0", name=SKILL, description=MINI_DESCRIPTION, raw_version=None):
    """A small valid SKILL.md; version None (and no raw_version) omits the metadata block."""
    lines = ["---", "name: " + name, "description: " + description, "license: MIT"]
    if raw_version is not None:
        lines += ["metadata:", "  version: " + raw_version]
    elif version is not None:
        lines += ["metadata:", '  version: "%s"' % version]
    lines += ["---", "", "# OKR-Ninja (test copy)", "", "Fictional content for installer tests.", ""]
    return "\n".join(lines)


def set_frontmatter(text, version=KEEP, name=None, description=None, raw_version=None):
    """Rewrite a SKILL.md's frontmatter: ensure `license: MIT`, set (or DROP) metadata.version,
    optionally replace name and description. Other metadata entries are kept."""
    lines = text.split("\n")
    if lines[0] != "---":
        raise ValueError("SKILL.md has no frontmatter")
    close = lines.index("---", 1)
    head, rest = lines[1:close], lines[close:]
    out, meta = [], []
    i = 0
    while i < len(head):
        line = head[i]
        if line.startswith("metadata:"):
            i += 1
            while i < len(head) and head[i].startswith(" "):
                meta.append(head[i])
                i += 1
            continue
        if name is not None and line.startswith("name:"):
            line = "name: " + name
        if description is not None and line.startswith("description:"):
            line = "description: " + description
        out.append(line)
        i += 1
    if not any(line.startswith("license:") for line in out):
        out.append("license: MIT")
    current = [m for m in meta if m.lstrip(" ").startswith("version:")]
    others = [m for m in meta if not m.lstrip(" ").startswith("version:")]
    if raw_version is not None:
        vlines = ["  version: " + raw_version]
    elif version is DROP:
        vlines = []
    elif version is KEEP:
        vlines = current
    else:
        vlines = ['  version: "%s"' % version]
    meta = vlines + others
    if meta:
        out += ["metadata:"] + meta
    return "\n".join(["---"] + out + rest)


def working_skill_text():
    return (REPO_ROOT / "SKILL.md").read_bytes().decode("utf-8")


def working_version():
    m = re.search(r'^metadata:\n(?:[ ]+.*\n)*?[ ]+version:[ ]*"?([^"\s]+)"?[ ]*$',
                  working_skill_text(), re.M)
    return m.group(1) if m else None


def working_license():
    p = REPO_ROOT / "LICENSE"
    return p.read_bytes() if p.is_file() else MIT_LICENSE.encode("ascii")


def working_dir_files():
    files = {}
    for top in ("references", "examples"):
        for p in sorted((REPO_ROOT / top).rglob("*")):
            rel = p.relative_to(REPO_ROOT).as_posix()
            if p.is_symlink() or not p.is_file() or is_payload_noise(rel):
                continue
            files[rel] = p.read_bytes()
    return files


# ---------------------------------------------------------------------------------------------
# Checkouts and release trees
# ---------------------------------------------------------------------------------------------

DEV_FILES = {
    "CLAUDE.md": b"# notes for agents\n",
    "evals/x.md": b"eval notes\n",
    ".claude/y.md": b"claude settings\n",
    "tests/test_x.py": b"# a test\n",
    "openspec/o.md": b"spec\n",
    "dist/okr-ninja.skill": b"a stale package\n",
    "references/.cache/x.md": b"hidden cache\n",
    "references/.DS_Store": b"\x00\x00\x00\x01Bud1",
    "examples/Thumbs.db": b"thumbs",
    "references/__pycache__/m.cpython-39.pyc": b"\x61\x0d\x0d\x0a",
    "references/__pycache__/notes.md": b"not bytecode\n",
    "references/m.pyc": b"\x61\x0d\x0d\x0a",
}


def make_tree(dest, version="0.2.0", name=None, description=None, extra=None, drop=(),
              license=True, dev_files=True, raw_version=None):
    """A checkout made of the working tree's payload (SKILL.md rewritten to carry `license: MIT`
    and metadata.version), README.md and the current install.py, plus development files, OS
    noise and a symlink under references/ that must never ship. No git metadata."""
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    skill = set_frontmatter(working_skill_text(), version=version, name=name,
                            description=description, raw_version=raw_version)
    files = {"SKILL.md": skill.encode("utf-8"),
             "README.md": (REPO_ROOT / "README.md").read_bytes(),
             "install.py": INSTALL_PY.read_bytes()}
    if license:
        files["LICENSE"] = working_license()
    files.update(working_dir_files())
    if dev_files:
        files.update(DEV_FILES)
    files.update(extra or {})
    for rel in drop:
        files.pop(rel, None)
    write_files(dest, files)
    if dev_files and POSIX:
        os.symlink("../SKILL.md", str(dest / "references" / "link.md"))
    return dest


def git(args, cwd):
    home = Path(scratch_root(), "git-home")
    home.mkdir(exist_ok=True)
    env = dict(os.environ)
    for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY"):
        env.pop(k, None)
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, HOME=str(home),
               GIT_TERMINAL_PROMPT="0", GIT_AUTHOR_DATE="2026-09-01T00:00:00Z",
               GIT_COMMITTER_DATE="2026-09-01T00:00:00Z")
    cmd = ["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false",
           "-c", "core.autocrlf=false", "-c", "init.defaultBranch=main"] + list(args)
    p = subprocess.run(cmd, cwd=str(cwd), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), p.stderr.decode("utf-8", "replace")))
    return p


def git_archive(tree, prefix, out):
    """Commit tree into a fresh repo and archive it exactly as GitHub's archive route does."""
    git(["init", "-q", "."], tree)
    git(["add", "-A", "-f", "."], tree)
    git(["commit", "-q", "-m", "fixture"], tree)
    git(["archive", "--format=zip", "--prefix=" + prefix, "HEAD", "-o", str(out)], tree)
    return Path(out)


Release = collections.namedtuple("Release", "key version tree zip blob payload")

_releases = {}
RELEASE_SPECS = {
    "v0.2.0": dict(version="0.2.0", extra={"references/only-in-020.md": b"removed in 0.3.0\n"}),
    "v0.3.0": dict(version="0.3.0", extra={"references/only-in-030.md": b"added in 0.3.0\n"}),
    "other": dict(version="0.2.0", name="other-skill"),
}


def release(key):
    """A git-archive release fixture, built once per run: tree, zip path, bytes, payload."""
    if key not in _releases:
        spec = RELEASE_SPECS[key]
        base = Path(scratch_root(), "releases", key)
        tree = make_tree(base / "tree", **spec)
        zip_path = git_archive(tree, "OKR-Ninja-%s/" % spec["version"], base / (key + ".zip"))
        _releases[key] = Release(key, spec["version"], tree, zip_path, zip_path.read_bytes(),
                                 expected_payload(tree))
    return _releases[key]


def checkout_from(rel, dest):
    """A scratch checkout made of the same files a release archive was built from."""
    shutil.copytree(str(rel.tree), str(dest), symlinks=True, ignore=shutil.ignore_patterns(".git"))
    Path(dest, "install.py").write_bytes(INSTALL_PY.read_bytes())
    return Path(dest)


# ---------------------------------------------------------------------------------------------
# Crafted zips
# ---------------------------------------------------------------------------------------------

def zip_bytes(entries, comment=b"", compress=zipfile.ZIP_DEFLATED, extras=None):
    """Write entries (name, data[, kind]) the way git archive does: files and folders with
    create_system 0 and mode 0 (folders flagged 0x10), symlinks with create_system 3 and
    Unix mode 0o120777. Duplicate names are written as given; `extras` maps an entry name to
    the extra field it carries."""
    buf = io.BytesIO()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with zipfile.ZipFile(buf, "w") as zf:
            for entry in entries:
                name, data = entry[0], entry[1]
                kind = entry[2] if len(entry) > 2 else FILE
                if isinstance(data, str):
                    data = data.encode("utf-8")
                if kind == "zipinfo":
                    zf.writestr(name, data)
                    continue
                info = zipfile.ZipInfo(name, date_time=(2026, 9, 1, 0, 0, 0))
                info.extra = (extras or {}).get(name, b"")
                if kind == LINK:
                    info.create_system = 3
                    info.external_attr = 0o120777 << 16
                elif kind == DIR:
                    info.create_system = 0
                    info.external_attr = 0x10
                else:
                    info.create_system = 0
                    info.external_attr = 0
                zf.writestr(info, data, compress_type=compress if kind == FILE else zipfile.ZIP_STORED)
            zf.comment = comment
    return buf.getvalue()


def release_files(version="0.2.0", name=SKILL, extra=None):
    files = {
        "SKILL.md": mini_skill_md(version, name=name).encode("utf-8"),
        "LICENSE": MIT_LICENSE.encode("ascii"),
        "README.md": b"# OKR-Ninja (test copy)\n",
        "install.py": b"# placeholder, not the installer\n",
        "CLAUDE.md": b"# notes for agents\n",
        "references/goodness-rubric.md": b"# Goodness rubric (test copy)\n",
        "references/alignment-taxonomy.md": b"# Alignment taxonomy (test copy)\n",
        "examples/sample-portfolio.md": b"# Sample portfolio (fictional)\n",
    }
    for rel, data in (extra or {}).items():
        if data is None:
            files.pop(rel, None)
        else:
            files[rel] = data if isinstance(data, bytes) else data.encode("utf-8")
    return files


def release_entries(version="0.2.0", name=SKILL, extra=None, prefix=None, links=None):
    """Entries of a small release archive under one top-level folder, with directory entries."""
    prefix = "OKR-Ninja-%s/" % version if prefix is None else prefix
    files = release_files(version, name=name, extra=extra)
    dirs = sorted({"/".join(rel.split("/")[:i]) + "/" for rel in files for i in range(1, rel.count("/") + 1)})
    entries = [(prefix, b"", DIR)] + [(prefix + d, b"", DIR) for d in dirs]
    entries += [(prefix + rel, files[rel]) for rel in sorted(files)]
    for rel, target in (links or {}).items():
        entries.append((prefix + rel, target.encode("utf-8"), LINK))
    return entries


def release_payload(version="0.2.0", name=SKILL, extra=None):
    return payload_of(release_files(version, name=name, extra=extra))


def entry_offsets(blob, name):
    """(local header offset, [central directory record offsets]) of an entry."""
    raw = name.encode("utf-8")
    eocd = blob.rfind(b"PK\x05\x06")
    cd_size, cd_off = struct.unpack_from("<II", blob, eocd + 12)
    local, central, pos = None, [], cd_off
    while pos < cd_off + cd_size:
        assert blob[pos:pos + 4] == b"PK\x01\x02", "not a central directory record"
        nlen, xlen, clen = struct.unpack_from("<HHH", blob, pos + 28)
        if blob[pos + 46:pos + 46 + nlen] == raw:
            central.append(pos)
            local = struct.unpack_from("<I", blob, pos + 42)[0]
        pos += 46 + nlen + xlen + clen
    assert central, "entry %r not found" % name
    return local, central


def patch_entry(blob, name, flags=0, method=None):
    """Set general-purpose flag bits and/or the compression method of an entry, in both its
    local header and its central directory record."""
    b = bytearray(blob)
    local, central = entry_offsets(blob, name)
    for off, flag_at, method_at in [(local, 6, 8)] + [(c, 8, 10) for c in central]:
        if flags:
            struct.pack_into("<H", b, off + flag_at, struct.unpack_from("<H", b, off + flag_at)[0] | flags)
        if method is not None:
            struct.pack_into("<H", b, off + method_at, method)
    return bytes(b)


def alias_entry(blob, name, alias):
    """Add a central-directory record named `alias` that points at `name`'s local header, so
    two records share one entry's data."""
    _, central = entry_offsets(blob, name)
    pos = central[0]
    nlen, xlen, clen = struct.unpack_from("<HHH", blob, pos + 28)
    new = alias.encode("utf-8")
    record = bytearray(blob[pos:pos + 46] + new + blob[pos + 46 + nlen:pos + 46 + nlen + xlen + clen])
    struct.pack_into("<H", record, 28, len(new))
    eocd = blob.rfind(b"PK\x05\x06")
    on_disk, total, cd_size, cd_off = struct.unpack_from("<HHII", blob, eocd + 8)
    end = cd_off + cd_size
    out = bytearray(blob[:end] + bytes(record) + blob[end:])
    struct.pack_into("<HHI", out, eocd + len(record) + 8, on_disk + 1, total + 1, cd_size + len(record))
    return bytes(out)


def entry_data_span(blob, name):
    local, _ = entry_offsets(blob, name)
    nlen, xlen = struct.unpack_from("<HH", blob, local + 26)
    info = zipfile.ZipFile(io.BytesIO(blob)).getinfo(name)
    start = local + 30 + nlen + xlen
    return start, start + info.compress_size


def read_skill_package(path):
    with zipfile.ZipFile(str(path)) as zf:
        names = zf.namelist()
        outside = [n for n in names if not n.startswith(SKILL + "/")]
        files = {n[len(SKILL) + 1:]: zf.read(n) for n in names
                 if n.startswith(SKILL + "/") and not n.endswith("/")}
    return files, outside


def read_plugin_package(path):
    prefix = "skills/%s/" % SKILL
    with zipfile.ZipFile(str(path)) as zf:
        names = zf.namelist()
        manifest = json.loads(zf.read(".claude-plugin/plugin.json").decode("utf-8"))
        files = {n[len(prefix):]: zf.read(n) for n in names if n.startswith(prefix) and not n.endswith("/")}
        outside = [n for n in names if n != ".claude-plugin/plugin.json" and not n.startswith(prefix)]
    return manifest, files, outside


# ---------------------------------------------------------------------------------------------
# The fake GitHub behind the real redirect handler
# ---------------------------------------------------------------------------------------------

class FakeResponse(urllib.response.addinfourl):
    """An addinfourl carrying what urllib's HTTPErrorProcessor reads (msg) and a getheader()."""

    def __init__(self, fp, headers, url, code, reason):
        urllib.response.addinfourl.__init__(self, fp, headers, url, code)
        self.msg = reason
        self.reason = reason

    def getheader(self, name, default=None):
        return self.headers.get(name, default)


def respond(req, code=200, body=b"", headers=None):
    msg = email.message.Message()
    for k, v in (headers or {}).items():
        msg[k] = v
    if isinstance(body, bytes):
        if "Content-Length" not in msg:
            msg["Content-Length"] = str(len(body))
        fp = io.BytesIO(body)
    else:
        fp = body
    return FakeResponse(fp, msg, req.full_url, code, http.client.responses.get(code, "Unknown"))


def redirect(code, location):
    return ("redirect", code, location)


def status(code):
    return ("status", code)


class FakeGitHub(urllib.request.BaseHandler):
    """Serves routes {url: bytes | redirect(...) | status(...) | callable(req)}; records every
    request. Unrouted github.com release-tag pages answer 200; anything else answers 404.
    http_open is defined too, so no request can ever reach the network."""
    handler_order = 100

    def __init__(self, routes=None):
        self.routes = dict(routes or {})
        self.requests = []
        self.reqs = []

    def https_open(self, req):
        return self._serve(req)

    def http_open(self, req):
        return self._serve(req)

    def _serve(self, req):
        url = req.full_url
        self.requests.append(url)
        self.reqs.append(req)
        route = self.routes.get(url)
        if route is None:
            parts = urllib.parse.urlsplit(url)
            if parts.scheme == "https" and parts.netloc == "github.com" and "/releases/tag/" in parts.path:
                return respond(req, 200, b"<html>release page</html>")
            return respond(req, 404, b"Not Found")
        if callable(route):
            return route(req)
        if isinstance(route, bytes):
            return respond(req, 200, route)
        if route[0] == "redirect":
            return respond(req, route[1], b"", {"Location": route[2]})
        return respond(req, route[1], b"")


def github_routes(latest=None, archives=None, repo=SLUG):
    """/releases/latest redirects to the tag page of `latest` (absent: 404); each archive URL
    redirects to codeload, which serves the zip bytes."""
    routes = {}
    if latest is not None:
        routes[latest_url(repo)] = redirect(302, tag_page_url(latest, repo))
    for tag, blob in (archives or {}).items():
        routes[archive_url(tag, repo)] = redirect(302, codeload_url(tag, repo))
        routes[codeload_url(tag, repo)] = blob
    return routes


class BreakingBody(io.RawIOBase):
    """A response body that delivers `head` and then breaks like a dropped connection."""

    def __init__(self, head):
        io.RawIOBase.__init__(self)
        self.head, self.pos = head, 0

    def readable(self):
        return True

    def readinto(self, b):
        if self.pos < len(self.head):
            n = min(len(b), len(self.head) - self.pos)
            b[:n] = self.head[self.pos:self.pos + n]
            self.pos += n
            return n
        raise http.client.IncompleteRead(bytes(self.head), 4096)


class ZeroStream(io.RawIOBase):
    """A response body of `size` zero bytes, produced lazily."""

    def __init__(self, size):
        io.RawIOBase.__init__(self)
        self.left = size

    def readable(self):
        return True

    def readinto(self, b):
        n = min(len(b), self.left)
        b[:n] = bytes(n)
        self.left -= n
        return n


# ---------------------------------------------------------------------------------------------
# Base test case
# ---------------------------------------------------------------------------------------------

Result = collections.namedtuple("Result", "code out err fake")


class InstallerCase(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.m = installer()

    def setUp(self):
        self.tmp = Path(self.mkdtemp("case"))
        self.home = self.tmp / "home"
        self.home.mkdir()
        self.cwd = self.tmp / "cwd"
        self.cwd.mkdir()
        self.systmp = Path(self.mkdtemp("systmp"))
        self.addCleanup(lambda: self.assertEqual(snapshot(self.systmp), {},
                                                 "install.py wrote into the system temp folder"))
        patcher = mock.patch.object(tempfile, "tempdir", str(self.systmp))
        patcher.start()
        self.addCleanup(patcher.stop)

    # -- scratch -------------------------------------------------------------------------------

    def mkdtemp(self, prefix="t"):
        d = os.path.realpath(tempfile.mkdtemp(prefix=prefix + "-", dir=scratch_root()))
        self.addCleanup(force_rmtree, d)
        return d

    def fresh(self):
        """A new (home, cwd) pair, for subtests that each must start clean."""
        base = Path(self.mkdtemp("sub"))
        (base / "home").mkdir()
        (base / "cwd").mkdir()
        return base / "home", base / "cwd"

    def targets(self, home=None):
        home = Path(home or self.home)
        return [home / ".claude" / "skills" / SKILL, home / ".agents" / "skills" / SKILL]

    def write_zip(self, blob_or_entries, name="release.zip"):
        blob = blob_or_entries if isinstance(blob_or_entries, bytes) else zip_bytes(blob_or_entries)
        path = Path(self.mkdtemp("zip")) / name
        path.write_bytes(blob)
        return path

    def mini_release(self, version="0.2.0", name=SKILL, extra=None, prefix=None):
        """(path of a small crafted release zip, its expected payload)."""
        path = self.write_zip(release_entries(version, name=name, extra=extra, prefix=prefix),
                              "okr-ninja-%s.zip" % version)
        return path, release_payload(version, name=name, extra=extra)

    # -- running install.py ----------------------------------------------------------------

    def opener(self, *handlers):
        """make_opener() built without proxies from the real environment."""
        with mock.patch.dict(os.environ):
            for k in PROXY_VARS:
                os.environ.pop(k, None)
            return self.m.make_opener(*handlers)

    def run_main(self, argv, handler=None, script_file=None, home=None, cwd=None):
        """Call main(argv) in-process: remote unless script_file names a checkout's install.py,
        HOME/USERPROFILE set to a scratch home, cwd a scratch folder, every request served by
        `handler` (default: a FakeGitHub with no routes)."""
        m = self.m
        fake = handler if handler is not None else FakeGitHub()
        home = str(home or self.home)
        cwd = str(cwd or self.cwd)
        out, err = io.StringIO(), io.StringIO()
        old_cwd = os.getcwd()
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.dict(os.environ, {"HOME": home, "USERPROFILE": home}))
            for k in PROXY_VARS:
                os.environ.pop(k, None)
            stack.enter_context(mock.patch.object(m, "SCRIPT_FILE",
                                                  None if script_file is None else str(script_file)))
            stack.enter_context(mock.patch.object(m, "_extra_handlers", (fake,)))
            stack.enter_context(mock.patch.object(sys, "argv", [str(script_file) if script_file else "-"]))
            stack.enter_context(contextlib.redirect_stdout(out))
            stack.enter_context(contextlib.redirect_stderr(err))
            os.chdir(cwd)
            stack.callback(os.chdir, old_cwd)
            try:
                code = m.main([str(a) for a in argv])
            except SystemExit as e:
                code = e.code if isinstance(e.code, int) else 1
        return Result(code, out.getvalue(), err.getvalue(), fake)

    def run_script(self, script=None, args=(), piped=False, cwd=None, home=None, timeout=120):
        """Run install.py as a subprocess in isolated mode: `python -I <script> args`, or with
        piped=True the documented `python -I - args` with install.py's bytes on stdin. Proxies
        point at a closed local port, so any request fails fast instead of reaching a network."""
        env = {k: v for k, v in os.environ.items() if k not in PROXY_VARS and not k.startswith("PYTHON")}
        env["HOME"] = env["USERPROFILE"] = str(home or self.home)
        for k in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy"):
            env[k] = CLOSED_PROXY
        for k in ("TMPDIR", "TEMP", "TMP"):
            env[k] = str(self.systmp)
        cmd = [sys.executable, "-I"] + (["-"] if piped else [str(script)]) + [str(a) for a in args]
        try:
            p = subprocess.run(cmd, input=INSTALL_PY.read_bytes() if piped else b"",
                               cwd=str(cwd or self.cwd), env=env, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=timeout)
        except subprocess.TimeoutExpired:
            self.fail("%s did not finish within %ss" % (" ".join(cmd), timeout))
        return Result(p.returncode, p.stdout.decode("utf-8", "replace"),
                      p.stderr.decode("utf-8", "replace"), None)

    # -- assertions --------------------------------------------------------------------------

    def assertOk(self, r):
        self.assertEqual(r.code, 0, "exit %s\nstdout:\n%s\nstderr:\n%s" % (r.code, r.out, r.err))

    def assertRefusedRun(self, r, *needles):
        self.assertEqual(r.code, 1, "expected exit 1\nstdout:\n%s\nstderr:\n%s" % (r.out, r.err))
        self.assertNotIn("Traceback", r.err)
        for n in needles:
            self.assertIn(n, r.err)

    def assertNothingWritten(self, home=None, cwd=None):
        self.assertEqual(home_snapshot(home or self.home), {}, "something was written under HOME")
        self.assertEqual(snapshot(cwd or self.cwd), {}, "something was written in the current folder")

    def assertArchiveRefused(self, blob, *needles, **kw):
        """read_archive refuses the bytes, and an install from them exits 1 naming the problem,
        in escaped (ASCII) form, and writes nothing."""
        forbidden = kw.get("forbidden", ())
        if not isinstance(blob, bytes):
            blob = zip_bytes(blob)
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.read_archive(blob)
        message = str(cm.exception)
        for n in needles:
            self.assertIn(n, message)
        for f in forbidden:
            self.assertNotIn(f, message)
        home, cwd = self.fresh()
        path = self.write_zip(blob)
        r = self.run_main(["install", "--source", path], home=home, cwd=cwd)
        self.assertRefusedRun(r, *needles)
        self.assertTrue(r.err.isascii(), "archive-derived names must be printed escaped: %r" % r.err)
        for f in forbidden:
            self.assertNotIn(f, r.err + r.out)
        self.assertNothingWritten(home, cwd)

    def assertHoldsExactly(self, target, expected):
        target = Path(target)
        self.assertTrue(target.is_dir() and not target.is_symlink(), "%s is not a real directory" % target)
        files, links = {}, []
        for dirpath, dirnames, filenames in os.walk(str(target)):
            for n in dirnames + filenames:
                if os.path.islink(os.path.join(dirpath, n)):
                    links.append(os.path.join(dirpath, n))
            for n in filenames:
                p = Path(dirpath, n)
                if not p.is_symlink():
                    files[p.relative_to(target).as_posix()] = p.read_bytes()
        self.assertEqual(links, [], "symlinks in %s" % target)
        self.assertEqual(sorted(files), sorted(expected), "files in %s" % target)
        for rel in expected:
            self.assertEqual(files[rel], expected[rel], "content of %s in %s" % (rel, target))

    def assertInstalled(self, out, version, target, was, nfiles=None):
        pattern = r"installed okr-ninja %s \((\d+) files\) -> %s \(%s\)" % (
            re.escape(version), re.escape(str(target)), re.escape(was))
        m = re.search(pattern, out)
        self.assertIsNotNone(m, "no line installing %s at %s (%s) in:\n%s" % (version, target, was, out))
        if nfiles is not None:
            self.assertEqual(int(m.group(1)), nfiles)

    def assertPackages(self, out_dir, expected, version):
        files, outside = read_skill_package(Path(out_dir) / (SKILL + ".skill"))
        self.assertEqual(outside, [], "entries outside okr-ninja/ in the .skill")
        self.assertEqual(files, expected)
        manifest, pfiles, poutside = read_plugin_package(Path(out_dir) / (SKILL + ".plugin"))
        self.assertEqual(poutside, [], "unexpected entries in the .plugin")
        self.assertEqual(pfiles, expected)
        self.assertEqual(manifest.get("name"), SKILL)
        self.assertEqual(manifest.get("version"), version)
        self.assertTrue(isinstance(manifest.get("description"), str) and manifest["description"].strip())


# =============================================================================================
# The installer is tested offline on every change: Python 3.8 grammar, no newer APIs, ASCII
# =============================================================================================

NEWER_THAN_38 = (
    ("str.removeprefix (3.9)", r"\.\s*removeprefix\b"),
    ("str.removesuffix (3.9)", r"\.\s*removesuffix\b"),
    ("functools.cache (3.9)", r"\bfunctools\s*\.\s*cache\b"),
    ("from functools import cache (3.9)", r"\bfrom\s+functools\s+import\b[^\n]*\bcache\b"),
    ("zoneinfo (3.9)", r"\bzoneinfo\b"),
    ("graphlib (3.9)", r"\bgraphlib\b"),
    ("tomllib (3.11)", r"\btomllib\b"),
    ("PurePath.is_relative_to (3.9)", r"\bis_relative_to\b"),
    ("PurePath.with_stem (3.9)", r"\bwith_stem\b"),
    ("Path.hardlink_to (3.10)", r"\bhardlink_to\b"),
    ("math.lcm (3.9)", r"\bmath\s*\.\s*lcm\b"),
    ("random.randbytes (3.9)", r"\brandbytes\b"),
    ("ast.unparse (3.9)", r"\bast\s*\.\s*unparse\b"),
    ("os.waitstatus_to_exitcode (3.9)", r"\bwaitstatus_to_exitcode\b"),
    ("argparse.BooleanOptionalAction (3.9)", r"\bBooleanOptionalAction\b"),
    ("ArgumentParser(exit_on_error=) (3.9)", r"\bexit_on_error\b"),
    ("itertools.pairwise (3.10)", r"\bpairwise\b"),
    ("int.bit_count (3.10)", r"\.\s*bit_count\b"),
    ("zip(strict=) (3.10)", r"\bzip\s*\([^()]*\bstrict\s*="),
    ("ZipFile(metadata_encoding=) (3.11)", r"\bmetadata_encoding\b"),
    ("hashlib.file_digest (3.11)", r"\bfile_digest\b"),
    ("datetime.UTC (3.11)", r"\bdatetime\s*\.\s*UTC\b"),
    ("Path.readlink (3.9)", r"\bPath\s*\.\s*readlink\b|\)\s*\.\s*readlink\s*\("),
)


def code_only(src):
    """install.py's code with comments and string literals blanked, one token per word."""
    skip = {tokenize.COMMENT, tokenize.STRING}
    for name in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END"):
        if hasattr(tokenize, name):
            skip.add(getattr(tokenize, name))
    parts = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type in (tokenize.NEWLINE, tokenize.NL):
            parts.append("\n")
        elif tok.type not in skip:
            parts.append(tok.string)
    return " ".join(parts)


def runtime_typing_newer_than_38(tree):
    """`X | None`-style unions and builtin generics (`list[str]`) evaluated at run time; both
    fail on 3.8. Annotations are exempt only under `from __future__ import annotations`."""
    lazy = any(isinstance(n, ast.ImportFrom) and n.module == "__future__"
               and any(a.name == "annotations" for a in n.names) for n in tree.body)
    in_annotation = set()
    for node in ast.walk(tree):
        anns = []
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            a = node.args
            anns.append(node.returns)
            for arg in list(getattr(a, "posonlyargs", [])) + a.args + a.kwonlyargs + [a.vararg, a.kwarg]:
                if arg is not None:
                    anns.append(arg.annotation)
        elif isinstance(node, ast.AnnAssign):
            anns.append(node.annotation)
        for ann in anns:
            if ann is not None:
                in_annotation.update(id(sub) for sub in ast.walk(ann))
    types = {"str", "int", "float", "bytes", "bool", "list", "dict", "tuple", "set", "frozenset",
             "type", "object", "Path"}
    generics = {"list", "dict", "tuple", "set", "frozenset", "type"}
    hits = []
    for node in ast.walk(tree):
        if lazy and id(node) in in_annotation:
            continue
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            if any(isinstance(side, ast.Dict) or (isinstance(side, ast.Call) and isinstance(side.func, ast.Name)
                                                  and side.func.id == "dict") for side in (node.left, node.right)):
                hits.append("line %d: dict union with | (3.9)" % node.lineno)
            for side in (node.left, node.right):
                if ((isinstance(side, ast.Name) and side.id in types)
                        or (isinstance(side, ast.Constant) and side.value is None)):
                    hits.append("line %d: a type union with |" % node.lineno)
                    break
        if (isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name)
                and node.value.id in generics):
            hits.append("line %d: builtin generic %s[...]" % (node.lineno, node.value.id))
    return hits


class TestInstallerSourceCompatibility(unittest.TestCase):
    """Requirement: The installer is tested offline on every change."""

    @classmethod
    def setUpClass(cls):
        cls.src_bytes = INSTALL_PY.read_bytes()
        cls.src = cls.src_bytes.decode("utf-8")

    def test_install_py_is_pure_ascii(self):
        bad = [(i, b) for i, b in enumerate(self.src_bytes) if b >= 128]
        self.assertEqual(bad[:10], [], "non-ASCII bytes at these offsets")

    def test_install_py_parses_under_python_3_8_grammar(self):
        ast.parse(self.src, filename=str(INSTALL_PY), feature_version=(3, 8))

    def test_install_py_uses_no_standard_library_api_newer_than_3_8(self):
        code = code_only(self.src)
        hits = [label for label, pattern in NEWER_THAN_38 if re.search(pattern, code)]
        self.assertEqual(hits, [])

    def test_install_py_evaluates_no_newer_typing_syntax_at_run_time(self):
        self.assertEqual(runtime_typing_newer_than_38(ast.parse(self.src)), [])

    def test_the_static_checks_catch_what_they_look_for(self):
        """Guard the guards: each check fires on a known 3.9+ construct."""
        self.assertTrue(re.search(NEWER_THAN_38[0][1], code_only("x = 'a'.removeprefix('b')\n")))
        self.assertFalse(re.search(NEWER_THAN_38[0][1], code_only("# 'a'.removeprefix\nx = 1\n")))
        self.assertTrue(runtime_typing_newer_than_38(ast.parse("isinstance(x, int | None)\n")))
        self.assertTrue(runtime_typing_newer_than_38(ast.parse("X = list[str]\n")))
        self.assertFalse(runtime_typing_newer_than_38(ast.parse(
            "from __future__ import annotations\ndef f(a: str | None) -> list[str]: pass\n")))
        self.assertTrue(runtime_typing_newer_than_38(ast.parse("def f(a: str | None): pass\n")))


# =============================================================================================
# The interface the tests rely on
# =============================================================================================

class TestInterface(InstallerCase):

    def test_constants(self):
        m = self.m
        self.assertEqual(m.SKILL_NAME, "okr-ninja")
        self.assertEqual(m.DEFAULT_REPO, "im1tta/OKR-Ninja")
        self.assertEqual(tuple(m.ALLOWED_HOSTS), ("github.com", "codeload.github.com"))
        self.assertEqual(m.MAX_DOWNLOAD, 100 * MB)
        self.assertEqual(m.MAX_PAYLOAD, 20 * MB)
        self.assertEqual(tuple(m.PAYLOAD_DIRS), ("references", "examples"))
        self.assertTrue(issubclass(m.Refusal, Exception))
        self.assertEqual(m._extra_handlers, ())

    def test_script_file_is_the_module_file(self):
        self.assertEqual(os.path.realpath(self.m.SCRIPT_FILE), os.path.realpath(str(INSTALL_PY)))

    def test_make_opener_pins_redirects_and_adds_extra_handlers(self):
        fake = FakeGitHub()
        opener = self.opener(fake)
        self.assertIsInstance(opener, urllib.request.OpenerDirector)
        self.assertTrue(any(isinstance(h, self.m.PinnedRedirects) for h in opener.handlers))
        self.assertFalse(any(type(h) is urllib.request.HTTPRedirectHandler for h in opener.handlers))
        self.assertIn(fake, opener.handlers)

    def test_archive_url(self):
        self.assertEqual(self.m.archive_url(SLUG, "v0.2.0"), archive_url("v0.2.0"))
        url = self.m.archive_url(SLUG, "v1.0.0-rc.1+build.5")
        self.assertNotIn("+", url, "the tag is percent-quoted")
        self.assertEqual(urllib.parse.unquote(url), archive_url("v1.0.0-rc.1+build.5"))

    def test_unknown_command_arguments_do_not_traceback(self):
        r = self.run_main(["install", "--only", "nowhere"])
        self.assertNotEqual(r.code, 0)
        self.assertNotIn("Traceback", r.err)
        self.assertNothingWritten()

    def test_usage_errors_print_the_command_line_escaped(self):
        # argparse echoes unrecognized arguments as given; they pass the same print filter
        r = self.run_main(["install", "rel\u202eeas", "\x1b[31mred"])
        self.assertEqual(r.code, 2)
        self.assertIn("unrecognized arguments", r.err)
        self.assertNotIn("\u202e", r.err)
        self.assertNotIn("\x1b", r.err)
        self.assertIn("rel\\u202eeas \\x1b[31mred", r.err)
        self.assertNothingWritten()


# =============================================================================================
# Requirement: The frontmatter check keeps the skill uploadable (metadata.version)
# =============================================================================================

class TestFrontmatterVersion(InstallerCase):

    VALID = ("0.2.0", "0.0.0", "10.20.30", "1.0.0-rc.1+build.5", "1.0.0-alpha", "1.0.0+20260924",
             "2.0.0-x-y.1")
    MALFORMED = {
        "0.2 (quoted)": '"0.2"',
        "0.2 (plain)": "0.2",
        "v0.2.0 (quoted)": '"v0.2.0"',
        "v0.2.0 (plain)": "v0.2.0",
        "01.2.0 (quoted)": '"01.2.0"',
        "1.02.0": '"1.02.0"',
        "1.2.03": '"1.2.03"',
        "1.2.3.4": '"1.2.3.4"',
        "empty": '""',
    }

    def test_valid_semantic_versions_pass(self):
        for v in self.VALID:
            with self.subTest(version=v):
                name, description, version, errors = self.m.check_skill_text(mini_skill_md(v))
                self.assertEqual(errors, [])
                self.assertEqual((name, version), (SKILL, v))
                self.assertTrue(description)

    def test_scenario_a_missing_or_malformed_version_fails_the_check(self):
        cases = dict(("version " + k, mini_skill_md(raw_version=v)) for k, v in self.MALFORMED.items())
        cases["no metadata"] = mini_skill_md(None)
        cases["metadata without version"] = mini_skill_md(None).replace(
            "license: MIT\n", "license: MIT\nmetadata:\n  author: someone\n")
        for label, text in cases.items():
            with self.subTest(label):
                errors = self.m.check_skill_text(text)[3]
                self.assertTrue(any("metadata.version" in e for e in errors),
                                "no error naming metadata.version: %r" % (errors,))

    def test_check_skill_reads_a_folder(self):
        root = write_files(self.tmp / "skill", {"SKILL.md": mini_skill_md("0.3.1")})
        self.assertEqual(self.m.check_skill(root), (SKILL, MINI_DESCRIPTION, "0.3.1", []))

    def test_check_skill_accepts_crlf_line_ends(self):
        root = write_files(self.tmp / "skill", {"SKILL.md": mini_skill_md("0.2.0").replace("\n", "\r\n")})
        name, _, version, errors = self.m.check_skill(root)
        self.assertEqual((name, version, errors), (SKILL, "0.2.0", []))

    @posix_only
    def test_check_skill_refuses_a_symlinked_skill_md(self):
        root = write_files(self.tmp / "skill", {"real.md": mini_skill_md("0.2.0")})
        os.symlink("real.md", str(root / "SKILL.md"))
        self.assertTrue(self.m.check_skill(root)[3])

    def test_version_in_reads_the_version_and_never_raises(self):
        self.assertEqual(self.m.version_in(mini_skill_md("0.3.0")), "0.3.0")
        self.assertIsNone(self.m.version_in(mini_skill_md(None)))
        for text in ("", "---", "---\n---\n", "no frontmatter at all", "\x00\x01\x02",
                     "\ufeff---\nmetadata:\n  version: \"0.2.0\"\n---\n", "---\nmetadata: 0.2.0\n---\n",
                     "---\nmetadata:\n\tversion: 0.2.0\n---\n", "---\nmetadata:\n  version: [0.2\n---\n",
                     "---\nname: x\n" + "y" * 100000):
            with self.subTest(text=text[:40]):
                v = self.m.version_in(text)
                self.assertTrue(v is None or isinstance(v, str))

    def test_scenario_the_shipped_skill_passes(self):
        version = working_version()
        self.assertIsNotNone(version, "the repo's SKILL.md carries no metadata.version")
        name, _, checked, errors = self.m.check_skill(REPO_ROOT)
        self.assertEqual((name, checked, errors), (SKILL, version, []))
        r = self.run_script(INSTALL_PY, ["check"])
        self.assertOk(r)
        self.assertIn("ok: okr-ninja %s" % version, r.out)
        self.assertRegex(r.out, r"ok: okr-ninja %s, description [\d,]+/1,024 characters" % re.escape(version))
        self.assertEqual(home_snapshot(self.home), {})

    def test_check_success_prints_name_and_version_from_a_checkout(self):
        co = make_tree(self.tmp / "co", "1.2.3-rc.1+b.7")
        r = self.run_script(co / "install.py", ["check"])
        self.assertOk(r)
        self.assertRegex(r.out, r"ok: okr-ninja 1\.2\.3-rc\.1\+b\.7, description [\d,]+/1,024 characters")

    def test_scenario_a_missing_or_malformed_version_blocks_check_build_and_install(self):
        for label, kwargs in (("missing", dict(version=DROP)), ("0.2", dict(raw_version='"0.2"')),
                              ("v0.2.0", dict(raw_version='"v0.2.0"')), ("01.2.0", dict(raw_version='"01.2.0"'))):
            with self.subTest(label):
                home, cwd = self.fresh()
                co = make_tree(Path(self.mkdtemp("co")) / "co", **kwargs)
                before = snapshot(co)
                r = self.run_script(co / "install.py", ["check"], home=home, cwd=cwd)
                self.assertEqual(r.code, 1)
                self.assertIn("metadata.version", r.out + r.err)
                r = self.run_script(co / "install.py", ["build"], home=home, cwd=cwd)
                self.assertRefusedRun(r, "metadata.version")
                r = self.run_script(co / "install.py", ["install"], home=home, cwd=cwd)
                self.assertRefusedRun(r, "metadata.version")
                self.assertEqual(snapshot(co), before)
                self.assertNothingWritten(home, cwd)

    def test_scenario_an_over_long_description_blocks_packaging_and_install(self):
        co = make_tree(self.tmp / "co", "0.2.0", description="A" * 1025)
        before = snapshot(co)
        r = self.run_script(co / "install.py", ["check"])
        self.assertEqual(r.code, 1)
        self.assertIn("1,025", r.out + r.err)
        self.assertIn("1,024", r.out + r.err)
        self.assertRefusedRun(self.run_script(co / "install.py", ["build"]))
        self.assertRefusedRun(self.run_script(co / "install.py", ["build", "--out", self.tmp / "out"]))
        self.assertRefusedRun(self.run_script(co / "install.py", ["install"]))
        self.assertEqual(snapshot(co), before)
        self.assertFalse((self.tmp / "out").exists())
        self.assertNothingWritten()

    def test_a_remote_payload_gets_the_same_check(self):
        cases = (
            ("no version", dict(extra={"SKILL.md": mini_skill_md(None)}), "metadata.version"),
            ("long description", dict(extra={"SKILL.md": mini_skill_md("0.2.0", description="A" * 1025)}), "1,024"),
        )
        for label, kwargs, needle in cases:
            with self.subTest(label):
                path, _ = self.mini_release("0.2.0", **kwargs)
                for command in ("install", "build", "check"):
                    home, cwd = self.fresh()
                    r = self.run_main([command, "--source", path], home=home, cwd=cwd)
                    self.assertEqual(r.code, 1, (command, r.out, r.err))
                    self.assertIn(needle, r.out + r.err)
                    self.assertNothingWritten(home, cwd)


# =============================================================================================
# Requirement: The runtime payload is the whole shipment
# =============================================================================================

class TestRuntimePayload(InstallerCase):

    def install_and_build(self, co):
        r = self.run_script(co / "install.py", ["install"])
        self.assertOk(r)
        out = self.tmp / "out"
        b = self.run_script(co / "install.py", ["build", "--out", out])
        self.assertOk(b)
        return out

    def test_scenario_development_files_never_ship(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        expected = expected_payload(co)
        self.assertIn("LICENSE", expected)
        for dev in ("CLAUDE.md", "README.md", "install.py", "tests/test_x.py", "evals/x.md",
                    "openspec/o.md", ".claude/y.md", "dist/okr-ninja.skill"):
            self.assertTrue((co / dev).exists(), dev)
        out = self.install_and_build(co)
        for t in self.targets():
            self.assertHoldsExactly(t, expected)
        self.assertPackages(out, expected, "0.2.0")

    def test_scenario_os_noise_is_dropped(self):
        co = make_tree(self.tmp / "co", "0.2.0", extra={"examples/.DS_Store": b"\x00\x00\x00\x01Bud1",
                                                          "references/sub/.DS_Store": b"Bud1",
                                                          "examples/desktop.ini": b"[.ShellClassInfo]"})
        out = self.install_and_build(co)
        installed = [p.relative_to(t).as_posix() for t in self.targets() for p in t.rglob("*")]
        packaged = list(read_skill_package(out / "okr-ninja.skill")[0]) + list(read_plugin_package(out / "okr-ninja.plugin")[1])
        for rel in installed + packaged:
            name = rel.split("/")[-1]
            self.assertFalse(name.startswith(".") or name.lower() in ("thumbs.db", "desktop.ini")
                             or name.endswith(".pyc") or "__pycache__" in rel, rel)

    def test_scenario_a_checkout_without_its_license_refuses(self):
        co = make_tree(self.tmp / "co", "0.2.0", license=False)
        before = snapshot(co)
        for args in (["install"], ["build"], ["build", "--out", self.tmp / "out"]):
            with self.subTest(args=args[:1]):
                self.assertRefusedRun(self.run_script(co / "install.py", args), "LICENSE")
        self.assertEqual(snapshot(co), before)
        self.assertFalse((self.tmp / "out").exists())
        self.assertNothingWritten()

    @posix_only
    def test_a_symlinked_license_is_never_read(self):
        co = make_tree(self.tmp / "co", "0.2.0", license=False)
        os.symlink("README.md", str(co / "LICENSE"))
        self.assertRefusedRun(self.run_script(co / "install.py", ["install"]), "LICENSE")
        self.assertRefusedRun(self.run_script(co / "install.py", ["build", "--out", self.tmp / "out"]), "LICENSE")
        self.assertFalse((self.tmp / "out").exists())
        self.assertNothingWritten()

    @needs_permissions
    def test_an_unreadable_folder_stops_the_build_and_the_install(self):
        co = make_tree(self.tmp / "co", "0.2.0", extra={"references/sub/x.md": b"x\n"})
        os.chmod(str(co / "references" / "sub"), 0)
        self.assertRefusedRun(self.run_script(co / "install.py", ["install"]))
        self.assertRefusedRun(self.run_script(co / "install.py", ["build", "--out", self.tmp / "out"]))
        self.assertFalse((self.tmp / "out").exists() and any((self.tmp / "out").iterdir()))
        self.assertNothingWritten()

    @needs_permissions
    def test_an_unreadable_file_stops_the_run_before_any_folder_is_created(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        os.chmod(str(co / "examples" / "sample-portfolio.md"), 0)
        self.assertRefusedRun(self.run_script(co / "install.py", ["install"]))
        self.assertNothingWritten()


# =============================================================================================
# Requirement: Built packages for upload and plugin hosts
# =============================================================================================

class TestBuiltPackages(InstallerCase):
    VERSION = "1.2.3-rc.1+b.7"  # not any constant in install.py: plugin.json must copy SKILL.md's

    def build(self, co, out):
        r = self.run_script(co / "install.py", ["build", "--out", out])
        self.assertOk(r)
        return r

    def test_scenario_skill_archive_layout(self):
        co = make_tree(self.tmp / "co", self.VERSION)
        self.build(co, self.tmp / "out")
        files, outside = read_skill_package(self.tmp / "out" / "okr-ninja.skill")
        self.assertEqual(outside, [])
        self.assertEqual(files, expected_payload(co))

    def test_scenario_plugin_archive_layout(self):
        co = make_tree(self.tmp / "co", self.VERSION)
        r = self.build(co, self.tmp / "out")
        self.assertPackages(self.tmp / "out", expected_payload(co), self.VERSION)
        self.assertIn("wrote %s" % (self.tmp / "out" / "okr-ninja.skill"), r.out)
        self.assertIn("wrote %s" % (self.tmp / "out" / "okr-ninja.plugin"), r.out)

    def test_scenario_rebuilds_are_reproducible(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        self.build(co, self.tmp / "b1")
        self.build(co, self.tmp / "b2")
        for name in ("okr-ninja.skill", "okr-ninja.plugin"):
            self.assertEqual((self.tmp / "b1" / name).read_bytes(), (self.tmp / "b2" / name).read_bytes(), name)

    def test_a_checkout_build_defaults_to_dist_and_replaces_previous_copies(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        r = self.run_script(co / "install.py", ["build"])
        self.assertOk(r)
        self.assertIn("reading the checkout at %s" % co, r.out)
        self.assertPackages(co / "dist", expected_payload(co), "0.2.0")
        self.assertNothingWritten()

    def test_an_empty_out_is_refused(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        before = snapshot(co)
        self.assertRefusedRun(self.run_script(co / "install.py", ["build", "--out", ""]))
        self.assertEqual(snapshot(co), before)
        self.assertNothingWritten()

    def test_the_repo_checkout_builds_its_own_payload(self):
        """The real checkout also holds CLAUDE.md, README.md, tests/, evals/, openspec/, .claude/."""
        out = self.tmp / "out"
        r = self.run_script(INSTALL_PY, ["build", "--out", out])
        self.assertOk(r)
        self.assertIn("reading the checkout at %s" % REPO_ROOT, r.out)
        self.assertPackages(out, expected_payload(REPO_ROOT), working_version())


# =============================================================================================
# Requirement: Installer targets
# =============================================================================================

class TestInstallerTargets(InstallerCase):

    def test_scenario_default_install_covers_the_folder_reading_platforms(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        expected = expected_payload(co)
        r = self.run_script(co / "install.py", [])
        self.assertOk(r)
        self.assertIn("reading the checkout at %s" % co, r.out)
        for t in self.targets():
            self.assertTrue((t / "SKILL.md").is_file())
            self.assertHoldsExactly(t, expected)
            self.assertInstalled(r.out, "0.2.0", t, "new install", len(expected))
        top = {rel.split("/")[0] for rel in home_snapshot(self.home)}
        self.assertEqual(top, {".claude", ".agents"})

    def test_scenario_project_install(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        project = self.tmp / "project"
        project.mkdir()
        r = self.run_script(co / "install.py", ["install", "--project", project])
        self.assertOk(r)
        for t in self.targets(project):
            self.assertHoldsExactly(t, expected_payload(co))
            self.assertIn(str(t), r.out)
        self.assertEqual(home_snapshot(self.home), {})

    def test_a_project_that_is_not_an_existing_directory_is_refused(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        a_file = self.tmp / "a-file"
        a_file.write_text("x")
        for value in (str(self.tmp / "missing"), "", str(a_file)):
            with self.subTest(project=value):
                self.assertRefusedRun(self.run_script(co / "install.py", ["install", "--project", value]))
        self.assertFalse((self.tmp / "missing").exists())
        self.assertNothingWritten()

    def test_scenario_one_target_only(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        r = self.run_script(co / "install.py", ["install", "--only", "agents"])
        self.assertOk(r)
        claude, agents = self.targets()
        self.assertHoldsExactly(agents, expected_payload(co))
        self.assertFalse(os.path.lexists(str(claude)))
        self.assertFalse((self.home / ".claude").exists())

    def test_only_claude(self):
        path, payload = self.mini_release("0.2.0")
        r = self.run_main(["install", "--only", "claude", "--source", path])
        self.assertOk(r)
        claude, agents = self.targets()
        self.assertHoldsExactly(claude, payload)
        self.assertFalse((self.home / ".agents").exists())

    def test_scenario_install_output_reports_the_version_change(self):
        z2, _ = self.mini_release("0.2.0")
        z3, p3 = self.mini_release("0.3.0")
        self.assertOk(self.run_main(["install", "--only", "claude", "--source", z2]))
        r = self.run_main(["install", "--source", z3])
        self.assertOk(r)
        claude, agents = self.targets()
        self.assertInstalled(r.out, "0.3.0", claude, "was 0.2.0", len(p3))
        self.assertInstalled(r.out, "0.3.0", agents, "new install", len(p3))
        for t in self.targets():
            self.assertHoldsExactly(t, p3)

    def test_scenario_an_install_from_before_versioning(self):
        claude = self.targets()[0]
        write_files(claude, {"SKILL.md": mini_skill_md(None), "references/old.md": "old\n"})
        path, payload = self.mini_release("0.2.0")
        r = self.run_main(["install", "--only", "claude", "--source", path])
        self.assertOk(r)
        self.assertInstalled(r.out, "0.2.0", claude, "was unversioned", len(payload))
        self.assertHoldsExactly(claude, payload)

    @unittest.skipUnless(POSIX and os.path.exists("/dev/zero"), "needs /dev/zero")
    def test_a_skill_md_symlinked_to_dev_zero_is_unversioned_and_replaced(self):
        claude = self.targets()[0]
        claude.mkdir(parents=True)
        os.symlink("/dev/zero", str(claude / "SKILL.md"))
        path, payload = self.mini_release("0.2.0")
        r = call_with_timeout(lambda: self.run_main(["install", "--only", "claude", "--source", path]))
        self.assertOk(r)
        self.assertInstalled(r.out, "0.2.0", claude, "was unversioned")
        self.assertHoldsExactly(claude, payload)


class TestPreviousVersion(InstallerCase):
    """Design D9: read the previous copy's version defensively before the swap."""

    def pv(self, target):
        return call_with_timeout(lambda: self.m.previous_version(Path(target)))

    def test_no_target_is_a_new_install(self):
        self.assertEqual(self.pv(self.tmp / "absent"), "new install")

    def test_a_versioned_copy(self):
        t = write_files(self.tmp / "t", {"SKILL.md": mini_skill_md("0.2.0")})
        self.assertEqual(self.pv(t), "was 0.2.0")

    def test_a_crlf_copy_still_reports_its_version(self):
        t = write_files(self.tmp / "t", {"SKILL.md": mini_skill_md("0.2.0").replace("\n", "\r\n")})
        self.assertEqual(self.pv(t), "was 0.2.0")

    def test_unversioned_copies(self):
        cases = {
            "no frontmatter": {"SKILL.md": "# OKR-Ninja\n\nNo frontmatter.\n"},
            "no metadata.version": {"SKILL.md": mini_skill_md(None)},
            "no SKILL.md": {"references/x.md": "x\n"},
            "not UTF-8": {"SKILL.md": b"---\nname: \xff\xfe\n---\n"},
            "SKILL.md is a folder": {"SKILL.md/x.md": "x\n"},
        }
        for label, files in cases.items():
            with self.subTest(label):
                t = write_files(Path(self.mkdtemp("pv")) / "t", files)
                self.assertEqual(self.pv(t), "was unversioned")

    @needs_permissions
    def test_an_unreadable_skill_md_is_unversioned(self):
        t = write_files(self.tmp / "t", {"SKILL.md": mini_skill_md("0.2.0")})
        os.chmod(str(t / "SKILL.md"), 0)
        self.assertEqual(self.pv(t), "was unversioned")

    @unittest.skipUnless(POSIX and os.path.exists("/dev/zero"), "needs /dev/zero")
    def test_a_skill_md_symlinked_to_dev_zero_is_unversioned(self):
        t = self.tmp / "t"
        t.mkdir()
        os.symlink("/dev/zero", str(t / "SKILL.md"))
        self.assertEqual(self.pv(t), "was unversioned")

    @unittest.skipUnless(POSIX, "needs symlinks")
    def test_a_dangling_link_target_is_unversioned(self):
        t = self.tmp / "t"
        os.symlink(str(self.tmp / "nowhere"), str(t))
        self.assertEqual(self.pv(t), "was unversioned")

    @unittest.skipUnless(POSIX, "needs symlinks")
    def test_a_skill_md_linked_to_a_versioned_file_reports_its_version(self):
        (self.tmp / "real.md").write_text(mini_skill_md("0.2.0"))
        t = self.tmp / "t"
        t.mkdir()
        os.symlink(str(self.tmp / "real.md"), str(t / "SKILL.md"))
        self.assertEqual(self.pv(t), "was 0.2.0")

    def test_a_version_past_64_kb_is_not_read(self):
        padding = "\n".join("# comment line %d" % i for i in range(6000))
        text = "---\nname: okr-ninja\n" + padding + "\nmetadata:\n  version: \"0.2.0\"\n---\n"
        self.assertGreater(len(text.encode()), 64 * 1024)
        t = write_files(self.tmp / "t", {"SKILL.md": text})
        self.assertEqual(self.pv(t), "was unversioned")


# =============================================================================================
# Requirement: Replacing an existing install is safe
# =============================================================================================

class TestReplacementSafety(InstallerCase):

    def test_scenario_stale_files_are_removed(self):
        z2, _ = self.mini_release("0.2.0", extra={"references/old.md": b"gone in 0.3.0\n"})
        z3, p3 = self.mini_release("0.3.0")
        self.assertOk(self.run_main(["install", "--source", z2]))
        r = self.run_main(["install", "--source", z3])
        self.assertOk(r)
        for t in self.targets():
            self.assertHoldsExactly(t, p3)
            self.assertInstalled(r.out, "0.3.0", t, "was 0.2.0")

    @posix_only
    def test_scenario_a_symlinked_checkout_becomes_a_copy(self):
        co = make_tree(self.tmp / "co", "0.1.0")
        before = snapshot(co)
        claude = self.targets()[0]
        claude.parent.mkdir(parents=True)
        os.symlink(str(co), str(claude))
        path, payload = self.mini_release("0.2.0")
        r = self.run_main(["install", "--source", path])
        self.assertOk(r)
        self.assertHoldsExactly(claude, payload)
        self.assertEqual(snapshot(co), before)

    def test_scenario_a_hand_made_folder_beside_the_target_is_never_deleted(self):
        path, payload = self.mini_release("0.2.0")
        self.assertOk(self.run_main(["install", "--source", path]))
        skills = self.targets()[0].parent
        for name in (".okr-ninja.my-backup.previous", ".okr-ninja.20260923.previous"):
            write_files(skills / name, {"keep.md": "keep\n", "sub/keep.md": "keep\n"})
        before = {name: snapshot(skills / name) for name in os.listdir(str(skills)) if name != SKILL}
        self.assertOk(self.run_main(["install", "--source", path]))
        after = {name: snapshot(skills / name) for name in os.listdir(str(skills)) if name != SKILL}
        self.assertEqual(after, before)
        self.assertHoldsExactly(self.targets()[0], payload)

    def test_scenario_a_repository_clone_at_a_target_is_never_deleted(self):
        claude = self.targets()[0]
        write_files(claude, {".git/HEAD": "ref: refs/heads/main\n", "SKILL.md": mini_skill_md("0.1.0")})
        before = home_snapshot(self.home)
        path, _ = self.mini_release("0.2.0")
        r = self.run_main(["install", "--source", path])
        self.assertRefusedRun(r, str(claude))
        self.assertEqual(home_snapshot(self.home), before)

    def test_a_target_that_is_a_file_refuses(self):
        claude = self.targets()[0]
        claude.parent.mkdir(parents=True)
        claude.write_text("not a folder\n")
        before = home_snapshot(self.home)
        path, _ = self.mini_release("0.2.0")
        self.assertRefusedRun(self.run_main(["install", "--source", path]))
        self.assertEqual(home_snapshot(self.home), before)

    def test_scenario_running_from_inside_a_target_refuses(self):
        claude = self.targets()[0]
        make_tree(claude, "0.2.0")
        before = home_snapshot(self.home)
        r = self.run_script(claude / "install.py", ["install"])
        self.assertRefusedRun(r, str(claude))
        self.assertEqual(home_snapshot(self.home), before)

    def test_scenario_a_case_variant_of_the_checkouts_path_still_refuses(self):
        skills = self.home / ".claude" / "skills"
        skills.mkdir(parents=True)
        if not case_insensitive(skills):
            self.skipTest("the scratch disk is case-sensitive")
        co = make_tree(skills / "OKR-Ninja", "0.2.0")
        before = home_snapshot(self.home)
        r = self.run_script(co / "install.py", ["install"])
        self.assertRefusedRun(r, str(skills / "okr-ninja"))
        self.assertEqual(home_snapshot(self.home), before)

    @unittest.skipUnless(hasattr(os, "chflags") and hasattr(stat, "UF_IMMUTABLE"), "needs BSD file flags")
    def test_scenario_an_undeletable_previous_copy_never_leaves_a_broken_install(self):
        z2, _ = self.mini_release("0.2.0")
        z3, p3 = self.mini_release("0.3.0")
        self.assertOk(self.run_main(["install", "--only", "claude", "--source", z2]))
        claude = self.targets()[0]
        try:
            os.chflags(str(claude / "references" / "goodness-rubric.md"), stat.UF_IMMUTABLE)
        except OSError as e:
            self.skipTest("cannot set the immutable flag here: %s" % e)
        r = self.run_main(["install", "--only", "claude", "--source", z3])
        self.assertOk(r)
        self.assertHoldsExactly(claude, p3)
        left = [p for p in claude.parent.iterdir() if p.name != SKILL]
        self.assertEqual(len(left), 1, left)
        self.assertIn(str(left[0]), r.out + r.err)


# =============================================================================================
# Requirement: Remote install from a published release -- checkout detection (design D1)
# =============================================================================================

class TestCheckoutDetection(InstallerCase):

    def checkout_dir(self, readme=True, skill=True):
        co = Path(self.mkdtemp("co"))
        files = {"install.py": INSTALL_PY.read_bytes()}
        if skill:
            files["SKILL.md"] = mini_skill_md("0.2.0")
        if readme:
            files["README.md"] = "# OKR-Ninja\n"
        write_files(co, files)
        return co

    def installed_copy(self, folder):
        """What an installed copy or an unpacked .skill holds (no README.md), plus install.py."""
        write_files(folder, release_payload("0.2.0"))
        (folder / "install.py").write_bytes(INSTALL_PY.read_bytes())
        return folder

    def test_a_real_file_beside_skill_md_and_readme_is_a_checkout(self):
        co = self.checkout_dir()
        script = str(co / "install.py")
        for argv0 in (script, "install.py", "python -m unittest"):
            with self.subTest(argv0=argv0):
                root = self.m.checkout_root(script, argv0)
                self.assertIsNotNone(root)
                self.assertEqual(Path(root).resolve(), co.resolve())

    def test_standard_input_and_command_strings_are_remote(self):
        script = str(self.checkout_dir() / "install.py")
        for file_attr, argv0 in ((None, "-c"), (None, "-"), ("", "x"), ("<stdin>", "-"),
                                 ("<string>", "-c"), (script, "-"), (script, "-c")):
            with self.subTest(file_attr=file_attr, argv0=argv0):
                self.assertIsNone(self.m.checkout_root(file_attr, argv0))

    def test_a_file_literally_named_stdin_does_not_count(self):
        co = self.checkout_dir()
        (co / "<stdin>").write_bytes(INSTALL_PY.read_bytes())
        old = os.getcwd()
        os.chdir(str(co))
        try:
            self.assertIsNone(self.m.checkout_root("<stdin>", "python3"))
        finally:
            os.chdir(old)

    def test_folders_that_are_not_checkouts_are_remote(self):
        cases = {
            "installed copy (no README.md)": self.installed_copy(Path(self.mkdtemp("copy")) / "okr-ninja") / "install.py",
            "no SKILL.md": self.checkout_dir(skill=False) / "install.py",
            "a folder, not a file": self.checkout_dir(),
            "a missing file": self.checkout_dir() / "missing.py",
        }
        for label, path in cases.items():
            with self.subTest(label):
                self.assertIsNone(self.m.checkout_root(str(path), str(path)))

    def test_scenario_a_checkout_run_stays_local(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        fake = FakeGitHub()
        r = self.run_main(["install"], handler=fake, script_file=co / "install.py")
        self.assertOk(r)
        self.assertEqual(fake.requests, [], "a checkout run made a request")
        self.assertIn("reading the checkout at %s" % co, r.out)
        for t in self.targets():
            self.assertHoldsExactly(t, expected_payload(co))
            self.assertInstalled(r.out, "0.2.0", t, "new install")

    def test_checkout_build_and_check_make_no_request(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        fake = FakeGitHub()
        self.assertOk(self.run_main(["check"], handler=fake, script_file=co / "install.py"))
        r = self.run_main(["build", "--out", self.tmp / "out"], handler=fake, script_file=co / "install.py")
        self.assertOk(r)
        self.assertIn("reading the checkout at %s" % co, r.out)
        self.assertEqual(fake.requests, [])
        self.assertPackages(self.tmp / "out", expected_payload(co), "0.2.0")

    def test_a_checkout_run_needs_no_network(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        r = self.run_script(co / "install.py", [])  # proxies point at a closed port
        self.assertOk(r)
        self.assertIn("reading the checkout at %s" % co, r.out)

    def test_remote_options_switch_a_checkout_run_to_remote_mode(self):
        co = make_tree(self.tmp / "co", "0.3.0")
        script = co / "install.py"
        path, payload = self.mini_release("0.2.0")
        # --source
        r = self.run_main(["install", "--only", "claude", "--source", path], script_file=script)
        self.assertOk(r)
        self.assertNotIn("reading the checkout", r.out)
        self.assertHoldsExactly(self.targets()[0], payload)
        # --release
        home, cwd = self.fresh()
        fake = FakeGitHub(github_routes(None, {"v0.2.0": path.read_bytes()}))
        r = self.run_main(["install", "--release", "v0.2.0"], handler=fake, script_file=script, home=home, cwd=cwd)
        self.assertOk(r)
        self.assertEqual(fake.requests, [archive_url("v0.2.0"), codeload_url("v0.2.0")])
        for t in self.targets(home):
            self.assertHoldsExactly(t, payload)
        # --repo
        home, cwd = self.fresh()
        fake = FakeGitHub()
        r = self.run_main(["install", "--repo", "someone/fork"], handler=fake, script_file=script, home=home, cwd=cwd)
        self.assertRefusedRun(r, "someone/fork")
        self.assertEqual(fake.requests, [latest_url("someone/fork")])
        self.assertNothingWritten(home, cwd)

    def test_scenario_a_piped_run_inside_a_checkout_is_remote(self):
        co = make_tree(self.tmp / "co", "0.2.0")
        before = snapshot(co)
        r = self.run_script(None, [], piped=True, cwd=co)
        self.assertRefusedRun(r, latest_url())
        self.assertNotIn("reading the checkout", r.out)
        self.assertEqual(snapshot(co), before)
        self.assertEqual(home_snapshot(self.home), {})

    def test_scenario_a_copy_beside_an_installed_skill_is_remote(self):
        folder = self.installed_copy(self.tmp / "unpacked" / "okr-ninja")
        before = snapshot(folder)
        r = self.run_script(folder / "install.py", [])
        self.assertRefusedRun(r, latest_url())
        self.assertNotIn("reading the checkout", r.out)
        self.assertEqual(snapshot(folder), before)
        self.assertNothingWritten()

    def test_an_installer_saved_inside_a_target_cannot_replace_itself(self):
        claude = self.targets()[0]
        self.installed_copy(claude)
        path, _ = self.mini_release("0.2.0")
        before = home_snapshot(self.home)
        r = self.run_script(claude / "install.py", ["--source", path])
        self.assertRefusedRun(r, str(claude))
        self.assertEqual(home_snapshot(self.home), before)


# =============================================================================================
# Requirement: Remote install -- hosts, schemes, redirects and failures (design D4, D12)
# =============================================================================================

class TestUrlPinning(InstallerCase):
    ALLOWED = (
        "https://github.com/im1tta/OKR-Ninja/releases/latest",
        "https://github.com/im1tta/OKR-Ninja/archive/refs/tags/v0.2.0.zip",
        "https://codeload.github.com/im1tta/OKR-Ninja/zip/refs/tags/v0.2.0",
    )
    REFUSED = (
        "http://github.com/im1tta/OKR-Ninja/releases/latest",
        "http://codeload.github.com/im1tta/OKR-Ninja/zip/refs/tags/v0.2.0",
        "https://evil.example/im1tta/OKR-Ninja.zip",
        "https://api.github.com/repos/im1tta/OKR-Ninja/releases/latest",
        "https://raw.githubusercontent.com/im1tta/OKR-Ninja/main/install.py",
        "https://github.com.evil.example/x.zip",
        "https://user@github.com/im1tta/OKR-Ninja.zip",
        "https://user:secret@codeload.github.com/x.zip",
        "https://github.com:8443/im1tta/OKR-Ninja.zip",
        "ftp://github.com/x.zip",
        "file:///etc/passwd",
    )

    def test_check_url_accepts_https_github_hosts(self):
        for url in self.ALLOWED:
            with self.subTest(url=url):
                self.m.check_url(url)

    def test_check_url_refuses_other_schemes_hosts_userinfo_and_ports(self):
        for url in self.REFUSED:
            with self.subTest(url=url):
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.check_url(url)
                self.assertIn(url, str(cm.exception))

    def redirect_request(self, newurl, code=302):
        req = urllib.request.Request(latest_url())
        headers = email.message.Message()
        headers["Location"] = newurl
        return self.m.PinnedRedirects().redirect_request(req, io.BytesIO(b""), code, "Found", headers, newurl)

    def test_the_redirect_handler_refuses_before_following(self):
        for url in self.REFUSED:
            with self.subTest(url=url):
                with self.assertRaises(self.m.Refusal) as cm:
                    self.redirect_request(url)
                self.assertIn(url, str(cm.exception))

    def test_the_redirect_handler_follows_allowed_targets(self):
        for url in self.ALLOWED:
            for code in (301, 302):
                with self.subTest(url=url, code=code):
                    self.assertEqual(self.redirect_request(url, code).full_url, url)

    def test_download_follows_the_archive_redirect_to_codeload(self):
        fake = FakeGitHub(github_routes(None, {"v0.2.0": b"zip bytes"}))
        self.assertEqual(self.m.download(archive_url("v0.2.0"), self.opener(fake)), b"zip bytes")
        self.assertEqual(fake.requests, [archive_url("v0.2.0"), codeload_url("v0.2.0")])

    def test_requests_carry_an_installer_user_agent_and_a_60_second_timeout(self):
        fake = FakeGitHub(github_routes(None, {"v0.2.0": b"zip bytes"}))
        self.m.download(archive_url("v0.2.0"), self.opener(fake))
        for req in fake.reqs:
            ua = req.get_header("User-agent") or ""
            self.assertTrue(ua, "no User-Agent")
            self.assertNotIn("python-urllib", ua.lower())
            self.assertRegex(ua.lower(), r"okr|install")
            self.assertEqual(req.timeout, 60)

    def test_the_first_url_is_checked_too(self):
        for url in ("http://github.com/x.zip", "https://evil.example/x.zip"):
            with self.subTest(url=url):
                fake = FakeGitHub({url: b"x"})
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.download(url, self.opener(fake))
                self.assertIn(url, str(cm.exception))
                self.assertEqual(fake.requests, [])

    def test_a_redirect_to_http_or_another_host_is_refused_and_never_requested(self):
        for bad in ("http://codeload.github.com/im1tta/OKR-Ninja/zip/refs/tags/v0.2.0",
                    "https://evil.example/OKR-Ninja-0.2.0.zip"):
            with self.subTest(bad=bad):
                fake = FakeGitHub({archive_url("v0.2.0"): redirect(302, bad), bad: b"x"})
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.download(archive_url("v0.2.0"), self.opener(fake))
                self.assertIn(bad, str(cm.exception))
                self.assertNotIn(bad, fake.requests)

    def test_a_declared_content_length_over_100_mb_is_refused_up_front(self):
        url = codeload_url("v0.2.0")
        fake = FakeGitHub({url: lambda req: respond(req, 200, ZeroStream(16),
                                                    {"Content-Length": str(self.m.MAX_DOWNLOAD + 1)})})
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.download(url, self.opener(fake))
        self.assertIn(url, str(cm.exception))

    def test_a_stream_past_100_mb_is_refused(self):
        url = codeload_url("v0.2.0")
        fake = FakeGitHub({url: lambda req: respond(req, 200, ZeroStream(self.m.MAX_DOWNLOAD + 1))})
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.download(url, self.opener(fake))
        self.assertIn(url, str(cm.exception))

    def test_an_http_error_is_refused_naming_the_url(self):
        url = archive_url("v9.9.9")
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.download(url, self.opener(FakeGitHub()))
        self.assertIn(url, str(cm.exception))
        self.assertIn("404", str(cm.exception))

    def test_network_failures_are_refused_naming_the_url_and_the_cause(self):
        url = codeload_url("v0.2.0")
        failures = {
            "refused": (urllib.error.URLError(ConnectionRefusedError(61, "Connection refused")), "Connection refused"),
            "reset": (ConnectionResetError(54, "Connection reset by peer"), "Connection reset"),
            "protocol": (http.client.BadStatusLine("garbage"), "garbage"),
            "value": (ValueError("bad chunk"), "bad chunk"),
        }
        for label, (exc, cause) in failures.items():
            with self.subTest(label):
                def boom(req, exc=exc):
                    raise exc
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.download(url, self.opener(FakeGitHub({url: boom})))
                self.assertIn(url, str(cm.exception))
                self.assertIn(cause, str(cm.exception))

    def test_a_connection_that_breaks_mid_download_is_refused(self):
        url = codeload_url("v0.2.0")
        fake = FakeGitHub({url: lambda req: respond(req, 200, BreakingBody(b"PK\x03\x04partial"),
                                                    {"Content-Length": "100000"})})
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.download(url, self.opener(fake))
        self.assertIn(url, str(cm.exception))


class TestResolveLatest(InstallerCase):
    """Design D2: the latest release comes from the /releases/latest redirect."""

    def resolve(self, routes, repo=SLUG):
        fake = FakeGitHub(routes)
        return self.m.resolve_latest(repo, self.opener(fake)), fake

    def assertNoRelease(self, routes, repo=SLUG):
        fake = FakeGitHub(routes)
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.resolve_latest(repo, self.opener(fake))
        self.assertIn(repo, str(cm.exception))
        return fake

    def test_a_302_to_a_release_tag_yields_the_tag(self):
        tag, fake = self.resolve({latest_url(): redirect(302, tag_page_url("v0.2.0"))})
        self.assertEqual(tag, "v0.2.0")
        self.assertEqual(fake.requests[0], latest_url())

    def test_a_rename_301_then_a_302_yields_the_tag(self):
        renamed = "im1tta/OKR-Ninja-Renamed"
        tag, _ = self.resolve({latest_url(): redirect(301, latest_url(renamed)),
                               latest_url(renamed): redirect(302, tag_page_url("v0.2.0", renamed))})
        self.assertEqual(tag, "v0.2.0")

    def test_a_final_releases_page_means_no_release(self):
        self.assertNoRelease({latest_url(): redirect(302, "https://github.com/%s/releases" % SLUG),
                              "https://github.com/%s/releases" % SLUG: b"<html>no releases</html>"})

    def test_a_tag_page_on_codeload_means_no_release(self):
        page = "https://codeload.github.com/%s/releases/tag/v0.2.0" % SLUG
        self.assertNoRelease({latest_url(): redirect(302, page), page: b"<html>page</html>"})

    def test_a_404_means_no_release(self):
        self.assertNoRelease({latest_url(): status(404)})

    def test_a_percent_encoded_tag_is_decoded(self):
        tag, _ = self.resolve({latest_url(): redirect(302, tag_page_url("v0.2.0%2Bbuild.1"))})
        self.assertEqual(tag, "v0.2.0+build.1")

    def test_a_malformed_tag_is_refused(self):
        for raw in ("v1%2F..%2Fx", "%2E%2E", "v1%20x", "v1%3Fx", "v1/extra"):
            with self.subTest(raw=raw):
                with self.assertRaises(self.m.Refusal):
                    self.resolve({latest_url(): redirect(302, tag_page_url(raw))})

    def test_a_redirect_off_github_is_refused(self):
        bad = "https://evil.example/releases/tag/v0.2.0"
        fake = FakeGitHub({latest_url(): redirect(302, bad)})
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.resolve_latest(SLUG, self.opener(fake))
        self.assertIn(bad, str(cm.exception))
        self.assertNotIn(bad, fake.requests)


# =============================================================================================
# Requirement: Remote install from a published release -- main() through the opener seam
# =============================================================================================

@needs_git
class TestRemoteRelease(InstallerCase):
    """Full runs: /releases/latest -> tag page -> archive -> codeload, behind the real redirect
    handler, with release zips built by git archive from the working tree's payload."""

    def chain(self, tag):
        return [latest_url(), tag_page_url(tag), archive_url(tag), codeload_url(tag)]

    def test_scenario_the_same_command_installs_and_updates(self):
        v2, v3 = release("v0.2.0"), release("v0.3.0")
        archives = {"v0.2.0": v2.blob, "v0.3.0": v3.blob}
        fake = FakeGitHub(github_routes("v0.2.0", archives))
        r = self.run_main([], handler=fake)
        self.assertOk(r)
        self.assertEqual(fake.requests, self.chain("v0.2.0"))
        self.assertIn("using okr-ninja 0.2.0 from im1tta/OKR-Ninja v0.2.0", r.out)
        for t in self.targets():
            self.assertInstalled(r.out, "0.2.0", t, "new install", len(v2.payload))
            self.assertHoldsExactly(t, v2.payload)
        # the repository publishes v0.3.0; the same command runs again
        fake = FakeGitHub(github_routes("v0.3.0", archives))
        r = self.run_main([], handler=fake)
        self.assertOk(r)
        self.assertEqual(fake.requests, self.chain("v0.3.0"))
        self.assertIn("using okr-ninja 0.3.0 from im1tta/OKR-Ninja v0.3.0", r.out)
        for t in self.targets():
            self.assertInstalled(r.out, "0.3.0", t, "was 0.2.0", len(v3.payload))
            self.assertHoldsExactly(t, v3.payload)
        self.assertEqual(snapshot(self.cwd), {})

    def test_scenario_a_pinned_release(self):
        v2, v3 = release("v0.2.0"), release("v0.3.0")
        fake = FakeGitHub(github_routes("v0.3.0", {"v0.2.0": v2.blob, "v0.3.0": v3.blob}))
        r = self.run_main(["install", "--release", "v0.2.0"], handler=fake)
        self.assertOk(r)
        self.assertEqual(fake.requests, [archive_url("v0.2.0"), codeload_url("v0.2.0")])
        self.assertNotIn(latest_url(), fake.requests)
        self.assertIn("using okr-ninja 0.2.0 from im1tta/OKR-Ninja v0.2.0", r.out)
        for t in self.targets():
            self.assertHoldsExactly(t, v2.payload)

    def test_release_latest_means_the_latest_release(self):
        v3 = release("v0.3.0")
        fake = FakeGitHub(github_routes("v0.3.0", {"v0.3.0": v3.blob}))
        r = self.run_main(["install", "--release", "latest"], handler=fake)
        self.assertOk(r)
        self.assertEqual(fake.requests, self.chain("v0.3.0"))

    def test_scenario_remote_build_for_upload_platforms(self):
        v2 = release("v0.2.0")
        fake = FakeGitHub(github_routes("v0.2.0", {"v0.2.0": v2.blob}))
        r = self.run_main(["build"], handler=fake)
        self.assertOk(r)
        self.assertEqual(sorted(os.listdir(str(self.cwd))), ["okr-ninja.plugin", "okr-ninja.skill"])
        self.assertIn("wrote ", r.out)
        self.assertIn("okr-ninja.skill", r.out)
        self.assertPackages(self.cwd, v2.payload, "0.2.0")
        self.assertEqual(home_snapshot(self.home), {})
        # byte-identical to a checkout build of the same files
        co = checkout_from(v2, self.tmp / "co")
        self.assertOk(self.run_script(co / "install.py", ["build", "--out", self.tmp / "out"]))
        for name in ("okr-ninja.skill", "okr-ninja.plugin"):
            self.assertEqual((self.cwd / name).read_bytes(), (self.tmp / "out" / name).read_bytes(), name)

    def test_remote_builds_are_reproducible(self):
        v2 = release("v0.2.0")
        for out in ("b1", "b2"):
            self.assertOk(self.run_main(["build", "--source", v2.zip, "--out", self.tmp / out]))
        for name in ("okr-ninja.skill", "okr-ninja.plugin"):
            self.assertEqual((self.tmp / "b1" / name).read_bytes(), (self.tmp / "b2" / name).read_bytes())

    def test_remote_check_prints_name_and_version(self):
        v2 = release("v0.2.0")
        fake = FakeGitHub(github_routes("v0.2.0", {"v0.2.0": v2.blob}))
        r = self.run_main(["check"], handler=fake)
        self.assertOk(r)
        self.assertIn("ok: okr-ninja 0.2.0", r.out)
        self.assertNothingWritten()

    def test_scenario_a_local_archive_needs_no_network(self):
        v2 = release("v0.2.0")
        fake = FakeGitHub()
        r = self.run_main(["install", "--source", v2.zip], handler=fake)
        self.assertOk(r)
        self.assertEqual(fake.requests, [])
        self.assertIn("using okr-ninja 0.2.0 from %s" % v2.zip, r.out)
        for t in self.targets():
            self.assertHoldsExactly(t, v2.payload)

    def test_scenario_an_archive_naming_another_skill_is_refused(self):
        other = release("other")
        write_files(self.home / ".claude" / "skills" / "other-skill",
                    {"SKILL.md": mini_skill_md("1.0.0", name="other-skill"), "notes.md": "mine\n"})
        before = home_snapshot(self.home)
        for command in ("install", "build"):
            with self.subTest(command=command):
                r = self.run_main([command, "--source", other.zip])
                self.assertRefusedRun(r, "other-skill")
                self.assertEqual(home_snapshot(self.home), before)
                self.assertEqual(snapshot(self.cwd), {})

    def test_a_break_mid_download_writes_nothing(self):
        v2 = release("v0.2.0")
        routes = github_routes("v0.2.0", {"v0.2.0": v2.blob})
        routes[codeload_url("v0.2.0")] = lambda req: respond(
            req, 200, BreakingBody(v2.blob[:1000]), {"Content-Length": str(len(v2.blob))})
        r = self.run_main([], handler=FakeGitHub(routes))
        self.assertRefusedRun(r)
        self.assertTrue(archive_url("v0.2.0") in r.err or codeload_url("v0.2.0") in r.err, r.err)
        self.assertNothingWritten()


class TestRemoteRefusals(InstallerCase):
    """Refusals of the remote path that need no release fixture."""

    def test_scenario_no_published_release(self):
        cases = {
            "404": {latest_url(): status(404)},
            "releases page": {latest_url(): redirect(302, "https://github.com/%s/releases" % SLUG),
                              "https://github.com/%s/releases" % SLUG: b"<html></html>"},
        }
        for label, routes in cases.items():
            with self.subTest(label):
                home, cwd = self.fresh()
                r = self.run_main(["install"], handler=FakeGitHub(routes), home=home, cwd=cwd)
                self.assertRefusedRun(r, SLUG)
                self.assertNothingWritten(home, cwd)

    def test_scenario_a_redirect_away_from_github_is_refused(self):
        path, _ = self.mini_release("0.2.0")
        blob = path.read_bytes()
        cases = (
            ("archive to http", archive_url("v0.2.0"),
             "http://codeload.github.com/im1tta/OKR-Ninja/zip/refs/tags/v0.2.0"),
            ("archive to another host", archive_url("v0.2.0"), "https://evil.example/OKR-Ninja-0.2.0.zip"),
            ("latest to another host", latest_url(), "https://evil.example/im1tta/OKR-Ninja/releases/tag/v0.2.0"),
        )
        for label, at, bad in cases:
            with self.subTest(label):
                routes = github_routes("v0.2.0", {"v0.2.0": blob})
                routes[at] = redirect(302, bad)
                routes[bad] = blob
                home, cwd = self.fresh()
                fake = FakeGitHub(routes)
                r = self.run_main(["install"], handler=fake, home=home, cwd=cwd)
                self.assertRefusedRun(r, bad)
                self.assertNotIn(bad, fake.requests)
                self.assertNothingWritten(home, cwd)

    def test_scenario_unsafe_repository_or_tag_values_are_refused_before_any_request(self):
        cases = [
            (["install", "--repo", "../x"], "../x"),
            (["install", "--repo", "a/b/c"], "a/b/c"),
            (["install", "--release", "v1/../x"], "v1/../x"),
            (["build", "--repo", "../x"], "../x"),
            (["check", "--release", "v1/../x"], "v1/../x"),
        ]
        for owner_or_name in ("-ab/x", "a_b/x", "a" * 40 + "/x", "a/.", "a/..", "a/" + "n" * 101,
                              "a", "/x", "a/", "a b/x", "a/b c", "a/b?c", "a/b%2Fc"):
            cases.append((["install", "--repo=" + owner_or_name], owner_or_name))  # "=": "-ab/x" is a value
        for tag in (".", "..", "v1 x", "v1/x", "v1\\x", "v1?x", "v1#x", "v1%2Fx", "v1:x"):
            cases.append((["install", "--release=" + tag], tag))
        for argv, value in cases:
            with self.subTest(argv=argv):
                home, cwd = self.fresh()
                fake = FakeGitHub()
                r = self.run_main(argv, handler=fake, home=home, cwd=cwd)
                self.assertRefusedRun(r)
                self.assertTrue(names(value, r.err), "%r is not named in:\n%s" % (value, r.err))
                self.assertEqual(fake.requests, [])
                self.assertNothingWritten(home, cwd)

    def test_repository_and_tag_rules_accept_their_whole_alphabet(self):
        for repo in ("a1-b/n.a_m-e", "a" * 39 + "/x", "x/" + "n" * 100, "A-B/..x"):
            with self.subTest(repo=repo):
                home, cwd = self.fresh()
                fake = FakeGitHub()
                r = self.run_main(["install", "--repo", repo], handler=fake, home=home, cwd=cwd)
                self.assertEqual(r.code, 1)
                self.assertEqual(fake.requests, [latest_url(repo)])
                self.assertIn(repo, r.err)
        tag = "v1.0.0-rc.1+build_5"
        fake = FakeGitHub()
        r = self.run_main(["install", "--release", tag], handler=fake)
        self.assertEqual(r.code, 1)
        self.assertEqual([urllib.parse.unquote(u) for u in fake.requests], [archive_url(tag)])
        self.assertNothingWritten()

    def test_source_with_release_latest_is_refused_naming_both_options(self):
        path, _ = self.mini_release("0.2.0")
        fake = FakeGitHub()
        r = self.run_main(["install", "--source", path, "--release", "latest"], handler=fake)
        self.assertRefusedRun(r, "--source", "--release")
        self.assertEqual(fake.requests, [])
        self.assertNothingWritten()

    def test_source_must_be_an_existing_regular_file(self):
        folder = Path(self.mkdtemp("src")) / "a-folder"
        folder.mkdir()
        for label, path in (("a folder", folder), ("missing", folder.parent / "missing.zip")):
            with self.subTest(label):
                home, cwd = self.fresh()
                fake = FakeGitHub()
                r = self.run_main(["install", "--source", path], handler=fake, home=home, cwd=cwd)
                self.assertRefusedRun(r, str(path))
                self.assertEqual(fake.requests, [])
                self.assertNothingWritten(home, cwd)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "needs mkfifo")
    def test_source_that_is_a_fifo_is_refused_without_hanging(self):
        fifo = Path(self.mkdtemp("fifo")) / "release.zip"
        os.mkfifo(str(fifo))
        r = self.run_script(None, ["install", "--source", fifo], piped=True, timeout=30)
        self.assertRefusedRun(r, str(fifo))
        self.assertNothingWritten()

    def test_source_over_100_mb_is_refused(self):
        big = Path(self.mkdtemp("big")) / "release.zip"
        with open(str(big), "wb") as f:
            f.truncate(self.m.MAX_DOWNLOAD + 1)  # sparse
        r = self.run_main(["install", "--source", big])
        self.assertRefusedRun(r, str(big))
        self.assertNothingWritten()

    def test_the_announcement_names_the_archive_and_version(self):
        path, _ = self.mini_release("0.2.0")
        r = self.run_main(["install", "--source", path])
        self.assertOk(r)
        self.assertIn("using okr-ninja 0.2.0 from %s" % path, r.out)

    def test_a_certificate_failure_says_how_to_install_ca_certificates(self):
        def boom(req):
            raise urllib.error.URLError(ssl.SSLCertVerificationError(
                1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: "
                   "unable to get local issuer certificate"))
        present = Path(self.mkdtemp("ca")) / "cert.pem"
        present.write_text("-----BEGIN CERTIFICATE-----\n")
        missing = present.parent / "missing-cert.pem"

        def paths(cafile):
            return ssl.DefaultVerifyPaths(None, None, "SSL_CERT_FILE", str(cafile), "SSL_CERT_DIR",
                                          str(cafile.parent / "certs"))

        cases = (("darwin", missing, "Install Certificates.command"),
                 ("darwin", present, "SSL_CERT_FILE"),
                 ("linux", missing, "SSL_CERT_FILE"))
        for platform, cafile, advice in cases:
            with self.subTest(platform=platform, cafile=cafile.name):
                home, cwd = self.fresh()
                with mock.patch.object(sys, "platform", platform), \
                        mock.patch("ssl.get_default_verify_paths", return_value=paths(cafile)):
                    r = self.run_main(["install"], handler=FakeGitHub({latest_url(): boom}), home=home, cwd=cwd)
                self.assertRefusedRun(r, latest_url(), advice)
                self.assertIn("certificate", r.err.lower())
                if advice == "SSL_CERT_FILE":
                    self.assertNotIn("Install Certificates.command", r.err)
                self.assertNothingWritten(home, cwd)


# =============================================================================================
# Requirement: Release archives are read, never extracted
# =============================================================================================

class TestArchiveReading(InstallerCase):

    def plus(self, *extra, **kw):
        return release_entries(**kw) + list(extra)

    P = "OKR-Ninja-0.2.0/"

    # -- what is read ----------------------------------------------------------------------

    def test_a_well_formed_archive_is_read(self):
        data, text = self.m.read_archive(zip_bytes(release_entries("0.2.0"), comment=b"0" * 40))
        self.assertEqual(data, release_payload("0.2.0"))
        self.assertEqual(text, mini_skill_md("0.2.0"))

    @needs_git
    def test_scenario_an_archive_shaped_like_githubs_is_read(self):
        v2 = release("v0.2.0")
        zf = zipfile.ZipFile(io.BytesIO(v2.blob))
        self.assertTrue(zf.comment, "git archive writes the commit as the zip comment")
        self.assertIn("OKR-Ninja-0.2.0/references/", zf.namelist())
        if POSIX:
            info = zf.getinfo("OKR-Ninja-0.2.0/references/link.md")
            self.assertEqual((info.external_attr >> 16) & 0o170000, 0o120000)
        data, text = self.m.read_archive(v2.blob)
        self.assertEqual(data, v2.payload)
        self.assertEqual(text, (v2.tree / "SKILL.md").read_text(encoding="utf-8"))
        for skipped in ("references/link.md", "references/.cache/x.md", "references/.DS_Store",
                        "examples/Thumbs.db", "references/m.pyc", "README.md", "install.py", "CLAUDE.md"):
            self.assertNotIn(skipped, data)

    @needs_git
    def test_scenario_only_the_payload_is_taken_from_a_release(self):
        v2 = release("v0.2.0")
        r = self.run_main(["install", "--source", v2.zip])
        self.assertOk(r)
        for t in self.targets():
            self.assertHoldsExactly(t, v2.payload)
        self.assertOk(self.run_main(["build", "--source", v2.zip, "--out", self.tmp / "out"]))
        self.assertPackages(self.tmp / "out", v2.payload, "0.2.0")

    def test_skipped_entries_never_reach_the_payload(self):
        P = self.P
        entries = release_entries("0.2.0", extra={
            "references/sub/deep.md": b"deep\n",
            "examples/nested/x.md": b"nested\n",
            "references/.cache/x.md": b"hidden\n",
            "references/sub/.hidden.md": b"hidden\n",
            "references/.DS_Store": b"Bud1",
            "examples/.DS_Store": b"Bud1",
            "references/__pycache__/m.cpython-39.pyc": b"pyc",
            "references/__pycache__/notes.md": b"not bytecode\n",
            "references/m.pyc": b"pyc",
            "references/Thumbs.db": b"thumbs",
            "examples/desktop.ini": b"ini",
            "examples/sub/DESKTOP.INI": b"ini",
            ".claude/y.md": b"y\n",
            "evals/x.md": b"x\n",
            "tests/test_x.py": b"x\n",
            "openspec/o.md": b"o\n",
            "dist/okr-ninja.skill": b"stale\n",
            "references.md": b"not a payload folder\n",
        }, links={"references/link.md": "../SKILL.md", "examples/folder-link": "../references"})
        link = zipfile.ZipInfo(P + "references/link755.md", date_time=(2026, 9, 1, 0, 0, 0))
        link.create_system = 3
        link.external_attr = 0o120755 << 16
        entries = entries + [(link, b"../../../etc/passwd", "zipinfo")]
        data, _ = self.m.read_archive(zip_bytes(entries))
        self.assertEqual(sorted(data), sorted(["SKILL.md", "LICENSE", "references/goodness-rubric.md",
                                               "references/alignment-taxonomy.md", "references/sub/deep.md",
                                               "examples/sample-portfolio.md", "examples/nested/x.md"]))
        self.assertIn(P + "references/link.md", zipfile.ZipFile(io.BytesIO(zip_bytes(entries))).namelist())

    def test_non_payload_entries_are_not_held_to_the_portable_name_rule(self):
        data, _ = self.m.read_archive(zip_bytes(release_entries("0.2.0", extra={
            "evals/a:b.md": b"x\n", "docs/NUL.md": b"x\n", "docs/trailing.": b"x\n"})))
        self.assertEqual(data, release_payload("0.2.0"))

    def test_crlf_skill_md_is_read_like_a_checkouts(self):
        crlf = mini_skill_md("0.2.0").replace("\n", "\r\n").encode("utf-8")
        blob = zip_bytes(release_entries("0.2.0", extra={"SKILL.md": crlf}))
        data, text = self.m.read_archive(blob)
        self.assertEqual(data["SKILL.md"], crlf)
        self.assertEqual(text, mini_skill_md("0.2.0"))
        r = self.run_main(["install", "--source", self.write_zip(blob), "--release", "v0.2.0"])
        self.assertOk(r)
        self.assertInstalled(r.out, "0.2.0", self.targets()[0], "new install")

    def test_a_large_non_payload_entry_is_not_counted_against_the_payload_cap(self):
        blob = zip_bytes(release_entries("0.2.0", extra={"evals/big.bin": bytes(self.m.MAX_PAYLOAD + 1)}))
        data, _ = self.m.read_archive(blob)
        self.assertEqual(data, release_payload("0.2.0"))

    # -- names -----------------------------------------------------------------------------

    def test_scenario_a_traversal_entry_is_refused(self):
        for name in (self.P + "references/../../escape.md", "/etc/passwd", self.P + "evals/../../../x.md"):
            with self.subTest(name=name):
                self.assertArchiveRefused(self.plus((name, b"x\n")), name)

    def test_unsafe_stored_names_are_refused(self):
        P = self.P
        for label, name, needle in (
                ("empty segment", P + "references//x.md", P + "references//x.md"),
                ("dot segment", P + "references/./x.md", P + "references/./x.md"),
                ("backslash", P + "references\\x.md", None),
                ("drive letter", "C:/evil.md", "drive letter"),
                ("drive letter, relative", "C:evil.md", "drive letter")):
            with self.subTest(label):
                self.assertArchiveRefused(self.plus((name, b"x\n")), *([needle] if needle else []))

    def test_a_drive_letter_top_level_folder_is_refused(self):
        self.assertArchiveRefused(release_entries("0.2.0", prefix="C:/"), "drive letter")

    def test_a_nul_in_a_stored_name_is_refused(self):
        blob = zip_bytes(self.plus((self.P + "references/aXb.md", b"x\n")))
        self.assertEqual(blob.count(b"references/aXb.md"), 2)  # local header and central directory
        blob = blob.replace(b"references/aXb.md", b"references/a\x00b.md")
        self.assertArchiveRefused(blob, forbidden=("\x00",))

    def test_duplicate_entries_are_refused(self):
        self.assertArchiveRefused(self.plus((self.P + "references/goodness-rubric.md", b"second copy\n")),
                                  "goodness-rubric.md")
        odd = self.P + "evals/\x1b[31mX"
        self.assertArchiveRefused(self.plus((odd, b"1"), (odd, b"2")), "\\x1b[31mX", forbidden=("\x1b",))

    def test_scenario_unsafe_payload_names_are_refused(self):
        R = self.P + "references/"
        cases = [
            ("escape character", R + "a\x1bb.md", "\\x1b", "\x1b"),
            ("colon", R + "a:b.md", "a:b.md", None),
            ("trailing dot", R + "notes.", "notes.", None),
            ("device name", R + "NUL.md", "NUL.md", None),
            ("trailing space", R + "notes ", "notes ", None),
            ("control 0x01", R + "a\x01b.md", "\\x01", "\x01"),
            ("control 0x1f", R + "a\x1fb.md", "\\x1f", "\x1f"),
            ("control 0x7f", R + "a\x7fb.md", "\\x7f", "\x7f"),
            ("C1 control 0x85 (NEL)", R + "a\x85b.md", "\\x85", "\x85"),
            ("C1 control 0x9b (CSI)", R + "a\x9b31mb.md", "\\x9b", "\x9b"),
            ("C1 control 0x80", R + "a\x80b.md", "\\x80", "\x80"),
            ("C1 control 0x9f", R + "a\x9fb.md", "\\x9f", "\x9f"),
            ("device name in a folder", R + "con/x.md", "con/x.md", None),
        ]
        for device in ("nul", "Con", "PRN", "aux.tar.gz", "COM1", "com9.txt", "LPT1", "lpt9.md"):
            cases.append(("device " + device, R + device, device, None))
        for ch in '<>"|?*':
            cases.append(("character " + ch, R + "a%sb.md" % ch, None, None))
        for label, name, needle, raw in cases:
            with self.subTest(label):
                self.assertArchiveRefused(self.plus((name, b"x\n")), *([needle] if needle else []),
                                          forbidden=(raw,) if raw else ())

    def test_scenario_colliding_payload_paths_are_refused(self):
        R = self.P + "references/"
        cases = (
            ("letter case", [(R + "Rubric.md", b"a"), (R + "rubric.md", b"b")], ("Rubric.md", "rubric.md")),
            ("file and folder", [(R + "a", b"a"), (R + "a/b.md", b"b")], ("references/a/b.md",)),
            ("file and folder, letter case", [(R + "A", b"a"), (R + "a/b.md", b"b")], ("a/b.md",)),
            ("dot segment", [(R + "./x.md", b"a")], ("references/./x.md",)),
            ("folder before file, letter case", [(R + "A/b.md", b"b"), (R + "a", b"a")], ("A/b.md", "references/a")),
            ("canonical caseless (casefold un-normalises)",
             [(R + "\u0390.md", b"a"), (R + "\u03aa\u0301.md", b"b")], ("\\u0390", "\\u03aa")),
            ("Unicode normalisation", [(R + "caf\u00e9.md", b"a"), (R + "cafe\u0301.md", b"b")], ()),
        )
        for label, extra, needles in cases:
            with self.subTest(label):
                self.assertArchiveRefused(self.plus(*extra), *needles)

    # -- shape -----------------------------------------------------------------------------

    def test_an_archive_without_exactly_one_top_level_folder_is_refused(self):
        flat = [(rel, data) for rel, data in sorted(release_files("0.2.0").items())]
        cases = {
            "two top-level folders": self.plus(("Other-1.0/x.md", b"x\n")),
            "no top-level folder": flat,
            "empty archive": [],
        }
        for label, entries in cases.items():
            with self.subTest(label):
                self.assertArchiveRefused(zip_bytes(entries))

    def test_scenario_a_symlinked_skill_md_is_refused(self):
        for rel, target in (("SKILL.md", "/etc/passwd"), ("LICENSE", "../../README.md")):
            with self.subTest(rel):
                entries = release_entries("0.2.0", extra={rel: None}, links={rel: target})
                self.assertArchiveRefused(entries, rel)

    def test_a_missing_skill_md_or_license_or_empty_payload_folder_is_refused(self):
        cases = (
            ("SKILL.md", {"SKILL.md": None}),
            ("LICENSE", {"LICENSE": None}),
            ("references", {"references/goodness-rubric.md": None, "references/alignment-taxonomy.md": None,
                            "references/.keep": b""}),
            ("examples", {"examples/sample-portfolio.md": None}),
        )
        for needle, extra in cases:
            with self.subTest(needle):
                self.assertArchiveRefused(release_entries("0.2.0", extra=extra), needle)

    # -- corrupt or hostile bytes -------------------------------------------------------------

    def test_unreadable_zips_are_refused(self):
        good = zip_bytes(release_entries("0.2.0"))
        cases = {
            "not a zip": b"this is not a zip file\n" * 10,
            "empty file": b"",
            "truncated in half": good[: len(good) // 2],
            "truncated tail": good[:-30],
        }
        for label, blob in cases.items():
            with self.subTest(label):
                self.assertArchiveRefused(blob)

    def test_an_entry_running_past_the_end_of_the_archive_is_refused(self):
        name = self.P + "references/goodness-rubric.md"
        b = bytearray(zip_bytes(release_entries("0.2.0"), compress=zipfile.ZIP_STORED))
        local, central = entry_offsets(bytes(b), name)
        struct.pack_into("<II", b, local + 18, 5000, 5000)
        for c in central:
            struct.pack_into("<II", b, c + 20, 5000, 5000)
        self.assertArchiveRefused(bytes(b), "goodness-rubric.md")

    def test_a_failed_checksum_is_refused(self):
        # a non-ASCII name: zipfile's message repeats it through %r, which keeps the letters
        blob = zip_bytes(self.plus((self.P + "references/r\u00e9sum\u00e9.md", b"CRC-MARKER-0123456789\n")),
                         compress=zipfile.ZIP_STORED)
        b = bytearray(blob)
        at = blob.index(b"CRC-MARKER")
        b[at] ^= 0xFF
        self.assertArchiveRefused(bytes(b))

    def test_a_corrupt_deflate_stream_is_refused(self):
        name = self.P + "references/long.md"
        blob = zip_bytes(self.plus((name, b"lorem ipsum dolor sit amet " * 400)))
        start, end = entry_data_span(blob, name)
        b = bytearray(blob)
        b[start:end] = b"\xff" * (end - start)
        self.assertArchiveRefused(bytes(b))

    def test_an_encrypted_entry_is_refused(self):
        name = self.P + "references/\u0440\u0443\u0431\u0440\u0438\u043a\u0430.md"
        blob = zip_bytes(self.plus((name, b"# rubric\n")))
        self.assertArchiveRefused(patch_entry(blob, name, flags=0x1), "encrypted")

    def test_an_unsupported_compression_method_is_refused(self):
        blob = zip_bytes(release_entries("0.2.0"))
        self.assertArchiveRefused(patch_entry(blob, self.P + "examples/sample-portfolio.md", method=97))

    def test_scenario_a_decompression_bomb_is_refused_before_it_is_decompressed(self):
        cap = self.m.MAX_PAYLOAD
        cases = {
            "one entry over 20 MB": {"references/bomb.md": bytes(cap + 1)},
            "entries adding up to over 20 MB": {"references/a.md": bytes(cap // 2 + 1),
                                                "examples/b.md": bytes(cap // 2 + 1)},
        }
        real_open = zipfile.ZipFile.open
        for label, extra in cases.items():
            with self.subTest(label):
                blob = zip_bytes(release_entries("0.2.0", extra=extra))
                self.assertLess(len(blob), cap // 10, "the fixture should be a small bomb")
                opened = []

                def spy(zf, name, *args, **kwargs):
                    opened.append(getattr(name, "filename", name))
                    return real_open(zf, name, *args, **kwargs)

                with mock.patch.object(zipfile.ZipFile, "open", spy):
                    with self.assertRaises(self.m.Refusal):
                        self.m.read_archive(blob)
                self.assertEqual(opened, [], "entries were decompressed before the size check")
                self.assertArchiveRefused(blob)


# =============================================================================================
# Requirement: A release's version agrees with its tag
# =============================================================================================

class TestReleaseVersionMatchesTag(InstallerCase):

    def test_scenario_a_mismatched_release_is_refused(self):
        # tag v0.3.0's archive (its folder named for 0.3.0) carries metadata.version 0.2.0
        blob = zip_bytes(release_entries("0.2.0", prefix="OKR-Ninja-0.3.0/"))
        for label, argv, routes in (
                ("resolved as latest", [], github_routes("v0.3.0", {"v0.3.0": blob})),
                ("pinned", ["install", "--release", "v0.3.0"], github_routes(None, {"v0.3.0": blob}))):
            with self.subTest(label):
                home, cwd = self.fresh()
                r = self.run_main(argv, handler=FakeGitHub(routes), home=home, cwd=cwd)
                self.assertRefusedRun(r, "v0.3.0", "0.2.0")
                self.assertNothingWritten(home, cwd)

    def test_scenario_a_matching_release_is_accepted(self):
        path, payload = self.mini_release("0.2.0")
        fake = FakeGitHub(github_routes("v0.2.0", {"v0.2.0": path.read_bytes()}))
        r = self.run_main(["install", "--release", "v0.2.0"], handler=fake)
        self.assertOk(r)
        for t in self.targets():
            self.assertHoldsExactly(t, payload)

    def test_source_with_release_is_compared_against_that_tag(self):
        path, _ = self.mini_release("0.2.0")
        for release_value, ok in (("v0.2.0", True), ("0.2.0", True), ("v0.3.0", False), ("vv0.2.0", False)):
            with self.subTest(release=release_value):
                home, cwd = self.fresh()
                fake = FakeGitHub()
                r = self.run_main(["install", "--source", path, "--release", release_value],
                                  handler=fake, home=home, cwd=cwd)
                self.assertEqual(fake.requests, [])
                if ok:
                    self.assertOk(r)
                else:
                    self.assertRefusedRun(r, release_value, "0.2.0")
                    self.assertNothingWritten(home, cwd)

    def test_source_without_release_makes_no_tag_comparison(self):
        path, payload = self.mini_release("9.9.9", prefix="OKR-Ninja-0.2.0/")
        r = self.run_main(["install", "--source", path])
        self.assertOk(r)
        self.assertInstalled(r.out, "9.9.9", self.targets()[0], "new install")


# =============================================================================================
# The documented piped form, as a subprocess (design D11, D13)
# =============================================================================================

@needs_git
class TestPipedRuns(InstallerCase):

    def test_piped_install_then_update_from_a_folder_that_shadows_the_standard_library(self):
        v2, v3 = release("v0.2.0"), release("v0.3.0")
        for module in ("json.py", "zipfile.py"):
            (self.cwd / module).write_text('raise SystemExit("shadowed")\n')
        before_cwd = snapshot(self.cwd)
        r = self.run_script(None, ["--source", v2.zip], piped=True)
        self.assertOk(r)
        self.assertNotIn("shadowed", r.err)
        self.assertEqual(r.out.count("(new install)"), 2, r.out)
        for t in self.targets():
            self.assertInstalled(r.out, "0.2.0", t, "new install", len(v2.payload))
        r = self.run_script(None, ["--source", v3.zip], piped=True)
        self.assertOk(r)
        self.assertEqual(r.out.count("(was 0.2.0)"), 2, r.out)
        for t in self.targets():
            self.assertInstalled(r.out, "0.3.0", t, "was 0.2.0", len(v3.payload))
            self.assertHoldsExactly(t, v3.payload)
        self.assertEqual(snapshot(self.cwd), before_cwd)
        top = {rel.split("/")[0] for rel in home_snapshot(self.home)}
        self.assertEqual(top, {".claude", ".agents"})

    def test_piped_remote_build_matches_a_checkout_build_byte_for_byte(self):
        v2 = release("v0.2.0")
        r = self.run_script(None, ["build", "--source", v2.zip], piped=True)
        self.assertOk(r)
        self.assertEqual(sorted(os.listdir(str(self.cwd))), ["okr-ninja.plugin", "okr-ninja.skill"])
        co = checkout_from(v2, self.tmp / "co")
        self.assertOk(self.run_script(co / "install.py", ["build", "--out", self.tmp / "out"]))
        for name in ("okr-ninja.skill", "okr-ninja.plugin"):
            self.assertEqual((self.cwd / name).read_bytes(), (self.tmp / "out" / name).read_bytes(), name)
        self.assertEqual(home_snapshot(self.home), {})


# =============================================================================================
# main must install every published release (design D13): frozen release shapes
# =============================================================================================

FROZEN_V020_SKILL_MD = (
    "---\n"
    "name: okr-ninja\n"
    "description: Audits OKRs for one team or a whole portfolio, checking goal quality and "
    "cross-team alignment. Frozen v0.2.0-shaped test copy.\n"
    "license: MIT\n"
    "metadata:\n"
    '  version: "0.2.0"\n'
    "---\n"
    "\n"
    "# OKR-Ninja\n"
    "\n"
    "Frozen v0.2.0-shaped test copy with fictional content.\n"
)


class TestFrozenReleaseShapes(InstallerCase):

    def frozen_v020(self):
        P = "OKR-Ninja-0.2.0/"
        files = {
            "SKILL.md": FROZEN_V020_SKILL_MD.encode("ascii"),
            "LICENSE": MIT_LICENSE.encode("ascii"),
            "references/goodness-rubric.md": b"# Goodness rubric (frozen test copy)\n",
            "examples/sample-portfolio.md": b"# Sample portfolio (fictional, frozen test copy)\n",
        }
        entries = [(P, b"", DIR), (P + ".claude/", b"", DIR), (P + ".claude/y.md", b"y\n"),
                   (P + "CLAUDE.md", b"# notes\n"), (P + "LICENSE", files["LICENSE"]),
                   (P + "README.md", b"# OKR-Ninja\n"), (P + "SKILL.md", files["SKILL.md"]),
                   (P + "evals/", b"", DIR), (P + "evals/x.md", b"x\n"),
                   (P + "examples/", b"", DIR), (P + "examples/sample-portfolio.md", files["examples/sample-portfolio.md"]),
                   (P + "install.py", b"# the v0.2.0 installer\n"),
                   (P + "references/", b"", DIR), (P + "references/goodness-rubric.md", files["references/goodness-rubric.md"])]
        blob = zip_bytes(entries, comment=b"4f2a0c9e1b7d3a5c8e6f0a2b4c6d8e0f1a3b5c7d")
        return self.write_zip(blob, "OKR-Ninja-v0.2.0.zip"), files

    def test_main_installs_checks_and_builds_the_frozen_v0_2_0_release_shape(self):
        path, payload = self.frozen_v020()
        r = self.run_main(["install", "--source", path, "--release", "v0.2.0"])
        self.assertOk(r)
        for t in self.targets():
            self.assertHoldsExactly(t, payload)
            self.assertInstalled(r.out, "0.2.0", t, "new install", len(payload))
        r = self.run_main(["check", "--source", path, "--release", "v0.2.0"])
        self.assertOk(r)
        self.assertIn("ok: okr-ninja 0.2.0", r.out)
        r = self.run_main(["build", "--source", path, "--release", "v0.2.0", "--out", self.tmp / "out"])
        self.assertOk(r)
        self.assertPackages(self.tmp / "out", payload, "0.2.0")


# =============================================================================================
# Repair cycle 1 (independent verification, 2026-09-25): shared folders, unbounded
# decompressors, exceptions no fixed list anticipates, escaped build output, short reads
# =============================================================================================

class FakeSocket(object):
    def __init__(self, data):
        self.data = data

    def makefile(self, mode="rb", *args, **kwargs):
        return io.BytesIO(self.data)


def real_http_response(req, body, declared):
    """A real http.client.HTTPResponse, as urllib's do_open returns it, whose declared
    Content-Length may exceed the bytes the connection actually delivers."""
    raw = b"HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n" % declared + body
    r = http.client.HTTPResponse(FakeSocket(raw), method="GET", url=req.full_url)
    r.begin()
    r.url = req.full_url
    r.msg = r.reason
    return r


class TestRepairCycle1(InstallerCase):

    P = "OKR-Ninja-0.2.0/"

    def planted_checkout(self, folder, name="other-skill"):
        """What another local user could plant in a shared folder: a full fake checkout."""
        files = release_files("9.9.9", name=name)
        write_files(folder, {rel: data for rel, data in files.items() if rel != "install.py"})
        return folder

    # -- 7.1 a world-writable folder is never a checkout -----------------------------------

    @unittest.skipUnless(POSIX, "world-writable folders are a POSIX notion")
    def test_checkout_root_refuses_a_world_writable_folder(self):
        folder = self.planted_checkout(self.tmp / "shared")
        script = folder / "tmp.AbCdEf1234"
        script.write_bytes(INSTALL_PY.read_bytes())
        os.chmod(str(folder), 0o755)
        (folder / "README.md").write_bytes(b"# a checkout\n")
        self.assertIsNotNone(self.m.checkout_root(str(script), str(script)))
        for mode in (0o1777, 0o777, 0o757):
            with self.subTest(mode=oct(mode)):
                os.chmod(str(folder), mode)
                try:
                    self.assertIsNone(self.m.checkout_root(str(script), str(script)))
                finally:
                    os.chmod(str(folder), 0o755)

    @unittest.skipUnless(POSIX, "world-writable folders are a POSIX notion")
    def test_scenario_a_checkout_in_a_world_writable_folder_is_never_read(self):
        shared = self.planted_checkout(self.tmp / "sharedtmp")
        victim = self.home / ".claude" / "skills" / "other-skill"
        write_files(victim, {"SKILL.md": b"precious\n"})
        before = home_snapshot(self.home)
        script = shared / "tmp.XyZ0123456"  # what GNU mktemp creates in /tmp
        script.write_bytes(INSTALL_PY.read_bytes())
        os.chmod(str(shared), 0o1777)
        try:
            r = self.run_script(script, [])
        finally:
            os.chmod(str(shared), 0o755)
        self.assertRefusedRun(r, latest_url())
        self.assertNotIn("reading the checkout", r.out)
        self.assertNotIn("other-skill", r.out)
        self.assertEqual(home_snapshot(self.home), before)
        self.assertEqual((victim / "SKILL.md").read_bytes(), b"precious\n")

    # -- 7.2 only stored and deflated payload entries are read ------------------------------

    def test_bzip2_and_lzma_payload_entries_are_refused_before_decompression(self):
        for method, label in ((zipfile.ZIP_BZIP2, "12"), (zipfile.ZIP_LZMA, "14")):
            with self.subTest(method=label):
                blob = zip_bytes(release_entries("0.2.0"), compress=method)
                opened = []
                real_open = zipfile.ZipFile.open

                def spy(zf, *a, **k):
                    opened.append(a[0] if a else k.get("name"))
                    return real_open(zf, *a, **k)
                with mock.patch.object(zipfile.ZipFile, "open", spy):
                    with self.assertRaises(self.m.Refusal) as cm:
                        self.m.read_archive(blob)
                self.assertIn("compression method " + label, str(cm.exception))
                self.assertEqual(opened, [], "no entry may be decompressed before the refusal")
                home, cwd = self.fresh()
                r = self.run_main(["install", "--source", self.write_zip(blob)], home=home, cwd=cwd)
                self.assertRefusedRun(r, "compression method " + label)
                self.assertNothingWritten(home, cwd)

    def test_an_unbounded_method_outside_the_payload_is_ignored(self):
        blob = zip_bytes(release_entries("0.2.0") + [(self.P + "evals/big.bin", b"x" * 1000)])
        blob = patch_entry(blob, self.P + "evals/big.bin", method=zipfile.ZIP_BZIP2)
        data, _ = self.m.read_archive(blob)
        self.assertEqual(data, release_payload("0.2.0"))

    # -- 7.3 any exception while reading is a named refusal ---------------------------------

    def test_any_exception_while_reading_an_entry_is_a_named_refusal(self):
        class LZMALikeError(Exception):  # _lzma.LZMAError subclasses Exception directly
            pass
        blob = zip_bytes(release_entries("0.2.0"))
        for exc, cause in ((LZMALikeError("Invalid or unsupported options"), "Invalid or unsupported"),
                           (OverflowError("Python int too large to convert"), "too large"),
                           (EOFError(), "EOFError"),
                           (MemoryError(), "MemoryError")):
            with self.subTest(exc=type(exc).__name__):
                with mock.patch.object(zipfile.ZipFile, "open", side_effect=exc):
                    with self.assertRaises(self.m.Refusal) as cm:
                        self.m.read_archive(blob)
                self.assertIn("cannot read", str(cm.exception))
                self.assertIn(cause, str(cm.exception))

    def test_any_exception_while_listing_an_archive_is_a_named_refusal(self):
        for exc, cause in ((OverflowError("offset out of range"), "offset out of range"),
                           (struct.error(), "error")):
            with self.subTest(exc=type(exc).__name__):
                with mock.patch.object(zipfile.ZipFile, "infolist", side_effect=exc):
                    with self.assertRaises(self.m.Refusal) as cm:
                        self.m.read_archive(zip_bytes(release_entries("0.2.0")))
                self.assertIn("not a readable zip", str(cm.exception))
                self.assertIn(cause, str(cm.exception))

    def test_the_payload_cap_refusal_is_not_renamed_by_the_catch_all(self):
        # Pass the declared-size check, then let the stream run past the cap inside the loop.
        blob = zip_bytes(release_entries("0.2.0"))
        declared = sum(i.file_size for i in zipfile.ZipFile(io.BytesIO(blob)).infolist())
        with mock.patch.object(self.m, "MAX_PAYLOAD", declared + 10), \
                mock.patch.object(zipfile.ZipFile, "open",
                                  lambda zf, *a, **k: io.BytesIO(b"x" * (declared + 11))):
            with self.assertRaises(self.m.Refusal) as cm:
                self.m.read_archive(blob)
        message = str(cm.exception)
        self.assertIn("exceeds", message)
        self.assertNotIn("cannot read", message)
        self.assertNotIn("declares", message)

    # -- 7.4 build prints archive-derived names escaped -------------------------------------

    def test_build_prints_non_ascii_payload_names_escaped(self):
        extra = {"references/café.md": b"# cafe\n"}
        path, payload = self.mini_release("0.2.0", extra=extra)
        r = self.run_main(["build", "--source", path, "--release", "v0.2.0"])
        self.assertOk(r)
        self.assertTrue(r.out.isascii(), "build output must be ASCII: %r" % r.out)
        self.assertIn("caf\\xe9.md", r.out)
        self.assertPackages(self.cwd, payload, "0.2.0")

    # -- 7.5 a response shorter than its Content-Length is refused ---------------------------

    def test_a_response_shorter_than_its_content_length_is_refused_naming_the_url(self):
        blob = zip_bytes(release_entries("0.2.0"))
        url = codeload_url("v0.2.0")
        fake = FakeGitHub({url: lambda req: real_http_response(req, blob[: len(blob) // 2], len(blob))})
        with self.assertRaises(self.m.Refusal) as cm:
            self.m.download(url, self.opener(fake))
        message = str(cm.exception)
        self.assertIn(url, message)
        self.assertIn("closed after %s of %s bytes" % (format(len(blob) // 2, ","), format(len(blob), ",")),
                      message)

    def test_a_complete_real_response_is_read(self):
        blob = zip_bytes(release_entries("0.2.0"))
        url = codeload_url("v0.2.0")
        fake = FakeGitHub({url: lambda req: real_http_response(req, blob, len(blob))})
        self.assertEqual(self.m.download(url, self.opener(fake)), blob)

    def test_a_short_release_download_installs_nothing(self):
        blob = zip_bytes(release_entries("0.2.0"))
        routes = github_routes("v0.2.0", {"v0.2.0": blob})
        routes[codeload_url("v0.2.0")] = lambda req: real_http_response(req, blob[:100], len(blob))
        r = self.run_main(["install"], handler=FakeGitHub(routes))
        self.assertRefusedRun(r, archive_url("v0.2.0"), "connection closed")
        self.assertNothingWritten()

    # -- 8.2 frontmatter values and every printed line are escaped ---------------------------

    def test_check_escapes_a_format_character_in_the_archive_name(self):
        text = mini_skill_md("0.2.0").replace("name: okr-ninja", "name: okr-ninja\u202egnp")
        self.assertIn("\u202e", text)
        path = self.write_zip(release_entries("0.2.0", extra={"SKILL.md": text}))
        r = self.run_main(["check", "--source", path])
        self.assertEqual(r.code, 1)
        both = r.out + r.err
        self.assertNotIn("\u202e", both)
        self.assertTrue(both.isascii(), both)
        self.assertIn("\\u202e", both)

    def test_shown_escapes_control_and_format_characters_only(self):
        self.assertEqual(self.m.shown("caf\u00e9 /Users/Jos\u00e9"), "caf\u00e9 /Users/Jos\u00e9")
        self.assertEqual(self.m.shown("a\u202eb\x1bc\u2028d\ne"), "a\\u202eb\\x1bc\\u2028d\ne")

    def test_a_non_ascii_archive_name_is_escaped_in_the_name_rule_message(self):
        # printable non-ASCII passes the print filter, so only ascii() at the message escapes it
        text = mini_skill_md("0.2.0").replace("name: okr-ninja", "name: okr-ninja-ф")
        path = self.write_zip(release_entries("0.2.0", extra={"SKILL.md": text}))
        r = self.run_main(["check", "--source", path])
        self.assertEqual(r.code, 1)
        self.assertIn("is named 'okr-ninja-\\u0444'", r.out)
        self.assertIn("name 'okr-ninja-\\u0444' must use only", r.out)
        self.assertTrue((r.out + r.err).isascii(), r.out + r.err)

    def test_every_printed_line_passes_the_escape_filter(self):
        # a --source path is printed in the 'using' line and never goes through ascii()
        path, _ = self.mini_release("0.2.0")
        odd = path.with_name("rel‮eas.zip")
        os.rename(str(path), str(odd))
        r = self.run_main(["check", "--source", odd])
        self.assertOk(r)
        self.assertNotIn("‮", r.out + r.err)
        self.assertIn("rel\\u202eeas.zip", r.out)

    def test_a_terminal_that_cannot_encode_the_output_gives_no_traceback(self):
        # not isolated, so PYTHONIOENCODING applies: an ASCII-only stdout meets a non-ASCII path
        path, _ = self.mini_release("0.2.0")
        odd = path.with_name("café.zip")
        os.rename(str(path), str(odd))
        env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")}
        env.update({"HOME": str(self.home), "PYTHONIOENCODING": "ascii", "PYTHONDONTWRITEBYTECODE": "1"})
        p = subprocess.run([sys.executable, "-", "check", "--source", str(odd)],
                           input=INSTALL_PY.read_bytes(), cwd=str(self.cwd), env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn(b"Traceback", p.stderr + p.stdout)
        self.assertIn(b"caf\\xe9.zip", p.stdout)

    # -- 8.3 a deleted current folder --------------------------------------------------------

    @unittest.skipUnless(POSIX, "a process can stand in a deleted folder only on POSIX")
    def test_scenario_a_deleted_current_folder(self):
        path, payload = self.mini_release("0.2.0")
        gone = Path(self.mkdtemp("gone"))
        out = Path(self.mkdtemp("out"))
        script = ("import os, subprocess, sys\n"
                  "os.chdir(sys.argv[1]); os.rmdir(sys.argv[1])\n"
                  "src = open(sys.argv[2], 'rb').read()\n"
                  "res = []\n"
                  "for args in sys.argv[3:]:\n"
                  "    p = subprocess.run([sys.executable, '-I', '-'] + args.split('|'), input=src,\n"
                  "                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n"
                  "    res.append('%d %s' % (p.returncode, p.stderr.decode('ascii', 'replace').strip()))\n"
                  "print('\\n'.join(res))\n")
        runs = ["install|--source|%s" % path, "check|--source|%s" % path,
                "build|--source|%s" % path, "build|--source|%s|--out|%s" % (path, out)]
        env = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")}
        env["HOME"] = env["USERPROFILE"] = str(self.home)
        p = subprocess.run([sys.executable, "-I", "-c", script, str(gone), str(INSTALL_PY)] + runs,
                           env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=300)
        lines = p.stdout.decode("utf-8", "replace").splitlines()
        self.assertEqual(len(lines), 4, p.stdout + p.stderr)
        self.assertTrue(lines[0].startswith("0 "), lines[0])
        self.assertTrue(lines[1].startswith("0 "), lines[1])
        self.assertTrue(lines[2].startswith("1 "), lines[2])
        self.assertIn("current folder no longer exists", lines[2])
        self.assertIn("--out", lines[2])
        self.assertNotIn("Traceback", lines[2])
        self.assertTrue(lines[3].startswith("0 "), lines[3])
        self.assertPackages(out, payload, "0.2.0")
        self.assertHoldsExactly(self.home / ".claude" / "skills" / "okr-ninja", payload)

    # -- 8.4 a file named __pycache__ ships from neither reader ------------------------------

    def test_a_file_named_pycache_ships_from_neither_reader(self):
        extra = {"references/__pycache__": b"not a folder\n"}
        data, _ = self.m.read_archive(zip_bytes(release_entries("0.2.0", extra=extra)))
        self.assertNotIn("references/__pycache__", data)
        co = self.tmp / "co"
        write_files(co, {rel: b for rel, b in release_files("0.2.0", extra=extra).items()})
        self.assertNotIn("references/__pycache__", self.m.payload_files(co))
        self.assertIn("references/goodness-rubric.md", self.m.payload_files(co))


    # -- 9.1 a Unicode Path extra field is refused on every interpreter ----------------------

    def unicode_path(self, stored, shown_as):
        """An Info-ZIP Unicode Path extra field (0x7075) that renames `stored` to `shown_as`."""
        name = shown_as.encode("utf-8")
        return struct.pack("<HHBL", 0x7075, 5 + len(name), 1, zlib.crc32(stored.encode("utf-8"))) + name

    def timestamp(self):
        """The extended-timestamp extra field (0x5455) git archive writes on every entry."""
        return struct.pack("<HHBI", 0x5455, 5, 1, 1788220800)

    def test_a_unicode_path_extra_field_is_refused(self):
        rubric = self.P + "references/goodness-rubric.md"
        cases = {
            "a payload file renamed past the rules": (rubric, self.P + "references/x\\..\\..\\evil.md"),
            "a non-payload file renamed into the payload": (self.P + "CLAUDE.md", self.P + "references/evil.md"),
            "a payload file renamed onto another": (self.P + "references/alignment-taxonomy.md", rubric),
            "the same name": (rubric, rubric),
        }
        for label, (stored, shown_as) in cases.items():
            with self.subTest(label):
                extra = self.timestamp() + self.unicode_path(stored, shown_as)  # not the first field
                blob = zip_bytes(release_entries("0.2.0"), extras={stored: extra})
                info = zipfile.ZipFile(io.BytesIO(blob)).getinfo(stored) if stored == shown_as else next(
                    i for i in zipfile.ZipFile(io.BytesIO(blob)).infolist() if i.orig_filename == stored)
                if sys.version_info >= (3, 12):  # the rename this refusal guards against
                    self.assertEqual(info.filename, shown_as)
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.read_archive(blob)
                self.assertIn("0x7075", str(cm.exception))
                self.assertIn(ascii(stored), str(cm.exception))
                home, cwd = self.fresh()
                r = self.run_main(["install", "--source", self.write_zip(blob)], home=home, cwd=cwd)
                self.assertRefusedRun(r, "Unicode Path extra field (0x7075)")
                self.assertNothingWritten(home, cwd)

    def test_a_unicode_path_field_python_cannot_parse_is_refused(self):
        rubric = self.P + "references/goodness-rubric.md"
        crc = zlib.crc32(rubric.encode("utf-8"))
        cases = {
            "an empty field": struct.pack("<HH", 0x7075, 0),
            "a name that is not UTF-8": struct.pack("<HHBL", 0x7075, 7, 1, crc) + b"\xff\xfe",
            "an empty name": struct.pack("<HHBL", 0x7075, 5, 1, crc),
        }
        for label, field in cases.items():
            with self.subTest(label):
                blob = zip_bytes(release_entries("0.2.0"), extras={rubric: self.timestamp() + field})
                with warnings.catch_warnings(record=True) as seen:
                    warnings.simplefilter("always")
                    with self.assertRaises(self.m.Refusal) as cm:
                        self.m.read_archive(blob)
                self.assertEqual([str(w.message) for w in seen], [], "zipfile's warning reached the user")
                if sys.version_info < (3, 12):  # 3.12+ may find the zip unreadable first
                    self.assertIn(ascii(rubric), str(cm.exception))
                home, cwd = self.fresh()
                r = self.run_main(["install", "--source", self.write_zip(blob)], home=home, cwd=cwd)
                self.assertRefusedRun(r, "0x7075")
                self.assertNothingWritten(home, cwd)

    def test_other_extra_fields_are_read_as_git_archive_writes_them(self):
        entries = release_entries("0.2.0")
        blob = zip_bytes(entries, extras={e[0]: self.timestamp() for e in entries})
        data, _ = self.m.read_archive(blob)
        self.assertEqual(data, release_payload("0.2.0"))
        self.assertEqual(self.m.extra_ids(self.timestamp() + self.unicode_path("a", "b")), [0x5455, 0x7075])

    # -- 9.2, 9.3 every frontmatter text from an archive is escaped in check errors ----------

    def check_errors(self, text):
        path = self.write_zip(release_entries("0.2.0", extra={"SKILL.md": text}))
        r = self.run_main(["check", "--source", path])
        self.assertEqual(r.code, 1, r.out + r.err)
        self.assertNotIn("Traceback", r.err)
        self.assertTrue((r.out + r.err).isascii(), r.out + r.err)
        return r.out + r.err

    def test_a_non_ascii_metadata_key_is_escaped(self):
        key = "\\u043a\\u043b\\u044e\\u0447"  # printable Cyrillic, which the print filter keeps
        base = mini_skill_md("0.2.0")
        err = self.check_errors(base.replace('  version: "0.2.0"', '  version: "0.2.0"\n  \u043a\u043b\u044e\u0447: yes'))
        self.assertIn("'metadata.%s' as a non-string" % key, err)
        err = self.check_errors(base.replace('  version: "0.2.0"', '  version: "0.2.0"\n  \u043a\u043b\u044e\u0447 #x: v'))
        self.assertIn("'metadata key %s #x' contains ' #'" % key, err)

    def test_an_unexpected_non_ascii_key_is_escaped(self):
        err = self.check_errors(mini_skill_md("0.2.0").replace("license: MIT", "license: MIT\n\u043a\u043b\u044e\u0447: v"))
        self.assertIn("unexpected frontmatter key(s): '\\u043a\\u043b\\u044e\\u0447'", err)

    def test_a_duplicate_non_ascii_key_is_escaped(self):
        err = self.check_errors(mini_skill_md("0.2.0").replace("license: MIT", "license: MIT\n\u043a: v\n\u043a: w"))
        self.assertIn("duplicate key '\\u043a'", err)

    def test_a_non_ascii_version_is_escaped(self):
        err = self.check_errors(mini_skill_md(None, raw_version='"0.2.0-\u0444"'))
        self.assertIn("metadata.version '0.2.0-\\u0444' is not a semantic version", err)

    def test_an_install_write_error_names_the_file_escaped(self):
        # 256 x U+00E9 is 512 bytes in UTF-8 and 256 UTF-16 units: too long for one name anywhere
        long_name = "references/" + "\u00e9" * 256 + ".md"
        path, _ = self.mini_release("0.2.0", extra={long_name: b"# long\n"})
        r = self.run_main(["install", "--source", path])
        self.assertRefusedRun(r, "could not install", "already installed: none", "\\xe9" * 256)
        self.assertTrue((r.out + r.err).isascii(), r.err)
        for t in self.targets():
            self.assertFalse(os.path.lexists(str(t)), t)
            if t.parent.is_dir():
                self.assertEqual([n for n in os.listdir(str(t.parent)) if "staging" in n], [])


    # -- 11.1 a character this Python cannot case-fold is refused -----------------------------

    def test_a_code_point_this_python_does_not_assign_is_refused(self):
        self.assertIn("does not know", self.m.unportable("x\u0378.md"))  # unassigned through Unicode 16
        self.assertIsNone(self.m.unportable("caf\u00e9.md"))
        extra = {"references/x\u0378.md": b"x\n"}
        self.assertArchiveRefused(zip_bytes(release_entries("0.2.0", extra=extra)),
                                  "x\\u0378.md", "does not know")

    def test_a_case_pair_newer_than_this_pythons_unicode_is_refused(self):
        # U+A7C0/U+A7C1 arrived in Unicode 14, and APFS merges them. 3.12 folds them into one
        # key; 3.9 (Unicode 13) cannot, and refuses the character instead.
        extra = {"references/note-\ua7c0.md": b"FIRST\n", "references/note-\ua7c1.md": b"SECOND\n"}
        unicode14 = tuple(int(n) for n in unicodedata.unidata_version.split(".")) >= (14,)
        self.assertArchiveRefused(zip_bytes(release_entries("0.2.0", extra=extra)),
                                  "collide" if unicode14 else "does not know")


    # -- 13.1 entries that share one local header are refused, and so is any read warning -----

    def test_entries_that_share_one_local_header_are_refused(self):
        resume = self.P + "references/r\u00e9sum\u00e9.md"
        blob = zip_bytes(release_entries("0.2.0", extra={"references/r\u00e9sum\u00e9.md": b"# cv\n"}),
                         compress=zipfile.ZIP_STORED)
        for label, alias, shown in (("outside the payload", "evals/\u00ff.md", "evals/\\xff.md"),
                                    ("inside the payload", "references/c\u00f3pia.md", "references/c\\xf3pia.md")):
            with self.subTest(label):
                aliased = alias_entry(blob, resume, self.P + alias)
                self.assertEqual(len(zipfile.ZipFile(io.BytesIO(aliased)).infolist()),
                                 len(zipfile.ZipFile(io.BytesIO(blob)).infolist()) + 1)
                with warnings.catch_warnings(record=True) as seen:
                    warnings.simplefilter("always")  # 3.12 warns 'Overlapped entries' when it reads one
                    self.assertArchiveRefused(aliased, "share one local header", "r\\xe9sum\\xe9.md", shown)
                self.assertEqual([str(w.message) for w in seen], [])

    def test_a_zipfile_warning_while_reading_is_a_named_refusal(self):
        real_open = zipfile.ZipFile.open

        def warning_open(zf, *a, **k):
            warnings.warn("Overlapped entries: 'caf\u00e9.md' (possible zip bomb)")
            return real_open(zf, *a, **k)
        with mock.patch.object(zipfile.ZipFile, "open", warning_open):
            with warnings.catch_warnings(record=True) as seen:
                warnings.simplefilter("always")
                with self.assertRaises(self.m.Refusal) as cm:
                    self.m.read_archive(zip_bytes(release_entries("0.2.0")))
        self.assertEqual([str(w.message) for w in seen], [])
        self.assertIn("cannot read", str(cm.exception))
        self.assertIn("caf\\xe9.md", str(cm.exception))
        self.assertTrue(str(cm.exception).isascii(), str(cm.exception))

    # -- 13.2 a Unicode Path field in the local header alone is refused ----------------------

    def test_a_unicode_path_field_in_the_local_header_alone_is_refused(self):
        rubric = self.P + "references/goodness-rubric.md"
        extra = self.timestamp() + self.unicode_path(rubric, self.P + "references/x\\..\\..\\evil.md")
        blob = bytearray(zip_bytes(release_entries("0.2.0"), extras={rubric: extra}))
        _, central = entry_offsets(bytes(blob), rubric)
        at = central[0] + 46 + struct.unpack_from("<H", blob, central[0] + 28)[0] + len(self.timestamp())
        self.assertEqual(struct.unpack_from("<H", blob, at)[0], 0x7075)
        struct.pack_into("<H", blob, at, 0x6666)  # only the central copy stops naming the field
        info = zipfile.ZipFile(io.BytesIO(bytes(blob))).getinfo(rubric)
        self.assertNotIn(0x7075, self.m.extra_ids(info.extra))
        self.assertEqual(info.filename, rubric, "no interpreter renames from the local header")
        self.assertArchiveRefused(bytes(blob), "0x7075", ascii(rubric))


if __name__ == "__main__":
    unittest.main()
