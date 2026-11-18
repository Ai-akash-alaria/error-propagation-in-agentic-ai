# Viva-ready five-minute code-and-results walkthrough

Your assessment is an oral viva, **not a mandatory slide presentation**. The assignment nevertheless requests a five-minute technical demonstration; this can be done by navigating GitHub files and results.

1. **Research question (40 s):** earlier review → GAP-1 stage-level propagation → actual study narrowed to paired HotpotQA context contamination, not causal γ.
2. **Source code (70 s):** `src/study.py`: `context_to_docs`/`evidence` serialize fixed provided contexts; `corrupt(item, seed)` inserts a false-answer marker without replacing original facts; `step` calls the model for plan, extraction, synthesis; `run_item` executes four named conditions and logs predictions.
3. **Environment and validation (40 s):** show `tests/test_study.py` / saved `test_log.txt` (five passed), and `results/hotpot_predictions_100.meta.json` (`n=100`, 3031.25 s). Tests using MockBackend do not equal inference tests.
4. **Results (65 s):** `results/metrics_100.csv`, graph: clean 57%, injected 54%, retry 54%, Reflexion-style 56%; six adverse and three reverse EM flips; 0/6 and 1/6 recovery on adverse flips.
5. **Failure inspection (45 s):** Scream 2: correct extraction Laurie Metcalf but injected synthesis Timothy Olyphant. Sasanian Empire: incorrect extracted relationship carried to answer. “Mach 2” vs “2” exemplifies exact-match alias issue.
6. **Validity and closing (40 s):** marker visible in 100/100 but not copied; no formal γ, no significant improvement established, no full Reflexion/ScholarQABench execution, next experiment would use targeted fact corruption and independent extraction labels.

## Questions to be ready for

- Why is a false annotation different from true document retrieval corruption?
- What exactly does `do_sample=False` control? What remains nondeterministic?
- Why does a marker not appearing in the output fail to prove containment?
- How is your `reflexion_style` different from the published Reflexion method?
- Difference between EM and semantic/factual correctness?
- Why 0/46 vs 0/6 denominators? Which is the specific recovery question?
- Why does a paired confidence interval including 0 block a strong improvement claim?
- Why are the exact model/dataset revision IDs missing? What would improve reproducibility?
