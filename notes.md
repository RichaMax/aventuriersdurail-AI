# observation space
- id du joueur ?

- etat de la carte (ville reliées - par qui - et chemin libre, c'est la matrice route matrix avec les id des joueur)

- pioche
    - taille de la pioche (nb cartes restantes)

    - 5 cartes wagon face visible de la pioche (encodé)

    - nombre de cartes dans la défausses

- Nombre de wagon restant

- nombre de wagon restant joueur i

- ...

- carte wagons en main (encodé)

- cartes destination à faire (plein de fois des sous matrice de la matrice route avec juste les villes, ou un juste une sous matrice correspondant à la addition de toutes les sous matrices [modulo(1)])

- cartes en main joueur i

- ...

- nombre de point avec les cartes destinations (et donc bonus et malus)

- nombre de point joueur i (sans les cartes destinations parce que tu connais jamais celles de tes adversaires sauf après la game)

- ...

- Cartes wagons à piocher si action qui le fait

- Les actions possible

# les actions

Soit on fait ça

>ya des action qui termine le tour et d'autres non.

> Ici on veut d'abord voir si les modèles vont arriver à apprendre comment choisir les cartes wagons (les cartes destination etant pour l'instant prisent aléatoirement)

>- Prendre des cartes destination => action final directement
>- Poser des wagons sur un tronçons => action final
>- Piocher une carte wagon => c'est pas finit faut en repiocher une (on call 2 fois la même méthode dans ce cas)

Soit ça

>a chaque tour tu fais 1 ou 2 actions. Du coup un tour ça peut être un ou deux step
> 
>
> à chaque step tu calculs un masque des actions possible pour le joueur.
>- Tu poses un train => action poser un train
>- Tu pioches une carte destination et tu les choisis => (piocher destinations, choisir une combinaison parmi tout les arrangements possible: choisir la première carte destination, choisir les deux premiere, choisir premiere et troisieme, les trois, ...)
>- tu piches deux fois un carte wagon. Tu choisis parmi, la face caché ou une des 5 face visible
>
>
>
>
>
>


# Par rapport aux cartes destinations

Normalement, il faudrait que à la fin l'IA soit capable en début de partie de determiner les deux meilleurs choix de cartes destination parmi les 3 ou bien prendre les 3. Et aussi d'effectuer le meilleure choix entre 1, 2 ou 3 cartes destinations et lesquelles quand elle fait l'action "choisir des cartes distinations".

Mais pour l'instant on va éviter cette complication en disant que c'est aléatoire:
- Au premier tour, les joueurs se voient assigner entre 2 et 3 cartes destinations (le choix des cartes parmi les 3 est aussi aléatoire 1-2 1-3 2-3)
- Pendant les autres tours, on est aussi sur de l'aléatoire mais en prenant en compte que cette fois ci on peut en avoir que une seule.

Alors ça rajoute bc d'aléatoire au jeu mais ça permet de faire abstraction de cette régle pour coder la V1 du jeu. On fera la V2 ou l'IA choisit quand toutes les autres actions seront claires et fonctionnelles.


# Condition de fin jeu V1

comme je l'imagine la maintenant, pour la fin de jeu:
- on check à chaque fois que un joueur finit un tour peu import l'action le nombre le train qui lui reste
- Si y en a un qui en a plus que 0, 1 ou 2, on entre dans le dernier tour
    => partie special de l'env mb une sous classe qui gère le dernier coup de chaque et fait le décompte, ou juste un counter qui commence à 0 et qui prendre +1 à chaque coup et quand il est égale au nombre de joueur ça stop le jeu, fait les compte et distribue les rewards ? 
- sinon, bah tranquille ça continue