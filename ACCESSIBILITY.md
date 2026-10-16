# Accessibility

Google AI Studio TTS aims to make its instructions and generated speech workflows usable by people with different hearing, visual, motor and cognitive needs. This repository provides documentation and helper scripts; the speech editor and playback controls belong to Google AI Studio.

## Current support and limitations

- Documentation uses headings, descriptive links, tables and copyable text examples. The README does not autoplay audio or animation.
- Scripts remain available as text before speech generation. Preserve that text as a transcript when sharing the resulting audio.
- The skill documents accessible labels for many browser controls, but browser automation does not establish keyboard or screen-reader accessibility of the underlying service.
- Voice, speaking rate, style and pauses can be adjusted through the workflow. Generated pronunciation, loudness, intelligibility and expression timing require listening review.
- The repository does not generate synchronized captions, sign-language interpretation or audio descriptions automatically.
- Pitch, silence and transcription measurements do not establish accessibility or the quality of a transcript. No complete accessibility conformance audit has been performed.

## Sharing accessible audio

Provide a text transcript alongside an audio-only recording. Identify speakers by name in the transcript and include meaningful non-speech sounds, such as laughter or a gasp, when needed to understand the content.

For videos, provide synchronized captions for speech and meaningful sounds. Include descriptions of essential visual information when the narration does not convey it.

Choose a pace that suits the audience. Explain unfamiliar terms, check pronunciation and leave enough space between ideas. Listen for clipped words, sudden loudness changes and expression tags read aloud. Offer the script so a listener can follow the content without audio.

When embedding audio in another project, provide keyboard-accessible controls with accessible names, visible focus and pause/stop controls. Let people start playback themselves and adjust volume and speed where possible.

## Contribution guidance

- Keep instructions sequential and explain prerequisites before commands.
- Use descriptive links and meaningful headings. Give informative images alternative text and include essential information in prose.
- Pair audio demonstrations with transcripts and identify voices and speaker turns in text.
- Use text labels as well as color or badges to communicate status.
- Prefer controls with accessible names in browser instructions. Describe any keyboard or assistive-technology checks you actually performed.
- Report listening observations separately from automated measurements; avoid claiming accessibility based only on a successful render.

## Report an accessibility issue

Open an [issue](https://github.com/Hostlife22/google-ai-studio-tts/issues) with **Accessibility:** in the title. Include the affected file or workflow, the barrier, expected behavior and your browser, operating system or assistive technology when relevant. A timestamp helps identify a problem in an audio example.

Share only information you are comfortable making public; no medical details are needed. If the barrier is in the external AI Studio interface, explain which step it affects so this project can document a workaround where possible.
