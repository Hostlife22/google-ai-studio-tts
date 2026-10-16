# Contributing to Google AI Studio TTS

Contributions are welcome: clearer examples, updated browser selectors, voice and delivery observations, audio-analysis fixes and accessibility improvements. Keep changes focused and reproducible.

## Before you start

Check the [open issues](https://github.com/Hostlife22/google-ai-studio-tts/issues) for related work. Discuss a new browser backend, dependency or substantial workflow change in an issue first. Small corrections can go straight to a pull request.

Report vulnerabilities through [SECURITY.md](SECURITY.md). For accessibility barriers, follow [ACCESSIBILITY.md](ACCESSIBILITY.md#report-an-accessibility-issue).

## Local setup

Fork and clone the repository, then create a branch for your change. The skill and reference documents do not need a build step. Browser verification requires Chrome, an agent with the `claude-in-chrome` MCP tools and your own signed-in Google AI Studio session.

For the optional analysis helpers:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install numpy praat-parselmouth
```

The tag-analysis workflow additionally needs FFmpeg, `whisper-cli` and a compatible Whisper model. See the [audio-analysis examples](README.md#audio-analysis).

## Project conventions

- Write shared documentation and code comments in English. Examples may demonstrate other languages.
- Keep the agent workflow in `SKILL.md`; keep detailed selectors, voice notes, tags and presets in `references/`.
- Prefer accessible names and stable selectors. Check input updates in the live Angular editor rather than assuming a DOM value change persists.
- Distinguish a measured observation from an expected behavior. For voice, tag and pacing results, record the date, model shown by the UI, voice, language, style and test text.
- Avoid presenting a quota, voice list, timing or model identifier as a permanent service guarantee.
- Keep account access under the user's control. Do not add credentials, browser profiles, cookies, private transcripts or recordings to a contribution.
- Follow the [accessibility guidance](ACCESSIBILITY.md#contribution-guidance) when changing instructions or examples.

## Validate your change

Choose checks that exercise what changed. Documentation edits need a review of local links, heading anchors and example commands.

Check whitespace and script syntax without creating audio or spending quota:

```sh
git diff --check
node --check scripts/tts-bench.js
python3 - <<'PY'
import ast
from pathlib import Path

for path in Path('scripts').glob('*.py'):
    ast.parse(path.read_text(), filename=str(path))
    print(f'OK: {path}')
PY
```

Syntax checks do not verify browser behavior. For selector or workflow changes, manually check the affected controls in AI Studio and record what you verified. Generation consumes account quota; use a short, non-sensitive script and obtain the user's authorization when testing in their session. Avoid unrelated batch generations.

For analysis changes, use a recording you can share or describe a reproducible synthetic sample. Document its format and dependencies, compare relevant metrics, and listen to any affected clips. Keep generated output out of the commit.

## Submit a pull request

Build the documentation before submitting changes to guides or repository policies:

```sh
python -m pip install -r requirements-docs.txt
python scripts/docs_site.py
```

Stage new Markdown files and add them to the navigation in `mkdocs.yml`. See [documentation, CI and releases](DOCUMENTATION.md) for live preview and tagged-release packaging. GitHub Actions checks every pull request, publishes successful `main` builds to Pages, and builds release archives for every pushed tag.

Describe the problem, resulting behavior and verification. For browser changes, include the observed model and affected control; for audio changes, include the test conditions and relevant measurements. Redact account information from screenshots and logs. Update affected references and add a changelog entry for a user-visible change.

Submit only material you can contribute under the project's [MIT license](LICENSE), and retain notices for any separately licensed material. Keep feedback respectful and focused on the work.
