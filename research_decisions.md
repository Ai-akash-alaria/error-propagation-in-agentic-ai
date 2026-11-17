# Research Decisions & Literature-to-Experiment Log (`research_decisions.md`)

- **Student Name:** Akash Alaria
- **Roll / Enrollment No.:** MHM2026015
- **Program:** M.Tech (Human-Computer Interaction & IT), IIIT Allahabad
- **Course:** AI Tools for Research (AITR)
- **Paper Title:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation
- **Repository:** `AITR_Lab02_MHM2026015_ErrorPropagation`

---

## 1. Scope Summary of Literature Review

- **Core Focus:** Addresses a major reliability bottleneck in multi-step autonomous AI research agents—how localized mistakes (misread citations, incorrect statistical extractions, or bad tool parameters) compound across sequential stages and lead to cascading system failure.
- **Theoretical Framework:** Probabilistic model capturing step reliability ($r_i$), conditional propagation ($\gamma_{j \to i}$), artifact propagation centrality ($PC(x)$), severity ($s_i$), and recovery probability ($\rho_i$):
  - **Conditional Propagation Coefficient:** $\gamma_{j \to i} = P(E_i \mid E_j) - P(E_i \mid \neg E_j)$
  - **Operational Intervention Formulation (Study B):** $\gamma_{j \to i} = P(E_i = 1 \mid do(Z_j = 1)) - P(E_i = 1 \mid do(Z_j = 0))$
  - **Artifact Propagation Centrality:** $PC(x) = \sum_{y \in Desc(x)} w_{xy} s(y)$
- **Comparative Scope:** Synthesizes error-mitigation strategies across ReAct (2023), Self-RAG, Reflexion (2023), Tree/Graph of Thoughts, Process Reward Models (PRM), AgentPro (EMNLP 2025), AgentDebug / AgentErrorBench (arXiv Sept 2025), and OpenScholar.

---

## 2. Evidence Verification Rules

Every claim, citation, dataset specification, and experimental metric in this repository is tagged using three strict labels:

- **`[VERIFIED]`**: Directly checked against primary paper text, official source repository, or actual code execution logs.
- **`[INFERRED]`**: Analytical conclusion or hypothesis extension derived from literature that requires direct experimental testing.
- **`[UNKNOWN]`**: Unverified citation, model access claim, or external dataset specification requiring manual primary-source inspection before use.

---

## 3. Decision Log

| Decision ID | Workflow Stage | Decision Made | Rationale / Evidence Source | Evidence Tag | Manual Verification / Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEC-01** | Topic Definition | Focus strictly on step-level error propagation trajectories rather than final-answer accuracy alone. | Final-answer accuracy masks intermediate cascading errors and invalid evidence paths (Review Sec. 1 & Sec. 3). | `[VERIFIED]` | Verified against Review Paper Sections 1 & 3. |
| **DEC-02** | Study Pathway | Select **Pathway B (Controlled Comparative Study)** targeting **GAP-1** ($\gamma_{2 \to 3}, \gamma_{2 \to 4}$) with a **GAP-3** recovery comparison ($\rho$) across a 4-stage pipeline (`Query Decomposition -> Evidence Retrieval -> Fact Extraction -> Final Synthesis`). | Enables controlled synthetic error injection at Stage 2 without model fine-tuning while measuring downstream propagation and recovery within a 3–4 week timeline. | `[INFERRED]` | Validate 4-stage pipeline prompts and logging schema in Week 1. |
| **DEC-03** | Dataset Selection | Use **HotpotQA (`distractor` split, $n=100$)** as the primary controlled testbed, **ScholarQABench (`ScholarQA-CS` / single-paper subset, $n=25$)** for research-domain validation, and retain **AgentErrorBench** (200 trajectories) only as an optional detector reference. | HotpotQA (CC BY-SA 4.0) includes paragraph-level supporting facts for automated step scoring; ScholarQABench (ODC-BY aggregate license) grounds claims in scientific literature synthesis. | `[INFERRED]` $\to$ Verify splits | Manually inspect HotpotQA and `AkariAsai/ScholarQABench` schemas, sample splits, and constituent licenses. |
| **DEC-04** | Base Model & Controls | Standardize on **Qwen2.5-7B-Instruct (4-bit quantized, `Q4_K_M`)** at `temperature=0` across four paired conditions: (1) Clean ReAct, (2) Injected ReAct, (3) Injected + Plain Retry, and (4) Injected + Reflexion (max 1 retry). | Fits single-GPU / Colab VRAM (~4.68 GB weights + KV cache) and isolates verbal reflection gains from simple re-sampling under identical model and prompt controls. | `[VERIFIED]` (Model specs) | Verify exact Colab/local GPU VRAM, inference backend, and context window limits before full runs. |
| **DEC-05** | Operational Metrics | Measure $\gamma_{2 \to 3}$, $\gamma_{2 \to 4}$, **injection-uptake rate**, recovery rate $\rho$, step-level accuracy, Answer EM/F1, Supporting Fact F1, error amplification, and token/latency overhead. | Separates whether the agent *accepted* the corrupted Stage-2 artifact from whether it *propagated* it downstream, and quantifies compute trade-offs. | `[INFERRED]` | Freeze exact metric computation scripts and bootstrap CI protocol in Prompt 07. |
| **DEC-06** | Bibliographic Audit | Correct publication years in review notes and `.bib`: **AgentDebug / AgentErrorBench** (Zhu et al.) is an **arXiv Sept 2025** preprint, and **AgentPro** (Deng et al.) is an **EMNLP 2025** paper (both previously cited as 2024). | Primary arXiv and ACL Anthology records confirm 2025 publication dates. | `[VERIFIED]` | Update `paper/references.bib` before drafting manuscript in Prompt 15. |

---

## 4. Evidence-Based Research Gap Matrix (Phase I)

| Gap ID | Research Gap Description | Source Citation & Exact Passage | Gap Type | Proposed Experimental Question | Required Evidence to Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GAP-1** *(Rank 1 — MVP)* | **Standardized Propagation Metrics for Long-Horizon Agent Tasks** | Review Sec. 7.6 & Sec. 8.7: *"Standardized metrics for propagation, recovery, and scientific validity remain underdeveloped."* | `[VERIFIED]` (Reported in Review) | How does injecting controlled intermediate errors at Stage 2 (Evidence Retrieval) alter step-level propagation coefficients ($\gamma_{2 \to 3}, \gamma_{2 \to 4}$) and uptake rates across multi-step trajectories? | Full JSONL trajectory logs, step-by-step artifact states, injection-uptake rates, and empirical $\gamma_{j \to i}$ values with bootstrap CIs. |
| **GAP-2** | **Causal Error Attribution Across Trajectories** | Review Sec. 8.3: *"Future systems should formalize this using causal graphs over trajectories... Interventions on earlier states could then estimate whether changing a particular state would have prevented final failure."* | `[VERIFIED]` (Reported in Review) | Can a counterfactual state-intervention algorithm localize the root cause of cascading failure more accurately than post-hoc LLM evaluators? | Counterfactual state rerun logs, root-cause localization accuracy scores, and causal DAG attribution models. |
| **GAP-3** *(Rank 2 — Extension)* | **State Invalidation & Memory Rollback Mechanisms** | Review Sec. 8.6: *"If a faulty evidence extraction contaminates five subsequent steps... Reliable systems should be able to invalidate downstream states that depend on the corrected artifact."* | `[INFERRED]` (Extrapolated from Recovery Analysis) | Does verbal reflection (Reflexion) or dependency-aware state invalidation achieve higher recovery rates ($\rho$) than plain re-prompting when an early retrieval error is injected? | Comparative recovery rate ($\rho$), post-recovery claim correctness, stale-artifact rate, and token consumption logs. |
| **GAP-4** | **Correlated Errors in Multi-Agent Ensembles** | Review Sec. 7.1: *"Multiple agents may share the same base model, retrieval corpus, prompt templates, or hidden biases. Consequently, majority voting among agents does not necessarily produce independent evidence."* | `[VERIFIED]` (Reported in Review) | To what degree does consensus voting among homogeneous agent ensembles fail to detect systematic evidence extraction errors compared to heterogeneous LLM ensembles? | Error detection accuracy across homogeneous vs. heterogeneous LLM ensembles under identical noisy inputs. |
| **GAP-5** *(Rank 3 — Future)* | **Risk-Adaptive Verification Efficiency** | Review Sec. 8.4: *"High-impact claims—for example, the numerical result driving a meta-analysis or the premise underlying an experimental recommendation—should receive stronger checks than low-impact formatting operations."* | `[INFERRED]` (Extrapolated from Cost Constraints) | Can a verification policy weighted by artifact propagation centrality $PC(x)$ maintain task correctness while reducing overall verification API token overhead? | End-to-end task accuracy, latency metrics, API token counts, and detected error ratios. |

