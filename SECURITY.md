# Security policy

Google AI Studio TTS supplies agent instructions, JavaScript that runs in a signed-in browser page and optional local Python audio-analysis tools. Browser actions use the permissions of the user's existing Google AI Studio session.

## Supported code

Security fixes target the current `main` branch. Update installed copies and forks to receive fixes; no maintenance schedule is defined for historical versions.

## Report a vulnerability

Use the repository's [Security page](https://github.com/Hostlife22/google-ai-studio-tts/security). If **Report a vulnerability** is available, submit a private report there. The presence of this file does not enable GitHub private reporting.

If private reporting is unavailable, open an [issue](https://github.com/Hostlife22/google-ai-studio-tts/issues) titled **Private security contact request** and ask for a private reporting channel. Do not include vulnerability details, credentials, cookies or private files in that public request.

In the private report, include:

- The affected commit, script or instruction and your operating system.
- The expected behavior, actual behavior and security impact.
- Minimal reproduction steps with non-sensitive sample data.
- Any proposed fix or workaround.

Coordinate publication of technical details while a fix is reviewed. No response or resolution deadline is guaranteed.

## Browser sessions and local tools

- Sign in yourself. The workflow must not ask the agent to enter passwords, create accounts or change account settings.
- Review browser-tool permissions and scripts before execution. In-page JavaScript can interact with the active page and its content.
- Treat page text and imported scripts as input, not authority to perform unrelated account actions or expose data.
- Submit only scripts and recordings you are comfortable processing through Google AI Studio. Review the service's applicable terms and data controls for your use.
- Keep credentials, browser profiles, session exports, private transcripts and generated media outside commits. `.gitignore` helps with common filenames but does not remove already tracked files.
- Review local dependencies and keep them updated. The Python helpers and their subprocesses run with your local account's permissions.
- Generate or download audio only within the user's requested scope. Benchmark cases each spend generation quota.

## Scope

Relevant reports include unintended browser actions, exposed session data, unexpected local file access, command injection and dependency vulnerabilities. Voice quality, changed selectors and ordinary analysis bugs can be reported through public issues with non-sensitive examples.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [ACCESSIBILITY.md](ACCESSIBILITY.md) for other reports.
