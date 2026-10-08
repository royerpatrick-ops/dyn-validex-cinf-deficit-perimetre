# Vérification des trois notes de démonstration du 8 octobre 2026

Notes examinées (v0.1, rédigées par ChatGPT/Codex) :
- **CV** — Convergence des probabilités de calottes vides ;
- **QU** — Queues uniformes et espérance complète ;
- **ID** — Identification de la constante.

## Verdict

La chaîne CV → QU → ID est complète ; aucune erreur trouvée, tous les nombres recalculés. Elle démontre, pour K convexe compact à bord C³ et courbure κ > 0, avec L = ρ(θ)(ℤ² + t), θ et t uniformes :

E[P(RK) − P(conv(L ∩ RK))] = C · ∫κ^{4/3} ds · R^{−1/3} + o(R^{−1/3}),
C = (6/π²) ∫₀^∞ a G(a) da ∈ ]0,71923298 ; 0,71923337[.

- Le bord C² avec κ > 0 suffit probablement : C³ ne sert qu'au taux O(R^{−2/3}) de (4) dans CV.
- Statut : vérifications par IA seulement (Codex, deux contre-lectures IA, Claude). Relecture humaine à faire.
- Hors théorème : superellipses p ≠ 2 (κ nul ou infini en 4 points), second terme B·R^{−1/2}, tout taux de convergence.

## Sources externes vérifiées sur le texte

- **Marklof–Strömbergsson** (Ann. Math. 2010, arXiv:0706.4395v2), corollaire 5.9, §5.4, au niveau q = 1. Les hypothèses sont remplies. Les auteurs notent que ces énoncés pour SL(d,ℝ) découlent du mélange, sans la théorie de Ratner.
- **Binh–Reitzner** (arXiv:2003.06864, Mathematika 2021).
  - Lemme 3.2 : borne c/V, avec des constantes qui ne dépendent que de d. Énoncé par Bárány–Matoušek (DCG 33, 2005), démontré par Bárány (Random Struct. Algorithms 30, 2007).
  - Lemme 3.1 : c'est l'identité (14) de QU, sans facteur manquant.
  - Théorèmes 1.1 et 1.4 : ils démontrent déjà ΔP ≍ R^{−1/3} pour K lisse (encadrement à constantes près).
  - Fin du §5 : ils écrivent ne pas savoir démontrer la convergence des probabilités de calottes normalisées. CV la démontre en dimension 2, avec f_K(x,u) = v_H(κ_u^{−1/3} x).

## Contrôles numériques (script verif_notes_2026-10-08.py, environ 1 minute)

| Contrôle | Résultat |
|---|---|
| H(d,a) = moyenne de phase de c, quel que soit le nombre de points (fenêtre ≥ a) | exact |
| Forme close de G0 | exacte ; J0 = 141/140 |
| J1, par (13) et à partir de G1 | 0,100019051910681 |
| JT, par (14) et à partir de (12) | 0,075929242314814 |
| C_void | 0,7192331748805058 |
| Certificat rationnel (N = 100, Machin 30 termes), refait de zéro | ]0,719232986 ; 0,719233362[ |
| Erreurs réelles de troncature, contre les bornes | 2,4·10⁻¹⁰ et 1,6·10⁻⁹, contre 4,6·10⁻¹⁰ et 3,1·10⁻⁷ |
| Monte-Carlo du modèle (1), 2·10⁶ tirages, 9 valeurs de a dans [0,25 ; 4] | tous les écarts < 1 σ |
| Même dépliage avec l'indicatrice d'arête | c₀/2π = 0,549672, soit c₀ = 3,45369 (Balog–Deshouillers : 3,453…) |
| Asymptotique de G | a³G(a) = (1 + 12/a³)/9 + … |

Le dernier point corrige la note du 2 octobre : la correction relative est en 12/a³, et non en 1/a².

## Corrections demandées

1. **Note du 2 octobre, §1.** L'ordre R^{−1/3} est démontré par Binh–Reitzner. Citer aussi Bárány–Matoušek 2005 (origine du modèle randomisé) et Bárány 2007.
2. **QU.** Créditer :
   - la preuve du théorème 5.1 de [NR], dont la domination est la version uniforme ;
   - le lemme 3.3 de [NR], qui donne la borne de Markov (12).
3. **ID, §6.** Justifier que H s'applique à une rangée de 3 points ou plus, au lieu de renvoyer à [M]. C'est le cas de la rangée 0 pour a < 2^{1/3} et de la rangée 1 pour a < (8/3)^{1/3}. La raison : x₂ est uniforme sur ]r−a, r] et x₁ sur [−r, −r+a[.
4. **Énoncé.** Séparer :
   - le théorème : premier terme, κ > 0 ;
   - la conjecture : points singuliers et terme B.

## Pistes

- Fusionner les trois notes en un seul manuscrit, avec en annexe les énoncés cités. Lecteur expert naturel : M. Reitzner.
- **Second ordre.** La correction relative R^{−1/6} = e^{−s/2}, avec s = ⅓ log(R/κ), est l'échelle d'une série d'Eisenstein de paramètre 3/4 le long des cercles dilatés. Σ_prim |w|^{−3/2}, qui donne B_petits, est (à normalisation près) E(i, 3/4). C'est une piste spectrale, non une preuve.
