#!/usr/bin/env python3
"""
Pinch geometry check (ETRG-5 toy, exploratory) -- the cone collapsing.

A free-fermion chain whose hopping t(x) passes smoothly through zero at
the center: the local "speed of causality" collapses to a near stop, the
lattice image of a lapse degeneracy / stasis point.  The stasis-cosmology
note (ETRG-5) asks what the entanglement structure does there:

  (a) the MI-geometry distance across the degeneracy diverges relative to
      a uniform chain (the pinch: causality stops);
  (b) the two sides' internal geometries become those of independent
      chains (two new causal domains, each with a NEW EDGE born at the
      degeneracy);
  (c) the entanglement spectrum develops near-zero modes localized at the
      degeneracy (horizon modes -- the modular shadow of the stasis).

Exploratory: no theorem at stake.  Controls: uniform chain; a chain with
a hard cut (t = 0 exactly on one bond) as the infinite-stasis limit.
"""

import numpy as np

L = 201
I0 = L // 2
W = 8.0                      # width of the pinch
FILL = 2 * L // 5
clip = 1e-12

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def chain(t_profile):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5 * t_profile(i)
    return h

def ground_state_correlation(h):
    _, V = np.linalg.eigh(h)
    occ = V[:, :FILL]
    return occ @ occ.T.conj()

def mi(C, i, j):
    s_i = binary_entropy(C[i, i].real)
    s_j = binary_entropy(C[j, j].real)
    s_ij = np.sum(binary_entropy(np.linalg.eigvalsh(C[np.ix_([i, j], [i, j])])))
    return max(s_i + s_j - s_ij, 0.0)

def bond_distances(C):
    """MI-metric nearest-neighbor bond lengths across the chain."""
    d = []
    for i in range(L - 1):
        v = mi(C, i, i + 1)
        d.append(-np.log(max(v, clip)))
    return np.array(d)

def S_of(C, sites):
    return float(np.sum(binary_entropy(
        np.linalg.eigvalsh(C[np.ix_(sites, sites)]))))

# -----------------------------------------------------------------------------
# Three chains: uniform, pinched, cut
# -----------------------------------------------------------------------------
profiles = {
    "uniform": lambda i: 1.0,
    "pinched": lambda i: np.tanh((i - I0) / W) ** 2,
    "cut": lambda i: 0.0 if i == I0 else 1.0,
}

print("=" * 72)
print("PINCH GEOMETRY CHECK -- the cone collapsing (ETRG-5 toy)")
print("=" * 72)
print()

results = {}
for name, tp in profiles.items():
    C = ground_state_correlation(chain(tp))
    d = bond_distances(C)
    # (a) pinch: bond length at the center vs the bulk median
    pinch_ratio = d[I0] / np.median(d)
    # (b) independence: MI between the two sides (sites I0-20 and I0+20)
    cross_mi = mi(C, I0 - 20, I0 + 20)
    # (c) entanglement spectrum of the central window (21 sites)
    window = np.arange(I0 - 10, I0 + 11)
    C_A = C[np.ix_(window, window)]
    n_k = np.sort(np.linalg.eigvalsh(C_A))
    # near-zero modes: eigenvalues within 1e-3 of 0 or 1 (frozen/edge)
    n_edge = int(np.sum((n_k < 1e-3) | (n_k > 1 - 1e-3)))
    # entropy of left half vs sum of parts (additivity = independence)
    left = np.arange(0, I0)
    right = np.arange(I0 + 1, L)
    S_left = S_of(C, left)
    S_right = S_of(C, right)
    S_all = S_of(C, np.arange(L))
    mutual = S_left + S_right - S_all
    results[name] = (pinch_ratio, cross_mi, n_edge, mutual)
    print(f"{name:>8s}:  center/bulk bond ratio = {pinch_ratio:8.2f}   "
          f"cross-MI(I0-20:I0+20) = {cross_mi:.2e}   "
          f"edge modes = {n_edge:2d}   I(left:right) = {mutual:.4f}")

print()
print("Reading:")
print("  (a) pinch_ratio >> 1: MI distance across the degeneracy diverges")
print("  (b) cross-MI -> 0 and I(left:right) -> 0: two independent domains")
print("  (c) edge modes > uniform: new frozen degrees of freedom at the")
print("      degeneracy (horizon modes)")
print()

# -----------------------------------------------------------------------------
# Adjudication (exploratory -- expectations, not theorems)
# -----------------------------------------------------------------------------
p = results["pinched"]
u = results["uniform"]
c = results["cut"]
checks = [
    ("(a) pinch: center bond anomalously long (> 2x uniform)",
     p[0] > 2 * u[0], f"{p[0]:.1f} vs uniform {u[0]:.1f}"),
    ("(b) pinch: cross-MI strongly suppressed (< 0.1x uniform)",
     p[1] < 0.1 * u[1], f"{p[1]:.2e} vs {u[1]:.2e}"),
    ("(b') pinch: left/right MI suppressed toward the cut limit",
     p[3] < 0.5 * u[3], f"{p[3]:.3f} vs uniform {u[3]:.3f}, cut {c[3]:.3f}"),
    ("(c) pinch: more edge modes than uniform",
     p[2] > u[2], f"{p[2]} vs {u[2]} (cut: {c[2]})"),
]
print("PASS / FAIL table (exploratory expectations):")
print("-" * 72)
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(x[1] for x in checks) else 'FAIL'}")
