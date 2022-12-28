# scrapping-linkedin

L'objectif de ce projet est de répondre à la "user story" suivante :
En tant qu'utilisateur, je veux pouvoir récupérer les informations 
du curriculum vitae linkedin associées à tous les comptes linkedin 
spécifiques pour un nom et prénom.
Optionnellement, je dois pouvoir récupérer ces données pour un compte 
spécifique si je connais l'identifiant spécifique du compte.

## Contraintes

Ce projet doit être réalisé en python en respectant les contraintes suivantes :

1) Resecter les bonnes pratiques de structuration d'un projet : 
   https://docs.python-guide.org/writing/structure/

2) Utiliser "unitest" ou "pytest" pour les tests unitaires avec un couverture minimum de 70%.

3) Ce programme doit pouvoir être utilisé en environnement de dev, preprod ou prod. Les variables d'environnement seront utilisées pour passer les données spécifiques à un environnement.

4) Une première version doit pouvoir fonctionner en ligne de commande et afficher les résultat sur la sortie standard

5) La version définitive doit être en mode API et doit au choix de l'utilisateur soit :
   - restituter les résultats sour la forme d'un JSON
   - stocker les résuslats JSON dans un bucker S3 avec l'identifiant de compte comme nom de l'objet.

6) Utiliser le  workflow "Git Workflow" pour la gestion des branches et du versionning.


 
