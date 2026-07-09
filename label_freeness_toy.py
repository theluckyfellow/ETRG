#!/usr/bin/env python3
"""
label_freeness_toy.py

Four-run toy for the label-freeness argument in ETRG-0_label_freeness_note.md.

Two-mode Bose-Hubbard mini-universe, N=60, Hilbert-space dimension 61.
H = -J(a1+ a2 + a2+ a1) + (U/2)(n1(n1-1) + n2(n2-1)),  J=1, U=0.02.
Bright sector = mode 1; initial state = all bosons in mode 1 (|n=N>).

Runs:
  1. Exact Schrodinger evolution psi(t), record S(t), tau(t)=integral |dS|.
  2. A7 reconstruction in entropic time: i dpsi/dtau = Ntilde[psi] H psi,
     Ntilde = |dS/dt|^{-1}.  Report matched-state fidelity to run 1.
  3. State-functional feedback: H -> H + g S_bright[psi] V, V=n1, g=0.05.
     Evolve in t and reconstruct in tau.  Orbits should coincide (fidelity ~1).
  4. Label-consuming feedback: H -> H + g (dS/dlambda) V.
     In t-run lambda=t (use dS/dt); in tau-run lambda=tau (use dS/dtau).
     Orbits should diverge.

Output: printed summary table (min/mean fidelity for runs 2,3,4) and optional
fidelity plot as label_freeness_toy.png.

Integrator: RK4 with dt <= 1e-3 in natural units, run to t=20.
"""

import numpy as np
from scipy.linalg import eigh

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
N = 60
J = 1.0
U = 0.02
g = 0.05

dt = 2.5e-4
t_max = 20.0
nt = int(round(t_max / dt)) + 1
ts = np.linspace(0.0, t_max, nt)

n_states = N + 1
rng = np.arange(n_states, dtype=float)

# ---------------------------------------------------------------------------
# Hamiltonian and operators
# ---------------------------------------------------------------------------
def two_mode_hamiltonian(N, J, U):
    n = np.arange(N + 1, dtype=float)
    H = np.zeros((N + 1, N + 1), dtype=complex)
    H[np.arange(N + 1), np.arange(N + 1)] = 0.5 * U * (n * (n - 1) + (N - n) * (N - n - 1))
    hop = -J * np.sqrt((n[:-1] + 1.0) * (N - n[:-1]))
    H[np.arange(N), np.arange(N) + 1] = hop
    H[np.arange(N) + 1, np.arange(N)] = hop
    return H

H = two_mode_hamiltonian(N, J, U).astype(complex)
V = np.diag(rng).astype(complex)       # number operator on mode 1

psi0 = np.zeros(n_states, dtype=complex)
psi0[N] = 1.0

def normalize(v):
    nrm = np.linalg.norm(v)
    return v / nrm if nrm > 0 else v

# ---------------------------------------------------------------------------
# Shannon entropy of the bright sector (populations are |psi_n|^2)
# ---------------------------------------------------------------------------
def entropy(psi):
    p = np.abs(psi) ** 2
    m = p > 1e-14
    return float(-np.sum(p[m] * np.log(p[m])))

def entropy_rows(P):
    """P[k,n] -> entropy for each row."""
    m = P > 1e-14
    return -np.sum(np.where(m, P * np.log(P), 0.0), axis=1)

# ---------------------------------------------------------------------------
# dS/d* rate: d/dlambda S = -2 Im[ <psi| ln rho_B  H_eff |psi> ]
#                    = -sum_n 2 Im(psi_n* (H_eff psi)_n) ln p_n
# where rho_B = diag(p_n) in the Fock basis.  This gives the instantaneous
# rate of change of S for ANY generator H_eff (Hermitian, may be state-dependent).
# ---------------------------------------------------------------------------
def dS_rate(psi, Heff_psi=None, Heff=None):
    if Heff_psi is None:
        Heff_psi = Heff @ psi
    p = np.abs(psi) ** 2
    pdot = 2.0 * np.imag(np.conj(psi) * Heff_psi)
    m = p > 1e-14
    return float(-np.sum(pdot[m] * np.log(p[m])))

def nt_lapse(rate, cap=1e6):
    if abs(rate) < 1e-15:
        return float(cap)
    return float(min(1.0 / abs(rate), cap))

def compute_step(rate, dtau, dt_ref, cap_mult=4.0):
    """Return (tau_step, t_step, effective_Nl) with t_step capped.

    We want to integrate i dpsi/dtau = Ntilde H psi.  With dtau as the
    entropic-time increment, the corresponding lab-time increment would be
    Ntilde*dtau.  At stasis points (rate -> 0) Ntilde diverges; we regularize
    by capping the effective lab-time step to cap_mult * dt_ref.
    """
    Nl = nt_lapse(rate)
    t_step = Nl * dtau
    cap = cap_mult * dt_ref
    if t_step > cap:
        t_step = cap
        Nl = t_step / max(dtau, 1e-30)
    return dtau, t_step, Nl

# ---------------------------------------------------------------------------
# Projective RK4 on the unit sphere for a state-dependent Hermitian operator
# Hfn(psi) returning a matrix.  Equation: i dpsi/dlambda = Heff[psi] psi.
# All internal evaluations are performed on normalized states so that the
# entropic-rate/entropy functionals are evaluated on physical states.
# ---------------------------------------------------------------------------
def rk4_step_operator(psi, h, Hfn):
    y = normalize(psi)
    k1 = -1j * h * (Hfn(y) @ y)
    y1 = normalize(y + 0.5 * k1)
    k2 = -1j * h * (Hfn(y1) @ y1)
    y2 = normalize(y + 0.5 * k2)
    k3 = -1j * h * (Hfn(y2) @ y2)
    y3 = normalize(y + k3)
    k4 = -1j * h * (Hfn(y3) @ y3)
    return normalize(y + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0)

# ---------------------------------------------------------------------------
# Run 1: exact linear evolution via full diagonalization
# ---------------------------------------------------------------------------
print("=" * 70)
print("Run 1: exact evolution, S(t), tau(t)")
print("=" * 70)

w, Vmat = eigh(H)
c0 = Vmat.T @ psi0

psi1 = np.zeros((nt, n_states), dtype=complex)
for i, t in enumerate(ts):
    psi1[i] = normalize(Vmat @ (np.exp(-1j * w * t) * c0))

P1 = np.abs(psi1) ** 2
S1 = entropy_rows(P1)
tau1 = np.concatenate(([0.0], np.cumsum(np.abs(np.diff(S1)))))
print(f"  End entropic time tau(20) = {tau1[-1]:.6f}")
print(f"  Max bright-sector entropy = {S1.max():.6f}")

# ---------------------------------------------------------------------------
# Run 2: A7 reconstruction in entropic time
# ---------------------------------------------------------------------------
print("=" * 70)
print("Run 2: A7 reconstruction (fidelity to exact t-evolution)")
print("=" * 70)

psi = psi0.copy()
fids2 = np.zeros(nt)
fids2[0] = 1.0
for i in range(nt - 1):
    dtau = tau1[i + 1] - tau1[i]
    if dtau > 1e-16:
        Hpsi = H @ psi
        r = dS_rate(psi, Heff_psi=Hpsi)
        _, _, Nl = compute_step(r, dtau, dt)
        psi = rk4_step_operator(psi, dtau, lambda p: Nl * H)
    target = psi1[i + 1]
    fids2[i + 1] = abs(np.vdot(target, psi))

print(f"  min fidelity  = {fids2[1:].min():.6e}")
print(f"  mean fidelity = {fids2[1:].mean():.12f}")

# ---------------------------------------------------------------------------
# Run 3: state-functional feedback H -> H + g S[psi] V
# ---------------------------------------------------------------------------
print("=" * 70)
print("Run 3: state-functional feedback (safe channel)")
print("=" * 70)

# t-run
psi3 = np.zeros((nt, n_states), dtype=complex)
S3 = np.zeros(nt)
tau3 = np.zeros(nt)
psi3[0] = psi0.copy()
psi = psi0.copy()
for i in range(nt - 1):
    def Hfn3_t(p):
        S_loc = entropy(p)
        return H + (g * S_loc) * V
    psi = rk4_step_operator(psi, dt, Hfn3_t)
    S = entropy(psi)
    tau3[i + 1] = tau3[i] + abs(S - S3[i])
    S3[i + 1] = S
    psi3[i + 1] = psi

print(f"  t-run: tau(20) = {tau3[-1]:.6f}")

psi = psi0.copy()
fids3 = np.zeros(nt)
fids3[0] = 1.0
for i in range(nt - 1):
    dtau = tau3[i + 1] - tau3[i]
    if dtau > 1e-16:
        S = entropy(psi)
        Heff = H + (g * S) * V
        Heff_psi = Heff @ psi
        r = dS_rate(psi, Heff_psi=Heff_psi)
        _, _, Nl = compute_step(r, dtau, dt)
        psi = rk4_step_operator(psi, dtau, lambda p: Nl * Heff)
    target = psi3[i + 1]
    fids3[i + 1] = abs(np.vdot(target, psi))

print(f"  min fidelity  = {fids3[1:].min():.6e}")
print(f"  mean fidelity = {fids3[1:].mean():.12f}")

# ---------------------------------------------------------------------------
# Run 4: label-consuming feedback H -> H + g (dS/dlambda) V
# ---------------------------------------------------------------------------
print("=" * 70)
print("Run 4: label-consuming feedback (control leak)")
print("=" * 70)

psi4 = np.zeros((nt, n_states), dtype=complex)
S4 = np.zeros(nt)
tau4 = np.zeros(nt)
psi4[0] = psi0.copy()
psi = psi0.copy()
for i in range(nt - 1):
    def Hfn4_t(p):
        Hp = H @ p
        r_loc = dS_rate(p, Heff_psi=Hp)
        return H + (g * r_loc) * V
    psi = rk4_step_operator(psi, dt, Hfn4_t)
    S = entropy(psi)
    tau4[i + 1] = tau4[i] + abs(S - S4[i])
    S4[i + 1] = S
    psi4[i + 1] = psi

print(f"  t-run: tau(20) = {tau4[-1]:.6f}")

psi = psi0.copy()
fids4 = np.zeros(nt)
fids4[0] = 1.0
for i in range(nt - 1):
    dtau = tau4[i + 1] - tau4[i]
    if dtau > 1e-16:
        # sign of dS/dt under the kinetic part; V diagonal -> same under full H_eff.
        Hpsi = H @ psi
        r = dS_rate(psi, Heff_psi=Hpsi)
        s = 1.0 if r > 0 else (-1.0 if r < 0 else 0.0)
        Heff = H + (g * s) * V
        Heff_psi = Heff @ psi
        r_full = dS_rate(psi, Heff_psi=Heff_psi)
        _, _, Nl = compute_step(r_full, dtau, dt)
        psi = rk4_step_operator(psi, dtau, lambda p: Nl * Heff)
    target = psi4[i + 1]
    fids4[i + 1] = abs(np.vdot(target, psi))

print(f"  min fidelity  = {fids4[1:].min():.6e}")
print(f"  mean fidelity = {fids4[1:].mean():.12f}")

# ---------------------------------------------------------------------------
# Run 5 (GLM round-4 proposal): couple the LAPSE itself, as a state functional.
# H -> H + g * Ncap[psi] * V with Ncap = min(1/|dS/dt[psi]|, NCAP), where
# dS/dt is computed from the state via the bare H (pure state functional,
# identical in both parameterizations). Refined R3 rule predicts SAFETY:
# state-computed rates are label-free; only d/d(label-in-use) leaks.
# ---------------------------------------------------------------------------
print("=" * 70)
print("Run 5: lapse-as-state-functional feedback (GLM control; predicted safe)")
print("=" * 70)

NCAP = 20.0

def Ncap_of(p):
    r_loc = dS_rate(p, Heff_psi=H @ p)
    return float(min(1.0 / max(abs(r_loc), 1e-15), NCAP))

psi5 = np.zeros((nt, n_states), dtype=complex)
S5 = np.zeros(nt)
tau5 = np.zeros(nt)
psi5[0] = psi0.copy()
psi = psi0.copy()
for i in range(nt - 1):
    def Hfn5_t(p):
        return H + (g * Ncap_of(p)) * V
    psi = rk4_step_operator(psi, dt, Hfn5_t)
    S = entropy(psi)
    tau5[i + 1] = tau5[i] + abs(S - S5[i])
    S5[i + 1] = S
    psi5[i + 1] = psi

print(f"  t-run: tau(20) = {tau5[-1]:.6f}")

psi = psi0.copy()
fids5 = np.zeros(nt)
fids5[0] = 1.0
for i in range(nt - 1):
    dtau = tau5[i + 1] - tau5[i]
    if dtau > 1e-16:
        Heff = H + (g * Ncap_of(psi)) * V
        r = dS_rate(psi, Heff_psi=Heff @ psi)
        _, _, Nl = compute_step(r, dtau, dt)
        psi = rk4_step_operator(psi, dtau, lambda p: Nl * Heff)
    target = psi5[i + 1]
    fids5[i + 1] = abs(np.vdot(target, psi))

print(f"  min fidelity  = {fids5[1:].min():.6e}")
print(f"  mean fidelity = {fids5[1:].mean():.12f}")

# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
print("=" * 70)
print("SUMMARY TABLE: min/mean matched-state fidelity")
print("=" * 70)
print(f"{'Run':>4}  {'Description':<40}  {'min fidelity':>16}  {'mean fidelity':>16}")
print("-" * 70)
runs = [
    ("2", "A7 reconstruction", fids2),
    ("3", "state-functional feedback", fids3),
    ("4", "label-consuming feedback", fids4),
    ("5", "lapse-as-state-functional (GLM control)", fids5),
]
for rnum, desc, f in runs:
    print(f"{rnum:>4}  {desc:<40}  {f[1:].min():16.6e}  {f[1:].mean():16.12f}")
print("=" * 70)

# ---------------------------------------------------------------------------
# Optional plot
# ---------------------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.semilogy(ts[1:], 1.0 - fids2[1:], label="Run 2: A7 reconstruction", alpha=0.8)
    plt.semilogy(ts[1:], 1.0 - fids3[1:], label="Run 3: state-functional feedback", alpha=0.8)
    plt.semilogy(ts[1:], 1.0 - fids4[1:], label="Run 4: label-consuming feedback", alpha=0.8)
    plt.xlabel("lab time  $t$")
    plt.ylabel("infidelity  $1 - |\\langle\\psi_t|\\psi_\\tau\\rangle|$")
    plt.title("Label-freeness toy: matched-state infidelity")
    plt.legend(frameon=False)
    plt.grid(True, which="both", ls=":", alpha=0.5)
    plt.tight_layout()
    plt.savefig("label_freeness_toy.png", dpi=150)
    print("Wrote label_freeness_toy.png")
except Exception as e:
    print(f"Plot skipped ({e})")
