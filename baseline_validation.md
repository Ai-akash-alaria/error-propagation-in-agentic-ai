

---

## Post-execution validation addendum (preserves earlier pre-run entry)

The earlier “NOT RUN” statements above describe the **pre-execution state**, not the current study. Actual student Colab outputs and archived result files now document the completed run.

| Check | Result | Evidence |
|---|---|---|
| Software unit tests | 5 passed in the supplied build environment | `results/test_log.txt`; `tests/test_study.py` |
| Dataset/sample | HotpotQA `distractor` **validation**, 100 unique matched IDs, sampling seed 42 | `scripts/prepare_hotpot.py`, 100 result rows, item IDs |
| Model | Qwen/Qwen2.5-7B-Instruct, 4-bit NF4 code path | `src/study.py`; 100-run `.meta.json` says `quantized_4bit: true` |
| Clean-context internal baseline | 57/100 exact match | `results/metrics_100.csv` |
| Injected context | 54/100 exact match | same metrics file |
| Plain retry / Reflexion-style | 54/100 / 56/100 exact match | same metrics file |
| Paired changes | 6 adverse exact-match flips, 3 reverse flips | `results/paired_analysis.csv`, archived predictions |
| Recovery on six adverse flips | 0/6 retry; 1/6 Reflexion-style | archived predictions; `results/failure_cases.json` |
| False-answer marker visibility | 100/100 marker visible in first 14,000 characters | Student-reported Colab reconstruction using actual input rows and seeds |
| Literal marker copied to extraction / answer | 0/100 in all methods | `results/metrics_100.csv` |
| Inference runtime | 3031.25 seconds total wall clock as archived | `results/hotpot_predictions_100.meta.json` |
| Paired bootstrap | injected-clean −0.03, 95% percentile interval [−0.09,+0.03] | `results/metrics_100.summary.json`, 2000 resamples |

**Nature of baseline.** This is an **internal clean-context control**, *not* an independent reproduction of ReAct, Reflexion or any published paper's baseline. The five unit tests use a MockBackend and do not prove LLM correctness. End-to-end recorded execution is distinct from independent reproduction of the original Colab run.

**Prompt/measurement limitations.** Clean, injected and feedback methods use matched question IDs but different evidence/prompts; feedback includes an explicit poisoning warning; fixed generation order and exact-match string normalization may confound interpretation. At least three of six adverse exact-match flips look like potentially correct answer aliases, requiring blinded adjudication before any factual-error claim. Stage-error probability coefficient γ cannot be computed without independently validated intermediate truth labels.

**Open verification:** exact GPU type, original `pip freeze`, model/dataset commit IDs, independent paper references, reproduction by a second person, and ScholarQABench domain test. These were **not** backfilled from a later runtime.
