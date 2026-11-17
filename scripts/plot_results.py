"""Plot ONLY genuine evaluation CSV. No synthetic example measurements."""
import argparse,csv
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--csv',default='results/metrics.csv');p.add_argument('--out',default='results/condition_em.png');a=p.parse_args()
import matplotlib.pyplot as plt
with Path(a.csv).open() as f:rows=list(csv.DictReader(f))
if not rows:raise ValueError('No measured CSV values')
fig,ax=plt.subplots(figsize=(8,4));ax.bar([r['method'] for r in rows],[float(r['exact_match']) for r in rows]);ax.set_ylabel('Exact-match accuracy');ax.set_ylim(0,1);ax.tick_params(axis='x',rotation=20);fig.tight_layout();Path(a.out).parent.mkdir(exist_ok=True,parents=True);fig.savefig(a.out,dpi=180);print(a.out)
