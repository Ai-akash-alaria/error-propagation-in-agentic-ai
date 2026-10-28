# Human-AI Collaboration & Manual Verification Audit Log

As required by the lab workflow, LLM prompts were used as an assistive tool to structure the initial workspace and draft candidate gap formulations, followed by personal critical review, manual cross-checking, and correction.

---

## Log Entry 1: Workspace Setup (Prompt 01 Execution)
- **Task:** Initialize project workspace, formalize evidence tagging rules, and establish scope tracking.
- **AI Tool Used:** Gemini (Interactive Chat).
- **My Prompt Input:**
  > *"I am a postgraduate student converting my completed literature review into an implementation-based research paper. My topic is Error Propagation in Multi-Step Agentic AI Workflows for Research Automation. Act as a critical research mentor and technical pair programmer. Guide me in stages... Mark statements as VERIFIED, INFERRED or UNKNOWN... Help me create a portable research_decisions.md log... Start by asking me to attach my existing review and summarize its scope without assuming unseen content."*
- **AI Output Review & Manual Corrections:**
  - *AI Output:* Provided a broad summary of agent architectures and suggested generic software bug-tracking frameworks.
  - *My Manual Verification & Correction:* Corrected the AI's focus to strictly reflect the mathematical formulation ($\gamma_{j\to i}$, $PC(x)$) and paper evaluation frameworks (ReAct, AgentDebug, OpenScholar) explicitly established in my review paper. Rejected generic software engineering additions and locked scope strictly to agent trajectory reliability.

---

## Log Entry 2: Gap Identification & Ranking (Prompt 02 Execution)
- **Task:** Extract testable research gaps from my review paper and establish feasibility rankings.
- **AI Tool Used:** Gemini (Interactive Chat).
- **My Prompt Input:**
  > *"Analyze my attached literature review. Identify central methods, datasets, measured findings, author-reported limitations and unresolved questions. Propose five computationally testable research gaps. For each, cite the specific passage or reference in my review; clearly distinguish a limitation reported in the original paper from your own inference; state the experimental question it suggests and what evidence would test it... Rank three gaps by research significance, available resources and implementation feasibility."*
- **AI Output Review & Manual Corrections:**
  - *AI Output:* Proposed 5 gaps, but initially misclassified my own inferred analytical points as "reported facts from external authors." It also suggested complex fine-tuning experiments that exceeded single-GPU feasibility.
  - *My Manual Verification & Correction:* Manually audited all 5 gaps against my PDF text (`L.REVIEW PAPER .pdf`). Corrected the classification tags to properly distinguish explicit author-reported gaps (Sections 7.1, 7.6, 8.3) from inferred research gaps (Sections 8.4, 8.6). Re-ranked the gaps based on actual computing setup (Google Colab / local GPU) to ensure experiments are realistic for an M.Tech project.

---

## Log Entry 3: Literature-to-Experiment Mapping (Prompt 03 Execution)
- **Task:** Map literature gaps to an executable experiment blueprint and select study pathway.
- **AI Tool Used:** Gemini (Interactive Chat).
- **My Prompt Input:**
  > *"My literature review identified candidate gaps GAP-1, GAP-3, GAP-5. Identify three published methods from my review that could realistically be implemented or reproduced. Map original papers to algorithm, dataset, code, metrics, and limitations. Compare three experimental studies (A, B, C) and recommend a minimum viable research experiment for 48-hour local GPU execution."*
- **AI Output Review & Manual Corrections:**
  - *AI Output:* Suggested attempting full OpenScholar datastore retrieval (45M papers) and running multi-agent consensus voting over a 1-week timeline.
  - *My Manual Verification & Correction:* Recognized that hosting a 45M paper embedding datastore exceeds local GPU storage. Sized the execution window to 48 hours (Oct 28–30). Identified that state rollback (GAP-3) on a linear path graph acts as simple truncation, requiring fan-out reuse graphs to demonstrate non-trivial recovery. Pinned ReAct trajectory logging via NetworkX as the primary substrate.

---

## Verification Checklist
- [x] Topic and author metadata accurately reflect my paper (*Error Propagation in Multi-Step Agentic AI Workflows for Research Automation*).
- [x] Scope summary and decision log (`research_decisions.md`) are established with explicit `[VERIFIED]`, `[INFERRED]`, and `[UNKNOWN]` tags.
- [x] Gap matrix contains 5 testable research gaps backed by exact citations to my review paper.
- [x] Top 3 gaps are ranked with concrete feasibility analysis (compute, datasets, fallback plans).
- [x] Human-AI audit log documents my personal verification, critical edits, and corrections to AI outputs.
