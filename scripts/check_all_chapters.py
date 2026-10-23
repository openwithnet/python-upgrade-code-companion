"""Resumable, chapter-isolated test runner for the Python Upgrade candidate.

Usage:
  python scripts/check_all_chapters.py --chapters 2,3,10
  python scripts/check_all_chapters.py --resume
  python scripts/check_all_chapters.py --retry-failed
  python scripts/check_all_chapters.py --reset

A passed check is reused only when its command, source tree fingerprint and
Python interpreter match. No source/test files are modified.
"""
from pathlib import Path
import argparse, hashlib, json, os, subprocess, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT/'docs'/'ALL_CHAPTER_TEST_STATE.json'
REPORT = ROOT/'docs'/'ALL_CHAPTER_TEST_RESULTS.json'

def jobs():
    result=[]
    for ch in range(1,18):
        root=ROOT/'chapters'/f'chapter{ch:02}'
        if ch==1:
            for f in sorted((root/'sections').glob('*.py')):
                result.append((ch,f.stem,[sys.executable,str(f)],f.parent,()))
        elif ch<=10:
            config={
                2: ('', ['test_ch02.py'],False),3:('', ['test_P1.py'],False),
                4:('', ['test_b1_dna_analysis.py'],True),5:('python_upgrade_ch05',['tests/test_c2.py'],True),
                6:('', ['test_p1.py'],True),7:('', ['test_b1_sequences.py'],True),
                8:('Chapter_08',['test_c3_calibration.py'],True),
                9:('', ['test_c3_pytest.py','test_c3_validation.py','test_ch09_additional.py'],True),
                10:('ch10_alignment_QA',['verified_suite','test_ch10_composition_example.py'],True)}
            sub,targets,pytest=config[ch]
            cwd=root/'original_package'/sub
            cmd=[sys.executable,'-m','pytest','-q',*(['--import-mode=importlib'] if ch==10 else []),*targets] if pytest else [sys.executable,targets[0]]
            result.append((ch,'original',cmd,cwd,()))
        elif ch==11:
            result.append((ch,'original',[sys.executable,'-m','pytest','-q','test_ch11_lab.py'],root,()))
        else:
            result.append((ch,'candidate',[sys.executable,'-m','pytest','-q','--import-mode=importlib','tests'],root,()))
    return result

def fingerprint(cwd):
    h=hashlib.sha256()
    for p in sorted(cwd.rglob('*.py')):
        if any(x in ('__pycache__','.pytest_cache','.git') for x in p.parts):continue
        h.update(str(p.relative_to(cwd)).encode()); h.update(p.read_bytes())
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--chapters',help='Comma-separated chapter numbers; default all')
    mode=ap.add_mutually_exclusive_group()
    mode.add_argument('--resume',action='store_true',help='Reuse previously passing jobs with matching source fingerprint')
    mode.add_argument('--retry-failed',action='store_true',help='Run missing and nonpassing jobs only')
    mode.add_argument('--reset',action='store_true',help='Discard previous run records')
    ap.add_argument('--timeout',type=int,default=120)
    a=ap.parse_args(); STATE.parent.mkdir(exist_ok=True)
    state={} if a.reset or not STATE.exists() else json.loads(STATE.read_text(encoding='utf-8'))
    selected=set(map(int,a.chapters.split(','))) if a.chapters else set(range(1,18))
    results=[]
    for ch,label,cmd,cwd,extra in jobs():
        if ch not in selected:continue
        key=f'{ch:02}/{label}'
        if not cwd.exists():
            record={'chapter':ch,'label':label,'status':'MISSING','reason':str(cwd)}
        else:
            fp=fingerprint(cwd)
            signature=hashlib.sha256(json.dumps([cmd,fp,sys.version,sys.executable],ensure_ascii=False).encode()).hexdigest()
            prev=state.get(key)
            skip=bool(prev and prev.get('signature')==signature and ((a.resume and prev['status']=='PASS') or (a.retry_failed and prev['status']=='PASS')))
            if skip:
                record={**prev,'reused':True}
            else:
                env=os.environ.copy()
                env['PYTHONPATH']=os.pathsep.join([str(cwd),str(cwd/'src'),str(cwd/'verified_suite'),*map(str,extra),env.get('PYTHONPATH','')])
                try:
                    p=subprocess.run(cmd,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=a.timeout)
                    status='PASS' if p.returncode==0 else 'FAIL'; tail=p.stdout[-4000:]
                except subprocess.TimeoutExpired as e:
                    status='TIMEOUT';tail=str(e)
                record={'chapter':ch,'label':label,'status':status,'signature':signature,'command':cmd,'output_tail':tail,'timestamp_utc':datetime.now(timezone.utc).isoformat(),'reused':False}
        state[key]=record; results.append(record)
        STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
        print(f'Chapter {ch:02} {label}: {record["status"]}'+(' [reused]' if record.get('reused') else ''),flush=True)
    REPORT.write_text(json.dumps({'timestamp_utc':datetime.now(timezone.utc).isoformat(),'results':results},ensure_ascii=False,indent=2),encoding='utf-8')
    count=sum(x['status']=='PASS' for x in results)
    print(f'CHECKS {len(results)} PASS {count} FAIL {len(results)-count}; cached state: {STATE}')
    return 0 if count==len(results) else 1
if __name__=='__main__':sys.exit(main())
