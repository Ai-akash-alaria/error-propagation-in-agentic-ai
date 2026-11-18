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

---

## Experimental decision outcomes and audit addendum

*The existing DEC-01–DEC-06 entries and original dates remain historical planning records. This section distinguishes the executed study from the earlier plan. Evidence labels refer to the listed artifacts, not to independent replication.*

| ID | Decision / outcome | Evidence and classification | Boundary / follow-up |
|---|---|---|---|
| DEC-07 | Use fixed HotpotQA distractor/validation contexts for a 100-ID matched controlled comparison | **[VERIFIED: run log]** `results/hotpot_predictions_100.jsonl`; `results/hotpot_predictions_100.meta.json` (`n=100`, seed 42); `scripts/prepare_hotpot.py` | Not live retrieval; HotpotQA is a short-answer proxy, not scholarly literature synthesis |
| DEC-08 | Use Qwen2.5-7B-Instruct, Transformers and bitsandbytes 4-bit **NF4** quantization | **[VERIFIED: implementation and run metadata]** `src/study.py`, `.meta.json` | Earlier DEC-04's `Q4_K_M` and “Clean ReAct” wording describes a plan, **not executed code**. Actual decoding: `do_sample=False`, not an explicit `temperature=0` argument. GPU/device and package revisions not archived |
| DEC-09 | Implemented controls: `clean`, `injected`, `plain_retry`, `reflexion_style` | **[VERIFIED: source and predictions]** `src/study.py`; 100 aligned IDs | Neither ReAct nor published Reflexion is reproduced. Reflexion-style is a single feedback-bearing rerun; no long-term memory. Plain retry and feedback prompts are not information-matched |
| DEC-10 | Add a conspicuous false-answer annotation to one seeded randomly selected context document, preserving source sentences | **[VERIFIED: source]** `corrupt()`; **[VERIFIED: student-reported audit]** synthetic marker visible within first 14,000 characters for all 100 | Literal marker in extraction/answer = 0/100; zero copying does not exclude semantic contamination |
| DEC-11 | Report actual benchmark and paired differences | **[VERIFIED: supplied outputs]** `results/metrics_100.csv`: clean 57/100, injected 54/100, plain retry 54/100, Reflexion-style 56/100 | Paired injection−clean difference −0.03; recorded bootstrap 95% interval [−0.09, +0.03] includes zero. No significant degradation claim |
| DEC-12 | Report two distinct recovery denominators | **[VERIFIED: item-level results]** among all 46 injected-incorrect examples, retry 0/46, Reflexion-style 2/46; among six clean-correct→injected-wrong, 0/6 and 1/6 | Only exact-match outcome recovery. Not validated semantic/factual recovery |
| DEC-13 | Perform six-case qualitative audit | **[VERIFIED: output inspection]** `results/failure_cases.json`, `failure_analysis.csv`; **[INFERRED]** three substantive factual changes, three likely semantic-equivalence/format mismatches | These judgments are not blinded or comprehensive. “Stone Brewing” vs “Stone Brewing Co.”, “2” vs “Mach 2”, “Alachua” vs “Alachua County” must not silently alter EM |
| DEC-14 | Narrow research claims to evidence-context sensitivity, not a causal propagation coefficient | **[VERIFIED: missing independent extraction-error labels]** `src/study.py`, trace structure and manuscript limitations | Proposed γ₂→₃/γ₂→₄, supporting fact F1 and ScholarQABench n=25 **NOT EXECUTED / NOT ESTIMATED**. Do not claim success on these planned metrics |
| DEC-15 | Preserve frozen-protocol history honestly | **[VERIFIED: current config]** `configs/frozen_protocol.json` says `PROPOSED_NOT_PREREGISTERED` | Do not retrospectively claim preregistration; identify the full-run protocol and any post-hoc audit separately |
| DEC-16 | Update provenance documentation and scientific checking | **[VERIFIED: repository artifacts and uploaded measurements]** paper, scripts, data source, tests | External source metadata and model/dataset revision hashes pending; original records retain original dates |

### Original-plan discrepancies that must be carried into the viva

- Planned `Q4_K_M` was **not** executed; code uses bitsandbytes `nf4` with CUDA.
- Planned “Clean ReAct / Injected ReAct” are **not** original ReAct agents. Stage 2 serializes pre-supplied HotpotQA evidence; there is no real retrieval tool/action loop.
- Planned full “Reflexion” was **not** executed; code applies a single reflection-style warning and previous answer in a final-answer prompt.
- Planned gamma coefficients, extraction correctness labels, supporting-fact F1 and 25 ScholarQABench examples are **not complete**.
- A 100-example data validation sample was used for evaluation, but no evidence of a separate non-overlapping development split for prompt design is archived. Potential leakage/selection concerns remain **[UNKNOWN]**.

### Prompt-to-artifact crosswalk

| Assignment prompt | Prepared/verified artifact |
|---|---|
| 01–02 | Existing Phase-I work and decision log; this addendum corrects executed status |
| 03 | `docs/literature_to_experiment_map.md` |
| 04 | `docs/feasibility_novelty_audit.md` |
| 05 | `docs/research_brief.md` |
| 06–07 | `data/datasets.md` or `data/README.md`, `configs/frozen_protocol.json`, `docs/research_brief.md`; not preregistered |
| 08–11 | Code, test log, `baseline_validation.md`, `docs/experiment_run_manifest.md`, `docs/ai_use_audit.md` |
| 12–14 | `docs/results_interpretation.md`, metrics and paired logs; selected Pathway B |
| 15 | `paper/main.tex`, `paper/main.pdf`, `paper/references.bib`; bibliographic cross-check outstanding |
| 16 | `docs/technical_peer_review.md` |
| 17 | README, scripts, results, requirements; exact versions pending |
| 18 | `ai_assistance_log.md`, `docs/ai_use_audit.md` |

**Remaining independent human tasks:** verify primary-source publication metadata; recover package versions/revision hashes or explicitly mark irrecoverable; cross-check a sample of predictions against primary dataset evidence; confirm final bibliography and README match the GitHub contents.
