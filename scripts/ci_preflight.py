"""Offline CI preflight: validate chapter jobs and dependency/config references.

This is *not* a substitute for a Python 3.11 or GitHub-hosted runtime test.
"""
from pathlib import Path
import ast
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    failures = []
    workflow = ROOT / '.github/workflows/chapter-tests.yml'
    content = workflow.read_text(encoding='utf-8')
    for item in ('actions/checkout@', 'actions/setup-python@', 'python-version: "3.11"',
                 'scripts/check_all_chapters.py', 'requirements/base.txt', 'requirements/ch15.txt'):
        if item not in content:
            failures.append(f'Workflow missing reference: {item}')
    if not re.search(r'chapter:\s*\[\s*1\s*,.*?17\s*\]', content, re.S):
        failures.append('Workflow chapter matrix does not contain expected endpoints')
    # Verify exact matrix numbers rather than relying solely on endpoints.
    matrix = re.search(r'chapter:\s*\[([^\]]+)\]', content)
    if not matrix or [int(x.strip()) for x in matrix.group(1).split(',')] != list(range(1, 18)):
        failures.append('Workflow chapter matrix must be 1..17 exactly')
    for rel in ['requirements/base.txt','requirements/ch15.txt',
                'environments/windows-cpu.yml','scripts/check_all_chapters.py']:
        if not (ROOT / rel).is_file():
            failures.append(f'Missing CI input: {rel}')
    sys.path.insert(0, str(ROOT / 'scripts'))
    from check_all_chapters import jobs
    by_chapter = {ch: [] for ch in range(1,18)}
    for chapter, label, command, cwd, _ in jobs():
        by_chapter[chapter].append((label, command, cwd))
        if not cwd.is_dir():
            failures.append(f'Chapter {chapter:02} {label}: working directory missing: {cwd}')
        if command[0] != sys.executable:
            failures.append(f'Chapter {chapter:02}: interpreter path inconsistent')
        if command[1:3] == ['-m','pytest']:
            targets = [v for v in command[3:] if not v.startswith('-')]
        else:
            targets = command[1:]
        for target in targets:
            if not (cwd / target).exists() and not Path(target).exists():
                failures.append(f'Chapter {chapter:02} {label}: target missing: {target}')
    for chapter, tasks in by_chapter.items():
        if not tasks:
            failures.append(f'Chapter {chapter:02}: no test jobs defined')
    if not (ROOT / 'LICENSE').exists():
        failures.append('Missing LICENSE')
    for p in (ROOT / 'scripts').glob('*.py'):
        try:
            ast.parse(p.read_text(encoding='utf-8'), filename=str(p), feature_version=(3,11))
        except SyntaxError as exc:
            failures.append(f'Python 3.11 syntax incompatible: {p}: {exc}')
    print(f'CI PREFLIGHT: chapters={len(by_chapter)}, jobs={sum(map(len,by_chapter.values()))}, errors={len(failures)}')
    for failure in failures:
        print('ERROR:', failure)
    return 1 if failures else 0

if __name__ == '__main__':
    raise SystemExit(main())
