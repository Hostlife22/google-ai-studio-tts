# Documentation, CI and releases

The complete documentation is published at [hostlife22.github.io/google-ai-studio-tts](https://hostlife22.github.io/google-ai-studio-tts/). It includes the README, agent instructions, every reference guide, project policies, changelog and MIT license.

The site uses MkDocs Material, with full-text search in English and Russian, section navigation, page contents, code-copy controls and light/dark themes. The source Markdown files remain the canonical documentation.

## Local build

Install Python 3.12 and create an environment for documentation tools:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/docs_site.py
```

The builder collects tracked Markdown files and the license into `.build/docs`, then generates the site in `.build/site`. It adapts README and license links in the generated copy and includes tracked Python/JavaScript helpers as downloadable files. Generated files are ignored by Git.

Stage new documentation with `git add` before building so the site can discover it. Add each new page to `nav` in `mkdocs.yml`. Strict validation fails on missing navigation entries, broken local links and missing heading anchors. The final HTML check also verifies local assets and confirms every tracked document was published. External services are not contacted by the link checker.

## Local preview

```sh
python scripts/docs_site.py serve
```

Open the URL printed by MkDocs, normally `http://127.0.0.1:8000/google-ai-studio-tts/`. Existing documentation and reference changes trigger a rebuild. If you add a new document, stage it, update the navigation and restart the preview. Stop the server with Ctrl+C.

## Continuous integration

The [GitHub Actions workflow](https://github.com/Hostlife22/google-ai-studio-tts/blob/main/.github/workflows/ci.yml) runs on pull requests, pushes to `main`, every pushed tag and manual dispatches.

Every run checks source syntax and whitespace, builds the full documentation with warnings treated as errors, and validates generated local links, assets and document coverage. The documentation build does not open AI Studio or consume speech-generation quota.

Successful builds of `main` publish the site using the GitHub Pages artifact and deployment actions. Pull requests and tags validate documentation without replacing the live site. Repository **Settings → Pages → Source** must be **GitHub Actions**; the repository is configured for this publishing method.

## Tagged releases

Push a tag on a commit containing the workflow to build and publish a release. For example, after updating `main` and choosing the next unused version:

```sh
git switch main
git pull --ff-only
git tag -a v1.0.0 -m "Google AI Studio TTS v1.0.0"
git push origin v1.0.0
```

A local tag alone does not trigger CI. Every pushed tag runs the build; the release job runs only after it succeeds. Tags containing a hyphen, such as `v1.0.0-rc.1`, create prereleases.

The [GitHub Release](https://github.com/Hostlife22/google-ai-studio-tts/releases) contains generated release notes and four uploaded assets:

| Asset | Contents |
| --- | --- |
| `google-ai-studio-tts-<tag>-source.zip` | All files committed at the tagged revision |
| `google-ai-studio-tts-<tag>-source.tar.gz` | The same committed source as a compressed tar archive |
| `google-ai-studio-tts-<tag>-docs.zip` | The complete built documentation site for that revision |
| `SHA256SUMS` | SHA-256 checksums for the three archives |

Archive filenames replace characters outside letters, digits, dots, hyphens and underscores with hyphens. GitHub also supplies its standard source downloads. Tags do not change the live documentation site, which continues to follow `main`.

To inspect packaging locally after building the site:

```sh
python scripts/package_release.py v1.0.0-local
cd dist
shasum -a 256 -c SHA256SUMS
```

Packaging reads committed source from `HEAD`; commit changes first when verifying a release candidate. Avoid moving a published tag or reusing an existing release tag. If a build fails, correct the issue before pushing the next tag. A failed deployment can be rerun from the repository's Actions page.
