"""Estimation de aG(a) par importance sampling; erreurs Monte-Carlo seules."""
import argparse
import numpy as np
from numerical_tools import write_json


def G_is(a, n, seed, p_unif=.25, sig_fac=4., max_ranks=None):
    if a <= 0 or n < 2 or not 0 < p_unif <= 1 or sig_fac <= 0:
        raise ValueError("a>0, n>=2, 0<p_unif<=1, sig_fac>0 requis.")
    rng = np.random.default_rng(seed)
    sig, half = sig_fac/a**2, a/2
    Zc = (2/np.pi)*np.arctan(half/sig)
    unif = rng.random(n) < p_unif
    b = np.empty(n)
    b[unif] = rng.uniform(-half, half, unif.sum())
    m, out = int((~unif).sum()), np.empty(0)
    while out.size < m:
        c = sig*np.tan(np.pi*(rng.random(2*m)-.5))
        out = np.concatenate([out, c[np.abs(c) <= half]])
    b[~unif] = out[:m]
    q = p_unif/a + (1-p_unif)/(np.pi*sig*(1+(b/sig)**2))/Zc
    w, be = (1/a)/q, np.mod(b, a)
    de, s = rng.uniform(0, 1/a, n), rng.uniform(0, a, n)
    cc, idx, k = np.zeros(n), np.arange(n), 0
    limit = int(np.ceil(a**3/8))+3 if max_ranks is None else max_ranks
    while idx.size:
        if k >= limit:
            raise RuntimeError("Limite de rangs atteinte : aucun résultat partiel exporté.")
        d, off = de[idx]+k/a, s[idx]+k*be[idx]
        L = np.sqrt(2*d)
        x1, x2 = off+a*np.ceil((-L-off)/a), off+a*np.floor((L-off)/a)
        occ = x1 <= x2+1e-12
        cc[idx[occ]] = (d*(x2-x1)-(x2**3-x1**3)/3)[occ]
        idx = idx[~occ]
        k += 1
    values = cc*w
    return float(values.mean()), float(values.std(ddof=1)/np.sqrt(n)), k


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", default="tail_is.json")
    p.add_argument("--n", type=int, default=200_000, help="défaut frugal jusqu'à a=12; événements rares")
    p.add_argument("--a-min", type=float, default=3.6)
    p.add_argument("--a-max", type=float, default=12.)
    p.add_argument("--points", type=int, default=9)
    p.add_argument("--seed", type=int, default=500)
    p.add_argument("--p-unif", type=float, default=.25)
    p.add_argument("--sig-fac", type=float, default=4.)
    p.add_argument("--max-ranks", type=int)
    p.add_argument("--check", action="store_true", help="deux points 3 et 5 seulement")
    a = p.parse_args(argv)
    if not a.a_max > a.a_min > 0 or a.points < 2 or a.n < 2:
        p.error("a_max>a_min>0, points>=2 et n>=2 requis.")
    grid = [3., 5.] if a.check else np.geomspace(a.a_min, a.a_max, a.points)
    rows = []
    for i, x in enumerate(grid):
        m, se, ranks = G_is(float(x), a.n, a.seed+i, a.p_unif, a.sig_fac, a.max_ranks)
        row = dict(a=float(x), aG=float(x*m), aG_mc_se=float(x*se), n=a.n, seed=a.seed+i, ranks=ranks,
                   variance_resolution="EMPIRICAL_ONLY" if se > 0 else "ZERO_EVENT_VARIANCE_UNRESOLVED")
        rows.append(row)
        print(f"a={x:.6g}; aG={x*m:.7g}; SE_MC_only={x*se:.3g}; ranks={ranks}", flush=True)
    unresolved = any(r["aG_mc_se"] == 0 for r in rows)
    out = dict(schema="dyn-cinf-tail-is-v0.2", status="ZERO_EVENT_VARIANCE_UNRESOLVED" if unresolved else "NUMERICAL_ESTIMATE_NOT_CERTIFIED",
               quantity="aG(a)", distribution="uniform + truncated Cauchy, importance weights",
               rng="numpy.default_rng", configuration=vars(a), rows=rows,
               uncertainty_statement="SE empirique de cc*w, MC seule; elle ne borne pas l'erreur globale ni l'extrapolation. Un SE nul sur zéro événement ne prouve pas une variance nulle.",
               integral="not computed", continuation_beyond_last_point="not certified")
    write_json(a.output, out)
    if unresolved:
        print("Zéro événement/SE=0 à au moins un point : variance non résolue; augmenter n ou réduire a_max avant un fit.")
    return out


if __name__ == "__main__":
    main()
