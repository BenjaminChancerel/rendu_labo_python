# TP class python 

## Sommaire
- [POO](#poo)
  - [I. Card ](#i-card)
  - [II. Cards ](#ii-cards)
  - [III. Game ](#iii-game)
  - [IV. Rendu ](#iv-rendu)


## I. Card 

**Voir commit numéro 1 (card) sur le git**

Comme demander dans la consigne j'ai donc créer un classe card avec les attributs value et color.

J'ai créer la méthode GetClasses pour pouvoir accéder aux attributs plus proprement et la méthode display pour afficher la valeur de la carte

## II. Cards 

**Voir commit numéro 2 (cards) sur le git**

Comme demander dans la consigne, j'ai ici créer une classe cards avec des attributs list et counter pour la liste des cartes que vous allez avoir en main
et le counter pour le nombre de carte que vous allez avoir en main.

on rentre alors dans la fonction piocher : 
  - En premier lieu cette fonction va vérifier si vous voulez piocher une carte "yes". Si ce n'est pas le cas elle vous demandera de voir ailleurs
  - Ensuite si la condition est vérifié, elle va enregister dans la list une valeur entre 1 et 52 qui sera votre nouvelle carte.
  - Puis elle va incrémenter le compteur.
  - Enfin elle vous affiche la liste de vos cartes et le nombre de cartes que vous avez