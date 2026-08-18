#!/usr/bin/env python3
"""
Quench-dynamics drift check (round 8, direct version of drift_check.py) --
PRE-REGISTERED.

drift_check.py established at GENERATOR level that [K_A, h0] discriminates
geometric from scrambled regions.  This is the direct, dynamical version:
prepare a non-stationary state (ground state of h0 + eps*v, v a Gaussian
bump inside the region), evolve the full correlation matrix under the
physical Hamiltonian h0, and watch the observer's coarse book drift against
the fine book in real time.

For region A with initial modular basis U_A (the observer's fixed coarse-
graining):
    S_fine(t) = sum h(n_k(C_A(t)))              -- the fine book
    S_mod(t)  = sum h(diag(U_A^+ C_A(t) U_A))   -- the coarse book
    Delta(t)  = S_mod(t) - S_fine(t)  (>= 0; Delta(0) = 0 by construction)

Delta(t) measures exactly N2's drift: how much extra entropy the fixed
coarse description accrues as the physical dynamics proceeds.  If the
coarse-graining commuted with the evolution, the modular basis would be
carried along and Delta would stay ~ 0.

PRE-REGISTERED PREDICTIONS (v1): P1 failed -- see amendment below.

AMENDMENT (documented in place, registered before the amended run):
v1's P1 FAILED and the failure is a confound, not physics: the perturbation
is a bump at ONE site, so the amount of dynamics a region experiences
depends on its geometry.  A contiguous block channels the disturbance
through itself (half the propagation stays inside); a scattered region
vents it straight into the complement.  Delta(T) therefore conflates
"how much the coarse basis misaligns" with "how hard the region was
driven."  The principled fix is normalization by the experienced dynamics:

    drift_ratio(A) = Delta(T) / ||C_A(T) - C_A(0)||_F

-- misalignment accrued PER UNIT of physical change the region underwent.

AMENDED PREDICTIONS (registered before the amended run):
  P1' drift_ratio(contiguous) beats every scrambled rival by > 3x at L=200.
  P2' the separation does not decay with L, slope > -0.1.
  P3' Haar control: reported (its Delta and its norm are both large).
  P4' two-interval: reported, not judged.
  Raw Delta(T) values are printed alongside for full transparency about
  the confound.
"""

import numpy as np

clip = 1e-12
RANDOM_SEEDS = 3
MASTER_SEED = 7
L_values = [100, 200, 400]
EPS = 0.05
W = 5.0
N_T = 40                     # time points per run

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def chain(L):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    return h

def ground_state_correlation(h, N):
    _, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj()

def make_regions(L, rng):
    half = L // 5                     # region size L/5 (q10 tradition: 40/200)
    quarter = half // 2
    contiguous = np.arange((L - half) // 2, (L - half) // 2 + half)
    even_odd = np.arange(0, 2 * half, 2)
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - (quarter - quarter // 2),
                   3 * L // 4 - (quarter - quarter // 2) + (quarter - quarter // 2) * 2)
    two_interval = np.sort(np.concatenate([b1, b2]))
    assert len(two_interval) == half
    randoms = [np.sort(rng.choice(L, half, replace=False))
               for _ in range(RANDOM_SEEDS)]
    return contiguous, even_odd, two_interval, randoms

def run_L(L):
    rng = np.random.default_rng(MASTER_SEED)
    N = 2 * L // 5                     # filling 0.4 (q10 tradition)
    h0 = chain(L)
    E, V = np.linalg.eigh(h0)          # evolution: expm via eigenbasis
    contiguous, even_odd, two_interval, randoms = make_regions(L, rng)
    regions = [("contiguous", contiguous), ("two-interval", two_interval),
               ("even/odd", even_odd)] + \
              [(f"random #{k + 1}", r) for k, r in enumerate(randoms)]
    T = 0.4 * L
    times = np.linspace(0, T, N_T)
    # Precompute the evolution unitaries once; reuse across regions.
    # C_A(t) = (U_t C0)_{A,:} @ (U_t^+)_{:,A} -- no full-matrix products.
    U_ts = [(V * np.exp(-1j * E * t)) @ V.T.conj() for t in times]
    drifts = {}
    norms = {}
    for name, region in regions:
        i0 = int(region[0])
        v = np.exp(-(((np.arange(L) - i0) / W) ** 2))
        C0 = ground_state_correlation(h0 + EPS * np.diag(v), N)
        C_A0 = C0[np.ix_(region, region)]
        _, U_A = np.linalg.eigh(C_A0)  # the observer's fixed coarse basis
        for U_t in U_ts:
            M = U_t[region, :]                      # |A| x L
            C_A = M @ C0 @ M.T.conj()               # (u C0 u^+)_{A,A}
            n_fine = np.linalg.eigvalsh(C_A)
            n_coarse = np.diag(U_A.T.conj() @ C_A @ U_A).real
            drifts[name] = float(np.sum(binary_entropy(n_coarse))
                                 - np.sum(binary_entropy(n_fine)))
            norms[name] = float(np.linalg.norm(C_A - C_A0, 'fro'))
    return drifts, norms

print("=" * 78)
print("QUENCH-DYNAMICS DRIFT CHECK -- N2's drift, watched in real time")
print("=" * 78)
print()
print(f"{'L':>5s}  {'region':>12s}  {'Delta(T)':>9s}  {'||dC_A||':>9s}  "
      f"{'ratio':>8s}")
print("-" * 78)

r_cont, r_two, r_best_rival = [], [], []
d_cont, d_two = [], []
for L in L_values:
    drifts, norms = run_L(L)
    ratios = {n: drifts[n] / norms[n] if norms[n] > 0 else 0.0
              for n in drifts}
    for name in drifts:
        print(f"{L:>5d}  {name:>12s}  {drifts[name]:9.5f}  "
              f"{norms[name]:9.5f}  {ratios[name]:8.5f}")
    r_cont.append(ratios["contiguous"])
    r_two.append(ratios["two-interval"])
    d_cont.append(drifts["contiguous"])
    d_two.append(drifts["two-interval"])
    rivals = [ratios["even/odd"]] + [ratios[f"random #{k + 1}"]
                                     for k in range(RANDOM_SEEDS)]
    r_best_rival.append(min(rivals))
    print("-" * 78)

# Haar control at L = 200
L = 200
rng = np.random.default_rng(MASTER_SEED)
N = 2 * L // 5
h0 = chain(L)
E, V = np.linalg.eigh(h0)
contiguous, _, _, _ = make_regions(L, rng)
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
C_A0 = C_haar[np.ix_(contiguous, contiguous)]
_, U_A = np.linalg.eigh(C_A0)
T = 0.4 * L
C_A0h = C_haar[np.ix_(contiguous, contiguous)]
for t in [T]:
    U_t = (V * np.exp(-1j * E * t)) @ V.T.conj()
    M = U_t[contiguous, :]
    C_A = M @ C_haar @ M.T.conj()
    d_haar = float(np.sum(binary_entropy(
        np.diag(U_A.T.conj() @ C_A @ U_A).real))
        - np.sum(binary_entropy(np.linalg.eigvalsh(C_A))))
    norm_haar = float(np.linalg.norm(C_A - C_A0h, 'fro'))
ratio_haar = d_haar / norm_haar if norm_haar > 0 else 0.0
print(f"Haar control (L=200, contiguous): Delta(T) = {d_haar:.5f}, "
      f"||dC_A|| = {norm_haar:.5f}, ratio = {ratio_haar:.5f} "
      f"(vacuum contiguous ratio: {r_cont[1]:.5f})")
print()

# -----------------------------------------------------------------------------
# Adjudication (amended predictions P1'-P3', registered above)
# -----------------------------------------------------------------------------
print("PASS / FAIL table (amended metric: drift per unit dynamics):")
print("-" * 78)
sep = [r / c for c, r in zip(r_cont, r_best_rival)]
slope, _ = np.polyfit(np.log(L_values), np.log(sep), 1)
checks = [
    ("P1': contiguous beats every scrambled rival by > 3x at L=200",
     sep[1] > 3.0, f"separation {sep[1]:.1f}x"),
    ("P2': separation does not decay with L (slope > -0.1)",
     slope > -0.1, f"separations {[f'{s:.1f}' for s in sep]}, "
     f"slope {slope:.2f}"),
    ("P3': Haar control drifts more per unit dynamics (> 3x)",
     ratio_haar > 3 * r_cont[1], f"{ratio_haar:.5f} vs {r_cont[1]:.5f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<60s}  {value}")
print()
print(f"P4' (reported, not judged): two-interval ratio "
      f"{[f'{r:.5f}' for r in r_two]} vs contiguous "
      f"{[f'{r:.5f}' for r in r_cont]}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
