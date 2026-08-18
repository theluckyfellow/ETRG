#!/usr/bin/env python3
"""
Near-local-rival factorization check (round 9, the killer test) --
PRE-REGISTERED.

The round-8 referee's deflation of rotated_factorization_check.py: the menu
(site / block / random / momentum) lacked the only hard case -- SMOOTH
QUASI-LOCAL ROTATIONS of the site basis, the regime where factorization
selection is actually difficult.  This is that test.

Rivals: O(eps) = exp(eps * A), A antisymmetric and banded (bandwidth 2,
random entries, several seeds).  Each virtual site is a smooth local
mixture of nearby sites -- nearly as local as the site basis itself.
As eps -> 0 the rival approaches F_site, so the margin MUST shrink
(sanity); the killer question is whether it ever CROSSES.

PRE-REGISTERED PREDICTIONS:
  P1  F_site wins bootstrap alignment over EVERY near-local rival
      (bar: strictly smallest -- the 1.5x bar was for the easy menu;
      the hard case gets the honest bar).
  P2  the margin shrinks monotonically as eps -> 0 (sanity).
  P3  Haar-random state: no factorization's alignment exceeds 3 (teeth,
      recalibrated per the round-8 referee's F2 -- no bar movement after
      the fact; this bar is set NOW, before the run).
  P4  if any rival beats F_site: the bootstrap selection principle fails
      in exactly the regime the referee named, and is scoped accordingly.
      Reported as measured.
"""

import numpy as np

L = 60
N = L // 2
clip = 1e-12
SCRAMBLES = 20
SEEDS = 5
EPS_VALUES = [0.1, 0.3, 0.5]
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
    evals, evecs = np.linalg.eigh(Lap)
    return np.argsort(evecs[:, 1])

def kernel_alignment(C_F, region, d_MI):
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
    return kernel_alignment(C_F, region, d_MI)

def near_local_rotation(eps, seed):
    rng_local = np.random.default_rng(seed)
    A = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, min(i + 3, L)):   # bandwidth 2
            A[i, j] = rng_local.standard_normal()
    A = A - A.T
    # matrix exponential via eigendecomposition of the antisymmetric A
    evals, evecs = np.linalg.eig(1j * A)
    return np.real(evecs @ np.diag(np.exp(-1j * eps * evals))
                   @ evecs.conj().T)

def orth_error(O):
    return float(np.max(np.abs(O @ O.T - np.eye(L))))

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
C = ground_state_correlation()
print("=" * 78)
print("NEAR-LOCAL-RIVAL FACTORIZATION CHECK -- the round-9 killer test")
print("=" * 78)
print()

a_site = alignment_of(np.eye(L), C)
print(f"F_site alignment: {a_site:.3f}")
print()
print(f"{'eps':>6s}  {'seed':>4s}  {'orth err':>9s}  {'alignment':>10s}  "
      f"{'margin vs site':>14s}")
print("-" * 78)

rival_align = {eps: [] for eps in EPS_VALUES}
for eps in EPS_VALUES:
    for s in range(SEEDS):
        O = near_local_rotation(eps, 1000 + s)
        err = orth_error(O)
        a = alignment_of(O, C)
        rival_align[eps].append(a)
        print(f"{eps:>6.1f}  {s:>4d}  {err:9.1e}  {a:10.3f}  "
              f"{a_site - a:14.3f}")
    print("-" * 78)

# Haar control
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
a_haar_site = alignment_of(np.eye(L), C_haar)
O_nl = near_local_rotation(0.3, 2000)
a_haar_nl = alignment_of(O_nl, C_haar)
print(f"Haar state: F_site {a_haar_site:.2f}, near-local(0.3) "
      f"{a_haar_nl:.2f}")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 78)
all_rivals = [a for eps in EPS_VALUES for a in rival_align[eps]]
best_rival = max(all_rivals)
mean_margins = [a_site - np.mean(rival_align[eps]) for eps in EPS_VALUES]
checks = [
    ("P1: F_site beats EVERY near-local rival",
     a_site > best_rival,
     f"site {a_site:.3f} vs best rival {best_rival:.3f}"),
    ("P2: margin shrinks monotonically as eps -> 0",
     mean_margins[0] < mean_margins[1] < mean_margins[2],
     f"margins {[f'{m:.3f}' for m in mean_margins]}"),
    ("P3: Haar alignments below 3 (teeth)",
     max(a_haar_site, a_haar_nl) < 3.0,
     f"{a_haar_site:.2f}, {a_haar_nl:.2f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("P4: if any rival beat F_site, the bootstrap principle is scoped")
print("    to coarse scrambling only -- reported as measured above.")
