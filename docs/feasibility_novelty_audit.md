# Prompt 04 — Feasibility, neighboring work, novelty check

## Source checks and boundary of verification

| Claim | Status | Primary evidence / action |
|---|---|---|
| ReAct interleaves reasoning and actions | **[VERIFIED publication]** | https://arxiv.org/abs/2210.03629 and ICLR 2023 |
| Reflexion uses verbal feedback / persistent experience | **[VERIFIED publication]** | NeurIPS 2023: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html |
| HotpotQA supports distractor setting and CC BY-SA 4.0 | **[VERIFIED dataset card]** | https://huggingface.co/datasets/hotpotqa/hotpot_qa |
| Qwen2.5-7B-Instruct weights have a public model card; card says Apache-2.0 | **[VERIFIED model card]** | https://huggingface.co/Qwen/Qwen2.5-7B-Instruct |
| ScholarQABench and OpenScholar scientific evaluation exist | **[VERIFIED original repository/paper]** | https://github.com/AkariAsai/OpenScholar ; https://github.com/AkariAsai/ScholarQABench |
| Current exact model/dataset commit and frozen Python packages | **[UNKNOWN]** | Original run metadata lacks commit IDs/package freeze; no retroactive claims |
| Novel conditional propagation metric is first of its kind | **[UNKNOWN]** | No exhaustive 2026 novelty/priority search completed; cannot claim originality |

## Neighboring work search plan (for submission literature check)

Search scholarly indexes: `"error propagation" "ReAct" agents`, `"LLM agent" "intermediate state" perturbation`, `"trajectory debugging" language model agents`, `"prompt injection" retrieval downstream accuracy`, `"Reflexion" ablation feedback warning`, `"process supervision" reasoning reliability`, `"causal attribution" agent trajectories`, `"retrieval corruption" multi-hop QA`.

Interpret reported limitations from original publications only, not assumptions. The review's candidate AgentDebug/AgentPro publication-year claims must still be individually checked before incorporating them in bibliography.

## Feasibility and actual constraints

- Model/data: `Qwen/Qwen2.5-7B-Instruct`, bitsandbytes NF4 in `src/study.py`; actual dataset `hotpotqa/hotpot_qa` distractor validation (100 IDs, seed 42). Both are public sources, but exact revisions were not pinned.
- Observed wall clock: 3031.25 seconds for 100 items/four conditions from run metadata; exact Colab GPU model and peak memory **UNKNOWN**.
- Budget: No external API or fine-tuning is required by the code. Repeating the full experiment costs substantial Colab compute.
- Feasible fallback: retain existing evidence and run reproducible CPU/mock tests or analyze saved predictions without regenerating model outputs; never represent mock outcomes as benchmark results.
- Threats: conspicuous marker, source evidence preserved, instruction to ignore retrieved instructions, asymmetric feedback prompts, fixed condition order, answer in raw context, single sample/model, exact-match aliases, and source truncation.

## Go/no-go conclusion

**GO** for an exploratory Pathway-B controlled-comparison *course study* using existing logs and honest caveats. **NO-GO** for claims of a new algorithm, replicated canonical ReAct/Reflexion, verified causal propagation coefficient, statistically reliable improvement, or scholarly generalization. Those require new controlled experiments, blinded semantic validation and/or different data.
