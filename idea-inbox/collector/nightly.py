#!/usr/bin/env python3
"""Nightly Mac collector. launchd runs this at 1:15 AM.

  1. Collect new items from the iMessage note-to-self thread into
     ~/.idea-inbox/outbox (one folder per item).
  2. Copy them into a dedicated clone of the repo at ~/.idea-inbox/repo,
     write HEARTBEAT.json, commit, and push to main.
  3. Clear the outbox only after the push lands, so a failed push loses nothing.

The dedicated clone keeps this job away from your iCloud checkout: it never
switches your branches, never touches your uncommitted work, and git's files
are never half-synced by iCloud while it runs.

  python3 nightly.py --check     test access to everything, change nothing
  python3 nightly.py --dry-run   collect into the outbox, skip git
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common  # noqa: E402
import imessage  # noqa: E402
import media  # noqa: E402

INBOX_REL = Path("idea-inbox") / "inbox"
BRANCH = "main"


def log(msg):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


def git(repo, *args, check=True):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {args[0]} failed: {(r.stderr or r.stdout).strip()[:500]}")
    return r


def run_check(config):
    ok_all = True

    def report(ok, name, msg):
        nonlocal ok_all
        ok_all &= ok
        print(f"[{'OK' if ok else 'FAIL'}] {name}: {msg}")

    report(media.have("ffmpeg") and media.have("ffprobe"), "ffmpeg",
           "found" if media.have("ffmpeg") else "missing: brew install ffmpeg")
    try:
        import faster_whisper  # noqa: F401
        report(True, "whisper", "faster-whisper installed")
    except ImportError:
        report(False, "whisper", "faster-whisper missing: re-run install.sh")
    if config.get("imessage_enabled", True):
        report(*_named(imessage.check(), "iMessage"))
        if not config.get("self_handles"):
            report(False, "iMessage", "self_handles is empty in ~/.idea-inbox/config.json")
    repo = Path(config.get("repo_path", common.HOME / "repo"))
    r = git(repo, "ls-remote", "--heads", "origin", BRANCH, check=False)
    report(r.returncode == 0, "git", f"can reach origin from {repo}" if r.returncode == 0 else r.stderr.strip()[:300])
    print("\nAll checks passed." if ok_all else "\nFix the FAIL lines above, then run --check again.")
    return 0 if ok_all else 1


def _named(result, name):
    ok, msg = result
    return ok, name, msg


def collect(config, state):
    status = {}
    for name, enabled, fn in (
        ("imessage", config.get("imessage_enabled", True), lambda: (imessage.collect(config, state), [])),
    ):
        if not enabled:
            status[name] = {"ok": True, "skipped": "disabled in config"}
            continue
        try:
            made, warnings = fn()
            if name == "imessage" and state.get("imessage", {}).get("warning"):
                warnings = [state["imessage"]["warning"]]
            status[name] = {"ok": True, "new_items": len(made), "warnings": warnings}
            log(f"{name}: {len(made)} new item(s)")
        except Exception as e:
            status[name] = {"ok": False, "error": f"{type(e).__name__}: {e}"}
            log(f"{name} FAILED: {e}\n{traceback.format_exc()}")
        common.save_state(state)  # outbox already holds the bundles, so advancing is safe
    return status


def push(config, status):
    repo = Path(config.get("repo_path", common.HOME / "repo"))
    git(repo, "fetch", "origin", BRANCH)
    git(repo, "checkout", "-q", BRANCH)
    git(repo, "reset", "-q", "--hard", f"origin/{BRANCH}")  # dedicated clone: nothing local to keep

    inbox = repo / INBOX_REL
    inbox.mkdir(parents=True, exist_ok=True)
    bundles = sorted(p for p in common.OUTBOX.iterdir() if p.is_dir()) if common.OUTBOX.exists() else []
    for b in bundles:
        dest = inbox / b.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(b, dest)

    heartbeat = {
        "last_run": common.utc_iso(datetime.now(timezone.utc)),
        "items_pushed": [b.name for b in bundles],
        "sources": status,
    }
    (inbox / "HEARTBEAT.json").write_text(json.dumps(heartbeat, indent=2) + "\n")

    git(repo, "add", str(INBOX_REL))
    if not git(repo, "status", "--porcelain", str(INBOX_REL)).stdout.strip():
        log("nothing to commit")
        return
    msg = f"Idea inbox: {len(bundles)} new item(s) from the Mac collector"
    git(repo, "commit", "-q", "-m", msg)
    for attempt in range(5):
        r = git(repo, "push", "-q", "origin", BRANCH, check=False)
        if r.returncode == 0:
            break
        log(f"push failed ({r.stderr.strip()[:200]}), retrying")
        time.sleep(2 ** (attempt + 1))
        git(repo, "pull", "-q", "--rebase", "origin", BRANCH, check=False)
    else:
        raise RuntimeError("push failed 5 times; items stay in the outbox for tomorrow")
    for b in bundles:
        shutil.rmtree(b)
    log(f"pushed {len(bundles)} item(s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    config = common.load_config()
    if args.check:
        return run_check(config)
    # The Mac mini sleeps after a minute idle. caffeinate holds it awake until this
    # process exits. Started as a child, not as the launchd program, so Full Disk
    # Access is still checked against this Python.
    subprocess.Popen(["/usr/bin/caffeinate", "-i", "-w", str(os.getpid())])
    common.OUTBOX.mkdir(parents=True, exist_ok=True)
    state = common.load_state()
    status = collect(config, state)
    if args.dry_run:
        log(f"dry run: bundles are in {common.OUTBOX}")
        return 0
    push(config, status)
    return 0


if __name__ == "__main__":
    sys.exit(main())
