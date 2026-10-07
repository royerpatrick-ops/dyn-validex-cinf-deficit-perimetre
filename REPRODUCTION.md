# Reproduction and verification

These instructions separate documentary reproduction from optional numerical checks. The publication process itself did not rerun scientific computations, Monte Carlo campaigns, P2 campaigns or RNG flows.

## Rebuild the manuscript

With a LaTeX installation, from the repository root:

```powershell
pdflatex -output-directory=manuscript manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.tex
```

The published PDF is the supplied corrective PDF. Rebuilding may change PDF metadata, compression or embedded credentials even when the typeset pages are visually identical.

## Inspect the script interface

Read [`scripts/README.md`](scripts/README.md) before running anything. It documents dependencies, frugal examples, explicit model choices and the limits of every output. The requirements are in `scripts/requirements.txt`.

The stored records report 10/10 targeted corrective checks and 7/7 reduced CLI sanity commands as passing. These are technical checks with finite-precision or synthetic fixtures. They are not a mathematical proof, a certified enclosure or reproduction of the missing historical data campaign.

## Missing inputs

- `reanalysis_92_points.csv` was not supplied. The 69-point historical fits were therefore not rerun.
- The historical Arb certification program was not supplied. No Arb certification was reissued or extended.
- Long-run raw outputs and a complete covariance reconstruction were not supplied.

## Integrity

The original corrective ZIP is preserved in `archive/` and its package manifest is preserved alongside it. The two source pieces received with the corrective are preserved byte for byte in `originals/`; their preservation receipt is in `evidence/originals_preservation.json`.

No certificate, frozen ledger or historical file is modified by these instructions.
