---
name: google-ai-studio-tts
description: Generate speech, podcasts, voiceovers, and two-speaker dialogue with Google AI Studio's Gemini Flash TTS by driving the live web app in Chrome via the claude-in-chrome MCP server. Use whenever the user asks to (1) create a podcast, audiobook chapter, narration, audio drama, or voiceover with Gemini / Google AI Studio TTS; (2) turn a script into two-speaker audio (e.g. "two-host podcast", "Speaker 1 / Speaker 2 dialogue", "Puck and Zephyr"); (3) tweak a TTS prompt with per-block Style, voice picker, speaker names, Filler words, or Temperature; or (4) render audio with inline expression tags like <gasp>, <sigh>, <tsk>. Triggers on phrases like "use AI Studio TTS", "generate this podcast in AI Studio", "render with gemini-3.8-flash-tts", "speak this with Fola/Puck/Zephyr", "сделай озвучку", or any request for browser-driven Gemini speech generation.
---

# Google AI Studio TTS (browser-driven)

## Overview

This skill drives `https://aistudio.google.com/generate-speech` in the user's already-open Chrome (via the `claude-in-chrome` MCP tools) to render audio with Gemini Flash TTS. The user must already be signed in to Google AI Studio in Chrome — never create accounts, never enter passwords, never share credentials.

The playground is a **block editor** (one "speech block" per utterance). There is no Text/Composer toggle and no Scene / Sample Context / Audio Profile / Director's note fields anymore — tone is steered per block via **Style** and inline **expression tags**.

The model is **dual-speaker**: at most Speaker 1 and Speaker 2.

Selectors and gotchas: [references/selectors.md](references/selectors.md). Tags: [references/audio-tags.md](references/audio-tags.md). Voices: [references/voices.md](references/voices.md). Delivery modes (tempo, emotion, pauses): [references/delivery-modes.md](references/delivery-modes.md).

**Channel preset (momentum history videos):** unless the user asks otherwise, use the voice and Style presets from [references/channel-voice-profile.md](references/channel-voice-profile.md). Scripts are in English by default. Use one voice for everything: **Enzo**. Base modes: THEATRICAL_FAST for shorts, SARCASTIC for the body of long videos. Pick the mode per block from [references/delivery-modes.md](references/delivery-modes.md): 15 calibrated delivery modes, a tempo ladder from 110 to 300 wpm, structure templates for shorts and long videos, and pause/punctuation rules. These were matched to the reference videos by measured pitch, intonation range and tempo.

**Voicing a channel script (short or long):**
1. Strip the editor layer: `[annotations]`, on-screen `(captions)` and emoticons.
2. Split the script into beats of 1–4 sentences and give each beat a mode using the decision rules in delivery-modes.md ("Assigning modes to a script"): format → position rules → cue table → priority order. Show the user the block/mode plan with estimated durations before clicking Run.
3. Merge consecutive beats with the same mode into one block. Use a new block whenever the mode changes. Set both speakers to Enzo.
4. Add 1–2 expression tags per block where the script has a reaction (audio-tags.md). Keep rhetorical questions, `…` and `—` per the punctuation rules.
5. For long videos, render in chunks of ~1–2 minutes (8–12 blocks) and stitch them in the edit. This keeps each Run manageable. Chunk length is a recommendation, not a tested limit.

**Quota:** each Run spends the daily TTS quota. Don't batch many test generations unless the user asked for voice testing.

## Required tools

Load these claude-in-chrome MCP tools via `ToolSearch` in one call before starting:

```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__find,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__tabs_close_mcp
```

## End-to-end workflow

### 1. Open the page

```
tabs_context_mcp({ createIfEmpty: true })
navigate({ tabId, url: "https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-tts" })
```

If AI Studio auto-switches to another TTS model, accept it. If the cookie notice bar is shown at the bottom, click its **Hide** button (`button.glue-cookie-notification-bar__accept`) — it covers the Run bar.

### 2. Open an empty dialog

The page lands on a gallery ("Turn text into natural-sounding speech"). Click the **Create new dialog** card:

```js
document.querySelector("mat-card.create-dialog-card").click();
```

The template cards next to it (`mat-card.dialog-example-card`: The Everyday Assistant, The Energetic Co-Host, The Master Storyteller, The Ad Voiceover, …) open pre-filled examples — use one only if the user asked for that template.

After clicking you get one empty block with `Speaker 1 - <voice>` (default voice is currently **Fola**).

### 3. Fill the blocks

Each block (`ms-speech-block`) contains:

- Speaker chip `button.voice-chip` — text `Speaker N - VoiceName`; click opens the voice library for **that speaker**.
- **Style** chip `button.attribute-chip[aria-label="Style"]` — per-block delivery style (step 4).
- **+ Expression** `button.add-expression-btn` — toggles a row of tag chips (`button.tag-chip`) that insert `<tag>` at the cursor.
- Textarea `textarea[aria-label="Speech block text"]`.
- Preview `button.play-block-btn`, `Delete speech block` button.

Add a block with `button.add-speech-block-button`. **New blocks alternate speakers** (1, 2, 1, 2…) — they do not inherit the previous speaker. Plan block order accordingly: for a monologue use a single block (it can hold several sentences); for a dialogue write alternating lines.

Set text with the Angular-safe helper from references/selectors.md (or click the textarea and use `computer` → `type`). Plain `el.value = …` does not stick.

Write the script in the language the user wants — Russian works fine.

### 4. (Optional) Style per block

Click the Style chip → menu with a free-text field `textarea.daikon-custom-style-textarea` ("Describe the voice style. e.g. Tone, mood, pace...") and presets (`button.attribute-menu-item`): **Whisper, Friendly, Narration, Promote, Podcast**. Only set it if the user asked for a specific delivery.

### 5. Choose voices

Click a block's speaker chip or the speaker card in the right panel (`button.active-voice-card-trigger`). The **Speaker settings** panel opens with:

- Search box `input[aria-label="Search voices"]` ("Search 2,000+ voices") — classic Gemini voices (Puck, Zephyr, Kore, Charon, Aoede…) are found here.
- Filters: Language, Gender, Pitch, Style, Use case.
- Grouped featured voices (`button.voice-card-content`, `aria-label` = voice name). Click a card to select it.
- Close with `button[aria-label="Close panel"]`.

The right panel also has a **Speaker name** input (`input.speaker-alias-input`) per speaker and, with two speakers, a **Filler words** toggle (`button[aria-label="Filler words"]`, adds "um/uh"-style disfluencies). Touch these only on request.

### 6. (Optional) Temperature

Click `button[aria-label="Expand or collapse Model settings"]`; Temperature is `input.slider-number-input` (0–2, default 1). Only change on request.

### 7. Run

```js
document.querySelector("button.ctrl-enter-submits").click();
```

Run is **disabled while any block is empty** — delete or fill empty blocks first. Render takes ~5–30 s. Detect completion by `document.querySelector("audio").duration > 0` (or the bottom bar's right counter `0:06` becoming non-zero — note there is no `/` between the counters).

### 8. Hand off

Tell the user the audio is ready (duration, voice, text) and point at the play button in the bottom bar (`button.play-pause-button`). Downloading (`button.download-button`) only on explicit request. Leave the AI Studio tab open so they can listen; close any extra tabs you opened.

## Prompting guidance

- Expression tags use **angle brackets**: `<gasp>`, `<sigh>`, `<tsk>`, `<short pause>`. The UI inserts them this way; typing `<` in a block opens tag suggestions. See references/audio-tags.md for the full list and test results. All 40 tags work when placed in a meaningful sentence. Next to a bare word or nonsense, they can be read aloud.
- Put the overall mood into **Style** (one short description per block), and use tags for moment-to-moment reactions.
- For a two-host podcast, the "Podcast" featured group (Brio, Jori, Rami) or classic Puck + Zephyr are safe pairs.

## What NOT to do

- Don't sign in, accept new ToS, or change account settings.
- Don't download generated audio without an explicit user ask.
- Don't navigate away from the AI Studio tab while a render is in flight — use a separate tab for exploration.
- Don't add a third speaker — the model is dual-speaker.
- Don't fabricate voice names — confirm via the search box; if missing, suggest the closest match.
- Don't `el.value = "…"` on Angular textareas without dispatching `input`/`change` events.
