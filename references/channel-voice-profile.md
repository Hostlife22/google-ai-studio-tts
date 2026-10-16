# Channel voice profile (momentum reference videos)

Voice + style presets matched to the reference videos in
`momentum/new/ref/long` (8 long videos, 19–38 min) and `momentum/new/ref/shorts` (12 shorts, 40–95 s).
Measured 2026-10-15: pitch with autocorrelation F0 (Praat-checked), speech rate from transcripts. The reference audio has background music, so pause metrics from the references are not usable.

## Reference narrator

| Metric | Shorts | Long videos | Long: dark cold open |
|---|---|---|---|
| Voice | young male, mid-low | same | same, quieter |
| Median F0 | 140–170 Hz | 125–155 Hz | ~115–120 Hz |
| Pitch variability (st. dev.) | 6.3–7.5 semitones (very animated) | 5.5–7 | ~5.5–6.6 |
| Speech rate | 170–190 wpm (up to 228) | 155–170 wpm | ~140 wpm |

**Delivery:** a fast, sarcastic, comedic history storyteller who talks to the viewer like a friend.
- **Hook:** opens with a provocative line ("If your friend likes Fanta, he's probably a Nazi").
- **Asides:** rhetorical questions with mock disbelief ("Suspicious? Extremely."), deadpan punchlines, asides like "Yeah, you are laughing, but this really happened", "Oh hell no!".
- **Long videos:** add skits, character voices, meme references and self-aware jokes. Some open with a slow, haunting cinematic cold open (e.g. The God of Horror), then switch to the casual mode.

## Measured candidates (same 70-word English excerpt from the Fanta short)

| Voice | Style | F0 Hz | Var st | wpm |
|---|---|---|---|---|
| **Puck** | FAST_SARCASTIC | 150 | 6.00 | 194 |
| **Enzo** | SARCASTIC | 133 | 6.51 | 163 |
| **Enzo** | THEATRICAL_FAST | 129 | 6.06 | 179 |
| Mako | THEATRICAL_FAST | 128 | 6.13 | 184 |
| Enzo | FAST_SARCASTIC (×2 runs) | 125–126 | 5.53–5.56 | 185–186 |
| Mako | FAST_SARCASTIC | 125 | 5.99 | 193 |
| Sadachbia | SARCASTIC / FAST | 126–140 | 5.0–5.95 | 162–194 |
| Puck | SARCASTIC / THEATRICAL | 157 | 4.9–5.5 | 172–178 |
| Fenrir, Knox, Koda, Jori, Ludo, Riko, Orus, Iapetus | SARCASTIC | 123–188 | 4.4–5.9 | 152–177 |

Russian test (same text translated, so wpm is not comparable to English):

| Voice | Style | F0 Hz | Var st | wpm |
|---|---|---|---|---|
| Enzo | THEATRICAL_FAST | 124 | 6.05 | 174 |
| Puck | FAST_SARCASTIC | 137 | 4.88 (flat) | 191 |

Full Russian short (Beer Tsunami, 124 words, Enzo + THEATRICAL_FAST, 2026-10-16): 55 s, 116 Hz, 4.68 st, 139 wpm. The pace is right, but the intonation is flatter on a long single block than on the 60-word excerpt (6.05). To keep the energy, split long scripts into several blocks with one beat each.

Run-to-run noise is small (Enzo repeated: ±0.03 st, ±1 wpm), but the style text changes results a lot.

## Recommended presets (English — primary language of the channel)

**One narrator for the whole channel: Enzo.** The reference uses the same narrator in shorts and long videos, so use one voice everywhere. Enzo hit the targets in both formats and is the only voice verified for the dark intro.

| Use | Voice | Style | Measured vs target |
|---|---|---|---|
| Shorts (whole video) | **Enzo** | THEATRICAL_FAST | 129 Hz / 6.06 st / 179 wpm vs 140–170 / 6.3–7.5 / 175–190 |
| Long video, main body | **Enzo** | SARCASTIC | 133 Hz / 6.51 st / 163 wpm vs 125–155 / 5.5–7 / 155–170 |
| Long video, serious cold open | **Enzo** | DARK | 109 Hz / 4.67 st / 144 wpm vs ~118 / 5.5–6.6 / 142 |
| Alternative for shorts only | Puck | FAST_SARCASTIC | 150 Hz / 6.00 st / 194 wpm. Pitch is closest, but results swing between styles (4.9–6.0 st), and it would sound like a different narrator than the long videos |
| Backup if Enzo is unavailable | Mako | THEATRICAL_FAST | 128 Hz / 6.13 st / 184 wpm |

Russian (secondary): Enzo + THEATRICAL_FAST. Puck goes flat in Russian (4.88 st).

## Which style when (per block)

Style is set per speech block, so split the script into blocks by beat and give each block the mode for its part. **The full palette lives in delivery-modes.md:** 15 modes with calibrated Style texts, the tempo ladder (110–300 wpm), long and short structure templates, and pause/punctuation rules. Quick defaults:

| Part of the script | Mode |
|---|---|
| **Shorts:** hook + story | THEATRICAL_FAST (3–5 blocks); lists → RAPID_MONTAGE; sting line → DEADPAN |
| **Long:** main narration | SARCASTIC, with DEADPAN for punchline sentences |
| **Long:** cold open | skit/gag (CHARACTER_SKIT, PERSONA_HOST, SARCASTIC) or DARK for a tragic topic |
| **Long:** battles, escalation, climax | DRAMATIC |
| **Long:** lists, time-skips, speedruns | RAPID_MONTAGE (FAST_SARCASTIC for milder speed-ups) |
| **Long:** sponsor | SPONSOR |
| **Long:** serious stretch, tragedy | DARK; POETRY for quoted verse |
| Skits, impersonations, outrage | CHARACTER_SKIT, PERSONA_HOST, MOCK_SHOUT; one block per line, back to SARCASTIC after |
| Asides to the viewer | CONSPIRATORIAL |
| Outro + CTA | OUTRO |

Inline tags inside any block: `<chuckle>` after a joke, `<gasp>` on a shocking reveal, `<sigh>` for mock exasperation, `<short pause>` (≈1–2 s) right before a punchline. 1–2 per block at most. Test results for every tag: audio-tags.md.

### Style texts (paste into the block's Style field)

**SARCASTIC** (long-video body and light cold opens)
> Energetic, sarcastic YouTube history storyteller. Fast, punchy pace with almost no pauses, playful irony, big pitch swings, dramatic emphasis on shocking words, casual and slightly mocking.

**FAST_SARCASTIC** (fast recap passages in long videos; Puck shorts alternative)
> Fast-talking, sarcastic YouTube history storyteller in his twenties. Rapid-fire pace, about 185 words per minute, no dramatic pauses, sentences run into each other. Mock disbelief on rhetorical questions, deadpan punchlines, big energetic pitch jumps on shocking facts, grinning, playful, a bit chaotic.

**THEATRICAL_FAST** (shorts — English and Russian)
> Fast-talking sarcastic YouTube history storyteller in his twenties, rapid-fire pace with no dramatic pauses. Very animated and theatrical: exaggerated pitch swings, mock shock and disbelief going high, deadpan punchlines dropping low, stressed key words, grinning the whole time like he's telling friends a crazy story.

**DARK** (cold open, verified 2026-10-16)
> Same young YouTube history storyteller, but for this intro he turns serious and reflective. Steady conversational pace, flowing sentences, normal speaking pitch, no whispering and no long pauses. Very expressive intonation with clear rises and falls, leaning hard on key words, emotional and haunting, like he's about to tell a sad true story.

Dark-intro tuning on Enzo (Poe cold-open text; reference ≈ 121 Hz in-page scale, 5.5–6.6 st, 142 wpm):

| Variant | F0 Hz | Var st | wpm | Verdict |
|---|---|---|---|---|
| "low, hushed, ominous… almost whispering" | 86 | 4.45 | 101 | far too slow and deep |
| "cinematic… ~140 wpm, normal pitch" | 102 | 4.02 | 114 | still too slow and deep |
| "same storyteller, serious and reflective" | 112 | 3.74 | 151 | pace OK, flat |
| **DARK (above)** | **109** | **4.67** | **144** | best: pace exact, slightly low and flatter |

Lesson: words like *cinematic*, *ominous*, *hushed*, *whisper* make Gemini TTS slow down and drop pitch a lot. Describe the mood ("serious, reflective, sad true story") and keep "same storyteller, normal pitch, steady pace". In the script, replace `...` with commas, because ellipses add long pauses. In DARK blocks use `<sigh>` / `<exhales>` and at most one `<short pause>`, never `<long pause>` (≈1.4–1.8 s).

## Script-writing tips to match the reference

- Start with a provocative hook sentence; follow it with a short rhetorical question ("Suspicious? Extremely.").
- Short sentences with punchlines; put the joke at the end of the sentence so the deadpan drop lands.
- Expression tags sparingly: `<chuckle>` after a joke, `<sigh>` for mock exasperation, `<short pause>` before a punchline, `<gasp>` on shock reveals. Full per-tag guide and channel cheat-sheet: audio-tags.md.
- Blocks alternate Speaker 1 / Speaker 2. For a single-narrator video split into blocks, set Speaker 2 to the same voice (Enzo) in the right panel.
- Keep each block to one beat (2–4 sentences). Then Style can differ per block, e.g. DARK for the cold-open block and SARCASTIC for the rest.

## How these numbers were measured (to repeat the test)

1. Reference: `ffmpeg -i video.mp4 -vn -ac 1 -ar 16000 clip.wav`; shorts transcribed with `whisper-cli -m ggml-base.en.bin`.
2. Pitch: autocorrelation F0 over 40 ms windows with a 10 ms hop, 65–400 Hz, voicing threshold r > 0.6. Report the median, plus the st. dev. in semitones around the median.
3. TTS output: the same algorithm runs in the page on `document.querySelector('audio').src` (a full WAV data URL) after playback finishes. The audio streams in chunks first, so wait until the footer shows `play_circle` and `src` > 200 KB.
4. If the page was just loaded, Chrome may block autoplay: playback sits at `0:00` and the full WAV never arrives. Click the play button once with a real `computer` click. Generation plus real-time playback can take 2–3× the audio length, so wait up to ~5 min.
5. One browser JS call times out at ~45 s, so start generation queues in the page without `await` and poll for the results.

## Scripts

- `scripts/tts-bench.js` — paste into the AI Studio page via `javascript_tool`; `__bench([{voice, style, text, tag}])` generates and measures each case in the background, poll `__results`.
- `scripts/tag_test.py` — builds a tag test text, then cuts the render into one clip per tag, transcribes each clip and measures pauses.
- `scripts/ref_pitch_acf.py clip.wav…` — same F0 algorithm as the in-page analyzer (numpy only).
- `scripts/ref_analyze_praat.py clip.wav…` — Praat-based check (needs `pip install numpy praat-parselmouth`); reads `clip.txt` next to the wav for wpm.
