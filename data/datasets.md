# Datasets and Benchmark Suites

Curated collection of evaluation benchmarks, trajectory datasets, and trace collections used to audit, evaluate, and benchmark error propagation, long-horizon reliability, and literature synthesis in agentic AI workflows.

---

## 1. Primary Evaluation Datasets & Benchmarks

### 1. ScholarQABench
* **Source:** OpenScholar Project / Semantic Scholar
* **Access Link:** [ScholarQABench Repository / Paper](https://arxiv.org/abs/2411.14199)
* **Format:** Multi-domain expert scientific questions with citation-grounded answers
* **Description:** A benchmark designed to evaluate multi-step scientific literature retrieval, synthesis quality, and citation correctness across diverse scientific fields.
* **Application in Project:** Used to benchmark baseline literature retrieval completeness and detect evidential error propagation during scientific synthesis.

### 2. AgentErrorBench / AgentError Trajectories
* **Source:** AgentDebug Project
* **Access Link:** [arXiv:2509.25370](https://arxiv.org/abs/2509.25370)
* **Format:** Labeled agent execution traces (`.jsonl`)
* **Description:** A detailed trajectory benchmark containing step-level annotations across memory, reflection, planning, and tool execution failures.
* **Application in Project:** Provides ground-truth failure sequences for testing root-cause localization algorithms and error propagation metrics.

### 3. BrowseComp Benchmark
* **Source:** OpenAI / Independent Research Alignment
* **Access Link:** [arXiv:2504.12516](https://arxiv.org/abs/2504.12516)
* **Format:** Interactive web browsing task suite
* **Description:** A challenging evaluation benchmark designed for web-browsing agents operating across dynamic, large-scale online environments.
* **Application in Project:** Tests agent resilience against operational failures, missing sources, and dynamic web page variations during long-horizon search.

### 4. PRM800K (Process Reward Model Dataset)
* **Source:** OpenAI
* **Access Link:** [GitHub - openai/prm800k](https://github.com/openai/prm800k)
* **Format:** 800,000 step-level human feedback annotations
* **Description:** Step-by-step process supervision annotations designed to train verifier models to identify intermediate reasoning errors before final completion.
* **Application in Project:** Serves as the foundational dataset format for building step-level process supervision verifiers in multi-step workflows.

---

## 2. Summary Comparison

| Benchmark / Dataset | Primary Task Domain | Target Failure Mode | Size / Scale |
|---|---|---|---|
| **ScholarQABench** | Literature Synthesis & Citation | Retrieval failure & Hallucinated synthesis | Expert multi-domain QA |
| **AgentErrorBench** | Multi-step Agent Execution | Cascading planning & memory errors | Multi-environment traces |
| **BrowseComp** | Autonomous Web Browsing | Navigation loops & obsolete data | Dynamic environment tasks |
| **PRM800K** | Step-level Verification | Reasoning step degradation | 800K step labels |
```[cite: 1, 2]

---
