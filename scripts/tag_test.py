"""Test what inline <tags> do in a Gemini TTS render.

1) Build the test text (paste it into one speech block and Run):
     python tag_test.py text sigh gasp tsk
   -> "Apple. <sigh> umbrella comes right after it. Bridge. <gasp> violin ..."

2) Download the WAV, then analyse it (needs whisper-cli + a ggml model):
     python tag_test.py analyze render.wav ggml-base.en.bin OUT_DIR sigh gasp tsk

   For every tag it cuts the line into OUT_DIR/NN_tag.wav (for listening), transcribes
   the clip and measures silences. What to read from the output:
     - tag name or a sound word in the transcript ("whispers", "cry", "yay", "gurr")
       -> the tag was read aloud, or the sound came out as a speech-like word
     - longest silence well above the ~0.2-0.3 s sentence gap -> the tag made a pause
   Whisper only transcribes speech, so a clean transcript does not prove the tag was
   silent: listen to the clip.
"""
import re
import subprocess
import sys
import tempfile
import wave

import numpy as np

W1 = ["Apple", "Bridge", "Candle", "Dolphin", "Engine", "Forest", "Garden", "Harbor", "Island", "Jacket",
      "Kettle", "Lemon", "Marble", "Needle", "Orange", "Pepper", "Quartz", "Rocket", "Saddle", "Tiger"]
W2 = ["umbrella", "violin", "window", "yellow", "zebra", "anchor", "button", "castle", "desert", "eagle",
      "falcon", "glacier", "hammer", "igloo", "jungle", "koala", "ladder", "magnet", "napkin", "oyster"]
MAX_TAGS = len(W1)
SILENCE_DB = 40  # below the 90th-percentile frame level
MIN_SILENCE = 0.12  # seconds


def build_text(tags):
    if len(tags) > MAX_TAGS:
        raise SystemExit(f"at most {MAX_TAGS} tags per render")
    return " ".join(f"{W1[i]}. <{t}> {W2[i]} comes right after it." for i, t in enumerate(tags))


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def to16k(src, dst):
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", "16000", dst])


def word_ends(wav16, model, word="it"):
    """Whisper end times of every occurrence of `word` (one per test line)."""
    out = run(["whisper-cli", "-m", model, "-f", wav16, "-ml", "1", "-sow", "-np"])
    ends = []
    for m in re.finditer(r"\[\d+:\d+:[\d.]+ --> (\d+):(\d+):([\d.]+)\]\s*(\S+)", out):
        if re.sub(r"[^a-z]", "", m.group(4).lower()) == word:
            ends.append(int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)))
    return ends


def silences(wav16):
    with wave.open(wav16) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
        hop = w.getframerate() // 100
    n = len(x) // hop
    db = 10 * np.log10((x[: n * hop].reshape(n, hop) ** 2).mean(axis=1) + 1e-12)
    silent = db < np.percentile(db, 90) - SILENCE_DB
    runs, start = [], None
    for i, s in enumerate(silent):
        if s and start is None:
            start = i
        elif not s and start is not None:
            if (i - start) / 100 >= MIN_SILENCE:
                runs.append(round((i - start) / 100, 2))
            start = None
    return runs


def analyze(render, model, out_dir, tags):
    with tempfile.TemporaryDirectory() as tmp:
        full16 = f"{tmp}/full.wav"
        to16k(render, full16)
        ends = word_ends(full16, model)
        if len(ends) != len(tags):
            print(f"warning: found {len(ends)} line ends for {len(tags)} tags; clips may be shifted")
        cuts = [0.0] + ends
        for i, tag in enumerate(tags[: len(ends)]):
            clip = f"{out_dir}/{i + 1:02d}_{tag.replace(' ', '-')}.wav"
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{cuts[i]:.2f}", "-to", f"{cuts[i + 1] + 0.1:.2f}", "-i", render, clip])
            clip16 = f"{tmp}/clip.wav"
            to16k(clip, clip16)
            text = " ".join(run(["whisper-cli", "-m", model, "-f", clip16, "-np", "-nt"]).split())
            sil = silences(clip16)
            print(f"<{tag}>  silences={sil}  longest={max(sil, default=0)}s  heard: {text}")


def main(argv):
    if len(argv) >= 2 and argv[0] == "text":
        print(build_text(argv[1:]))
    elif len(argv) >= 5 and argv[0] == "analyze":
        analyze(argv[1], argv[2], argv[3], argv[4:])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
