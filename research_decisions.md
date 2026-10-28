# Research Workspace Setup & Decision Log (Phase I)

**Student Name:** Akash Alaria  
**Roll / Enrollment No.:** MHM2026015  
**Program:** M.Tech (Human-Computer Interaction & IT), IIIT Allahabad  
**Course:** AI Tools for Research (AITR)  
**Date:** October 22, 2026  
**Paper Title:** *Error Propagation in Multi-Step Agentic AI Workflows for Research Automation*  

---

## 1. Research Workspace Setup & Scope Summary

### 1.1 Scope Summary of Literature Review
- **Core Focus:** Addressing a major reliability bottleneck in multi-step autonomous AI research agents: how localized mistakes (misread citations, incorrect statistical extractions, or bad tool parameters) compound across sequential stages and lead to cascading system failure.
- **Theoretical Framework:** Probabilistic modeling of step reliability ($r_i$), conditional propagation ($\gamma_{j\to i}$), artifact propagation centrality ($PC(x)$), severity ($s_i$), and recovery probability ($\rho_i$):
  - Conditional Propagation Coefficient: $\gamma_{j\to i} = P(E_i \mid E_j) - P(E_i \mid \neg E_j)$
  - Artifact Propagation Centrality: $PC(x) = \sum_{j \in D(x)} w_j$
- **Comparative Scope:** Synthesizes error-mitigation strategies across existing agent architectures including ReAct, Self-RAG, Reflexion, Tree/Graph of Thoughts, Process Reward Models (PRM), AgentPro, AgentDebug, and OpenScholar.

### 1.2 Evidence Verification Rules
To ensure rigor throughout this project, three evidence labels are enforced across all notes, logs, and claims:
- **`[VERIFIED]`:** Directly checked against primary paper text, official source code, or actual execution outputs.
- **`[INFERRED]`:** Analytical conclusions or hypothesis extensions derived from literature that require direct experimental testing.
- **`[UNKNOWN]`:** Unverified citations, model access claims, or external dataset specifications needing manual primary source verification.

### 1.3 Decision Log

| Decision ID | Workflow Stage | Decision Made | Rationale / Evidence Source | Evidence Tag | Manual Verification / Action Required |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEC-01** | Topic Definition | Focus strictly on error propagation trajectories rather than final answer accuracy. | Final-answer accuracy masks cascading errors and invalid evidence paths. | `[VERIFIED]` | Checked against Section 1 & Section 3 of review paper. |
| **DEC-02** | Study Pathway | Select Pathway B (Controlled Comparative Study) / Pathway C (Targeted Modification). | Allows isolated testing of state invalidation/rollback vs. linear re-prompting under controlled error injection. | `[INFERRED]` | Evaluated compute trade-offs on local GPU resources. |
| **DEC-03** | Dataset Selection | Target ScholarQABench / AgentErrorBench trajectory subsets. | Provides scientific QA ground-truth alongside documented agent failure taxonomies. | `[UNKNOWN]` | Inspected repository access and data split availability manually. |

---

## 2. Evidence-Based Research Gap Matrix

| Gap ID | Research Gap Description | Source Citation & Exact Passage from Review | Gap Type | Proposed Experimental Research Question | Required Evidence to Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GAP-1** | Standardized Propagation Metrics for Long-Horizon Agent Tasks | **Section 7.6 & 8.7:** *"Standardized metrics for propagation, recovery, and scientific validity remain underdeveloped."* | `[VERIFIED]` (Reported in Review) | How does injecting controlled intermediate errors (e.g., corrupted metadata or tool output failures) alter step-level propagation coefficients across multi-step research trajectories? | Full execution logs, step-by-step state matrices, and empirical calculation of propagation coefficients ($\gamma_{j\to i}$). |
| **GAP-2** | Causal Error Attribution Across Trajectories | **Section 8.3:** *"Future systems should formalize this using causal graphs over trajectories... Interventions on earlier states could then estimate whether changing a particular state would have prevented final failure."* | `[VERIFIED]` (Reported in Review) | Can a counterfactual state-intervention algorithm localize the root cause of cascading failure in an agent trajectory more accurately than post-hoc LLM evaluators? | Counterfactual state rerun logs, root-cause localization accuracy scores, and causal DAG attribution models. |
| **GAP-3** | State Invalidation & Memory Rollback Mechanisms | **Section 8.6:** *"If a faulty evidence extraction contaminates five subsequent steps... Reliable systems should be able to invalidate downstream states that depend on the corrected artifact."* | `[INFERRED]` (Extrapolated from Recovery Analysis) | Does a provenance-aware memory system with automatic dependency-graph rollback achieve higher recovery rates ($\rho_i$) than linear re-prompting or Reflexion when an early extraction error is corrected? | Comparative recovery rate ($\rho_i$), post-recovery claim correctness, and token consumption logs. |
| **GAP-4** | Correlated Errors in Multi-Agent Ensembles | **Section 7.1:** *"Multiple agents may share the same base model, retrieval corpus, prompt templates, or hidden biases. Consequently, majority voting among agents does not necessarily produce independent evidence."* | `[VERIFIED]` (Reported in Review) | To what degree does consensus voting among homogeneous agent ensembles fail to detect systematic evidence extraction errors compared to heterogeneous LLM ensembles? | Error detection accuracy across homogeneous vs. heterogeneous LLM ensembles under identical noisy inputs. |
| **GAP-5** | Risk-Adaptive Verification Efficiency | **Section 8.4:** *"High-impact claims—for example, the numerical result driving a meta-analysis or the premise underlying an experimental recommendation—should receive stronger checks than low-impact formatting operations."* | `[INFERRED]` (Extrapolated from Cost Constraints) | Can a verification policy weighted by artifact propagation centrality ($PC(x)$) maintain task correctness while reducing overall verification API token overhead? | End-to-end task accuracy, latency metrics, API token counts, and detected error ratios. |

---

## 3. Gap Ranking & Feasibility Analysis (Top 3)

### Priority Order
1. **GAP-1:** Standardized Error Propagation Measurement & Benchmark Protocol (`[VERIFIED]`)
2. **GAP-3:** Provenance-Aware State Invalidation & Dependency Memory Rollback (`[INFERRED]`)
3. **GAP-5:** Risk-Adaptive Verification Policy using Artifact Propagation Centrality (`[INFERRED]`)

### Justification & Resource Plan

#### 1. Rank 1: GAP-1 (Controlled Error Injection & Propagation Benchmarking)
- **Scientific Focus:** Addresses the core thesis of my review—that standard benchmarks evaluate end-to-end accuracy while ignoring step-level error compounding.
- **Execution Strategy:** Implement an open-source agent pipeline (built with custom async loop / ReAct) and programmatically inject synthetic perturbations (altered extraction values or missing citations) into intermediate outputs to observe downstream propagation.
- **Resource Feasibility:** Fully feasible using Google Colab / local GPU resources and open-weights models (Llama-3-8B / Qwen-2.5-7B). API costs remain minimal because perturbations are injected directly into state variables.
- **Fallback Plan:** Restrict the experimental scope to a 3-stage modular pipeline (Search $\to$ Extraction $\to$ Synthesis) with script-level intermediate checks.

#### 2. Rank 2: GAP-3 (Provenance-Aware State Invalidation & Dependency Rollback)
- **Scientific Focus:** Solves the recovery problem ($\rho_i$) by testing active state containment instead of passive error logging.
- **Execution Strategy:** Build a Directed Acyclic Graph (DAG) state tracker in Python (using NetworkX) where each generated node stores its parent dependency IDs ($M = (c, e, s, t, q)$).
- **Resource Feasibility:** Low computational footprint. Focus is on memory data structures and execution control logic rather than heavy model inference.
- **Fallback Plan:** Test a 2-step localized stack rollback mechanism rather than a full multi-branch dependency graph.

#### 3. Rank 3: GAP-5 (Risk-Adaptive Verification Policy via Propagation Centrality)
- **Scientific Focus:** Directly tackles the trade-off between expensive step-by-step process supervision and system reliability.
- **Execution Strategy:** Implement a gating function based on the propagation centrality formula $PC(x) = \sum_{j \in D(x)} w_j$, verifying only intermediate outputs whose downstream dependency weight exceeds a pre-set threshold.
- **Resource Feasibility:** Directly measurable through API token usage and runtime latency logs.
- **Fallback Plan:** Substitute dynamic dependency tracking with static node weighting (high weight for numerical extractions, low weight for text formatting).
