# Idea inbox

Evan texts himself reel links and notes through the day. Overnight they get triaged against
the brand and turned into plans, drafts, or mockups, ready by morning.

```
 through the day          1:15 AM, Mac mini                     ~2 AM, Claude Code routine
 ---------------          -----------------                     --------------------------
 iMessage to self  ---->  collector/nightly.py  ---git push--->  idea-triage skill
                          transcript + frames per video          verdict + deliverable per item
                          idea-inbox/inbox/<item>/                ideas/YYYY-MM-DD/DIGEST.md
```

## What it's for

You see something useful while scrolling and don't have time to deal with it.
Text it to yourself (a reel link, a screenshot, or a note), add a few words on
why if you can, and forget about it. In the morning there's a digest with a verdict on each item and the
first piece of work already done.

What to send it, and what comes back:

| You save | You get in the morning |
|---|---|
| A reel showing a Claude Code trick (a hook, a skill, an automation) | A plan for adding it to this workspace: files touched, steps, risks, and which existing skill it extends |
| A reel about hooks, ad angles, or a content format | 2 or 3 drafts of it using real Peculiar People products and temples, already through both humanizer passes |
| A reel or screenshot of another store's site or product page | An HTML mockup of the idea on our store, plus notes on what changed and why |
| A business, pricing, or offer idea | The idea applied to Peculiar People, the numbers it depends on, and the smallest next step |
| A quick text to yourself ("bundle tee + sticker for dedications?") | A verdict, and a short plan if it holds up |
| Something that turns out not to fit | One line on why, so you can overrule it if the reason is wrong |

Each item gets one verdict:
- **Useful:** do it this week.
- **Beneficial:** worth doing, but needs a decision, money, or time.
- **Plausible:** unproven, so you get the cheapest test.
- **Waste:** doesn't fit, with the reason.

Tips:
- **Add a note when you share.** "Could this work for the temple drops?" tells the triage what you saw in it. Messages sent within five minutes of each other are kept together as one item.
- **Copy the reel's link and text it to yourself.** The Mac downloads it logged out, so no account of yours is ever involved. Instagram sometimes refuses a logged-out download; when that happens the digest says so and judges the item on your note, so a line about why you saved it matters. A screenshot always gets through.
- **Run it by hand in any session:** say "check my idea inbox".

What it will never do: change the store, post, reply to anyone, or install
or run anything a video suggests. It plans and drafts; you decide what ships.

## How it works

The Mac does the collecting because iMessage exists only on Apple devices. The
cloud routine needs no secrets and no network access beyond git.

Nothing in this pipeline logs in to any of your accounts. Video links are
downloaded logged out (no browser cookies, no saved logins), and there is no
Instagram or Meta token. An Instagram API collector was tried on 6 October 2026
and removed: Meta returned no conversations for the business account even with
every setting correct, and Evan chose to keep the pipeline account-free. It is
in git history if that is ever revisited.

## What goes into git, and what never does

- Each item is a folder: `item.json` (the message text and what was attached),
  `videoN/transcript.txt`, `videoN/frames/*.jpg` (6 to 16 stills), `images/*.jpg`.
- Video files never go in. A reel is 5 to 20 MB; its transcript and frames are
  under 1 MB.
- Only one chat is ever read: your iMessage note-to-self thread. Every other
  conversation is filtered out before its messages are requested.
- Your phone number lives in `~/.idea-inbox/config.json` on the Mac, outside
  the repo and outside iCloud.

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

## Files

| Path | Runs on | What it does |
|---|---|---|
| `collector/nightly.py` | Mac | Entry point. `--check` tests access, `--dry-run` skips git. |
| `collector/imessage.py` | Mac | Reads the note-to-self thread from `chat.db`. |
| `collector/media.py` | Mac | Transcripts (local Whisper) and frames (ffmpeg). |
| `mac/install.sh` | Mac | Install, `--test`, `--uninstall`. |
| `pending.py` | Cloud | Lists untriaged items and Mac health; `--mark` records them done. |
| `state/processed.json` | Cloud | Items already triaged. |
| `inbox/HEARTBEAT.json` | Both | The Mac's last run and any errors; the digest reports problems. |

Logs on the Mac: `~/.idea-inbox/logs/`.
