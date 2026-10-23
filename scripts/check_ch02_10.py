"""Isolated tests for original Chapter 02–10 packages. Does not modify source."""
from pathlib import Path
import os, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
CONFIG={
2: ('', ['test_ch02.py'],False),3:('', ['test_P1.py'],False),
4:('', ['test_b1_dna_analysis.py'],True),5:('python_upgrade_ch05',['tests/test_c2.py'],True),
6:('', ['test_p1.py'],True),7:('', ['test_b1_sequences.py'],True),
8:('Chapter_08',['test_c3_calibration.py'],True),
9:('', ['test_c3_pytest.py','test_c3_validation.py','test_ch09_additional.py'],True),
10:('ch10_alignment_QA',['verified_suite','test_ch10_composition_example.py'],True)}
for n,(sub,targets,pytest) in CONFIG.items():
    cwd=ROOT/'chapters'/f'chapter{n:02}'/'original_package'/sub
    cmd=[sys.executable,'-m','pytest','-q',*(['--import-mode=importlib'] if n==10 else []),*targets] if pytest else [sys.executable,targets[0]]
    env={**os.environ,'PYTHONPATH':os.pathsep.join([str(cwd),str(cwd/'verified_suite'),os.environ.get('PYTHONPATH','')])}
    print(f'Chapter {n:02}:', ' '.join(cmd),flush=True)
    rc=subprocess.run(cmd,cwd=cwd,env=env).returncode
    if rc: raise SystemExit(f'Chapter {n:02} FAIL: exit {rc}')
print('Chapter 02–10 isolated checks passed')
