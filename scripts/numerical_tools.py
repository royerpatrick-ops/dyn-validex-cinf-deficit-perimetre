"""Utilitaires numériques en double précision : aucune arithmétique d'intervalles."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad


def simpson_weights(grid):
    """Poids de Simpson composite; grille uniforme, nombre de points impair."""
    x = np.asarray(grid, dtype=float)
    if x.ndim != 1 or len(x) < 3 or len(x) % 2 != 1:
        raise ValueError("Simpson requiert au moins 3 points, en nombre impair.")
    h = np.diff(x)
    if h[0] <= 0 or not np.allclose(h, h[0], rtol=1e-10, atol=1e-13):
        raise ValueError("La grille doit être strictement croissante et uniforme.")
    w = np.full(len(x), 2.0)
    w[1:-1:2] = 4.0
    w[0] = w[-1] = 1.0
    return w * h[0] / 3.0


def simpson_mc(grid, values, standard_errors):
    """SE de la somme pondérée, sous indépendance des tirages par point."""
    w = simpson_weights(grid)
    y, se = np.asarray(values), np.asarray(standard_errors)
    if y.shape != w.shape or se.shape != w.shape or np.any(se < 0):
        raise ValueError("Valeurs/SE invalides pour la grille.")
    return float(w @ y), float(np.linalg.norm(w * se)), w.tolist()


def write_json(path, data):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def primitive_h_times_r(r, a):
    return (2*r**5/5 + 3*a*r**4/4 - 4*a*a*r**3/3 + a**3*r*r/2) / 6


def Hm_float(d, a):
    r = np.sqrt(2*d)
    if r < a/2:
        return 0.0
    return (2*r-a)*(r*r+2*a*r-a*a)/6


def G_exact(a):
    """Formule locale du manuscrit sur 0<a<=2, évaluée en double précision."""
    a = float(a)
    if not 0 < a <= 2:
        raise ValueError("La formule locale de G exige 0 < a <= 2.")
    g0 = a*(primitive_h_times_r(np.sqrt(2/a), a)-primitive_h_times_r(a/2, a))
    # d=a²t²/2 régularise le deuxième terme de la formule du pont.
    g1 = a**3*quad(lambda t: t*(1-2*t)*Hm_float(a*a*t*t/2+1/a, a), 0, .5,
                    epsabs=1e-12, epsrel=1e-11)[0]
    return g0+g1


def local_J02():
    # a=u² : l'intégrande possède une limite finie en u=0.
    def integrand(u):
        return 2**3.5/15 if u == 0 else 2*u**3*G_exact(u*u)
    value, error_estimate = quad(integrand, 0, np.sqrt(2), epsabs=2e-11,
                                  epsrel=2e-11, points=[.5, 1, 2**(1/6)])
    return float(value), float(error_estimate)


def G_mc(a, n=20_000, seed=1, max_ranks=None):
    """Première rangée occupée du modèle local; SE empirique Monte-Carlo."""
    if a <= 0 or n < 2:
        raise ValueError("a > 0 et n >= 2 sont requis.")
    rng = np.random.default_rng(seed)
    de, s, be = rng.uniform(0, 1/a, n), rng.uniform(0, a, n), rng.uniform(0, a, n)
    cc, done, k = np.zeros(n), np.zeros(n, bool), 0
    limit = int(np.ceil(a**3/8))+3 if max_ranks is None else max_ranks
    while not done.all():
        if k >= limit:
            raise RuntimeError("Limite de rangs atteinte : aucun résultat partiel n'est exporté.")
        d, off = de+k/a, s+k*be
        L = np.sqrt(2*d)
        x1 = off+a*np.ceil((-L-off)/a)
        x2 = off+a*np.floor((L-off)/a)
        occ = (x1 <= x2+1e-12) & ~done
        cc[occ] = (d*(x2-x1)-(x2**3-x1**3)/3)[occ]
        done |= occ
        k += 1
    return float(cc.mean()), float(cc.std(ddof=1)/np.sqrt(n)), k
