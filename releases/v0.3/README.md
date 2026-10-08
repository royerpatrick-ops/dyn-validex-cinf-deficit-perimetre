# DYN-VALIDEX: leading perimeter-deficit asymptotic — v0.3

**Patrick Royer · 8 October 2026 · AI-assisted mathematical preprint**

For a fixed planar convex body K with C² boundary and strictly positive curvature, the unified manuscript derives

E[P(RK) − P(conv(L ∩ RK))] = C_void (∫∂K κ^(4/3) ds) R^(−1/3) + o_K(R^(−1/3)),

where L is an independently uniformly rotated and translated square lattice. The coefficient is identified by a stationary parabolic row model and enclosed by exact rational computation:

**0.719232985957311632 < C_void < 0.719233362190182706.**

The certified rounded value is 0.719233. The exact coefficient is not asserted to equal 0.719 or 0.719233. The previously established order R^(−1/3) is attributed to Ngoc–Reitzner (2021). This package does not establish a second term, a convergence rate, or an extension to flat or nonsmooth points.

## Read and reproduce

- `manuscript/`: unified English manuscript, French abstract, PDF and LaTeX source.
- `code/cert_identity_rational.py`: minimal exact-arithmetic certificate, Python standard library only.
- `code/verif_notes_arrondis_exterieurs.py`: independently written symbolic, floating and statistical diagnostics; only part C is a rational enclosure.
- `results/`: freshly reproduced exact fractions and reference outputs.
- `evidence/`: dated original notes and Claude audit, preserved unchanged.
- `licenses/`, `metadata/`, `provenance/`: rights, citation and research provenance.
- `publication/`: concrete Codex deposition instructions and status.
- `SHA256SUMS.txt`: all included files except the checksum manifest itself.

Run from this directory:

```bash
python3 code/validate_release.py
python3 code/cert_identity_rational.py --N 100 --output ../CERTIFICATE_replay.json
python3 code/verif_notes_arrondis_exterieurs.py C
```

For all diagnostic sections, install the packages in `code/requirements-diagnostics.txt`, then run:

```bash
python3 code/verif_notes_arrondis_exterieurs.py A B C D E
```

The exact fractions and outward bounds must reproduce; elapsed times can differ. Replaying a command overwrites its results file and thus changes its archived checksum when a duration is recorded. Validate the original manifest before replay, or retain regenerated results outside the extracted archive.

To compile the manuscript, use pdfLaTeX twice from `manuscript/` (TeX Live with the packages declared in the source). The supplied PDF was rendered and visually inspected. Poppler is used for rendering, not for the mathematical certificate.

## Verification status

The argument and computations have been developed and checked with AI assistance. **No independent human mathematical review and no formal proof-assistant verification are attested.** The certificate proves the numerical evaluation of stated series with the supplied remainder bounds; model identification is the mathematical argument. Monte Carlo checks and floating quadratures are diagnostics. Prior notes retain their original, historically incomplete status statements; the unified manuscript is the current presentation.

## Rights and citation

The author-selected custom DEL 1.1 licence applies to the designated new corpus to the extent of the author's rights. See `LICENSE`, the unchanged licence PDF and `licenses/LICENSE_SCOPE.md`. It is not an OSI-approved open-source licence. No CC or MIT relicensing is authorized by this package. Third-party software and references retain their own terms; mathematical facts and formulas are not made exclusive by the licence.

Use `CITATION.cff`. The v0.3 version DOI reserved by Zenodo is **10.5281/zenodo.23238780** and the concept DOI is **10.5281/zenodo.23209552**. The previous preprint is version DOI 10.5281/zenodo.23209553; that identifier is **not** the new version's DOI. The source repository is https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre and the v0.3 release is https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/releases/tag/v0.3.

The immutable archive deposited on GitHub and Zenodo was regenerated after the GitHub v0.3 release and before final Zenodo publication. The repository copy of `publication/PUBLICATION_STATUS.json` was then updated with the verified final publication facts; this post-publication status update does not alter the deposited proof, manuscript, certificate or archive.
