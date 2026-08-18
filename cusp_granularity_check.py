#!/usr/bin/env python3
"""
Cusp granularity check (overnight-referee nomination 2) -- PRE-REGISTERED.

The toehold's extremum is cusp-shaped (margin ~ eps^0.34, overnight
referee's small-eps control).  Prime suspect: the alignment score's r_99
quantile is DISCRETE-VALUED (it jumps between values of the finite
MI-distance spectrum), so "smoothness" was never available to it.  This
check re-scores the eps-sweep with a CONTINUOUS locality functional --
the |H|^2-weighted mean MI-distance, which takes continuous values -- and
asks whether the cusp survives.

PRE-REGISTERED PREDICTIONS:
  C1  F_site still wins at every eps (selection robust to the functional
      change).
  C2  margin shape: fit margin(eps) ~ eps^alpha.  alpha ~ 2 -> smooth
      extremum (the cusp was quantile granularity); alpha < 1 -> the
      cusp is physics.  Reported with the fit; barred as alpha > 1.2 OR
      alpha < 0.8 (i.e., one of the two readings must win clearly).
  C3  Haar-random state: alignment < 3 (teeth, same bar as the killer
      test).
"""

import numpy as np

L = 60
N = L // 2
clip = 1e-12
SCRAMBLES = 20
SEEDS = 5
EPS_VALUES = [0.01, 0.03, 0.1, 0.3, 0.5]
rng = np.random.default_rng(7)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def ground_state_correlation():
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
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

def mean_mi_range(H, d_MI):
    """CONTINUOUS locality functional: |H|^2-weighted mean MI distance."""
    W = np.abs(H) ** 2
    np.fill_diagonal(W, 0.0)
    total = W.sum()
    if total == 0:
        return 0.0
    return float((W * d_MI).sum() / total)

def alignment_continuous(C_F, region, d_MI):
    C_A = C_F[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    h_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    H = np.zeros((L, L))
    H[np.ix_(region, region)] = h_A
    r_actual = mean_mi_range(H, d_MI)
    evals, _ = np.linalg.eigh(H)
    r_rand = []
    for _ in range(SCRAMBLES):
        Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
        r_rand.append(mean_mi_range(Q @ np.diag(evals) @ Q.T, d_MI))
    return float(np.mean(r_rand) / r_actual) if r_actual > 0 else 0.0

def alignment_of(O_F, C):
    C_F = O_F.T @ C @ O_F
    I = mi_matrix(C_F)
    off = I[np.triu_indices(L, k=1)]
    if off.max() < 1e-9:
        return float('nan')
    d_MI = -np.log(np.clip(I / off.max(), clip, None))
    np.fill_diagonal(d_MI, 0.0)
    order = fiedler_order(I)
    region = np.sort(order[:L // 2])
    return alignment_continuous(C_F, region, d_MI)

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
C = ground_state_correlation()
print("=" * 78)
print("CUSP GRANULARITY CHECK -- continuous locality functional")
print("=" * 78)
print()

a_site = alignment_of(np.eye(L), C)
print(f"F_site alignment (continuous): {a_site:.3f}")
print()
print(f"{'eps':>6s}  {'mean rival':>10s}  {'margin':>8s}")
print("-" * 78)

margins = []
for eps in EPS_VALUES:
    rivals = [alignment_of(near_local_rotation(eps, 5000 + s), C)
              for s in range(SEEDS)]
    m = a_site - np.mean(rivals)
    margins.append(m)
    print(f"{eps:>6.2f}  {np.mean(rivals):10.3f}  {m:8.3f}")
print("-" * 78)

# Haar control
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
a_haar = alignment_of(np.eye(L), C_haar)
print(f"Haar control: alignment {a_haar:.2f} (bar < 3)")
print()

# margin shape fit
log_eps = np.log(EPS_VALUES)
log_m = np.log(margins)
alpha, intercept = np.polyfit(log_eps, log_m, 1)
print(f"margin ~ eps^{alpha:.2f}   (alpha ~ 2: smooth extremum; "
      f"alpha < 1: cusp is physics)")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("C1: F_site wins at every eps",
     all(m > 0 for m in margins), f"margins {[f'{m:.2f}' for m in margins]}"),
    ("C2: margin shape decided (alpha > 1.2 or < 0.8)",
     alpha > 1.2 or alpha < 0.8, f"alpha = {alpha:.2f}"),
    ("C3: Haar alignment < 3", a_haar < 3.0, f"{a_haar:.2f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
verdict = ("cusp was quantile GRANULARITY (smooth extremum)"
           if alpha > 1.2 else
           "cusp is PHYSICS (sublinear margin at the extremum)"
           if alpha < 0.8 else "inconclusive")
print(f"Verdict on the cusp: {verdict} (alpha = {alpha:.2f})")
