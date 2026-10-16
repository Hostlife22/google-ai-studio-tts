# Google AI Studio TTS

Generate speech, podcasts, narration and voiceovers with Gemini in Google AI Studio. This agent skill controls the live speech editor in Chrome through the `claude-in-chrome` MCP tools, with guides for voices, expression tags, pacing and two-speaker dialogue.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent skill](https://img.shields.io/badge/Agent-skill-6f42c1.svg)](SKILL.md)
[![Google AI Studio](https://img.shields.io/badge/Google-AI_Studio-4285F4.svg)](https://aistudio.google.com/generate-speech)

**Up to 2 speakers · 40 documented expression tags · 15 delivery modes · Local audio analysis tools**

[Quick start](#quick-start) · [Examples](#examples) · [Voice and delivery](#voice-and-delivery) · [Audio analysis](#audio-analysis) · [Documentation](#documentation) · [Project information](#project-information)

## Quick start

### Install the skill

With Node.js and the [Skills CLI](https://github.com/vercel-labs/skills), install it for your agent:

```sh
npx skills add Hostlife22/google-ai-studio-tts
```

Alternatively, clone the repository and follow your agent's instructions for loading a local skill. Keep `SKILL.md`, `references/` and `scripts/` together:

```sh
git clone https://github.com/Hostlife22/google-ai-studio-tts.git
cd google-ai-studio-tts
```

Installing the skill supplies instructions and reference files. Browser access must be configured separately.

### Connect the browser

1. Use an agent with access to the `claude-in-chrome` MCP tools listed in [SKILL.md](SKILL.md#required-tools).
2. Open Chrome and sign in to [Google AI Studio](https://aistudio.google.com/generate-speech) yourself.
3. Ask the agent to use `google-ai-studio-tts` and provide your script, language and desired delivery.

The generation workflow uses your existing browser session; it does not require an API key in this repository. Each Run consumes your account's TTS quota. Available models, voices and controls depend on the live AI Studio interface.

### Generate your first voiceover

> Use google-ai-studio-tts to narrate this text in English with a calm, friendly delivery. Choose an available voice and leave the result ready to play in AI Studio: “Every great story starts with a question. What will yours be?”

The agent opens a dialog, fills the speech blocks, selects voices and styles, and runs generation. It reports the result and leaves the tab open for playback. Ask explicitly if you also want to download the audio.

## Examples

### Two-host podcast

> Use Google AI Studio TTS to turn this script into a two-host podcast. Use Puck and Zephyr if they are available, keep the delivery conversational, and alternate the speakers. Host A: “Why do we remember some stories?” Host B: “Because they make us feel something.”

Assign speakers through the editor controls. Writing `Speaker 1:` inside a speech block can make the label part of the spoken audio.

### Short-form narration

> Use google-ai-studio-tts to voice this 45-second history script with the Enzo channel preset. Plan the delivery modes and estimated timing before generating, and use a few expression tags where they fit the story.

The bundled channel preset uses Enzo for both speaker slots and changes delivery by block. Specify your preferred voice and style to override that preset.

### Russian voiceover

> Используй google-ai-studio-tts: озвучь этот текст по-русски, спокойно и выразительно. Подбери доступный голос и оставь аудио готовым к прослушиванию: «Иногда самый короткий путь к открытию начинается с простого вопроса».

### Expression and pauses

Use per-block **Style** for overall delivery and inline tags for individual reactions:

```text
And then, <sigh> they tried the exact same thing again.
The room went quiet. <short pause> Someone knocked.
```

Tags need meaningful surrounding text. Their sound and timing vary between renders; a tag may be spoken literally in unsuitable context. See the [expression-tag reference](references/audio-tags.md) for observations and examples.

## Voice and delivery

| Control | Use it for | Guide |
| --- | --- | --- |
| Voice picker | Choose an available voice for each speaker | [Voices](references/voices.md) |
| Style | Set tone, emotion and pace for a speech block | [Delivery modes](references/delivery-modes.md) |
| Expression tags | Add reactions, breaths, laughter and pauses | [Audio tags](references/audio-tags.md) |
| Channel preset | Plan expressive history shorts and long narration | [Channel voice profile](references/channel-voice-profile.md) |
| Speaker settings | Assign voices, aliases and dialogue roles | [Skill workflow](SKILL.md) |

The references record project observations from October 2026. Voice names and selectors should be checked against the current page. Measured speech rates and tag durations describe individual renders, rather than guaranteed output.

For long scripts, the guide recommends chunks of roughly 1–2 minutes and combining them in your editor. This is a working recommendation, not a measured service limit.

## Audio analysis

The Python helpers are optional. You can generate speech through the browser without installing them.

Create an isolated environment for local analysis:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install numpy praat-parselmouth
```

| Tool | Purpose | Requirements |
| --- | --- | --- |
| [ref_analyze_praat.py](scripts/ref_analyze_praat.py) | Pitch, pitch variation, pauses and optional speech rate | NumPy, praat-parselmouth; an adjacent `.txt` transcript enables WPM |
| [ref_pitch_acf.py](scripts/ref_pitch_acf.py) | Autocorrelation pitch estimate over the first 40 seconds | NumPy; use mono 16-bit PCM WAV input |
| [tag_test.py](scripts/tag_test.py) | Build tag-test text; split and transcribe a downloaded render | NumPy; analysis also needs FFmpeg, `whisper-cli` and a compatible model |
| [tts-bench.js](scripts/tts-bench.js) | Compare voices and delivery in the live AI Studio page | Browser JavaScript tool and a prepared speech dialog; each case consumes generation quota |

Analyze a local recording:

```sh
python scripts/ref_analyze_praat.py narration.wav
python scripts/ref_pitch_acf.py narration-mono.wav
```

Prepare expression-tag test text:

```sh
python scripts/tag_test.py text sigh gasp tsk
```

After generating and downloading that test, create an output directory and analyze it. Replace the model path with your own compatible Whisper model:

```sh
mkdir -p renders/tag-test
python scripts/tag_test.py analyze render.wav /path/to/ggml-base.en.bin renders/tag-test sigh gasp tsk
```

Listen to the clips as well as checking the measurements. Transcription alone does not establish whether a non-speech expression was produced. Reference audio, transcripts, model files and generated clips are not bundled.

## Documentation

| Resource | Contents |
| --- | --- |
| [Skill instructions](SKILL.md) | Browser tools, generation workflow and account boundaries |
| [Selectors](references/selectors.md) | Editor controls, Angular-safe input and browser troubleshooting |
| [Voices](references/voices.md) | Featured voices, search and speaker selection |
| [Expression tags](references/audio-tags.md) | 40 documented tags, context guidance and measured observations |
| [Delivery modes](references/delivery-modes.md) | 15 modes, tempo planning, punctuation and script structure |
| [Channel voice profile](references/channel-voice-profile.md) | Enzo presets and reference-narrator measurements |

<details>
<summary>Repository layout</summary>

```text
google-ai-studio-tts/
├── SKILL.md                 # Instructions for the agent
├── README.md                # Installation, examples and documentation
├── references/              # Voices, tags, selectors and delivery guides
├── scripts/                 # Browser benchmarking and local audio analysis
├── CONTRIBUTING.md          # Contribution and validation guidance
├── SECURITY.md              # Vulnerability reporting and browser-session handling
├── ACCESSIBILITY.md         # Transcripts, listening needs and known limitations
├── CHANGELOG.md             # Project changes
├── LICENSE                  # MIT license
└── THIRD_PARTY_NOTICES.md    # External services, tools and attribution
```

</details>

## Project information

| Resource | Details |
| --- | --- |
| [Contributing](CONTRIBUTING.md) | Setup, documentation conventions and validation before a pull request |
| [Changelog](CHANGELOG.md) | Changes to the skill and repository |
| [MIT license](LICENSE) | Maintained by [Hostlife22](https://github.com/Hostlife22) |
| [Security](SECURITY.md) | Vulnerability reporting, browser sessions and local execution |
| [Accessibility](ACCESSIBILITY.md) | Transcripts, output guidance, current support and limitations |
| [Third-party notices](THIRD_PARTY_NOTICES.md) | External services, dependencies and naming |

This is an independent project, unaffiliated with Google or Anthropic. Google AI Studio, Gemini and Chrome are Google products; Claude is an Anthropic product.
