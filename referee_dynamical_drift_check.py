#!/usr/bin/env python3
"""
Referee verification (round 8): the direct dynamical drift, operationalized
WITHOUT a clock decision -- contra the quench postscript.

The postscript to note section 12 claims the correct dynamical drift
"requires the region observer's evolution model" and is therefore a physics
decision, not a coding one.  That is wrong as stated.  N2's drift is
    coarsen-then-evolve  vs  evolve-then-coarsen,
and both paths are computable with NO region-local evolution law: evolution
is the full-chain e^{-i h0 t} (the same choice section 12 already made to
justify [K_A, h0]); coarsening is the observer's dephasing channel in the
t=0 modular basis of their region.  At the Gaussian level the dephasing
channel D_A acts on the full correlation matrix as: pinch the A-block to
its diagonal in the modular basis, zero the A-complement cross blocks,
keep the complement block (phase-averaging over each region-modular mode).

    m(T) = || ( D[U_T C0 U_T^+] - U_T D[C0] U_T^+ )_AA ||_F

m(0) = 0 exactly; m(T) is the drift of the coarse book against the
observer's own (global-physical-time) evolution model.  If [K_A, h0] is
what section 12 says it is, contiguous must win this -- especially at
small T, where m linearizes to the superoperator commutator [D, ad_h0].

Design fix for quench_drift_check.py's confound: ONE shared initial state
(bump at the chain center), and rivals with the SAME footprint as the
contiguous region -- alternating sites of the central window, and random
subsets of the central window -- so all candidates receive comparable
drive.  Global-random and even/odd kept for reference.  Per-unit-dynamics
ratio reported alongside raw.

Referee predictions (registered here, before the run):
  R1  contiguous beats alternating-in-window and random-in-window on
      m(T)/||dC_A|| at small T (T = 5), where the generator picture holds.
  R2  if R1 fails, the generator-level eta of drift_check.py does not
      measure N2 drift, and "the weld's first real number" loses its
      dynamical interpretation.
"""

import numpy as np

clip = 1e-12
L = 200
FILL = 2 * L // 5
EPS = 0.05
W_BUMP = 5.0
T_VALUES = [5.0, 20.0, 80.0]
rng = np.random.default_rng(7)

def chain(L):
    h = np.zeros((L, L))
    for i in range(L - 1):
        h[i, i + 1] = h[i + 1, i] = -0.5
    return h

def make_regions():
    half = L // 5                       # 40 sites, quench-check convention
    center = L // 2
    window = np.arange(center - half, center + half)      # 80-site window
    contiguous = np.arange(center - half // 2, center + half // 2)
    alternating = window[::2]
    rand_window = [np.sort(rng.choice(window, half, replace=False))
                   for _ in range(2)]
    rand_global = np.sort(rng.choice(L, half, replace=False))
    even_odd = np.arange(0, 2 * half, 2)                  # quench-check's
    quarter = half // 2
    b1 = np.arange(L // 4 - quarter // 2, L // 4 - quarter // 2 + quarter)
    b2 = np.arange(3 * L // 4 - quarter // 2, 3 * L // 4 - quarter // 2
                   + half - quarter)
    two_interval = np.sort(np.concatenate([b1, b2]))
    return ([("contiguous", contiguous),
             ("alt-window", alternating),
             ("rand-window1", rand_window[0]),
             ("rand-window2", rand_window[1]),
             ("two-interval", two_interval),
             ("rand-global", rand_global),
             ("even/odd", even_odd)])

def dephase(C, region, U_A):
    """Gaussian dephasing channel in the region's fixed modular basis:
    pinch A-block in U_A basis, kill A-complement coherences."""
    D = C.copy()
    A = np.ix_(region, region)
    X = U_A.conj().T @ C[A] @ U_A
    D[A] = U_A @ np.diag(np.diag(X).real) @ U_A.conj().T
    comp = np.setdiff1d(np.arange(L), region)
    D[np.ix_(region, comp)] = 0.0
    D[np.ix_(comp, region)] = 0.0
    return D

h0 = chain(L)
bump = EPS * np.diag(np.exp(-(((np.arange(L) - L // 2) / W_BUMP) ** 2)))
_, V0 = np.linalg.eigh(h0 + bump)
C0 = (V0[:, :FILL] @ V0[:, :FILL].T).astype(complex)     # shared state
E, V = np.linalg.eigh(h0)

print("=" * 78)
print("REFEREE CHECK: direct dynamical drift, no clock ambiguity")
print("shared central bump; footprint-matched rivals")
print("=" * 78)
print(f"{'T':>6s}  {'region':>13s}  {'m(T)':>9s}  {'||dC_A||':>9s}  "
      f"{'ratio':>8s}")
print("-" * 78)

regions = make_regions()
ratios = {}
for T in T_VALUES:
    U_T = (V * np.exp(-1j * E * T)) @ V.T
    C_T = U_T @ C0 @ U_T.conj().T
    for name, region in regions:
        A = np.ix_(region, region)
        _, U_A = np.linalg.eigh(C0[A])
        path_evolve_coarsen = dephase(C_T, region, U_A)
        DC0 = dephase(C0, region, U_A)
        path_coarsen_evolve = U_T @ DC0 @ U_T.conj().T
        m = float(np.linalg.norm(
            path_evolve_coarsen[A] - path_coarsen_evolve[A], 'fro'))
        drive = float(np.linalg.norm(C_T[A] - C0[A], 'fro'))
        ratios[(T, name)] = m / drive if drive > 0 else 0.0
        print(f"{T:>6.1f}  {name:>13s}  {m:9.5f}  {drive:9.5f}  "
              f"{ratios[(T, name)]:8.5f}")
    print("-" * 78)

print()
print("Adjudication of referee prediction R1 (footprint-matched rivals,")
print("ratio = drift per unit dynamics; contiguous must be smallest):")
for T in T_VALUES:
    c = ratios[(T, "contiguous")]
    rivals = {n: ratios[(T, n)] for n in
              ["alt-window", "rand-window1", "rand-window2"]}
    worst = min(rivals.values())
    verdict = "PASS" if worst > c else "FAIL"
    print(f"  T={T:5.1f}  contiguous {c:.5f} vs best footprint rival "
          f"{worst:.5f}  ({worst / c:.2f}x)  {verdict}")
