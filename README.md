# DYN-VALIDEX: leading perimeter-deficit asymptotic — v0.3

**Patrick Royer · independent researcher without institutional affiliation · 8 October 2026**<br>
**AI-assisted mathematical preprint; no independent human mathematical review is attested.**

For a fixed planar convex body K with C² boundary and strictly positive curvature, the current unified manuscript derives

E[P(RK) − P(conv(L ∩ RK))] = C_void (∫∂K κ^(4/3) ds) R^(−1/3) + o_K(R^(−1/3)),

where L is an independently uniformly rotated and translated square lattice. Exact rational computation encloses the coefficient by

**0.719232985957311632 < C_void < 0.719233362190182706.**

The certified rounded value is **0.719233**. The order R^(−1/3) was already known and is credited to Ngoc–Reitzner (2021). This release does not establish a second term, a convergence rate, or an extension to flat or nonsmooth boundary points.

**Zenodo version DOI:** [10.5281/zenodo.23238780](https://doi.org/10.5281/zenodo.23238780)<br>
**Zenodo concept DOI:** [10.5281/zenodo.23209552](https://doi.org/10.5281/zenodo.23209552)

## Current presentation

- [`manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.pdf`](manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.pdf) — current unified manuscript.
- [`manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.tex`](manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.tex) — LaTeX source.
- [`releases/v0.3/`](releases/v0.3/) — complete v0.3 corpus: exact certificate, reproduced results, evidence, metadata, provenance and DEL 1.1 scope.
- [`archive/DYN-PUBLICATION_DEFICIT_PERIMETRE_v0_3.zip`](archive/DYN-PUBLICATION_DEFICIT_PERIMETRE_v0_3.zip) — reproducible publication archive, with SHA-256 sidecar.
- [`RELEASE_NOTES_v0_3.md`](RELEASE_NOTES_v0_3.md) and [`CHANGELOG.md`](CHANGELOG.md) — release notes and version history.

Run the integrity check from `releases/v0.3/`:

```bash
python3 code/validate_release.py
python3 code/cert_identity_rational.py --N 100 --output ../../../CERTIFICATE_replay.json
```

The exact fractions and outward bounds must reproduce; elapsed time can differ. Floating quadrature and Monte Carlo sections are diagnostics, not proof certification. The standard-library certificate verifies numerical evaluation of the stated series and remainder bounds, not the mathematical model identification.

## Version history and preservation

Version 0.3 is the current presentation. Version 0.2 remains available in the repository and in its original archive; its conjectural status statements describe that historical release and are not silently rewritten. The prepublication handoff archive for v0.3 is also retained unchanged as [`archive/DYN-PUBLICATION_DEFICIT_PERIMETRE_v0_3_PREPUBLICATION.zip`](archive/DYN-PUBLICATION_DEFICIT_PERIMETRE_v0_3_PREPUBLICATION.zip).

The prior Zenodo version is [10.5281/zenodo.23209553](https://doi.org/10.5281/zenodo.23209553). The version series has concept DOI [10.5281/zenodo.23209552](https://doi.org/10.5281/zenodo.23209552).

Related earlier deposits:

- [Initial development — DOI 10.5281/zenodo.23110956](https://doi.org/10.5281/zenodo.23110956)
- [Pont idéal 1–2 — DOI 10.5281/zenodo.23188815](https://doi.org/10.5281/zenodo.23188815)

## Rights, provenance and citation

The author-selected custom **DEL 1.1** licence applies to the designated v0.3 corpus to the extent of Patrick Royer’s rights. The operative PDF is unchanged and its v0.3 scope notice is explicit in [`releases/v0.3/licenses/`](releases/v0.3/licenses/). DEL 1.1 is not an OSI-approved open-source licence, has no invented SPDX identifier here, and does not replace third-party rights or establish exclusivity over mathematical facts and formulas.

The work was developed and checked with AI assistance. ChatGPT/Codex contributed mathematical development, implementation, assisted verification, drafting and integration; Claude supplied the dated external AI audit and verification material preserved in the corpus. These tools are not human authors, independent reviewers or scientific guarantors.

Use [`CITATION.cff`](CITATION.cff) and cite the exact release and commit when reviewing or reusing modified files.
