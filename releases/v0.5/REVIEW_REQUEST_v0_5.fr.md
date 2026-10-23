# Appel à relecture humaine : reste explicite du déficit moyen de périmètre du disque

Nous sollicitons une relecture mathématique critique d’une preuve proposée et de son complément quantitatif, dans le cadre du projet Dynagénèse de Patrick Royer, chercheur indépendant non affilié.

Pour le disque fermé $D_R$ de rayon $R$, et une translation $t$ uniforme dans $[0,1)^2$, l’observable est

$$
m(R)=\mathbb E_t\left[2\pi R-P\left(\mathrm{conv}(D_R\cap(\mathbb Z^2+t))\right)\right].
$$

Le dossier propose un développement

$$
m(R)=2\pi(CR^{-1/3}-BR^{-1/2})+r(R),
$$

où $C=\mu(\Psi)$ est la moyenne de Haar d’une profondeur parabolique moyennée sur les translations, et $B=-\sqrt2\,Z_{\mathrm{prim}}(3/2)/(6\pi)$. La valeur $Z_{\mathrm{prim}}(3/2)$ est obtenue par prolongement analytique, et non par la somme positive divergente à cet exposant.

Le complément propose, pour tout $R\ge2$,

$$
|r(R)|\le2\pi\left[2{,}5\times10^9\left(1+\frac{\log R}{3}\right)R^{-11/21}+2000R^{-7/12}\right]+550000R^{-4/3}.
$$

**Statut : preuve proposée, développée et contre-relue avec assistance IA. Aucune expertise humaine indépendante ni vérification formelle n’est attestée.** Les contrôles arithmétiques reproductibles portent sur le calcul du majorant, sans constituer une vérification informatique de la preuve.

La borne est volontairement très conservatrice et non informative aux rayons déjà calculés, notamment 50 et 1600. Le seuil $R_0=2$ indique son domaine de validité proposé, pas le début observable du régime asymptotique. Elle ne permet pas de valider numériquement $C$ ou $B$ à ces rayons.

Nous demandons en priorité un avis sur trois points :

1. **Identités géométriques.** Les formules exactes de compétition entre rangées et de correction de corde courte, leurs prolongements aux axes et le contrôle des dérivées justifient-ils la régularité globale de $\Psi-E_g$ et le transfert vers le disque ?
2. **Chaîne analytique quantitative.** La sommation de Stieltjes, les normalisations primitives et spectrales, puis le lissage par chaleur justifient-ils les trois majorants annoncés ? La coupure explicite $C^2$ remplace ici la coupure lisse abstraite de la preuve initiale.
3. **Possibilité d’une borne utile.** Une estimation adaptée à cet observable permettrait-elle de réduire substantiellement les pertes des normes globales et de l’estimation circulaire ?

Une objection localisée, un contre-exemple, une référence pertinente ou une correction d’un seul maillon seraient déjà utiles. Nous ne sollicitons pas une approbation générale du projet.

Le dossier joint contient la note de neuf pages, le manuscrit de départ, les dérivations détaillées, le compte rendu de contre-lecture IA, les sources LaTeX et le calcul rationnel reproductible. Aucun nouveau Monte-Carlo n’a été utilisé pour ce complément.

Feedback / retours : https://github.com/royerpatrick-ops/dyn-validex-cinf-deficit-perimetre/issues
