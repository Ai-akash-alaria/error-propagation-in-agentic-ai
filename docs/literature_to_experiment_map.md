# Prompt 03 — Literature-to-experiment mapping

**Source basis:** user's literature review, Phase-I lab, actual Python pipeline, and official method/dataset pages linked below. The **published algorithms are distinct** from the study's simple fixed-context implementation.

| Published method / primary source | Original idea and evaluation | Code/data/access evidence | Feasibility vs implemented study |
|---|---|---|---|
| ReAct — Yao et al., ICLR 2023, https://arxiv.org/abs/2210.03629 | Interleaves reasoning with actual actions/tool observations, evaluated in QA/interactive tasks | Primary article verified; original benchmark reproduction **NOT performed** | Would require a tool/action loop, not merely a decomposition prompt. Existing study uses supplied contexts and is **not ReAct** |
| Reflexion — Shinn et al., NeurIPS 2023, https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html | Uses verbal feedback and episodic memory to improve repeated attempts | Published code linked from NeurIPS paper: https://github.com/noahshinn/reflexion | Current study tests only a one-pass feedback prompt, **not original Reflexion**; compare labels carefully |
| OpenScholar — Asai et al., https://github.com/AkariAsai/OpenScholar | Literature retrieval and citation-grounded scientific synthesis; ScholarQABench relates to domain validation | Official repository and Nature article: https://www.nature.com/articles/s41586-025-10072-4 | Full research-paper corpus/retrieval and evaluation are beyond the 100-question proxy; 25-item extension **not executed** |

## Candidate studies considered

| Pathway | Minimal baseline | Primary question | Resource and scientific considerations | Evidence status |
|---|---|---|---|---|
| A — Published-method reproduction + extension | Original ReAct or Reflexion procedure and matching benchmark | Can a validated published method recover under injected evidence? | More implementation and baseline-alignment time; original source code and environment needed | **NOT EXECUTED** |
| **B — Controlled comparison (selected)** | Fixed-context clean question-answering pipeline | Do corrupt context annotations change EM, and how do two retry instructions compare? | Single 7B model, no fine-tuning; paired 100-ID logs + failures | **EXECUTED**; small, narrow study |
| C — Targeted modification | Clean baseline plus a separately validated verifier/rollback module | Does a specific verifier contain propagation while preserving accuracy? | Additional module, error labels, ablation and balanced controls needed | **NOT EXECUTED** |

**Selected experiment:** Pathway B. Actual `src/study.py` performs three model generations per condition (plan, extraction, synthesis) and injects a false-answer sentence into fixed evidence at stage 2. Source context is not retrieved live. Use four conditions `clean`, `injected`, `plain_retry`, `reflexion_style`; do not call these canonical ReAct or Reflexion replications.

**Original-to-study bridge:** Review identifies stage reliability and GAP-1 → fixed-context intervention isolates one input modification → same 100 IDs measured across four conditions → measured final-answer EM and limited marker checks → paired error-case audit reveals failure modes and limitations. Independent extraction-label-based γ remains unestimated.
