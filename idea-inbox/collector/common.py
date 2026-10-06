"""Shared pieces for the Mac-side collector: paths, config, state, bundles.

Everything private lives in ~/.idea-inbox, outside the repo and outside
iCloud: the config (your own phone number), the run state, and the outbox
of bundles waiting to be pushed.
"""

import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.environ.get("IDEA_INBOX_HOME", Path.home() / ".idea-inbox"))
CONFIG_PATH = HOME / "config.json"
STATE_PATH = HOME / "state.json"
OUTBOX = HOME / "outbox"
LOG_DIR = HOME / "logs"

# Messages sent within this many seconds of each other become one item, so a
# shared reel followed by "could this work for the temple drops?" stays together.
GROUP_WINDOW_SECONDS = 300

URL_RE = re.compile(r"https?://[^\s<>\"']+")


def load_config():
    if not CONFIG_PATH.exists():
        raise SystemExit(f"Missing {CONFIG_PATH}. Run idea-inbox/mac/install.sh first.")
    return json.loads(CONFIG_PATH.read_text())


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def save_state(state):
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(STATE_PATH)


def utc_iso(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find_urls(text):
    return [u.rstrip(").,!?") for u in URL_RE.findall(text or "")]


def group_messages(messages, window=GROUP_WINDOW_SECONDS):
    """Split time-sorted messages into bursts. Each message needs a 'time' datetime."""
    groups = []
    for m in messages:
        if groups and (m["time"] - groups[-1][-1]["time"]).total_seconds() <= window:
            groups[-1].append(m)
        else:
            groups.append([m])
    return groups


def new_bundle(source, first_time, key):
    """Create an empty bundle folder in the outbox and return (item_id, path)."""
    digest = hashlib.sha1(f"{source}:{key}".encode()).hexdigest()[:8]
    stamp = first_time.astimezone(timezone.utc).strftime("%Y%m%d-%H%M")
    item_id = f"{source}-{stamp}-{digest}"
    path = OUTBOX / item_id
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    return item_id, path


def write_item(path, item):
    (path / "item.json").write_text(json.dumps(item, indent=2, ensure_ascii=False))
