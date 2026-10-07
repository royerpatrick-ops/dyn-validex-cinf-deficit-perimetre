"""Fits sur CSV externe fourni; filtre explicite R>=1230, erreurs conditionnelles."""
import argparse
from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numerical_tools import write_json


def fit_table(frame, C_fixed=.7193, R_min=1230.):
    required = ["forme", "param", "R", "C_eff", "C_eff_se", "ratio_I32_I43"]
    missing = set(required)-set(frame.columns)
    if missing:
        raise ValueError("Colonnes manquantes: "+", ".join(sorted(missing)))
    d = frame.copy()
    for col in required[1:]:
        d[col] = pd.to_numeric(d[col], errors="raise")
    numeric = d[required[1:]].to_numpy(float)
    if (not np.isfinite(numeric).all() or (d.C_eff_se <= 0).any() or (d.R <= 0).any()
            or (d.ratio_I32_I43 <= 0).any() or (d.param <= 0).any()):
        raise ValueError("Valeurs non finies ou R/SE/ratio/param non strictement positifs dans le CSV.")
    selections = [("disque", (d.forme == "ellipse") & np.isclose(d.param, 1.) & (d.R >= R_min)),
                  ("ellipses_R_ge_1230", (d.forme == "ellipse") & (d.R >= R_min))]
    output = []
    for label, mask in selections:
        g = d.loc[mask]
        if len(g) < 4:
            raise ValueError(f"{label}: au moins quatre lignes admissibles sont requises.")
        x, y, se, r = [g[col].to_numpy(float) for col in ("R", "C_eff", "C_eff_se", "ratio_I32_I43")]
        for fixed in (True, False):
            fn = (lambda X, B, gamma: C_fixed-B*r*X**(-gamma)) if fixed else (lambda X, C, B, gamma: C-B*r*X**(-gamma))
            params, cov = curve_fit(fn, x, y, p0=[.3, 1/6] if fixed else [.72, .3, 1/6],
                                   sigma=se, absolute_sigma=True, maxfev=20_000)
            prediction = fn(x, *params)
            residual = y-prediction
            sd = np.sqrt(np.diag(cov))
            corr = cov/np.outer(sd, sd)
            if not np.isfinite(cov).all() or not np.isfinite(corr).all():
                raise ValueError("Covariance non finie; fit non exploitable.")
            output.append(dict(selection=label, n=int(len(g)), source_row_indices=g.index.tolist(),
                               filter=f"forme='ellipse'; R>={R_min}"+("; param approximately 1" if label=="disque" else ""),
                               C_fixed=C_fixed if fixed else None, model="C_eff=C_inf-B*ratio_I32_I43*R^(-gamma)",
                               parameter_names=["B", "gamma"] if fixed else ["C_inf", "B", "gamma"],
                               parameters=params.tolist(), nominal_standard_errors=sd.tolist(),
                               nominal_covariance=cov.tolist(), parameter_correlations=corr.tolist(),
                               chi2=float(np.sum((residual/se)**2)), dof=int(len(g)-len(params)),
                               residuals=[dict(source_row=int(idx), R=float(xx), observed=float(yy), predicted=float(pp),
                                               residual=float(rr), standardized_residual=float(rr/ss))
                                          for idx, xx, yy, pp, rr, ss in zip(g.index, x, y, prediction, residual, se)],
                               interpretation="Fit descriptif sur plage finie; covariance conditionnelle aux SE et à l'indépendance, exposant asymptotique non établi. Le ratio I32/I43 est conservé descriptivement même lorsque gamma est libre; une loi géométrique homogène d'exposant différent demanderait I_(4/3+gamma)."))
    return output


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv", help="CSV externe réel requis; aucune donnée n'est fournie ou inventée")
    p.add_argument("--c-fixed", type=float, default=.7193)
    p.add_argument("--r-min", type=float, default=1230.)
    p.add_argument("--output", default="fit_gamma.json")
    args = p.parse_args(argv)
    if args.r_min < 1230:
        p.error("La corrective exige R_min>=1230; un autre domaine nécessite une analyse distincte.")
    source = Path(args.csv)
    data = pd.read_csv(source)
    result = dict(schema="dyn-cinf-gamma-fit-v0.2", status="DESCRIPTIVE_FIT_NOT_ASYMPTOTIC_PROOF",
                  source=str(source.resolve()), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  configuration=vars(args), n_input=int(len(data)), fits=fit_table(data, args.c_fixed, args.r_min),
                  input_covariance="not supplied; diagonal weighting assumes independent means")
    write_json(args.output, result)
    for fit in result["fits"]:
        print(fit["selection"], fit["parameter_names"], fit["parameters"], "chi2/dof=", fit["chi2"], "/", fit["dof"])
    return result


if __name__ == "__main__":
    main()
