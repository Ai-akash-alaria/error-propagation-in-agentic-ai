# G2/G3 — Recorded environment and run manifest

The following values come from the uploaded original run metadata, code and results, **not** a new reconstruction of the former Colab environment.

| Property | Recorded value |
|---|---|
| Model | `Qwen/Qwen2.5-7B-Instruct` |
| Quantization | `quantized_4bit: true`, implemented with bitsandbytes NF4 |
| Dataset | `hotpotqa/hotpot_qa` / `distractor` / `validation`; 100 sampled items |
| Sampling/perturbation seed | 42 (perturbation seed advances by item index) |
| Model decoding | `do_sample=False`; `max_new_tokens=96` per LLM call |
| Python | 3.13.16 (as metadata records) |
| Host | Linux x86_64 (see full `.meta.json`) |
| Wall clock | 3031.25 seconds for 100 matched cases (four methods each) |
| GPU type, CUDA driver/version, free memory | **NOT RECORDED**; do not claim T4 merely from earlier availability discussions |
| Exact `torch`, `transformers`, `datasets`, `bitsandbytes` versions | **NOT RECORDED** |
| Model & dataset exact revision hashes | **NOT RECORDED** |
| Source of scores | `results/hotpot_predictions_100.jsonl` and `results/metrics_100.csv` |

## Commands actually consistent with checked scripts

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/prepare_hotpot.py --n 100 --seed 42 --out data/hotpot_100.jsonl
python scripts/run_experiment.py --data data/hotpot_100.jsonl --out results/hotpot_predictions_100.jsonl
python scripts/evaluate.py --predictions results/hotpot_predictions_100.jsonl --out results/metrics_100.csv
python scripts/plot_results.py --csv results/metrics_100.csv --out results/final_accuracy.png
```

**Important:** `plot_results.py` imports `matplotlib`; the previous `requirements.txt` lacked it. The accompanying patch adds a declared Matplotlib dependency without pretending a complete version-locked environment has been tested. Original inference used an existing Colab image; these commands are reproduction instructions, not claims they were freshly executed in that exact sequence under all future packages.

## Regeneration and provenance limits

- `run_experiment.py` overwrites the named output file on rerun. Preserve uploaded predictions before any new experiment.
- Pre-run config has status `PROPOSED_NOT_PREREGISTERED`. No post-hoc config edit makes the experiment preregistered.
- The original dataset `data/hotpot_100.jsonl` was not included in archived project due to distribution/storage conventions; regeneration uses a revision-unpinned public dataset. Exact sample IDs in predictions should be checked against regenerated data before claiming bitwise reproduction.
- Do not compare absolute speed numbers across different GPUs; don't interpret prompt-length differences as efficiency superiority.
- If the original Colab notebook retains `pip freeze`, model/dataset cache revision hashes or `nvidia-smi` output, attach it as separate original evidence. Otherwise say **not recorded**.
