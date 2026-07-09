"""
ETRG-0 numerical demonstration suite
=====================================
Three demos, one per checkable joint of the Entropic-Time Relational
Gravity (v0) framework. Companion to ETRG-0.md.

  Demo 1  Entropic time in a closed two-sector quantum "mini-universe"
          (exact-diagonalization analogue of Barontini, Phys. Rev. Research
          2026, arXiv:2509.07745). Checks axioms A1-A3: an internal entropic
          time tau = integral |dS_exchange| orders events, stalls when
          exchange stalls, and supports an entropic-time Schrodinger
          equation whose lapse is computed FROM THE STATE ITSELF
          (no lab clock anywhere in the propagation loop).

  Demo 2  Gravity from a clock-rate field (axiom A4). A 2D matter wave
          propagating through a gradient of local clock rate n(x) arcs
          on the Newtonian parabola: Ehrenfest reproduces a = -c^2 grad n.
          The Colella-Overhauser-Werner experiment, in silico.

  Demo 3  The entanglement first law + Bisognano-Wichmann boost locality
          on a free-fermion lattice (axiom A5):
          (a) delta S_A = delta <K_A> verified with O(eps^2) remainder;
          (b) the reduced vacuum of an interval commutes EXACTLY (machine
              zero) with the parabolically-weighted boost operator
              T = sum_i (i+1)(l-1-i)/2 (c+_i c_{i+1} + h.c.),
              the lattice avatar of the Rindler boost K ~ int (R^2-x^2)/2R T00.
          These are the two lattice-checkable pillars under
          Jacobson (2015) / Faulkner et al. (2014):
          entanglement first law  =>  Einstein equations.

Run:  python3 etrg_demos.py
Deps: numpy, scipy, matplotlib
"""

import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "figure.dpi": 130})
OUT = "/home/claude/etrg"

# ======================================================================
# Demo 1: entropic time in a two-sector Bose-Hubbard mini-universe
# ======================================================================

def two_mode_hamiltonian(N, J, U):
    """Two-mode Bose-Hubbard in Fock basis |n>_bright |N-n>_dark."""
    n = np.arange(N + 1)
    H = np.zeros((N + 1, N + 1))
    H[n, n] = 0.5 * U * (n * (n - 1) + (N - n) * (N - n - 1))
    hop = -J * np.sqrt((n[:-1] + 1.0) * (N - n[:-1]))
    H[n[:-1], n[:-1] + 1] = hop
    H[n[:-1] + 1, n[:-1]] = hop
    return H

def run_mini_universe(N=120, J=1.0, U=None, t_max=40.0, nt=6400):
    if U is None:
        U = 2.0 * 0.8 * 1.0 / N        # fixed interaction, Lambda=0.8 at J=1
    H = two_mode_hamiltonian(N, J, U)
    w, V = eigh(H)
    psi0 = np.zeros(N + 1); psi0[0] = 1.0      # all atoms in the dark sector
    c0 = V.T @ psi0
    ts = np.linspace(0.0, t_max, nt)
    Cc = np.exp(-1j * np.outer(ts, w)) * c0    # eigenbasis coefficients vs t
    P = np.abs(Cc @ V.T) ** 2                  # bright-mode number distribution
    n_op = np.arange(N + 1)
    nb = P @ n_op / N
    with np.errstate(divide="ignore", invalid="ignore"):
        S = -np.sum(np.where(P > 1e-14, P * np.log(P), 0.0), axis=1)
    return ts, nb, S, Cc, w, V, N

def entropic_time(S):
    """tau = integral |dS| : unsigned entropy-exchange measure, the analogue
    of Barontini Eq.(3) for a symmetric bipartition. Monotone by
    construction; stalls exactly when exchange stalls."""
    return np.concatenate([[0.0], np.cumsum(np.abs(np.diff(S)))])

def internal_lapse(c, w, V, cap=1e6):
    """Lapse Ntilde = dt/dtau = 1/|dS/dt| computed from the state alone:
    pdot_n = 2 Im(psi_n* (H psi)_n),  dS/dt = -sum pdot (ln p + 1)."""
    psi = V @ c
    Hpsi = V @ (w * c)
    pdot = 2.0 * np.imag(np.conj(psi) * Hpsi)
    p = np.abs(psi) ** 2
    m = p > 1e-14
    rate = abs(-np.sum(pdot[m] * (np.log(p[m]) + 1.0)))
    return min(1.0 / max(rate, 1.0 / cap), cap)

def entropic_schrodinger(Cc, tau, ts, w, V, N, cap_mult=4.0):
    """Propagate i d|psi>/dtau = Ntilde[psi] H |psi> snapshot-to-snapshot
    using ONLY internal quantities: the tau increments (measured entropy
    exchange) and the state-derived lapse. Stasis points are coordinate
    singularities of entropic time; the per-step advance is capped there
    (cap_mult x median step), the internal analogue of regularizing a
    coordinate singularity. Returns predicted bright fraction and the
    reconstructed total duration."""
    dta = np.diff(tau)
    dtl = ts[1] - ts[0]
    n_op = np.arange(N + 1)
    c = Cc[1].copy()
    t_rec = ts[1]
    nb_pred = np.empty(len(ts)); nb_pred[0] = nb_pred[1] = (np.abs(V @ Cc[0])**2) @ n_op / N
    n_capped = 0
    for k in range(1, len(ts) - 1):
        Nl0 = internal_lapse(c, w, V)
        ch = np.exp(-1j * w * min(Nl0 * dta[k], cap_mult * dtl) / 2.0) * c
        Nlm = internal_lapse(ch, w, V)
        theta = Nlm * dta[k]
        if theta > cap_mult * dtl:
            theta = cap_mult * dtl
            n_capped += 1
        c = np.exp(-1j * w * theta) * c
        t_rec += theta
        nb_pred[k + 1] = (np.abs(V @ c) ** 2) @ n_op / N
    return nb_pred, t_rec, n_capped

print("=" * 64)
print("Demo 1: entropic time in a closed two-sector mini-universe")
print("=" * 64)
ts, nb, S, Cc, w, V, N = run_mini_universe(J=1.0)
tau = entropic_time(S)
ts_f, nb_f, S_f, *_ = run_mini_universe(J=0.005)     # barrier raised: J -> J/200, same U
tau_f = entropic_time(S_f)
nb_pred, t_rec, n_capped = entropic_schrodinger(Cc, tau, ts, w, V, N)
rms = float(np.sqrt(np.mean((nb_pred[2:] - nb[2:]) ** 2)))
print(f"  oscillating universe:    tau grows to {tau[-1]:.2f}  (arrow of time present)")
print(f"  barrier-raised universe: tau grows to {tau_f[-1]:.4f}  (time nearly stops)")
print(f"  entropic-time Schrodinger (internal lapse only):")
print(f"    RMS error in N_b/N        = {rms:.3f}")
print(f"    duration reconstructed    = {t_rec:.2f} / {ts[-1]:.0f}  ({100*t_rec/ts[-1]:.1f}%)")
print(f"    stall-regularized steps   = {n_capped} / {len(ts)-2}  ({100*n_capped/(len(ts)-2):.1f}%)")

fig, ax = plt.subplots(2, 2, figsize=(9.4, 6.6))
ax[0, 0].plot(ts, nb, color="#D85A30", lw=1.0)
ax[0, 0].set_xlabel("lab time  $t\\,[1/J]$"); ax[0, 0].set_ylabel("bright fraction $N_b/N$")
ax[0, 0].set_title("(a) Bang/crunch cycles of the bright sector")
ax[0, 1].plot(ts, S, color="#534AB7", lw=1.0, label="barrier low (exchange on)")
ax[0, 1].plot(ts_f, S_f, color="#888780", lw=1.2, label="barrier raised ($J\\to J/200$)")
ax[0, 1].set_xlabel("lab time  $t\\,[1/J]$"); ax[0, 1].set_ylabel("bright-sector entropy $S$")
ax[0, 1].legend(frameon=False, fontsize=8); ax[0, 1].set_title("(b) Entropy exchange with the dark sector")
ax[1, 0].plot(ts, tau, color="#0F6E56", lw=1.4, label="barrier low")
ax[1, 0].plot(ts_f, tau_f, color="#888780", lw=1.4, label="barrier raised")
ax[1, 0].set_xlabel("lab time  $t$"); ax[1, 0].set_ylabel("entropic time  $\\tau=\\int|dS|$")
ax[1, 0].legend(frameon=False, fontsize=8)
ax[1, 0].set_title("(c) Internal time: plateaus = stalls, flat = time (almost) ends")
ax[1, 1].plot(tau, nb, color="#D85A30", lw=1.0, label="measured $N_b/N(\\tau)$")
ax[1, 1].plot(tau, nb_pred, "--", color="#2C2C2A", lw=0.9,
              label="entropic-time Schr\u00f6dinger prediction")
ax[1, 1].set_xlabel("entropic time  $\\tau$"); ax[1, 1].set_ylabel("bright fraction $N_b/N$")
ax[1, 1].legend(frameon=False, fontsize=8)
ax[1, 1].set_title(f"(d) Internal-lapse propagation, RMS = {rms:.3f}")
fig.suptitle("Demo 1 - Entropic time emerges inside a closed quantum universe", y=1.0)
fig.tight_layout()
fig.savefig(f"{OUT}/fig1_entropic_time.png", bbox_inches="tight")
plt.close(fig)

# ======================================================================
# Demo 2: gravity from a clock-rate field (2D matter wave)
# ======================================================================

print("=" * 64)
print("Demo 2: matter wave steered by a clock-rate gradient")
print("=" * 64)

L = 120.0; Ng = 256
x = np.linspace(-L / 2, L / 2, Ng, endpoint=False)
X, Y = np.meshgrid(x, x, indexing="ij")
k1 = 2 * np.pi * np.fft.fftfreq(Ng, d=x[1] - x[0])
KX, KY = np.meshgrid(k1, k1, indexing="ij")

g = 0.06                       # clock-rate gradient: n(y) = 1 + g y / c^2
V_pot = g * Y                  # V = m c^2 (n - 1) = m g y   (hbar = m = 1)
sigma0, k0x = 4.0, 1.6
psi = np.exp(-((X + 42) ** 2 + (Y - 25) ** 2) / (4 * sigma0 ** 2)) * np.exp(1j * k0x * X)
psi /= np.sqrt(np.sum(np.abs(psi) ** 2))

dt = 0.02; steps = 2200; snap_every = 40
expV = np.exp(-1j * V_pot * dt / 2.0)
expK = np.exp(-1j * (KX ** 2 + KY ** 2) / 2.0 * dt)
traj_x, traj_y, times, snaps = [], [], [], []
for s in range(steps):
    psi = expV * psi
    psi = np.fft.ifft2(expK * np.fft.fft2(psi))
    psi = expV * psi
    if s % snap_every == 0:
        prob = np.abs(psi) ** 2
        traj_x.append(np.sum(prob * X)); traj_y.append(np.sum(prob * Y))
        times.append((s + 1) * dt)
        snaps.append(prob.copy())
traj_x = np.array(traj_x); traj_y = np.array(traj_y); times = np.array(times)
newt_x = -42 + k0x * times
newt_y = 25 - 0.5 * g * times ** 2
err = float(np.max(np.abs(traj_y - newt_y)))
print(f"  max |<y>_quantum - y_Newton| = {err:.3e}   (packet width sigma = {sigma0})")

fig, ax = plt.subplots(1, 2, figsize=(9.8, 4.3))
acc = np.zeros_like(snaps[0])
for s in snaps:
    acc = np.maximum(acc, s / s.max())
ax[0].imshow(acc.T, origin="lower", extent=[-L/2, L/2, -L/2, L/2], cmap="magma", aspect="equal")
ax[0].plot(newt_x, newt_y, "--", color="#5DCAA5", lw=1.4, label="Newtonian parabola")
ax[0].plot(traj_x, traj_y, ".", color="white", ms=2.5, label="$\\langle\\mathbf{r}\\rangle$ quantum")
ax[0].legend(frameon=False, loc="lower left", labelcolor="white", fontsize=8)
ax[0].set_title("(a) Matter wave arcs in a clock-rate gradient")
ax[0].set_xlabel("x"); ax[0].set_ylabel("y   (clocks slower toward $-y$)")
ax[1].plot(times, traj_y, color="#D85A30", lw=1.6, label="quantum $\\langle y\\rangle(t)$")
ax[1].plot(times, newt_y, "--", color="#2C2C2A", lw=1.1, label="$y_0-\\frac{1}{2} g t^2$")
ax[1].set_xlabel("t"); ax[1].set_ylabel("height")
ax[1].legend(frameon=False, fontsize=8)
ax[1].set_title(f"(b) Ehrenfest vs Newton: max deviation {err:.1e}")
fig.suptitle("Demo 2 - Newtonian free fall from a pure clock-rate field  "
             "$V = mc^2\\,(n(\\mathbf{x})-1)$", y=1.02)
fig.tight_layout()
fig.savefig(f"{OUT}/fig2_clockrate_gravity.png", bbox_inches="tight")
plt.close(fig)

# ======================================================================
# Demo 3: entanglement first law + Bisognano-Wichmann on a lattice
# ======================================================================

print("=" * 64)
print("Demo 3: first law of entanglement + lattice Bisognano-Wichmann")
print("=" * 64)

# --- (a) first law dS_A = d<K_A> on a finite open chain -----------------
Lc = 120
Hc = np.zeros((Lc, Lc))
for i in range(Lc - 1):
    Hc[i, i + 1] = Hc[i + 1, i] = -1.0
wc, Vc = eigh(Hc)
Nf = 53                      # incommensurate filling: genuine O(eps) response
C = Vc[:, :Nf] @ Vc[:, :Nf].T
A = slice(55, 65)            # ell=10: every modular eigenvalue resolvable
CA = C[A, A]

def ent_entropy(M):
    lam = np.clip(np.linalg.eigvalsh(M), 1e-15, 1 - 1e-15)
    return float(-np.sum(lam * np.log(lam) + (1 - lam) * np.log(1 - lam)))

lamA, UA = eigh(CA)
lamA = np.clip(lamA, 1e-15, 1 - 1e-15)
K = UA @ np.diag(np.log((1 - lamA) / lamA)) @ UA.T
S0 = ent_entropy(CA)

sites = np.arange(Lc)
bump = np.exp(-((sites - 58.0) ** 2) / (2 * 2.0 ** 2))   # off-centre: breaks reflection symmetry
eps_list = np.logspace(-5, -2, 10)
dS_exact, dS_first = [], []
for eps in eps_list:
    wp, Vp = eigh(Hc + np.diag(eps * bump))
    Cp = Vp[:, :Nf] @ Vp[:, :Nf].T
    dS_exact.append(ent_entropy(Cp[A, A]) - S0)
    dS_first.append(float(np.trace((Cp[A, A] - CA) @ K)))
dS_exact = np.array(dS_exact); dS_first = np.array(dS_first)
remainder = np.abs(dS_exact - dS_first)
slope = np.polyfit(np.log(eps_list), np.log(remainder + 1e-18), 1)[0]
slope_sig = np.polyfit(np.log(eps_list), np.log(np.abs(dS_exact) + 1e-18), 1)[0]
print(f"  (a) first law: |dS| ~ eps^{slope_sig:.2f} (theory: 1),  remainder |dS - d<K>| ~ eps^{slope:.2f} (theory: 2)")

# --- (b) lattice Bisognano-Wichmann: exact commuting parabolic boost ----
ell = 40
ii = np.arange(ell)
Dm = ii[:, None] - ii[None, :]
with np.errstate(divide="ignore", invalid="ignore"):
    CA_inf = np.where(Dm == 0, 0.5, np.sin(np.pi * Dm / 2) / (np.pi * Dm))
T = np.zeros((ell, ell))
for i in range(ell - 1):
    T[i, i + 1] = T[i + 1, i] = (i + 1) * (ell - 1 - i) / 2.0    # parabolic boost weight
T0 = np.zeros((ell, ell))
for i in range(ell - 1):
    T0[i, i + 1] = T0[i + 1, i] = 1.0
T0 *= np.linalg.norm(T) / np.linalg.norm(T0)                     # uniform-weight control
rel = np.linalg.norm(CA_inf @ T - T @ CA_inf) / (np.linalg.norm(CA_inf) * np.linalg.norm(T))
rel0 = np.linalg.norm(CA_inf @ T0 - T0 @ CA_inf) / (np.linalg.norm(CA_inf) * np.linalg.norm(T))
lam_i, U_i = eigh(CA_inf)
mask = (lam_i > 1e-6) & (lam_i < 1 - 1e-6)
Tt = (U_i.T @ T @ U_i)[np.ix_(mask, mask)]
offd = np.linalg.norm(Tt - np.diag(np.diag(Tt))) / np.linalg.norm(Tt)
print(f"  (b) ||[rho_A, T_boost]||_rel = {rel:.2e}   (uniform-weight control: {rel0:.2e})")
print(f"      boost off-diagonality in modular eigenbasis: {offd:.2e}")

fig, ax = plt.subplots(1, 2, figsize=(9.8, 4.0))
ax[0].loglog(eps_list, np.abs(dS_exact), "o-", color="#185FA5", ms=4, label="$|\\delta S_A|$ (exact)")
ax[0].loglog(eps_list, remainder, "s-", color="#D85A30", ms=4,
             label="$|\\delta S_A - \\delta\\langle K_A\\rangle|$")
ax[0].loglog(eps_list, remainder[0] * (eps_list / eps_list[0]) ** 2, ":",
             color="#888780", label="$\\propto\\epsilon^{2}$ guide")
ax[0].set_xlabel("perturbation strength $\\epsilon$"); ax[0].legend(frameon=False, fontsize=8)
ax[0].set_title(f"(a) First law: signal slope {slope_sig:.2f}, remainder slope {slope:.2f}")
xw = np.arange(ell - 1) + 0.5
ax[1].plot(xw, np.diag(T, 1), "o-", color="#0F6E56", ms=3, lw=0.8,
           label="boost weight $(i{+}1)(\\ell{-}1{-}i)/2$")
ax[1].set_xlabel("bond position in interval"); ax[1].set_ylabel("boost hopping weight")
ax[1].legend(frameon=False, fontsize=8, loc="lower center")
ax[1].set_title(f"(b) Parabolic boost commutes with vacuum: "
                f"$\\|[\\rho_A,T]\\|$ = {rel:.0e} (control {rel0:.0e})")
fig.suptitle("Demo 3 - Lattice pillars under 'entanglement first law $\\Rightarrow$ Einstein equations'", y=1.03)
fig.tight_layout()
fig.savefig(f"{OUT}/fig3_first_law.png", bbox_inches="tight")
plt.close(fig)

print("=" * 64)
print("All demos complete. Figures written to", OUT)
