# Prompt 05 — One-page research brief (G1)

| Field | Evidence-grounded brief |
|---|---|
| Prior review | *Error Propagation in Multi-Step Agentic AI Workflows for Research Automation*; identifies propagation, provenance, cascading errors and limitations of answer-only evaluation |
| Gap | GAP-1: intermediate error propagation remains insufficiently measured; reported in review Sections 7.6/8.7. This is a motivation, **not** a universal novelty assertion |
| Question | On paired 100 HotpotQA validation questions, how does adding a false annotation to fixed evidence change final-answer exact match and literal marker reproduction? Does retry feedback recover failures? |
| Pathway | B: controlled comparative study, not published-method reproduction |
| Input / intervention | HotpotQA `distractor` validation contexts; one seed-chosen document receives an added false-answer annotation; original evidence stays intact |
| Controlled conditions | Clean, injected, injected+plain-retry prompt, injected+Reflexion-style feedback prompt; same IDs/model, greedy decoding; prompt information differs |
| Primary metric | Answer exact-match accuracy; pairwise injected−clean EM over matched IDs |
| Secondary metrics | Literal marker in extraction/answer, recovery on injected-wrong examples and adverse clean-correct→injected-wrong cases, wall clock and tokens; *not* a formal stage causal γ |
| Hypothesis 1 | Injected EM lower than clean; contradiction: zero or positive paired difference / interval spanning zero does not substantiate a robust decline |
| Hypothesis 2 | Feedback prompt improves recovery over plain retry; contradiction: no improvement or confidence interval consistent with zero |
| Actual observations | n=100; clean 57%, injected 54%, retry 54%, Reflexion-style 56%; 6 adverse string flips, 3 beneficial flips; among adverse cases 0/6 and 1/6 recovered |
| Uncertainty | Paired bootstrap injection-clean −0.03, interval [−0.09,+0.03] includes zero; effect modest and uncertain |
| Compute | Qwen2.5-7B-Instruct bitsandbytes NF4 path, Python 3.13.16 in metadata, 3031.25 seconds logged; exact GPU/model revision unavailable |
| Baseline validity | Clean condition is an internal control with a recorded result, not the original ReAct or Reflexion baseline |
| Deeper analysis | Six manually inspected exact-match adverse flips; three possibly semantic-equivalent; no blinded full-100 factual adjudication |
| First executable milestone | Five software unit tests passed and a 100-item inference run completed; documented by archived test log/predictions |
| Unfinished extensions | ScholarQABench 25 domain items; targeted semantic corruption; formal γ propagation coefficient; supporting-fact F1 |

**Decision:** retain this as a limited experimental study. Avoid claims that Reflexion wins or a causal propagation coefficient has been measured. Publication-level novelty remains **UNKNOWN**.
