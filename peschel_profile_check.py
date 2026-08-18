#!/usr/bin/env python3
"""
Peschel/CFT profile check (referee nomination 2) -- PRE-REGISTERED.

The weld conjecture says Q10/Bisognano-Wichmann is the exact-locality limit
of P-select.  Its anchor so far is a CITATION (BW + Eisler-Peschel).  This
check converts the anchor to a MEASUREMENT: for a contiguous interval of a
critical chain, the modular kernel's nearest-neighbor hopping profile J(x)
must follow the CFT/Peschel parabola

    J(x)  proportional to  (x - x_0)(x_1 - x)     over the interval [x_0, x_1]

(the entanglement Hamiltonian of an interval is the local boost generator
with a parabolic weight -- the lattice image of Bisognano-Wichmann).

PRE-REGISTERED PREDICTIONS:
  P1  vacuum, interval L/2: Pearson r(J, parabola) > 0.9
  P2  vacuum, interval L/4: Pearson r > 0.9 (robust to interval size)
  P3  Haar-random state, same interval: r < 0.5 (teeth -- a parabola is
      not extractable from noise)
If P1/P2 pass and P3 fails, the weld's anchor is measured, not cited.
"""

import numpy as np

L = 400
N = L // 2
clip = 1e-12
rng = np.random.default_rng(7)

def ground_state_correlation():
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    _, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj()

def modular_kernel_dense(C, region):
    C_A = C[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    return (U * np.log((1.0 - n_k) / n_k)) @ U.T

def parabola_correlation(h_A, region):
    """Pearson r between |h_{x,x+1}| and the interval parabola.
    h_A is region-local (indices 0..ell-1)."""
    ell = len(region)
    ks = np.arange(ell - 1)
    J = np.array([abs(h_A[k, k + 1]) for k in ks])
    p = (ks + 0.5) * (ell - 1 - ks + 0.5)   # centered parabola on bonds
    return float(np.corrcoef(J, p)[0, 1])

print("=" * 72)
print("PESCHEL/CFT PROFILE CHECK -- is the interval kernel the boost generator?")
print("=" * 72)
print()

C_vac = ground_state_correlation()
results = {}
for frac, tag in [(2, "L/2"), (4, "L/4")]:
    ell = L // frac
    x0 = (L - ell) // 2
    region = np.arange(x0, x0 + ell)
    h_A = modular_kernel_dense(C_vac, region)
    r = parabola_correlation(h_A, region)
    results[tag] = r
    print(f"vacuum, interval {tag} (sites {x0}..{x0 + ell - 1}):  "
          f"Pearson r = {r:.4f}   (predicted > 0.9)")

# Haar control
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
ell = L // 2
x0 = (L - ell) // 2
region = np.arange(x0, x0 + ell)
h_A = modular_kernel_dense(C_haar, region)
r_haar = parabola_correlation(h_A, region)
print(f"Haar state, interval L/2:                      "
      f"Pearson r = {r_haar:.4f}   (predicted < 0.5)")
print()

print("PASS / FAIL table:")
print("-" * 72)
checks = [
    ("P1: vacuum L/2 interval, r > 0.9", results["L/2"] > 0.9,
     f"{results['L/2']:.4f}"),
    ("P2: vacuum L/4 interval, r > 0.9", results["L/4"] > 0.9,
     f"{results['L/4']:.4f}"),
    ("P3: Haar control, r < 0.5", r_haar < 0.5, f"{r_haar:.4f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<44s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()

# -----------------------------------------------------------------------------
# EXPLORATORY (NOT pre-registered): why did P1/P2 fail?
# -----------------------------------------------------------------------------
# The failure is an operationalization error, diagnosed below and labeled
# exploratory -- none of this retroactively rescues the pre-registered check.
# Findings:
#   (a) The lattice kernel at half filling is STAGGERED: in the bulk,
#       h(mid, mid+r) vanishes for even r and alternates sign for odd r
#       (2k_F / particle-hole structure).  The nn channel is dominated by
#       this staggered part, whose magnitude SATURATES (~17.6) independently
#       of interval size -- it is not the CFT parabola and never was.
#   (b) The CFT parabola is the continuum ENVELOPE of the full kernel
#       (all ranges), not of any single channel.
#   (c) One clean universal number does emerge: the EDGE bond J(1) = pi
#       exactly, for every L and interval size tested -- the lattice image
#       of the linear boost weight near the entangling edge.
print("EXPLORATORY diagnostics (not pre-registered, no PASS/FAIL):")
print("-" * 72)
print(f"{'L':>5} {'ell':>5} {'J(1)/pi':>8} {'J_mid':>8} {'r_para':>7} "
      f"{'r_para full-range':>17}")
for Lx, ellx in [(400, 200), (800, 100), (800, 200), (1600, 400)]:
    h = np.zeros((Lx, Lx))
    for i in range(Lx - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    _, V = np.linalg.eigh(h)
    Cx = V[:, :Lx // 2] @ V[:, :Lx // 2].T
    reg = np.arange((Lx - ellx) // 2, (Lx - ellx) // 2 + ellx)
    hA = modular_kernel_dense(Cx, reg)
    J = np.array([abs(hA[k, k + 1]) for k in range(ellx - 1)])
    ks = np.arange(ellx - 1)
    p = (ks + 0.5) * (ellx - 1 - ks + 0.5)
    W = np.array([np.sum(np.abs(hA[k, :])) - abs(hA[k, k])
                  for k in range(ellx)])
    pw = (np.arange(ellx) + 0.5) * (ellx - np.arange(ellx) - 0.5)
    print(f"{Lx:>5} {ellx:>5} {J[0] / np.pi:8.3f} {J[ellx // 2]:8.3f} "
          f"{np.corrcoef(J, p)[0, 1]:7.4f} "
          f"{np.corrcoef(W, pw)[0, 1]:17.4f}")
print("-" * 72)
print("Round-8 nomination: pre-register the check against the EXACT lattice")
print("form (Eisler-Peschel, elliptic-function kernel) or the entanglement-")
print("spectrum spacing Delta_eps = pi^2/ln(ell) -- not the naive continuum")
print("parabola on the nn channel.  The edge slope J(1) = pi is a candidate")
print("sharp anchor, pending the same pre-registration discipline.")
