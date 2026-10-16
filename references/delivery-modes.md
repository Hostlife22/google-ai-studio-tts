# Delivery modes: tempo, emotion and pauses for shorts and long videos

The reference narrator (momentum `ref/long` and `ref/shorts`) is not one style but a **palette of delivery modes** that switch every few sentences. This file maps every mode found in the references to a Style text calibrated on Enzo (2026-10-16), so a script can be voiced with the same changes of tempo, emotion and pauses.

Voice: **Enzo** for every mode (see channel-voice-profile.md). Each mode is one or more speech blocks with its own Style; blocks alternate Speaker 1/2, so set both speakers to Enzo.

## What the references contain (audit 2026-10-16)

- **Tempo.**
  - Long videos: median 163 wpm, 80% of 60-s windows between 138 and 180.
  - Range from ~100 wpm (grief, poetry, climax) to 250–310 wpm (sponsor reads, list rattles), sometimes within 30 s.
  - Shorts: median 186 wpm (10-s windows 150–218); the "Pope" short runs at 229.
- **Pitch.**
  - Per 10-s window: 110 Hz (calm or dark) → 139 Hz (median) → 181 Hz (p95).
  - Shouts and skit voices reach 200–245 Hz; pitch variability 4.7–8.2 semitones.
- **Long-video airtime by mode:**

  | Mode | Share |
  |---|---|
  | Wry explainer | 30% |
  | Deadpan punchline | 10% |
  | Dramatic storytelling | 9% |
  | Character skits | 9% |
  | Fast montage | 7% |
  | Persona host | 7% |
  | Dark / reflective | 7% |
  | Sponsor | 6% |
  | Conspiratorial aside | 3% |
  | Rhetorical Q + mock disbelief | 3% |
  | Gaming commentary | 3% |
  | Mock shout | 2% |
  | Meta jokes | 2% |
  | Poetry | 1% |
  | Hype outro | 1% |

- **Shorts airtime:** explainer 45%, deadpan 18%, fast montage 10%, dramatic 8%, dark 5%, rhetorical Q 5%, the rest ≤3%.

## Tempo ladder (measured on Enzo)

| Tier | wpm | Modes |
|---|---|---|
| Slow | 110–155 | PERSONA_HOST (112), POETRY (127–153), CHARACTER_SKIT (122) |
| Measured | 140–160 | DARK (144), DRAMATIC (155–158), MOCK_SHOUT (150) |
| Base, long video | 160–170 | SARCASTIC (163), DEADPAN (164) |
| Fast, shorts | 175–200 | THEATRICAL_FAST (179), CONSPIRATORIAL (185), FAST_SARCASTIC (185–194), OUTRO (196) |
| Rapid | 215–300 | RAPID_MONTAGE (217), SPONSOR (298) |

## Mode palette

The Measured column is the Enzo render: wpm / median F0 / pitch variability / loudness vs. the narration. "Target" comes from the reference audit. ✅ = matches the target.

| Mode | Use it for | Target (refs) | Measured | |
|---|---|---|---|---|
| **SARCASTIC** | Long-video main narration, wry explainer | 160–170 wpm, 125–155 Hz | 163 / 133 Hz / 6.5 st | ✅ |
| **THEATRICAL_FAST** | Shorts: hook + whole story | 175–190 wpm, 140–170 Hz | 179 / 129 Hz / 6.1 st | ✅ |
| **FAST_SARCASTIC** | Faster explainer stretches | ~185 wpm | 185–194 / 125–150 Hz | ✅ |
| **DEADPAN** | Dry punchlines, understatement, "It went exactly as well as you'd expect." | baseline tempo, flat | 164 / 108 Hz / 3.2 st (flat) | ✅ |
| **DRAMATIC** | Battles, escalation, "and then…" build-ups, climaxes | ~150 wpm, intense | 155–158 / 98–106 Hz / 4.8–5.1 st | ✅ (pitch drops into Enzo's serious register) |
| **DARK** | Tragedy, death, horror cold opens, sincere passages | ~142 wpm, ~118 Hz | 144 / 109 Hz / 4.7 st | ✅ |
| **RAPID_MONTAGE** | Speedruns, lists, "dynasty one, gone", time-skips | 210–250 wpm | 217 / 135 Hz / 5.9 st | ✅ |
| **SPONSOR** | Sponsor reads, ad parodies | 250–310 wpm, bright | 298 / 154 Hz, +4 dB | ✅ |
| **MOCK_SHOUT** | Fake outrage, caps lines ("OH GOD HE'S BECOMING A KING") | 200–245 Hz, loud | 150 / **254 Hz** / 7.5 st, +3.7 dB | ✅ |
| **CONSPIRATORIAL** | Asides to the viewer, gossip, "you didn't hear that from me" | quieter, faster | 185 / 131 Hz, −2.7 dB | ✅ |
| **CHARACTER_SKIT** | Impersonations (whiny child Hitler, kings, gods) | big timbre change | 122 / **318 Hz** (child voice) | ✅ (one character type tested) |
| **PERSONA_HOST** | Recurring personas: fact-check clerk, teacher, announcer | slow-ish, smug | 112 / 116 Hz / 5.3 st | ✅ |
| **POETRY** | Quoting poems or scripture, solemn quotes | ~110–145 wpm | 127–153 / 92–98 Hz / 1.4–2.0 st | ⚠️ tempo OK but monotone; use for 1–3 lines only |
| **OUTRO** | Hyped ending + CTA, "see you next time, fellow history lovers" | fast, loud, giddy | 196 / 177 Hz / 7.4 st, +2.9 dB | ✅ |
| GAMING_COMMENTARY | WW1-style "game" framing | fast, playful, panicky | not tested; start from OUTRO energy + THEATRICAL_FAST tempo | ❓ |

### Style texts (paste into the block's Style field)

SARCASTIC, THEATRICAL_FAST, FAST_SARCASTIC and DARK: see channel-voice-profile.md.

**DEADPAN**
> Same narrator, totally deadpan: dry, flat and unimpressed, but at his normal quick conversational pace, about 165 words per minute. Only a tiny beat before the punchline.

**DRAMATIC**
> Same young YouTube history narrator, now telling the most gripping part of the story. Energetic, normal speaking pitch, steady pace of about 140 words per minute, no long pauses. Intensity comes from emphasis and rising energy, not from slowing down or lowering the voice. No jokes.

**RAPID_MONTAGE**
> Fast montage mode, rattling through events like a speedrun. Very fast, about 230 words per minute, breathless and gleeful, barely any gaps between sentences, energy rising.

**SPONSOR**
> Same young YouTube narrator doing the sponsor read: very fast, about 270 words per minute, bright and salesy, smiling, high energy, rattling it off in one breath like a radio ad disclaimer.

**MOCK_SHOUT**
> Fake comedic outrage. Suddenly shouting, loud, exasperated and fast, high pitch, over-the-top anger that collapses into a tired mutter on the last word.

**CONSPIRATORIAL**
> Sly aside to the viewer, leaning in close. Quieter, slightly faster, half-whispered, amused, like sharing juicy gossip.

**CHARACTER_SKIT** (rewrite the character part for each skit)
> Comedy skit: the narrator impersonates a whiny, spoiled child. High-pitched, petulant, sing-song and exaggerated.

**PERSONA_HOST**
> Comedy persona: a bored, slightly smug corporate host reading from a clipboard. Monotone office voice, nasal, normal pace, faintly condescending.

**POETRY**
> Same narrator reciting a famous poem with feeling. Unhurried, about 120 words per minute, melodic and expressive with a clear rise and fall on every line, soft and sad, normal speaking pitch.

**OUTRO**
> Hyped YouTube outro. Fast, loud, warm and giddy, big smile, playful, ending on a high note.

### Calibration lessons

- **Numbers in the Style are loose.**
  - DRAMATIC: "about 150" gave 105 wpm with the old wording, and "about 160" with "not slowing down" gave 188. The final text ("about 140" + "not slowing down") gives 155–158.
  - POETRY: "about 115–120" gave 127–153.
  - Always measure a new style once.
- **Mood words slow the voice down and drop the pitch:** *dramatic, solemn, cinematic, ominous, slow*. Anchor them with "same young narrator, normal speaking pitch, steady pace, no long pauses".
- **Describe a persona or character concretely** (who, age, attitude). That is what moves the pitch: child 318 Hz, shout 254 Hz.
- **In a full script, modes pull toward their neighbours.** In the Emu War short (2026-10-16), the RAPID_MONTAGE block between THEATRICAL_FAST blocks came out at 189 wpm (217 when calibrated alone). The short overall: 49.6 s, 162 wpm, 160 Hz, 6.0 st. For a clearly faster montage, make the block longer or push the Style number higher.
- **`<long pause>` stretches with the style.** It is ~0.5–2.6 s after fast or neutral blocks and 5–7 s after slow blocks (DRAMATIC, POETRY, DEADPAN in the first calibration). Avoid it at block ends in slow modes.

## Script structure templates

### Long video (15–35 min)

| Section | Typical length | Mode(s) | Notes |
|---|---|---|---|
| Cold open | 0:00–1:00 | CHARACTER_SKIT / PERSONA_HOST / SARCASTIC gag, or DARK for a tragic topic | Most references open with a gag or skit. Poe opens with POETRY → DARK. |
| Series marker | ~0:30–1:15 | OUTRO energy, short | "Historically Facts part N", hyped |
| Main explainer | bulk | SARCASTIC, with DEADPAN punchlines every few sentences | Switch to DEADPAN for the kicker sentence only |
| Escalations | as needed | DRAMATIC | Battles, betrayals, "and then…" |
| Skits inside the story | every 1–3 min in skit-heavy videos | CHARACTER_SKIT, PERSONA_HOST, MOCK_SHOUT | One block per character line; switch back to SARCASTIC right after |
| Lists / time-skips | 10–30 s | RAPID_MONTAGE | |
| Sponsor | ¼–½ of the way in, 30–60 s | SPONSOR, then back with SARCASTIC "Anyway, where were we?" | |
| Asides | anywhere | CONSPIRATORIAL | One or two sentences |
| Serious stretch | 1–3 min, once per video | DARK (POETRY for quotes) | No jokes; tags `<sigh>`, `<exhales>` |
| Climax / twist | 30–60 s | DRAMATIC → DEADPAN sting | |
| Outro + CTA | last 20–40 s | OUTRO | |

### Short (40–95 s)

| Beat | Mode | Example shape |
|---|---|---|
| 1. Shock hook (1–2 sentences) | THEATRICAL_FAST | Provocative claim, then "Yes, …" or "Let me explain." |
| 2. Fast build | THEATRICAL_FAST (or RAPID_MONTAGE for lists) | Even, fast facts with 1–2 deadpan asides |
| 3. Escalation | THEATRICAL_FAST or DRAMATIC for one sentence | "But here's the craziest part…" |
| 4. Sting (last line) | DEADPAN, or MOCK_SHOUT for an outrage gag | "Congratulations!", "Oh my god." |

Dark shorts (e.g. Suiyang) can use DARK for the sting line only, keeping the fast tempo elsewhere.

## Assigning modes to a script (decision rules)

Use this procedure on any script the user gives. Then show the plan before spending a Run.

### Step 1: format

- **Short:** under ~250 words, or the user says short. Base mode THEATRICAL_FAST.
- **Long:** anything longer. Base mode SARCASTIC.
- Split the text into sentences and strip the editor layer (`[..]`, on-screen `(..)`, emoticons).

### Step 2: position rules (apply first)

| Position | Short | Long |
|---|---|---|
| First 1–2 sentences | Hook → THEATRICAL_FAST | Cold open: use the cue table. A gag or skit gets its cue mode; a tragic topic gets DARK; otherwise SARCASTIC. |
| "Historically Facts part N" / title line | — | OUTRO energy, one short block |
| Last sentence | Sting → DEADPAN for a dry kicker, MOCK_SHOUT for an outrage gag, DARK for a grim ending | Outro/CTA → OUTRO |

### Step 3: cue table (text signal → mode)

| If the beat contains… | Mode |
|---|---|
| Sponsor talk: "sponsor", promo code, "link in the description", product pitch | SPONSOR |
| A character speaking in first person: quoted lines of a historical figure, god, child, villain, a skit exchange | CHARACTER_SKIT (write who it is into the Style) |
| A recurring host/persona frame: "settle down, children", "contestants", "our programme" | PERSONA_HOST |
| A quoted poem, verse, prayer or famous inscription | POETRY (1–3 lines max) |
| Death, massacre, grief or atrocity told sincerely, with no joke in the beat | DARK |
| A whole sentence in CAPS, several "!", or "OH GOD", "ARE YOU KIDDING ME" | MOCK_SHOUT. A single CAPS word inside a normal sentence gets a `<shout>` tag instead. |
| 3+ items in a row, rapid dates or time-skips, "Day one… Day two…", "X, gone. Y, gone." | RAPID_MONTAGE |
| An attack or battle, rising stakes, "and then…", countdown to a climax | DRAMATIC |
| An aside to the viewer: "officially… unofficially", "between us", "you didn't hear that from me", a parenthetical joke | CONSPIRATORIAL |
| A short dry kicker after a setup, understatement, "It went exactly as well as you'd expect" | DEADPAN |
| Subscribe, "see you next time", thanks for watching | OUTRO |
| Anything else | Base mode (THEATRICAL_FAST / SARCASTIC) |

**Several cues in one beat:** take the first match in this order: SPONSOR > CHARACTER_SKIT / PERSONA_HOST > POETRY > DARK > MOCK_SHOUT > RAPID_MONTAGE > DRAMATIC > CONSPIRATORIAL > DEADPAN > OUTRO > base.

### Step 4: block sizing and balance

- **Block size.** A block is 1–4 sentences. Merge neighbouring beats with the same mode. A mode change starts a new block.
- **Shorts.** Keep ≥70% of the words in THEATRICAL_FAST. Use at most 3 other modes, usually one list/RAPID_MONTAGE beat and a DEADPAN sting. Don't switch more often than every 2 sentences, except for the sting.
- **Long videos.** The mix should roughly match the references: base + DEADPAN ~40%, DRAMATIC ~10%, skits/personas ~15%, RAPID_MONTAGE ~7%, DARK ~7%, SPONSOR ~6%, rest ≤3% each. One DARK stretch per video.

### Step 5: tags and punctuation

Add 1–2 tags per block where the text reacts: `<chuckle>` after a joke, `<pff>` before a scoffing answer, `<gasp>` before a reveal, `<short pause>` before the last words of a punchline (see audio-tags.md and the punctuation table below). Don't put tags in POETRY blocks.

### Step 6: show the plan, then render

Before clicking Run, show the user a table: block #, mode, text with tags, and estimated seconds (words ÷ the mode's wpm from the tempo ladder × 60). Let them change modes, then render. This costs no quota.

### Worked example (rendered and measured 2026-10-16)

The Emu War short, 134 words → short → base THEATRICAL_FAST:

| # | Text (tags added) | Rule that fired | Mode | Measured |
|---|---|---|---|---|
| 1 | In 1932, Australia declared war on birds. And lost. `<chuckle>` Yes, really. Let me explain. | first sentences → hook | THEATRICAL_FAST | 118 wpm (incl. laugh) |
| 2 | After World War One… And the army said: sure, how hard can it be? | no cue → base | THEATRICAL_FAST | 175 wpm |
| 3 | Two soldiers. Two machine guns. Ten thousand bullets. Day one… Day two… Day three… | list + "Day one/two" | RAPID_MONTAGE | 189 wpm |
| 4 | But here's the craziest part? After a month, the army gave up. `<pff>` The birds had basically won a war… | escalation, no stronger cue → base | THEATRICAL_FAST | 204 wpm |
| 5 | So the final score? Australia, zero. `<short pause>` Emus, one. | last sentence, dry kicker | DEADPAN | 125 wpm, −6 dB |

Result: 49.6 s, 160 Hz, 6.0 st, within the reference shorts' pitch range. File: `~/Downloads/SHORT_emu-war_Enzo.wav`.

## Pauses, punctuation and reactions

| Reference device | How often | How to voice it |
|---|---|---|
| Rhetorical question + answer ("Suspicious? Extremely.") | ~40 in long, ~6 in shorts | Write it as two sentences. The question rises and the answer drops. Optionally add `<pff>` or `<snort>` before the answer. |
| Ellipsis "…" before a reveal or deadpan beat | 0–43 per long video | Use `…` in fast modes for a beat. In DARK or slow modes it creates long pauses, so use a comma or `<short pause>` there. |
| Em dash "—" interruption / aside | 0–31 per video | Keep it, for a short break. For a self-correction ("dad — I mean"), put both parts in the same block. |
| Cut-off word ("whole agai—") + interruption | up to 13 per video | Not tested. Try ending the block with "agai—" and starting the next block (other mode) immediately. |
| Interjections ("Oh hell no!", "Oh god. Okay.", "Huh?", "dude") | ~120 long, ~8 shorts | Write them as words. Add `<gasp>` for shock, `<groan>` for "oh god". |
| ALL CAPS shouting | ~60 lines in long videos | MOCK_SHOUT block, or a `<shout>` tag inside a SARCASTIC block for a single phrase |
| Whispered aside | rare | `<whispers>` + full sentence, or a CONSPIRATORIAL block |
| Laugh cues | rare in narration | `<chuckle>`, `<snicker>`, `<laugh>` (see audio-tags.md) |
| Transitions ("Anyway", "So,", "Now,", "Meanwhile") | ~100 per long video | Keep them; they reset the tempo. "Anyway" after a skit returns to SARCASTIC. |

**Don't voice the editor layer.** Square-bracket annotations (`[you get em waldo]`, `[OHGOD-]`), on-screen captions in round brackets (`(THE HORROR)`, `(awww)`) and emoticons (`0-0`, `:3`) are edit/SFX notes. Strip them from the TTS script, or turn them into a separate short block if they must be heard.

## Hard to reproduce with one TTS voice

- **Rapid multi-character dialogue with overlaps** (Greek Myths, Romulus vs Remus). The model is dual-speaker, so give the second character Speaker 2 with a different voice, or alternate CHARACTER_SKIT blocks. Overlaps are not possible.
- **Accents and impersonations** (Italian, anime, Saul Goodman, German). Describe them in CHARACTER_SKIT. Untested; check by ear.
- **Sound effects, glitches, laugh tracks and music stings.** These belong in the video edit, not in TTS.
- **Instant mid-word tone flips.** Approximate them with a block boundary; there is always a small gap.
