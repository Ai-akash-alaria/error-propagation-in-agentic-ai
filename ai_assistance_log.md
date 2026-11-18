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

---

## Subsequent AI-assisted debugging and analysis (continuation of existing log)

This log records assistance **reported in the chat and supported by user-shared outputs**, rather than claiming autonomous access to the user's Colab/GitHub account. Original log dates and earlier statements are preserved as historical notes.

| Task / AI suggestion | Human observation or decision | Verification / outcome |
|---|---|---|
| Shell path quoting on Google Drive | User supplied `/content/drive/MyDrive/... (1)/...` Bash syntax error | Path quoted; Colab directory changed with `%cd` |
| Module imports / environment | `requirements.txt` not found and `src` import initially failed | Correct project root and `PYTHONPATH`; subsequent tests run, with five tests documented in archived `test_log.txt` |
| Dataset record count | `hotpot_100.jsonl` had only 5 lines after pilot generation | Human reran `prepare_hotpot.py --n 100 --seed 42` and asserted 100 rows |
| End-to-end inference | User ran Colab 100-ID inference and uploaded outputs | Actual 100-record JSONL and metadata (`elapsed_s=3031.25`) inspected; no invented GPU model |
| Paired metrics and uncertainty | AI suggested analysis; human supplied output | 57/54/54/56 EM; six adverse flips, three reverse, recovery 0/6 vs 1/6; bootstrap in evaluation summary |
| Injection integrity | AI noted marker non-reproduction did not prove no corruption | Human reconstructed dirty contexts; 100/100 marker visibility, 0/100 copying in extraction/answer |
| Failure-case analysis | AI proposed six-case audit and noted semantic mismatch risks | User displayed original and modified extractions/answers; three potentially equivalent strings flagged, no full semantic regrading |
| Research paper and GitHub repository | AI drafted manuscript, README and review documents | Student uploaded code, results, PDF and README and showed repository screenshots; publication claims and references still require primary-source review |

**At least three observed AI/software limitations:** (1) earlier instructions ran from the wrong working directory, (2) the five-item pilot overwrote a misleadingly named `hotpot_100.jsonl` file, (3) naive exact-match scoring misclassified potentially equivalent answers, and (4) initial research documents incorrectly retained pre-run status after GPU execution. These were identified through actual user console output or files, not imagined incidents.

**Human ownership:** Student is responsible for understanding `src/study.py`, confirming source citations, describing experimental decisions, verifying results, and accurately disclosing AI assistance under institute policies. The GitHub commit history and Colab notebook are additional first-party evidence not independently fetched during this documentation patch.
