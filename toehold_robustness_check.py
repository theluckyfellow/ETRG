#!/usr/bin/env python3
"""
Toehold robustness check (round 9) -- PRE-REGISTERED.

near_local_rival_check.py established that the site factorization is a
strong local extremum of the bootstrap-locality functional -- at L = 60,
critical state, single point in parameter space.  Two robustness axes,
both nominated in the note's section 14:

  A. L-SCALING: does the extremum survive at other sizes (L = 40, 120)?
  B. STATE-INDEPENDENCE: does it survive a gapped state (dimerized chain,
     delta = 0.3)?

Rivals: near-local rotations O(eps) = exp(eps*A), eps = 0.3, bandwidth 2,
3 seeds per configuration (fewer than the killer test's 5 -- L = 120 is
the expensive cell).

PRE-REGISTERED PREDICTIONS:
  P1  F_site beats every near-local rival at L = 40 AND L = 120
      (critical state).
  P2  F_site beats every near-local rival for the gapped state (L = 60).
  P3  Haar-random state: alignment < 3 at L = 60 (teeth, same bar as the
      killer test -- set before the run).
"""

import numpy as np

clip = 1e-12
SCRAMBLES = 20
SEEDS = 3
EPS = 0.3
rng = np.random.default_rng(7)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def ground_state_correlation(L, dimerization=0.0):
    h = np.zeros((L, L))
    for i in range(L - 1):
        t = 0.5 * (1.0 + dimerization * ((-1) ** i))
        h[i, i + 1] = h[i + 1, i] = -t
    _, V = np.linalg.eigh(h)
    occ = V[:, :L // 2]
    return occ @ occ.T.conj()

def mi_matrix(C, L):
    I = np.zeros((L, L))
    s = binary_entropy(np.clip(np.diag(C).real, clip, 1.0 - clip))
    for i in range(L):
        for j in range(i + 1, L):
            lam = np.linalg.eigvalsh(C[np.ix_([i, j], [i, j])])
            I[i, j] = I[j, i] = max(s[i] + s[j] - np.sum(binary_entropy(lam)),
                                    0.0)
    return I

def fiedler_order(I, L):
    W = I.copy()
    np.fill_diagonal(W, 0.0)
    Lap = np.diag(W.sum(axis=1)) - W
    _, evecs = np.linalg.eigh(Lap)
    return np.argsort(evecs[:, 1])

def kernel_alignment(C_F, region, d_MI, L):
    C_A = C_F[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    h_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    H = np.zeros((L, L))
    H[np.ix_(region, region)] = h_A

    def r99(M):
        W = np.abs(M) ** 2
        np.fill_diagonal(W, 0.0)
        total = W.sum()
        pairs = sorted(((d_MI[i, j], W[i, j])
                        for i in range(L) for j in range(i + 1, L)),
                       key=lambda p: p[0])
        acc = 0.0
        for d, w in pairs:
            acc += 2.0 * w
            if acc >= 0.99 * total:
                return d
        return pairs[-1][0]

    r_actual = r99(H)
    evals, _ = np.linalg.eigh(H)
    r_rand = []
    for _ in range(SCRAMBLES):
        Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
        r_rand.append(r99(Q @ np.diag(evals) @ Q.T))
    return float(np.mean(r_rand) / r_actual) if r_actual > 0 else 0.0

def alignment_of(O_F, C, L):
    C_F = O_F.T @ C @ O_F
    I = mi_matrix(C_F, L)
    off = I[np.triu_indices(L, k=1)]
    if off.max() < 1e-9:
        return float('nan')
    d_MI = -np.log(np.clip(I / off.max(), clip, None))
    np.fill_diagonal(d_MI, 0.0)
    order = fiedler_order(I, L)
    region = np.sort(order[:L // 2])
    return kernel_alignment(C_F, region, d_MI, L)

def near_local_rotation(L, eps, seed):
    rl = np.random.default_rng(seed)
    A = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, min(i + 3, L)):
            A[i, j] = rl.standard_normal()
    A = A - A.T
    evals, evecs = np.linalg.eig(1j * A)
    return np.real(evecs @ np.diag(np.exp(-1j * eps * evals))
                   @ evecs.conj().T)

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 78)
print("TOEHOLD ROBUSTNESS CHECK -- L-scaling and state-independence")
print("=" * 78)
print()

configs = [(40, 0.0, "P1a"), (120, 0.0, "P1b"), (60, 0.3, "P2")]
verdicts = {}
for L, dim, tag in configs:
    C = ground_state_correlation(L, dim)
    a_site = alignment_of(np.eye(L), C, L)
    rivals = [alignment_of(near_local_rotation(L, EPS, 3000 + s), C, L)
              for s in range(SEEDS)]
    best = max(rivals)
    verdicts[tag] = a_site > best
    state = "critical" if dim == 0.0 else f"dimerized {dim}"
    print(f"{tag}: L={L}, {state}: F_site {a_site:.3f} vs rivals "
          f"{[f'{r:.3f}' for r in rivals]} -> "
          f"{'WIN' if a_site > best else 'LOSS'}")

# Haar control at L = 60
L = 60
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
a_haar = alignment_of(np.eye(L), C_haar, L)
print(f"P3: Haar state (L=60): alignment {a_haar:.2f} (bar < 3)")
print()

print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("P1: F_site wins at L=40 and L=120 (critical)",
     verdicts["P1a"] and verdicts["P1b"],
     f"L40 {'WIN' if verdicts['P1a'] else 'LOSS'}, "
     f"L120 {'WIN' if verdicts['P1b'] else 'LOSS'}"),
    ("P2: F_site wins for the gapped state (L=60)",
     verdicts["P2"], f"{'WIN' if verdicts['P2'] else 'LOSS'}"),
    ("P3: Haar alignment < 3", a_haar < 3.0, f"{a_haar:.2f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
