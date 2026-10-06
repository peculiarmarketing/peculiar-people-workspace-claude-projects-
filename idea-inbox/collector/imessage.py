"""Read new messages from your own note-to-self iMessage thread.

Messages keeps its history in ~/Library/Messages/chat.db, a SQLite file. macOS
blocks every program from reading it unless that program has Full Disk Access,
which is why install.sh asks you to grant it to the collector's Python.

Only chats whose sole participant is one of your own handles (config
"self_handles") are read. Every other conversation is filtered out in the SQL
query itself, so its text never enters this process's results.
"""

import shutil
import sqlite3
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from common import find_urls, group_messages, new_bundle, utc_iso, write_item
import media

CHAT_DB = Path.home() / "Library" / "Messages" / "chat.db"
APPLE_EPOCH = datetime(2001, 1, 1, tzinfo=timezone.utc)
FIRST_RUN_LOOKBACK_DAYS = 2


class AccessDenied(Exception):
    pass


def normalize_handle(h):
    h = (h or "").strip().lower()
    if "@" in h:
        return h
    digits = "".join(c for c in h if c.isdigit())
    return digits[-10:]  # US numbers: ignore +1 and formatting


def apple_time(value):
    # Since High Sierra, message.date is nanoseconds since 2001; before, seconds.
    if value is None:
        return APPLE_EPOCH
    seconds = value / 1e9 if value > 1e12 else value
    return APPLE_EPOCH + timedelta(seconds=seconds)


def decode_attributed_body(blob):
    """Recent macOS often leaves message.text empty and stores the text in a
    typedstream blob. The string follows the NSString class marker, prefixed
    by a length that is one byte, or 0x81 + 2 bytes, or 0x82 + 4 bytes."""
    if not blob:
        return None
    i = blob.find(b"NSString")
    if i == -1:
        return None
    i += len(b"NSString") + 5
    if i >= len(blob):
        return None
    n = blob[i]
    i += 1
    if n == 0x81:
        n = int.from_bytes(blob[i:i + 2], "little")
        i += 2
    elif n == 0x82:
        n = int.from_bytes(blob[i:i + 4], "little")
        i += 4
    return blob[i:i + n].decode("utf-8", errors="replace") or None


def open_snapshot(tmpdir):
    """Copy chat.db (and its WAL files) so we never hold a lock on the live database."""
    try:
        for suffix in ("", "-wal", "-shm"):
            src = Path(str(CHAT_DB) + suffix)
            if src.exists():
                shutil.copy2(src, Path(tmpdir) / ("chat.db" + suffix))
    except PermissionError as e:
        raise AccessDenied(
            "macOS refused to let Python read the Messages database. Grant Full Disk "
            "Access to the Python path that install.sh printed, then run --check again."
        ) from e
    conn = sqlite3.connect(f"file:{Path(tmpdir) / 'chat.db'}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def columns(conn, table):
    return {r["name"] for r in conn.execute(f"PRAGMA table_info({table})")}


def self_chat_ids(conn, self_handles):
    wanted = {normalize_handle(h) for h in self_handles}
    ids = []
    for chat in conn.execute("SELECT ROWID, chat_identifier FROM chat"):
        handles = [r["id"] for r in conn.execute(
            "SELECT h.id FROM chat_handle_join chj JOIN handle h ON h.ROWID = chj.handle_id "
            "WHERE chj.chat_id = ?", (chat["ROWID"],))]
        normalized = {normalize_handle(h) for h in handles}
        if normalized:
            if normalized <= wanted and len(normalized) == 1:
                ids.append(chat["ROWID"])
        elif normalize_handle(chat["chat_identifier"]) in wanted:
            ids.append(chat["ROWID"])
    return ids


def check():
    if not CHAT_DB.exists():
        return False, f"{CHAT_DB} not found. Is Messages set up on this Mac?"
    try:
        with tempfile.TemporaryDirectory() as tmp:
            conn = open_snapshot(tmp)
            n = conn.execute("SELECT COUNT(*) FROM message").fetchone()[0]
            conn.close()
        return True, f"Messages database readable ({n} messages total)."
    except AccessDenied as e:
        return False, str(e)


def collect(config, state):
    """Write one bundle per burst of new self-messages. Returns list of item ids."""
    self_handles = config.get("self_handles") or []
    if not self_handles:
        raise RuntimeError("config self_handles is empty: add the number or email you text yourself at")
    st = state.setdefault("imessage", {})
    made = []
    with tempfile.TemporaryDirectory() as tmp:
        conn = open_snapshot(tmp)
        chats = self_chat_ids(conn, self_handles)
        if not chats:
            st["warning"] = "no note-to-self chat found for the configured self_handles"
            return made
        mcols = columns(conn, "message")
        last_rowid = st.get("last_rowid")
        params = list(chats)
        where = f"cmj.chat_id IN ({','.join('?' * len(chats))})"
        if last_rowid is None:
            cutoff = datetime.now(timezone.utc) - timedelta(days=FIRST_RUN_LOOKBACK_DAYS)
            ns = int((cutoff - APPLE_EPOCH).total_seconds() * 1e9)
            where += " AND m.date > ?"
            params.append(ns)
        else:
            where += " AND m.ROWID > ?"
            params.append(last_rowid)
        if "associated_message_type" in mcols:
            where += " AND COALESCE(m.associated_message_type, 0) = 0"  # skip tapbacks
        body = "m.attributedBody" if "attributedBody" in mcols else "NULL AS attributedBody"
        rows = conn.execute(
            f"SELECT m.ROWID, m.guid, m.text, {body}, m.date FROM message m "
            f"JOIN chat_message_join cmj ON cmj.message_id = m.ROWID "
            f"WHERE {where} ORDER BY m.ROWID", params).fetchall()

        msgs, seen = [], set()
        for r in rows:
            text = r["text"] or decode_attributed_body(r["attributedBody"]) or ""
            text = text.replace("￼", "").strip()  # object-replacement char marks attachments
            t = apple_time(r["date"])
            atts = [dict(a) for a in conn.execute(
                "SELECT a.filename, a.mime_type, a.transfer_name FROM attachment a "
                "JOIN message_attachment_join maj ON maj.attachment_id = a.ROWID "
                "WHERE maj.message_id = ?", (r["ROWID"],))
                # Link-preview cards, not real attachments; the link itself is in the text.
                if not (a["transfer_name"] or a["filename"] or "").endswith(".pluginPayloadAttachment")]
            # A note-to-self can be stored twice (sent and received copies).
            key = (text, tuple(a["transfer_name"] for a in atts), int(t.timestamp()) // 10)
            if key in seen:
                continue
            seen.add(key)
            msgs.append({"rowid": r["ROWID"], "guid": r["guid"], "time": t,
                         "text": text, "attachments": atts})
        max_rowid = conn.execute("SELECT COALESCE(MAX(ROWID), 0) FROM message").fetchone()[0]
        conn.close()

    for group in group_messages(msgs):
        item_id, bundle = new_bundle("imessage", group[0]["time"], group[0]["guid"])
        texts = [m["text"] for m in group if m["text"]]
        urls = [u for t in texts for u in find_urls(t)]
        item = {
            "id": item_id,
            "source": "imessage",
            "source_label": "iMessage note to self",
            "received_at": utc_iso(group[0]["time"]),
            "messages": [{"time": utc_iso(m["time"]), "text": m["text"],
                          "attachments": [a["transfer_name"] for a in m["attachments"]]}
                         for m in group],
            "note_text": "\n".join(texts),
            "links": urls,
            "media": [],
        }
        vid = 1
        for m in group:
            for a in m["attachments"]:
                src = Path(str(a["filename"] or "").replace("~", str(Path.home()), 1))
                mime = a["mime_type"] or ""
                name = a["transfer_name"] or src.name
                if not src.exists():
                    item["media"].append({"kind": "missing", "name": name,
                                          "errors": ["attachment not downloaded to this Mac"]})
                elif mime.startswith("image/"):
                    item["media"].append(media.process_image(src, bundle, name))
                elif mime.startswith("video/"):
                    r = media.process_video(src, bundle, f"video{vid}", config.get("whisper_model", "small"))
                    r["name"] = name
                    item["media"].append(r)
                    vid += 1
                else:
                    item["media"].append({"kind": "file", "name": name, "mime": mime,
                                          "errors": ["file type not processed"]})
        item["media"] += media.process_links(urls, bundle, config, start_index=vid)
        write_item(bundle, item)
        made.append(item_id)
        st["last_rowid"] = max(m["rowid"] for m in group)
    if msgs:
        st["last_rowid"] = max(st.get("last_rowid") or 0, msgs[-1]["rowid"])
    elif last_rowid is None:
        st["last_rowid"] = max_rowid  # first run, nothing recent: start from now
    st.pop("warning", None)
    return made
