import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# -----------------------------
# Données de démonstration
# -----------------------------

# KPIs (valeurs d'exemple)
WATER_SAVED_M3 = 480
CO2_SAVED_KG = 210
IRRIGATION_REDUCTION_PERCENT = 26
AREA_OPTIMIZED_HA = 10

# Données mensuelles pour le graphique eau
months = ["Avril", "Mai", "Juin"]
baseline_water = [300, 350, 280]   # m³ sans optimisation
optimized_water = [220, 260, 230]  # m³ avec Smart Drop

# CO2 évité cumulatif (exemple)
co2_cumulative = [50, 120, CO2_SAVED_KG]  # kg

# Données par parcelle
parcels = [
    ("Olivier Nord", "Oliviers", 4, 190, 80, "Optimal"),
    ("Agrumes Est", "Agrumes", 3, 150, 65, "À suivre"),
    ("Maraîchage Sud", "Légumes", 3, 140, 65, "Stable"),
]


# -----------------------------
# Création de la fenêtre
# -----------------------------

root = tk.Tk()
root.title("Smart Drop – Smart Irrigation & CO₂ Saver (Prototype)")
root.geometry("1300x750")
root.configure(bg="white")

# Pour un peu de marge générale
PADX = 10
PADY = 8


# -----------------------------
# HEADER
# -----------------------------

header_frame = tk.Frame(root, bg="white")
header_frame.pack(fill="x", padx=PADX, pady=(PADY, 0))

title_label = tk.Label(
    header_frame,
    text="Smart Drop – Smart Irrigation & CO₂ Saver",
    font=("Segoe UI", 20, "bold"),
    bg="white"
)
title_label.pack(anchor="w")

subtitle_label = tk.Label(
    header_frame,
    text="Pilotage intelligent de l’irrigation avec S.sensor & analyse CO₂ en temps réel",
    font=("Segoe UI", 11),
    fg="#555555",
    bg="white"
)
subtitle_label.pack(anchor="w")

context_label = tk.Label(
    header_frame,
    text="Exploitation : Ferme Oliviers Nord – Période : Saison 2024 (Avril–Juin)",
    font=("Segoe UI", 9),
    fg="#777777",
    bg="white"
)
context_label.pack(anchor="w", pady=(3, 0))


# -----------------------------
# KPIs (4 cartes)
# -----------------------------

kpi_frame = tk.Frame(root, bg="white")
kpi_frame.pack(fill="x", padx=PADX, pady=(PADY, 0))

def create_kpi(parent, title, value, subtitle):
    frame = tk.Frame(parent, bg="#f5f5f5", bd=1, relief="solid")
    frame.pack(side="left", expand=True, fill="both", padx=5)

    lbl_title = tk.Label(
        frame,
        text=title,
        font=("Segoe UI", 11, "bold"),
        bg="#f5f5f5"
    )
    lbl_title.pack(anchor="w", padx=8, pady=(6, 0))

    lbl_value = tk.Label(
        frame,
        text=value,
        font=("Segoe UI", 18, "bold"),
        bg="#f5f5f5"
    )
    lbl_value.pack(anchor="w", padx=8, pady=(2, 0))

    lbl_subtitle = tk.Label(
        frame,
        text=subtitle,
        font=("Segoe UI", 9),
        fg="#555555",
        bg="#f5f5f5",
        justify="left"
    )
    lbl_subtitle.pack(anchor="w", padx=8, pady=(0, 6))

# KPI 1 – Eau économisée
create_kpi(
    kpi_frame,
    "💧 Eau économisée",
    f"{WATER_SAVED_M3} m³",
    "≈ 48 000 litres d’eau économisés sur la saison"
)

# KPI 2 – CO₂ évité
create_kpi(
    kpi_frame,
    "🌍 CO₂ évité",
    f"{CO2_SAVED_KG} kg",
    "Équivalent à ~1 000 km parcourus en voiture"
)

# KPI 3 – Réduction de l’irrigation
create_kpi(
    kpi_frame,
    "📉 Réduction de l’irrigation",
    f"-{IRRIGATION_REDUCTION_PERCENT} %",
    "par rapport aux pratiques habituelles de la ferme"
)

# KPI 4 – Surface optimisée
create_kpi(
    kpi_frame,
    "🌱 Surface optimisée",
    f"{AREA_OPTIMIZED_HA} ha",
    "Parcelles connectées via S.sensor & Smart Drop"
)


# -----------------------------
# FRAME GRAPHIQUES + ALERTES
# -----------------------------

middle_frame = tk.Frame(root, bg="white")
middle_frame.pack(fill="both", expand=True, padx=PADX, pady=(PADY, 0))

charts_frame = tk.Frame(middle_frame, bg="white")
charts_frame.pack(side="left", fill="both", expand=True)

alerts_frame = tk.Frame(middle_frame, bg="white", bd=1, relief="solid")
alerts_frame.pack(side="right", fill="y", padx=(10, 0))


# -----------------------------
# GRAPHIQUE 1 – Eau Avant / Après
# -----------------------------

fig = Figure(figsize=(7, 3), dpi=100)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Graphique Eau
x = range(len(months))
bar_width = 0.35

ax1.bar([i - bar_width/2 for i in x], baseline_water, width=bar_width, label="Baseline")
ax1.bar([i + bar_width/2 for i in x], optimized_water, width=bar_width, label="Avec Smart Drop")
ax1.set_xticks(x)
ax1.set_xticklabels(months)
ax1.set_ylabel("Volume d'eau (m³)")
ax1.set_title("Volume d’eau utilisé – Avant vs Avec Smart Drop")
ax1.legend(fontsize=7)

# Texte explicatif
ax1.text(
    0.5, -0.25,
    "Résultat : – 26 % de volume d’eau pompé sur la saison\npour un même niveau de production.",
    ha="center", va="top",
    transform=ax1.transAxes,
    fontsize=7
)

# GRAPHIQUE 2 – CO2 cumulatif
ax2.plot(months, co2_cumulative, marker="o")
ax2.set_ylabel("CO₂ évité (kg)")
ax2.set_title("CO₂ évité (kg) – cumul sur la saison")

ax2.text(
    0.5, -0.25,
    "Chaque optimisation réduit le temps de pompe → moins d’énergie → moins de CO₂.",
    ha="center", va="top",
    transform=ax2.transAxes,
    fontsize=7
)

fig.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=charts_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)


# -----------------------------
# ALERTES & RECOMMANDATIONS
# -----------------------------

alerts_title = tk.Label(
    alerts_frame,
    text="⚠️ Alertes & Recommandations",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
alerts_title.pack(anchor="w", padx=8, pady=(6, 4))

alerts_text = (
    "• Olivier Nord – Profondeur 40–60 cm :\n"
    "  Humidité en baisse → irriguer dans les prochaines 24h\n"
    "  pour éviter le stress hydrique.\n\n"
    "• Agrumes Est – Semaine dernière :\n"
    "  Sur-irrigation légère (+15 % vs besoin réel) → réduire la\n"
    "  durée de la prochaine irrigation.\n\n"
    "• Maraîchage Sud :\n"
    "  Humidité stable dans la zone idéale → aucune action urgente."
)

alerts_label = tk.Label(
    alerts_frame,
    text=alerts_text,
    font=("Segoe UI", 9),
    justify="left",
    bg="white"
)
alerts_label.pack(anchor="w", padx=8, pady=(0, 6))

alerts_footer = tk.Label(
    alerts_frame,
    text="✅ Smart Drop convertit les données S.sensor\n"
         "en décisions simples, actionnables et basées\n"
         "sur l’impact CO₂.",
    font=("Segoe UI", 8, "italic"),
    fg="#555555",
    bg="white",
    justify="left"
)
alerts_footer.pack(anchor="w", padx=8, pady=(4, 8))


# -----------------------------
# TABLEAU DES PARCELLES
# -----------------------------

table_frame = tk.Frame(root, bg="white")
table_frame.pack(fill="both", expand=False, padx=PADX, pady=(PADY, PADY))

table_title = tk.Label(
    table_frame,
    text="Détail par parcelle",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
table_title.pack(anchor="w", pady=(0, 4))

columns = ("parcelle", "culture", "surface", "eau", "co2", "statut")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=5)

tree.heading("parcelle", text="Parcelle")
tree.heading("culture", text="Culture")
tree.heading("surface", text="Superficie (ha)")
tree.heading("eau", text="Eau économisée (m³)")
tree.heading("co2", text="CO₂ évité (kg)")
tree.heading("statut", text="Statut")

for col in columns:
    tree.column(col, anchor="center", width=150)

for p in parcels:
    tree.insert("", "end", values=p)

tree.pack(fill="x")

table_footer = tk.Label(
    table_frame,
    text="Les recommandations d’irrigation sont générées à partir des mesures multi-profondeurs du sol par S.sensor, "
         "puis optimisées par le moteur CO₂ de Smart Drop.",
    font=("Segoe UI", 8),
    fg="#555555",
    bg="white",
    justify="left"
)
table_footer.pack(anchor="w", pady=(4, 0))


# -----------------------------
# FOOTER GLOBAL
# -----------------------------

global_footer = tk.Label(
    root,
    text="Prototype de démonstration – Smart Drop (Smart Irrigation & CO₂ Saver) – Données de test",
    font=("Segoe UI", 8),
    fg="#777777",
    bg="white"
)
global_footer.pack(side="bottom", pady=(0, 4))


# -----------------------------
# Lancer l'interface
# -----------------------------
root.mainloop()
