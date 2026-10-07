"""Intégrale TRONQUÉE J_[0,3.6]; ce script ne calcule pas C_inf complet."""
import argparse
import numpy as np
from scipy.integrate import quad
from numerical_tools import G_exact, G_mc, local_J02, simpson_mc, write_json


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, default=20_000, help="tirages indépendants par point (défaut frugal)")
    p.add_argument("--points", type=int, default=17, help="nombre impair de points sur [2,3.6]")
    p.add_argument("--seed", type=int, default=100)
    p.add_argument("--checks", action="store_true", help="contrôles MC locaux facultatifs")
    p.add_argument("--output", default="cinf_truncated.json")
    args = p.parse_args(argv)
    if args.n < 2 or args.points < 3 or args.points % 2 != 1:
        p.error("--n >= 2 et --points impair >= 3 requis.")
    checks = []
    if args.checks:
        for a in (.3, .7, 1.5, 2.):
            m, se, k = G_mc(a, args.n, 1)
            row = dict(a=a, G_local_formula=G_exact(a), G_mc=m, G_mc_se=se, ranks=k)
            checks.append(row)
            print(row)
    J02, quad_error = local_J02()
    J12, quad_error12 = quad(lambda a: a*G_exact(a), 1, 2, epsabs=2e-11, epsrel=2e-11)
    grid = np.linspace(2, 3.6, args.points)
    rows = []
    for i, a in enumerate(grid):
        m, se, k = G_mc(a, args.n, args.seed+i)
        rows.append(dict(a=float(a), aG=float(a*m), aG_mc_se=float(a*se), n=args.n, seed=args.seed+i, ranks=k))
    Jtail, Jtail_se, weights = simpson_mc(grid, [r["aG"] for r in rows], [r["aG_mc_se"] for r in rows])
    J = J02+Jtail
    out = dict(schema="dyn-cinf-truncated-v0.2", status="NUMERICAL_ESTIMATE_NOT_CERTIFIED",
               domain=[0, 3.6], local_formula_domain=[0, 2], J_local_02=J02,
               J_local_12=float(J12), local_quad_error_estimate_NOT_BOUND=quad_error,
               local_12_quad_error_estimate_NOT_BOUND=float(quad_error12),
               J_mc_2_3_6=Jtail, J_mc_2_3_6_se_MC_ONLY=Jtail_se,
               J_truncated_0_3_6=J, J_truncated_se_MC_ONLY=Jtail_se,
               coefficient_truncated_6_over_pi2=float(6/np.pi**2*J),
               coefficient_truncated_se_MC_ONLY=float(6/np.pi**2*Jtail_se),
               integration="composite Simpson", simpson_weights=weights,
               quadrature_discretization_error="not bounded", missing_tail=[3.6, "infinity"],
               uncertainty_statement="SE MC seule, tirages indépendants par point; aucune borne globale ni IC global.",
               configuration=vars(args), checks=checks, rows=rows)
    write_json(args.output, out)
    print(f"J_truncated_[0,3.6] = {J:.9g}; SE_MC_only = {Jtail_se:.3g}")
    print(f"Coefficient tronqué (6/pi²)J = {6/np.pi**2*J:.9g}; queue a>3.6 absente.")
    print("Erreur de quadrature non bornée; résultat non certifié.")
    return out


if __name__ == "__main__":
    main()
