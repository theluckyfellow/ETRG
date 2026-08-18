#!/usr/bin/env python3
"""
Finite-size scaling of the modular-locality class separation (round 7, item 1).

The round-7 claim (ETRG-3_modular_locality_note.md) rests on a separation
measured at L = 80: geometric partitions have r_99 ~ 3, scrambled partitions
r_99 >= 17.  Existence proof is not evidence: if the separation does not GROW
with L, the principle is a finite-size artifact.

Prediction: for the critical vacuum, the geometric kernel's r_99 stays O(1)
(the modular Hamiltonian of an interval is quasi-local with fast-decaying
tails), while any scrambled partition's r_99 grows ~ L (its far couplings
span the system).  Class separation should therefore grow ~ linearly:
log-log slope ~ 1.

Regions are parameterized in L (the L = 80 run of modular_locality_check.py
hardcoded the two-interval block positions; that is fixed here).
"""

import numpy as np

clip = 1e-12
RANDOM_SEEDS = 3
MASTER_SEED = 7

# -----------------------------------------------------------------------------
# Helpers (same metrics as modular_locality_check.py)
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

def range_quantile(H, dist, q):
    W = np.abs(H) ** 2
    np.fill_diagonal(W, 0.0)
    total = W.sum()
    L = H.shape[0]
    pairs = [(dist[i, j], W[i, j]) for i in range(L) for j in range(i + 1, L)]
    pairs.sort(key=lambda p: p[0])
    acc = 0.0
    for d, w in pairs:
        acc += 2.0 * w
        if acc >= q * total:
            return float(d)
    return float(pairs[-1][0])

def make_regions(L, rng):
    """All regions have size L/2.  Two-interval: two quarter-size blocks
    centered at L/4 and 3L/4."""
    half = L // 2
    quarter = half // 2
    contiguous = np.arange((L - half) // 2, (L - half) // 2 + half)
    even_odd = np.arange(0, L, 2)
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - (quarter - quarter // 2),
                   3 * L // 4 - (quarter - quarter // 2) + (quarter - quarter // 2) * 2)
    two_interval = np.sort(np.concatenate([b1, b2]))
    assert len(two_interval) == half, \
        f"two-interval block arithmetic gave {len(two_interval)} != {half}"
    randoms = [np.sort(rng.choice(L, half, replace=False))
               for _ in range(RANDOM_SEEDS)]
    return contiguous, even_odd, two_interval, randoms

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def mi_matrix(C, L):
    """Mutual information I(i:j) between single sites, from 2x2 blocks."""
    I = np.zeros((L, L))
    s = binary_entropy(np.clip(np.diag(C).real, clip, 1.0 - clip))
    for i in range(L):
        for j in range(i + 1, L):
            lam = np.linalg.eigvalsh(C[np.ix_([i, j], [i, j])])
            I[i, j] = I[j, i] = max(s[i] + s[j] - np.sum(binary_entropy(lam)),
                                    0.0)
    return I

def alignment(H, d_MI, rng, scrambles=20):
    """K's 99% range in the MI metric vs randomly rotated same-spectrum
    kernels.  >> 1: aligned with the state's own correlation geometry."""
    L = H.shape[0]
    r_actual = range_quantile(H, d_MI, 0.99)
    evals, _ = np.linalg.eigh(H)
    r_rand = []
    for _ in range(scrambles):
        Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
        r_rand.append(range_quantile(Q @ np.diag(evals) @ Q.T, d_MI, 0.99))
    return float(np.mean(r_rand) / r_actual) if r_actual > 0 else 0.0

# -----------------------------------------------------------------------------
# Scaling sweep
# -----------------------------------------------------------------------------
L_values = [40, 80, 160, 320]

print("=" * 78)
print("FINITE-SIZE SCALING: modular-locality class separation vs L")
print("=" * 78)
print()
print("PART A: lattice-metric r_99 (the round-7 discriminator)")
print("-" * 78)
header = (f"{'L':>5s}  {'r99 cont':>9s}  {'r99 2int':>9s}  {'r99 e/o':>8s}  "
          f"{'r99 rand':>9s}  {'sep e/o':>8s}  {'sep rand':>9s}  "
          f"{'r999 c':>7s}  {'r999 2i':>8s}")
print(header)
print("-" * 78)

sep_eo = []
sep_rand = []
align_geo = []
align_scr = []
for L in L_values:
    rng = np.random.default_rng(MASTER_SEED)
    C = ground_state_correlation(L, L // 2)
    dist = np.abs(np.subtract.outer(np.arange(L), np.arange(L))).astype(float)
    contiguous, even_odd, two_interval, randoms = make_regions(L, rng)

    r99 = {}
    kernels = {}
    for name, region in ([("cont", contiguous), ("2int", two_interval),
                          ("e/o", even_odd)] +
                         [(f"rand{k}", r) for k, r in enumerate(randoms)]):
        H = modular_kernel(C, region, L)
        kernels[name] = H
        r99[name] = range_quantile(H, dist, 0.99)

    # r_99.9 tail column (referee §4: the tail-hierarchy retraction cited
    # numbers no committed script reproduced; they are now committed)
    r999_cont = range_quantile(kernels["cont"], dist, 0.999)
    r999_2int = range_quantile(kernels["2int"], dist, 0.999)

    geometric = max(r99["cont"], r99["2int"])
    sep_eo.append(r99["e/o"] / geometric)
    rand_min = min(r99[f"rand{k}"] for k in range(RANDOM_SEEDS))
    sep_rand.append(rand_min / geometric)
    print(f"{L:>5d}  {r99['cont']:9.1f}  {r99['2int']:9.1f}  {r99['e/o']:8.1f}  "
          f"{rand_min:9.1f}  {sep_eo[-1]:7.1f}x  {sep_rand[-1]:8.1f}x  "
          f"{r999_cont:7.1f}  {r999_2int:8.1f}")

    # PART B: bootstrap form -- alignment with the state's own MI metric
    I = mi_matrix(C, L)
    # Off-diagonal max only (referee §7: (I + eye).max() injected a 1.0
    # diagonal that won the max -- wrong normalization).
    I_max = I[np.triu_indices(L, k=1)].max()
    d_MI = -np.log(np.clip(I / I_max, clip, None))
    np.fill_diagonal(d_MI, 0.0)
    a_geo = min(alignment(kernels["cont"], d_MI, rng),
                alignment(kernels["2int"], d_MI, rng))
    a_scr = max([alignment(kernels["e/o"], d_MI, rng)] +
                [alignment(kernels[f"rand{k}"], d_MI, rng)
                 for k in range(RANDOM_SEEDS)])
    align_geo.append(a_geo)
    align_scr.append(a_scr)
print("-" * 78)
print()

slope_eo, _ = np.polyfit(np.log(L_values), np.log(sep_eo), 1)
slope_rand, _ = np.polyfit(np.log(L_values), np.log(sep_rand), 1)
print(f"Log-log slopes: separation(even/odd) ~ L^{slope_eo:.2f}   "
      f"separation(random) ~ L^{slope_rand:.2f}")
print()

print("PART B: bootstrap form -- MI-metric alignment vs L")
print("-" * 78)
print(f"{'L':>5s}  {'align geometric (min)':>21s}  {'align scrambled (max)':>21s}")
print("-" * 78)
for i, L in enumerate(L_values):
    print(f"{L:>5d}  {align_geo[i]:21.2f}  {align_scr[i]:21.2f}")
print("-" * 78)
slope_al, _ = np.polyfit(np.log(L_values),
                         np.log([g / s for g, s in zip(align_geo, align_scr)]), 1)
print(f"Log-log slope of alignment ratio (geo/scr) ~ L^{slope_al:.2f}")
print()

# -----------------------------------------------------------------------------
# PASS / FAIL adjudication
# -----------------------------------------------------------------------------
# NOTE (round-7, second pre-hardening correction): the lattice-metric r_99
# separation does NOT scale (slope ~ 0 for random scrambling; the critical
# chain's interval kernel has algebraic tails, so geometric r_99 itself grows
# slowly).  What survives scaling:
#   (a) maximal scrambling (even/odd) is caught with linearly growing
#       separation;
#   (b) the bootstrap (MI-metric) form is the candidate that must carry the
#       principle -- it separated random scrambling at L = 80 and is checked
#       for scaling here.
# The L = 80 tail hierarchy (r_99.9 singles out the interval) did NOT survive
# scaling and is retracted as a finite-size artifact.
print("PASS / FAIL table:")
print("-" * 70)
checks = [
    ("maximal scrambling caught with growing separation (slope > 0.5)",
     slope_eo > 0.5, f"slope {slope_eo:.2f}"),
    ("bootstrap alignment separates classes at all L (geo > 1.5x scr)",
     all(g > 1.5 * s for g, s in zip(align_geo, align_scr)),
     f"ratios {[f'{g / s:.1f}' for g, s in zip(align_geo, align_scr)]}"),
    ("bootstrap separation does not decay with L (slope > -0.1)",
     slope_al > -0.1, f"slope {slope_al:.2f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<56s}  {value}")
print("-" * 70)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
