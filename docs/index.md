---
layout: home
---

Les CFF sont reconnus pour leur excellence en matière de transport ferroviaire en comparaison avec les pays voisins. D'un point de vue purement topologique, le réseau ferré Suisse est maillé et décentralisé, contrairement au réseau Français en étoile, polarisé autour de Paris. 

Cependant, des disparités en matière d’offre ferroviaire peuvent apparaître dans certaines régions suisses. En effet, les niveaux d’investissement en infrastructure sur le réseau ferroviaire n’ont pas profité équitablement aux différents cantons suisses. Ces inégalités peuvent être perçues en observant les projets de développement entrepris par les CFF. Par exemple, la plupart des projets de [Rail 2000](https://en.wikipedia.org/wiki/Rail_2000) proposent principalement des améliorations en Suisse alémanique. Ce n’est que récemment que l’importance a été donnée à la Suisse romande à travers les projets comme [Léman 2030](https://company.sbb.ch/fr/entreprise/projets/suisse-romande-et-valais/leman-2030.html) et Léman Express. 
<br/><br/>
**La typologie du réseau ferroviaire helvétique traduit-elle des particularités territoriales suisses ?**
<br/><br/>
Il s’agira dans ce travail d'analyser la topologie du réseau ferroviaire suisse d’un point de vue (purement) mathématique. Dans un premier temps, nous étudierons les données [GTFS](https://developers.google.com/transit/gtfs/?hl=fr) (*General Transit Feed Specification*) mises à disposition par les CFF afin de construire un graphe représentant le réseau ferré. Ensuite, à l’aide d’outils d’analyse de graphes, nous étudierons les propriétés de ce dernier pour détecter des particularités territoriales et créer une typologie. 

Une telle modélisation nous permettra donc d'étudier les différentes propriétés du réseau comme la centralité des gares ou encore le poids de certains tronçons au sein du système ferroviaire. Des méthodes comme le clustering ou encore la détection d’éléments connectés pourraient nous aider à identifier des zones mal desservies. 

Nous profiterons également de porter un regard critique sur la représentation des données de transport et ses limites ainsi que sur la comparabilité et interprétabilité des résultats de notre étude. Pour cela, nous comparerons d’abord les différents moyens de représenter des données de transport, pour tenter de justifier l’utilisation du standard GTFS. Nous verrons ensuite dans quelles mesures des études similaires peuvent être comparées.

## Travaux connexes

Beaucoup de chercheurs se sont aussi intéressés à l'analyse des réseaux formés par les systèmes de transport public, et ce à différentes échelles. Il est donc intéressant de citer quelques travaux similaires au nôtre, à des fins de comparaison. Cela s'avérera utile lors du choix des analyses à effectuer.

- Mohmand & Wang (2014) étudient les propriétés structurelles du réseau ferroviaire pakistanais,
- Soh et al. (2010) apportent une analyse de réseau complexe pondéré des itinéraires de voyage sur les systèmes de transport par rail et par bus de Singapour,
- De Regt et al. (2019) étudient les caractéristiques topologiques et spatiales des réseaux de transport public au Royaume-Uni, 
- Erath et al. (2009) étudient le développement du réseau routier et ferroviaire suisse au cours des années 1950-2020.

## La construction du graphe

Pour analyser le réseau ferroviaire helvétique, il faut d'abord commencer par construire le l'objet mathématique sous-jacent. 

Les données GTFS incluent tous les modes de transport public en Suisse. Comme notre étude porte sur le transport ferroviaire, nous avons décidé de garder les données relatives aux trains, en éliminant trams, métros, crémaillères et remontées mécaniques. Nous avons aussi décidé d'ignorer les liens vers les arrêts en dehors de la Suisse. Enfin, pour pouvoir étudier les propriétés du réseau lors d'une journée type, nous avons choisi de modéliser notre réseau selon l'horaire du Jeudi, journée durant laquelle circule le plus de services. 

Les données sont séparées en plusieurs tables: celle des arrêts, celle des itinéraires et celle de l'horaire. En joignant ces tables sur les identifiants uniques, nous pouvons reconstruire les séquences d'arrêts des itinéraires de chaque ligne. Cela nous permet donc de modéliser chaque gare en tant que nœud, et de lier deux nœuds s'il existe un itinéraire qui rejoint directement les deux gares correspondantes. 

Tous les nœuds et tous les segments d'itinéraires n'ont pas la même importance. Pour pondérer notre graphe, nous avons pris en compte la fréquence de passage des trains sur un tronçon du réseau, ainsi que la fréquentation journalière moyenne de chaque gare. La fréquence de passage est trivialement obtenue en comptant le nombre d'itinéraires qui passent sur un tronçon lors d'une journée. Quant à la fréquentation journalière, nous avons utilisé un jeu de données additionnel contenant les informations nécessaires. Ce dernier ne couvrant qu'un peu plus de la moitié des gares de notre réseau, nous avons supposé une fréquentation nulle pour les gares manquantes.  

Le graphe construit est visible sur la carte ci-dessous. Il est possible de masquer le calque des nœuds ou celui des liens. 

<br/>
<iframe src="network.html" id="map" height="600px" width="100%" style="border:none;"></iframe>

## L'analyse du réseau

Une fois le graphe représentant le réseau ferroviaire construit, nous pouvons passer à son analyse. Nous avons trouvé pertinent de travailler avec des statistiques identiques à celles utilisées dans les études mentionnées plus haut. En s'aidant des guides de Ducruet (2010), nous avons étudié les caractéristiques locales et globales de notre graphe.  

Les résultats sont présentés dans le tableau ci-dessous. Nous avons aussi rapporté ceux des travaux connexes à des fins de comparaison. Remarquez la distinction entre Réseau Ferré (RF) et Transport Public (TP).

| Propriété | Traduction | RF Suisse | RF Pakistanais | TP Singapourien | RF Britanique | RF Chinois |
|-|-|:-:|:-:|:-:|:-:|:-:|
| Nombre de noeuds | Number of nodes | 1663 | 628 | 93 | 2575 | 1192 |
| Nombre de liens | Number of edges | 2514 | 6078 | 3843 | 4450 | 67594 |
| Diamètre | Diameter | 36 | 5 | 2 | 48 | - |
| Chemin le plus court moy. | Shortest path (avg.) | 10.319 | 3.15 | 1.101 | 11.82 | 2.21 |
| Efficacité | Efficiency | 0.1068 | 0.25 | - | - | - |
| Centralité de proximité moy.| Closeness centrality (avg.) | 0.0917 | 0.2 | - | - | 0.46 |
| Centralité d’intermédiarité moy.| Betweenness centrality (avg.) | 0.0074 | 0.01 | - | - | 0.001 |
| Degré moyen | Average degree | 3.0271 | 19.36 | 82.6452 | 3.46 | 113 |
| Plage de degrés | Degree range | (1, 29) | (2, 69) | (35,92) | (-, 31) | (1, 673) |
| Transitivité moyenne | Average clustering | 0.2602 | 0.97 | 0.9341 | 0.309 | 0.68 |
| Assortativité | Assortativity | 0.2815 | 0.34 | −0.0875 | 0.24 | - |

Les mesures descriptives de la taille du réseau offrent une vue globale sur sa structure. Le rapport du nombre de nœuds contre le nombre de liens semble élevé en Suisse, tout comme il l'est en Grande-Bretagne. Cela indique que le réseau ferré suisse comporte beaucoup de gares, mais que seulement quelques-unes sont fortement connectées. De plus, les nœuds ont un degré moyen de 3 : cela veut dire qu'en moyenne, il est possible d'atteindre trois destinations en un seul arrêt. Le diamètre du réseau ferré suisse est de 36. Cette mesure correspond au nombre maximal de gares qui séparent deux nœuds. 

En prenant en compte la pondération des liens, c'est-à-dire le nombre de trains par jour sur un certain tronçon, la distribution des degrés peut être interprétée. Le degré pondéré d'un nœud correspond donc au nombre de trains qui s'arrêtent à ce nœud lors d'une journée. En moyenne, 170 trains s'arrêtent à un nœud donné. La gare centrale de Zurich connaît le nombre d'arrêts maximal du réseau de 2931.

Notre graphe n'est pas connecté ; c'est-à-dire qu'il existe un ou plusieurs nœuds qui ne sont pas atteignables depuis le reste du réseau. Certaines mesures requièrent un graphe connecté : nous avons donc calculé ces dernières un considérant la plus grande composante connectée du graphe. 

### Taille moyenne du chemin le plus court

Pour obtenir cette mesure, le chemin le plus court entre chaque paire de nœuds est calculé. La taille moyenne de ces chemins peut être interprétée comme une mesure d'efficacité du réseau. Plus elle est courte, plus l'efficacité à faire faire transiter le flux, ici les trains, est grande. En d'autre termes, cette mesure indique qu'en moyenne, 10 arrêts sont nécessaires pour voyager d'un arrêt à un autre. 
 
### Centralité des noeuds

Les mesures de centralité permettent d'identifier les stations qui connaissent un fort trafic et une congestion élevée. La centralité d'intermédiarité d'un nœud est le nombre de plus courts chemins qui y passent. La gare d'Olten est la plus centrale vis-à-vis de cette mesure : elle joue le rôle de carrefour entre les différentes régions de la Suisse. La centralité de proximité d'un nœud indique la proximité de ce nœud au reste du graphe. Plus précisément, c'est la plus courte distance moyenne avec tous les autres nœuds: plus la valeure est grande, plus la gare est centrale et offre une gamme de service plus large. Ici, la distance entre deux stations est le nombre de stations minimal qui les sépare. 

| Gare | Centralité d’intermédiarité |  |  |  | Gare | Centralité de proximité |
|-|:-:|-|-|-|-|:-:|
| Olten | 0.4795 |  |  |  | Olten | 0.1629 |
| Brig | 0.3930 |  |  |  | Zürich HB | 0.1621 |
| Zürich HB | 0.3384 |  |  |  | Bern | 0.1615 |
| Zollikofen | 0.2799 |  |  |  | Basel SBB | 0.1588 |
| Basel SBB | 0.2587 |  |  |  | Münsingen | 0.1511 |
| Münsingen | 0.2486 |  |  |  | Brig | 0.1509 |
| Bellinzona | 0.2277 |  |  |  | Aarau | 0.1505 |
| Nyon | 0.1736 |  |  |  | Oensingen | 0.1489 |
| Sion | 0.1692 |  |  |  | Brugg AG | 0.1489 |
| Lausanne | 0.1669 |  |  |  | Fribourg/Freiburg | 0.1479 |

<br/>

<iframe src="network_betweenness.html" id="map_betweenness" height="600px" width="100%" style="border:none;"></iframe>

### Transitivité moyenne

La transitivité d'un nœud, ou le *clustering coefficient* en anglais, désigne le nombre de triades fermées (triangle formé par trois nœuds) auxquelles participe ce nœud, sur le nombre de triades possibles dans le réseau. En d'autre termes, c'est la probabilité que, pour un nœud donné, ses deux voisins soient aussi connectés entre eux. Cette mesure peut aussi être étendue à des groupes de 4 ou 5 nœuds interconnectés. 

La transitivité moyenne de 0.26 est caractéristique d'un réseau décentralisé, sans beaucoup de gares centrales. Cela justifie aussi la centralité de proximité moyenne très basse.

### Coefficient d'assortativité

Cette mesure prend en considération la corrélation  des degrés au sein de chaque paire de nœuds. Autrement dit, elle indique si les nœuds similaires (vis-à-vis de leur degré) sont connectés entre eux. Cela peut être illustré en le degré moyen des voisins les plus proches, pour les nœuds de degré *k*. D'après Mohmand & Wang (2014), si le degré moyen augmente avec la valeur de *k*, alors le réseau est assortatif. Nous avons réalisé l'expérience (visualisée ci-dessous) et pouvons donc conclure que le réseau ferré suisse est assortatif. 

<div align="center">
    <img src="avg_nn_deg.png" alt="average neareast neighbor degree" class="center">
</div>

### Détection de communautés

Nous avons trouvé intéressant de faire une détection de communauté sur le réseau étudié, en utilisant la *détection de communautés par modularité*. Cet algorithme cherche à maximiser la modularité du graphe, c'est-à-dire à le séparer en sous-graphes fortement intra-connectés mais peu interconnectés. Cette approche aboutit à 55 sous-graphes différents : les 10 les plus grands couvrent la majorité du territoire suisse.

<br/>

<iframe src="network_communities.html" id="map_communities" height="600px" width="100%" style="border:none;"></iframe>

### Réseau petit monde

Un réseau petit monde, ou *small-world network*, est un réseau où:
- La plupart des nœuds ne sont pas voisins entre eux,  
- Les voisins d'un nœud sont probablement voisins entre eux, 
- Un nœud est atteignable depuis presque n'importe quel nœud, en un petit nombre de sauts. 

En d'autres termes, dans de tels réseaux, des groupes de nœuds sont fortement connectés entre eux, mais ces groupes ne sont pas fortement interconnectés. Cela se manifeste par la présence de *cliques* et une forte densité de liens. Ils sont caractérisés par un petit diamètre et une forte transitivité.s 

Pour déterminer si un réseau est *small world*, il suffit de calculer la transitivité et le diamètre du graphe et les comparer avec les mêmes mesures d'un graphe aléatoire de la même taille. L'indice sigma (Humphries & Gurney, 2008) calculé en fonction du rapport de ces deux mesures permet donc de savoir si un réseau est *small world*: c'est le cas s'il est supérieur à 1. Dans le cas de la Suisse, sigma vaut environ 30 : le réseau ferré helvétique est donc un réseau petit monde. 

## À propos du format des données 

Il existe plusieurs façons de représenter les données de transport, chacune étant adéquate à telle ou telle utilisation. Il est donc légitime de se demander si le format GTFS que nous utilisons pour construire le graphe du réseau ferré suisse répond bien à nos demandes, et si d’autres alternatives auraient pu être utilisées. Parmi les autres formats disponibles, nous pouvons citer NeTEx (*Network Timetable Exchange*), le *Public Transport Version 2* (ptv2) d’OpenStreetMap, et le graphe de connaissances WikiData. 

Les trois formats mentionnés ci-dessus permettent la représentation d’informations et de relations complexes, comme la différenciation des quais et des entrées au sein d’une gare. Il est donc important de se limiter aux fonctionnalités dont nous avons besoin pour cette étude, notamment la représentation des gares, celle de la politique de desserte des différentes lignes, et le lien entre les deux. 

### La représentation des lignes

Les lignes de transport public opèrent le long d’itinéraires prédéfinis, s'arrêtant à plusieurs arrêts pour la montée et la descente de passagers. Prenons par exemple la ligne IR 90 reliant Brig à Genève-Aéroport qui dessert systématiquement les villes principales contrairement aux villes secondaires, desservies ou non selon les différents services.

| Format | Commentaire | Exemple |
|-|-|-|
| GTFS | Fait la distinction entre une ligne et les itinéraires qui opèrent sur cette dernière. On peut dire que ce format offre une vision temporelle des lignes, car il permet aussi de spécifier les horaires (jours, et heures exactes) de chaque itinéraire.  | L’itinéraire s'arrêtant à Genève, Nyon, Morges puis Lausanne est différent de celui qui lie directement Lausanne à Genève. Ces deux différents itinéraires sont opérés sur la même ligne IR 90. |
| ptv2, OpenStreetMap | Ne fait pas la distinction entre itinéraires, et représente une ligne d’un point de vue géographique. La modélisation des lignes sur OSM est loin d’être homogène. La couverture des lignes n’est pas exhaustive, malgré tous les efforts mis en place pour instaurer un format commun. | La [ligne IR 90](https://www.openstreetmap.org/relation/7796313) sur OpenStreetMap. En choisissant une direction, il est possible de visualiser les arrêts de la ligne et de les obtenir grâce à l’attribut “membres”.  |
| WikiData | Ne permet pas de représenter des lignes commerciales spécifiques. Le format contient des informations plus génériques comme “ligne du Simplon” plutôt que "IR 90". Très peu de lignes  commerciales de transport y sont modélisées.  | [Ligne du Simplon](https://www.wikidata.org/wiki/Q667559) sur WikiData. |
| NeTEx | Similaire au format GTFS. |  |

### La représentation des gares

La représentation des gares est très similaire dans les quatre formats. Ils emploient tous la notion de points d'arrêt. Nous nous intéressons à la localisation des gares et au lien entre ces dernières et les lignes. 

| Format | Localisation | Relation arrêts-lignes | Exemple |
|-|-|-|-|
| GTFS | Obligatoire | Le lien entre une ligne et ses arrêts est indirect et est lié aux horaires de la ligne et de ses services |  |
| ptv2, OpenStreetMap | Obligatoire | Le lien entre une ligne et ses arrêts est explicitement indiqué. | La [gare de Lausanne](https://www.openstreetmap.org/node/1800313662) sur OpenStreetMap |
| WikiData | Obligatoire | Le lien entre un arrêt et une ligne est parfois indiqué.  | La [gare de Lausanne](https://www.wikidata.org/wiki/Q669678) sur WikiData |
| NeTEx | Optionnelle  | Permet d’obtenir les arrêts d’une ligne de manière plus directe. | |

### Disponibilité des formats

Il est possible de télécharger directement les données au format GTFS ou NeTEx : ces formats sont indépendants de toute plateforme. Dans le cas de WikiData et d’OpenStreetMap, il est nécessaire de faire recours à du web scraping pour récupérer les informations nécessaires.

En Suisse, CFF Infrastructure est responsable de la conduite des tâches systémiques relatives aux données d’informations voyageurs ou SKI (*Systemaufgaben der Kundeninformation*). Le Secrétariat des tâches SKI valide officiellement le format HRDF qu’il retranscrit automatiquement au format GTFS. Le support pour le format NeTEx est encore en phase alpha de test. 

Les plateformes OpenStreetMap et WikiData sont accessibles et modifiables par le grand public. Leur utilisation à l'échelle Suisse n’est pas adéquate vu qu’il existe une alternative officielle. Cependant, dans le cadre d’un projet à échelle plus large (européenne ou mondiale), il serait envisageable de les utiliser comme source unique de données, au lieu d'agréger les sources de plusieurs pays. 

## Interprétabilité de l’étude

<!-- À partir du graphe construit, nous avons eu l’occasion de réaliser plusieurs analyses sur l’objet mathématique obtenu. Pour choisir les mesures adéquates, nous nous sommes inspirés d’études similaires effectuées dans d’autres pays ou villes.    -->

### La subjectivité de nos choix 

Comme Boyd et Crawford le mentionnent dans leur *deuxième* provocation pour les Big Data, l’impératif  d’objectivité et d'exactitude est trompeur. Lors de la construction initiale du graphe, nous avons dû faire des choix quant au nettoyage et au traitement des données. Dès lors, notre analyse devient subjective et nous sommes limités en matière de comparaison et d’interprétation. 

<blockquote>
As a large mass of raw information, Big Data is not self-explanatory. And yet the specific methodologies for interpreting the data are open to all sorts of philosophical debate. Can the data represent an “objective truth” or is any interpretation necessarily biased by some subjective filter or the way that data is “cleaned?”
<p>‒ David Bollier, The Promise and Peril of Big Data</p>
</blockquote>

Prenons aussi les résultats de la détection de communautés qui, à première vue, semblent très satisfaisants et représentatifs des communautés tarifaires en Suisse, ou même de la géographie suisse. Nous pouvons cependant voir quelques irrégularités à la limite entre deux communautés : Brig (VS) fait partie du même sous-graphe que Berne et Bâle, Palézieux et Palézieux-village sont dans deux communautés différentes. Cela est inhérent à la conception de l'algorithme utilisé : un nœud devrait pouvoir appartenir à plusieurs communautés.

### La comparaison avec d'autres études

Pour pouvoir comparer des analyses, il faut que ces dernières soient effectuées dans des conditions similaires. Rien ne garantit que notre graphe a été construit de la même manière que celui d’une étude connexe. De plus, chaque ville ou pays connaît une situation unique, et une géographie propre à son territoire. Il faut donc tenir compte de cela lors de la comparaison des résultats d’un pays à l’autre. Alors qu'il est vrai que nous abstrayons le réseau ferroviaire sous forme de graphe, le contexte reste essentiel : cela résonne avec la *quatrième* provocation de Boyd et Crawford. 

Par exemple, il serait tentant de dire que le réseau ferré pakistanais est plus connecté que le suisse, vu son degré moyen plus élevé. Cependant, un regard plus attentif révèle que la différence s'explique par la construction du graphe du réseau ferré de l'étude : dans notre analyse nous n'incluons que les trains, alors que Mohmand & Wang (2014) prennent aussi en compte les métros, ce qui introduit beaucoup plus de liens, et explique donc une connectivité supérieure.

### L'utilisation de plusieurs sources de données

Enfin, notre graphe croise deux sources d’information : les données GTFS d’une part, et les statistiques sur le nombre de personnes montant et descendant des trains par gare d’autre part. Le nombre de gares dans la première est largement supérieur au nombre de gares de la deuxième. Nous avons, ici aussi, dû faire un choix qui introduit un biais devant être pris en compte lors de l’interprétation des résultats. Il est pertinent de faire le lien avec la troisième *provocation* de Boyd et Crawford, stipulant que l’abondance des données ne rime pas avec qualité. 

<blockquote>
“Every one of those sources is error-prone, and there are assumptions that you can safely match up two pieces together. So I think we are just magnifying that problem [when we combine multiple data sets]. There are a lot of things we can do to correct such problems, but all of them are hypothesis-driven.”
<p> ‒ Jesper Andersen</p>
</blockquote>


