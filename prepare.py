#!/usr/bin/env python3
"""Fetch the pinned diagrams.net browser distribution, then stage reviewed assets.

Run at build time. This does not run on visitor computers; generated files and
node_modules are intentionally excluded from source control.
"""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
COMMIT = '84487b4891cbc0f32d7e30f34cf878c87cb1f414'
assets = json.loads((HERE / 'app.json').read_text())['assets']
with tempfile.TemporaryDirectory(prefix='codi-drawio-') as directory:
    repo = Path(directory)
    def git(*args):
        subprocess.run(['git', '-C', str(repo), *args], check=True, stdout=subprocess.DEVNULL)
    git('init', '--quiet')
    git('remote', 'add', 'origin', 'https://github.com/jgraph/drawio.git')
    git('config', 'core.sparseCheckout', 'true')
    (repo / '.git/info/sparse-checkout').write_text('/src/main/webapp/\n')
    git('fetch', '--quiet', '--depth=1', '--filter=blob:none', 'origin', COMMIT)
    git('checkout', '--quiet', '--detach', 'FETCH_HEAD')
    actual = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != COMMIT:
        raise RuntimeError('Unexpected diagrams.net source commit')
    source = repo / 'src/main/webapp'
    target = HERE / 'node_modules/drawio'
    for name in assets:
        if name == 'LICENSE.drawio.txt':
            continue
        rel = Path(name).relative_to('node_modules/drawio')
        file = source / rel
        if not file.is_file() or file.is_symlink():
            raise RuntimeError('Missing diagrams.net asset: ' + str(rel))
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, dest)
print('Prepared pinned diagrams.net assets.')
