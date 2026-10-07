"""Valeur de coupure conjecturale; Z_prim(3/4) par PROLONGEMENT ANALYTIQUE.

La série primitive définissant Z_prim(s) converge pour Re(s)>1 seulement.
Au point s=3/4 on évalue 4*zeta(s)*beta(s)/zeta(2*s) prolongé.
La valeur négative ne représente pas la somme d'une série positive convergente.
"""
import argparse
import math
import numpy as np
from scipy.special import bernoulli, poch
from scipy.integrate import quad
from numerical_tools import write_json


def hurwitz_em(s, q=1., terms=128, corrections=8):
    """Euler–Maclaurin en double précision, évaluation non certifiée."""
    if s == 1 or q <= 0:
        raise ValueError("pôle s=1 ou q<=0.")
    a = terms+q
    value = float(np.sum((np.arange(terms)+q)**(-s)))+a**(1-s)/(s-1)+.5*a**(-s)
    B = bernoulli(2*corrections)
    for k in range(1, corrections+1):
        value += B[2*k]/math.factorial(2*k)*poch(s, 2*k-1)*a**(-s-2*k+1)
    return float(value)


def calculation(terms=128):
    s = .75
    zs = hurwitz_em(s, terms=terms)
    beta = 4**(-s)*(hurwitz_em(s, .25, terms)-hurwitz_em(s, .75, terms))
    zp = 4*zs*beta/hurwitz_em(2*s, terms=terms)
    # Changement d'ordre de la double intégrale de c0 : intégrande (1-B²)/(4√B).
    integral = quad(lambda B: (1-B*B)/(4*np.sqrt(B)), 0, 1, epsabs=1e-12)[0]
    c0_quad = np.sqrt(2)/12*integral
    c0 = np.sqrt(2)/30
    return dict(s=s, series_convergence_domain="Re(s)>1", evaluation_at_s="analytic continuation",
                method="Euler–Maclaurin double precision; not interval-certified", terms=terms,
                c0_closed_form=float(c0), c0_quadrature_check=float(c0_quad),
                zeta_s=zs, beta_s=beta, Z_prim_analytic_continuation=zp,
                B_cut_conjectural=float(-c0/np.pi*zp),
                interpretation="Nombre conjectural de mécanisme de coupure; aucun second terme démontré ni complément nécessaire établi.")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--terms", type=int, default=128)
    p.add_argument("--output", default="zeta_b.json")
    args = p.parse_args(argv)
    if args.terms < 16:
        p.error("--terms>=16 requis.")
    result = calculation(args.terms)
    result["schema"] = "dyn-cinf-cutoff-v0.2"
    result["status"] = "CONJECTURAL_MECHANISM_NOT_CERTIFIED"
    write_json(args.output, result)
    print("Z_prim(3/4), prolongement analytique =", result["Z_prim_analytic_continuation"])
    print("B_cut conjectural =", result["B_cut_conjectural"], "; aucune série convergente à s=3/4.")
    return result


if __name__ == "__main__":
    main()
