# Corrective distincte des scripts — v0.2

Cette copie corrige la restitution et la traçabilité des scripts joints. Les originaux sont conservés. Elle ne transforme aucune estimation en preuve et ne prétend pas reproduire les données historiques absentes.

## Installation et lancement

Depuis ce dossier, dans PowerShell, Python 3.10 ou ultérieur :

```powershell
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe cinf.py --checks --output results/cinf_truncated.json
& .\.venv\Scripts\python.exe tail_is.py --output results/tail_is.json
& .\.venv\Scripts\python.exe assemble_tail.py --base results/cinf_truncated.json --tail results/tail_is.json --fit-min 6 --cut 12 --output results/assembled_tail.json
& .\.venv\Scripts\python.exe vertices.py --output results/vertices.json
& .\.venv\Scripts\python.exe vertices2.py --output results/vertices2.json
& .\.venv\Scripts\python.exe zeta_b.py --output results/zeta_b.json
& .\.venv\Scripts\python.exe hull_disc.py --radii 1230 --n 20 --output results/hull_disc.json
& .\.venv\Scripts\python.exe check_corrective.py
```

Ces valeurs sont des exemples de lancement frugal. `--fit-min 6 --cut 12` ne sont pas les seuils historiques du manuscrit. L'assembleur exige leur choix explicite et `--cut` doit correspondre à un point effectivement mesuré. Les tirages par point se règlent avec `--n`; utiliser `--help` pour chaque programme. Le défaut de la queue est 200 000 tirages par point (9 points jusqu'à 12), les autres défauts sont 20 000. Ce réglage de queue tient compte de la rareté des événements, sans garantir un nombre suffisant. Les modules n'exécutent aucun Monte-Carlo lors de leur import.

Sur Linux, remplacer l'exécutable PowerShell par `python` après activation de l'environnement. Le paquet ne contient aucune procédure de publication.

## Portée des sorties

| Programme | Résultat et restriction |
|---|---|
| `cinf.py` | `J_truncated_[0,3.6]` uniquement; le coefficient tronqué n'est pas (C_\infty\). SE intégrée avec les poids de Simpson. |
| `tail_is.py` | Points de (aG(a)), configuration, graines, tirages, SE empirique de l'importance sampling. Aucune intégrale extrapolée. |
| `assemble_tail.py` | Intégrale numérique jusqu'au cut, puis fits (A/a^2+c/a^3+d/a^4), avec (A=1/9) ou libre. Paramètres, covariance et sélection exportés. |
| `vertices.py`, `vertices2.py` | Contrôle local des sommets; la queue (8/(3a^5)) reste un modèle non certifié. Aucune valeur historique de la partie locale n'est injectée. |
| `fit_gamma.py` | Fits descriptifs sur un CSV externe réellement fourni, avec filtre explicite (R\ge1230), résidus, covariance, corrélations et chi². |
| `zeta_b.py` | Valeur au point (s=3/4) par prolongement analytique Euler–Maclaurin; la série primitive converge seulement pour \(\Re(s)>1\). |
| `hull_disc.py` | Simulation finie indépendante du disque; nombre de tirages frugal configurable. |

L'erreur `SE_MC_ONLY` porte seulement sur la variabilité des tirages sous le modèle numérique et les hypothèses d'indépendance. Elle n'inclut pas le biais de quadrature, la validité du modèle local, l'erreur d'extrapolation, ni le transfert aux enveloppes entières. Les erreurs retournées par `scipy.quad` sont des estimations internes, pas des bornes prouvées. Aucune sortie n'est un encadrement rigoureux ou un intervalle de confiance global. Si aucun événement contribuant n'est observé, la SE empirique nulle ne prouve pas une variance nulle : `tail_is.py` marque la variance non résolue et l'assembleur refuse le fit; augmenter `--n` ou réduire `--a-max`.

L'assembleur tient compte de la dépendance entre la quadrature et le fit lorsqu'ils réutilisent les mêmes points, via leurs poids linéaires combinés. Sa SE globale **Monte-Carlo seulement** reste conditionnelle à chaque modèle d'extrapolation. Si les ensembles de graines du calcul tronqué et de la queue se recouvrent, cette SE combinée est omise. Des graines différentes constituent une pratique de simulation, pas une preuve mathématique d'indépendance des pseudo-aléas.

L'assembleur vérifie aussi que la queue ajustée reste non négative pour `a>=cut`, dans son modèle polynomial en double précision. Un modèle qui échoue est marqué non physique; ses paramètres nominaux restent inspectables mais aucune plage commune de deux modèles admissibles n'est affichée. Ce contrôle de forme ne certifie pas la queue réelle.

## CSV absent du paquet

Le fichier `reanalysis_92_points.csv` et le programme du certificat Arb historique ne sont pas fournis dans les pièces reçues. Aucun fit des 69 points et aucune certification Arb n'est déclaré reproduit ici. Exemple, après obtention du CSV réel :

```powershell
& .\.venv\Scripts\python.exe fit_gamma.py chemin/reanalysis_92_points.csv --output results/fit_gamma.json
```

Colonnes requises : `forme,param,R,C_eff,C_eff_se,ratio_I32_I43`. Le disque correspond à `forme=ellipse,param=1`; toutes les ellipses retenues ont `R>=1230`. Le nombre de lignes réellement retenues est imprimé et enregistré, sans imposer artificiellement « 69 ».

Dans le fit à `gamma` libre, le ratio `I32/I43` est conservé comme facteur descriptif du CSV. Une loi géométrique homogène avec cet exposant demanderait en général `I_(4/3+gamma)` : le fit actuel ne démontre pas cette extension.

## Changements de méthode numérique

La dépendance `mpmath` des scripts d'origine est remplacée par SciPy en double précision. Le premier terme de (G(a)) est intégré par une primitive polynomiale; son deuxième terme utilise une quadrature régularisée. Les formules locales restent celles du manuscrit, mais leurs évaluations ne sont pas des calculs exacts ou certifiés. Le script de coupure utilise Euler–Maclaurin pour le prolongement analytique, avec contrôles de stabilité courts. Les défauts Monte-Carlo ont été réduits; les nouveaux résultats frugaux ne remplacent pas les estimations historiques à plusieurs millions de tirages.
