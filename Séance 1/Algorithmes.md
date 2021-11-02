# Quelques notions sur les algorithmes

Avant même de comprendre les particularités d’un langage, c’est-à-dire la manière d’écrire des lignes de code, il est intéressant d’avoir une idée de comment penser le déroulement de ces instructions. Dit autrement, de savoir construire un plan général.

Un **algorithme est une succession d’opérations élémentaires** (une séquence d’instructions) qui permettent de résoudre un problème, donc d’atteindre un objectif. Cette notion très générale d’algorithme se retrouve au coeur des mathématiques : beaucoup de calculs sont des algorithmes, une suite d’étapes à réaliser1. Elle se retrouve aussi dans toute activité nécessitant de combiner des étapes : manuel de montage d’une étagère, recette de cuisine, etc.

Construire un algorithme consiste donc à donner les éléments pour résoudre de manière systématique un problème. En d'autres termes, un algorithme ne doit demander aucune initiative à celui ou celle qui l'exécute. 

Un ordinateur est un outil permettant de réaliser plein d’opérations élémentaires (afficher sur un écran, faire un calcul compliqué, lire un fichier, etc.). Cependant, un ordinateur n'étant capable d'aucune initiative, il ne peut exécuter une tâche que si on lui fournit strictement un algorithme pour le faire. Tout programme informatique a donc, par définition, la structure d'un algorithme2. L’objectif de la programmation est alors de définir un algorithme qui part des opérations élémentaires disponibles (les actions possibles de l’ordinateur), et les applique les unes après les autres en respectant certaines règles. Tout l’enjeu est de construire la bonne séquence d’actions.

Un algorithme au sens très large n’a pas besoin d’un langage particulier pour être formalisé : vous pouvez le décrire avec la langue courante, sous la forme d’un pseudo-code : l’étape 1 fait ceci, l’étape deux fait cela… La mise en œuvre concrète sera alors de le traduire dans un langage spécifique, adapté à vos usages.

Un point important est donc qu’un algorithme – un script en programmation – a un début, puis se décompose en une série d’opérations – et s’arrête généralement à un moment.

Comme il n’existe pas une infinité de manière de décrire des opérations, des blocs de base se retrouvent dans presque tous les algorithmes. Cela donne un air de famille entre les différents langages. Ces blocs de base sont alors :

1. des variables, c’est à dire des espaces avec un nom spécifique qui permettent de conserver de l’information et de la modifier. La question se pose alors de la forme de cette information : des nombres, des textes, des listes, bref… elle peut être de plusieurs types.

2. des opérations d’entrée, c’est à dire des moments où de l’information va être donnée à votre algorithme : lire un fichier, une entrée au clavier, etc. 

3. des opérations de sortie, c’est à dire des affichages sur un écran, de l’écriture dans un disque dur, etc.

4. des opérations spécifiques qui permettent de traiter l’information, souvent appelées fonctions : par exemple calculer la moyenne, la taille d’une variable, etc. Ces fonctions qui sont des actions vont évidemment dépendre du matériel que vous allez utiliser (dans certains langages, certaines fonctions vont être disponibles, pas d’autres).

5. des embranchements ou conditions qui permettent de réaliser ou non une action en fonction de l’état général de l’algorithme. La structure la plus simple est de se demander si quelque chose est vrai, et ne faire l’action que si c’est le cas. Une version évoluée est de donner aussi une instruction à exécuter si ce n’est pas vrai.

6. la répétition un certain nombre de fois d’une opération : au lieu d’écrire 10 fois la même instruction, dire de répéter l’opération 10 fois. Ou bien répéter tant qu’une certaine situation n’est pas rencontrée.

A partir de ces éléments de base, il est alors possible de construire des procédures plus ou moins complexes.

Dans de nombreux cas bien définis, des « bonnes » façons d’écrire ces étapes ont été identifiées, et vous pourrez les trouver dans les manuels, comme trier un tableau ou faire le plus rapidement certains calculs. Cependant, quand vous voulez atteindre des objectifs plus spécifiques à vos besoins, ou plus complexes, c’est à vous de trouver une manière d’écrire l’algorithme adapté, potentiellement en combinant des morceaux de solutions existantes.

S’il existe beaucoup de manière d’écrire un algorithme, une question souvent centrale est son efficacité. En effet, un enjeu pour résoudre efficacement un problème est le nombre d’étapes nécessaires, et donc le temps que cela va prendre. Si vous voulez trouver dans un très gros ensemble de données une information particulière, quelle est la manière la plus efficace ? Le domaine de l’algorithmique apporte des résultats à ces questions.

En particulier, une notion particulièrement importante est celle de la complexité d’un algorithme. En effet, un algorithme vise souvent à traiter des entrées. La question est donc : est-ce que cela prend plus de temps si on augmente la taille de l’entrée ? Dans certains cas, cela peut prendre un peu plus de temps. Dans d’autres, au contraire, le temps explose. Pour cela, il faut décomposer les étapes, les boucles, et identifier les conséquences en termes de nombre d’opérations si les entrées sont différentes.



















