# Prompt 16 — Technical peer-review and revision log

**Review type:** AI-assisted internal technical critique of the current 100-example manuscript, source code and archived outcomes. **Not external peer review.** Page locations refer to the 7-page uploaded `paper/main.pdf` and section numbers seen in its text/screenshots.

## Major findings

| Priority | Location | Concern / why it matters | Concrete remedy | Status / author response |
|---|---|---|---|---|
| M1 | Sec. III/IV, pp. 2–4 | The original γ₂→₃/γ₂→₄ hypothesis is not measurable from marker-copying; no independently rated extraction correctness | Keep primary analysis as paired EM; collect blinded extraction factual labels and independently perturbed states for a future γ study | **Acknowledged, not resolved experimentally** |
| M2 | Sec. IV/V, pp. 3–4 | Prompts/controls differ in length and information; warning in Reflexion-style condition confounds reflection effect | New matched-length warning-only ablation, fixed evaluation protocol | **Acknowledged; no extra data** |
| M3 | Sec. V/VII, pp. 4–6 | Three of six adverse EM flips look like equivalent answers; EM is not factual accuracy | Blind semantic review across all 100 paired items, report separate semantic scores | **Partial six-case manual audit** |
| M4 | Sec. IV/V, pp. 3–4 | Intervention uses salient synthetic marker and retains true evidence, so is not typical factual corruption | Targeted plausible source substitution; pre-register severity levels and intervention checks | **Unexecuted future test** |
| M5 | Sec. V and repository | Exact package versions, model and dataset revisions, confirmed GPU specification unavailable | Capture actual original Colab environment records if recoverable; pin versions after independent rerun | **Open provenance gap** |
| M6 | Related Work, Sec. II; references | Need full source-by-source bibliographic verification and up-to-date novelty check | Verify each cited paper against official record and update `.bib` only as warranted | **Partially checked; unresolved full audit** |
| M7 | All results, pp. 4–6 | 100 paired IDs, one model and fixed prompt order limit generalization and uncertainty | Hold out separate development questions, rerun multiple model seeds/perturbations and more items | **Not executed; paper appropriately limited** |

## Minor findings

- Avoid calling the clean path “ReAct” and feedback prompt “Reflexion” without qualifiers; use “fixed-context pipeline” and “Reflexion-style”.
- Plain retry is not a true restart with identical information as Reflexion-style. Label it generic retry prompting.
- Clearly distinguish 0/46 vs 0/6 and 2/46 vs 1/6 recovery denominators.
- State that `marker_in_extraction=0` counts **literal matching**, not arbitrary misinformation.
- README results should refer to `metrics_100.csv`, not the earlier 11-item `metrics.csv`.
- Figure is descriptive; report confidence intervals adjacent to interpretation.
- Check paper references match claims/URLs; check `main.tex` can rebuild from uploaded figure paths.

## Prioritized revision checklist

- [x] Recorded 100-item results rather than placeholder metrics.
- [x] Described small and uncertain paired EM differences.
- [x] Distinguished two recovery denominators.
- [x] Analyzed six adverse cases and explicit alias limitations.
- [x] Explained why this is not full ReAct/Reflexion reproduction or formal causal γ.
- [ ] Complete independent bibliographic verification.
- [ ] Recover/pin executed versions and revisions where possible.
- [ ] Obtain a blinded all-case semantic evaluation if factual accuracy is claimed.
- [ ] Run matched warning and targeted-corruption ablations only if stronger causal contribution is required.

**Author response:** The current course-level study claims only a narrow paired, reproducible result; the unperformed analyses are disclosed as unresolved rather than fabricated. These notes document an internal review, not a published reviewer's acceptance.
