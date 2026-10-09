# DYN-VALIDEX: effective remainder and second perimeter-deficit term — v0.4

**Patrick Royer · independent researcher without institutional affiliation · 9 October 2026**<br>
**AI-assisted mathematical preprint. The new proof is proposed and counter-reviewed by several Codex branches; no independent human mathematical review is attested.**

Version 0.4 preserves the leading-term manuscript published in v0.3 and adds a separate proof note (internal version 0.1, 9 October 2026). Earlier manuscripts, releases and audits retain their original versions.

For full circle averages on the space of planar unimodular lattices, the new note derives

$$
\left|\mathcal M_s\Psi_{\mathrm{rem}}-\int_X\Psi_{\mathrm{rem}}\,d\mu\right|
=O((1+s)e^{-4s/7}),
$$

and $O_c(e^{-cs})$ for every $0<c<2/3$. An exact cusp formula gives global Lipschitz and $W^{1,2}$ regularity. A spectral estimate and uniform smoothing then give the rate. The endpoint $c=2/3$ is not claimed.

Combined with the documented Mellin calculation and parabolic-envelope transfer, this gives, for each fixed planar convex body $K$ with **$C^3$ boundary and strictly positive curvature**,

$$
\mathbb E[P(RK)-P(\operatorname{conv}(L\cap RK))]
=C R^{-1/3}\int_{\partial K}\kappa^{4/3}\,ds
-B R^{-1/2}\int_{\partial K}\kappa^{3/2}\,ds
+O_{K,\delta}(R^{-1/2-\delta/3}),
\qquad 0<\delta<1/6.
$$

Here $L$ is a uniformly rotated and translated square lattice, and

$$
B=-\frac{\sqrt2}{6\pi}Z_{\mathrm{prim}}(3/2)
\approx0.289423417860128>0.
$$

The primitive Epstein zeta function is understood by analytic continuation; the positive vector series at $3/2$ diverges. The decimal for $B$ is a high-precision evaluation, **not an interval certificate**.

The v0.3 leading-term manuscript has a distinct $C^2$ scope and certified evaluation of $C$. The new second term requires $C^3$. The order $R^{-1/3}$ was already known and is credited to Ngoc–Reitzner (2021). No second term in dimension 3, endpoint exponent, or flat/singular-curvature case is established here.

**Zenodo v0.4 version DOI:** pending actual Zenodo assignment and public verification<br>
**Zenodo concept DOI:** [10.5281/zenodo.23209552](https://doi.org/10.5281/zenodo.23209552)<br>
**Previous Zenodo version DOI (v0.3):** [10.5281/zenodo.23238780](https://doi.org/10.5281/zenodo.23238780)<br>
**GitHub release:** [v0.4](https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/releases/tag/v0.4)

## Current presentation

- [`manuscript/DYN-PREUVE_TAUX_PSI_REM_v0_1.txt`](manuscript/DYN-PREUVE_TAUX_PSI_REM_v0_1.txt) — new proof note, internal version 0.1.
- [`releases/v0.4/preuve_taux_psirem_v0_1/`](releases/v0.4/preuve_taux_psirem_v0_1/) — proof corpus, provenance, deterministic checks and counter-reviews.
- [`archive/DYN-PREUVE_TAUX_PSI_REM_v0_1.zip`](archive/DYN-PREUVE_TAUX_PSI_REM_v0_1.zip) — preserved proof archive.
- [`RELEASE_NOTES_v0_4.md`](RELEASE_NOTES_v0_4.md) and [`CHANGELOG.md`](CHANGELOG.md) — release notes and version history.
- [`manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.pdf`](manuscript/DYN-MANUSCRIT_DEFICIT_PERIMETRE_v0_3.pdf) — unchanged v0.3 leading-term manuscript.
- [`releases/v0.3/`](releases/v0.3/) — unchanged complete v0.3 corpus.

From the v0.4 proof folder, run:

```bash
python3 VERIFIER_SHA256.py
python3 obstruction/CONTROLE_FORMULES.py
```

The second command requires SciPy and performs deterministic quadratures, not a new Monte Carlo. One diagnostic point outside the proved cusp domain is explicitly labelled. These decimals are not interval certificates. The documented check environment used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0 (the latter for the earlier high-precision constant calculation).

## Version history and preservation

Version 0.4 adds the separate second-term proof supplement without rewriting the v0.3 manuscript. Version 0.3 remains the leading-term presentation with its $C^2$ scope and certified enclosure of $C$. Version 0.2 remains available in the repository and in its original archive; its conjectural status statements describe that historical release and are not silently rewritten.

The v0.3 version DOI is [10.5281/zenodo.23238780](https://doi.org/10.5281/zenodo.23238780). The historical v0.2 DOI is [10.5281/zenodo.23209553](https://doi.org/10.5281/zenodo.23209553). The version series has concept DOI [10.5281/zenodo.23209552](https://doi.org/10.5281/zenodo.23209552).

Related earlier deposits:

- [Initial development — DOI 10.5281/zenodo.23110956](https://doi.org/10.5281/zenodo.23110956)
- [Pont idéal 1–2 — DOI 10.5281/zenodo.23188815](https://doi.org/10.5281/zenodo.23188815)

## Rights, provenance and citation

The author-selected custom **DEL 1.1** licence applies within each designated scope and to the extent of Patrick Royer’s rights. Its operative PDF is preserved unchanged in the v0.4 proof corpus. DEL 1.1 is not an OSI-approved open-source licence, has no invented SPDX identifier here, and does not replace third-party rights or establish exclusivity over mathematical facts and formulas. Earlier versions retain their own notices and rights.

Claude AI supplied the antecedent note and script, preserved unchanged. ChatGPT/Codex developed the new proof, assisted verification, code, counter-reviews, drafting and integration. AI systems are tools, not human authors, independent reviewers or scientific guarantors. See [`PROVENANCE.json`](releases/v0.4/preuve_taux_psirem_v0_1/PROVENANCE.json) for the detailed trace.

Use [`CITATION.cff`](CITATION.cff) and cite the exact release, content commit and verified Zenodo version when reviewing or reusing modified files.
