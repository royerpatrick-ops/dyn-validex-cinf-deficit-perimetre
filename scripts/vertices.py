"""Contrôle local sur les sommets; SE MC seule, queue asymptotique non certifiée."""
import argparse
import numpy as np
from scipy.integrate import quad
from numerical_tools import simpson_mc, write_json


def P2(r, a):
    return float(np.clip(2*r/a-1, 0, 1))


def p_exact(a):
    if a == 0:
        return 1.
    if not 0 < a <= 2:
        raise ValueError("La formule locale exige 0<a<=2.")
    def f(d):
        return P2(np.sqrt(2*d), a)+(1-min(1., 2*np.sqrt(2*d)/a))*P2(np.sqrt(2*(d+1/a)), a)
    pts = sorted({0., min(a*a/8, 1/a), 1/a} | {x for x in (a*a/2, a*a/2-1/a, a*a/8-1/a) if 0 < x < 1/a})
    return a*sum(quad(f, left, right, epsabs=1e-11, epsrel=1e-11)[0] for left, right in zip(pts[:-1], pts[1:]))


def local_JV02():
    return quad(lambda a: a*p_exact(a), 0, 2, points=[.5, 1, 2**(1/3), 1.5], epsabs=1e-10, epsrel=1e-10)


def p_mc(a, n=20_000, seed=11):
    if a <= 0 or n < 2:
        raise ValueError("a>0 et n>=2 requis.")
    rng = np.random.default_rng(seed)
    de, s, be = rng.uniform(0, 1/a, n), rng.uniform(0, a, n), rng.uniform(0, a, n)
    two, idx, k = np.zeros(n), np.arange(n), 0
    while idx.size:
        d, off = de[idx]+k/a, s[idx]+k*be[idx]
        L = np.sqrt(2*d)
        x1, x2 = off+a*np.ceil((-L-off)/a), off+a*np.floor((L-off)/a)
        occ = x1 <= x2+1e-12
        two[idx[occ]] = (x2-x1 > a/2)[occ]
        idx = idx[~occ]
        k += 1
    return float(two.mean()), float(two.std(ddof=1)/np.sqrt(n))


def run(n=20_000, points=21, seed=50, replicates=1, checks=False):
    if n < 2 or points < 3 or points % 2 != 1 or replicates < 1:
        raise ValueError("n>=2, points impair>=3, replicates>=1 requis.")
    grid = np.linspace(2, 4, points)
    rows = []
    for i, a in enumerate(grid):
        pairs = [p_mc(a, n, seed+1000*j+i) for j in range(replicates)]
        m = np.mean([v[0] for v in pairs])
        se = np.linalg.norm([v[1] for v in pairs])/replicates
        rows.append(dict(a=float(a), ap=float(a*m), ap_mc_se=float(a*se), seeds=[seed+1000*j+i for j in range(replicates)]))
    J02, quad_err = local_JV02()
    J24, J24se, weights = simpson_mc(grid, [r["ap"] for r in rows], [r["ap_mc_se"] for r in rows])
    tail = (8/3)/(4*4**4)
    result = dict(schema="dyn-cinf-vertices-v0.2", status="MODEL_CHECK_NOT_CERTIFIED", rows=rows,
                  n_per_point_per_replicate=n, replicates=replicates, J_local_02=float(J02),
                  local_quad_error_estimate_NOT_BOUND=float(quad_err), J_mc_2_4=J24,
                  J_mc_2_4_se_MC_ONLY=J24se, simpson_weights=weights,
                  tail_model="a*p(a)~8/(3*a^5)", tail_4_infinity_model_estimate=tail,
                  tail_error="not bounded; continuation not certified",
                  coefficient_model_conditional=float(12/np.pi*(J02+J24+tail)),
                  coefficient_se_MC_ONLY=float(12/np.pi*J24se),
                  uncertainty_statement="SE MC seule; erreur quadrature et queue exclues, aucun IC global.",
                  comparison_Balog_Deshouillers_value=3.4536898915)
    if checks:
        result["asymptote_checks"] = [dict(a=a, p_mc=p_mc(a, n, int(a*100)), ap_asymptote=8/(3*a**5)) for a in (5., 6., 7.)]
    return result


def main(argv=None, default_replicates=1):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, default=20_000)
    p.add_argument("--points", type=int, default=21)
    p.add_argument("--seed", type=int, default=50)
    p.add_argument("--replicates", type=int, default=default_replicates)
    p.add_argument("--checks", action="store_true")
    p.add_argument("--output", default="vertices.json")
    a = p.parse_args(argv)
    result = run(a.n, a.points, a.seed, a.replicates, a.checks)
    result["configuration"] = vars(a)
    write_json(a.output, result)
    print("Coefficient conditionnel:", result["coefficient_model_conditional"], "; SE MC seule:", result["coefficient_se_MC_ONLY"])
    print("Queue au-delà de 4 non certifiée; erreur quadrature non bornée.")
    return result


if __name__ == "__main__":
    main()
