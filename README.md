# A candidate leading constant for the perimeter deficit of randomized integer convex hulls — corrective v0.2

**Patrick Royer — independent researcher, unaffiliated, France**  
7 October 2026 · [Zenodo DOI 10.5281/zenodo.23209553](https://doi.org/10.5281/zenodo.23209553)

This repository is the public source companion to the distinct corrective note v0.2. It preserves the received historical material, exposes the corrected manuscript and scripts, and asks for specialist review.

## Scientific status

- The candidate leading coefficient for the global perimeter deficit is **conjectural**. Equality between the local-model integral and the finite-radius lattice asymptotic has not been proved.
- The proposed second-order term is **exploratory**. Its existence, exponent and remainder are not established.
- The finite-domain script checks and reduced CLI smoke runs are technical consistency checks. They do **not** prove the conjecture and are not rigorous global error bounds.
- No new long scientific campaign, P2 campaign, RNG flow, Arb certification or global theorem certification was run for this publication.

## Contents

- [`manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.pdf`](manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.pdf) — corrective manuscript (8 pages; main publication PDF).
- [`manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.tex`](manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.tex) — editable LaTeX source.
- [`scripts/`](scripts/) — corrected Python programs, dependency list and detailed usage notes.
- [`evidence/`](evidence/) and [`validation/`](validation/) — already-produced validation records and reduced-run outputs.
- [`originals/`](originals/) — the two received historical pieces, preserved byte for byte.
- [`archive/DYN-CINF_CORRECTIVE_v0_2.zip`](archive/DYN-CINF_CORRECTIVE_v0_2.zip) — original corrective package as supplied, with its SHA-256 sidecar and internal manifest.
- [`REPRODUCTION.md`](REPRODUCTION.md) — build and optional verification instructions.
- [`REVIEW_REQUEST.md`](REVIEW_REQUEST.md) — questions for independent specialist review.

## Reproducibility limits

The historical `reanalysis_92_points.csv` and the historical Arb certification program were not present in the supplied material. Consequently, the reported 69-point fits and historical certified decimal evaluation cannot be independently reproduced from this repository. The corrected scripts use Python, NumPy, SciPy and pandas in finite precision. See [`scripts/README.md`](scripts/README.md) for all qualifications.

## AI assistance and responsibility

Patrick Royer developed the source simulations and finite-domain model with substantial assistance from ChatGPT/Codex. Claude (Anthropic) contributed the initial heuristic assembly, tail and cutoff analyses and numerical checks. ChatGPT/Codex assisted with corrective implementation checks, distinctions between proved, numerical and conjectural statements, documentary integration, repository preparation, metadata and publication verification. These are AI-assisted checks; **no independent human mathematical peer review is attested**. Patrick Royer remains the author responsible for the claims and submission.

The numerical and typesetting workflow uses Python, NumPy, SciPy, pandas and LaTeX. Git, GitHub and Zenodo are used for versioning and dissemination. This list does not imply that every AI service was free of charge.

## Related deposits

- [Initial development — DOI 10.5281/zenodo.23110956](https://doi.org/10.5281/zenodo.23110956) · [GitHub](https://github.com/royerpatrick-ops/dyn-validex-developpement-initial)
- [Pont idéal 1–2 — DOI 10.5281/zenodo.23188815](https://doi.org/10.5281/zenodo.23188815) · [GitHub](https://github.com/royerpatrick-ops/dyn-validex-pont-ideal-1-2)

Those records are prior, related deposits; this corrective has its own version, repository and DOI.

## Licence

Eligible repository material is distributed under the custom **Dynagénèse Ethical Licence (DEL) 1.1**, adapted only to identify this v0.2 corpus. The French text is authoritative; the English text is a reading translation. DEL 1.1 includes use restrictions and is not an OSI-approved open-source licence. Third-party and historical items retain their own rights and conditions. See [`licenses/LICENSE_SCOPE.md`](licenses/LICENSE_SCOPE.md) and [`metadata/RIGHTS_AND_LICENSES.md`](metadata/RIGHTS_AND_LICENSES.md).

## Citation

Use the Zenodo DOI above and the metadata in [`CITATION.cff`](CITATION.cff). If you inspect or reuse modified files, cite the exact release and commit.
