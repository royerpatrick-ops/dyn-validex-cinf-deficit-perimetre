"""Simulation indépendante : déficit de périmètre de conv(L ∩ R·D), L = rotation(θ)·Z² + translation uniforme.
C_eff = E[2πR − P_hull]·R^{1/3}/(2π)."""
import numpy as np, argparse, math
from numerical_tools import write_json
def hull_perimeter(px, py):
    o = np.lexsort((py, px)); P = np.column_stack((px[o], py[o]))
    def chain(pts):
        h = []
        for p in pts:
            while len(h) >= 2 and (h[-1][0]-h[-2][0])*(p[1]-h[-2][1]) - (h[-1][1]-h[-2][1])*(p[0]-h[-2][0]) <= 0:
                h.pop()
            h.append(tuple(p))
        return h
    lo = chain(P); up = chain(P[::-1]); H = np.array(lo[:-1] + up[:-1])
    return np.sum(np.hypot(*(np.roll(H, -1, 0) - H).T))
def one(R, rng):
    th = rng.uniform(0, np.pi/2); u, v = rng.random(2)
    c, s = math.cos(th), math.sin(th)
    # point du réseau : p = rot(θ)·(m+u, n+v). On balaie m ; pour chaque m, les n admissibles forment un intervalle.
    M = int(math.ceil(R)) + 2
    m = np.arange(-M, M+1) + u
    # |rot·(m, y)|² = m² + y² ≤ R²  (rotation isométrique) → y ∈ [-√(R²-m²), √(R²-m²)], y = n+v
    rad2 = R*R - m*m; ok = rad2 >= 0; m = m[ok]; r = np.sqrt(rad2[ok])
    nlo = np.ceil(-r - v); nhi = np.floor(r - v); ok = nlo <= nhi
    m, nlo, nhi = m[ok], nlo[ok] + v, nhi[ok] + v
    X = np.concatenate([m, m]); Y = np.concatenate([nlo, nhi])
    px, py = c*X - s*Y, s*X + c*Y
    return 2*np.pi*R - hull_perimeter(px, py)
def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--radii", type=float, nargs="+", default=[1230.])
    p.add_argument("--n", type=int, default=20, help="tirages par rayon (défaut frugal)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", default="hull_disc.json")
    args = p.parse_args(argv)
    if args.n < 2 or any(R < 2 for R in args.radii):
        p.error("n>=2 et rayons>=2 requis.")
    rng = np.random.default_rng(args.seed)
    rows = []
    for R in args.radii:
        vals = np.array([one(R, rng) for _ in range(args.n)])*R**(1/3)/(2*np.pi)
        rows.append(dict(R=R, n=args.n, C_eff=float(vals.mean()), C_eff_se_MC_ONLY=float(vals.std(ddof=1)/np.sqrt(args.n))))
        print(rows[-1], flush=True)
    result = dict(schema="dyn-cinf-hull-disc-v0.2", status="FINITE_RADIUS_MC_NOT_ASYMPTOTIC_PROOF",
                  configuration=vars(args), rows=rows,
                  uncertainty_statement="SE Monte-Carlo seule en double précision; aucune certification numérique ou asymptotique.")
    write_json(args.output, result)
    return result


if __name__ == "__main__":
    main()
