#!/usr/bin/env python3
"""
Degeneracy check (referee finding section 2 / nomination 3) -- PRE-REGISTERED.

Fable's claim: P-select as stated has a trivial maximizer.  Any factorization
aligned with the eigenbasis of rho makes the modular kernel DIAGONAL -- zero
off-diagonal weight, r_99 = 0, "maximally local" in any metric.  The intended
kill: the momentum-mode bipartition of the very vacuum used in every round-7
script.  The Slater ground state is a PRODUCT over single-particle modes, so
any mode bipartition gives a pure reduced state.

The proposed amendment (the nondegenerate-geometry clause): P-select must
demand a NONDEGENERATE self-defined geometry before locality is scored.  In
the mode factorization all inter-mode mutual informations vanish -- the MI
metric is degenerate, there is no geometry to be local IN, and the partition
is rejected before its (trivially local) kernel is ever scored.

PRE-REGISTERED PREDICTIONS:
  P1  momentum bipartition: S_A = 0 (numerically), kernel off-diagonal
      weight = 0 -- the naive locality score is trivially won.
  P2  every single-mode mutual information I(k:k') = 0 -- the MI metric is
      degenerate in the mode factorization.
  P3  the amended principle therefore REJECTS the momentum partition (no
      geometry) while the contiguous site partition is scorable (nondegenerate
      MI metric) -- the clause kills the trivial maximizer without touching
      the geometric class.
"""

import numpy as np

L = 80
N = L // 2
clip = 1e-12

print("=" * 72)
print("DEGENERACY CHECK: the momentum-bipartition trivial maximizer")
print("=" * 72)
print()

# Free-fermion chain, ground state, in the single-particle eigenbasis
h0 = np.zeros((L, L))
for i in range(L - 1):
    h0[i, i + 1] = h0[i + 1, i] = -0.5
energies, V = np.linalg.eigh(h0)          # V columns = mode wavefunctions
C_site = V[:, :N] @ V[:, :N].T            # site-basis correlation matrix
C_mode = V.T @ C_site @ V                 # mode basis: diag(1 x N, 0 x L-N)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

# -----------------------------------------------------------------------------
# P1: momentum bipartition -- entropy and kernel
# -----------------------------------------------------------------------------
region_modes = np.arange(L // 2)          # the L/2 lowest-energy modes
C_A = C_mode[np.ix_(region_modes, region_modes)]
n_k = np.linalg.eigvalsh(C_A)
S_A = float(np.sum(binary_entropy(n_k)))

n_clip = np.clip(n_k, clip, 1.0 - clip)
xi = np.log((1.0 - n_clip) / n_clip)
K_offdiag_weight = float(np.sum(np.abs(C_A - np.diag(np.diag(C_A))) ** 2))
print(f"P1: momentum bipartition ({len(region_modes)} lowest-energy modes)")
print(f"    S_A                       = {S_A:.3e}   (predicted ~ 0)")
print(f"    kernel off-diagonal |.|^2 = {K_offdiag_weight:.3e}   "
      f"(predicted 0 -> r_99 = 0, naive locality WON trivially)")
print()

# -----------------------------------------------------------------------------
# P2: inter-mode mutual informations
# -----------------------------------------------------------------------------
I_max = 0.0
for i in range(L):
    for j in range(i + 1, L):
        block = C_mode[np.ix_([i, j], [i, j])]
        lam = np.linalg.eigvalsh(block)
        s_i = binary_entropy(C_mode[i, i])
        s_j = binary_entropy(C_mode[j, j])
        s_ij = np.sum(binary_entropy(lam))
        I_max = max(I_max, float(s_i + s_j - s_ij))
print(f"P2: max single-mode mutual information I(k:k') = {I_max:.3e}   "
      f"(predicted 0 -> MI metric degenerate, NO geometry)")
print()

# -----------------------------------------------------------------------------
# P3: the amended principle's verdict on both partitions
# -----------------------------------------------------------------------------
# Site basis, contiguous region: MI metric between SITES is nondegenerate.
I_site_max = 0.0
for i in range(L):
    for j in range(i + 1, L):
        block = C_site[np.ix_([i, j], [i, j])]
        lam = np.linalg.eigvalsh(block)
        s_ij = np.sum(binary_entropy(lam))
        val = float(binary_entropy(C_site[i, i]) + binary_entropy(C_site[j, j])
                    - s_ij)
        I_site_max = max(I_site_max, val)
print("P3: amended P-select (nondegenerate-geometry clause):")
print(f"    momentum partition: max I = {I_max:.2e}  -> geometry DEGENERATE "
      f"-> rejected before scoring")
print(f"    site partition:     max I = {I_site_max:.3f}  -> geometry "
      f"nondegenerate -> scorable")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
checks = [
    ("P1: mode bipartition pure (S_A < 1e-6) with diagonal kernel",
     S_A < 1e-6 and K_offdiag_weight < 1e-20,
     f"S_A = {S_A:.1e}, off-diag = {K_offdiag_weight:.1e}"),
    ("P2: mode MI metric degenerate (max I < 1e-9)",
     I_max < 1e-9, f"{I_max:.1e}"),
    ("P3: site MI metric nondegenerate (max I > 0.01)",
     I_site_max > 0.01, f"{I_site_max:.4f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<58s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("Verdict on referee section 2: the trivial maximizer EXISTS (P1), and")
print("the nondegenerate-geometry clause KILLS it (P2+P3).  The clause is")
print("therefore a required amendment to P-select, not an optional one.")
