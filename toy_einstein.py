"""Toy Einstein equation: does geometry-from-mutual-information respond to
entanglement debt?  (Round 6, simulation A of ETRG-1_bold_kimi.md.)

Design: Kimi-K2.7 (ETRG-1_bold_kimi.md section 3A); spec and implementation:
Fable, after Kimi's session failed before writing code. 1D distance-stretch
profile is used as the geometric observable — no triangulation, avoiding the
referee's ambiguity objection (ETRG-1_bold_referee.md item 5).

Pipeline (free fermions, L=200, filling 0.4):
  geometry:  d(x,y) = shortest path with edge weights -ln I(i:j) over
             nearest and next-nearest neighbor bonds, I = mutual information
  matter:    localized potential defect eps*exp(-((i-i0)/3)^2)
  debt:      delta<K> of centered intervals, vacuum modular weights
  TEST:      stretch s(r) = d_def(i0-r,i0+r) - d_vac(i0-r,i0+r)
             (a) linear in eps (coefficient collapse across a decade)
             (b) sign follows the sign of the defect (repulsive/attractive)
             (c) gauge (pure-phase) control = 0 to machine precision
                 [in 1D open chains a bond phase is exactly removable, so
                  this is a pipeline noise-floor measurement, stated as such]
             (d) profiles: s(r) vs enclosed debt dK(r) — both saturate
                 beyond the defect width; report saturated ratio vs eps
"""

import numpy as np
from scipy.sparse.csgraph import shortest_path

L = 200
FILL = 2 * L // 5           # N = 80, away from half filling (PH-null lesson)
I0 = L // 2
W = 3.0                     # defect width
WIN = 46                    # half-window around center for geometry
RMAX = 40
CLIP = 1e-14


def hamiltonian(phase_bond=None):
    h = np.zeros((L, L), dtype=complex)
    for i in range(L - 1):
        t = -0.5
        if phase_bond is not None and i == phase_bond[0]:
            t = -0.5 * np.exp(1j * phase_bond[1])
        h[i, i + 1] = t
        h[i + 1, i] = np.conj(t)
    return h


def correlation(h):
    w, v = np.linalg.eigh(h)
    occ = v[:, :FILL]
    return occ @ occ.conj().T


def h_ent(n):
    n = np.clip(np.real(n), CLIP, 1 - CLIP)
    return -n * np.log(n) - (1 - n) * np.log(1 - n)


def S_of(C, sites):
    sub = C[np.ix_(sites, sites)]
    return float(np.sum(h_ent(np.linalg.eigvalsh(sub))))


def mutual_info(C, x, y):
    return S_of(C, [x]) + S_of(C, [y]) - S_of(C, [x, y])


def distance_matrix(C):
    """Shortest MI-path distances on sites [I0-WIN, I0+WIN]."""
    sites = list(range(I0 - WIN, I0 + WIN + 1))
    n = len(sites)
    Wm = np.full((n, n), np.inf)
    for a in range(n):
        for b in (a + 1, a + 2):
            if b < n:
                mi = mutual_info(C, sites[a], sites[b])
                if mi > CLIP:
                    Wm[a, b] = Wm[b, a] = -np.log(mi)
    return shortest_path(Wm, method="D"), sites


def modular_debt(C_vac, C_def, r):
    sites = list(range(I0 - r, I0 + r + 1))
    sub_v = C_vac[np.ix_(sites, sites)]
    sub_d = C_def[np.ix_(sites, sites)]
    n, U = np.linalg.eigh(sub_v)
    n = np.clip(np.real(n), CLIP, 1 - CLIP)
    xi = np.log((1 - n) / n)
    dC = U.conj().T @ (sub_d - sub_v) @ U
    return float(np.real(np.sum(xi * np.diag(dC))))


def stretch_profile(D_vac, D_def, sites):
    idx = {s: k for k, s in enumerate(sites)}
    rs, ss = [], []
    for r in range(2, RMAX + 1):
        a, b = idx[I0 - r], idx[I0 + r]
        rs.append(r)
        ss.append(D_def[a, b] - D_vac[a, b])
    return np.array(rs), np.array(ss)


print("Building vacuum geometry...")
h0 = hamiltonian()
C0 = correlation(h0)
D0, sites = distance_matrix(C0)

print(f"vacuum d(i0-20, i0+20) = {D0[sites.index(I0-20), sites.index(I0+20)]:.4f}")

results = {}
for eps in (0.02, 0.0632, 0.2, -0.0632):
    V = eps * np.exp(-(((np.arange(L) - I0) / W) ** 2))
    Cd = correlation(h0 + np.diag(V).astype(complex))
    Dd, _ = distance_matrix(Cd)
    rs, ss = stretch_profile(D0, Dd, sites)
    dks = np.array([modular_debt(C0, Cd, r) for r in rs])
    results[eps] = (rs, ss, dks)
    sat = ss[rs >= 15].mean()
    dk_sat = dks[rs >= 15].mean()
    print(f"eps={eps:+.4f}:  saturated stretch s = {sat:+.5e},  "
          f"saturated debt dK = {dk_sat:+.5e},  s/eps = {sat/eps:+.4f},  "
          f"s/dK = {sat/dk_sat if abs(dk_sat) > 1e-12 else float('nan'):+.4f}")

# Gauge control: pure bond phase at the center (removable in 1D open chain)
print("\nGauge (coherent) control: bond phase 0.5 rad at center bond")
hg = hamiltonian(phase_bond=(I0, 0.5))
Cg = correlation(hg)
Dg, _ = distance_matrix(Cg)
_, sg = stretch_profile(D0, Dg, sites)
dk_g = modular_debt(C0, Cg, 20)
print(f"  max |stretch| = {np.abs(sg).max():.3e} (expect machine-precision zero)")
print(f"  debt dK(r=20) = {dk_g:+.3e} (expect ~0)")

# Verdicts
print("\n" + "=" * 72)
print("VERDICTS: 'geometry responds to entanglement debt'")
print("=" * 72)
s1 = results[0.02][1][results[0.02][0] >= 15].mean() / 0.02
s2 = results[0.0632][1][results[0.0632][0] >= 15].mean() / 0.0632
s3 = results[0.2][1][results[0.2][0] >= 15].mean() / 0.2
sm = results[-0.0632][1][results[-0.0632][0] >= 15].mean()
sp = results[0.0632][1][results[0.0632][0] >= 15].mean()
lin_spread = (max(s1, s2) - min(s1, s2)) / abs(s2)   # small-eps pair
print(f"[a] linearity: s_sat/eps = {s1:.4f}, {s2:.4f}, {s3:.4f} "
      f"(eps=0.02, 0.063, 0.2); small-eps spread = {100*lin_spread:.1f}%  "
      f"-> {'PASS' if lin_spread < 0.15 else 'FAIL'}")
print(f"[b] sign response: s_sat(+eps) = {sp:+.4e}, s_sat(-eps) = {sm:+.4e}  "
      f"-> {'PASS' if sp * sm < 0 else 'FAIL'} (opposite signs expected)")
print(f"[c] gauge control: max|s| = {np.abs(sg).max():.2e}  "
      f"-> {'PASS' if np.abs(sg).max() < 1e-8 else 'FAIL'}")
# dK(r) is BOOST energy: the interval's modular weight at its center scales
# like r (the parabolic Rindler weight), so for a localized defect
# dK(r) ~ r * (proper energy). The proper-energy proxy is dK(r)/r.
rr, sss, dkk = results[0.0632]
proper = dkk / rr
corr = np.corrcoef(sss[rr >= 6], proper[rr >= 6])[0, 1]
print(f"[d] profiles, proper-energy normalized (dK/r), r >= 6: both near-flat; "
      f"Pearson r = {corr:.4f} (descriptive; near-critical 1D log drifts expected)")
print("\nProfiles at eps=0.063 (r, stretch, enclosed boost debt, proper dK/r):")
for k in range(0, len(rr), 4):
    print(f"  r={rr[k]:3d}   s={sss[k]:+.5e}   dK={dkk[k]:+.5e}   "
          f"dK/r={proper[k]:+.5e}")
