# Error Propagation in Multi-Step Agentic AI Workflows for Research Automation

<!-- BEGIN AITR EXPERIMENTAL STUDY -->
## Experimental Study: HotpotQA Evidence-Context Contamination (n=100)

This section documents the implementation-based follow-up to the literature review below. It investigates whether inserting an unverified, instruction-like annotation into a fixed evidence context changes downstream fact extraction and short-answer synthesis. The study follows **Pathway B (controlled comparative study)** in the AI Tools for Research assignment.

### Research question and workflow

**Question:** Under a fixed model and 100 matched HotpotQA distractor questions, how do clean evidence, injected evidence, a plain-retry prompt, and a Reflexion-*style* feedback prompt compare in exact-match answers and recovery?

Conceptual stages: **query decomposition → fixed dataset evidence (clean/corrupted) → fact extraction → final synthesis**. The project uses the gold HotpotQA contexts, **not a live web/paper retriever**. `src/study.py` inserts one unverified false-answer annotation into a randomly selected document; the original passages are retained. Its synthetic marker is visible in all 100 injected prompts, but none of the output extraction or answer texts copied the marker verbatim. Marker non-copying does not establish that no misinformation was used.

The model-run configuration was **Qwen2.5-7B-Instruct** using the script's 4-bit CUDA loading path and greedy decoding (`do_sample=False`), with a deterministic 100-item validation sample (dataset sampling seed 42). The implementation is **not** an exact reproduction of ReAct or the original Reflexion algorithm.

### Measured results (100 matched questions)

| Condition | Exact-match correct | Exact-match accuracy |
|---|---:|---:|
| Clean | 57/100 | **57%** |
| Injected | 54/100 | **54%** |
| Plain retry | 54/100 | **54%** |
| Reflexion-style feedback | 56/100 | **56%** |

Paired string-based analysis: **6** clean-correct → injected-wrong changes, and **3** clean-wrong → injected-correct changes. Of the six adverse exact-match flips, **0/6** were recovered by plain retry and **1/6** by Reflexion-style feedback. The broader all-injected-wrong denominator yields **0/46** and **2/46**, respectively; these denominators address different questions and must not be interchanged.

The six adverse flips were inspected: three appear to be substantive answer errors, while three appear to be **semantic-equivalence / formatting mismatches** (for example, `2` vs `Mach 2`). These judgments are preliminary and do **not** replace the benchmark's recorded string exact match. The paired bootstrap interval reported for injected minus clean exact match spans **−9 to +3 percentage points**; these results do not demonstrate a statistically reliable accuracy decline.

**Interpretation:** This is an exploratory study of changes under *evidence-context contamination*. It does **not** establish that injected content caused each error, nor does marker-copy frequency estimate the proposed conditional error-propagation coefficient. A stronger causal test requires targeted factual corruption and independently evaluated intermediate-stage errors.

### Reproduce the experiment

From the repository root, using a suitable CUDA GPU environment with access to model weights and the dataset:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/prepare_hotpot.py --n 100 --seed 42 --out data/hotpot_100.jsonl
python scripts/run_experiment.py --data data/hotpot_100.jsonl --out results/hotpot_predictions_100.jsonl
python scripts/evaluate.py --predictions results/hotpot_predictions_100.jsonl --out results/metrics_100.csv
python scripts/plot_results.py --csv results/metrics_100.csv --out results/final_accuracy.png
```

The inference script overwrites the output path: **use a new filename if preserving prior predictions**. The actual runs were performed in Google Colab; runtime packages, model/dataset revisions, and GPU diagnostics should be recorded for strict reproducibility. Free GPU availability is not guaranteed.

### Repository navigation and evidence

- [`src/study.py`](src/study.py) — pipeline, evidence injection, four conditions, extraction and answer traces.
- [`scripts/`](scripts/) — dataset preparation, inference, evaluation, and plotting.
- [`tests/`](tests/) — deterministic checks (not evidence of model accuracy).
- [`configs/`](configs/) — experiment configuration.
- [`results/`](results/) — logged predictions, paired comparison, failure-case audit, tables and plots.
- [`paper/`](paper/) — follow-up paper and LaTeX sources.
- [`research_decisions.md`](research_decisions.md), [`baseline_validation.md`](baseline_validation.md), [`ai_assistance_log.md`](ai_assistance_log.md) — provenance, validation and AI-use documentation.

### Limitations and pending verification

Gold-answer exact match is sensitive to semantically equivalent strings. The experiment uses short-answer HotpotQA rather than scientific-paper synthesis; the proposed ScholarQABench extension has **not** been executed. The recovery prompts add a fresh model run rather than performing full independent fact-checking or reproducing published Reflexion. Verify dataset/model versions, source citations, license obligations, and any publication claims before formal submission. The literature-review resources and historical context are preserved in the original sections below.

<!-- END AITR EXPERIMENTAL STUDY -->

A curated collection of research papers, benchmark datasets, process supervision tools, and open-source implementations focused on cascading failure mitigation, trajectory debugging, and reliability engineering in agentic AI research automation.

---

## Contents
- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Curated Research Papers](#curated-research-papers)
  - [Survey and Review Papers](#survey-and-review-papers)
  - [Foundational Papers](#foundational-papers)
  - [Recent Research Papers](#recent-research-papers)
  - [Methods and Verification Algorithms](#methods-and-verification-algorithms)
  - [Evaluation Benchmarks](#evaluation-benchmarks)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [License](#license)

---

## Overview

Large language models (LLMs) are evolving from passive text generators into autonomous agents capable of planning, information retrieval, tool invocation, and multi-stage reasoning. In scientific research automation, agentic systems perform literature synthesis, hypothesis generation, data analysis, and manuscript drafting. However, multi-step autonomy introduces severe **error propagation (cascading failures)**: errors committed at an early stage can become inputs to downstream tasks, where they are amplified, concealed, or transformed into system-level scientific contamination.

Reliability in agentic research systems is a property of the full trajectory and dependency structure, not simply the base model's capabilities. This repository curates foundational research, process supervision frameworks, step-level verification techniques, and failure recovery mechanisms designed to detect, localize, and contain errors before they degrade downstream scientific conclusions.

---

## AI-Assisted Research Paper

- **Title:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation: Mechanisms, Metrics, Mitigation, and Research Directions
- **Author:** Akash Alaria
- **Document:** [Read Paper PDF](paper/Error_Propagation_in_Multi_Step_Agentic_AI_Workflows_for_Research_Automation.pdf)
- **Abstract Summary:** This paper establishes a formal probabilistic framework for understanding error propagation across agentic research pipelines. It categorizes four distinct propagation channels—semantic, structural, evidential, and operational—and evaluates current mitigations including ReAct closed loops, Self-RAG, process supervision, verifier models, and tree/graph search spaces.

---

## Citation Integrity Audit

- **Audit Status:** 100% Complete (10/10 systematically sampled references audited)
- **Authenticity Score:** 97.5 / 100
- **Document:** [Read Citation Audit PDF](citation-audit/Citation_Integrity_Audit.pdf)
- **Key Findings:** All 10 audited references correspond to genuine, verified scholarly publications on arXiv, ICLR, NeurIPS, or publisher databases. The primary minor integrity issue detected was co-author list truncation (Code B) on large collaborator papers.

---

## Curated Research Papers

### Survey and Review Papers

* **A Survey on Large Language Model Based Autonomous Agents**
  * Zhao et al. (2025), *Frontiers of Computer Science*
  * [DOI: 10.1007/s11704-024-40231-1](https://doi.org/10.1007/s11704-024-40231-1)
  * Comprehensive taxonomy characterizing agentic cognitive cores, planning, memory, and tool integration.

* **Understanding the Planning of LLM Agents: A Survey**
  * Huang et al. (2024), *arXiv preprint*
  * [arXiv:2402.02716](https://arxiv.org/abs/2402.02716)
  * Analyzes task decomposition, plan selection, reflection, and trajectory maintenance in autonomous agents.

* **Retrieval-Augmented Generation for Large Language Models: A Survey**
  * Gao et al. (2023), *arXiv preprint*
  * [arXiv:2312.10997](https://arxiv.org/abs/2312.10997)
  * Outlines RAG paradigms and examines retrieval failure vectors that lead to generative hallucination.

* **A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions**
  * Huang et al. (2025), *ACM Transactions on Information Systems*
  * [DOI: 10.1145/3703155](https://doi.org/10.1145/3703155)
  * Distinguishes retrieval-induced errors from parametric generation errors in complex models.

* **A Survey on Evaluation of LLM-based Agents**
  * Yehudai et al. (2026), *Findings of ACL 2026*
  * [DOI: 10.18653/v1/2026.findings-acl.1330](https://doi.org/10.18653/v1/2026.findings-acl.1330)
  * Identifies methodological gaps in multi-turn robustness, fine-grained verification, and trajectory evaluation.

---

### Foundational Papers

* **Toolformer: Language Models Can Teach Themselves to Use Tools**
  * Schick et al. (2023), *NeurIPS 2023*
  * [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)
  * Demonstrates how language models can self-instruct to invoke external APIs, calculators, and search engines.

* **ReAct: Synergizing Reasoning and Acting in Language Models**
  * Yao et al. (2023), *ICLR 2023*
  * [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
  * Introduces the interleaving of reasoning traces with tool execution to allow environmental feedback to correct plans.

* **Reflexion: Language Agents with Verbal Reinforcement Learning**
  * Shinn et al. (2023), *arXiv preprint*
  * [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
  * Uses linguistic self-reflection memory to enable agent self-correction without weight updating.

* **Training Verifiers to Solve Math Word Problems**
  * Cobbe et al. (2021), *arXiv preprint*
  * [arXiv:2110.14168](https://arxiv.org/abs/2110.14168)
  * Demonstrates that independent verifier models trained to evaluate output correctness outperform direct generation.

---

### Recent Research Papers

* **OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs**
  * Asai et al. (2024), *arXiv preprint*
  * [arXiv:2411.14199](https://doi.org/10.48550/arXiv.2411.14199)
  * Introduces an open retrieval-augmented system designed to answer scientific queries with verifiable citations.

* **Synthesizing Scientific Literature with Retrieval-Augmented Language Models**
  * Asai et al. (2026), *Nature*
  * [DOI: 10.1038/s41586-025-10072-4](https://doi.org/10.1038/s41586-025-10072-4)
  * Validates retrieval-grounded synthesis engines for automated scientific literature review.

* **Where LLM Agents Fail and How They Can Learn From Failures**
  * Zhu et al. (2025), *arXiv preprint*
  * [arXiv:2509.25370](https://arxiv.org/abs/2509.25370)
  * Formulates the AgentError Taxonomy and AgentDebug framework to trace downstream failures to early root causes.

* **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions**
  * Gridach et al. (2025), *ICLR Workshop on AI for Scientific Discovery*
  * Explores agent application across review, hypothesis formation, experimental setup, and automated execution.

---

### Methods and Verification Algorithms

* **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**
  * Asai et al. (2024), *ICLR 2024*
  * [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
  * Incorporates reflection tokens to allow models to adaptively retrieve, evaluate passage relevance, and critique outputs.

* **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
  * Yao et al. (2023), *NeurIPS 2023*
  * [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
  * Extends chain-of-thought to tree structures, enabling deliberate search algorithms (BFS/DFS) and path evaluation.

* **Graph of Thoughts: Solving Elaborate Problems with Large Language Models**
  * Besta et al. (2024), *AAAI 2024*
  * [arXiv:2308.09687](https://arxiv.org/abs/2308.09687)
  * Generalizes execution to arbitrary graphs, supporting aggregation, transformations, and cross-branch feedback.

* **Let's Verify Step by Step**
  * Lightman et al. (2024), *ICLR 2024*
  * [arXiv:2305.20050](https://arxiv.org/abs/2305.20050)
  * Shows that step-level process supervision drastically outperforms final outcome supervision for complex reasoning.

* **AgentPro: Enhancing LLM Agents with Automated Process Supervision**
  * Deng et al. (2025), *EMNLP 2025*
  * [DOI: 10.18653/v1/2025.emnlp-main.506](https://doi.org/10.18653/v1/2025.emnlp-main.506)
  * Uses MCTS and step-level reward models to interrupt faulty reasoning before trajectory corruption.

---

### Evaluation Benchmarks

* **AgentBench: Evaluating LLMs as Agents**
  * Liu et al. (2024), *ICLR 2024*
  * [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)
  * Multi-environment benchmark examining multi-step planning, tool use, and long-horizon failure modes.

* **WebArena: A Realistic Web Environment for Building Autonomous Agents**
  * Zhou et al. (2024), *ICLR 2024*
  * [arXiv:2307.13854](https://arxiv.org/abs/2307.13854)
  * End-to-end web environment highlighting performance drops in extended interactive execution tasks.

* **GAIA: A Benchmark for General AI Assistants**
  * Mialon et al. (2024), *ICLR 2024*
  * [arXiv:2311.12983](https://arxiv.org/abs/2311.12983)
  * Tests complex real-world tasks requiring multimodal reasoning, web browsing, and tool composition.

* **BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents**
  * Wei et al. (2025), *arXiv preprint*
  * [arXiv:2504.12516](https://arxiv.org/abs/2504.12516)
  * Evaluates web browsing agents navigating dynamic, changing information spaces.

---

## Datasets

Detailed descriptions, formats, and repository applications can be found in [`datasets/datasets.md`](datasets/datasets.md).

- **ScholarQABench:** Expert-written scientific QA benchmark for literature synthesis and citation grounding.
- **AgentErrorBench:** Trajectory dataset labeled with memory, planning, action, and reflection failure categories.
- **BrowseComp:** Web browsing dataset for evaluating long-horizon search stability.
- **PRM800K:** 800,000 step-level human feedback annotations for process reward modelling.

---

## Tools and Libraries

Detailed architectural details and usages are available in [`tools/tools.md`](tools/tools.md).

- **ReAct Framework:** Closed-loop architecture interleaving reasoning traces and environment tool calls.
- **SELF-RAG:** Adaptive retrieval and reflection engine using fine-grained critique tokens.
- **OpenScholar:** Scientific paper synthesis engine with provenance-grounded citation generation.
- **Tree-of-Thoughts (ToT):** Tree-based search engine supporting backtracking on error detection.
- **Graph-of-Thoughts (GoT):** Arbitrary graph reasoning unit execution for LLM workflows.
- **Reflexion:** Verbal reinforcement framework providing post-failure reflective memories.

---

## GitHub Implementations

Detailed codebase links and repository descriptions can be found in [`implementations/github-repositories.md`](implementations/github-repositories.md).

- [`princeton-nlp/ReAct`](https://github.com/princeton-nlp/ReAct): Official ReAct execution loop implementation.
- [`AkariAsai/self-rag`](https://github.com/AkariAsai/self-rag): Self-RAG training and critique token generation engine.
- [`princeton-nlp/tree-of-thought-llm`](https://github.com/princeton-nlp/tree-of-thought-llm): ToT search algorithm codebase.
- [`spcl/graph-of-thoughts`](https://github.com/spcl/graph-of-thoughts): Executable Graph-of-Thoughts reasoning engine.
- [`openai/prm800k`](https://github.com/openai/prm800k): Step-level process reward model dataset and evaluation routines.

---

## Tutorials and Learning Resources

1. **Prompt Engineering & Agentic Workflows (DeepLearning.AI):** Foundational instruction on multi-agent execution, planning, and memory architectures.
2. **LangChain & LlamaIndex Production Documentation:** Architectural guides for implementing state verification, fallback chains, and tool routing.
3. **ICLR Tutorials on Autonomous Agent Evaluation:** Lecture series covering multi-turn evaluation, trajectory analysis, and safety guardrails.
4. **OpenAI Guide to Process Supervision:** Technical documentation detailing step-level verifier training versus outcome reward models.
5. **ArXiv Computer Science & Agent Trajectory Auditing:** Literature hub for tracking state-of-the-art developments in multi-step LLM debugging.

---

## License

This repository is released under the terms of the [MIT License](LICENSE).
