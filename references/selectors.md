# DOM selectors and Angular gotchas

The AI Studio playground is an Angular app. These selectors were verified live against `https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-tts` on 2026-10-15. Google changes them — if a selector returns null, fall back to `find` (natural-language search) before failing.

## Landing gallery

| Element | Selector |
|---|---|
| Create new dialog | `mat-card.create-dialog-card` |
| Template dialogs | `mat-card.dialog-example-card` (Everyday Assistant, Energetic Co-Host, Master Storyteller, Ad Voiceover, …) |
| Create new voice | `mat-card.create-voice-card` |
| Voice presets | `mat-card.voice-card` (aria-label = "Name - description") |
| Cookie notice "Hide" | `button.glue-cookie-notification-bar__accept` |

## Speech blocks (`ms-speech-block`, one per utterance)

| Element | Selector | Notes |
|---|---|---|
| Text | `textarea[aria-label="Speech block text"]` | Indexed in DOM order. Placeholder: "Type what you want the model to say... Type '<' to add expression tags." |
| Speaker chip | `button.voice-chip` | Text `Speaker N - VoiceName`. Opens the voice library for that speaker. |
| Style chip | `button.attribute-chip[aria-label="Style"]` | Opens style menu (below). |
| Expression toggle | `button.add-expression-btn` | Shows/hides tag chips row. |
| Tag chip | `button.tag-chip` | Inserts `<tag> ` at cursor. |
| Preview block | `button.play-block-btn` | aria-label "Preview this block". |
| Speech to text | `button[aria-label="Speech to text"]` | Mic — don't use. |
| Delete block | `button[aria-label="Delete speech block"]` | |
| Add block | `button.add-speech-block-button` | New block alternates speaker (1→2→1…). |

### Style menu (overlay `.voice-style-dropdown-menu`)

| Element | Selector |
|---|---|
| Custom style text | `textarea.daikon-custom-style-textarea` (aria-label "Describe the voice style") |
| Presets | `button.attribute-menu-item` — Whisper, Friendly, Narration, Promote, Podcast |
| Close | click `.cdk-overlay-backdrop` |

## Speaker settings panel (overlay, `ms-speaker-settings-panel`)

| Element | Selector |
|---|---|
| Search | `input[aria-label="Search voices"]` |
| Filters | `button.filter-dropdown-chip` — Language, Gender, Pitch, Style, Use case |
| Voice card | `button.voice-card-content` (aria-label = voice name) |
| Voice sample | `button.play-pill` |
| View all in group | `button.group-view-all-btn` |
| New voice | `button.new-voice-btn` |
| Close | `button[aria-label="Close panel"]` |

## Right side panel (`ms-run-settings`)

| Element | Selector |
|---|---|
| Model card | `button.model-selector-card` |
| Model settings expander | `button[aria-label="Expand or collapse Model settings"]` |
| Temperature | `input.slider-number-input` (visible after expanding; 0–2, default 1) |
| Speaker card | `button.active-voice-card-trigger` (aria-label "Open voice settings") |
| Speaker name | `input.speaker-alias-input` |
| Filler words toggle | `button[aria-label="Filler words"]` (only with 2 speakers) |
| Get code | `button[aria-label="Get code"]` |

## Bottom bar (`ms-audio-footer`)

| Element | Selector |
|---|---|
| Run | `button.ctrl-enter-submits` (disabled if any block is empty; also Cmd/Ctrl+Enter) |
| Play / pause | `button.play-pause-button` |
| Download | `button.download-button` |
| Audio element | `audio` |

## Setting Angular textareas

```js
function setNgInputValue(el, value) {
  const proto = el instanceof HTMLInputElement ? HTMLInputElement.prototype : HTMLTextAreaElement.prototype;
  Object.getOwnPropertyDescriptor(proto, "value").set.call(el, value);
  el.dispatchEvent(new Event("input", { bubbles: true }));
  el.dispatchEvent(new Event("change", { bubbles: true }));
  el.dispatchEvent(new Event("blur", { bubbles: true }));
}

setNgInputValue(document.querySelectorAll('textarea[aria-label="Speech block text"]')[0],
                "Привет! <laugh> Это тест.");
```

Clicking the textarea and using `computer` → `type` also works and is the most robust option.

## Detecting render completion

```js
const isReady = () => (document.querySelector("audio")?.duration || 0) > 0;
```

The bottom bar text reads `0:00 … 0:06` (no slash) — don't regex for `X:XX / Y:YY`.

## Common breakage modes

- **Run does nothing / is greyed out.** A block is empty — fill or delete it.
- **Cookie bar covers the bottom bar.** Click Hide.
- **Wrong speaker on a block.** Blocks alternate speakers automatically; reorder/delete blocks rather than expecting a speaker picker on the chip.
- **Overlay stays open.** Click `.cdk-overlay-backdrop` or the panel's Close button before the next action.
