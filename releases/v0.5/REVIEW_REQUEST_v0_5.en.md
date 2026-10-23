# Request for human mathematical review: an explicit remainder bound for the disk perimeter deficit

We invite critical mathematical review of a proposed proof and its quantitative supplement, developed within Patrick Royer’s Dynagénèse project. Patrick Royer is an independent, unaffiliated researcher.

Let $D_R$ be the closed disk of radius $R$, and let $t$ be uniformly distributed in $[0,1)^2$. The observable is

$$
m(R)=\mathbb E_t\left[2\pi R-P\left(\mathrm{conv}(D_R\cap(\mathbb Z^2+t))\right)\right].
$$

The dossier proposes an expansion

$$
m(R)=2\pi(CR^{-1/3}-BR^{-1/2})+r(R),
$$

where $C=\mu(\Psi)$ is the Haar mean of a translation-averaged parabolic first-depth observable, and $B=-\sqrt2\,Z_{\mathrm{prim}}(3/2)/(6\pi)$. Here $Z_{\mathrm{prim}}(3/2)$ denotes analytic continuation, rather than the divergent positive primitive-vector sum at that exponent.

The supplement proposes, for every $R\ge2$,

$$
|r(R)|\le2\pi\left[2.5\times10^9\left(1+\frac{\log R}{3}\right)R^{-11/21}+2000R^{-7/12}\right]+550000R^{-4/3}.
$$

**Status: a proposed proof developed and counter-checked with AI assistance. No independent human mathematical review or formal proof verification is attested.** The reproducible arithmetic checks concern evaluation of the bound; they are not a computer verification of the mathematical proof.

The bound is deliberately very conservative and uninformative at the radii already computed, including 50 and 1600. The proposed threshold $R_0=2$ concerns validity of this bound, rather than observable onset of the asymptotic regime. It does not enable numerical validation of $C$ or $B$ at those radii.

We particularly seek feedback on three points:

1. **Geometric identities.** Do the exact row-competition and short-chord correction formulas, their extensions to the axes, and their derivative estimates establish the claimed global regularity of $\Psi-E_g$ and the transfer to the disk?
2. **Quantitative analytic chain.** Do Stieltjes summation, the primitive and spectral normalizations, and heat smoothing justify the three stated bounds? An explicit $C^2$ cutoff replaces the abstract smooth cutoff of the initial proof in this supplement.
3. **A potentially useful bound.** Could an estimate tailored to this observable substantially reduce the losses from global norms and the circular-average estimate?

A localized objection, counterexample, relevant reference, or correction to a single step would already be valuable. We are not seeking a general endorsement of the project.

The accompanying dossier contains the nine-page note, the starting manuscript, detailed derivations, the AI counter-review, LaTeX sources, and a reproducible rational-arithmetic calculation. No new Monte Carlo experiment was used for this supplement.

Feedback / retours : https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/issues
