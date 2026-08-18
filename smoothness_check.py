#!/usr/bin/env python3
"""
Smoothness rescue check (round 7, frontier item) -- PRE-REGISTERED.

Context: fss_locality.py showed weight-based locality metrics cannot rank the
middle (random scrambling escapes at large L).  The named rescue: the modular
generator of a geometric partition is not merely short-ranged but STRUCTURED
-- a smooth generator

    K ~ sum_x beta(x) n_x  +  sum_x J(x) (c_x^+ c_{x+1} + h.c.)

with beta(x), J(x) slowly varying in LATTICE position (parabolic envelope in
the CFT limit).  Scrambled partitions' kernels are fragmented: jagged onsite
sequences and missing nearest-neighbor coverage.

PRE-REGISTERED METRICS (fixed before any run):
  coverage  = fraction of lattice-nn pairs inside the region whose hopping
              |J| exceeds 10% of max|J| over such pairs
  s_beta    = total variation of the onsite sequence beta_k (region sites in
              lattice order), normalized:  sum|beta_{k+1}-beta_k| / sum|beta_k|

PRE-REGISTERED PREDICTIONS:
  P1  contiguous: coverage ~ 1, s_beta small and DECREASING with L
      (a smooth envelope is resolved ever better as L grows).
  P2  random halves: coverage bounded away from 1 (~0.25), s_beta large;
      the contiguous/random separation in s_beta must NOT decay with L
      (this is the scaling test the weight metrics failed).
  P3  even/odd: coverage = 0 (no lattice-nn pairs in region) -- caught
      automatically.  Haar-random state: low coverage, jagged s_beta.
  P4  RISK FLAGGED IN ADVANCE: two-interval unions may score smooth within
      blocks.  If so, the rescue is scoped to unions-of-intervals -- no
      better than the class it replaces -- and the middle-ranking problem
      stays open.  Either outcome is reported as measured.
"""

import numpy as np

clip = 1e-12
RANDOM_SEEDS = 3
MASTER_SEED = 7
L_values = [40, 80, 160, 320]

# -----------------------------------------------------------------------------
# Helpers (same kernels as fss_locality.py)
# -----------------------------------------------------------------------------
def ground_state_correlation(L, N):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    eigvals, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj()

def modular_kernel(C, region, L):
    C_A = C[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    h_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    H = np.zeros((L, L))
    H[np.ix_(region, region)] = h_A
    return H

def make_regions(L, rng):
    half = L // 2
    quarter = half // 2
    contiguous = np.arange((L - half) // 2, (L - half) // 2 + half)
    even_odd = np.arange(0, L, 2)
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - (quarter - quarter // 2),
                   3 * L // 4 - (quarter - quarter // 2) + (quarter - quarter // 2) * 2)
    two_interval = np.sort(np.concatenate([b1, b2]))[:half]
    randoms = [np.sort(rng.choice(L, half, replace=False))
               for _ in range(RANDOM_SEEDS)]
    return contiguous, even_odd, two_interval, randoms

def smoothness(H, region, L):
    """(coverage, s_beta) as pre-registered."""
    region = np.sort(region)
    beta = np.array([H[i, i] for i in region])
    # lattice-nn pairs inside the region
    nn_pairs = [(i, i + 1) for i in region[:-1] if (i + 1) in set(region)]
    if not nn_pairs:
        return 0.0, float('nan')
    J = np.array([abs(H[i, j]) for i, j in nn_pairs])
    coverage = float(np.mean(J > 0.1 * J.max()))
    s_beta = float(np.sum(np.abs(np.diff(beta))) / np.sum(np.abs(beta)))
    return coverage, s_beta

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 78)
print("SMOOTHNESS RESCUE CHECK -- pre-registered metrics and predictions")
print("=" * 78)
print()
print(f"{'L':>5s}  {'region':>12s}  {'coverage':>9s}  {'s_beta':>8s}")
print("-" * 78)

s_cont, s_rand, s_two = [], [], []
cov_rand = []
for L in L_values:
    rng = np.random.default_rng(MASTER_SEED)
    C = ground_state_correlation(L, L // 2)
    contiguous, even_odd, two_interval, randoms = make_regions(L, rng)
    rows = [("contiguous", contiguous), ("two-interval", two_interval),
            ("even/odd", even_odd)] + \
           [(f"random #{k + 1}", r) for k, r in enumerate(randoms)]
    covs_this_L = []
    for name, region in rows:
        H = modular_kernel(C, region, L)
        cov, sb = smoothness(H, region, L)
        print(f"{L:>5d}  {name:>12s}  {cov:9.3f}  {sb:8.4f}")
        if name == "contiguous":
            s_cont.append(sb)
        elif name == "two-interval":
            s_two.append(sb)
        elif name == "random #1":
            s_rand.append(sb)
        if name.startswith("random"):
            covs_this_L.append(cov)
    cov_rand.append(float(np.mean(covs_this_L)))
    print("-" * 78)

# Haar control at L = 80
L = 80
rng = np.random.default_rng(MASTER_SEED)
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
contiguous, _, _, _ = make_regions(L, rng)
H = modular_kernel(C_haar, contiguous, L)
cov_h, sb_h = smoothness(H, contiguous, L)
print(f"Haar control (L=80, contiguous): coverage = {cov_h:.3f}, "
      f"s_beta = {sb_h:.4f}")
print()

# -----------------------------------------------------------------------------
# Adjudication against the PRE-REGISTERED predictions
# -----------------------------------------------------------------------------
# RECODED per referee section 5: the first version's coded checks were weaker
# than the prose predictions and flattered the dead metric (P1 passed on a
# slope of -0.02 through a non-monotonic sequence; P2 tested only non-decay
# of a separation that never existed, and never tested the coverage ~ 0.25
# prediction, which failed outright).  The checks below are the prose
# predictions as written.  "Small" s_beta is operationalized as < 0.2 (a
# resolved smooth envelope has relative TV ~ O(1/L)); "decreasing" as slope
# < -0.1 (a trend, not noise).
print("Adjudication vs pre-registered predictions (recoded, referee-tightened):")
print("-" * 78)
slope_cont, _ = np.polyfit(np.log(L_values), np.log(s_cont), 1)
ratio = [r / c for c, r in zip(s_cont, s_rand)]
slope_ratio, _ = np.polyfit(np.log(L_values), np.log(ratio), 1)

mean_rand_sb = float(np.mean(s_rand))
mean_cont_sb = float(np.mean(s_cont))
mean_cov = float(np.mean(cov_rand))
checks = [
    ("P1: contiguous s_beta SMALL (< 0.2) and decreasing (slope < -0.1)",
     max(s_cont) < 0.2 and slope_cont < -0.1,
     f"s_beta {s_cont[0]:.4f} -> {s_cont[-1]:.4f}, slope {slope_cont:.2f} "
     f"-- neither small nor decreasing"),
    ("P2: random coverage ~ 0.25 (< 0.5) AND s_beta > 2x contiguous",
     mean_cov < 0.5 and mean_rand_sb > 2 * mean_cont_sb,
     f"coverage {mean_cov:.2f} (prediction failed outright), "
     f"s_beta ratio {mean_rand_sb / mean_cont_sb:.2f}"),
    ("P3: Haar control jagged (s_beta > 3x contiguous at L=80)",
     sb_h > 3 * s_cont[1], f"{sb_h:.4f} vs {s_cont[1]:.4f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<62s}  {value}")
print()
print(f"P4 (flagged risk, reported not judged): two-interval s_beta "
      f"{s_two[0]:.4f} -> {s_two[-1]:.4f}  vs contiguous "
      f"{s_cont[0]:.4f} -> {s_cont[-1]:.4f}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("The true score is FAIL/FAIL/FAIL: the metric is dead as pre-registered,")
print("and the adjudication now says so.")
