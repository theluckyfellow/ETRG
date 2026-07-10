"""Portraits of the two simulated mini universes.

Figure A — the entropic-time universe (two-mode Bose-Hubbard, N=60):
  the matter field (bright-sector number distribution) through three
  bang/crunch cycles, shown in laboratory time and replotted in the
  universe's own entropic time, with S(t) and tau(t) beneath.

Figure B — the computable-geometry universe (free-fermion chain, L=200):
  the matter field (density), the metric field (-ln I between neighbors)
  dimpling around an entanglement defect, and the pairwise distance
  stretch — the toy gravitational well, pictured.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.sparse.csgraph import shortest_path

AMBER, TEAL, MUTED, INK = "#A8660A", "#0B7DA8", "#5A646E", "#1E242B"
plt.rcParams.update({
    "font.family": "serif", "font.size": 10, "axes.titlesize": 10.5,
    "axes.edgecolor": MUTED, "axes.linewidth": 0.8, "xtick.color": MUTED,
    "ytick.color": MUTED, "text.color": INK, "axes.labelcolor": INK,
    "figure.dpi": 190, "savefig.bbox": "tight",
})

# ============================ Figure A =====================================
N, J, U = 60, 1.0, 0.02
n = np.arange(N + 1, dtype=float)
H = np.zeros((N + 1, N + 1))
H[np.arange(N + 1), np.arange(N + 1)] = 0.5 * U * (n * (n - 1) + (N - n) * (N - n - 1))
hop = -J * np.sqrt((n[:-1] + 1) * (N - n[:-1]))
H[np.arange(N), np.arange(N) + 1] = hop
H[np.arange(N) + 1, np.arange(N)] = hop
w, V = np.linalg.eigh(H)
psi0 = np.zeros(N + 1); psi0[N] = 1.0
c0 = V.T @ psi0

ts = np.linspace(0, 20, 1600)
P = np.abs((V[None, :, :] * np.exp(-1j * w * ts[:, None])[:, None, :]) @ c0)**2  # [t, n]
m = P > 1e-14
S = -np.sum(np.where(m, P * np.log(np.where(m, P, 1)), 0), axis=1)
tau = np.concatenate(([0], np.cumsum(np.abs(np.diff(S)))))
tau_strict = tau + 1e-9 * ts                      # strictly increasing for resampling
tau_grid = np.linspace(0, tau_strict[-1], 1600)
P_tau = np.stack([np.interp(tau_grid, tau_strict, P[:, k]) for k in range(N + 1)], axis=1)

fig = plt.figure(figsize=(8.6, 5.4))
gs = fig.add_gridspec(2, 2, height_ratios=[2.4, 1], hspace=0.34, wspace=0.18)
a1 = fig.add_subplot(gs[0, 0]); a2 = fig.add_subplot(gs[0, 1])
a3 = fig.add_subplot(gs[1, 0]); a4 = fig.add_subplot(gs[1, 1])

a1.imshow(P.T, origin="lower", aspect="auto", cmap="magma",
          extent=[0, 20, 0, N], vmax=P.max() * 0.5)
a1.set_title("the matter field, in laboratory time", loc="left")
a1.set_xlabel("lab time t"); a1.set_ylabel("atoms in bright sector  n")

a2.imshow(P_tau.T, origin="lower", aspect="auto", cmap="magma",
          extent=[0, tau_grid[-1], 0, N], vmax=P.max() * 0.5)
a2.set_title("the same universe, in its own entropic time", loc="left")
a2.set_xlabel("entropic time τ  (arclength in entropy)"); a2.set_yticklabels([])

a3.plot(ts, S, color=AMBER, lw=1.6)
a3.set_title("bright-sector entropy S(t)", loc="left")
a3.set_xlabel("lab time t"); a3.set_ylabel("S")
a4.plot(ts, tau, color=TEAL, lw=1.6)
a4.set_title("entropic time τ(t) — flat where entropy stalls", loc="left")
a4.set_xlabel("lab time t"); a4.set_ylabel("τ")
for a in (a3, a4):
    a.spines[["top", "right"]].set_visible(False)
fig.suptitle("The entropic-time mini universe: time is the record of entropy exchange",
             y=0.99, fontsize=12)
plt.savefig("fig_mini_universe_time.png"); plt.close()

# ============================ Figure B =====================================
L, FILL, EPS, W = 200, 0.4, 0.2, 3.0
NF = int(FILL * L)
I0 = L // 2
WIN = 45
CLIP = 1e-14

def ground_C(h):
    wv, vv = np.linalg.eigh(h)
    occ = vv[:, :NF]
    return occ @ occ.T

def h_ent(x):
    x = np.clip(x, CLIP, 1 - CLIP)
    return -x * np.log(x) - (1 - x) * np.log(1 - x)

def S_sub(C, sites):
    return float(np.sum(h_ent(np.linalg.eigvalsh(C[np.ix_(sites, sites)]))))

def bond_metric(C, sites):
    return np.array([-np.log(max(S_sub(C, [a]) + S_sub(C, [b]) - S_sub(C, [a, b]), CLIP))
                     for a, b in zip(sites[:-1], sites[1:])])

h0 = np.zeros((L, L))
for i in range(L - 1):
    h0[i, i + 1] = h0[i + 1, i] = -0.5
vdef = EPS * np.exp(-(((np.arange(L) - I0) / W) ** 2))
C_vac, C_def = ground_C(h0), ground_C(h0 + np.diag(vdef))

sites = list(range(I0 - WIN, I0 + WIN + 1))
bm_vac, bm_def = bond_metric(C_vac, sites), bond_metric(C_def, sites)
xs = np.array(sites[:-1]) + 0.5 - I0

def dist_matrix(C):
    nn = len(sites)
    Wm = np.full((nn, nn), np.inf)
    for a in range(nn):
        for b in (a + 1, a + 2):
            if b < nn:
                mi = max(S_sub(C, [sites[a]]) + S_sub(C, [sites[b]])
                         - S_sub(C, [sites[a], sites[b]]), CLIP)
                Wm[a, b] = Wm[b, a] = -np.log(mi)
    return shortest_path(Wm, method="D")

D_stretch = dist_matrix(C_def) - dist_matrix(C_vac)

fig = plt.figure(figsize=(8.6, 5.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.5], hspace=0.42, wspace=0.24)
b1 = fig.add_subplot(gs[0, 0]); b2 = fig.add_subplot(gs[0, 1])
b3 = fig.add_subplot(gs[1, :])

x_all = np.arange(L) - I0
b1.plot(x_all, np.diag(C_vac), color=MUTED, lw=1.2, label="vacuum")
b1.plot(x_all, np.diag(C_def), color=AMBER, lw=1.6, label="with defect")
b1.set_xlim(-WIN, WIN)
b1.set_title("the matter field: density n(x)", loc="left")
b1.set_xlabel("x (sites from center)"); b1.legend(frameon=False, fontsize=8.5)

b2.plot(xs, bm_vac, color=MUTED, lw=1.2, label="vacuum")
b2.plot(xs, bm_def, color=TEAL, lw=1.6, label="with defect")
b2.set_title("the metric field: −ln I(x, x+1) — space dilates at the mass", loc="left")
b2.set_xlabel("x (sites from center)"); b2.legend(frameon=False, fontsize=8.5)
for a in (b1, b2):
    a.spines[["top", "right"]].set_visible(False)

im = b3.imshow(D_stretch, origin="lower", cmap="magma",
               extent=[-WIN, WIN, -WIN, WIN])
b3.set_title("the gravitational well: pairwise distance stretch  d_defect(x,y) − d_vacuum(x,y)",
             loc="left")
b3.set_xlabel("site x"); b3.set_ylabel("site y")
cb = fig.colorbar(im, ax=b3, shrink=0.9, pad=0.02)
cb.set_label("stretch (nats of lost mutual information)", fontsize=8.5)
fig.suptitle("The computable-geometry mini universe: distances from entanglement alone,\n"
             "curving around matter built from entanglement debt", y=1.01, fontsize=12)
plt.savefig("fig_mini_universe_geometry.png"); plt.close()
print("wrote fig_mini_universe_time.png and fig_mini_universe_geometry.png")
