# DYN-VALIDEX — Perimeter deficit of randomized integer convex hulls

Patrick Royer, independent researcher without institutional affiliation,
Dynagénèse project. Mathematical developments, counter-checks and integration
were carried out with AI assistance. No independent human mathematical review
or formal proof verification is attested for the proposed proof and this supplement.

## Candidate v0.5: explicit disk remainder bounds

**Staging status: `RELEASE_CANDIDATE_DOI_RESERVED`, 23 October 2026.**

Reserved DOI for v0.5: https://doi.org/10.5281/zenodo.23598602

This DOI has been reserved in the existing Zenodo series. Publication and a
new tagged content commit are not yet attested in this staging document.

The quantitative note v0.1a proposes explicit bounds
$K_f=2.5\times10^9$, $K_E=2000$, $K_{\mathrm{geo}}=550000$, with a common
validity threshold $R_0=2$, for the remainder of the proposed two-term disk
perimeter-deficit expansion.

**The bound is very conservative and uninformative at the radii already
studied.** The threshold is a validity threshold, not a practical onset of
the asymptotic regime. These bounds do not numerically validate the two
coefficients at those radii. C51 remains partial; a complete certified mean
at R=50 is not claimed.

- [Nine-page quantitative note, PDF](releases/v0.5/DYN-CHIFFRAGE_RESTE_I43_DISQUE_v0_1a.pdf)
- [Complete source and review dossier](releases/v0.5/DYN-PUBLICATION_CHIFFRAGE_RESTE_I43_v0_5.zip)
- [Release notes](releases/v0.5/RELEASE_NOTES_v0_5.md)
- [Version provenance](releases/v0.5/PROVENANCE_v0_5.json)
- [SHA-256 checksums](releases/v0.5/SHA256SUMS_v0_5.txt)

The archive contains the proposed starting proof, the quantitative derivations,
the separate AI counter-review, LaTeX sources, figures and a reproducible
rational-arithmetic calculation. It includes no new Monte-Carlo or QMC campaign.

## Human mathematical review requested

- [Request in English](releases/v0.5/REVIEW_REQUEST_v0_5.en.md)
- [Appel en français](releases/v0.5/REVIEW_REQUEST_v0_5.fr.md)

Localized objections, counterexamples, relevant references and corrections
to a single step are welcome through [Issues](https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/issues). The priority is
review of the exact geometric identities, the quantitative Stieltjes/heat
chain, and estimates that could make the remainder bound useful.
No individual reviewer or endorsement is claimed.

## Version history

- v0.5: current quantitative supplement candidate; internal note v0.1a.
- [v0.4 proposed proof corpus](https://doi.org/10.5281/zenodo.23258648)
- [v0.3 historical record](https://doi.org/10.5281/zenodo.23238780)
- [v0.2 historical record](https://doi.org/10.5281/zenodo.23209553)
- [Zenodo concept DOI](https://doi.org/10.5281/zenodo.23209552)

Historical tags, release assets, source attribution and scientific limits
retain their original scope. The supplement does not resolve the separate
Weyl bridge.

## Licence and citation

The new supplement is distributed under the custom DEL 1.1 licence within
the rights held by Patrick Royer. See the [scope notice](releases/v0.5/LICENSE_SCOPE_v0_5.txt)
and the operative, unchanged licence PDF included in the archive. Historical
and third-party rights remain separate. No exclusive rights over mathematical
facts are claimed, and DEL 1.1 is not represented as OSI-approved.

See [CITATION.cff](CITATION.cff). The reserved DOI must not be taken as
attestation of publication; citation and public status should be completed
from the verified publication record once available.
