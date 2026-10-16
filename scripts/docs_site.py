"""Build all tracked documentation and validate the generated site's local links.

Run with the documentation environment's Python:
    python scripts/docs_site.py
    python scripts/docs_site.py serve

MkDocs also loads on_pre_build as a hook to refresh sources during live preview.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / '.build' / 'docs'
SITE = ROOT / '.build' / 'site'
BASE_PATH = '/google-ai-studio-tts/'


def tracked_files():
    result = subprocess.run(
        ['git', 'ls-files', '-z'], cwd=ROOT, check=True, capture_output=True
    )
    return [Path(name) for name in result.stdout.decode().split('\0') if name]


def document_path(source):
    if source == Path('README.md'):
        return Path('index.md')
    if source == Path('LICENSE'):
        return Path('LICENSE.md')
    return source


def prepare_docs():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    documents = []
    for source in tracked_files():
        if source.suffix == '.md' or source == Path('LICENSE'):
            target = DOCS / document_path(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            text = (ROOT / source).read_text(encoding='utf-8')
            if source == Path('LICENSE'):
                text = '# MIT license\n\n```text\n' + text + '```\n'
            else:
                # Adapt links in the generated copy, keeping GitHub sources intact.
                text = re.sub(
                    r'(\]\((?:\.\./)*)(README\.md|LICENSE)(?=[)#])',
                    lambda match: match[1] + {
                        'README.md': 'index.md', 'LICENSE': 'LICENSE.md'
                    }[match[2]],
                    text,
                )
                text = text.replace('<details>', '<details markdown="1">')
            target.write_text(text, encoding='utf-8')
            documents.append(document_path(source))
        elif source.parts[0] == 'scripts' and source.suffix in {'.py', '.js'}:
            target = DOCS / source
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / source, target)
    return documents


def on_pre_build(config):
    prepare_docs()


class PageLinks(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag in {'a', 'link'} and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in {'img', 'script'} and attrs.get('src'):
            self.links.append(attrs['src'])


def check_site():
    pages = {
        path.resolve(): PageLinks(path.read_text(encoding='utf-8'))
        for path in SITE.rglob('*.html')
    }
    errors = []
    checked = 0
    for page, content in pages.items():
        for link in content.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith('/'):
                if not path.startswith(BASE_PATH):
                    errors.append(f'{page.relative_to(SITE)}: outside site: {link}')
                    continue
                target = SITE / path.removeprefix(BASE_PATH)
            else:
                target = page.parent / path if path else page
            target = target.resolve()
            if not target.is_relative_to(SITE.resolve()):
                errors.append(f'{page.relative_to(SITE)}: outside site: {link}')
                continue
            if target.is_dir():
                target /= 'index.html'
            checked += 1
            if not target.is_file():
                errors.append(f'{page.relative_to(SITE)}: missing target: {link}')
            elif url.fragment and target in pages:
                if unquote(url.fragment) not in pages[target].ids:
                    errors.append(f'{page.relative_to(SITE)}: missing anchor: {link}')
    for source in tracked_files():
        if source.suffix == '.md' or source == Path('LICENSE'):
            document = document_path(source)
            output = (SITE / document.parent / document.stem / 'index.html'
                      if document.name != 'index.md'
                      else SITE / document.parent / 'index.html')
            if not output.is_file():
                errors.append(f'Document was not published: {source}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated {len(pages)} HTML pages and {checked} local links/assets.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['build', 'serve'], default='build', nargs='?')
    args = parser.parse_args()
    documents = prepare_docs()
    print(f'Prepared {len(documents)} documentation pages.', flush=True)
    subprocess.run(
        [sys.executable, '-m', 'mkdocs', args.command, '--strict'],
        cwd=ROOT, check=True,
    )
    if args.command == 'build':
        check_site()


if __name__ == '__main__':
    main()
