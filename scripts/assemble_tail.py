"""Assemblage conditionnel de J; deux extrapolations polynomiales NON certifiées.

f(a)=aG(a)=(1/9)/a²+c/a³+d/a⁴, puis A/a²+c/a³+d/a⁴ avec A libre.
Les seuils --fit-min et --cut sont obligatoires : aucun seuil publié n'est inventé.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.integrate import simpson
from numerical_tools import write_json


def assemble(base, tail, fit_min, cut):
    if base.get("schema") != "dyn-cinf-truncated-v0.2" or tail.get("schema") != "dyn-cinf-tail-is-v0.2":
        raise ValueError("Les JSON cinf/tail_is correctifs v0.2 sont requis.")
    rows = sorted(tail["rows"], key=lambda r: r["a"])
    x = np.array([r["a"] for r in rows], float)
    y = np.array([r["aG"] for r in rows], float)
    se = np.array([r["aG_mc_se"] for r in rows], float)
    if len(x) < 4 or np.any(np.diff(x) <= 0) or np.any(se <= 0):
        raise ValueError("Au moins 4 points distincts et SE>0 requis.")
    if not np.isclose(x[0], 3.6, atol=1e-10, rtol=0):
        raise ValueError("La grille de queue doit commencer exactement à 3.6.")
    cut_matches = np.flatnonzero(np.isclose(x, cut, atol=1e-10, rtol=1e-10))
    if len(cut_matches) != 1:
        raise ValueError("--cut doit être l'un des points mesurés (aucun point interpolé inventé).")
    last = int(cut_matches[0])
    if last < 2 or not 3.6 <= fit_min < cut:
        raise ValueError("Au moins 3 points avant cut; 3.6<=fit-min<cut requis.")
    selected = np.flatnonzero((x >= fit_min) & (x <= x[last]))
    if len(selected) < 4:
        raise ValueError("Au moins 4 points dans [fit-min,cut] sont requis pour comparer les deux fits.")
    # Poids linéaires EXACTS de scipy.simpson pour cette grille, incluant son cas pair.
    qw = np.zeros(len(x))
    qw[:last+1] = simpson(np.eye(last+1), x=x[:last+1], axis=0)
    qvalue = float(qw @ y)
    qse = float(np.linalg.norm(qw * se))
    ix, iy, ise = x[selected], y[selected], se[selected]
    independent = not ({r.get("seed") for r in base["rows"]} & {r.get("seed") for r in rows})
    models = []
    for fixed in (True, False):
        powers = np.array([3, 4] if fixed else [2, 3, 4])
        # Paramétrisation mise à l'échelle pour éviter le mauvais conditionnement d'a^-p.
        design = (cut/ix[:, None])**powers
        offset = (1/9)/ix**2 if fixed else np.zeros(len(ix))
        weighted = design/ise[:, None]
        scaled, _, rank, _ = np.linalg.lstsq(weighted, (iy-offset)/ise, rcond=None)
        if rank != len(powers):
            raise ValueError("Ajustement de queue de rang insuffisant.")
        scaled_cov = np.linalg.inv(weighted.T @ weighted)
        linear_map = scaled_cov @ (design.T/ise**2)
        param = scaled*cut**powers
        covariance = scaled_cov*np.outer(cut**powers, cut**powers)
        prediction = offset+design @ scaled
        residual = iy-prediction
        # Intégrale des bases de cut à l'infini : cut/(p-1).
        tail_vector = cut/(powers-1)
        extrapolation = float(tail_vector @ scaled + ((1/9)/cut if fixed else 0))
        extrapolation_se = float(np.sqrt(tail_vector @ scaled_cov @ tail_vector))
        A, c, d = (1/9, *param) if fixed else param
        # f(a)>=0 pour a>=cut ssi P(t)=A+c*t+d*t²>=0 sur 0<=t<=1/cut.
        # Contrôle du modèle en double précision; ce n'est pas une borne du vrai G.
        candidates_t = [0., 1/cut]
        if d > 0 and 0 < -c/(2*d) < 1/cut:
            candidates_t.append(float(-c/(2*d)))
        polynomial_min = float(min(A+c*t+d*t*t for t in candidates_t))
        physical = bool(A >= 0 and polynomial_min >= 0)
        global_tail_weights = qw.copy()
        global_tail_weights[selected] += tail_vector @ linear_map
        conditional_mc_se_tail = float(np.linalg.norm(global_tail_weights*se))
        combined_mc_se = float(np.hypot(base["J_truncated_se_MC_ONLY"], conditional_mc_se_tail)) if independent else None
        J = base["J_truncated_0_3_6"]+qvalue+extrapolation
        models.append(dict(model="fixed_A_1_over_9" if fixed else "free_A",
                           form="f(a)=A/a^2+c/a^3+d/a^4", A_fixed=1/9 if fixed else None,
                           fitted_parameter_names=["c", "d"] if fixed else ["A", "c", "d"],
                           parameters=param.tolist(), nominal_covariance_MC_model_conditional=covariance.tolist(),
                           physical_tail_nonnegative=physical,
                           polynomial_min_double_precision=polynomial_min,
                           physical_tail_check="Polynomial model only, double precision; no certification of the true tail.",
                           warning=None if physical else "Extrapolation nominale non physique: queue négative dans le modèle; ne pas retenir sa valeur dans une plage admissible.",
                           chi2=float(np.sum((residual/ise)**2)), dof=int(len(selected)-len(powers)),
                           residuals=residual.tolist(), numerical_tail_3_6_cut=qvalue,
                           numerical_tail_se_MC_ONLY=qse, extrapolation_cut_infinity=extrapolation,
                           extrapolation_fit_se_MC_ONLY_NOT_MODEL_ERROR=extrapolation_se,
                           J_model_conditional=J, coefficient_model_conditional=float(6/np.pi**2*J),
                           J_se_MC_ONLY_model_conditional=combined_mc_se,
                           coefficient_se_MC_ONLY_model_conditional=None if combined_mc_se is None else float(6/np.pi**2*combined_mc_se),
                           combined_MC_weights_include_fit_quadrature_dependence=True,
                           combined_tail_MC_weights=global_tail_weights.tolist()))
    coeffs = [m["coefficient_model_conditional"] for m in models if m["physical_tail_nonnegative"]]
    return dict(schema="dyn-cinf-tail-assembly-v0.2", status="CONJECTURAL_MODEL_ASSEMBLY_NOT_CERTIFIED",
                fit_min=fit_min, cut=cut, fit_a_values=ix.tolist(), selected_indices=selected.tolist(),
                quadrature="scipy composite Simpson with nonuniform-grid weights", quadrature_weights=qw.tolist(),
                MC_base_tail_independence_assumed_from_disjoint_seed_sets=independent,
                models=models, n_physically_admissible_models=len(coeffs),
                model_spread=[min(coeffs), max(coeffs)] if len(coeffs) == 2 else None,
                interpretation="Écart entre deux choix de modèle, ni encadrement rigoureux ni intervalle de confiance global.",
                excluded_uncertainties=["erreur de quadrature non bornée", "biais de modèle local", "erreur d'extrapolation", "transfert aux enveloppes entières"],
                published_range_reproduction="NOT_CLAIMED: seuils originaux et données historiques non fournis")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--base", required=True)
    p.add_argument("--tail", required=True)
    p.add_argument("--fit-min", required=True, type=float)
    p.add_argument("--cut", required=True, type=float)
    p.add_argument("--output", default="assembled_tail.json")
    args = p.parse_args(argv)
    base = json.loads(Path(args.base).read_text(encoding="utf-8"))
    tail = json.loads(Path(args.tail).read_text(encoding="utf-8"))
    result = assemble(base, tail, args.fit_min, args.cut)
    result["sources"] = dict(base=str(Path(args.base).resolve()), tail=str(Path(args.tail).resolve()))
    write_json(args.output, result)
    for model in result["models"]:
        print(model["model"], "coefficient conditionnel nominal =", model["coefficient_model_conditional"],
              "; SE MC seule =", model["coefficient_se_MC_ONLY_model_conditional"])
        if not model["physical_tail_nonnegative"]:
            print(model["warning"])
    print("Écart de modèles:", result["model_spread"], "(aucun encadrement certifié ni IC global)")
    return result


if __name__ == "__main__":
    main()
