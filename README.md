# 🌿 SmartDrop – Smart Irrigation & CO₂ Saver  
### *Python GUI Prototype (Tkinter + Matplotlib)*

SmartDrop est un prototype conçu pour le challenge EcoThoughts.  
Il montre comment améliorer l’irrigation agricole en utilisant :

- Les données du **capteur tunisien S.sensor** (humidité multi-profondeurs, météo, besoins hydriques)  
- Un modèle d’optimisation de l’eau  
- Un calculateur d’énergie et d’émissions CO₂  
- Une interface intuitive pour agriculteurs & jurys

Ce prototype Python est entièrement exécutable et optimisé pour une **démo rapide et professionnelle**.

---

## 🚀 Fonctionnalités Principales

### 💧 Optimisation intelligente de l’eau
- Comparaison *Avant vs Optimisé*  
- Économies d’eau (m³)  
- Réduction d’irrigation (%)  

### 🌍 CO₂ Saver Engine
- Calcul du temps de pompe économisé  
- Conversion en énergie (kWh)  
- Calcul CO₂ évité (kg) selon source énergétique  

### 📊 Dashboard complet
- 4 KPIs : Eau, CO₂, Irrigation, Surface  
- Graphique Eau (Baseline vs Optimisé)  
- Courbe CO₂ cumulative  
- Tableau des parcelles  
- Zone d’alertes & recommandations  

### 🪟 Interface GUI Python
- Tkinter pour la structure  
- Matplotlib pour les graphiques  
- TreeView pour les tableaux  
- Parfait pour screenshot & pitch

---

## 📁 Structure du Projet

```
SmartDrop/
│── smartdrop_dashboard.py   # Interface graphique principale
│── README.md                # Documentation du projet
└── screenshots/             # (Optionnel) Captures d’écran
```

---

## 🛠 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/<your-username>/SmartDrop.git
cd SmartDrop
```

### 2. Installer les dépendances nécessaires

```bash
pip install matplotlib
```

*(Tkinter est installé par défaut avec Python.)*

---

## ▶️ Exécution du prototype

```bash
python smartdrop_dashboard.py
```

Une interface graphique s’affichera avec :

- Les KPI  
- Deux graphiques  
- Les recommandations  
- La liste des parcelles  

Prêt pour une démonstration en live ou une capture d’écran.

---

## 📸 Ajouter un Screenshot

Une fois ta capture prise, ajoute-la ici :

```
![Dashboard Screenshot](screenshots/dashboard.png)
```

---

## 📌 Notes & Limitations

- Les données sont **simulées** pour la démonstration.  
- Le S.sensor réel fournit : humidité du sol, météo, prévisions, besoins en eau, etc.  
- Le calcul CO₂ fonctionne avec :
  - énergie du réseau  
  - diesel  
  - solaire  

Ce prototype sert de base pour un futur système complet (API + automatisation pompe).

---

## 🤝 Crédits

- Développé pour **EcoThoughts 2025**  
- Capteur utilisé : **S.sensor (made in Tunisia 🇹🇳)**  
- UI créée en **Python 3, Tkinter & Matplotlib**  
- Projet officiel : **SmartDrop**

---

## 📄 Licence

MIT License – libre d’utilisation, modification et distribution.
