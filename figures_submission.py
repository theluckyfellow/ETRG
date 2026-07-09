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
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.set_xlim(-10, 10); ax.set_ylim(-1.2, 5.2); ax.axis("off")
th = np.linspace(0, 2 * np.pi, 100)
ax.fill(0.55 * np.cos(th), 0.55 * np.sin(th), color="#1E242B", zorder=5)
ax.text(0, -1.05, "mass M", ha="center", fontsize=9.5, color=MUTED)
x = np.linspace(-10, 10, 400)
b = 2.2
for k, c, lbl in [(0.5, AMBER, "slow matter — time face only:  δ = 2GM/c²b   (0.87″)"),
                  (1.0, TEAL, "light — both faces:  δ = 4GM/c²b   (1.75″ = 2×)")]:
    y = b + k * 0.9 * (1 + x / np.hypot(x, b))
    ax.plot(x, y, color=c, lw=2.2)
    ax.text(-9.8, y[0] + 0.16, lbl, fontsize=9.5, color=c)
ax.annotate("", xy=(9.6, 0.4), xytext=(7.2, 0.4),
            arrowprops=dict(arrowstyle="->", color=MUTED, lw=1))
ax.text(8.4, 0.62, "travel", ha="center", fontsize=8.5, color=MUTED)
ax.set_title("The factor of two: a particle samples the two faces in proportion to (v/c)²")
plt.savefig(f"{OUT}/fig1_deflection.png"); plt.close()

# ---- Fig 2: toy Einstein — collapse + boost weight --------------------------
data = json.load(open("toy_einstein_data.json"))
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.1))
shades = ["#D8B27E", "#BC8A3F", AMBER]
for (e, c) in zip(["0.02", "0.0632", "0.2"], shades):
    r = np.array(data[e]["r"]); s = np.array(data[e]["s"])
    a1.plot(r, s / float(e), color=c, lw=1.8, label=f"ε = {float(e):g}")
a1.set_xlabel("r  (sites)"); a1.set_ylabel("stretch  s(r) / ε")
a1.set_title("Linear response: profiles collapse")
a1.legend(frameon=False, fontsize=9)
e = "0.0632"
r = np.array(data[e]["r"]); dk = np.array(data[e]["dK"])
a2.plot(r, dk / r, color=TEAL, lw=1.8)
a2.set_ylim(0, 0.011)
a2.set_xlabel("r  (sites)"); a2.set_ylabel("δ⟨K⟩ / r")
a2.set_title("Enclosed debt / r: the Rindler boost weight,\nreproduced unprompted (constant to ~1%)")
for a in (a1, a2):
    a.spines[["top", "right"]].set_visible(False)
fig.subplots_adjust(wspace=0.32)
fig.suptitle("A lattice geometry built from mutual information curves in response to entanglement debt",
             y=1.14, fontsize=11)
plt.savefig(f"{OUT}/fig2_toy_einstein.png"); plt.close()

# ---- Fig 3: Q10 — the lock is basis-selective -------------------------------
fig, ax = plt.subplots(figsize=(5.6, 2.8))
names = ["modular basis\n(admissible observer)", "site basis\n(inadmissible control)"]
vals = [0.99992, 4.216]
cols = [TEAL, AMBER]
bars = ax.barh(names, vals, color=cols, height=0.52)
ax.axvline(1.0, color=MUTED, lw=1, ls="--")
ax.text(1.0, 1.45, "first-law lock (ratio = 1)", fontsize=8.5, color=MUTED, ha="center")
for b, v in zip(bars, vals):
    ax.text(v + 0.06, b.get_y() + b.get_height() / 2, f"{v:g}", va="center",
            fontsize=10, color="#1E242B")
ax.set_xlim(0, 4.8)
ax.set_xlabel("coarse-grained / fine-grained first-law response")
ax.set_title("Coarse-graining preserves the entanglement first law\niff it is modular-covariant (free-fermion chain)")
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
ax.set_xlim(0.85, 1.005); ax.set_yticks([])
ax.set_xlabel("mean matched-state fidelity between lab-time and entropic-time evolution")
ax.set_title("The time label cannot leak into dynamics — and the control shows the test could see it")
ax.spines[["top", "right", "left"]].set_visible(False)
plt.savefig(f"{OUT}/fig4_label_freeness.png"); plt.close()

print("figures written to", OUT)
