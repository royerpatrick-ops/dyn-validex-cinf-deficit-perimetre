"""
Contrôles indépendants des notes DYN-VALIDEX du 8 octobre 2026
  [ID] Identification de la constante v0.1
  [QU] Queues uniformes et espérance complète v0.1

Usage : python verif_notes_2026-10-08.py [A] [B] [C] [D] [E]   (toutes les parties par défaut)

A  Calcul symbolique : moyenne de phase H(d,a) (valable pour tout nombre de
   points dans la rangée), forme close de G0, J0 = 141/140.
B  Quadratures haute précision de J1 et JT, sous les formes substituées (13), (14)
   et directement à partir des définitions de G1 et de (12).
C  Certificat rationnel (16)-(19) + encadrement de π par Machin, refait de zéro.
D  Monte-Carlo direct du modèle de rangées (définition (1)) contre G(a).
E  Asymptotique de G(a) pour a grand ; contrôle de normalisation par la densité
   de sommets c0/2π (Balog–Deshouillers) ; borne inférieure (12) de [QU].

Dépendances : numpy, mpmath, sympy (la partie C n'utilise que la bibliothèque standard).
    pip install numpy mpmath sympy
Durée totale : environ 2 minutes (la partie D domine).
"""
import sys
import time
from decimal import Decimal, getcontext
from fractions import Fraction as Fr
from math import comb, factorial

try:                                   # sortie lisible aussi sous Windows redirigé
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# ---------------------------------------------------------------- A
def part_A():
    import sympy as sp
    a, r, y = sp.symbols('a r y', positive=True)
    H = (2*r - a)*(r**2 + 2*a*r - a**2)/6
    # Moyenne de phase de c = d(x2-x1) - (x2^3-x1^3)/3 avec d = r^2/2 :
    # x2 uniforme sur (r-a, r], x1 uniforme sur [-r, -r+a), quel que soit le
    # nombre de points, dès que la fenêtre [-r, r] a une longueur >= a.
    Hph = sp.Rational(2)/a*sp.integrate((r**2/2)*y - y**3/3, (y, r - a, r))
    print("A1  H(d,a) = moyenne de phase, tout nombre de points :",
          sp.simplify(H - Hph) == 0)
    # G0 = a * int_{a^2/8}^{1/a} H(sqrt(2 delta), a) d delta ; delta = r^2/2
    G0_int = a*sp.integrate(sp.expand(H*r), (r, a/2, sp.sqrt(2/a)))
    G0_doc = (4*sp.sqrt(2)/15*a**sp.Rational(-3, 2) + sp.Rational(1, 2)
              - 4*sp.sqrt(2)/9*a**sp.Rational(3, 2) + a**3/6
              - sp.Rational(17, 5760)*a**6)
    num = max(abs(float((G0_int - G0_doc).subs(a, v))) for v in (0.1, 0.7, 1.3, 1.9))
    print("A2  G0 forme close du §6 :", sp.simplify(sp.expand(G0_int - G0_doc)) == 0,
          f"(écart numérique max {num:.1e})")
    print("    G0(2) =", sp.nsimplify(G0_doc.subs(a, 2)))
    J0 = sp.nsimplify(sp.integrate(sp.expand(a*G0_doc), (a, 0, 2)))
    print("A3  J0 =", J0, "=", float(J0))


# ---------------------------------------------------------------- outils mpmath
def mpfuncs(dps=30):
    import mpmath as mp
    mp.mp.dps = dps

    def H(d, a):
        r = mp.sqrt(2*d)
        return (2*r - a)*(r**2 + 2*a*r - a**2)/6

    def G0(a):
        a = mp.mpf(a)
        return (4*mp.sqrt(2)/15*a**mp.mpf(-1.5) + mp.mpf(1)/2
                - 4*mp.sqrt(2)/9*a**mp.mpf(1.5) + a**3/6 - mp.mpf(17)/5760*a**6)

    def G1(a):
        a = mp.mpf(a)
        return a*mp.quad(lambda dl: (1 - 2*mp.sqrt(2*dl)/a)*H(dl + 1/a, a), [0, a**2/8])

    def GT(a):                       # formule exacte (12), a >= 2
        a = mp.mpf(a)
        h = a**2/8
        return a*mp.quad(lambda d: (1 - 2*mp.sqrt(2*(d - 1/a))/a)*H(d, a), [h, h + 1/a])

    def G(a):
        return G0(a) + G1(a) if a <= 2 else GT(a)

    return mp, H, G0, G1, GT, G


# ---------------------------------------------------------------- B
def part_B():
    mp, H, G0, G1, GT, G = mpfuncs(30)
    t = time.time()

    def f13(v, s):
        R = mp.sqrt(1 + v**6*s**2)
        return mp.mpf(16)/3*v**6*s*(1 - s)*(R - v**3)*(R**2 + 4*v**3*R - 4*v**6)

    def f14(v, f):
        s1 = mp.sqrt(1 + v**3*f)
        s0 = mp.sqrt(1 - v**3*(1 - f))
        return mp.mpf(4)/3*f*(1 - f)*(v**3*f - 3 + 4*s1)/((1 + s0)*(1 + s1))

    J1 = mp.quad(f13, [0, 1], [0, 1])
    JT = mp.quad(f14, [0, 1], [0, 1])
    print("B1  J1 par (13) =", mp.nstr(J1, 18), "   note : 0.100019051910681")
    print("B2  JT par (14) =", mp.nstr(JT, 18), "   note : 0.075929242314814")
    mp.mp.dps = 20
    J1d = mp.quad(lambda a: a*G1(a), [0, 1, 2])
    # La forme (12) non rationalisée soustrait des nombres presque égaux quand a
    # est grand (1 - sqrt(1 - 8/a^3 ...)) : 40 chiffres sont nécessaires ici.
    mp.mp.dps = 40
    JTd = mp.quad(lambda a: a*GT(a), [2, 4, 8, 16, 64, mp.inf])
    print("B3  J1 directement (G1)  =", mp.nstr(J1d, 15))
    print("B4  JT directement (12)  =", mp.nstr(JTd, 15))
    mp.mp.dps = 30
    C = 6*(mp.mpf(141)/140 + J1 + JT)/mp.pi**2
    print("B5  C_void =", mp.nstr(C, 18), "   note : 0.719233174880506")
    print(f"    ({time.time() - t:.0f} s)")


# ---------------------------------------------------------------- C
def part_C(N=100, K=30):
    t = time.time()

    def gbinom(x, nmax):
        out = [Fr(1)]
        for n in range(nmax):
            out.append(out[-1]*(x - n)/(n + 1))
        return out

    b = gbinom(Fr(1, 2), N + 2)
    q = gbinom(Fr(3, 2), N + 2)
    S1 = sum((q[n]/(6*n + 7) - 8*b[n]/(6*n + 13))/((2*n + 2)*(2*n + 3)) for n in range(N + 1))
    J1 = Fr(16, 3)*(Fr(1, 20) + Fr(3, 320) + Fr(1, 24) + S1)
    E1 = Fr(16, 3*(2*N + 4)*(2*N + 5))*(abs(q[N + 1])/(6*N + 13) + 8*abs(b[N + 1])/(6*N + 19))
    al = [None] + [-((-1)**m)*b[m] for m in range(1, N + 1)]
    p = [None, Fr(1, 2)] + [b[n - 1] - 7*b[n] for n in range(2, N + 1)]
    assert all(x > 0 for x in al[1:])
    f = [factorial(k) for k in range(2*N + 3)]
    JT = Fr(0)
    for m in range(1, N + 1):
        inner = sum(p[n]*Fr(f[n], f[m + n + 1]*(3*(m + n) - 5)) for n in range(1, N + 1))
        JT += al[m]*f[m]*inner
    JT *= Fr(4, 3)

    def T(k):
        return Fr(comb(2*k, k), 4**k)

    ET = Fr(4, 3)*(T(N - 1) + 12*T(N))/((N + 2)*(N + 3)*(3*N + 1))

    def arctan_inv(x):
        S = sum(Fr((-1)**k, (2*k + 1)*x**(2*k + 1)) for k in range(K))
        e = Fr(1, (2*K + 1)*x**(2*K + 1))
        return S - e, S + e

    l5, h5 = arctan_inv(5)
    l239, h239 = arctan_inv(239)
    pil, pih = 16*l5 - 4*h239, 16*h5 - 4*l239
    Jc = Fr(141, 140) + J1 + JT
    Clo = 6*(Jc - E1 - ET)/pih**2
    Chi = 6*(Jc + E1 + ET)/pil**2
    getcontext().prec = 40

    def dec(x):
        return Decimal(x.numerator)/Decimal(x.denominator)

    print(f"C1  J1 tronqué = {float(J1):.15f}   JT tronqué = {float(JT):.15f}")
    print(f"    E1 = {float(E1):.4e} (note < 4.607e-10)   ET = {float(ET):.4e} (note < 3.090e-7)")
    print(f"C2  {dec(Clo):.18f} < C_void < {dec(Chi):.18f}")
    print("    note (20) : 0.71923298 < C_void < 0.71923337")
    print("C3  arrondi 0,719 justifié :", Fr(7185, 10000) < Clo and Chi < Fr(7195, 10000),
          "  arrondi 0,719233 justifié :", Fr(7192325, 10**7) < Clo and Chi < Fr(7192335, 10**7))
    print(f"    ({time.time() - t:.0f} s)")


# ---------------------------------------------------------------- D
def part_D(Nmc=2_000_000, seed=20261008):
    import numpy as np
    mp, H, G0, G1, GT, G = mpfuncs(20)
    rng = np.random.default_rng(seed)
    chunk = 500_000
    print("D   Monte-Carlo du modèle de rangées tel que défini en (1), 2·10⁶ tirages par a")
    print("      a     MC                      formule     écart/σ")
    for a in [0.25, 0.5, 1.0, 1.5, 1.9, 2.0, 2.2, 3.0, 4.0]:
        S = S2 = 0.0
        n = 0
        for _ in range(Nmc//chunk):
            dl = rng.random(chunk)/a
            s = rng.random(chunk)*a
            be = rng.random(chunk)*a
            c = np.zeros(chunk)
            done = np.zeros(chunk, bool)
            k = 0
            while not done.all():
                dk = dl + k/a
                w = np.sqrt(2*dk)
                off = s + k*be
                x1 = off + a*np.ceil((-w - off)/a)      # plus petit point >= -w
                x2 = off + a*np.floor((w - off)/a)      # plus grand point <= w
                adm = ~done & (x1 <= x2)                # première rangée admissible
                c[adm] = dk[adm]*(x2[adm] - x1[adm]) - (x2[adm]**3 - x1[adm]**3)/3
                done |= adm
                k += 1
            S += c.sum()
            S2 += (c*c).sum()
            n += chunk
        mean = S/n
        se = ((S2/n - mean**2)/(n - 1))**0.5
        g = float(G(a))
        print(f"    {a:4.2f}  {mean:.6f} ± {se:.6f}   {g:.6f}   {(mean - g)/se:+.2f}")


# ---------------------------------------------------------------- E
def part_E():
    mp, H, G0, G1, GT, G = mpfuncs(25)
    print("E1  a³G(a) : formule exacte (12) contre (1 + 12/a³)/9")
    print("    (note du 2 octobre : 0,1170 à a = 6 et 0,1138 à a = 8, « correction en 1/a² »)")
    for a in [4, 6, 8, 16, 32]:
        g = GT(a)*a**3
        print(f"    a = {a:3d}   a³G = {mp.nstr(g, 9)}   (1+12/a³)/9 = {mp.nstr((1 + mp.mpf(12)/a**3)/9, 9)}")

    def Pedge(a):        # probabilité que la première rangée admissible ait >= 2 points
        a = mp.mpf(a)
        if a <= 2:
            def g(dl):
                L0 = 2*mp.sqrt(2*dl)
                L1 = 2*mp.sqrt(2*(dl + 1/a))
                two0 = min(max(L0/a - 1, 0), 1)
                empty0 = max(1 - L0/a, 0)
                two1 = min(max(L1/a - 1, 0), 1)
                return two0 + empty0*two1
            br = sorted({mp.mpf(0), 1/a} |
                        {x for x in (a**2/8, a**2/2, a**2/2 - 1/a) if 0 < x < 1/a})
            return a*mp.quad(g, br)
        h = a**2/8
        return a*mp.quad(lambda d: (1 - 2*mp.sqrt(2*(d - 1/a))/a)*(2*mp.sqrt(2*d)/a - 1),
                         [h, h + 1/a])

    brk = [0, 0.5, 1, mp.cbrt(2), mp.cbrt(4), 2, 4, 8, mp.inf]
    I = mp.quad(lambda a: a*Pedge(a), brk)
    lam = 6/mp.pi**2*I
    print("E2  densité de sommets (6/π²)∫ a·P(arête) da =", mp.nstr(lam, 12))
    print("    c0 = 2π·λ =", mp.nstr(2*mp.pi*lam, 10),
          "   référence de la note du 2 oct. : c0/2π = 0,54967 (Balog–Deshouillers, 3,453…)")
    lb = mp.mpf(3)/5*(3/(4*mp.sqrt(2)))**(mp.mpf(2)/3)
    print("E3  borne inférieure (12) de [QU] : C_void >", mp.nstr(lb, 6))


if __name__ == "__main__":
    parts = [p.upper() for p in sys.argv[1:]] or list("ABCDE")
    for P in parts:
        print(f"\n===== Partie {P} =====")
        {"A": part_A, "B": part_B, "C": part_C, "D": part_D, "E": part_E}[P]()
