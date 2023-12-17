# Projet répertoire (base de données)

Ce projet a été réalisé par Maxan FOURNIER et Martin LEMEE (classe de Terminale F, groupe NSI) et porte sur l'élaboration d'un répertoire de contacts.

## Prérequis

Afin de lancer le projet :

-   Une version relativement récente de **Python** doit être installée (le projet a été testé avec **Python 3.11.7**) ;
-   La bibliothèque **customtkinter** doit également être ajoutée (`pip install customtkinter`).

Le projet peut ensuite être exécuté à l'aide de la commande `python main.py`.

## Structure du projet

Le projet est divisé en 4 fichiers distincts.

-   `main.py`: C'est le fichier qui permet de lancer le programme.
-   `repertoire.py`: Définit la classe Repertoire, qui gère les interactions avec une base de données SQLite pour stocker et manipuler les informations de contact.
-   `interface.py`: Responsable de l'interface graphique utilisateur, utilise la bibliothèque "customtkinter".
-   `contacts.sqlite`: Base de données présente dans le cadre de tests, contenant par défaut 2 contacts.

## Statut d'implémentation

-   [x] Menu (sous forme d'interface graphique)
-   [x] Ajout d'un contact dans la base de données
-   [x] Suppression d'un contact
-   [x] Demande de confirmation avant la suppression
-   [x] Affichage de tous les contacts dans l'ordre spécifié
-   [x] Recherche parmi les contacts
-   [x] Quitter l'application
-   [x] Interface graphique
-   [x] Code propre
-   [x] Code optimisé
-   [x] Commentaires

## Contact

Pour toute information supplémentaire, veuillez nous contacter aux adresses mail suivantes :

-   `mfournie@immacjp2.fr`
-   `mlemee@immacjp2.fr`
