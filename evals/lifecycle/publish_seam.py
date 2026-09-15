#!/usr/bin/env python3
"""Publish seam — a local stand-in for the artifact surface, for lifecycle eval runs only.

A run given this seam publishes through it instead of to the real artifact surface, and follows
the publish decision procedure in `references/report-format.md` ("Artifact lifecycle") unchanged:
the working folder's `artifacts.json` registry still decides update-vs-create.

Operations (there are deliberately only three — there is no listing operation, because the
contract forbids deciding update-vs-create by listing artifacts or matching titles):

  read   --url URL                                  verify a URL: exit 0 = reachable, exit 3 = dead
  publish --key KEY --title T --favicon F --file P  create a new artifact, print its URL
  update  --key KEY --url URL --file P [--title T] [--favicon F]
                                                    update the artifact at URL in place

Every operation is appended to the store's ledger, so a run's publish decisions can be graded
after the fact. State lives in one JSON file named by --store (or $OKR_SEAM_STORE); nothing
touches the network. Python 3 standard library only.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path

URL_PREFIX = "https://artifacts.test/a/"


def now_iso():
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def store_path(args):
    p = args.store or os.environ.get("OKR_SEAM_STORE")
    if not p:
        fail("no store given: pass --store <path> (or set OKR_SEAM_STORE)")
    return Path(p)


def load_store(p):
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"artifacts": {}, "ledger": [], "seq": 0}


def save_store(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fail(msg, code=2, **extra):
    print(json.dumps({"ok": False, "error": msg, **extra}, ensure_ascii=False))
    sys.exit(code)


def record(store, **event):
    store["seq"] = store.get("seq", 0) + 1
    store["ledger"].append({"n": store["seq"], "at": now_iso(), **event})
    return store["ledger"][-1]


def content_of(path):
    p = Path(path)
    if not p.exists() or p.is_dir():
        fail("file not found: %s" % path)
    b = p.read_bytes()
    return hashlib.sha256(b).hexdigest(), len(b)


def new_url(store, key):
    seed = "%s:%d" % (key, store.get("seq", 0) + 1)
    return URL_PREFIX + hashlib.sha1(seed.encode("utf-8")).hexdigest()[:8]


def cmd_read(args):
    sp = store_path(args)
    store = load_store(sp)
    art = store["artifacts"].get(args.url)
    record(store, op="read", url=args.url, result="alive" if art else "dead")
    save_store(sp, store)
    if not art:
        print(json.dumps({"ok": False, "url": args.url, "reason": "no such artifact"}, ensure_ascii=False))
        sys.exit(3)
    print(json.dumps({"ok": True, "url": args.url, "title": art["title"], "favicon": art["favicon"],
                      "versions": art["versions"]}, ensure_ascii=False))


def cmd_publish(args):
    sp = store_path(args)
    store = load_store(sp)
    sha, size = content_of(args.file)
    url = new_url(store, args.key)
    store["artifacts"][url] = {"url": url, "title": args.title, "favicon": args.favicon,
                              "created_at": now_iso(), "updated_at": now_iso(), "versions": 1,
                              "content_sha": sha, "bytes": size}
    record(store, op="publish", key=args.key, url=url, title=args.title, favicon=args.favicon, content_sha=sha)
    save_store(sp, store)
    print(json.dumps({"ok": True, "op": "publish", "key": args.key, "url": url, "title": args.title,
                      "favicon": args.favicon}, ensure_ascii=False))


def cmd_update(args):
    sp = store_path(args)
    store = load_store(sp)
    art = store["artifacts"].get(args.url)
    if not art:
        record(store, op="update_failed", key=args.key, url=args.url, reason="no such artifact")
        save_store(sp, store)
        fail("cannot update: no artifact at %s" % args.url, code=3, url=args.url, key=args.key)
    sha, size = content_of(args.file)
    if args.title:
        art["title"] = args.title
    if args.favicon:
        art["favicon"] = args.favicon
    art.update({"updated_at": now_iso(), "versions": art["versions"] + 1, "content_sha": sha, "bytes": size})
    record(store, op="update", key=args.key, url=args.url, title=art["title"], favicon=art["favicon"], content_sha=sha)
    save_store(sp, store)
    print(json.dumps({"ok": True, "op": "update", "key": args.key, "url": args.url, "title": art["title"],
                      "favicon": art["favicon"], "versions": art["versions"]}, ensure_ascii=False))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="publish_seam.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--store", help="path to this run's seam store (default: $OKR_SEAM_STORE)")

    p = sub.add_parser("read", parents=[common], help="verify a URL (exit 0 reachable, exit 3 dead)")
    p.add_argument("--url", required=True)
    p.set_defaults(fn=cmd_read)

    p = sub.add_parser("publish", parents=[common], help="create a new artifact and print its URL")
    p.add_argument("--key", required=True, help="deliverable key this artifact is for")
    p.add_argument("--title", required=True)
    p.add_argument("--favicon", required=True)
    p.add_argument("--file", required=True, help="file whose content is published")
    p.set_defaults(fn=cmd_publish)

    p = sub.add_parser("update", parents=[common], help="update the artifact at URL in place")
    p.add_argument("--key", required=True, help="deliverable key this artifact is for")
    p.add_argument("--url", required=True)
    p.add_argument("--file", required=True)
    p.add_argument("--title")
    p.add_argument("--favicon")
    p.set_defaults(fn=cmd_update)

    args = ap.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
