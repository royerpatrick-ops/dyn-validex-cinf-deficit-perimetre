# Second terme de la loi du déficit de périmètre : réduction à la pointe et forme close de B (9 octobre 2026)

Objet : démontrer le second terme −B·∫κ^{3/2} ds·R^{−1/2} de la conjecture. Le premier terme est démontré (chaîne CV → QU → ID, vérifiée le 8 octobre).

## Verdict

- **La démonstration n'est pas complète.** Le second terme est ramené à un énoncé précis d'équirépartition effective, l'hypothèse (H) du §5, elle-même ramenée à un lemme de régularité (lemme R). Tout le reste est démontré ici, sauf un lemme de localisation routinier (lemme Q, §1).
- **Forme close de B (nouveau, démontré) :**

  B = (√2/6π)·|Z_prim(3/2)| = (2√2/3π)·|ζ(3/4)·β(3/4)| / ζ(3/2) = 0,2894234179…

  C'est la valeur 0,2894 de la note du 2 octobre, désormais exacte. L'ajustement des simulations donnait 0,289 ± 0,001.
- **Les deux contributions de la note n'en font qu'une.** On a exactement B_grands = B_petits/4 (identité de Mellin, §4). Les arêtes à petit a et les arêtes à deux colonnes sont les deux régimes d'un même objet : les réseaux qui ont un vecteur très court, c'est-à-dire la pointe de l'espace des réseaux. Un seul calcul (§2 et §3) donne B d'un coup.
- **Question ouverte 3 de la note.** L'équirépartition de la projection du vecteur partenaire n'est plus nécessaire pour calculer B. Elle est remplacée par l'hypothèse (H), qui ne porte que sur une fonction bornée et nulle au fond de la pointe.
- **Statut :** vérifications par IA seulement. Relecture humaine à faire.

## 0. Cadre et notations

- K est un convexe compact du plan, à bord C⁴ et courbure κ > 0 (C³ suffit probablement). L = ρ(θ)(ℤ² + t), avec θ et t uniformes, et ΔP(R) = P(RK) − P(conv(L ∩ RK)).
- A = {(X, Y) : Y ≥ X²/2} est l'intérieur de la parabole normalisée. Pour un réseau Λ de covolume 1 et t ∈ ℝ², on pose Z*(Λ + t) = min{Y : (X, Y) ∈ (Λ + t) ∩ A}, puis Ψ(Λ) = E_t[Z*(Λ + t)], avec t uniforme sur ℝ²/Λ.
- μ est la mesure de Haar de probabilité sur X₂ = SL₂(ℤ)\SL₂(ℝ). Le théorème du 8 octobre donne C = ∫Ψ dμ = 0,7192331749.
- Les réseaux s'écrivent Λ = ℤ²g (vecteurs lignes). k_θ est la rotation d'angle θ et a_s = diag(e^{−s}, e^{s}).
- **Moyenne de cercle :** M(s) = (1/2π) ∫₀^{2π} Ψ(ℤ² k_θ a_s) dθ.
- **Zêta d'Epstein primitive :** Z_prim(σ) = Σ_{w ∈ ℤ² primitif} |w|^{−σ} = 4ζ(σ/2)β(σ/2)/ζ(σ), où β est la fonction bêta de Dirichlet. Elle se prolonge en une fonction méromorphe, avec un pôle simple en σ = 2 de résidu 2π/ζ(2) = 12/π, et Z_prim(3/2) = −3,857623095.

## 1. Réduction exacte aux moyennes de cercles

La formule de Cauchy donne ΔP(R) = ∫₀^{2π} D_R(φ) dφ, où D_R(φ) = h_{RK}(φ) − h_{P_R}(φ) est la profondeur de la première calotte de direction φ qui contient un point de L.

Fixons φ. Au point du bord de RK de normale φ, la courbure vaut κ_a = κ/R. On pose s = ⅓ log(R/κ), soit e^{−s} = κ_a^{1/3}. Dans le repère (tangente, normale intérieure), l'application (x, y) ↦ (e^{−s}x, e^{s}y) :
- conserve les aires ;
- envoie le bord sur la courbe Y = X²/2 + ε₃X³ + …, avec ε₃ = O(R^{−2/3}) ;
- envoie L sur ℤ² k_{θ−φ} a_s + t′, avec t′ uniforme.

Comme θ est uniforme, il vient exactement :

E[D_R(φ)] = κ_a^{1/3} · [M(s) + ε_R(φ)],

où ε_R(φ) ne mesure que l'écart entre le bord et sa parabole osculatrice. **Aucune équirépartition n'intervient dans cette étape** : la moyenne sur θ est, par construction, une moyenne sur le cercle {ℤ² k_θ a_s}. Pour le disque, C_eff(R) = M(⅓ log R) au terme ε_R près : les simulations de la note mesurent directement M(s).

**Lemme Q (localisation quantitative, à rédiger).** ε_R(φ) = O(R^{−1/2}), uniformément en φ. Ingrédients :
1. La profondeur réelle est bornée par une constante absolue c₀ : une calotte de RK de profondeur c₀ contient un disque de rayon > √2/2, donc un point du réseau. D'où Z* ≤ c₀e^{s}, et |X| ≤ (2c₀)^{1/2}e^{s/2} pour le point le plus bas : il n'y a pas de queue à contrôler.
2. Formule de première variation : déplacer le bord de δ(X) le long de la normale change E_t[Z*] de ∫δ(X)·ϖ(X)·J(X) dX au premier ordre. Ici ϖ(X) est la densité de l'événement « le point du bord d'abscisse X est un point du réseau, et le plus bas », et J(X) est le saut moyen de Z* quand on retire ce point.
3. On a δ(X) = O(ε₃|X|³), ϖ(X) = O(min(1, |X|^{−3})) (queue de P(Z* > z) en z^{−3/2}) et J borné. D'où ε_R = O(ε₃·e^{s/2}) = O(R^{−1/2}).

Une borne pointuelle ne suffirait pas : quand le point le plus bas sort de la calotte, Z* peut sauter beaucoup. Mais ces sauts sont rares, et c'est ce que mesure ϖ.

La borne est sans doute très pessimiste. Le terme cubique est impair et la loi du cercle est invariante par la symétrie X ↦ −X (car ℤ² k_θ a_s, réfléchi, donne ℤ² k_{−θ} a_s) : sa contribution d'ordre un est donc nulle. Il reste le terme quartique, d'où O(R^{−1}) attendu. La borne O(R^{−1/2}) suffit.

**Conclusion de la réduction.** Avec dφ = κ ds, on a κ_a^{1/3} dφ = R^{−1/3} κ^{4/3} ds et κ_a^{1/3} e^{−s/2} dφ = R^{−1/2} κ^{3/2} ds. La conjecture découle donc de l'énoncé suivant sur les moyennes de cercles.

**Théorème B.** Sous l'hypothèse (H) du §5 :

M(s) = C − B·e^{−s/2} + O(e^{−(1/2+δ)s}), avec B = (√2/6π)·|Z_prim(3/2)|.

Sous (H) et le lemme Q, on obtient alors :

E[ΔP(R)] = C·∫κ^{4/3} ds·R^{−1/3} − B·∫κ^{3/2} ds·R^{−1/2} + O(R^{−1/2−δ/3}).

## 2. La pointe : le modèle des droites (démontré)

Soit Λ un réseau qui a un vecteur primitif court v = (x, y), avec x > 0. Ses points se rangent sur des droites parallèles à v, espacées de 1/|v|, et sont espacés de |v| sur chaque droite. Remplaçons chaque droite par la droite pleine, et notons Z*_∞ la profondeur obtenue.

**Lemme F (formule exacte).** E_t[Z*_∞] = F(x, y), avec τ = |y|/(√2·x) et :
- F = 1/(2x) − (4/3)·τ/√x + τ² si y² ≤ x/2 (régime intérieur) ;
- F = 1/(24y²) si y² ≥ x/2 (régime extérieur).

F est de classe C² au raccord y² = x/2 et ne dépend pas du décalage b entre rangées.

*Preuve.* Supposons y ≥ 0 et posons τ′ = y/x. Les droites s'écrivent Y = τ′X + c_k ; leur espacement vertical vaut 1/x et c₀ est uniforme modulo 1/x. La droite k rencontre A si et seulement si q_k := τ′² + 2c_k ≥ 0. Son point le plus bas dans A est alors l'extrémité X = τ′ − √q_k, de hauteur (τ′ − √q_k)²/2.

Les q_k positifs forment une progression de pas 2/x, d'origine uniforme. La variable U = √(2Z*_∞) = min_k |τ′ − √q_k| vérifie donc :
- P(U > u) = 1 − 2τ′xu pour u ≤ τ′ ;
- P(U > u) = 1 − (τ′ + u)²x/2 pour u ≥ τ′ ;

ces expressions étant tronquées à 0.

Si τ′² ≥ 1/(2x), c'est-à-dire y² ≥ x/2, U est uniforme sur [0, 1/(2τ′x)] et E[U²/2] = 1/(24y²). Sinon, E[U²/2] = ∫₀^∞ u·P(U > u) du = 1/(2x) − (2/3)τ′√(2/x) + τ′²/2, ce qui est la première formule. ∎

**Corollaire (intégrale transverse).** Φ(x) := ∫_ℝ F(x, y) dy = (√2/3)·x^{−1/2}, exactement. Le régime intérieur apporte √2/4 et le régime extérieur √2/12. Contrôle par quadrature : √x·Φ(x) = 0,4714045208 = √2/3, pour x de 10⁻⁶ à 0,04.

**Lemme L (encadrement).** Si v est le plus court vecteur de Λ et |v| ≤ ½, alors :

0 ≤ Ψ(Λ) − F(v) ≤ C₀·|v|, avec C₀ une constante absolue.

*Preuve.*
- *Minoration.* Les points du réseau sont sur les droites, donc Z* ≥ Z*_∞.
- *Majoration.* Sur la droite qui réalise Z*_∞, le premier point du réseau après l'extrémité basse est à une hauteur au plus Z*_∞ + |y|. Sa position le long de la droite est uniforme (moyenne sur t), d'où un excès moyen de |y|/2.
- *Cas rare.* Si la corde de cette droite est plus courte que |v|, il faut passer à une autre droite. Cet événement a une probabilité O(x³) dans le régime intérieur et O(x^{3/2}) près du raccord, pour un coût O(1/x). Sa contribution est donc O(|v|). ∎

Le Monte-Carlo sur de vrais réseaux (§7) donne (Ψ − F)/|v| entre 0,45 et 0,52 là où l'erreur statistique est ≤ 0,02, contre |y|/(2|v|) entre 0,48 et 0,50. L'excès moyen |y|/2 est donc presque atteint : le premier point de la droite minimisante est presque toujours le point le plus bas.

**Lien avec la note du 2 octobre.**
- *Régime intérieur* (y² < x/2) : v est presque tangent, et beaucoup de points sont alignés sur une même droite. Ce sont les « petits a ».
- *Régime extérieur* (y² > x/2) : v est presque normal, et les points forment deux colonnes. Ce sont les « grands a ». Le « vecteur partenaire » de la note est ici le vecteur court v lui-même. Avec x = 2m/a² et y = 1/a, la condition d'arête |m| < 1 de la note équivaut exactement à y² > x/2.

La note décompose le déficit par arêtes ; on le décompose ici par profondeur. Les deux décompositions répartissent différemment la même constante : √2/3 = g₀ + g₀/4 (avec g₀ = 4√2/15) dans la note, contre √2/4 + √2/12 ici.

## 3. Le second terme vient de la pointe (démontré)

Soit χ une fonction lisse, égale à 1 sur [0, ½] et à 0 sur [1, ∞[. Pour η ∈ ]0, ½], on pose g(v) = ½·F(v)·χ(|v|/η) et E_g(Λ) = Σ_{v ∈ Λ primitif} g(v) (transformée de Siegel). Si le plus court vecteur v de Λ vérifie |v| < η/2, alors E_g(Λ) = F(v) : seuls ±v contribuent, car tout autre vecteur primitif est de longueur ≥ 1/|v| > η.

**Lemme E.**

(1/2π) ∫₀^{2π} E_g(ℤ² k_θ a_s) dθ − ∫E_g dμ = (√2/6π)·Z_prim(3/2)·e^{−s/2} + O_η(e^{−(1−ε)s}), pour tout ε > 0.

*Preuve.*
1. **Moyenne de Haar.** Par la formule de Siegel, ∫E_g dμ = (1/ζ(2))∫g = (6/π²)∫₀^∞ Φ̃(x) dx, avec Φ̃(x) = ∫F(x, y)·χ(|(x, y)|/η) dy.
2. **Moyenne de cercle.** Pour w ∈ ℤ² primitif, w k_θ a_s = |w|·(e^{−s} cos ψ, e^{s} sin ψ), où ψ est uniforme. Ce vecteur n'entre dans le support de g que si |w| ≤ 2ηe^{s} et |sin ψ| ≤ ηe^{−s}/|w|, ce qui arrive deux fois par tour. Le changement de variable y = e^{s}|w| sin ψ donne, pour chaque w, une contribution (1/2π)·Φ̃(e^{−s}|w|)/(e^{s}|w|)·(1 + O(e^{−2s})).
3. **Écart.** Avec k(r) = Φ̃(r)/r, l'écart vaut :

   (1/2π)·[e^{−2s} Σ_{w primitif} k(e^{−s}|w|) − (1/ζ(2)) ∫_{ℝ²} k(|w|) d²w] + O(e^{−2s}).
4. **Mellin.** Pour c > 2, Σ_prim k(|w|/T) = (1/2πi) ∫_{(c)} k̃(σ)·T^σ·Z_prim(σ) dσ, où k̃ est la transformée de Mellin de k.
   - Près de 0, k(r) = (√2/3)·r^{−3/2} − φ₁(0)·r^{−1} + O(r), où φ₁ est la part de Φ coupée par χ, lisse et paire.
   - k est C² sur ]0, ∞[ et à support compact, donc k̃(σ) = O(|σ|^{−2}) sur les droites verticales.
   - On déplace la droite d'intégration jusqu'à Re σ = 1 + ε. Le pôle σ = 2 de Z_prim redonne exactement le terme de Haar. Le pôle σ = 3/2 de k̃ donne (√2/3)·Z_prim(3/2)·T^{3/2}.
   - Sur Re σ = 1 + ε, 1/ζ(σ) est borné et ζ(σ/2)β(σ/2) = O(|σ|^{1/2}) (borne de convexité). L'intégrale restante est donc O(T^{1+ε}).
   - Avec T = e^{s}, on obtient le lemme. ∎

Contrôle numérique (coupure lisse) : Σ_prim |w|^{−3/2}·χ(|w|/T) − (6/π²)·2π·T^{1/2}·∫₀¹ r^{−1/2}χ(r) dr vaut −3,8577 ± 0,0001 pour T de 100 à 1 999, contre Z_prim(3/2) = −3,85762.

**Conséquence.** On écrit Ψ = E_g + Ψ_rem. Alors :

M(s) − C = [Lemme E] + [M_{Ψ_rem}(s) − ∫Ψ_rem dμ],

où M_f désigne la moyenne de cercle de f. Le premier crochet vaut exactement −B·e^{−s/2} + O(e^{−(1−ε)s}). Il reste à montrer que le second est o(e^{−s/2}) : c'est l'hypothèse (H).

Le signe est le bon : Z_prim(3/2) < 0 parce que ℤ² n'a aucun vecteur de longueur < 1, région où |w|^{−3/2} est le plus grand. Le cercle visite donc moins la pointe que la mesure de Haar, et C_eff tend vers C par valeurs inférieures.

## 4. Identité de Mellin pour ρ : B_grands = B_petits/4 (démontré)

La note du 2 octobre (§3.5) définit :
- ρ(λ) = (πλ/8)·Σ_{v primitif, |v| < 1/λ} (1 − λ²|v|²)/|v| ;
- B_grands = −(6/π²)·(1/9)·(√2/4)·∫₀^∞ λ^{−3/2}(ρ(λ) − 1) dλ, intégrale évaluée numériquement à −2,4238.

**Proposition.** ∫₀^∞ λ^{−3/2}(ρ(λ) − 1) dλ = (π/5)·Z_prim(3/2) = −2,423816…

*Preuve.*
1. Pour Re σ > 0, chaque v contribue ∫₀^{1/|v|} λ^{σ−1}·(πλ/8)(1 − λ²|v|²)/|v| dλ = (π/4)·|v|^{−σ−2}/((σ+1)(σ+3)). Donc ∫₀^∞ λ^{σ−1}ρ(λ) dλ = (π/4)·Z_prim(σ+2)/((σ+1)(σ+3)).
2. On a ρ = 0 pour λ ≥ 1. En 0, ρ(λ) − 1 = O(λ log²(1/λ)), par le comptage des vecteurs primitifs, dont l'erreur est O(r log r).
3. Pour −1 < Re σ < 0, ∫₀^∞ λ^{σ−1}(ρ − 1) dλ est donc le prolongement analytique du même membre de droite : le −1 compense exactement le pôle en σ = 0.
4. En σ = −½, le membre de droite vaut (π/4)·Z_prim(3/2)/(5/4) = (π/5)·Z_prim(3/2). ∎

Contrôle : la somme sur |v| < 2 000 donne −2,42382.

**Conséquences.**
- B_grands = (6/π²)·(1/9)·(√2/4)·(π/5)·|Z_prim(3/2)| = (√2/30π)·|Z_prim(3/2)|.
- Comme B_petits = (g₀/2π)·|Z_prim(3/2)| = (2√2/15π)·|Z_prim(3/2)|, on a exactement B_grands = B_petits/4.
- B = B_petits + B_grands = (√2/6π)·|Z_prim(3/2)|.

C'est la constante du lemme E, obtenue par une voie indépendante : la somme par arêtes de la note, avec son hypothèse d'équirépartition du partenaire. Les deux calculs concordent exactement.

## 5. Ce qui reste : l'hypothèse (H)

On pose Ψ_rem = Ψ − E_g. Ce qui est établi :
- Ψ_rem = Ψ sur la partie compacte {λ₁ ≥ η}, où λ₁ est la longueur du plus court vecteur ;
- 0 ≤ Ψ_rem ≤ C₀·λ₁ sur la pointe {λ₁ < η/2} (lemme L).

Ψ_rem est donc bornée, continue, et tend vers 0 au fond de la pointe.

**Hypothèse (H).** Il existe δ > 0 tel que |M_{Ψ_rem}(s) − ∫Ψ_rem dμ| = O(e^{−(1/2+δ)s}).

**Pourquoi (H) est attendue.**
1. **Fonctions lisses.** Pour f lisse sur X₂ (normes de Sobolev finies), M_f(s) − ∫f dμ = O(s·e^{−s}). Esquisse, à rédiger avec des normes de Sobolev adaptées à la pointe :
   - f ↦ ∫_K f(k) dk est une fonctionnelle invariante par K ; dans chaque représentation irréductible π de L²(X₂), elle est proportionnelle au vecteur sphérique u_π ;
   - l'écart vaut donc Σ_π u_π(i)·⟨π(a_s)f_π, u_π⟩, plus l'intégrale analogue sur le spectre continu (séries d'Eisenstein) ;
   - pour SL₂(ℤ), toutes les π non triviales sont tempérées, car il n'y a pas de valeur propre exceptionnelle ;
   - la borne de Cowling–Haagerup–Howe donne |⟨π(a_s)v, u⟩| ≤ ‖v‖·‖u‖·Ξ(a_s), avec Ξ(a_s) ≍ (1 + s)e^{−s}, car les K-types de SL₂ sont de dimension 1.
2. **Ψ_rem n'est pas lisse.** Elle présente un pli lipschitzien le long de l'hypersurface S des réseaux qui ont un vecteur primitif horizontal (parallèle à la tangente).
   - Origine : le bord supérieur plat de la calotte {X²/2 ≤ Y ≤ z}. Deux translatées de la calotte par un vecteur horizontal ont leurs bords plats parallèles, et l'aire de leur intersection a un point anguleux.
   - Ailleurs, les contacts tangents entre arcs de parabole donnent des raccords en distance^{3/2}, plus réguliers.
3. **Les cercles coupent S transversalement.** Pour un w donné, la composante normale y = e^{s}|w| sin ψ varie à la vitesse e^{2s}x par unité de θ. La fraction du cercle à distance < δ de S est donc O(δ).
   - En lissant Ψ_rem à l'échelle δ, l'erreur commise sur la moyenne de cercle est O(δ²), et non O(δ).
   - Le coût en norme de Sobolev est une puissance négative de δ.
   - On obtient un taux e^{−cs} avec c > 1/2 : un décompte grossier des normes de Sobolev donne déjà c = 2/3.
4. **Données.** Les simulations du disque jusqu'à R = 10⁶ donnent B = 0,289 ± 0,001 à C fixé, pour 0,28942 prédit par la seule pointe. Aucune contribution du cœur n'est visible à l'ordre R^{−1/6}.

**Lemme R (à démontrer).** Ψ est de classe C² hors de S ∪ T, où T est l'ensemble des contacts tangents. Elle a une singularité en distance^{3/2} le long de T et un pli lipschitzien à travers S, avec des bornes polynomiales en la hauteur dans la pointe.

Avec le lemme R, les points 1 et 3 donnent (H), et le théorème B s'ensuit.

## 6. Bilan

| Étape | Statut |
|---|---|
| Réduction de E[ΔP] aux moyennes de cercles M(s) (§1) | démontrée : formule de Cauchy et changement de variables exact |
| Lemme Q : bord contre parabole osculatrice (§1) | à rédiger, routinier ; erreur O(R^{−1/2}), O(R^{−1}) attendue |
| Lemme F et Φ(x) = (√2/3)·x^{−1/2} (§2) | démontrés |
| Lemme L : 0 ≤ Ψ − F ≤ C₀·\|v\| (§2) | démontré |
| Lemme E : la pointe donne −B·e^{−s/2} (§3) | démontré |
| Forme close de B et B_grands = B_petits/4 (§4) | démontrées |
| Hypothèse (H) : cœur, taux meilleur que e^{−s/2} (§5) | ramenée au lemme R, non démontrée |

**Énoncé obtenu (conditionnel).** Soit K un convexe à bord C⁴ et κ > 0. Sous (H) et le lemme Q :

E[ΔP(R)] = C·∫κ^{4/3} ds·R^{−1/3} − B·∫κ^{3/2} ds·R^{−1/2} + O(R^{−1/2−δ/3}),

avec C = 0,7192331749 et B = (√2/6π)·|Z_prim(3/2)| = 0,2894234179.

## 7. Contrôles numériques

Script `verif_second_terme.py` (NumPy, mpmath ; 4 secondes).

| Contrôle | Résultat |
|---|---|
| Z_prim(3/2) = 4ζ(3/4)β(3/4)/ζ(3/2) | −3,857623095, avec ζ(3/4) = −3,441285387 et β(3/4) = 0,732107218 |
| B, forme close | 0,2894234179 ; B_petits = 0,2315387, B_grands = 0,0578847 |
| ∫λ^{−3/2}(ρ − 1) dλ, somme sur \|v\| < 2 000 | −2,42382, contre (π/5)·Z_prim(3/2) = −2,423816 |
| √x·Φ(x), quadrature exacte, x de 10⁻⁶ à 0,04 | 0,4714045208 = √2/3 |
| Somme d'Epstein à coupure lisse, T de 100 à 1 999 | −3,8577 ± 0,0001, contre −3,85762 |
| Indépendance en b (x = 0,01, au raccord) | 8,360 ; 8,354 ; 8,353 (± 0,012), pour F = 8,333 |

**Modèle des droites contre vrais réseaux** (Monte-Carlo, 4·10⁵ translations par point ; extrait) :

| x | y/√(x/2) | Ψ | F | (Ψ − F)/\|v\| | \|y\|/(2\|v\|) |
|---|---|---|---|---|---|
| 0,04 | 2 | 0,6616 ± 0,0007 | 0,5208 | 0,493 ± 0,003 | 0,495 |
| 0,04 | 4 | 0,4046 ± 0,0003 | 0,1302 | 0,484 ± 0,001 | 0,499 |
| 0,01 | 2 | 2,1527 ± 0,0029 | 2,0833 | 0,489 ± 0,021 | 0,499 |
| 0,01 | 4 | 0,6609 ± 0,0007 | 0,5208 | 0,495 ± 0,003 | 0,500 |
| 0,0025 | 0 | 200,06 ± 0,18 | 200,00 | 22 ± 73 | 0 |
| 0,0025 | 4 | 2,1563 ± 0,0029 | 2,0833 | 0,516 ± 0,021 | 0,500 |

Dans le régime intérieur, F ≈ 1/(2x) domine et l'écart Ψ − F est dans le bruit, comme le prévoit le lemme L (|y|/2 est petit devant F).

## 8. Pistes

1. **Démontrer le lemme R.** On écrit v(z; Λ) = 1 − aire(A(z) mod Λ) par inclusion-exclusion sur les translatées de A(z) = {X²/2 ≤ Y ≤ z}, puis Ψ = ∫₀^∞ v(z; Λ) dz. On suit ensuite les singularités de l'aire d'intersection de deux translatées :
   - un pli quand les bords plats sont parallèles (S) ;
   - une puissance 3/2 pour les contacts tangents (T).
2. **Contrôle direct du théorème B.** Mesurer M(s) par Monte-Carlo pour e^{s} jusqu'à 10⁶, soit R/κ jusqu'à 10¹⁸, très au-delà des simulations du disque. Il faut alors traiter la pointe exactement par F, et ne simuler que Ψ − F, qui est bornée : sans cela, la variance infinie de Z* rend l'estimation inutilisable.
3. **Dimension 3 (heuristique, à vérifier).** Le même mécanisme, avec les vecteurs courts de ℤ³ (droites denses) et les plans denses, prédit une correction relative d'ordre R^{−1/2}, à un logarithme près. La note 3D mesure un exposant apparent de 0,4 à 0,5 entre R = 10² et 10⁴.
4. **Rédaction.** Intégrer les §2 à §4 au manuscrit fusionné : ce sont des énoncés autonomes et complets. Présenter le second terme comme théorème conditionnel à (H), avec la forme close de B.
