# Prompt 18 — Human–AI collaboration and research integrity audit

**Scope:** User-supplied logs and screenshots, previous Phase-I lab, ChatGPT-created source/reporting artifacts and archived experimental results. This report does not pretend to access unshared Colab browser history or a complete chat prompt export.

| AI-assisted activity | Proposed artifact or approach | Human action and independent evidence | Outcome / caveat |
|---|---|---|---|
| Research ideation and gap selection | Move from review toward GAP-1 paired study, GAP-3 inspired retry comparison | Phase-I lab PDF and research decision log establish user-selected direction | Planned priority; external novelty remains unverified |
| Python implementation and tests | `src/study.py`, scripts, MockBackend tests | `results/test_log.txt` and code, five passing tests | Tests validate mechanics, not model performance |
| Colab environment/path assistance | Quote spaces/parentheses, correct working directory, import root | User supplied error traces and later successful execution screenshots | Real issues diagnosed; no invented execution claims |
| Dataset preparation | Generate n=100, seed=42 | User found misleadingly named n=5 file, reran loader, confirmed 100 | Actual file count validated |
| Evaluation | Four conditions, EM, paired analysis and bootstrap | Uploaded metrics CSV, 100 predictions, summary JSON | 57/54/54/56; uncertain outcome |
| Injection exposure | Check marker inside truncated evidence | User reported 100/100 visibility | Literal zero copying is not evidence of no semantic propagation |
| Failure analysis | Analyze six adverse EM flips | User displayed extraction/answer traces; three candidate aliases detected | Provisional human/AI semantic judgments; no blinded exhaustive audit |
| Manuscript and GitHub documentation | Paper draft, README, logs, peer review | Uploaded PDF and GitHub screenshots show real files | Scientific integrity requires clear AI attribution and bibliographic checks |

## Four documented AI-assisted correction examples

1. **Working-directory bug:** early commands assumed the repository root, causing `requirements.txt` missing and `src` import errors. Correcting the directory/import path fixed workflow setup.
2. **Five-example file disguised as a 100-example file:** filename was not reliable. A human line-count check caught the problem; dataset generation was rerun, then 100-row assert passed.
3. **Exact-match overinterpretation:** model output `Mach 2` versus gold `2`, etc., demonstrated that string errors may not be factual errors. The report keeps the original metric and qualifies semantic correctness.
4. **Stale documentation:** pre-run logs called GPU work “not run” after real execution; this update preserves the original timeline and appends the observed status.

## Ownership and boundaries

Human: select research question, run and inspect actual Colab outputs, retain raw logs, understand all code modules, approve final repository changes, verify citations and ethically disclose tool involvement. AI: proposed code, experiment controls, debugging approaches, results summaries, and manuscript wording. AI assistance does not constitute primary scientific source verification and does not warrant inventing missing logs.

**Unverified:** exact historical prompt versions and Git diffs beyond user-visible outputs, GPU type, all package revisions, blind scoring, independent reproduction. They remain explicitly missing, not assumed.

Unchecked items are acknowledged limitations or future research requirements; they have not been experimentally completed in this submission.
