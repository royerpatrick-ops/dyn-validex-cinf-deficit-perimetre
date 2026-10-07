DYN-CINF_CORRECTIVE_v0_2 — 7 octobre 2026

Lecture principale :
manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.pdf

Le PDF est une corrective distincte en anglais de 8 pages. Le texte source .tex
permet son édition. NOTE_CORRECTIVE_FR.txt présente les changements en français.
Le modèle local est corroboré, la constante globale est conjecturale et le
second ordre reste exploratoire. Aucun nouveau résultat certifié n'est annoncé.

Les deux pièces reçues sont conservées dans originals/. Le reçu d'identité est
evidence/originals_preservation.json. SHA256SUMS.txt couvre les fichiers de ce
dossier, sauf lui-même.

Les programmes corrigés se trouvent dans scripts/. Leur guide README.md donne
les commandes Python et PowerShell, leurs dépendances et les options de calcul.
Aucune simulation ne démarre lors de l'import d'un module. Aucun lancement ne
publie ni n'envoie le dossier.

Validation des scripts : 10/10 contrôles ciblés PASS, 7/7 commandes de lancement
PASS. Les sorties de ces essais frugaux sont rangées dans
evidence/CLI_SANITY_OUTPUTS/ et servent à vérifier le fonctionnement seulement.
Leurs estimations à faible effectif ne remplacent aucune estimation scientifique
du manuscrit. Les ajustements historiques ne sont pas recalculés sans leur CSV.

Le programme historique de certification Arb et le CSV reanalysis_92_points.csv
ne figurent pas dans les pièces reçues. La corrective ne fabrique aucun de ces
éléments. Leurs reprises ultérieures devront s'appuyer sur les véritables sources.

Pour recomposer le PDF avec une installation LaTeX, depuis ce dossier :
pdflatex -output-directory=manuscript manuscript/DYN-MANUSCRIT_CINF_DEFICIT_PERIMETRE_v0_2.tex
Répéter une deuxième fois pour résoudre les références croisées.

Les licences des dépôts sources restent celles décidées par l'auteur ; cette
corrective n'en crée ni n'en remplace les termes.
