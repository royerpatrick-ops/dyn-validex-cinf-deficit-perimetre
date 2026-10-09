"""Contrôles numériques de la note du 9 octobre 2026 (second terme).
1. Forme close de B et identité B_grands = B_petits / 4.
2. Identité de Mellin : int_0^inf lam^(-3/2) (rho(lam) - 1) dlam = (pi/5) Z_prim(3/2).
3. Modèle des droites dans la pointe : Psi (Monte-Carlo, vrais réseaux) contre F(x, y),
   et intégrale transverse sqrt(x) * Phi(x) = sqrt(2)/3.
4. Lemme d'Epstein avec coupure lisse : somme - intégrale -> Z_prim(3/2).
Dépendances : numpy, mpmath. Durée : quelques secondes.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30
# ---------- 1. Forme close de B ----------
z34 = mp.zeta(mp.mpf(3) / 4)
b34 = mp.dirichlet(mp.mpf(3) / 4, [0, 1, 0, -1])      # beta de Dirichlet
z32 = mp.zeta(mp.mpf(3) / 2)
Zp = 4 * z34 * b34 / z32                                # Z_prim(3/2), régularisé
g0 = 4 * mp.sqrt(2) / 15
B_pet = g0 * abs(Zp) / (2 * mp.pi)
B_gr = B_pet / 4
B = mp.sqrt(2) / (6 * mp.pi) * abs(Zp)
print("zeta(3/4) =", mp.nstr(z34, 12), " beta(3/4) =", mp.nstr(b34, 12))
print("Z_prim(3/2) =", mp.nstr(Zp, 12))
print("B_petits =", mp.nstr(B_pet, 10), " B_grands = B_petits/4 =", mp.nstr(B_gr, 10))
print("B (forme close) =", mp.nstr(B, 12), "  somme =", mp.nstr(B_pet + B_gr, 12))
print("(pi/5) Z_prim(3/2) =", mp.nstr(mp.pi / 5 * Zp, 10))

# ---------- 2. Identité de Mellin pour rho ----------
# rho(lam) = (pi lam / 8) sum_{v prim, |v| < 1/lam} (1 - lam^2 |v|^2) / |v|
Lmax = 2000
norms = []
for m in range(1, Lmax + 1):                            # quadrant m >= 1, n >= 0 (x4)
    n = np.arange(0, Lmax + 1)
    r = np.hypot(m, n)
    keep = (np.gcd(m, n) == 1) & (r < Lmax)
    norms.append(r[keep])
r = np.sort(np.concatenate(norms))
Sm1 = np.concatenate([[0.0], np.cumsum(4 / r)])
S1 = np.concatenate([[0.0], np.cumsum(4 * r)])

def rho_of_L(L):                                        # L = 1/lam
    k = np.searchsorted(r, L, side="left")
    return (np.pi / (8 * L)) * (Sm1[k] - S1[k] / L**2)

# int_0^1 lam^(-3/2)(rho-1) dlam = int_1^inf L^(-1/2)(rho(1/L)-1) dL ; plus int_1^inf (-lam^(-3/2)) = -2
Ls = np.linspace(1.0, Lmax * 0.999, 4_000_001)
vals = Ls ** -0.5 * (rho_of_L(Ls) - 1)
I = np.trapezoid(vals, Ls) - 2
print(f"int lam^(-3/2)(rho-1) (|v| < {Lmax}) = {I:.5f}   attendu {float(mp.pi/5*Zp):.5f}")

# ---------- 3. Modèle des droites ----------
def F_line(x, y):
    x, y = abs(x), abs(y)
    if y * y <= x / 2:
        tau = y / (np.sqrt(2) * x)
        return 1 / (2 * x) - (4 / 3) * tau / np.sqrt(x) + tau**2
    return 1 / (24 * y * y)

def psi_mc(x, y, nsamp, rng, b=None):
    """E_t[Z*] pour le réseau de base v=(x,y), u = v_perp/|v|^2 + b v (det 1), translaté de t."""
    l = np.hypot(x, y)
    upx, upy = -y / l**2, x / l**2
    nx, ny = -y / l, x / l
    bb = rng.random(nsamp) if b is None else np.full(nsamp, b)
    ux, uy = upx + bb * x, upy + bb * y
    ta, tb = rng.random(nsamp), rng.random(nsamp)
    tx, ty = ta * x + tb * ux, ta * y + tb * uy
    Zmax = 6 * F_line(x, y) + 20
    S = (abs(y) * np.sqrt(2 * Zmax) + abs(x) * Zmax) / l
    s0 = tx * nx + ty * ny
    nlo = int(np.floor(((-S - s0) * l).min())) - 1
    nhi = int(np.ceil(((S - s0) * l).max())) + 1
    best = np.full(nsamp, np.inf)
    a = -x * x / 2
    for k in range(nlo, nhi + 1):
        Qx, Qy = k * ux + tx, k * uy + ty
        bq = y - Qx * x
        c = Qy - Qx * Qx / 2
        disc = bq * bq - 4 * a * c
        ok = disc >= 0
        sq = np.sqrt(np.where(ok, disc, 0.0))
        q = -0.5 * (bq + np.where(bq >= 0, sq, -sq))
        q = np.where(q == 0, 1e-300, q)
        r1, r2 = q / a, c / q
        lo, hi = np.ceil(np.minimum(r1, r2)), np.floor(np.maximum(r1, r2))
        ok &= lo <= hi
        m = lo if y >= 0 else hi
        Y = Qy + m * y
        best = np.where(ok & (Y < best), Y, best)
    assert np.all(best < Zmax), "Zmax trop petit"
    return best.mean(), best.std() / np.sqrt(nsamp)

rng = np.random.default_rng(20261009)
print("\n   x      y/sqrt(x/2)   Psi (MC)             F (droites)   (Psi-F)/|v|        |y|/(2|v|)")
for x in (0.04, 0.01, 0.0025):
    for cc in (0.0, 0.5, 1.0, 2.0, 4.0):
        y = cc * np.sqrt(x / 2)
        m, e = psi_mc(x, y, 400_000, rng)
        f = F_line(x, y)
        l = np.hypot(x, y)
        print(f"{x:8.4f}   {cc:4.1f}   {m:10.4f} ± {e:7.4f}   {f:10.4f}   "
              f"{(m - f) / l:+.3f} ± {e / l:.3f}   {abs(y) / (2 * l):.3f}")
# indépendance vis-à-vis du décalage des rangées (paramètre b)
x, y = 0.01, np.sqrt(0.005)
print("\nb fixé (x = 0.01, transition) :",
      [round(psi_mc(x, y, 400_000, rng, b=bf)[0], 3) for bf in (0.0, 0.37, 0.81)],
      " F =", round(F_line(x, y), 3))

# intégrale de F en y : Phi(x) * sqrt(x) = sqrt(2)/3 (quadrature avec point de raccord)
for x in (0.04, 0.01, 0.0025, 1e-6):
    xm = mp.mpf(x)
    yc = mp.sqrt(xm / 2)
    Phi = 2 * (mp.quad(lambda yy: F_line(float(xm), float(yy)), [0, yc])
               + mp.quad(lambda yy: 1 / (24 * yy**2), [yc, mp.inf]))
    print(f"x = {x}: sqrt(x) * Phi(x) = {mp.nstr(mp.sqrt(xm) * Phi, 10)}   (sqrt(2)/3 = {mp.nstr(mp.sqrt(2)/3, 10)})")

# ---------- 4. Lemme d'Epstein, coupure lisse ----------
# Sum_{w prim} |w|^(-3/2) chi(|w|/T) - (6/pi^2) * 2 pi * T^(1/2) * int_0^1 r^(-1/2) chi(r) dr  ->  Z_prim(3/2)
chi = lambda u: np.where(u < 1, np.exp(1 - 1 / np.clip(1 - u * u, 1e-300, None)), 0.0)
Ichi = mp.quad(lambda u: u**-0.5 * mp.e**(1 - 1 / (1 - u * u)), [0, 1])
for T in (100, 300, 1000, 1999):
    S = np.sum(4 * r ** -1.5 * chi(r / T))
    val = S - float(6 / mp.pi**2 * 2 * mp.pi * Ichi) * T**0.5
    print(f"T = {T:5d}: somme - intégrale = {val:.6f}   (Z_prim(3/2) = {float(Zp):.6f})")
