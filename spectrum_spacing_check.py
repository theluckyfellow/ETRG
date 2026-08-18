#!/usr/bin/env python3
"""
Exact-lattice weld check (round 8): the entanglement-spectrum spacing --
PRE-REGISTERED.

The weld conjecture's anchor is Bisognano-Wichmann, whose lattice image is
Peschel's exact result for a segment of a critical hopping chain: the
single-particle entanglement levels xi_k = ln((1-n_k)/n_k) of an interval
are EQUALLY SPACED, with spacing

    Delta_xi = pi^2 / ln(ell)      (large ell, up to an O(1) constant
                                    inside the logarithm)

This is a LATTICE theorem, not a continuum approximation -- the correct
target after the nn-parabola check failed as operationalized
(peschel_profile_check.py).  A measured equal spacing with the predicted
scaling converts the weld's anchor from citation to measurement.

Protocol notes: interval ell << L (avoids the finite-complement distortion
found in the profile check); half filling (particle-hole gives xi <-> -xi
symmetry); central levels only (the spacing is uniform in the bunch around
xi = 0; extreme levels deviate).

PRE-REGISTERED PREDICTIONS:
  P1  uniformity: for each ell, the central 6 spacings have
      std/mean < 0.15.
  P2  scaling: Delta_xi * ln(ell) is constant across ell = 100..800
      within a 20% band.
  P3  magnitude: that constant is pi^2 within 30% (the O(1) additive
      constant inside ln(ell) makes this approximate -- bar set honestly).
  P4  Haar-random state: central spacings NOT uniform (std/mean > 0.3).
"""

import numpy as np

clip = 1e-12
L = 3200
N = L // 2
ELL_VALUES = [100, 200, 400, 800]
N_CENTRAL = 7                      # central levels -> 6 spacings

def ground_state_correlation():
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    _, V = np.linalg.eigh(h)
    occ = V[:, :N]
    return occ @ occ.T.conj()

def entanglement_spectrum(C, region):
    C_A = C[np.ix_(region, region)]
    n_k = np.linalg.eigvalsh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    return np.sort(np.log((1.0 - n_k) / n_k))

def central_spacings(xi):
    mid = len(xi) // 2
    bunch = xi[mid - N_CENTRAL // 2: mid + N_CENTRAL // 2 + 1]
    return np.diff(bunch)

print("=" * 72)
print("EXACT-LATTICE WELD CHECK: entanglement-spectrum spacing")
print("=" * 72)
print()
print(f"Chain L = {L}, half filling; intervals ell << L, centered")
print()
print(f"{'ell':>6s}  {'mean d_xi':>10s}  {'std/mean':>9s}  {'d_xi*ln(ell)':>13s}")
print("-" * 72)

C = ground_state_correlation()
products = []
uniformities = []
for ell in ELL_VALUES:
    x0 = (L - ell) // 2
    region = np.arange(x0, x0 + ell)
    xi = entanglement_spectrum(C, region)
    sp = central_spacings(xi)
    mean_sp = float(np.mean(sp))
    unif = float(np.std(sp) / mean_sp)
    prod = mean_sp * np.log(ell)
    products.append(prod)
    uniformities.append(unif)
    print(f"{ell:>6d}  {mean_sp:10.5f}  {unif:9.4f}  {prod:13.4f}")
print("-" * 72)
print(f"pi^2 = {np.pi**2:.4f}")
print()

# Haar control, ell = 200
rng = np.random.default_rng(7)
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
x0 = (L - 200) // 2
region = np.arange(x0, x0 + 200)
xi_h = entanglement_spectrum(C_haar, region)
sp_h = central_spacings(xi_h)
unif_h = float(np.std(sp_h) / np.mean(sp_h))
print(f"Haar control (ell=200): std/mean = {unif_h:.4f} "
      f"(vacuum: {uniformities[1]:.4f})")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
prod_arr = np.array(products)
band = (prod_arr.max() - prod_arr.min()) / prod_arr.mean()
mean_prod = float(prod_arr.mean())
checks = [
    ("P1: central spacings uniform (all std/mean < 0.15)",
     all(u < 0.15 for u in uniformities),
     f"{[f'{u:.3f}' for u in uniformities]}"),
    ("P2: d_xi*ln(ell) constant within 20% band",
     band < 0.20, f"band {band * 100:.1f}%"),
    ("P3: constant = pi^2 within 30%",
     abs(mean_prod - np.pi**2) / np.pi**2 < 0.30,
     f"{mean_prod:.3f} vs {np.pi**2:.3f}"),
    ("P4: Haar spacings NOT uniform (std/mean > 0.3)",
     unif_h > 0.3, f"{unif_h:.3f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
