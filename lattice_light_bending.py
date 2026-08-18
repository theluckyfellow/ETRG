#!/usr/bin/env python3
"""
Lattice light bending (the T3 mechanism test) -- PRE-REGISTERED.

The thesis's T3: entropy writes TWO faces of the geometry -- the lapse
(clock rate; slow matter falls by maximizing aging) and the spatial/causal
face (the cone itself; light reads it directly).  The deflection factor is
(1 + v^2/c^2): 1 at rest, exactly 2 at the cone.  The user's phrasing:
entropy shifts the spatial orientation of causality, and light -- moving
at the speed of causality -- is more affected.

On a 2D tight-binding lattice the two faces have exact analogs:
  lapse face:  on-site potential V(x)         (band-bottom shift)
  cone face:   hopping modulation t(x)        (local cone speed c(x) = 2t(x))
A "metric defect" drives both faces with one profile -- the lattice image
of g_00 and g_ij carrying the same Phi.

Ordinary potential scattering bends LESS at high speed (theta*v^2 ~ const);
metric gravity bends MORE slowly falling -- theta(v)*v^2 ~ (1 + v^2/c^2).
The discriminating statistic is alpha in theta(v)*v^2 = A(1 + alpha v^2/c^2):
  alpha = 0  Newtonian/lapse-only     alpha = 1  GR two-face metric
  alpha >> 1 pure refraction (cone-only)

Protocol: 2D lattice 80x40, absorbing boundaries.  Wavepackets (Gaussian,
impact parameter b = 8) at v/c in {0.2, 0.4, 0.6, 0.8, 0.95}, deflection
measured as transverse momentum kick / longitudinal momentum.  Three
defects: lapse-only, cone-only, metric (both faces, calibrated so lapse
and cone alone give equal slow-probe deflection).

PRE-REGISTERED PREDICTIONS:
  P1  lapse-only: theta*v^2 constant within 30% (alpha ~ 0).
  P2  metric: alpha = 1 +/- 0.3 (the GR fingerprint).
  P3  theta_metric/theta_lapse at v = 0.95c in [1.7, 2.3] (factor 2).
  P4  cone-only: reported (expect refraction-dominated, alpha large).
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

LX, LY = 80, 40
W = 6.0                    # defect width
B = 8                      # impact parameter
T_HOP = 0.5
CONE = 2 * T_HOP           # cone velocity c = 2t
EPS = 0.15                 # defect strength
V_FRACTIONS = [0.2, 0.4, 0.6, 0.8, 0.95]
ABSORB = 0.5               # absorbing boundary strength
EDGE = 5

def idx(x, y):
    return y * LX + x

def profile():
    """Gaussian defect profile Phi(x,y), peak 1 at center."""
    cx, cy = LX // 2, LY // 2
    Phi = np.zeros((LX, LY))
    for x in range(LX):
        for y in range(LY):
            Phi[x, y] = np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * W ** 2))
    return Phi

def build_h(Phi, v_lapse=0.0, cone_mod=0.0):
    """2D tight-binding with optional on-site (lapse) and hopping (cone)
    defects, plus absorbing boundary layers."""
    N = LX * LY
    h = sparse.lil_matrix((N, N), dtype=complex)
    for x in range(LX):
        for y in range(LY):
            i = idx(x, y)
            # absorbing boundary
            edge = min(x, y, LX - 1 - x, LY - 1 - y)
            if edge < EDGE:
                h[i, i] += -1j * ABSORB * (EDGE - edge) / EDGE
            # lapse defect
            h[i, i] += v_lapse * Phi[x, y]
            # hoppings with cone modulation
            if x + 1 < LX:
                j = idx(x + 1, y)
                t = T_HOP * (1 - cone_mod * 0.5 * (Phi[x, y] + Phi[x + 1, y]))
                h[i, j] = -t
                h[j, i] = -t
            if y + 1 < LY:
                j = idx(x, y + 1)
                t = T_HOP * (1 - cone_mod * 0.5 * (Phi[x, y] + Phi[x, y + 1]))
                h[i, j] = -t
                h[j, i] = -t
    return h.tocsr()

def wavepacket(v_frac):
    """Gaussian packet at left edge, impact parameter B, momentum (kx, 0)
    chosen for group velocity v = 2t sin(kx)."""
    kx = np.arcsin(np.clip(v_frac, 0, 1))
    psi = np.zeros((LX, LY), dtype=complex)
    sx, sy = 8.0, 4.0
    x0, y0 = 12, LY // 2 + B
    for x in range(LX):
        for y in range(LY):
            psi[x, y] = np.exp(-((x - x0) ** 2) / (2 * sx ** 2)
                               - ((y - y0) ** 2) / (2 * sy ** 2)) \
                * np.exp(1j * kx * x)
    psi = psi.reshape(-1)
    return psi / np.linalg.norm(psi), kx

def deflection(h, v_frac, T):
    """Transverse momentum kick after crossing, normalized by p_x."""
    psi0, kx = wavepacket(v_frac)
    psi_T = expm_multiply(-1j * h * T, psi0)
    p = psi_T.reshape(LX, LY)
    # <p_y> = sum psi* (-i d/dy) psi
    py = 0.0
    for y in range(1, LY - 1):
        d = (p[:, y + 1] - p[:, y - 1]) / 2.0
        py += np.vdot(p[:, y], -1j * d).real
    return py / np.sin(kx) if np.sin(kx) > 1e-9 else 0.0

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
Phi = profile()
print("=" * 78)
print("LATTICE LIGHT BENDING -- the T3 two-face mechanism test")
print("=" * 78)
print()

# Calibration: lapse-only and cone-only strengths matched at v = 0.2c
T_cross = 1.4 * LX / (0.2 * CONE)
h_lapse = build_h(Phi, v_lapse=4 * T_HOP * EPS)
h_cone = build_h(Phi, cone_mod=EPS)
th_lapse_cal = deflection(h_lapse, 0.2, T_cross)
th_cone_cal = deflection(h_cone, 0.2, T_cross)
print(f"calibration at v=0.2c: lapse-only theta = {th_lapse_cal:+.5f}, "
      f"cone-only theta = {th_cone_cal:+.5f}")
# rescale lapse so both faces give equal slow-probe deflection
lapse_strength = 4 * T_HOP * EPS * abs(th_cone_cal / th_lapse_cal) \
    * np.sign(th_cone_cal * th_lapse_cal)
print(f"matched lapse strength: {lapse_strength:+.5f} "
      f"(raw {4 * T_HOP * EPS:+.5f})")
print()

defects = {
    "lapse": build_h(Phi, v_lapse=lapse_strength),
    "cone": build_h(Phi, cone_mod=EPS),
    "metric": build_h(Phi, v_lapse=lapse_strength, cone_mod=EPS),
}

results = {name: [] for name in defects}
for name, h in defects.items():
    for vf in V_FRACTIONS:
        T = 1.4 * LX / (vf * CONE)
        th = deflection(h, vf, T)
        results[name].append(th)
        print(f"{name:>7s}  v={vf:.2f}c  theta = {th:+.6f}  "
              f"theta*v^2 = {th * vf ** 2:+.6f}")
    print()

# -----------------------------------------------------------------------------
# Analysis
# -----------------------------------------------------------------------------
v2 = np.array(V_FRACTIONS) ** 2

def fit_alpha(thetas):
    """theta*v^2 = A(1 + alpha v^2): linear fit in v^2."""
    y = np.abs(np.array(thetas)) * v2
    A_mat = np.vstack([np.ones_like(v2), v2]).T
    coef, *_ = np.linalg.lstsq(A_mat, y, rcond=None)
    return coef[1] / coef[0] if abs(coef[0]) > 1e-12 else np.nan, coef[0]

alpha_lapse, _ = fit_alpha(results["lapse"])
alpha_metric, _ = fit_alpha(results["metric"])
alpha_cone, _ = fit_alpha(results["cone"])
ratio_95 = abs(results["metric"][-1] / results["lapse"][-1])

# P1: constancy of theta*v^2 for lapse
y_lapse = np.abs(np.array(results["lapse"])) * v2
constancy = (y_lapse.max() - y_lapse.min()) / y_lapse.mean()

print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("P1: lapse-only theta*v^2 constant within 30% (alpha ~ 0)",
     constancy < 0.30, f"spread {100 * constancy:.0f}%, "
     f"alpha = {alpha_lapse:.2f}"),
    ("P2: metric alpha = 1 +/- 0.3 (GR fingerprint)",
     abs(alpha_metric - 1.0) < 0.3, f"alpha = {alpha_metric:.2f}"),
    ("P3: theta_metric/theta_lapse at 0.95c in [1.7, 2.3]",
     1.7 < ratio_95 < 2.3, f"{ratio_95:.2f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<54s}  {value}")
print()
print(f"P4 (reported): cone-only alpha = {alpha_cone:.2f} "
      f"(refraction-dominated expected)")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
