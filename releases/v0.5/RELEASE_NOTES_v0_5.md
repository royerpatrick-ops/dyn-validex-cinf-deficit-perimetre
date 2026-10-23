# DYN-VALIDEX v0.5 — Explicit disk remainder bounds and request for human review

Patrick Royer — independent, unaffiliated researcher — 23 October 2026.

**Release candidate: `RELEASE_CANDIDATE_DOI_RESERVED`.**
Reserved DOI: https://doi.org/10.5281/zenodo.23598602
Publication is not yet attested; the new tagged content commit is not yet known.

**Proposed AI-assisted mathematical work. No independent human mathematical
review or formal proof verification is attested.**

This version supplements the v0.4 proof corpus with an explicit quantitative
note, internally versioned **v0.1a**, and a public request for critical human
review. The proposed bounds are

$$K_f=2.5\times10^9,\qquad K_E=2000,\qquad K_{\mathrm{geo}}=550000,\qquad R_0=2.$$

The note fixes the metric and cutoff, replaces the Mellin contour argument
with primitive counting and Stieltjes summation, uses heat smoothing to
make the spectral cost explicit, and separates the positive disk geometry
correction. All three constants and the common validity threshold have a
written derivation and a separate AI counter-review.

**The bounds are not numerically informative at the radii already studied.**
The threshold R0=2 is a validity threshold, not an observed onset of the
asymptotic regime. The illustrative radius 2^2100 is only a sufficient,
highly conservative threshold for an absolute normalized-remainder target;
it is neither necessary nor proposed as a computational target.

The internal v0.1a documentary revision clarifies that a fully certified
mean at R=50 is still a possible future result: C51 remains partial.
It also includes the operative DEL1.1 licence, its scope and the public
human-review request. The mathematical constants, formulas, figure and
evaluation program are unchanged from the internal v0.1 chiffrage.

The v0.4 tag, earlier release assets, manuscripts and historical audit
statements retain their versions. This release does not claim peer review,
a completed certified mean at R=50, numerical validation of C or B,
or resolution of the separate Weyl bridge. No new QMC or Windows-chain run
has been performed for this supplement.

## Public request

See `REVIEW_REQUEST.en.md` and `REVIEW_REQUEST.fr.md`. Localized objections,
counterexamples, references and corrections to a single step are welcome
through the repository's Issues section. No individual reviewer has been
contacted or is presented as endorsing this work.

## Version lineage and rights

Previous version: https://doi.org/10.5281/zenodo.23258648

Concept DOI: https://doi.org/10.5281/zenodo.23209552

Repository: https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre

Licence: custom DEL1.1, within the scope described in `LICENSE_SCOPE.txt`;
historical and third-party rights are preserved. AI assistance and scientific
limits must remain explicit.

The DOI above is reserved in the Zenodo draft. The exact tagged content
commit remains unassigned and must be recorded only after GitHub has
actually created it. A separate verified receipt must attest publication.
