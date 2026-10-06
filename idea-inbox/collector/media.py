"""Turn videos and images into things the nightly triage can read.

A video becomes a timestamped transcript plus a handful of still frames. The
video file itself never goes into git: a reel is 5 to 20 MB and the repo would
balloon, while the transcript and frames for the same reel are well under 1 MB.

Transcription is local (faster-whisper on the Mac mini's CPU). Nothing goes to
a paid API.
"""

import json
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path

MAX_VIDEO_SECONDS = 45 * 60      # longer videos get their first 45 minutes
MAX_DOWNLOAD_BYTES = 400 * 1024 * 1024
FRAME_WIDTH = 720
IMAGE_MAX_PX = 1600

VIDEO_HOSTS = ("instagram.com/reel", "instagram.com/p/", "instagram.com/tv",
               "youtube.com/watch", "youtube.com/shorts", "youtu.be/",
               "tiktok.com/", "vimeo.com/", "x.com/", "twitter.com/")

_whisper_model = None


def have(cmd):
    return shutil.which(cmd) is not None


def _run(args, timeout=None):
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout, check=True)


def duration_seconds(path):
    out = _run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "json", str(path)], timeout=60).stdout
    try:
        return float(json.loads(out)["format"]["duration"])
    except (KeyError, ValueError):
        return 0.0


def has_audio(path):
    out = _run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                "stream=index", "-of", "csv=p=0", str(path)], timeout=60).stdout
    return bool(out.strip())


def extract_frames(video, out_dir, duration):
    """Evenly spaced stills: one every ~5 seconds, between 6 and 16 frames."""
    out_dir.mkdir(parents=True, exist_ok=True)
    usable = min(duration, MAX_VIDEO_SECONDS) or 1.0
    count = int(max(6, min(16, usable / 5)))
    frames = []
    for i in range(count):
        t = usable * (i + 0.5) / count
        name = f"{i + 1:02d}_t{int(t // 60):02d}m{int(t % 60):02d}s.jpg"
        dest = out_dir / name
        try:
            _run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}", "-i", str(video),
                  "-frames:v", "1", "-vf", f"scale={FRAME_WIDTH}:-2", "-q:v", "5",
                  str(dest)], timeout=120)
        except subprocess.CalledProcessError:
            continue
        if dest.exists():
            frames.append(name)
    return frames


def transcribe(video, model_name):
    """Return (text_with_timestamps, language) or raise if whisper is missing."""
    global _whisper_model
    from faster_whisper import WhisperModel  # imported late so --check can report it

    if _whisper_model is None:
        _whisper_model = WhisperModel(model_name, device="cpu", compute_type="int8")
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        _run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-t", str(MAX_VIDEO_SECONDS),
              "-vn", "-ac", "1", "-ar", "16000", str(wav)], timeout=600)
        # Hand whisper raw samples rather than a path: given a path, faster-whisper
        # decodes through PyAV, and PyAV 19 dropped an argument it passes.
        import numpy as np
        with wave.open(str(wav)) as w:
            pcm = w.readframes(w.getnframes())
        audio = np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768.0
        segments, info = _whisper_model.transcribe(audio, vad_filter=True)
        lines = []
        for seg in segments:
            m, s = divmod(int(seg.start), 60)
            lines.append(f"[{m:02d}:{s:02d}] {seg.text.strip()}")
    return "\n".join(lines), info.language


def process_video(video, bundle, label, model_name):
    """Write <label>/frames/*.jpg and <label>/transcript.txt into the bundle."""
    out = bundle / label
    out.mkdir(parents=True, exist_ok=True)
    result = {"kind": "video", "folder": label, "errors": []}
    try:
        duration = duration_seconds(video)
        result["duration_seconds"] = round(duration, 1)
        result["truncated_to_seconds"] = MAX_VIDEO_SECONDS if duration > MAX_VIDEO_SECONDS else None
        result["frames"] = [f"{label}/frames/{f}" for f in extract_frames(video, out / "frames", duration)]
    except Exception as e:  # keep going; a transcript alone is still useful
        result["errors"].append(f"frames: {e}")
    try:
        if has_audio(video):
            text, lang = transcribe(video, model_name)
            (out / "transcript.txt").write_text(text or "(no speech detected, likely music only)\n")
            result["transcript"] = f"{label}/transcript.txt"
            result["language"] = lang
        else:
            result["transcript"] = None
            result["errors"].append("video has no audio track")
    except Exception as e:
        result["errors"].append(f"transcript: {e}")
    return result


def process_image(image, bundle, name):
    """Copy an image as a resized JPEG. sips handles HEIC on the Mac."""
    images = bundle / "images"
    images.mkdir(exist_ok=True)
    dest = images / (Path(name).stem + ".jpg")
    try:
        if have("sips"):
            _run(["sips", "-s", "format", "jpeg", "-Z", str(IMAGE_MAX_PX), str(image),
                  "--out", str(dest)], timeout=120)
        else:
            _run(["ffmpeg", "-y", "-v", "error", "-i", str(image), "-vf",
                  f"scale='min({IMAGE_MAX_PX},iw)':-2", str(dest)], timeout=120)
        return {"kind": "image", "path": f"images/{dest.name}", "errors": []}
    except Exception as e:
        return {"kind": "image", "path": None, "errors": [f"image: {e}"]}


def download(url, dest_dir):
    """Plain HTTP download of a direct media URL (Instagram CDN). Returns (path, content_type)."""
    import requests

    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        ctype = r.headers.get("content-type", "")
        ext = ".mp4" if "video" in ctype else ".jpg" if "image" in ctype else ".bin"
        path = Path(dest_dir) / f"download{ext}"
        size = 0
        with open(path, "wb") as f:
            for chunk in r.iter_content(1 << 16):
                size += len(chunk)
                if size > MAX_DOWNLOAD_BYTES:
                    raise RuntimeError("download larger than limit")
                f.write(chunk)
    return path, ctype


def is_video_link(url):
    return any(h in url for h in VIDEO_HOSTS)


def fetch_link_video(url, dest_dir, cookies_browser=None):
    """Download a video page (YouTube, TikTok, an Instagram reel link) with yt-dlp.

    Instagram links usually need a logged-in browser's cookies; set
    ytdlp_cookies_browser in the config to "safari" or "chrome" to allow that.
    Returns (path, info) or raises.
    """
    import yt_dlp

    opts = {
        "outtmpl": str(Path(dest_dir) / "link.%(ext)s"),
        "format": "best[height<=720]/best",
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "max_filesize": MAX_DOWNLOAD_BYTES,
    }
    if cookies_browser:
        opts["cookiesfrombrowser"] = (cookies_browser,)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = Path(ydl.prepare_filename(info))
    meta = {k: info.get(k) for k in ("title", "uploader", "channel", "duration", "webpage_url", "description")}
    if meta.get("description"):
        meta["description"] = meta["description"][:2000]
    return path, meta


def process_links(urls, bundle, config, start_index=1):
    """Fetch every video link in a message and process it. Non-video links are just recorded."""
    results = []
    n = start_index
    for url in urls:
        if not is_video_link(url):
            results.append({"kind": "link", "url": url, "errors": []})
            continue
        with tempfile.TemporaryDirectory() as tmp:
            try:
                path, meta = fetch_link_video(url, tmp, config.get("ytdlp_cookies_browser"))
            except Exception as e:
                results.append({"kind": "link", "url": url,
                                "errors": [f"could not download video: {str(e)[:300]}"]})
                continue
            r = process_video(path, bundle, f"video{n}", config.get("whisper_model", "small"))
            r["url"] = url
            r["source_meta"] = meta
            results.append(r)
            n += 1
    return results
