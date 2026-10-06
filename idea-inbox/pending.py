#!/usr/bin/env python3
"""Cloud-side helper for the idea-triage skill.

  python3 idea-inbox/pending.py              list unprocessed items and the Mac's health
  python3 idea-inbox/pending.py --mark ID... --digest ideas/2026-10-02/DIGEST.md
                                             record items as triaged

Processed ids live in idea-inbox/state/processed.json, which is tracked, so a
fresh session each night knows what earlier nights already handled.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "inbox"
STATE = ROOT / "state" / "processed.json"
STALE_HOURS = 30


def load_processed():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def heartbeat_report():
    hb_path = INBOX / "HEARTBEAT.json"
    if not hb_path.exists():
        return {"ok": False, "problems": ["The Mac collector has never pushed. Is install.sh done?"]}
    hb = json.loads(hb_path.read_text())
    problems = []
    last = datetime.strptime(hb["last_run"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    age_h = (datetime.now(timezone.utc) - last).total_seconds() / 3600
    if age_h > STALE_HOURS:
        problems.append(f"Mac collector last ran {age_h:.0f} hours ago. Is the Mac mini on and logged in?")
    for name, s in hb.get("sources", {}).items():
        if not s.get("ok"):
            problems.append(f"{name} failed on the Mac: {s.get('error')}")
        for w in s.get("warnings") or []:
            problems.append(f"{name}: {w}")
    return {"ok": not problems, "last_run": hb["last_run"], "problems": problems}


def list_pending():
    done = load_processed()
    items = []
    for p in sorted(INBOX.glob("*/item.json")):
        item = json.loads(p.read_text())
        if item["id"] in done:
            continue
        folder = p.parent
        files = sorted(str(f.relative_to(ROOT.parent)) for f in folder.rglob("*") if f.is_file())
        items.append({
            "id": item["id"],
            "source": item.get("source_label", item["source"]),
            "received_at": item["received_at"],
            "note_text": item.get("note_text", ""),
            "folder": str(folder.relative_to(ROOT.parent)),
            "files": files,
            "media_errors": [e for m in item.get("media", []) for e in m.get("errors", [])],
        })
    print(json.dumps({"mac_health": heartbeat_report(), "pending_count": len(items), "pending": items}, indent=2))


def mark(ids, digest):
    done = load_processed()
    known = {json.loads(p.read_text())["id"] for p in INBOX.glob("*/item.json")}
    missing = [i for i in ids if i not in known]
    if missing:
        sys.exit(f"unknown item ids: {missing}")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for i in ids:
        done[i] = {"triaged_at": now, "digest": digest}
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(done, indent=2, sort_keys=True) + "\n")
    print(f"marked {len(ids)} item(s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mark", nargs="+")
    ap.add_argument("--digest")
    a = ap.parse_args()
    if a.mark:
        if not a.digest:
            sys.exit("--digest is required with --mark")
        mark(a.mark, a.digest)
    else:
        list_pending()
