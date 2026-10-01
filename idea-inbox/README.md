# Idea inbox

Evan saves reels and notes through the day. Overnight they get triaged against
the brand and turned into plans, drafts, or mockups, ready by morning.

```
 through the day          1:15 AM, Mac mini                     ~2 AM, Claude Code routine
 ---------------          -----------------                     --------------------------
 iMessage to self  --+
 IG personal -> biz --+--> collector/nightly.py ---git push--->  idea-triage skill
 IG biz -> itself  --+    transcript + frames per video          verdict + deliverable per item
                          idea-inbox/inbox/<item>/                ideas/YYYY-MM-DD/DIGEST.md
```

The Mac does the collecting because iMessage exists only on Apple devices, and
because the Instagram token can refresh itself there. The cloud routine needs no
secrets and no network access beyond git.

## What goes into git, and what never does

- Each item is a folder: `item.json` (the message text and what was attached),
  `videoN/transcript.txt`, `videoN/frames/*.jpg` (6 to 16 stills), `images/*.jpg`.
- Video files never go in. A reel is 5 to 20 MB; its transcript and frames are
  under 1 MB.
- Only three chats are ever read: your iMessage note-to-self thread, and the
  business account's Instagram chats with your personal account and with
  itself. Every other conversation is filtered out before its messages are
  requested.
- Your phone number, usernames, and the Instagram token live in
  `~/.idea-inbox/` on the Mac, outside the repo and outside iCloud.

## Setup on the Mac mini

1. Merge this branch to `main` (the installer clones `main`).
2. In your normal checkout: `bash idea-inbox/mac/install.sh`
   It makes `~/.idea-inbox/` and a separate clone of the repo there. The job
   uses that clone so it never touches your iCloud working copy or your
   branches. It also installs ffmpeg (via Homebrew) and the local Whisper
   model, and schedules the 1:15 AM job.
3. Grant Full Disk Access to the Python path the installer prints (System
   Settings > Privacy & Security > Full Disk Access). Without it macOS blocks
   reading Messages.
4. Edit `~/.idea-inbox/config.json`: `self_handles` is the number and/or
   Apple ID email you text yourself at.
5. `bash idea-inbox/mac/install.sh --test` runs the check under launchd, which
   is how the real job runs. Running the check from Terminal would borrow
   Terminal's permissions and could pass when the real job would fail.

The Mac has to be awake and logged in at 1:15 AM. Check that System Settings >
Energy does not put it to sleep.

## Turning on Instagram (later)

Needs the business account to be a Business or Creator account.

1. At developers.facebook.com, create an app and add the **Instagram** product,
   choosing "API setup with Instagram login".
2. Add the business Instagram account and generate a token with
   `instagram_business_basic` and `instagram_business_manage_messages`. Because
   you are an admin of the app reading your own account, App Review is not
   needed.
3. Put it in `~/.idea-inbox/.env` as `IG_ACCESS_TOKEN=...`, set
   `ig_personal_username` and `"instagram_enabled": true` in the config, and
   run `install.sh --test`.

The token refreshes itself weekly. The API only shows the 20 most recent
messages per chat, so more than 20 shares in one day can drop the oldest.
Instagram may not expose a chat with yourself at all; if so the morning digest
says so, and sharing from personal to business always works.

Reel links pasted as text (rather than shared) usually need a logged-in
browser to download. Set `"ytdlp_cookies_browser": "safari"` to allow that, or
just share the reel instead of pasting its link.

## Files

| Path | Runs on | What it does |
|---|---|---|
| `collector/nightly.py` | Mac | Entry point. `--check` tests access, `--dry-run` skips git. |
| `collector/imessage.py` | Mac | Reads the note-to-self thread from `chat.db`. |
| `collector/instagram.py` | Mac | Reads the two Instagram chats, refreshes the token. |
| `collector/media.py` | Mac | Transcripts (local Whisper) and frames (ffmpeg). |
| `mac/install.sh` | Mac | Install, `--test`, `--uninstall`. |
| `pending.py` | Cloud | Lists untriaged items and Mac health; `--mark` records them done. |
| `state/processed.json` | Cloud | Items already triaged. |
| `inbox/HEARTBEAT.json` | Both | The Mac's last run and any errors; the digest reports problems. |

Logs on the Mac: `~/.idea-inbox/logs/`.
