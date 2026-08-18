#!/usr/bin/env python3
"""
Drift across factorizations (round 9) -- PRE-REGISTERED.

The weld's discriminating number is the drift commutator eta = ||[K, h0]||
(region level, site factorization).  The toehold result is factorization-
level: bootstrap locality ranks F_site first.  Do the two weld together?
For each factorization F, take its natural region (Fiedler first half of
its own MI graph), build the region's modular kernel, embed it in the full
space, transform back to the SITE frame (physics lives there), and compute
the drift commutator with the physical Hamiltonian h0.

If the site factorization also MINIMIZES the drift commutator, the two
independent discriminators (bootstrap locality and dynamical consistency)
select the same factorization -- the weld closes over the hard kernel.

Menu: F_site, near-local rivals (eps = 0.3, bandwidth 2, 3 seeds),
F_rand (generic orthogonal).  F_mom is degenerate (no region structure).

PRE-REGISTERED PREDICTIONS:
  P1  eta(F_site) is the smallest of the menu, by > 1.5x over the best
      rival.
  P2  Haar-random state: eta(F_site) NOT smallest / not small (teeth).
"""

import numpy as np

L = 60
N = L // 2
clip = 1e-12
SEEDS = 3
EPS = 0.3
rng = np.random.default_rng(7)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def chain(L):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    return h

def ground_state_correlation(h):
    _, V = np.linalg.eigh(h)
    occ = V[:, :N]
    return occ @ occ.T.conj()

def mi_matrix(C):
    I = np.zeros((L, L))
    s = binary_entropy(np.clip(np.diag(C).real, clip, 1.0 - clip))
    for i in range(L):
        for j in range(i + 1, L):
            lam = np.linalg.eigvalsh(C[np.ix_([i, j], [i, j])])
            I[i, j] = I[j, i] = max(s[i] + s[j] - np.sum(binary_entropy(lam)),
                                    0.0)
    return I

def fiedler_order(I):
    W = I.copy()
    np.fill_diagonal(W, 0.0)
    Lap = np.diag(W.sum(axis=1)) - W
    _, evecs = np.linalg.eigh(Lap)
    return np.argsort(evecs[:, 1])

def near_local_rotation(eps, seed):
    rl = np.random.default_rng(seed)
    A = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, min(i + 3, L)):
            A[i, j] = rl.standard_normal()
    A = A - A.T
    evals, evecs = np.linalg.eig(1j * A)
    return np.real(evecs @ np.diag(np.exp(-1j * eps * evals))
                   @ evecs.conj().T)

def drift_eta(O_F, C, h0):
    """Drift commutator of the factorization's natural region, computed in
    the site frame."""
    C_F = O_F.T @ C @ O_F
    I = mi_matrix(C_F)
    order = fiedler_order(I)
    region = np.sort(order[:L // 2])
    C_A = C_F[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    h_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    # embed in the factorization's full space, transform to the site frame
    K_F = np.zeros((L, L))
    K_F[np.ix_(region, region)] = h_A
    K_site = O_F @ K_F @ O_F.T
    comm = K_site @ h0 - h0 @ K_site
    return float(np.linalg.norm(comm, 'fro')
                 / (np.linalg.norm(K_site, 'fro') * np.linalg.norm(h0, 'fro')))

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
h0 = chain(L)
C = ground_state_correlation(h0)

print("=" * 72)
print("DRIFT ACROSS FACTORIZATIONS -- does [K, h0] rank F_site first?")
print("=" * 72)
print()

menu = [("F_site", np.eye(L))]
menu += [(f"near-local #{s}", near_local_rotation(EPS, 4000 + s))
         for s in range(SEEDS)]
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
menu += [("F_rand", Q)]

etas = {}
for tag, O in menu:
    etas[tag] = drift_eta(O, C, h0)
    print(f"  {tag:>14s}  eta = {etas[tag]:.5f}")
print()

# Haar control
Q2, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q2 @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q2.T
eta_haar = drift_eta(np.eye(L), C_haar, h0)
print(f"Haar state, F_site: eta = {eta_haar:.5f} "
      f"(vacuum F_site: {etas['F_site']:.5f})")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
rivals = [v for k, v in etas.items() if k != "F_site"]
best = min(rivals)
checks = [
    ("P1: eta(F_site) smallest by > 1.5x",
     best / etas["F_site"] > 1.5,
     f"site {etas['F_site']:.5f} vs best rival {best:.5f} "
     f"({best / etas['F_site']:.1f}x)"),
    ("P2: Haar control NOT drift-free (> 3x vacuum)",
     eta_haar > 3 * etas["F_site"],
     f"{eta_haar:.5f} vs {etas['F_site']:.5f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<44s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
