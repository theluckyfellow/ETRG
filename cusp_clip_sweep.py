#!/usr/bin/env python3
"""
Clip sweep for the cusp (gates-audit nomination 1) -- PRE-REGISTERED.

The small-eps control found the continuous functional's margin is
logarithmic in eps and that 870/1770 site-basis d_MI pairs sit AT the
-ln(clip) cap.  If the cap is load-bearing, the cusp's DEPTH and its
vanishing scale belong to the regulator, and only the SIGN of the margin
(site basis a strict local extremum) is physics.  This sweep varies the
d_MI floor alone (DCLIP in {1e-8, 1e-12, 1e-16}; all numerical-stability
clips stay at 1e-12) and re-scores the eps sweep.

PRE-REGISTERED PREDICTIONS (regulator-structured reading):
  R1  a_site scales ~linearly with -ln(DCLIP): fitting
      a_site = c0 + c1 * (-ln DCLIP) gives r^2 > 0.9 with c1 > 0.
  R2  the margin's vanishing scale tracks the floor: at eps = 1e-4 the
      margin shrinks markedly at DCLIP = 1e-8 (below half its 1e-12
      value) and grows at DCLIP = 1e-16.
  R3  the SIGN is physics: F_site wins (margin > 0) at every DCLIP and
      every eps probed.
Adjudication: R1+R2 pass -> the cusp's sharpness/depth are the
regulator's; committed cusp claims must carry their clip and only the
strict-local-extremum statement survives regulator-free.  R3 fail at any
clip -> the extremum itself is regulator-dependent (far worse; report
loudly).

Pipeline copied verbatim from cusp_granularity_check.py except the d_MI
floor parameter.
"""

import numpy as np

L = 60
N = L // 2
clip = 1e-12                     # numerical-stability clip (unchanged)
DCLIP_VALUES = [1e-8, 1e-12, 1e-16]
SCRAMBLES = 20
SEEDS = 5
EPS_VALUES = [1e-4, 1e-3, 1e-2, 1e-1]
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
    W = np.abs(H) ** 2
    np.fill_diagonal(W, 0.0)
    total = W.sum()
    if total == 0:
        return 0.0
    return float((W * d_MI).sum() / total)

def alignment_of(O_F, C, dclip):
    C_F = O_F.T @ C @ O_F
    I = mi_matrix(C_F)
    off = I[np.triu_indices(L, k=1)]
    if off.max() < 1e-9:
        return float('nan')
    d_MI = -np.log(np.clip(I / off.max(), dclip, None))
    np.fill_diagonal(d_MI, 0.0)
    order = fiedler_order(I)
    region = np.sort(order[:L // 2])
    C_A = C_F[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_k = np.clip(n_k, clip, 1.0 - clip)
    h_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    H = np.zeros((L, L))
    H[np.ix_(region, region)] = h_A
    r_actual = mean_mi_range(H, d_MI)
    evals, _ = np.linalg.eigh(H)
    r_rand = [mean_mi_range(Q @ np.diag(evals) @ Q.T, d_MI)
              for Q in (np.linalg.qr(rng.standard_normal((L, L)))[0]
                        for _ in range(SCRAMBLES))]
    return float(np.mean(r_rand) / r_actual) if r_actual > 0 else 0.0

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
C = ground_state_correlation()
print("=" * 78)
print("CUSP CLIP SWEEP -- is the cusp's sharpness the regulator's?")
print("=" * 78)
print()

a_sites = {}
margins = {}
for dclip in DCLIP_VALUES:
    a_site = alignment_of(np.eye(L), C, dclip)
    a_sites[dclip] = a_site
    print(f"DCLIP = {dclip:.0e}  (cap = {-np.log(dclip):5.1f}):  "
          f"a_site = {a_site:.3f}")
    for eps in EPS_VALUES:
        rivals = [alignment_of(near_local_rotation(eps, 5000 + s), C, dclip)
                  for s in range(SEEDS)]
        m = a_site - np.mean(rivals)
        margins[(dclip, eps)] = m
        print(f"    eps = {eps:6.0e}:  mean rival {np.mean(rivals):8.3f}   "
              f"margin {m:8.3f}")
    print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
caps = np.array([-np.log(d) for d in DCLIP_VALUES])
sites = np.array([a_sites[d] for d in DCLIP_VALUES])
c1, c0 = np.polyfit(caps, sites, 1)
pred = c0 + c1 * caps
ss_res = float(np.sum((sites - pred) ** 2))
ss_tot = float(np.sum((sites - sites.mean()) ** 2))
r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0

m8, m12, m16 = (margins[(1e-8, 1e-4)], margins[(1e-12, 1e-4)],
                margins[(1e-16, 1e-4)])
print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("R1: a_site ~ linear in -ln(DCLIP) (r^2 > 0.9, slope > 0)",
     r2 > 0.9 and c1 > 0,
     f"slope {c1:.3f}/nat, r^2 = {r2:.3f}, a_site = "
     f"{[f'{a_sites[d]:.1f}' for d in DCLIP_VALUES]}"),
    ("R2: margin(1e-4) tracks the floor (halves at 1e-8, grows at 1e-16)",
     m8 < 0.5 * m12 and m16 > m12,
     f"{m8:.2f} / {m12:.2f} / {m16:.2f} at caps 18.4/27.6/36.8"),
    ("R3: sign is physics -- F_site wins everywhere",
     all(m > 0 for m in margins.values()),
     f"min margin {min(margins.values()):.3f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<58s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
print()
print("Reading (if R1+R2+R3): the cusp's depth and vanishing scale are")
print("REGULATOR-STRUCTURED -- quantitative margin/exponent claims must")
print("carry their clip -- while the strict-local-extremum statement")
print("(F_site wins, margin > 0) is clip-independent and stands as the")
print("toehold's regulator-free content.")
print()

# -----------------------------------------------------------------------------
# POST-HOC ADDENDUM (run after R1-R3 were known; reported, not barred):
# does the round-9 r_99 functional share the cap?
# -----------------------------------------------------------------------------
def r99_alignment(O_F, C, dclip):
    C_F = O_F.T @ C @ O_F
    I = mi_matrix(C_F)
    off = I[np.triu_indices(L, k=1)]
    d_MI = -np.log(np.clip(I / off.max(), dclip, None))
    np.fill_diagonal(d_MI, 0.0)
    region = np.sort(fiedler_order(I)[:L // 2])
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
        pairs = sorted(((d_MI[i, j], W[i, j]) for i in range(L)
                        for j in range(i + 1, L)), key=lambda p: p[0])
        acc = 0.0
        for d, w in pairs:
            acc += 2.0 * w
            if acc >= 0.99 * total:
                return d
        return pairs[-1][0]

    r_act = r99(H)
    evals, _ = np.linalg.eigh(H)
    r_rand = [r99(Q @ np.diag(evals) @ Q.T)
              for Q in (np.linalg.qr(rng.standard_normal((L, L)))[0]
                        for _ in range(SCRAMBLES))]
    return float(np.mean(r_rand) / r_act) if r_act > 0 else 0.0

print("ADDENDUM: r_99 functional (round-9 killer test's metric) vs the cap:")
for dclip in DCLIP_VALUES:
    a = r99_alignment(np.eye(L), C, dclip)
    print(f"  DCLIP = {dclip:.0e} (cap {-np.log(dclip):5.1f}):  "
          f"a_site = {a:.3f}   a_site/cap = {a / -np.log(dclip):.4f}")
print()
print("a_site/cap is CONSTANT: the scrambled r_99 baseline saturates the cap")
print("(>= 1% of a scrambled kernel's weight sits on capped pairs), so the")
print("r_99 alignment is exactly cap / r_99_actual.  Consequences: (i) the")
print("round-9 candidate ORDERING is exactly clip-invariant -- the cap")
print("cancels in every same-clip ratio -- so the killer test's comparisons")
print("stand rigorously; (ii) absolute alignment values, and fixed-number")
print("bars like the Haar-teeth 'alignment < 3', are regulator-denominated")
print("and should be restated as fractions of the cap (3/27.6 = 0.11).")
