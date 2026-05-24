import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
plt.style.use("rose-pine")

df = pd.read_csv("AllRanksEUW1.csv")

tiers = df["tier"]
divisions = df["division"]
players = df["total"]

tier_divisions = []
tier_colours = []

for tier, division in zip(tiers, divisions):
        tier_divisions.append(f"{tier} {division}")
        tier_colours.append(f"{tier} {division}")

def make_color():
    color_map = {
        "IRON": "#525252",
        "BRONZE": "#dd8521",
        "SILVER": "#bdbdbd",
        "GOLD": "#ffd344",
        "PLATINUM": "#3bdfbb",
        "EMERALD": "#21ce54",
        "DIAMOND":"#1f47c7", 
        "MASTER": "#c422d3", 
        "GRANDMASTER": "#b61f1f",
        "CHALLENGER": "#2eb1ee"
    }

    for tier in tiers:
        colors = [color_map[tier] for tier in tiers]

    return colors

plt.figure(figsize=(12, 6))
plt.bar(tier_divisions, players, width=0.5, color=make_color(), alpha=0.95, label=tier_colours)
plt.title("EUW Rank Distribution - May 2026", fontsize=18, fontweight="bold")
plt.xticks(rotation=40, ha='right')
plt.legend(fontsize=8.5)
plt.grid(True)
plt.show()