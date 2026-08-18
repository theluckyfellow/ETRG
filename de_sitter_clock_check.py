#!/usr/bin/env python3
"""
de Sitter clock check (the comoving-observer computation) -- PRE-REGISTERED.

GLM's adjudication of B7 (ETRG-1_bold_referee.md section 2): having a
horizon is necessary but not sufficient -- the comoving observer's mode
algebra is not the static-patch wedge algebra, so the horizon does not
make the partition canonical FOR THE COMOVING OBSERVER.  This script makes
that verdict computable, in the one setting where the toy is exact:

1+1D de Sitter is conformally flat, so a conformal field's equal-time
vacuum correlators on the circle are EXACTLY the critical chain's
(periodic free-fermion chain, half filling).  The dictionary:
  comoving spatial region      <->  interval of the chain
  comoving momentum modes      <->  momentum bipartition (what cosmology uses)
  static patch (a geodesic     <->  half-circle interval; its modular flow
  observer's causal patch)          is the CFT circle-diamond (Hislop-Longo/
                                    Casini-Huerta-Myers sine kernel), the
                                    toy image of Gibbons-Hawking

PRE-REGISTERED PREDICTIONS:
  P1  the comoving momentum bipartition is DEGENERATE (max inter-mode
      MI < 1e-9): killed by the degeneracy clause -- the Fourier-mode
      observer has no entropic clock at all.
  P2  the static-patch (half-circle) kernel's full-range weight profile
      matches the CFT circle-diamond sine form
          f(theta) = sin((theta-theta1)/2) sin((theta2-theta)/2)
                     / sin((theta2-theta1)/2)
      with correlation r_sine > 0.85 AND r_sine > r_parabola (the
      flat-space form loses on the circle).
  P3  comoving SPATIAL intervals are modular-local (r_99 <= 5): the
      comoving observer's only admissible clock is position-space, not
      momentum-space.
  P4  Haar-random state: no sine profile (r_sine < 0.5).

If P1-P3 pass: GLM's verdict is confirmed at toy level, and B7's
corrected form is computable -- the horizon selects the static patch's
diamond clock, not the comoving modes.
"""

import numpy as np

L = 200
N = L // 2
clip = 1e-12
rng = np.random.default_rng(7)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def periodic_chain():
    h = np.zeros((L, L))
    for i in range(L):
        h[i, (i + 1) % L] = h[(i + 1) % L, i] = -0.5
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

def modular_kernel(C, region):
    C_A = C[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    return (U * np.log((1.0 - n_k) / n_k)) @ U.T

def full_range_weight(h_A):
    n = h_A.shape[0]
    return np.array([np.sum(np.abs(h_A[k, :])) - abs(h_A[k, k])
                     for k in range(n)])

def r99_kernel(h_A, region):
    H = np.zeros((L, L))
    H[np.ix_(region, region)] = h_A
    dist = np.abs(np.subtract.outer(np.arange(L), np.arange(L))).astype(float)
    W = np.abs(H) ** 2
    np.fill_diagonal(W, 0.0)
    total = W.sum()
    pairs = sorted(((dist[i, j], W[i, j]) for i in range(L)
                    for j in range(i + 1, L)), key=lambda p: p[0])
    acc = 0.0
    for d, w in pairs:
        acc += 2.0 * w
        if acc >= 0.99 * total:
            return d
    return pairs[-1][0]

print("=" * 72)
print("DE SITTER CLOCK CHECK -- the comoving-observer computation")
print("=" * 72)
print()

h0 = periodic_chain()
C = ground_state_correlation(h0)

# -----------------------------------------------------------------------------
# P1: comoving momentum bipartition (exact plane-wave eigenbasis)
# -----------------------------------------------------------------------------
energies, V = np.linalg.eigh(h0)      # V columns = momentum modes
C_mode = V.T @ C @ V                  # should be diag(1 x N, 0 x L-N)
region_modes = np.arange(L // 2)      # the L/2 lowest-energy modes
C_A = C_mode[np.ix_(region_modes, region_modes)]
S_A = float(np.sum(binary_entropy(np.linalg.eigvalsh(C_A))))
I_max = 0.0
for i in range(L):
    for j in range(i + 1, L):
        block = C_mode[np.ix_([i, j], [i, j])]
        lam = np.linalg.eigvalsh(block)
        val = float(binary_entropy(C_mode[i, i]) + binary_entropy(C_mode[j, j])
                    - np.sum(binary_entropy(lam)))
        I_max = max(I_max, val)
print(f"P1: comoving momentum bipartition: S_A = {S_A:.2e}, "
      f"max inter-mode MI = {I_max:.2e}  (bar < 1e-9)")
print()

# -----------------------------------------------------------------------------
# P2: the static patch = half-circle; kernel vs sine-diamond form
# -----------------------------------------------------------------------------
theta1, theta2 = 0, L // 2
region = np.arange(theta1, theta2)
h_A = modular_kernel(C, region)
W_prof = full_range_weight(h_A)
ell = len(region)
ks = np.arange(ell)
# CFT circle-diamond weight
f_sine = (np.sin((ks + 0.5) * np.pi / (2 * ell))
          * np.sin((ell - ks - 0.5) * np.pi / (2 * ell)))
f_sine /= np.sin(np.pi / 2)
# flat-space parabola
f_para = (ks + 0.5) * (ell - ks - 0.5)
r_sine = float(np.corrcoef(W_prof, f_sine)[0, 1])
r_para = float(np.corrcoef(W_prof, f_para)[0, 1])
print(f"P2: static-patch kernel profile: r_sine = {r_sine:.4f} "
      f"(bar > 0.85), r_parabola = {r_para:.4f} (must lose)")
print()

# -----------------------------------------------------------------------------
# P3: comoving spatial interval locality
# -----------------------------------------------------------------------------
r99 = r99_kernel(h_A, region)
print(f"P3: spatial interval (half-circle) kernel r_99 = {r99:.1f} "
      f"(bar <= 5)")
print()

# -----------------------------------------------------------------------------
# P4: Haar control
# -----------------------------------------------------------------------------
Q, _ = np.linalg.qr(rng.standard_normal((L, L)))
C_haar = Q @ np.diag(rng.uniform(0.05, 0.95, L)) @ Q.T
h_A_h = modular_kernel(C_haar, region)
W_h = full_range_weight(h_A_h)
r_sine_h = float(np.corrcoef(W_h, f_sine)[0, 1])
print(f"P4: Haar control: r_sine = {r_sine_h:.4f}  (bar < 0.5)")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
checks = [
    ("P1: momentum bipartition degenerate (no Fourier-mode clock)",
     S_A < 1e-6 and I_max < 1e-9, f"S_A {S_A:.1e}, max MI {I_max:.1e}"),
    ("P2: static-patch kernel = circle-diamond sine form",
     r_sine > 0.85 and r_sine > r_para,
     f"{r_sine:.3f} vs parabola {r_para:.3f}"),
    ("P3: spatial interval modular-local (r_99 <= 5)",
     r99 <= 5.0, f"{r99:.1f}"),
    ("P4: Haar control has no sine profile",
     r_sine_h < 0.5, f"{r_sine_h:.3f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("If P1-P3 pass: GLM's necessity-not-sufficiency verdict is confirmed")
print("at toy level -- the horizon selects the static patch's diamond clock,")
print("not the comoving modes; the comoving observer's only entropic clock")
print("is position-space.")
