"""Recalcul des constantes de la composante singuliere, a 80 decimales.

Dependances : mpmath ; numpy (version renseignee pour la tracabilite).
Utilisation : python RECALCUL_CONSTANTES.py
Ecrit CONSTANTES_HAUTE_PRECISION.json a cote de ce fichier.
Evaluation haute precision : aucun certificat d'intervalles.
"""
import json
from pathlib import Path
import sys

import mpmath as m
import numpy as np


def main():
    m.mp.dps = 80
    sigma = m.mpf(3) / 2
    z_primitive = (
        4 * m.zeta(sigma / 2)
        * m.dirichlet(sigma / 2, [0, 1, 0, -1])
        / m.zeta(sigma)
    )
    mellin_integral = m.pi * z_primitive / 5
    b_small = -(2 * m.sqrt(2) / (15 * m.pi)) * z_primitive
    b_large = (
        -(6 / m.pi**2) * (m.mpf(1) / 9)
        * (m.sqrt(2) / 4) * mellin_integral
    )
    b_singular = -m.sqrt(2) / (6 * m.pi) * z_primitive
    results = {
        "schema": "DYN-SECOND-TERME-CONSTANTES-HAUTE-PRECISION-v0.1",
        "python_version": sys.version,
        "numpy_version": np.__version__,
        "mpmath_version": m.__version__,
        "mpmath_module_path": m.__file__,
        "mpmath_dps": m.mp.dps,
        "arithmetic_status": "HIGH_PRECISION_EVALUATION_NOT_INTERVAL_CERTIFICATE",
        "Z_primitive_regularized_3_2": m.nstr(z_primitive, 80),
        "B_small_from_Z": m.nstr(b_small, 80),
        "B_large_from_Mellin_I": m.nstr(b_large, 80),
        "B_total_singular_from_Z": m.nstr(b_singular, 80),
        "B_sum": m.nstr(b_small + b_large, 80),
        "rho_Mellin_integral_target": m.nstr(mellin_integral, 80),
        "difference_Bsum_B": m.nstr(b_small + b_large - b_singular, 20),
        "difference_Blarge_Bsmall_over4": m.nstr(b_large - b_small / 4, 20),
        "scope": (
            "Z_primitive(3/2) is evaluated by analytic continuation; the positive "
            "primitive-vector series diverges. B is the singular contribution, "
            "not an unconditional identification of the complete second term."
        ),
    }
    output_path = Path(__file__).resolve().with_name("CONSTANTES_HAUTE_PRECISION.json")
    output_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(results, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
