"""Contrôles courts, indépendants des sorties scientifiques historiques.

Les données synthétiques internes vérifient le code d'assemblage et de filtre;
elles ne sont jamais des données d'enveloppes et ne servent à aucun résultat.
"""
import argparse
import importlib
import io
import contextlib
import numpy as np
import pandas as pd
from scipy.integrate import quad, simpson
from scipy.spatial import ConvexHull
from numerical_tools import G_exact, G_mc, Hm_float, local_J02, simpson_mc, write_json
from vertices import local_JV02
from zeta_b import calculation, hurwitz_em
from assemble_tail import assemble
from fit_gamma import fit_table
from hull_disc import one


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", default="corrective_checks.json")
    args = p.parse_args(argv)
    checks = []
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        for name in ("cinf", "tail_is", "vertices", "vertices2", "fit_gamma", "zeta_b", "hull_disc", "assemble_tail"):
            importlib.import_module(name)
    assert capture.getvalue() == "", "Effet de bord à l'import."
    checks.append(dict(name="imports_without_execution", status="PASS"))
    for a in (.3, .7, 1., 1.5, 2.):
        h = a*a/8
        direct = a*quad(lambda d: Hm_float(d, a), h, 1/a, epsabs=1e-11)[0]
        direct += a*quad(lambda d: (1-2*np.sqrt(2*d)/a)*Hm_float(d+1/a, a), 0, h, epsabs=1e-11)[0]
        assert abs(G_exact(a)-direct) < 2e-10
    checks.append(dict(name="G_formula_independent_d_quadrature", status="PASS"))
    J02, _ = local_J02()
    J01 = quad(lambda u: 2*u**3*G_exact(u*u) if u else 2**3.5/15, 0, 1, epsabs=1e-11)[0]
    J12 = quad(lambda a: a*G_exact(a), 1, 2, epsabs=1e-11)[0]
    assert abs(J01-.872472643047247) < 2e-10
    assert abs(J12-.234689266006291) < 2e-10
    assert abs(J01+J12-J02) < 2e-10
    JV02, _ = local_JV02()
    assert abs(JV02-.86125501) < 2e-8
    checks.append(dict(name="local_integrals_previous_numeric_values", status="PASS", J01=J01, J12=J12, J02=J02, JV02=float(JV02)))
    x = np.linspace(0, 2, 9)
    value, se, weights = simpson_mc(x, x**3, np.full(len(x), .02))
    assert abs(value-4) < 1e-13
    # Variance de la combinaison confirmée par tirages gaussiens à petit coût.
    samples = np.random.default_rng(123).normal(size=(50_000, len(x)))*.02
    observed_se = float((samples @ np.array(weights)).std(ddof=1))
    assert abs(observed_se/se-1) < .02
    checks.append(dict(name="Simpson_variance_independent_simulation", status="PASS", formula_se=se, simulated_se=observed_se))
    for a in (.7, 2., 3.6):
        value, error, ranks = G_mc(a, 200, seed=33)
        assert np.isfinite([value, error]).all() and error >= 0 and ranks <= int(np.ceil(a**3/8))+3
    checks.append(dict(name="short_MC_termination", status="PASS", n=200))
    small, large = calculation(64), calculation(256)
    assert abs(small["B_cut_conjectural"]-large["B_cut_conjectural"]) < 1e-12
    assert abs(large["B_cut_conjectural"]-.05788468) < 5e-9
    assert abs(hurwitz_em(2)-np.pi**2/6) < 1e-12
    assert abs(large["c0_closed_form"]-large["c0_quadrature_check"]) < 1e-12
    checks.append(dict(name="Euler_Maclaurin_stability_and_zeta2", status="PASS", B_cut=large["B_cut_conjectural"]))
    # Fixture synthétique connue : les deux modèles retrouvent exactement la queue.
    tx = np.geomspace(3.6, 12, 9)
    ty = (1/9)/tx**2+.02/tx**3-.01/tx**4
    rows = [dict(a=float(a), aG=float(b), aG_mc_se=1e-5, seed=500+i) for i, (a, b) in enumerate(zip(tx, ty))]
    base = dict(schema="dyn-cinf-truncated-v0.2", J_truncated_0_3_6=1., J_truncated_se_MC_ONLY=.01, rows=[dict(seed=100)])
    tail = dict(schema="dyn-cinf-tail-is-v0.2", rows=rows)
    assembly = assemble(base, tail, 6, 12)
    expected_tail = (1/9)/12+.02/(2*12**2)-.01/(3*12**3)
    for model in assembly["models"]:
        assert abs(model["extrapolation_cut_infinity"]-expected_tail) < 1e-11
    checks.append(dict(name="synthetic_tail_models_analytic_integrals", status="PASS", fixture="synthetic, no scientific inference"))
    negative_tail = dict(tail)
    negative_tail["rows"] = [dict(r, aG=float(-1/r["a"]**2)) for r in rows]
    rejected = assemble(base, negative_tail, 6, 12)
    assert not rejected["models"][1]["physical_tail_nonnegative"]
    assert rejected["model_spread"] is None
    checks.append(dict(name="synthetic_negative_tail_rejected_from_model_spread", status="PASS", fixture="synthetic, no scientific inference"))
    records = []
    for param in (1., 2.):
        for i, radius in enumerate(np.geomspace(1230, 100_000, 8)):
            ratio = param**.2
            records.append(dict(forme="ellipse", param=param, R=radius, C_eff=.7193-.3*ratio*radius**(-1/6)+1e-5*np.sin(i), C_eff_se=.001, ratio_I32_I43=ratio))
    records.append(dict(forme="ellipse", param=1., R=1000, C_eff=999, C_eff_se=.001, ratio_I32_I43=1.))
    fits = fit_table(pd.DataFrame(records))
    assert all(all(r["R"] >= 1230 for r in f["residuals"]) for f in fits)
    assert {f["n"] for f in fits} == {8, 16}
    checks.append(dict(name="synthetic_CSV_R_filter_and_fit_exports", status="PASS", fixture="synthetic, no historical fit"))
    for R in (2., 3., 5.):
        seed = int(100*R)
        measured = one(R, np.random.default_rng(seed))
        rng = np.random.default_rng(seed)
        th, u, v = rng.uniform(0, np.pi/2), *rng.random(2)
        M = int(np.ceil(R))+2
        X, Y = np.meshgrid(np.arange(-M, M+1)+u, np.arange(-M, M+1)+v)
        pts = np.column_stack((X.ravel(), Y.ravel()))
        pts = pts[np.sum(pts**2, axis=1) <= R*R]
        # Pour le disque, la rotation conserve le périmètre.
        expected = 2*np.pi*R-ConvexHull(pts).area
        assert abs(measured-expected) < 1e-10
    checks.append(dict(name="hull_reduced_points_vs_all_points_scipy", status="PASS", radii=[2, 3, 5]))
    result = dict(schema="dyn-cinf-corrective-checks-v0.2", status="PASS", n_checks=len(checks), checks=checks,
                  scope="Code et concordances numériques locales; aucune queue certifiée, aucun fit historique, aucune preuve asymptotique.")
    write_json(args.output, result)
    print(f"PASS {len(checks)}/{len(checks)} contrôles ciblés.")
    return result


if __name__ == "__main__":
    main()
