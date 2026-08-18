#!/usr/bin/env python3
"""
MI decomposition check (Route-B structure question) -- PRE-REGISTERED.

Route B (ETRG-4): geometry = cone field x entropic scale.  The probe
kinematics passed (geodesic_bending_check: null rays read only the cones).
This is the STRUCTURE question: does the mutual-information geometry of
the state itself decompose -- a cone part that responds to the hopping
(causality) field and a scale part that responds to entanglement debt?

Two deformations, centered at i0, Gaussian width w, MATCHED in
entanglement debt delta<K> (calibration run):
  cone:  hopping t_i -> t_i (1 - eps Phi_i)        (deforms c(x) = 2t(x))
  scale: on-site potential V_i = eps' Phi_i        (no cone deformation)

PRE-REGISTERED PREDICTIONS:
  D1  cone response is cone-shaped: the MI-distance change under the
      hopping deformation correlates with the cone-distance change
      Delta d_cone(i,j) = sum_bonds (1/c_def - 1/c_vac), Pearson r > 0.8.
  D2  scale response is NOT cone-shaped: under the debt-matched potential
      deformation, Delta d_MI correlates with Delta d_cone at r < 0.5
      (it responds to the debt instead -- the toy_einstein channel).
  D3  the lattice cone is the hopping field: wavefront arrival times of
      a single-particle quench track the cone prediction
      T(j) = sum (1/c(x)) dx with r > 0.9.
  D4  sign control: flipped hopping deformation flips the sign of the
      cone-shaped response.
"""

import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.linalg import expm_multiply
from scipy import sparse

L = 200
FILL = 2 * L // 5
I0 = L // 2
W = 6.0
EPS = 0.3
CLIP = 1e-14

def hamiltonian(cone_mod=0.0, pot_mod=0.0):
    h = np.zeros((L, L))
    Phi = np.exp(-(((np.arange(L) - I0) / W) ** 2))
    for i in range(L - 1):
        t = 0.5 * (1 - cone_mod * 0.5 * (Phi[i] + Phi[i + 1]))
        h[i, i + 1] = h[i + 1, i] = -t
    h += np.diag(pot_mod * Phi)
    return h

def correlation(h):
    _, V = np.linalg.eigh(h)
    occ = V[:, :FILL]
    return occ @ occ.T.conj()

def h_ent(n):
    n = np.clip(np.real(n), CLIP, 1 - CLIP)
    return -n * np.log(n) - (1 - n) * np.log(1 - n)

def S_of(C, sites):
    return float(np.sum(h_ent(np.linalg.eigvalsh(C[np.ix_(sites, sites)]))))

def mutual_info(C, x, y):
    return S_of(C, [x]) + S_of(C, [y]) - S_of(C, [x, y])

def distance_matrix(C):
    sites = list(range(I0 - 60, I0 + 61))
    n = len(sites)
    Wm = np.full((n, n), np.inf)
    for a in range(n):
        for b in (a + 1, a + 2):
            if b < n:
                mi = mutual_info(C, sites[a], sites[b])
                if mi > CLIP:
                    Wm[a, b] = Wm[b, a] = -np.log(mi)
    return shortest_path(Wm, method="D"), sites

def modular_debt(C_vac, C_def, r=20):
    sites = list(range(I0 - r, I0 + r + 1))
    sub_v = C_vac[np.ix_(sites, sites)]
    sub_d = C_def[np.ix_(sites, sites)]
    n, U = np.linalg.eigh(sub_v)
    n = np.clip(np.real(n), CLIP, 1 - CLIP)
    xi = np.log((1 - n) / n)
    dC = U.conj().T @ (sub_d - sub_v) @ U
    return float(np.real(np.sum(xi * np.diag(dC))))

def cone_distances(def_eps):
    """Cone (light-travel-time) distance change for site pairs, from the
    hopping field c(x) = 2t(x)."""
    Phi = np.exp(-(((np.arange(L) - I0) / W) ** 2))
    c = np.array([2 * 0.5 * (1 - def_eps * 0.5 * (Phi[i] + Phi[i + 1]))
                  for i in range(L - 1)])
    c0 = np.ones(L - 1) * 2 * 0.5
    seg = 1.0 / c - 1.0 / c0          # per-bond travel-time change
    cum = np.concatenate([[0], np.cumsum(seg)])
    return lambda i, j: cum[j] - cum[i] if j >= i else cum[i] - cum[j]

# -----------------------------------------------------------------------------
# Build states, calibrate the debt match
# -----------------------------------------------------------------------------
print("=" * 78)
print("MI DECOMPOSITION CHECK -- cone part vs scale part of the MI geometry")
print("=" * 78)
print()

C0 = correlation(hamiltonian())
C_cone = correlation(hamiltonian(cone_mod=EPS))
debt_cone = modular_debt(C0, C_cone)
# calibrate potential strength to match the debt
from scipy.optimize import brentq
eps_p = brentq(lambda e: modular_debt(C0, correlation(hamiltonian(pot_mod=e)))
               - debt_cone, 0.001, 2.0)
C_scale = correlation(hamiltonian(pot_mod=eps_p))
debt_scale = modular_debt(C0, C_scale)
print(f"debt match: cone debt = {debt_cone:+.5f} (eps={EPS}), "
      f"scale debt = {debt_scale:+.5f} (eps'={eps_p:.4f})")
print()

D0, sites = distance_matrix(C0)
D_cone, _ = distance_matrix(C_cone)
D_scale, _ = distance_matrix(C_scale)
d_cone_fn = cone_distances(EPS)

# pair sample: all pairs spanning the defect at various separations
pairs = []
for r in range(5, 55, 5):
    pairs.append((I0 - r, I0 + r))
idx = {s: k for k, s in enumerate(sites)}
dd_mi_cone, dd_mi_scale, dd_cone = [], [], []
for i, j in pairs:
    a, b = idx[i], idx[j]
    dd_mi_cone.append(D_cone[a, b] - D0[a, b])
    dd_mi_scale.append(D_scale[a, b] - D0[a, b])
    dd_cone.append(d_cone_fn(i, j))
dd_mi_cone = np.array(dd_mi_cone)
dd_mi_scale = np.array(dd_mi_scale)
dd_cone = np.array(dd_cone)

r1 = float(np.corrcoef(dd_mi_cone, dd_cone)[0, 1])
r2 = float(np.corrcoef(dd_mi_scale, dd_cone)[0, 1])
print(f"D1: corr(Delta d_MI[cone], Delta d_cone)  = {r1:.4f}  (bar > 0.8)")
print(f"D2: corr(Delta d_MI[scale], Delta d_cone) = {r2:.4f}  (bar < 0.5)")
print()

# -----------------------------------------------------------------------------
# D3: quench front tracks the hopping cone field
# -----------------------------------------------------------------------------
def front_arrivals(h, src, probe_sites, thresh=0.02):
    H = sparse.csr_matrix(h)
    psi0 = np.zeros(L)
    psi0[src] = 1.0
    arrivals = {}
    T_MAX = 400
    dt = 2.0
    psi = psi0
    for t in np.arange(0, T_MAX, dt):
        psi = expm_multiply(-1j * H * dt, psi)
        for p in probe_sites:
            if p not in arrivals and abs(psi[p]) ** 2 > thresh:
                arrivals[p] = t + dt
    return arrivals

probe_sites = list(range(I0 - 50, I0 + 51, 10))
arr_vac = front_arrivals(hamiltonian(), I0 - 50, probe_sites)
arr_def = front_arrivals(hamiltonian(cone_mod=EPS), I0 - 50, probe_sites)
Phi = np.exp(-(((np.arange(L) - I0) / W) ** 2))
c_def = np.array([2 * 0.5 * (1 - EPS * 0.5 * (Phi[i] + Phi[i + 1]))
                  for i in range(L - 1)])
t_pred_vac = {p: (p - (I0 - 50)) / (2 * 0.5) for p in probe_sites}
cum = np.concatenate([[0], np.cumsum(1.0 / c_def)])
t_pred_def = {p: cum[p] - cum[I0 - 50] for p in probe_sites}
tv = [arr_vac.get(p, np.nan) for p in probe_sites]
td = [arr_def.get(p, np.nan) for p in probe_sites]
pv = [t_pred_vac[p] for p in probe_sites]
pd = [t_pred_def[p] for p in probe_sites]
mask = ~np.isnan(tv) & ~np.isnan(td)
r3 = float(np.corrcoef(np.array(td)[mask], np.array(pd)[mask])[0, 1])
print(f"D3: corr(measured front arrivals, cone prediction) = {r3:.4f} "
      f"(bar > 0.9)")
print()

# D4: sign control
C_flip = correlation(hamiltonian(cone_mod=-EPS))
D_flip, _ = distance_matrix(C_flip)
dd_flip = np.array([D_flip[idx[i], idx[j]] - D0[idx[i], idx[j]]
                    for i, j in pairs])
sign_ok = np.corrcoef(dd_flip, dd_mi_cone)[0, 1] < -0.5
print(f"D4: flipped cone deformation anti-correlates "
      f"(r = {np.corrcoef(dd_flip, dd_mi_cone)[0, 1]:.3f}, bar < -0.5)")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("D1: cone response is cone-shaped (r > 0.8)", r1 > 0.8, f"{r1:.3f}"),
    ("D2: scale response is NOT cone-shaped (r < 0.5)", r2 < 0.5,
     f"{r2:.3f}"),
    ("D3: quench front tracks the hopping cone (r > 0.9)", r3 > 0.9,
     f"{r3:.3f}"),
    ("D4: flipped deformation flips the response", sign_ok, ""),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
