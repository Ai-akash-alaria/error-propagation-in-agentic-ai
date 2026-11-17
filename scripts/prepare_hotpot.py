import argparse,json,random
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=100);p.add_argument('--seed',type=int,default=42);p.add_argument('--out',default='data/hotpot_100.jsonl');a=p.parse_args()
from datasets import load_dataset
rows=load_dataset('hotpotqa/hotpot_qa','distractor',split='validation')
indices=random.Random(a.seed).sample(range(len(rows)),a.n)
out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w') as f:
 for i in indices:
  x=rows[i]
  f.write(json.dumps({k:x[k] for k in ('id','question','answer','context')},ensure_ascii=False)+'\n')
print('Wrote',len(indices),'rows to',out,'seed',a.seed)
