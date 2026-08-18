#!/usr/bin/env python3
"""
Referee verification (round 8): is drift_check.py's eta regulator-dependent?

The modular kernel clips occupations at `clip`, capping |xi| at ln(1/clip)
(27.6 at 1e-12).  For a GEOMETRIC region of the critical vacuum the
occupations pin to 0/1 exponentially, so many kernel eigenvalues sit AT the
cap -- both ||K||_F and ||[K, h0]||_F are then functions of the regulator.
Scrambled regions (volume-law, occupations away from 0/1) clip less.  If
the separations and the slope 0.64 move materially with clip, the "weld's
first real number" is partly an artifact of an arbitrary cutoff.

Protocol: drift_check.py's exact pipeline, clip swept over 1e-6 / 1e-9 /
1e-12, plus a count of clipped eigenvalues per region at L = 320.
"""

import numpy as np

RANDOM_SEEDS = 3
MASTER_SEED = 7
L_values = [40, 80, 160, 320]
CLIPS = [1e-6, 1e-9, 1e-12]

def ground_state_correlation(L, N):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    _, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj(), h

def make_regions(L, rng):
    half = L // 2
    quarter = half // 2
    contiguous = np.arange((L - half) // 2, (L - half) // 2 + half)
    even_odd = np.arange(0, L, 2)
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - (quarter - quarter // 2),
                   3 * L // 4 - (quarter - quarter // 2)
                   + (quarter - quarter // 2) * 2)
    two_interval = np.sort(np.concatenate([b1, b2]))
    randoms = [np.sort(rng.choice(L, half, replace=False))
               for _ in range(RANDOM_SEEDS)]
    return contiguous, even_odd, two_interval, randoms

def drift_eta(C, h0, region, clip):
    L = h0.shape[0]
    C_A = C[np.ix_(region, region)]
    n_k, U = np.linalg.eigh(C_A)
    n_clipped = int(np.sum((n_k < clip) | (n_k > 1.0 - clip)))
    n_k = np.clip(n_k, clip, 1.0 - clip)
    k_A = (U * np.log((1.0 - n_k) / n_k)) @ U.T
    K = np.zeros((L, L))
    K[np.ix_(region, region)] = k_A
    comm = K @ h0 - h0 @ K
    eta = float(np.linalg.norm(comm, 'fro')
                / (np.linalg.norm(K, 'fro') * np.linalg.norm(h0, 'fro')))
    return eta, n_clipped

print("=" * 78)
print("REFEREE CHECK: clip sensitivity of the drift commutator eta")
print("=" * 78)
for clip in CLIPS:
    sep = []
    clip_counts = {}
    for L in L_values:
        rng = np.random.default_rng(MASTER_SEED)
        C, h0 = ground_state_correlation(L, L // 2)
        contiguous, even_odd, two_interval, randoms = make_regions(L, rng)
        etas = {}
        for name, region in ([("contiguous", contiguous),
                              ("even/odd", even_odd)]
                             + [(f"random #{k+1}", r)
                                for k, r in enumerate(randoms)]):
            etas[name], nc = drift_eta(C, h0, region, clip)
            if L == 320:
                clip_counts[name] = nc
        rivals = [etas[n] for n in etas if n != "contiguous"]
        sep.append(min(rivals) / etas["contiguous"])
    slope, _ = np.polyfit(np.log(L_values), np.log(sep), 1)
    print(f"clip = {clip:.0e}:  separations "
          f"{[f'{s:.1f}' for s in sep]}  slope {slope:.2f}")
    print(f"    clipped eigenvalues at L=320 (of 160): {clip_counts}")
print("-" * 78)
print("If separations/slope drift with clip, eta is regulator-dependent.")
