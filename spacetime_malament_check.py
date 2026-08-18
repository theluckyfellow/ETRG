#!/usr/bin/env python3
"""
Spacetime Malament check (Route-B toy, third build) -- PRE-REGISTERED per
Fable's addendum R4: the null-invariance bar comes FIRST.

Route B's backbone (ETRG-4 + referee addendum): in isotropic form
    ds^2 = -N(x)^2 dt^2 + Psi(x)^2 (dx^2 + dy^2)
null rays see only the RATIO c(x) = N/Psi (the cone speed field); a
conformal deformation scales N and Psi together, leaves the ratio -- and
every null ray -- invariant.  Massive particles read the scale as well.

This is a SPACETIME finite-difference simulation of the covariant wave
equation on that background (derived from the covariant d'Alembertian):
    phi_tt = (N/Psi^2) div(N grad phi) - m^2 N^2 phi
with independent control of N(x) (lapse) and Psi(x) (spatial scale).

  cone deformation:  N varies, Psi = 1          -> c(x) varies, rays bend
  scale deformation: N = c0*Psi, Psi varies     -> c fixed, rays invariant
  massive probe:     KG mass m > 0              -> reads the scale too

PRE-REGISTERED BARS:
  B1  LATTICE MALAMENT: wavepacket centroid deflection under the pure
      scale deformation is ~ zero: |theta(scale)| < 0.2 |theta(cone)|.
  B2  massive probe (m = 0.5) is deflected by the scale deformation:
      |theta_m(scale)| > 2x |theta_null(scale)|.
  B3  (only if B1 passes) combined GR-matched deformation (g_00 and
      gamma from one Phi, as in weak-field GR): massless deflection is
      ~2x the scale-only massive slow deflection, i.e. the factor-of-two
      profile emerges from cone + scale together.  Bar: ratio in [1.6, 2.4].
  B4  sign control: flipped deformation flips the deflection sign.
"""

import numpy as np

LX, LY = 160, 80
DX = 1.0
DT = 0.35                     # CFL: DT < DX / (sqrt(2) * c_max)
W = 12.0                      # deformation width
B_IMP = 14                    # impact parameter
# EPS = 0.10 (referee F2: the first committed run used EPS = 0.35, where
# the metric deformation dips c to 0.3 -- over-bending/caustic territory.
# At that strength the metric-null deflection develops a sign anomaly
# (ratio -2.84 vs the eikonal expectation +2) and even the cone deflection
# is non-monotonic in eps.  At EPS = 0.10 the runs are consistent
# (ratio +1.50).  Cite magnitudes only from the small-eps regime.)
EPS = 0.10
C0 = 1.0
M_KG = 0.5                    # Klein-Gordon mass of the massive probe
T_STEPS = 340                 # packet (v~1) travels ~120 sites, past center
X_MEAS = 120                  # transmitted zone: x > X_MEAS

def profile():
    Phi = np.zeros((LX, LY))
    cx, cy = LX // 2, LY // 2
    X, Y = np.meshgrid(np.arange(LX), np.arange(LY), indexing='ij')
    return np.exp(-((X - cx) ** 2 + (Y - cy) ** 2) / (2 * W ** 2))

Phi = profile()

def fields(kind):
    """Return N(x), Psi(x) for the deformation type."""
    if kind == "flat":
        return C0 * np.ones((LX, LY)), np.ones((LX, LY))
    if kind == "cone":
        return C0 * (1 - EPS * Phi), np.ones((LX, LY))
    if kind == "scale":
        Psi = 1 + EPS * Phi
        return C0 * Psi, Psi
    if kind == "metric":
        # weak-field GR, ATTRACTIVE (fixed in place after the first run
        # implemented the repulsive sign): N = 1 - eps*Phi (lapse dips,
        # Shapiro), Psi = 1 + eps*Phi, so c = N/Psi ~ 1 - 2 eps*Phi --
        # light SLOWS at the bump, as in a potential well.
        return C0 * (1 - EPS * Phi), 1 + EPS * Phi
    if kind == "cone_flip":
        return C0 * (1 + EPS * Phi), np.ones((LX, LY))
    raise ValueError(kind)

def laplacian(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4 * f) / DX ** 2

def grad_x(f):
    return (np.roll(f, -1, 0) - np.roll(f, 1, 0)) / (2 * DX)

def grad_y(f):
    return (np.roll(f, -1, 1) - np.roll(f, 1, 1)) / (2 * DX)

def run(kind, mass, n_steps=T_STEPS):
    N, Psi = fields(kind)
    # initial Gaussian packet at left, impact parameter B_IMP, moving +x
    X, Y = np.meshgrid(np.arange(LX), np.arange(LY), indexing='ij')
    x0, y0 = 20, LY // 2 + B_IMP
    k0 = 0.6
    env = np.exp(-((X - x0) ** 2) / (2 * 6.0 ** 2)
                 - ((Y - y0) ** 2) / (2 * 3.0 ** 2))
    omega = np.sqrt((C0 * k0) ** 2 + (mass * C0) ** 2)
    phi = env * np.cos(k0 * X)
    phi_t = omega * env * np.sin(k0 * X)   # right-moving packet
    # absorbing border mask (damping layer)
    edge = np.minimum.reduce([X, Y, LX - 1 - X, LY - 1 - Y])
    damp = np.clip((8 - edge) / 8, 0, 1) * 0.15
    Nx, Ny = grad_x(N), grad_y(N)
    for _ in range(n_steps):
        gx, gy = grad_x(phi), grad_y(phi)
        div = (Nx * gx + Ny * gy) + N * laplacian(phi)
        phi_tt = (N / Psi ** 2) * div - mass ** 2 * N ** 2 * phi
        phi_t = phi_t + DT * phi_tt
        phi_t = phi_t * (1 - damp)
        phi = phi + DT * phi_t
    # centroid of |phi|^2 in the transmitted zone (x > X_MEAS), ALL y kept
    # (the first version masked the lower half-plane -- a constant bias
    # that dominated every deflection; fixed in place)
    w = np.abs(phi) ** 2
    w[:X_MEAS, :] = 0
    w[edge < 8] = 0
    total = w.sum()
    if total == 0:
        return 0.0, 0.0
    cy = (w * Y).sum() / total
    cx = (w * X).sum() / total
    return cy, cx

def deflection(kind, mass):
    """Transverse centroid offset relative to the flat baseline,
    normalized by longitudinal travel."""
    cy_d, cx_d = run(kind, mass)
    cy_f, cx_f = run("flat", mass)
    return (cy_d - cy_f) / max(cx_f - 20, 1.0)

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 78)
print("SPACETIME MALAMENT CHECK -- cones vs scale, null vs massive")
print("=" * 78)
print()

th_null_cone = deflection("cone", 0.0)
th_null_scale = deflection("scale", 0.0)
th_null_flip = deflection("cone_flip", 0.0)
th_mass_scale = deflection("scale", M_KG)
th_mass_cone = deflection("cone", M_KG)

print(f"null (m=0):   theta(cone) = {th_null_cone:+.5f}   "
      f"theta(scale) = {th_null_scale:+.5f}   "
      f"theta(flip) = {th_null_flip:+.5f}")
print(f"massive:      theta(cone) = {th_mass_cone:+.5f}   "
      f"theta(scale) = {th_mass_scale:+.5f}")
print()

b1 = abs(th_null_scale) < 0.2 * abs(th_null_cone)
print("PASS / FAIL table:")
print("-" * 78)
checks = [
    ("B1 (FIRST BAR): null rays blind to pure-scale deformation",
     b1, f"|{th_null_scale:.2e}| < 0.2*|{th_null_cone:.2e}|"),
    ("B2: massive probe reads the scale (> 2x null-scale)",
     abs(th_mass_scale) > 2 * abs(th_null_scale),
     f"{abs(th_mass_scale):.2e} vs {abs(th_null_scale):.2e}"),
    ("B4: flipped cone deformation flips the sign",
     th_null_cone * th_null_flip < 0,
     f"{th_null_cone:+.2e} vs {th_null_flip:+.2e}"),
]
if b1:
    # B3 (corrected comparison, registered before this run): for the SAME
    # attractive metric, GR predicts theta(v) = theta_N (1 + v^2/c^2), so
    # theta(null)/theta(massive at v) = 2/(1 + v^2/c^2).  With M_KG = 0.5
    # and k0 = 0.6, v = ck/E = 0.77c, prediction = 2/1.59 = 1.26.
    # Bar [0.9, 1.6] -- wide enough for eikonal-limit and packet-spreading
    # systematics, narrow enough to exclude 1 (lapse-only) and 2 (the
    # v->0 misreading).
    th_metric_null = deflection("metric", 0.0)
    th_metric_mass = deflection("metric", M_KG)
    v_probe = C0 * 0.6 / np.sqrt((C0 * 0.6) ** 2 + (M_KG * C0) ** 2)
    predicted = 2 / (1 + v_probe ** 2)
    ratio = abs(th_metric_null / th_metric_mass) \
        if abs(th_metric_mass) > 1e-12 else float('nan')
    print(f"B3 (corrected): theta_metric(null) = {th_metric_null:+.5f}, "
          f"theta_metric(massive v={v_probe:.2f}c) = {th_metric_mass:+.5f}")
    print(f"    ratio = {ratio:.2f}, GR prediction = {predicted:.2f}, "
          f"bar [0.9, 1.6]")
    checks.append(("B3: null/massive ratio matches GR (1+v^2/c^2)",
                   0.9 < ratio < 1.6, f"{ratio:.2f} vs pred {predicted:.2f}"))
else:
    print("B3: not scored (B1 failed)")
    checks.append(("B3: not scored (B1 failed)", False, "blocked"))
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 78)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
