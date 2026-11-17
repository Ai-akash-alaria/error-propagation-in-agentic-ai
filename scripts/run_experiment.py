import argparse,json,platform,time,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.study import run_item,validate_item,TransformersBackend
p=argparse.ArgumentParser();p.add_argument('--data',default='data/hotpot_100.jsonl');p.add_argument('--out',default='results/hotpot_predictions.jsonl');p.add_argument('--model',default='Qwen/Qwen2.5-7B-Instruct');p.add_argument('--seed',type=int,default=42);p.add_argument('--limit',type=int,default=None);p.add_argument('--no-4bit',action='store_true');a=p.parse_args()
items=[validate_item(json.loads(s)) for s in Path(a.data).read_text().splitlines() if s.strip()]
if a.limit is not None: items=items[:a.limit]
if not items: raise ValueError('No input items')
if len(set(x['id'] for x in items))!=len(items): raise ValueError('Duplicate IDs')
b=TransformersBackend(a.model,not a.no_4bit)
out=Path(a.out);out.parent.mkdir(exist_ok=True,parents=True)
start=time.time()
with out.open('w') as f:
 for i,x in enumerate(items):
  result=run_item(x,b,a.seed+i)
  f.write(json.dumps(result,ensure_ascii=False)+'\n');f.flush()
  print(i+1,'/',len(items),'id',x['id'])
meta={'source':a.data,'model':a.model,'seed':a.seed,'n':len(items),'quantized_4bit':not a.no_4bit,
      'system':platform.platform(),'python':sys.version,'elapsed_s':round(time.time()-start,2),
      'prompt_style':'controlled fixed budget 4 conditions; Reflexion-inspired single feedback pass; not original Reflexion reproduction'}
out.with_suffix('.meta.json').write_text(json.dumps(meta,indent=2))
print('Saved',out)
