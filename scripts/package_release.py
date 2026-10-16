"""Package committed sources and the built documentation for a tagged release."""

import argparse
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
SITE = ROOT / '.build' / 'site'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('version', help='Release tag used in archive filenames')
    args = parser.parse_args()
    version = re.sub(r'[^A-Za-z0-9._-]', '-', args.version)
    prefix = f'google-ai-studio-tts-{version}'
    if not (SITE / 'index.html').is_file():
        raise SystemExit('Build the documentation before packaging a release.')
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    archives = []
    for extension in ['zip', 'tar.gz']:
        archive = DIST / f'{prefix}-source.{extension}'
        subprocess.run(
            ['git', 'archive', f'--prefix={prefix}/', f'--output={archive}', 'HEAD'],
            cwd=ROOT, check=True,
        )
        archives.append(archive)

    docs_archive = DIST / f'{prefix}-docs.zip'
    with zipfile.ZipFile(docs_archive, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SITE.rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(SITE))
    with zipfile.ZipFile(docs_archive) as archive:
        if archive.testzip() is not None or 'index.html' not in archive.namelist():
            raise SystemExit('Documentation archive verification failed.')
    archives.append(docs_archive)

    lines = [
        f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n'
        for path in sorted(archives)
    ]
    (DIST / 'SHA256SUMS').write_text(''.join(lines), encoding='utf-8')
    print(f'Created {len(archives)} archives and SHA256SUMS in {DIST}')


if __name__ == '__main__':
    main()
