#!/usr/bin/env python3
"""
Dirac-Malament check (Route-B toy, rebuilt) -- PRE-REGISTERED per Fable's
addendum R4: the null-invariance bar comes FIRST, before any 2:1 profile.

Route B's backbone (ETRG-4): the cone field (conformal class) and the scale
Omega are independent degrees of freedom; null rays read only the cones;
massive matter reads both.  Lattice realization: a 2D Dirac lattice
(graphene-like), where
  cone field  = hopping t(x)        -> local cone speed c(x) = 2t(x)
  scale Omega = mass term m(x)      -> what massive probes' clocks read
  null probe  = massless wavepacket at the Dirac point (linear dispersion,
                no spreading -- the failure mode of the Schroedinger toy)
  massive     = packet with bare mass m0, group velocity < c

PRE-REGISTERED BARS (Fable's order: Malament first, profile second):
  B1  LATTICE MALAMENT: null-probe deflection under a pure-m(x)
      deformation (fixed cone field) is ~ zero:
      |theta_null(m-def)| < 0.15 * |theta_null(c-def)|.
  B2  massive probes READ the scale: |theta_massive(m-def)| > 3x
      |theta_null(m-def)|.
  B3  (scored only if B1 passes) the 2:1 profile: with both faces driven
      by one profile matched GR-style, theta(v)*v^2 = A(1 + alpha v^2/c^2)
      has alpha = 1 +/- 0.4, and theta_metric/theta_scale at the cone is
      in [1.6, 2.4].
  B4  sign control: the deformation with flipped sign flips the
      deflection sign (coherent response, not numerical noise).
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

LX, LY = 60, 30
W = 5.0                    # deformation width
B_IMP = 6                  # impact parameter
T_HOP = 0.5
CONE = 2 * T_HOP
EPS = 0.3                  # deformation strength
M0 = 0.3                   # bare mass of the massive probe
K0 = 0.35                  # carrier momentum of probes
EDGE = 4
ABSORB = 0.4

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)

def profile():
    Phi = np.zeros((LX, LY))
    cx, cy = LX // 2, LY // 2
    for x in range(LX):
        for y in range(LY):
            Phi[x, y] = np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * W ** 2))
    return Phi

def build_h(Phi, cone_mod=0.0, mass_mod=0.0, bare_mass=0.0):
    """2D Dirac lattice: -i t sigma_x on x-bonds, -i t sigma_y on y-bonds,
    (bare_mass + mass_mod*Phi) sigma_z on sites, absorbing edges."""
    N = LX * LY * 2
    h = sparse.lil_matrix((N, N), dtype=complex)

    def idx(x, y, a):
        return (y * LX + x) * 2 + a

    for x in range(LX):
        for y in range(LY):
            edge = min(x, y, LX - 1 - x, LY - 1 - y)
            absorb = -1j * ABSORB * max(0, EDGE - edge) / EDGE
            m = bare_mass + mass_mod * Phi[x, y]
            for a in range(2):
                i = idx(x, y, a)
                h[i, i] += absorb
                for b in range(2):
                    h[idx(x, y, a), idx(x, y, b)] += m * sz[a, b]
            if x + 1 < LX:
                t = T_HOP * (1 - cone_mod * 0.5 * (Phi[x, y] + Phi[x + 1, y]))
                for a in range(2):
                    for b in range(2):
                        h[idx(x, y, a), idx(x + 1, y, b)] += -1j * t * sx[a, b] / 2
                        h[idx(x + 1, y, b), idx(x, y, a)] += 1j * t * sx[a, b] / 2
            if y + 1 < LY:
                t = T_HOP * (1 - cone_mod * 0.5 * (Phi[x, y] + Phi[x, y + 1]))
                for a in range(2):
                    for b in range(2):
                        h[idx(x, y, a), idx(x, y + 1, b)] += -1j * t * sy[a, b] / 2
                        h[idx(x, y + 1, b), idx(x, y, a)] += 1j * t * sy[a, b] / 2
    return h.tocsr()

def wavepacket(bare_mass):
    """Positive-energy Gaussian packet, carrier (K0, 0), impact B_IMP."""
    E = np.sqrt((2 * T_HOP * K0) ** 2 + bare_mass ** 2)
    v_dirac = np.array([2 * T_HOP * K0 + bare_mass, E])
    v_dirac /= np.linalg.norm(v_dirac)
    psi = np.zeros((LX, LY, 2), dtype=complex)
    x0, y0 = 10, LY // 2 + B_IMP
    sx_, sy_ = 6.0, 3.0
    for x in range(LX):
        for y in range(LY):
            env = np.exp(-((x - x0) ** 2) / (2 * sx_ ** 2)
                         - ((y - y0) ** 2) / (2 * sy_ ** 2))
            psi[x, y, :] = env * np.exp(1j * K0 * x) * v_dirac
    psi = psi.reshape(-1)
    return psi / np.linalg.norm(psi)

def deflection(h, bare_mass, T):
    psi0 = wavepacket(bare_mass)
    psiT = expm_multiply(-1j * h * T, psi0).reshape(LX, LY, 2)
    py = 0.0
    for y in range(1, LY - 1):
        d = (psiT[:, y + 1, :] - psiT[:, y - 1, :]) / 2.0
        py += np.vdot(psiT[:, y, :].reshape(-1),
                      (-1j * d).reshape(-1)).real
    return py / K0

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
Phi = profile()
print("=" * 78)
print("DIRAC-MALAMENT CHECK -- cones vs scale, null vs massive")
print("=" * 78)
print()

T = 0.9 * LX / CONE
h_c = build_h(Phi, cone_mod=EPS)
h_m = build_h(Phi, mass_mod=EPS)
h_c_flip = build_h(Phi, cone_mod=-EPS)

th_null_c = deflection(h_c, 0.0, T)
th_null_m = deflection(h_m, 0.0, T)
th_null_flip = deflection(h_c_flip, 0.0, T)
th_mass_c = deflection(build_h(Phi, cone_mod=EPS, bare_mass=M0), M0, T)
th_mass_m = deflection(build_h(Phi, mass_mod=EPS, bare_mass=M0), M0, T)

print(f"null probe:    theta(cone-def) = {th_null_c:+.6f}   "
      f"theta(mass-def) = {th_null_m:+.6f}   "
      f"theta(flipped) = {th_null_flip:+.6f}")
print(f"massive probe: theta(cone-def) = {th_mass_c:+.6f}   "
      f"theta(mass-def) = {th_mass_m:+.6f}")
print()

# -----------------------------------------------------------------------------
# B3: the 2:1 profile (scored only if B1 passes)
# -----------------------------------------------------------------------------
b1_pass = abs(th_null_m) < 0.15 * abs(th_null_c)
profile_results = {}
if b1_pass:
    # GR-matched metric deformation: both faces, one profile
    h_metric = build_h(Phi, cone_mod=EPS, mass_mod=EPS)
    h_scale = build_h(Phi, mass_mod=EPS)
    v_fracs = [0.3, 0.5, 0.7, 0.9]
    # velocity tuning via bare mass: v = 2tK0/sqrt((2tK0)^2 + m^2)
    print("B3 profile run (metric vs scale-only):")
    rows = []
    for vf in v_fracs:
        m_bare = 2 * T_HOP * K0 * np.sqrt(1 / vf ** 2 - 1)
        T_v = 0.9 * LX / (vf * CONE)
        th_met = deflection(build_h(Phi, cone_mod=EPS, mass_mod=EPS,
                                    bare_mass=m_bare), m_bare, T_v)
        th_scl = deflection(build_h(Phi, mass_mod=EPS,
                                    bare_mass=m_bare), m_bare, T_v)
        rows.append((vf, th_met, th_scl))
        print(f"  v={vf:.1f}c: theta_metric = {th_met:+.6f}, "
              f"theta_scale = {th_scl:+.6f}, "
              f"ratio = {abs(th_met / th_scl) if abs(th_scl) > 1e-9 else float('nan'):.3f}")
    v2 = np.array(v_fracs) ** 2
    y = np.abs([r[1] for r in rows]) * v2
    A_mat = np.vstack([np.ones_like(v2), v2]).T
    coef, *_ = np.linalg.lstsq(A_mat, y, rcond=None)
    alpha = coef[1] / coef[0] if abs(coef[0]) > 1e-12 else np.nan
    ratio_cone = abs(rows[-1][1] / rows[-1][2])
    profile_results = {"alpha": alpha, "ratio_cone": ratio_cone}
    print(f"  alpha = {alpha:.2f} (bar 1 +/- 0.4), "
          f"cone ratio = {ratio_cone:.2f} (bar [1.6, 2.4])")
    print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("B1 (FIRST BAR): null blind to pure-scale deformation",
     b1_pass,
     f"|{th_null_m:.2e}| < 0.15*|{th_null_c:.2e}| = "
     f"{0.15 * abs(th_null_c):.2e}"),
    ("B2: massive probe reads the scale (> 3x null)",
     abs(th_mass_m) > 3 * abs(th_null_m),
     f"{abs(th_mass_m):.2e} vs {abs(th_null_m):.2e}"),
    ("B4: flipped deformation flips the sign",
     th_null_c * th_null_flip < 0,
     f"{th_null_c:+.2e} vs {th_null_flip:+.2e}"),
]
if b1_pass and profile_results:
    checks.append(("B3a: alpha = 1 +/- 0.4",
                   abs(profile_results["alpha"] - 1.0) < 0.4,
                   f"{profile_results['alpha']:.2f}"))
    checks.append(("B3b: cone ratio in [1.6, 2.4]",
                   1.6 < profile_results["ratio_cone"] < 2.4,
                   f"{profile_results['ratio_cone']:.2f}"))
else:
    checks.append(("B3: not scored (B1 failed)", False, "blocked"))
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
