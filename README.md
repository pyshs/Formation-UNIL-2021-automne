# Formation PySHS UNIL automne 2021

Intervenants : [Émilien Schultz](http://eschultz.fr) et Léo Mignot

(:warning: Github a du mal à rendre les Notebooks en ligne ; si cela vous arrive, Vous pouvez télécharger tous le dossier avec Code > Download zip)


## Déroulement de la formation

Les séances ont lieu en ligne les mardis de 16h à 18h, suivi d'un espace libre d'échange après la séance pour ceux et celles qui sont disponibles. En fonction des centres d'intérêt des inscrit.e.s, certaines thématiques abordées pourront être modifiées. [Page de la formation](https://news.unil.ch/display/1633344954933).
 
Prérequis pour la première séance : installation du logiciel Anaconda qui installe les outils nécessaires (Python ainsi que les autres interfaces) : https://www.anaconda.com/products/individual
 
Dépôt de la formation : https://github.com/pyshs/Formation-UNIL-2021-automne
 
### 02.11 - Pourquoi programmer en Python? 
 
Cette première séance sera l'occasion de faire un petit tour du langage Python et de l'univers qui l'entoure, ceci pour identifier les principaux usages en sciences humaines et sociales. Nous verrons ensuite de manière pratique les bases du langage en nous familiarisant avec les Notebook Jupyter permettant d'exécuter des lignes de code de manière interactive. 
 
### :warning: Date déplacée. 11/11 - Les blocs de base du langage

Cette séance portera sur la structure d'un script autour des principaux blocs qui constituent un script : boucle, condition, ouverture d'un fichier, mais sera aussi l'occasion d'approfondir nos connaissances sur la manipulation de données. Nous verrons en particulier comment manipuler des données textuelles.
 
### 16.11 - S'appuyer sur la puissance des bibliothèques pour le traitement de données

Quand on parle de Python, on parle à la fois du langage en lui-même et des outils développés à partir de celui-ci. Les bibliothèques regroupent des outils déjà constitués pour réaliser des traitements plus avancés. Nous verrons comment identifier une bibliothèque, l'installer et l'utiliser, avec des exemples autour de la récupération de données sur internet.
 
### 23.11 - Manipuler des tableaux de données avec Pandas
 
Nous allons plonger un peu plus en détail dans l'univers spécifique de la bibliothèque Pandas qui permet de faire le lien entre des manipulations de fichier tableaux (comme Excel) et l'automatisation de certaines tâches. Cela nous amènera à charger des fichiers, à manipuler les colonnes en recodant certaines informations et à calculer des statistiques descriptives.  
 
### 30.11 - Statistiques et visualisations
 
Une fois les données nettoyées et recodées, la porte est ouverte aux traitements plus avancées. Nous verrons comment mettre en oeuvre les statistiques habituelles en SHS, et comment produire des visualisations en nous appuyant sur Pandas et la bibliothèque Matplotlib. 
 
### 07.12 - Petit tour des usages avancées de traitements des données

Les séances précédentes ont permis de voir plusieurs usages de Python, en particulier orientés vers le traitement de données. Dans cette séance, nous aborderons des usages plus avancés allant de l'automatisation dans la collecte de données à la production de cartes ou la mise en place de stratégies de traitement de corpus textuels ou d'images.

## Préparer les séances

### Rapide panorama

Python est un langage interprété qui nécessite un environnement. 

Il existe plusieurs manières de l'utiliser :
- Sur votre ordinateur, avec Anaconda (ci-dessous)
- Sur le Cloud, avec différentes solutions, par exemple Google colab https://colab.research.google.com/

### Installation d'Anaconda

Anaconda est un environnement qui fournit l'ensemble des éléments nécessaires pour exécuter du code python. Il permet de construire des environnements (une version du langage et de librairies spécifiques) et de travailler au sein de ces environnements permettant d'en avoir plusieurs (par exemple, pour tester des versions différentes de librairies, etc.)

- Télécharger Anaconda pour votre OS : https://www.anaconda.com/distribution/
- Installer (suivant que vous soyez sous Windows, Linux ou Mac, la procédure va changer)
- Lancer Anaconda pour créer un environnement de travail
  - Sur windows : Aller dans environnements > Create > donner un nom (ex. p38) et une version de python 3.8 (__Attention bien installer la version 3.8 ou plus de Python __)
  - Sur linux/mac : Ouvrir un terminal, puis créer un environnement en tappant la commande : conda create --name p38 python=3.8 (pour toute information sur les commandes conda : https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- Lancer python (sur windows en lançant Anaconda ; sous linux/mac en tapant la commande source activate p38 dans un terminal)
- lancez un terminal (vous pouvez le faire sous le logiciel Anaconda) et vérifiez que ipython est bien installé en tapant ipython de manière similaire, lancez Jupyter notebook en tapant jupyter notebook

Autres logiciels : vous pouvez installer Sublime text : https://www.sublimetext.com/ (pour visualiser des documents textes)
