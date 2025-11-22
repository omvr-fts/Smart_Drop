# SmartDrop – Smart Irrigation & CO₂ Saver
Python GUI Prototype (Tkinter + Matplotlib)

SmartDrop est un prototype développé dans le cadre du challenge EcoThoughts.  
Il présente un système simplifié permettant d'illustrer la gestion intelligente de l’irrigation agricole en se basant sur des données issues d’un capteur de type S.sensor.  
Le prototype met en avant l’optimisation de l'eau, l'estimation de l’énergie utilisée et l’évaluation des émissions de CO₂ associées.

## Objectif du projet

Ce projet vise à fournir :
- Une interface de démonstration utilisable lors d’un pitch ou d’une présentation.
- Une visualisation claire des indicateurs liés à l’irrigation.
- Une base technique permettant d’évoluer vers une solution complète intégrée à de vrais capteurs.

Les données affichées sont simulées et servent uniquement pour la présentation.

## Fonctionnalités

- Affichage de quatre indicateurs principaux :  
  eau économisée, CO₂ évité, réduction d’irrigation, surface optimisée.
- Graphique comparatif entre irrigation de référence et irrigation optimisée.
- Graphique cumulatif des émissions de CO₂ évitées.
- Tableau des parcelles (culture, superficie, économies d’eau et de CO₂, statut).
- Bloc de recommandations généré à partir d'exemples d’état hydrique.

## Structure du projet

```
SmartDrop/
│── smartdrop_dashboard.py   # Interface graphique Tkinter + Matplotlib
│── README.md                # Documentation

```

## Installation

### Prérequis
- Python 3.x
- Tkinter (généralement inclus avec Python)
- Matplotlib

### Étapes d'installation

1. Cloner le dépôt :

```bash
git clone https://github.com/omvr-fts/Smart_Drop.git
cd Smart_Drop
```

2. Installer les dépendances :

```bash
pip install matplotlib
```

## Exécution

Lancer simplement :

```bash
python smartdrop_dashboard.py
```

L'interface se chargera et affichera :
- Les KPI
- Les graphiques
- Les recommandations
- Le tableau des parcelles

Ce tableau de bord peut être utilisé pour une démonstration en direct ou pour des captures d’écran intégrées à une présentation.

## Limitations

- Les données sont intégralement simulées.
- Aucun lien direct avec un capteur réel n’est implémenté.
- Le modèle d’estimation CO₂ est simplifié pour l’usage démonstratif.

## Évolutions possibles

- Connexion à des capteurs physiques (ex : S.sensor).
- Intégration d’une API ou d’un backend cloud.
- Exports automatiques (PDF, CSV).
- Version web ou mobile du tableau de bord.

## Crédits

Projet réalisé dans le cadre d’EcoThoughts 2025.  
Interface développée en Python (Tkinter & Matplotlib).  
Concept basé sur l’utilisation d’un capteur d’humidité du sol de type S.sensor.

