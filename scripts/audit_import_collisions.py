"""Inventory duplicate module basenames across chapters; no source modification."""
from pathlib import Path
from collections import defaultdict
import csv
ROOT=Path(__file__).resolve().parents[1]
idx=defaultdict(list)
for p in (ROOT/'chapters').rglob('*.py'):
    if any(x in p.parts for x in ('__pycache__','.pytest_cache')):continue
    idx[p.stem].append(str(p.relative_to(ROOT)))
rows=[]
for name,paths in sorted(idx.items()):
    chapters={p.split('/')[1] for p in paths}
    if len(chapters)>1:
        rows.append({'module_name':name,'chapter_count':len(chapters),'file_count':len(paths),'paths':' | '.join(paths),'risk':'test or import collision if sys.path is shared'})
out=ROOT/'docs'/'CROSS_CHAPTER_IMPORT_COLLISIONS.csv'
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['module_name','chapter_count','file_count','paths','risk']);w.writeheader();w.writerows(rows)
print('Cross-chapter duplicate module basenames:',len(rows));print('Examples:',[(x['module_name'],x['chapter_count']) for x in rows[:15]])
