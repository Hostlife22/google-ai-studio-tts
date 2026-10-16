import sys, glob, os, json, numpy as np, parselmouth

def analyze(path, words=None):
    snd = parselmouth.Sound(path)
    pitch = snd.to_pitch_ac(time_step=0.01, pitch_floor=65, pitch_ceiling=400)
    f0 = pitch.selected_array["frequency"]
    voiced = f0[f0 > 0]
    st = 12 * np.log2(voiced / np.median(voiced))
    inten = snd.to_intensity(time_step=0.01).values[0]
    thr = np.percentile(inten, 90) - 25
    silent = inten < thr
    # pauses = silent runs >= 250ms
    runs, cur = [], 0
    for s in silent:
        cur = cur + 1 if s else (runs.append(cur) or 0)
    runs.append(cur)
    pauses = [r for r in runs if r >= 25]
    dur = snd.duration
    res = {
        "file": os.path.basename(path), "dur": round(dur, 1),
        "f0_median_hz": round(float(np.median(voiced)), 1),
        "f0_p10_p90": [round(float(np.percentile(voiced, 10))), round(float(np.percentile(voiced, 90)))],
        "pitch_var_st": round(float(np.std(st)), 2),
        "pauses_per_min": round(len(pauses) / dur * 60, 1),
        "pause_ratio": round(sum(pauses) / 100 / dur, 3),
    }
    if words: res["wpm"] = round(words / dur * 60)
    return res

if __name__ == "__main__":
    out = []
    for p in sys.argv[1:]:
        txt = p[:-4] + ".txt"
        w = len(open(txt).read().split()) if os.path.exists(txt) else None
        out.append(analyze(p, w))
    for r in out: print(json.dumps(r, ensure_ascii=False))
