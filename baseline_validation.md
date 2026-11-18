# Baseline Verification and Validation Report

**Project:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation  
**Course:** AI Tools for Research (AITR)  
**Experiment:** Controlled Evidence-Context Contamination on HotpotQA

## 1. Baseline Objective

The baseline evaluates a four-stage question-answering pipeline under clean, unmodified evidence.

The implemented workflow consists of query decomposition, fixed evidence presentation, fact extraction, and final-answer synthesis.

The baseline is an internal clean-context control, not an exact reproduction of the original ReAct algorithm.

## 2. Dataset and Model

| Parameter | Configuration |
|---|---|
| Dataset | HotpotQA distractor validation subset |
| Evaluation sample | 100 questions |
| Sampling seed | 42 |
| Model | Qwen2.5-7B-Instruct |
| Quantization | 4-bit bitsandbytes NF4 |
| Generation | Greedy decoding (`do_sample=False`) |
| Execution environment | Google Colab with CUDA-based inference |

The exact model revision, dataset revision, and complete package versions have not yet been independently recorded.

## 3. Implementation Verification

The repository contains the following implementation components:

- `src/study.py` — pipeline, model backend, deterministic corruption, and condition execution.
- `scripts/prepare_hotpot.py` — dataset preparation.
- `scripts/run_experiment.py` — experiment execution and logging.
- `scripts/evaluate.py` — accuracy and recovery evaluation.
- `tests/test_study.py` — deterministic software checks.

**Software validation:** Five unit tests passed.

The tests validate selected software behaviors using a mock backend. They do not establish model accuracy or reproduce a published baseline.

## 4. Measured Baseline and Comparators

All four conditions were evaluated on the same 100 question IDs.

| Condition | Exact-Match Correct | Accuracy |
|---|---:|---:|
| Clean | 57/100 | 57% |
| Injected | 54/100 | 54% |
| Plain retry | 54/100 | 54% |
| Reflexion-style feedback | 56/100 | 56% |

The clean-context baseline achieved 57% exact-match accuracy.

The injected-minus-clean difference was −3 percentage points. The reported paired bootstrap interval includes zero, so this study does not establish a statistically reliable decline.

## 5. Injection Verification

The corruption function adds one seeded unverified false-answer annotation to a randomly selected source document while preserving the original evidence.

A reconstruction check confirmed that the inserted marker was within the evidence passed to the model on all 100 evaluated examples.

Literal injection-marker reproduction was 0/100 in extracted facts and 0/100 in final answers.

These measurements do not rule out indirect or paraphrased misinformation.

## 6. Paired Failure and Recovery Analysis

Six examples changed from clean-correct to injected-wrong under strict exact match.

Three examples changed from clean-wrong to injected-correct.

Among the six adverse exact-match transitions:

| Recovery condition | Recovered |
|---|---:|
| Plain retry | 0/6 (0%) |
| Reflexion-style | 1/6 (16.67%) |

Three of the six adverse transitions appear to be substantive factual errors; the other three appear to involve naming or answer-format equivalence. These preliminary classifications have not been independently adjudicated across the entire dataset.

## 7. Limitations and Validation Status

- The clean condition is a working internal baseline, not a reproduction of published ReAct.
- The Reflexion-style condition is a feedback-guided retry, not the complete original Reflexion algorithm.
- Supporting-fact F1 and the proposed conditional propagation coefficient were not measured.
- Exact-match scoring can penalize semantically equivalent answers.
- The model and dataset revision identifiers require verification.
- The ScholarQABench extension has not been executed.

**Validation status:** The software tests, completed 100-question run, saved predictions, and recorded exact-match measurements are supported by experiment artifacts. Independent published-method reproduction and formal causal propagation validation remain incomplete.

## 8. Evidence Files

- `results/hotpot_predictions_100.jsonl`
- `results/hotpot_predictions_100.meta.json`
- `results/metrics_100.csv`
- `results/metrics_100.summary.json`
- `results/paired_analysis.csv`
- `results/failure_cases.json`
- `results/failure_analysis.csv`
- `results/test_log.txt`

The experimental manuscript and its methods are in `paper/main.pdf` and `paper/main.tex`.
