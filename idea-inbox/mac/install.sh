#!/bin/bash
# One-time setup for the nightly idea-inbox collector on the Mac mini.
# Safe to re-run: it keeps your config, token and state, and refreshes the rest.
#
#   bash idea-inbox/mac/install.sh            install or update
#   bash idea-inbox/mac/install.sh --test     run the access check the way launchd will
#   bash idea-inbox/mac/install.sh --uninstall
set -euo pipefail

LABEL="com.peculiarpeople.idea-inbox"
HOME_DIR="$HOME/.idea-inbox"
AGENT="$HOME/Library/LaunchAgents/$LABEL.plist"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC_REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"
RUN_HOUR=1
RUN_MINUTE=15
PATH_FOR_JOB="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

say() { printf '\n== %s\n' "$*"; }

write_agent() {  # write_agent <label> <plist path> <extra python arg or ""> <schedule: yes|no>
  local label="$1" path="$2" arg="$3" scheduled="$4"
  {
    echo '<?xml version="1.0" encoding="UTF-8"?>'
    echo '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    echo '<plist version="1.0"><dict>'
    echo "  <key>Label</key><string>$label</string>"
    echo '  <key>ProgramArguments</key><array>'
    echo "    <string>$HOME_DIR/venv/bin/python</string>"
    echo "    <string>$HOME_DIR/repo/idea-inbox/collector/nightly.py</string>"
    [ -n "$arg" ] && echo "    <string>$arg</string>"
    echo '  </array>'
    echo "  <key>EnvironmentVariables</key><dict><key>PATH</key><string>$PATH_FOR_JOB</string></dict>"
    echo "  <key>StandardOutPath</key><string>$HOME_DIR/logs/$label.log</string>"
    echo "  <key>StandardErrorPath</key><string>$HOME_DIR/logs/$label.log</string>"
    if [ "$scheduled" = yes ]; then
      echo "  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>$RUN_HOUR</integer><key>Minute</key><integer>$RUN_MINUTE</integer></dict>"
    else
      echo '  <key>RunAtLoad</key><true/>'
    fi
    echo '</dict></plist>'
  } > "$path"
}

if [ "${1:-}" = "--uninstall" ]; then
  launchctl bootout "gui/$(id -u)" "$AGENT" 2>/dev/null || true
  rm -f "$AGENT"
  echo "Nightly job removed. Your config, token and state in $HOME_DIR were kept; delete that folder to remove them too."
  exit 0
fi

if [ "${1:-}" = "--test" ]; then
  # Running --check from Terminal would borrow Terminal's permissions. This runs it
  # under launchd instead, exactly as the 1:15 AM job will, so the result is real.
  TEST_LABEL="$LABEL.test"
  TEST_AGENT="$HOME/Library/LaunchAgents/$TEST_LABEL.plist"
  : > "$HOME_DIR/logs/$TEST_LABEL.log"
  write_agent "$TEST_LABEL" "$TEST_AGENT" "--check" no
  launchctl bootout "gui/$(id -u)" "$TEST_AGENT" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$TEST_AGENT"
  echo "Running the check under launchd (up to 60 seconds)..."
  for _ in $(seq 1 30); do
    sleep 2
    grep -q -e "All checks passed" -e "Fix the FAIL" "$HOME_DIR/logs/$TEST_LABEL.log" 2>/dev/null && break
  done
  launchctl bootout "gui/$(id -u)" "$TEST_AGENT" 2>/dev/null || true
  rm -f "$TEST_AGENT"
  cat "$HOME_DIR/logs/$TEST_LABEL.log"
  exit 0
fi

[ "$(uname)" = "Darwin" ] || { echo "This installer is for the Mac mini."; exit 1; }

say "Folders"
mkdir -p "$HOME_DIR/logs" "$HOME_DIR/outbox"
chmod 700 "$HOME_DIR"

say "Dedicated repo clone (outside iCloud, so the job never touches your working copy)"
ORIGIN="$(git -C "$SRC_REPO" remote get-url origin)"
if [ -d "$HOME_DIR/repo/.git" ]; then
  git -C "$HOME_DIR/repo" fetch -q origin main && git -C "$HOME_DIR/repo" checkout -q main \
    && git -C "$HOME_DIR/repo" reset -q --hard origin/main
else
  git clone -q "$ORIGIN" "$HOME_DIR/repo"
fi
[ -f "$HOME_DIR/repo/idea-inbox/collector/nightly.py" ] || {
  echo "The collector is not on main yet. Merge the idea-inbox branch first, then re-run."; exit 1; }

say "ffmpeg"
if ! command -v ffmpeg >/dev/null; then
  if command -v brew >/dev/null; then brew install ffmpeg
  else echo "Install Homebrew (https://brew.sh) and re-run, or install ffmpeg another way."; exit 1; fi
fi

say "Python environment"
PY="$(command -v /opt/homebrew/bin/python3 || command -v python3)"
[ -x "$HOME_DIR/venv/bin/python" ] || "$PY" -m venv "$HOME_DIR/venv"
"$HOME_DIR/venv/bin/pip" install -q --upgrade pip
"$HOME_DIR/venv/bin/pip" install -q --upgrade faster-whisper yt-dlp requests

say "Whisper model (one-time download, about 500 MB)"
"$HOME_DIR/venv/bin/python" -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"

say "Config"
if [ ! -f "$HOME_DIR/config.json" ]; then
  sed "s#__REPO__#$HOME_DIR/repo#" "$SCRIPT_DIR/config.example.json" > "$HOME_DIR/config.json"
  echo "Created $HOME_DIR/config.json. Fill in self_handles."
fi
chmod 600 "$HOME_DIR/config.json"

say "Nightly job ($RUN_HOUR:$(printf %02d $RUN_MINUTE) AM)"
write_agent "$LABEL" "$AGENT" "" yes
launchctl bootout "gui/$(id -u)" "$AGENT" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$AGENT"

REAL_PY="$("$HOME_DIR/venv/bin/python" -c 'import os,sys; print(os.path.realpath(sys.executable))')"
APP_PY="$(dirname "$REAL_PY")/../Resources/Python.app"
say "Last step: Full Disk Access (macOS will not let the job read Messages without it)"
cat <<EOF
1. Open System Settings > Privacy & Security > Full Disk Access.
2. Click +, press Cmd+Shift+G, paste this path, and add it:
     $REAL_PY
EOF
if [ -d "$APP_PY" ]; then
  echo "   Also add this one (Homebrew Python runs through it):"
  echo "     $(cd "$APP_PY" && pwd)"
fi
cat <<EOF
3. Fill in self_handles in $HOME_DIR/config.json.
4. Run:  bash "$SCRIPT_DIR/install.sh" --test
   It runs the check under launchd, the same way the nightly job runs.
EOF
