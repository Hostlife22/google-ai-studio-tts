# Expression tags & style

Gemini Flash TTS in AI Studio is steered by two things: per-block **Style** and inline **expression tags**.

## Speakers

Speakers are assigned per block (the chip `Speaker N - Voice`), not by text prefixes. Don't write `Speaker 1:` inside a block — it would be read aloud. Max two speakers.

## How tags work

Tags use **angle brackets** and are not spoken. In a block, type `<` for suggestions, or click **+ Expression** and pick a chip (it inserts `<tag> ` at the cursor). The 40 tags below are the full chip list from the UI.

| Type | What happens | Where to put it |
|---|---|---|
| **Sound** (gasp, sigh, sneeze…) | The voice makes the sound once, at that point. Some sounds blend into the next words instead of standing alone. | Where the sound belongs: before a reveal, after a joke. |
| **Mode** (`<whispers>`, `<whispering>`, `<shout>`, `<cry>`) | Changes how the following phrase is spoken: whispered, louder, or tearful. | Right before the words; keep that sentence short. |
| **Pause** (`<short pause>`, `<long pause>`) | Silence. **Longer than the name suggests:** short ≈ 1–2 s, long ≈ 1.4–1.8 s (normal sentence gap ≈ 0.2–0.3 s). It can land one word later than the tag. | Before a punchline. Use `<long pause>` only in slow, serious passages. |

### How the tags were verified (2026-10-16, Enzo, English)

**A/B test.** The same meaningful sentences were rendered twice, with the tag and without it (control), separated by `<long pause>` so each sentence can be cut out by silence. For each sentence the tagged version is compared to its control: extra duration, extra non-silent sound, voicing (whisper ≈ unvoiced) and loudness. Whisper transcripts confirm whether the tag was read aloud. Result: **all 40 tags work in meaningful sentences; none was read aloud.**

**Context matters.** In an earlier test with nonsense lines (`Rocket. <whispers> magnet comes right after it.`), `<whispers>`, `<whispering>` and `<cry>` were read aloud as words, and many sound tags left no measurable trace. A tag needs a real sentence around it, and a mode tag needs a full phrase after it.

`Δ` in the table = extra audio the tag added vs the control sentence, from one render each. Run-to-run variation is roughly ±0.3 s, so treat values under ~0.4 s as subtle. Clips from the first (nonsense-line) test are in `~/Downloads/tts-tag-test/`.

## Tag reference

### Laughter

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<chuckle>` | Short, soft laugh. | Default after a joke or ironic fact. | ✅ subtle, +0.4 s sound |
| `<chuckles>` | Chuckling carried into the next words. | Laughing while starting the next sentence. | ✅ +1.0 s |
| `<laugh>` | One clear laugh. | A genuinely absurd fact, once per video. | ✅ +0.8 s |
| `<laughter>` | Longer laughing burst. | A skit. Easily sounds forced. | ✅ +1.8 s |
| `<giggle>` | Light, playful laugh. | Silly details; may sound out of character. | ✅ +1.0 s |
| `<snicker>` | Suppressed, mocking laugh. | Mocking a bad historical decision. | ✅ +1.1 s |
| `<cackle>` | Villainous laugh. | Skit or villain impression only. | ✅ +1.3 s |

### Breath & sighs

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<sigh>` | One audible sigh. | Mock exasperation: "And of course, <sigh> they did it again." | ✅ sound ~0.26 s |
| `<sighs>` | Sighing into the next words. | Tired or resigned delivery. | ✅ sound ~0.2 s |
| `<exhales>` | Out-breath. | Relief, or a reset before a new section. | ✅ sound ~0.26 s |
| `<breath>` | In-breath. | Before an intense sentence. | ✅ +0.6 s, quiet |
| `<heavy breath>` | Heavy breathing. | Exhaustion or fear in a skit. | ✅ +2.5 s |
| `<pant>` | Out of breath. | A joke after a fast montage. | ✅ +0.55 s |
| `<phew>` | Relieved "phew". | After a tense passage: "<phew> Okay, that's over." | ✅ heard as "Whew" |
| `<yawn>` | Yawn. | A joke about a boring period. | ✅ +2.8 s |

### Pauses

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<short pause>` | Pause ≈ 1–2 s; can shift by one word. | Before a punchline or a twist, once or twice per short. | ✅ ≈1 s silence (isolated); +2 s in a sentence; may shift one word |
| `<long pause>` | Silence ≈ 1.4–1.8 s. | Not for this channel: every channel style asks for few or no long pauses. Only for slow non-channel narration. | ✅ 1.4–1.8 s |

### Voice mode

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<whispers>` | The following phrase is whispered. | A secret or grim aside: "<whispers> Nobody ever found the body." Put a full sentence after it. | ✅ whispered: voicing 0.30→0.08, −4.5 dB (needs a full phrase after it) |
| `<whispering>` | The following phrase is whispered (continuous). | A longer whispered sentence. | ✅ whispered: voicing 0.47→0.09, −6 dB (needs a full phrase after it) |
| `<shout>` | Next words louder. | Mock outrage, once per video. | ✅ ~3 dB louder |
| `<scream>` | A scream ("ah!"). | Horror skit only. | ✅ heard as "ah!" |
| `<shriek>` | Loud high scream. | Comic fright. | ✅ loud, ~0.5 s |
| `<cheer>` | Cheer ("yay"). | Sarcastic victory: "<cheer> Rome is saved! …for a week." | ✅ heard as "yay" |

### Distress

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<gasp>` | Sharp in-breath of shock. | Before a shocking reveal. | ✅ fills the gap before the reveal |
| `<groan>` | Annoyed groan. | Reacting to a dumb decision. | ✅ subtle, +0.4 s |
| `<sob>` | Sob. | Mock-tragic joke. | ✅ +0.8 s |
| `<cry>` | Shaky, tearful delivery of the following words. | A genuinely sad moment in a dark intro: "<cry> Her only son." | ✅ shaky, quieter delivery (−4.4 dB), not read aloud |
| `<whimper>` | Scared whine. | Comic fear. | ✅ +1.2 s |
| `<moan>` | Low "oh" moan. | Avoid in narration (can read the wrong way). | ✅ heard as "Oh" |

### Anger

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<tsk>` | Disapproving tongue click. | Light judgement: "<tsk> Classic Habsburg move." | ✅ ~70 ms click |
| `<grr>` | Playful growl. | Mock anger. | ✅ "Grrrr!", ~0.7 s |
| `<argh>` | Frustrated "argh". | Narrator's mock frustration. | ✅ heard as "ah"/"uh" |
| `<growl>` | Growl. | Angry character in a skit. | ✅ +1.4 s (heard as "Grow") |
| `<grunt>` | Short effort sound. | Physical action in a skit. | ✅ sound |
| `<hiss>` | Hiss. | Villain or snake joke. | ✅ heard as "suh" |

### Misc

| Tag | Effect | Best use | Test |
|---|---|---|---|
| `<pff>` | Dismissive "pff". | Scoffing at a claim: "He said he was the Tsar. <pff> Sure." | ✅ +1.2 s |
| `<snort>` | Snort. | A ridiculous fact. | ✅ +0.8 s |
| `<throat-clearing>` | Clears throat. | "<throat-clearing> Anyway, back to the war." | ✅ +0.4 s |
| `<cough>` | Cough. | Comedic hint: "totally legal <cough> not really." | ✅ +0.5 s |
| `<sneeze>` | Sneeze. | Gag only. | ✅ heard as "Hachu" |

## Rules for natural sound

1. **Use 1–2 tags per block, about 1 per 15–20 seconds of audio.** More than that sounds like a cartoon.
2. **Put sounds at sentence edges.** Put a sound after the joke, not in the middle of a phrase: `…named it Fanta. <chuckle> Which means imagination.`
3. **Pause, then punchline.** `<short pause>` already gives ~1–2 s, so don't add `...` or a second pause next to it.
4. **Give every tag a real sentence.** Put a full, meaningful phrase after a mode tag (`<whispers> Nobody ever found the body.`). Next to a bare word or nonsense, tags get read aloud.
5. **Don't repeat the same tag back-to-back.** Vary it: `<chuckle>`, `<snort>`, `<pff>`.
6. **The tag must match the Style.** No `<long pause>` in any channel style (SARCASTIC, FAST_SARCASTIC, THEATRICAL_FAST and DARK all ask for few or no long pauses). No `<cackle>` or `<cheer>` in DARK.
7. **Don't stack tags** (`<gasp> <laugh>`). Use one, then the words.
8. **Write the emotion into the words too.** "Oh hell no!" with `<gasp>` works better than the tag alone.
9. **Mind the length.** `<yawn>`, `<heavy breath>` and `<laughter>` add 2–3 s. In a fast short use the short sounds instead (`<chuckle>`, `<tsk>`, `<gasp>`, `<pff>`).

## Channel cheat-sheet (sarcastic history narrator)

| Script moment | Tag | Example |
|---|---|---|
| After a joke or ironic fact | `<chuckle>` ✅ / `<snort>` ✅ | `…your granddad's drug dealer. <chuckle>` |
| Scoffing at a false claim | `<pff>` ✅ | `"I am Dmitri." <pff> Sure you are.` |
| Before a shocking reveal | `<gasp>` ✅ | `An hour later, <gasp> the whole thing explodes.` |
| Before a punchline | `<short pause>` ✅ | `The jury decided it was <short pause> an act of God.` |
| Mock exasperation | `<sigh>` ✅ | `<sigh> They tried it a fourth time.` |
| Light disapproval | `<tsk>` ✅ | `<tsk> Rookie mistake, Napoleon.` |
| Mock outrage | `<shout>` ✅ | `<shout> Half a million liters!` |
| Sarcastic celebration | `<cheer>` ✅ | `<cheer> Rome is saved! For about a week.` |
| Secret or grim aside | `<whispers>` ✅ | `<whispers> Nobody ever found the body.` |
| Transition back to the topic | `<throat-clearing>` ✅ | `<throat-clearing> Anyway.` |
| Dark cold open (DARK style) | `<sigh>` ✅, `<exhales>` ✅, at most one `<short pause>` ✅ | `Nothing lasts. <sigh> Everything ends.` |

Keep for skits rather than narration: `<moan>`, `<scream>`, `<cackle>`, `<sneeze>`. Use `<cry>` only for real tragedy.

## Style (per block)

The overall mood belongs in the block's **Style**: a free-text description or a preset (**Whisper, Friendly, Narration, Promote, Podcast**). Tags add moment-level reactions on top. Channel styles: see channel-voice-profile.md.

## Pitfalls

- Use the exact tag names above, lowercase. Unknown tags may be read aloud.
- Square-bracket tags (`[laughs]`) are the old format. Use `<laugh>`.
- Parenthetical stage directions (`(she sighs)`) are read aloud.
