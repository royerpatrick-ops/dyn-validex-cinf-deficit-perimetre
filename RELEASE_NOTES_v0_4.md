# v0.4 — Effective parabolic remainder and second perimeter-deficit term

This release extends v0.3 with a separate proof note, internally versioned 0.1. It derives $O((1+s)e^{-4s/7})$ and every strict exponent $0<c<2/3$ for full circle averages of the parabolic remainder. Exact cusp geometry gives global Lipschitz and $W^{1,2}$ regularity; the spectral argument includes the continuous spectrum, and smoothing is uniform in the cusp.

With the documented Mellin and parabolic-envelope arguments, it derives the second perimeter-deficit term for fixed planar $C^3$ convex bodies with positive curvature:

$$
-B R^{-1/2}\int_{\partial K}\kappa^{3/2}\,ds,
\qquad
B=-\frac{\sqrt2}{6\pi}Z_{\rm prim}(3/2)>0.
$$

The complete remainder is $O_{K,\delta}(R^{-1/2-\delta/3})$ for every $0<\delta<1/6$. The approximate decimal $B\approx0.289423417860128$ is not an interval certificate.

The proof is proposed and counter-reviewed by several Codex branches. Claude AI supplied the antecedent note and script, preserved unchanged. No independent human mathematical review, endpoint exponent, second term in dimension 3, or singular-curvature extension is claimed. Earlier releases and dated audits remain intact.

Author: Patrick Royer, independent researcher without institutional affiliation. AI assistance, the documented Python/NumPy/SciPy/mpmath environment and the custom DEL 1.1 scope are recorded in the corpus.

Publicly verified publication identifiers:

- GitHub release: <https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/releases/tag/v0.4>
- Tagged content commit: [`08f329dd9ae1949906ca10fc6c908c1b4a9bf65f`](https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/commit/08f329dd9ae1949906ca10fc6c908c1b4a9bf65f)
- Zenodo v0.4 version DOI: [10.5281/zenodo.23258648](https://doi.org/10.5281/zenodo.23258648)
- Zenodo concept DOI: [10.5281/zenodo.23209552](https://doi.org/10.5281/zenodo.23209552)
- Previous v0.3 DOI: [10.5281/zenodo.23238780](https://doi.org/10.5281/zenodo.23238780)

The tag `v0.4` remains on the content commit. These identifiers and the cumulative Zenodo file checksums are added afterward in [`releases/v0.4/PUBLICATION_RECEIPT.json`](releases/v0.4/PUBLICATION_RECEIPT.json) without retagging.
