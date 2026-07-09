"""Publication figures for the ETRG submission package.
Palette: validated light-mode set (amber #A8660A time face, teal #0B7DA8
entanglement face, violet #6D53C9)."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AMBER, TEAL, VIOLET, MUTED = "#A8660A", "#0B7DA8", "#6D53C9", "#5A646E"
plt.rcParams.update({
    "font.family": "serif", "font.size": 10.5, "axes.titlesize": 11,
    "axes.labelsize": 10.5, "axes.edgecolor": MUTED, "axes.linewidth": 0.8,
    "xtick.color": MUTED, "ytick.color": MUTED, "text.color": "#1E242B",
    "axes.labelcolor": "#1E242B", "figure.dpi": 200, "savefig.bbox": "tight",
})
OUT = "submission/figures"
import os
os.makedirs(OUT, exist_ok=True)

# ---- Fig 1: the deflection / two-face conceptual diagram --------------------
fig, ax = plt.subplots(figsize=(7.2, 3.0))
ax.set_xlim(-10.4, 10.4); ax.set_ylim(-1.5, 4.0); ax.axis("off")
ax.plot(0, 0, "o", ms=17, color="#1E242B", zorder=5)
ax.text(0, -0.85, "mass M", ha="center", fontsize=9.5, color=MUTED)
x = np.linspace(-10, 10, 400)
b = 2.3
# deflection bends TOWARD the mass (downward); light bends twice as much
for k, c, lbl in [(0.5, AMBER, "slow matter — time face only\nδ = 2GM/c²b  →  0.87″"),
                  (1.0, TEAL, "light — both faces\nδ = 4GM/c²b  →  1.75″ = 2×")]:
    y = b - k * 0.75 * (1 + x / np.hypot(x, b))
    ax.plot(x, y, color=c, lw=2.2)
    ax.text(10.15, y[-1], lbl, fontsize=9, color=c, va="center", ha="left", linespacing=1.35)
ax.plot([-10, 10], [b, b], color=MUTED, lw=0.7, ls=":")
ax.text(-10, b + 0.18, "undeflected path (b above M)", fontsize=8.5, color=MUTED)
ax.annotate("", xy=(-6.4, 3.55), xytext=(-9.6, 3.55),
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=1))
ax.text(-8.0, 3.72, "travel", ha="center", fontsize=8.5, color=MUTED)
ax.set_xlim(-10.4, 16.5)  # room for right-hand labels
ax.set_title("The factor of two: a particle samples the two faces in proportion to (v/c)²",
             loc="left", pad=10)
plt.savefig(f"{OUT}/fig1_deflection.png"); plt.close()

# ---- Fig 2: toy Einstein — collapse + boost weight --------------------------
data = json.load(open("toy_einstein_data.json"))
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.1))
shades = ["#D8B27E", "#BC8A3F", AMBER]
for (e, c) in zip(["0.02", "0.0632", "0.2"], shades):
    r = np.array(data[e]["r"]); s = np.array(data[e]["s"])
    a1.plot(r, s / float(e), color=c, lw=1.8, label=f"ε = {float(e):g}")
a1.set_xlabel("r  (sites)"); a1.set_ylabel("stretch  s(r) / ε")
a1.set_title("Linear response: profiles collapse", loc="left", pad=10)
a1.legend(frameon=False, fontsize=9)
e = "0.0632"
r = np.array(data[e]["r"]); dk = np.array(data[e]["dK"])
a2.plot(r, dk / r, color=TEAL, lw=1.8)
a2.set_ylim(0, 0.011)
a2.set_xlabel("r  (sites)"); a2.set_ylabel("δ⟨K⟩ / r")
a2.set_title("Enclosed debt / r: the Rindler\nboost weight (constant to ~1%)", loc="left", pad=10)
for a in (a1, a2):
    a.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(wspace=0.34, top=0.80)
plt.savefig(f"{OUT}/fig2_toy_einstein.png"); plt.close()

# ---- Fig 3: Q10 — the lock is basis-selective -------------------------------
fig, ax = plt.subplots(figsize=(5.6, 2.8))
names = ["modular basis\n(admissible observer)", "site basis\n(inadmissible control)"]
vals = [0.99992, 4.216]
cols = [TEAL, AMBER]
bars = ax.barh(names, vals, color=cols, height=0.52)
ax.set_ylim(-0.55, 1.95)
ax.axvline(1.0, color=MUTED, lw=1, ls="--")
ax.text(1.06, 1.68, "first-law lock (ratio = 1)", fontsize=8.5, color=MUTED, ha="left")
for b, v in zip(bars, vals):
    ax.text(v + 0.06, b.get_y() + b.get_height() / 2, f"{v:g}", va="center",
            fontsize=10, color="#1E242B")
ax.set_xlim(0, 4.8)
ax.set_xlabel("coarse-grained / fine-grained first-law response")
ax.set_title("The first-law lock is modular-basis-selective (free-fermion chain)",
             loc="left", pad=12)
ax.spines[["top", "right"]].set_visible(False)
plt.savefig(f"{OUT}/fig3_q10_lock.png"); plt.close()

# ---- Fig 4: label-freeness fidelities ----------------------------------------
fig, ax = plt.subplots(figsize=(6.4, 3.0))
rows = [("A7 reconstruction (no feedback)", 0.999846, TEAL),
        ("state-functional feedback", 0.999828, TEAL),
        ("lapse-as-state-functional (referee's control)", 0.999840, TEAL),
        ("label-consuming control — the leak", 0.898054, AMBER)]
ys = np.arange(len(rows))[::-1]
for y, (n, v, c) in zip(ys, rows):
    ax.barh(y, v - 0.85, left=0.85, color=c, height=0.5)
    ax.text(0.851, y + 0.42, n, fontsize=9, color="#1E242B")
    ax.text(v + 0.002, y, f"{v:.4f}", va="center", fontsize=9.5, color=c)
ax.set_xlim(0.85, 1.005); ax.set_ylim(-0.6, 3.95); ax.set_yticks([])
ax.set_xlabel("mean matched-state fidelity, lab vs entropic time")
ax.set_title("The time label cannot leak into dynamics —\nand the control shows the test could see it",
             loc="left", pad=12)
ax.spines[["top", "right", "left"]].set_visible(False)
plt.savefig(f"{OUT}/fig4_label_freeness.png"); plt.close()

print("figures written to", OUT)
