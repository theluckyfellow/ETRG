#!/usr/bin/env python3
"""
Interval-entropy cone check (referee F1's successor, PRE-REGISTERED) --
the static state's cone face, done right.

Referee F1 showed mi_decomposition_check.py's D1 was doubly broken: a
saturated predictor (all pairs symmetric, cone-distance change nearly
constant) and the wrong static observable (nn-MI graph distance conflates
compressibility with velocity).  The correct static observable (Dubail-
Stephan-Viti-Calabrese, SciPost 2017): a chain with varying hopping is a
curved-space CFT vacuum whose INTERVAL ENTROPIES are functions of the
conformal cone distance

    d_conf(i,j) = sum_{x=i}^{j-1} 1/v_F(x),   v_F(x) = 2 t(x) sin(pi n)

so that for defect-spanning intervals,  Delta S = (1/3) Delta ln d_conf.

TWO CONES, stated explicitly (referee's requirement): the BARE band-edge
cone 2t(x) is what quench fronts read (mi_decomposition D3); the DRESSED
Fermi-velocity cone 2t(x) sin(pi n) is what static correlations read.
This check uses the dressed cone.

PRE-REGISTERED PREDICTIONS:
  E1  cone deformation: corr(Delta S, (1/3) Delta ln d_conf) > 0.7,
      slope reported (finite-size deficit expected, not barred).
  E2  debt-matched scale deformation: corr < 0.3 (no distance-structured
      trace -- the debt is distance-unstructured).
  E3  FSS: E1's correlation holds or grows across L = 100, 200, 400.
  E4  intervals are ASYMMETRIC (left endpoints I0-40..I0-10, right
      I0+10..I0+40) so the predictor is non-saturated by construction.
"""

import numpy as np
from scipy.optimize import brentq

clip = 1e-14
FILL_FRAC = 0.4
W = 6.0
EPS = 0.3
I0_FRAC = 0.5

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def hamiltonian(L, I0, cone_mod=0.0, pot_mod=0.0):
    h = np.zeros((L, L))
    Phi = np.exp(-(((np.arange(L) - I0) / W) ** 2))
    for i in range(L - 1):
        t = 0.5 * (1 - cone_mod * 0.5 * (Phi[i] + Phi[i + 1]))
        h[i, i + 1] = h[i + 1, i] = -t
    h += np.diag(pot_mod * Phi)
    return h

def correlation(h, N):
    _, V = np.linalg.eigh(h)
    occ = V[:, :N]
    return occ @ occ.T.conj()

def S_interval(C, a, b):
    sub = C[np.ix_(np.arange(a, b + 1), np.arange(a, b + 1))]
    return float(np.sum(binary_entropy(np.linalg.eigvalsh(sub))))

def modular_debt(C_vac, C_def, I0, r=20):
    sites = list(range(I0 - r, I0 + r + 1))
    sub_v = C_vac[np.ix_(sites, sites)]
    sub_d = C_def[np.ix_(sites, sites)]
    n, U = np.linalg.eigh(sub_v)
    n = np.clip(np.real(n), clip, 1 - clip)
    xi = np.log((1 - n) / n)
    dC = U.conj().T @ (sub_d - sub_v) @ U
    return float(np.real(np.sum(xi * np.diag(dC))))

def d_conf_fn(L, I0, cone_mod):
    """Cumulative conformal distance along the chain (dressed cone)."""
    Phi = np.exp(-(((np.arange(L) - I0) / W) ** 2))
    vF = np.array([2 * 0.5 * (1 - cone_mod * 0.5 * (Phi[i] + Phi[i + 1]))
                   for i in range(L - 1)]) * np.sin(np.pi * FILL_FRAC)
    cum = np.concatenate([[0], np.cumsum(1.0 / vF)])
    return lambda a, b: cum[b] - cum[a]

def run_L(L):
    I0 = int(L * I0_FRAC)
    N = int(L * FILL_FRAC)
    C0 = correlation(hamiltonian(L, I0), N)
    C_cone = correlation(hamiltonian(L, I0, cone_mod=EPS), N)
    debt = modular_debt(C0, C_cone, I0)
    eps_p = brentq(
        lambda e: modular_debt(C0, correlation(
            hamiltonian(L, I0, pot_mod=e), N), I0) - debt, 0.001, 2.0)
    C_scale = correlation(hamiltonian(L, I0, pot_mod=eps_p), N)

    dc_vac = d_conf_fn(L, I0, 0.0)
    dc_def = d_conf_fn(L, I0, EPS)

    dS_cone, dS_scale, pred = [], [], []
    for da in [40, 30, 20, 10]:
        for db in [10, 20, 30, 40]:
            a, b = I0 - da, I0 + db
            dS_cone.append(S_interval(C_cone, a, b) - S_interval(C0, a, b))
            dS_scale.append(S_interval(C_scale, a, b) - S_interval(C0, a, b))
            pred.append((1 / 3) * np.log(dc_def(a, b) / dc_vac(a, b)))
    r_cone = float(np.corrcoef(dS_cone, pred)[0, 1])
    r_scale = float(np.corrcoef(dS_scale, pred)[0, 1])
    slope = float(np.polyfit(pred, dS_cone, 1)[0])
    return r_cone, r_scale, slope

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 78)
print("INTERVAL-ENTROPY CONE CHECK -- the static state's cone face")
print("=" * 78)
print()
print(f"{'L':>5s}  {'r_cone':>8s}  {'r_scale':>8s}  {'slope':>7s}")
print("-" * 78)
rs = []
rscales = []
for L in [100, 200, 400]:
    r_cone, r_scale, slope = run_L(L)
    rs.append(r_cone)
    rscales.append(r_scale)
    print(f"{L:>5d}  {r_cone:8.4f}  {r_scale:8.4f}  {slope:7.3f}")
print("-" * 78)
print()

print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("E1: cone deformation, corr(Delta S, (1/3)Delta ln d_conf) > 0.7",
     rs[1] > 0.7, f"{rs[1]:.3f} at L=200"),
    ("E2: debt-matched scale deformation, corr < 0.3",
     rscales[1] < 0.3, f"{rscales[1]:.3f} at L=200"),
    ("E3: correlation holds or grows across L",
     rs[2] >= rs[0] - 0.05, f"{rs[0]:.3f} -> {rs[1]:.3f} -> {rs[2]:.3f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<58s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
