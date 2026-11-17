import argparse,csv,json,random
from collections import defaultdict
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--predictions',required=True);p.add_argument('--out',default='results/metrics.csv');a=p.parse_args()
raw=[json.loads(s) for s in Path(a.predictions).read_text().splitlines() if s.strip()]
if not raw: raise ValueError('Empty prediction file')
ids=[r['id'] for r in raw]
if len(ids)!=len(set(ids)): raise ValueError('Duplicate IDs')
methods=['clean','injected','plain_retry','reflexion_style']
for r in raw:
 if not all(k in r['conditions'] for k in methods):raise ValueError('Missing comparator')
 if any('answer' not in r['conditions'][k] or 'em' not in r['conditions'][k] for k in methods):raise ValueError('Missing prediction/metric')
metrics=[]
for m in methods:
 xs=[r['conditions'][m] for r in raw]
 metrics.append({'method':m,'n':len(xs),'exact_match':sum(x['em'] for x in xs)/len(xs),
  'injected_marker_in_extraction':sum(x['marker_in_extraction'] for x in xs)/len(xs),
  'injected_marker_in_answer':sum(x['marker_in_answer'] for x in xs)/len(xs),
  'mean_seconds':sum(x['seconds'] for x in xs)/len(xs),
  'mean_input_tokens':sum(x.get('input_tokens',0) for x in xs)/len(xs),
  'mean_output_tokens':sum(x.get('output_tokens',0) for x in xs)/len(xs)})
# Paired difference estimates refer to same IDs; no p-values or unjustified significance claims.
for x in metrics: x['delta_em_vs_injected']=x['exact_match']-metrics[1]['exact_match']
out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=metrics[0].keys());w.writeheader();w.writerows(metrics)
print('Wrote',out)
for x in metrics:print(x)
# Properly identify conditional error differences; zero denominators are undefined.
by_condition=defaultdict(list)
for r in raw:
 for m in methods:by_condition[m].append(r['conditions'][m])
pinj=1-metrics[1]['exact_match'];pclean=1-metrics[0]['exact_match']
summary={'n':len(raw),'injection_effect_error_probability':pinj-pclean,
 'recovery_plain_given_injected_wrong':None,'recovery_reflexion_given_injected_wrong':None}
failed=[r for r in raw if not r['conditions']['injected']['em']]
if failed:
 for name,key in [('plain','plain_retry'),('reflexion','reflexion_style')]:
  summary['recovery_'+name+'_given_injected_wrong']=sum(r['conditions'][key]['em'] for r in failed)/len(failed)
# Paired bootstrap of per-item differences using one index sample shared across conditions.
rng=random.Random(42)
for name,m in [('injection_vs_clean', 'injected'),('reflection_vs_retry','reflexion_style')]:
 comparator='clean' if name=='injection_vs_clean' else 'plain_retry'
 diffs=[r['conditions'][m]['em']-r['conditions'][comparator]['em'] for r in raw]
 estimates=[]
 for _ in range(2000):
  estimates.append(sum(diffs[rng.randrange(len(diffs))] for __ in range(len(diffs)))/len(diffs))
 estimates.sort()
 summary[name+'_paired_difference']=sum(diffs)/len(diffs)
 summary[name+'_bootstrap_95pct']=[estimates[50], estimates[1949]]
summary_path=out.with_suffix('.summary.json');summary_path.write_text(json.dumps(summary,indent=2))
print('Wrote',summary_path)
