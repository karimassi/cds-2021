# Typologie par Topologie
*Une étude de la topologie du réseau ferroviaire suisse.*

> This repository contains work done in the scope of the *Critical Data Studies* class at EPFL. The report and companion website are written in French. 

Ce dépôt contient notre travail dans le cadre du projet de *Critical Data Studies*. Il s'agit d'une étude de la structure du réseau ferroviaire suisse. 

Il contient:

- Le notebook [`graph_construction.ipynb`](graph_construction.ipynb), dans lequel nous nettoyons les données puis construisons le graphe associé au réseau ferroviaire.
- Le notebook [`graph_analysis.ipynb`](graph_analysis.ipynb), dans lequel nous analysons le graphe construit. 
- Le [rapport](rapport.pdf) qui décrit notre démarche, nos résultats et leur analyse sous un format statique. 
- Le dossier `docs` qui contient tous les éléments nécessaires au site web. Le site est accessible à [cette addresse](karimassi.github.io/railgraph-ch/).
- Le fichier `environment.yml` qui spécifie toutes les librairies utilisées dans ce projet, à des fins de reproductibilité. 

Pour lancer le premier notebook, il faut que les données originales soient disponibles dans le dossier `data/raw` avec l'arborescence ci-dessous. Pour lancer le second notebook, il faut soit avoir lancé le premier notebook, soit utiliser les données traitées, dans le dossier `data/processed`.
```
.
├── data
│   ├── processed
│   │   ├── edges_counts.pickle
│   │   ├── railgraph.pickle
│   │   ├── railway_stops.pickle
│   │   └── stop_id_to_name
│   └── raw
│       ├── agency.txt
│       ├── calendar.txt
│       ├── calendar_dates.txt
│       ├── feed_info.txt
│       ├── peinaussteiger2018.xlsx
│       ├── routes.txt
│       ├── stop_times.txt
│       ├── stops.txt
│       ├── transfers.txt
│       └── trips.txt
├── ...
```

Les fichiers donc le nom suit la forme `*.txt` correspondent au jeu de données GTFS disponible [ici](https://opentransportdata.swiss/fr/dataset/timetable-2021-gtfs2020). Le fichier `peinaussteiger2018.xlsx` contient les fréquentations moyennes des gares, et est disponible [ici](https://opentransportdata.swiss/fr/dataset/einundaus).

