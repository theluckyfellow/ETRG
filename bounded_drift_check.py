#!/usr/bin/env python3
"""
Bounded-generator drift variant (overnight-referee nomination 3) --
PRE-REGISTERED.

The weld's first number (drift_check.py) carries a regulator asterisk:
K = ln[(1-C)C^{-1}] is unbounded, and at L = 320, 82% of the contiguous
kernel's eigenvalues sit at the clip cap (referee F3).  But the drift's
leading-order content is eigenBASIS compatibility of C_A with h0 -- and C
is bounded in [0,1] with the SAME eigenvectors as K.  The bounded variant

    eta_C = ||[C_emb, h0]||_F / (||C_emb||_F * ||h0||_F)

tests the same compatibility with NO CLIP ANYWHERE.  If the separation
survives, the weld's number ships without the asterisk.

Protocol identical to drift_check.py (same regions, same L sweep, same
seed), computing eta for both generators.

PRE-REGISTERED PREDICTIONS:
  B1  eta_C separates contiguous from every scrambled rival by > 3x at
      L = 80.
  B2  the separation grows with L (slope > 0.3).
  B3  eta_C is clip-independent by construction (verified: no clip in the
      code path) and its separations are the same order as eta_K's
      (reported, not barred).
  B4  Haar-random state: eta_C(contiguous) NOT small (teeth).
"""

import numpy as np

clip = 1e-12
RANDOM_SEEDS = 3
MASTER_SEED = 7
L_values = [40, 80, 160, 320]

def ground_state_correlation(L, N):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    _, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj(), h

def modular_kernel(C, region):
    C_A = C[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    return (U * np.log((1.0 - n_k) / n_k)) @ U.T

def make_regions(L, rng):
    half = L // 2
    quarter = half // 2
    contiguous = np.arange((L - half) // 2, (L - half) // 2 + half)
    even_odd = np.arange(0, L, 2)
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - (quarter - quarter // 2),
                   3 * L // 4 - (quarter - quarter // 2) + (quarter - quarter // 2) * 2)
    two_interval = np.sort(np.concatenate([b1, b2]))
    assert len(two_interval) == half
    randoms = [np.sort(rng.choice(L, half, replace=False))
               for _ in range(RANDOM_SEEDS)]
    return contiguous, even_odd, two_interval, randoms

def drift_eta(C, h0, region, generator):
    L = h0.shape[0]
    if generator == "K":
        k_A = modular_kernel(C, region)
    else:  # bounded: the correlation matrix itself (same eigenvectors)
        k_A = C[np.ix_(region, region)]
    K_full = np.zeros((L, L))
    K_full[np.ix_(region, region)] = k_A
    comm = K_full @ h0 - h0 @ K_full
    norm = np.linalg.norm(K_full, 'fro') * np.linalg.norm(h0, 'fro')
    return float(np.linalg.norm(comm, 'fro') / norm)

print("=" * 78)
print("BOUNDED-GENERATOR DRIFT VARIANT -- the weld's number, asterisk-free")
print("=" * 78)
print()

seps_K, seps_C = [], []
for L in L_values:
    rng = np.random.default_rng(MASTER_SEED)
    C, h0 = ground_state_correlation(L, L // 2)
    contiguous, even_odd, two_interval, randoms = make_regions(L, rng)
    regions = [("contiguous", contiguous), ("two-interval", two_interval),
               ("even/odd", even_odd)] + \
              [(f"random #{k + 1}", r) for k, r in enumerate(randoms)]
    for gen in ["K", "C"]:
        etas = {name: drift_eta(C, h0, region, gen)
                for name, region in regions}
        rivals = [etas["even/odd"]] + [etas[f"random #{k + 1}"]
                                       for k in range(RANDOM_SEEDS)]
        sep = min(rivals) / etas["contiguous"]
        (seps_K if gen == "K" else seps_C).append(sep)
        if gen == "C":
            print(f"L={L:>4d} [{gen}]: eta(cont) = {etas['contiguous']:.5f}, "
                  f"best rival = {min(rivals):.5f}, separation = {sep:.1f}x")
print()

# Haar control at L = 80
L = 80
rng = np.random.default_rng(MASTER_SEED)
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
_, h0 = ground_state_correlation(L, L // 2)
contiguous, _, _, _ = make_regions(L, rng)
eta_haar = drift_eta(C_haar, h0, contiguous, "C")
eta_vac = None
rng = np.random.default_rng(MASTER_SEED)
C_vac, _ = ground_state_correlation(L, L // 2)
eta_vac = drift_eta(C_vac, h0, contiguous, "C")
print(f"Haar control (L=80, bounded): eta = {eta_haar:.5f} "
      f"(vacuum: {eta_vac:.5f})")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 78)
slope_C, _ = np.polyfit(np.log(L_values), np.log(seps_C), 1)
checks = [
    ("B1: bounded generator separates > 3x at L=80",
     seps_C[1] > 3.0, f"{seps_C[1]:.1f}x"),
    ("B2: separation grows with L (slope > 0.3)",
     slope_C > 0.3, f"slope {slope_C:.2f}, seps "
     f"{[f'{s:.1f}' for s in seps_C]}"),
    ("B3: bounded separations same order as K's",
     0.3 < seps_C[1] / seps_K[1] < 3.0,
     f"C {seps_C[1]:.1f}x vs K {seps_K[1]:.1f}x"),
    ("B4: Haar control NOT drift-free (> 3x vacuum)",
     eta_haar > 3 * eta_vac, f"{eta_haar:.5f} vs {eta_vac:.5f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("If B1-B2 pass: the weld's first number ships as eta_C -- same")
print("eigenbasis compatibility, no regulator anywhere, no asterisk.")
