"""Read new messages from two Instagram chats on the business account.

Uses Meta's Instagram API with Instagram Login (graph.instagram.com). This
works only for a Business or Creator account and needs a token with
instagram_business_basic and instagram_business_manage_messages.

Only two conversations are ever read:
  - ig-personal: the business account's chat with your personal account
    (config "ig_personal_username")
  - ig-self: the business account's chat with itself, if Instagram exposes it
Every other conversation (customers, collaborators) is skipped by username
before any of its messages are requested.

Two API limits that shape this file:
  - Only the 20 most recent messages in a conversation can be read. A nightly
    run keeps up unless you share more than 20 things in one day.
  - Long-lived tokens expire after 60 days. The token is refreshed here once a
    week, and the new one is written back to ~/.idea-inbox/.env.
"""

import json
import tempfile
from datetime import datetime, timedelta, timezone

import requests

from common import find_urls, group_messages, load_env, new_bundle, save_env, utc_iso, write_item
import media

API = "https://graph.instagram.com"
REFRESH_EVERY_DAYS = 7
MESSAGE_FIELDS = "id,created_time,from,to,message,attachments,shares,story,is_unsupported"
MESSAGE_FIELDS_MIN = "id,created_time,from,to,message"


class ApiError(Exception):
    pass


def _get(path, token, version, **params):
    params["access_token"] = token
    url = path if path.startswith("http") else f"{API}/{version}/{path.lstrip('/')}"
    r = requests.get(url, params=params, timeout=60)
    try:
        data = r.json()
    except ValueError:
        data = {}
    if r.status_code != 200 or "error" in data:
        err = data.get("error", {})
        raise ApiError(f"{r.status_code} {err.get('type', '')} {err.get('message', r.text[:200])}")
    return data


def _token():
    env = load_env()
    token = env.get("IG_ACCESS_TOKEN")
    if not token:
        raise ApiError("IG_ACCESS_TOKEN is not set in ~/.idea-inbox/.env")
    return env, token


def maybe_refresh(env, token):
    """Swap the token for a fresh 60-day one about once a week. Returns the token to use."""
    last = env.get("IG_TOKEN_REFRESHED_AT")
    if last:
        try:
            if datetime.now(timezone.utc) - datetime.fromisoformat(last) < timedelta(days=REFRESH_EVERY_DAYS):
                return token, None
        except ValueError:
            pass
    r = requests.get(f"{API}/refresh_access_token",
                     params={"grant_type": "ig_refresh_token", "access_token": token}, timeout=60)
    data = r.json() if r.content else {}
    if r.status_code != 200 or "access_token" not in data:
        return token, f"token refresh failed: {data.get('error', {}).get('message', r.status_code)}"
    env["IG_ACCESS_TOKEN"] = data["access_token"]
    env["IG_TOKEN_REFRESHED_AT"] = datetime.now(timezone.utc).isoformat()
    days = int(data.get("expires_in", 0)) // 86400
    env["IG_TOKEN_EXPIRES_ON"] = (datetime.now(timezone.utc) + timedelta(days=days)).date().isoformat()
    save_env(env)
    return data["access_token"], None


def check(config):
    try:
        env, token = _token()
        me = _get("me", token, config.get("ig_api_version", "v23.0"), fields="user_id,username")
        exp = env.get("IG_TOKEN_EXPIRES_ON", "unknown (refreshes on the first nightly run)")
        return True, f"Instagram API OK as @{me.get('username')}. Token expires: {exp}."
    except (ApiError, requests.RequestException) as e:
        return False, f"Instagram API not ready: {e}"


def _parse_time(s):
    # Meta returns e.g. 2026-10-01T08:12:45+0000
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")


def _usernames(conv):
    return [p.get("username", "").lower() for p in conv.get("participants", {}).get("data", [])]


def _fetch_message(mid, token, version):
    try:
        return _get(mid, token, version, fields=MESSAGE_FIELDS)
    except ApiError:
        return _get(mid, token, version, fields=MESSAGE_FIELDS_MIN)


def _media_urls(obj, found=None):
    """Collect every URL in an attachment or share payload. The exact shape Meta
    uses for a shared reel varies, so walk the whole object rather than guess keys."""
    found = [] if found is None else found
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and v.startswith("http") and k in ("url", "link", "file_url", "preview_url", "video_url"):
                found.append(v)
            else:
                _media_urls(v, found)
    elif isinstance(obj, list):
        for v in obj:
            _media_urls(v, found)
    return found


def collect(config, state):
    version = config.get("ig_api_version", "v23.0")
    personal = (config.get("ig_personal_username") or "").lower().lstrip("@")
    st = state.setdefault("instagram", {})
    seen_list = list(st.get("seen_message_ids", []))  # oldest first, trimmed to the last 1000
    seen = set(seen_list)
    warnings = []

    env, token = _token()
    token, warn = maybe_refresh(env, token)
    if warn:
        warnings.append(warn)
    me = _get("me", token, version, fields="user_id,username")
    business = (me.get("username") or "").lower()

    convs = _get("me/conversations", token, version, platform="instagram",
                 fields="participants,updated_time").get("data", [])
    targets = []
    for c in convs:
        names = set(_usernames(c))
        if names and names <= {business}:
            targets.append(("ig-self", "Instagram, business account to itself", c))
        elif personal and personal in names and names <= {business, personal}:
            targets.append(("ig-personal", "Instagram, personal account to business", c))
    if not any(t[0] == "ig-personal" for t in targets):
        warnings.append(f"no conversation with @{personal} found on @{business}")
    if not any(t[0] == "ig-self" for t in targets):
        warnings.append("Instagram did not expose a self-chat; share to the business account from personal instead")

    made = []
    for source, label, conv in targets:
        listing = _get(conv["id"], token, version, fields="messages").get("messages", {}).get("data", [])
        new = []
        for m in listing:
            if m["id"] in seen:
                continue
            full = _fetch_message(m["id"], token, version)
            full["time"] = _parse_time(full["created_time"])
            new.append(full)
        if len(listing) >= 20 and len(new) >= 20:
            warnings.append(f"{source}: 20 or more new messages; the API only shows the latest 20, so some may be missed")
        new.sort(key=lambda m: m["time"])
        for group in group_messages(new):
            item_id, bundle = new_bundle(source, group[0]["time"], group[0]["id"])
            texts = [m.get("message", "") for m in group if m.get("message")]
            links = [u for t in texts for u in find_urls(t)]
            item = {
                "id": item_id,
                "source": source,
                "source_label": label,
                "received_at": utc_iso(group[0]["time"]),
                "messages": [{"time": utc_iso(m["time"]), "text": m.get("message", ""),
                              "from": (m.get("from") or {}).get("username"),
                              "raw": {k: m[k] for k in ("attachments", "shares", "story", "is_unsupported") if k in m}}
                             for m in group],
                "note_text": "\n".join(texts),
                "links": links,
                "media": [],
            }
            vid = 1
            for m in group:
                payload = {k: m[k] for k in ("attachments", "shares", "story") if k in m}
                for url in dict.fromkeys(_media_urls(payload)):
                    if "cdninstagram" in url or "fbcdn" in url or "lookaside" in url:
                        with tempfile.TemporaryDirectory() as tmp:
                            try:
                                path, ctype = media.download(url, tmp)
                            except Exception as e:
                                item["media"].append({"kind": "download", "errors": [f"media download failed: {e}"]})
                                continue
                            if "video" in ctype:
                                r = media.process_video(path, bundle, f"video{vid}", config.get("whisper_model", "small"))
                                vid += 1
                            elif "image" in ctype:
                                r = media.process_image(path, bundle, f"image{len(item['media']) + 1}.jpg")
                            else:
                                r = {"kind": "file", "mime": ctype, "errors": ["unrecognised media type"]}
                            item["media"].append(r)
                    else:
                        links.append(url)
                if m.get("is_unsupported"):
                    item["media"].append({"kind": "unsupported", "errors": [
                        "Instagram marked this message unsupported by the API; the triage only has any text"]})
            item["links"] = list(dict.fromkeys(links))
            item["media"] += media.process_links(
                [u for u in item["links"] if media.is_video_link(u)], bundle, config, start_index=vid)
            write_item(bundle, item)
            made.append(item_id)
            for m in group:
                seen.add(m["id"])
                seen_list.append(m["id"])
            st["seen_message_ids"] = seen_list[-1000:]
    st["warnings"] = warnings
    return made, warnings
