# Human-AI Collaboration & Verification Log (`ai_assistance_log.md`)

- **Student Name:** Akash Alaria (`MHM2026015`)
- **Project:** Error Propagation in Multi-Step Agentic AI Workflows for Research Automation
- **Rule:** Every significant AI interaction is audited against primary sources or execution outputs. AI suggestions are never treated as verified authority without manual inspection.

---

### Log Entry 1: Workspace Setup & Scope Formalization (Prompt 01 Execution)
- **Date:** 2026-10-22
- **Task:** Initialize project workspace, formalize evidence tagging rules (`[VERIFIED]`, `[INFERRED]`, `[UNKNOWN]`), and establish scope tracking in `research_decisions.md`.
- **AI Tool Used:** Gemini (Interactive Chat).
- **Prompt Summary:** Requested a critical research mentor setup to convert the completed literature review into an implementation study while enforcing strict evidence labels and preventing fabricated citations or results.
- **AI Proposal:** Provided a broad summary of agent architectures and suggested generic software bug-tracking frameworks.
- **Human Verification & Manual Correction:** Corrected the AI's focus to strictly reflect the probabilistic formulation ($r_i, \gamma_{j \to i}, PC(x), s_i, \rho_i$) and target frameworks (ReAct, Reflexion, AgentDebug, AgentPro, OpenScholar) established in my review paper. Rejected generic software engineering additions and locked the scope to agent trajectory reliability (`DEC-01`).

---

### Log Entry 2: Gap Identification & Feasibility Ranking (Prompt 02 Execution)
- **Date:** 2026-10-22
- **Task:** Extract five computationally testable research gaps from the literature review and rank the top three by scientific significance and single-GPU feasibility.
- **AI Tool Used:** Gemini (Interactive Chat).
- **Prompt Summary:** Instructed the AI to extract central methods, measured findings, and limitations from `REVIEWPAPER.pdf`, distinguish author-reported limitations from inferred gaps, and rank three gaps by implementation feasibility.
- **AI Proposal:** Proposed five candidate gaps (`GAP-1` through `GAP-5`), but initially misclassified my own inferred analytical points as reported external author facts and suggested resource-heavy fine-tuning experiments unsuitable for a single GPU.
- **Human Verification & Manual Correction:** Audited all five gaps line-by-line against my review PDF. Re-tagged `GAP-1`, `GAP-2`, and `GAP-4` as `[VERIFIED]` (explicitly reported in Sections 7.1, 7.6, and 8.3) and `GAP-3` and `GAP-5` as `[INFERRED]` (extrapolated from Sections 8.4 and 8.6). Re-ranked `GAP-1`, `GAP-3`, and `GAP-5` based on local/Colab single-GPU constraints without fine-tuning.

---

### Log Entry 3: Literature-to-Experiment Mapping & Pathway Selection (Prompt 03 Execution)
- **Task:** Map review architectures (ReAct, Reflexion, AgentDebug) to a minimum viable experiment, select datasets, and compare Study Pathways A, B, and C.
- **AI Tool Used:** LLM Assistant (Prompt 03 execution).
- **AI Proposal:**
  - Recommended **Study Pathway B** (controlled Stage-2 error injection on a 4-stage pipeline: `Query Decomposition -> Evidence Retrieval -> Fact Extraction -> Final Synthesis`) using **Qwen2.5-7B-Instruct (4-bit)**, **HotpotQA distractor ($n=100$)** as the primary controlled testbed, and **ScholarQABench** for research-domain validation.
  - Flagged two bibliographic year errors in my prior notes: **AgentDebug / AgentErrorBench** (Zhu et al.) is a September 2025 arXiv preprint, and **AgentPro** (Deng et al.) is an EMNLP 2025 paper (not 2024).
  - Recommended deferring **GAP-5** ($PC(x)$ verification gating) until propagation behavior is empirically measured under **GAP-1**.
- **Human Verification & Manual Correction:**
  - Accepted Study Pathway B, the 4-stage pipeline, and the bibliographic corrections (`DEC-06`).
  - Added a **`Injected + Plain Retry`** control condition alongside **`Injected + Reflexion`** (`DEC-04`) so recovery rate ($\rho$) gains from verbal reflection are separated from simple second-attempt re-sampling.
  - Restricted HotpotQA claims strictly to controlled multi-hop evidence reasoning while retaining a 25-example `ScholarQABench` validation slice to preserve domain relevance to scientific research automation (`DEC-03`).
  - Marked repository code execution and dataset split inspection as pending manual verification before running Prompt 04.

