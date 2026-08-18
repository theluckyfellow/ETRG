#!/usr/bin/env python3
"""
Geodesic bending check (the clean B3) -- PRE-REGISTERED.

The wave-packet B3 failed three times (Schroedinger dispersion, Dirac sign
bug, KG massive-probe subtleties).  The eikonal content of those
simulations is just geodesic motion -- so integrate the geodesics
directly.  Background (static, isotropic, attractive):

    ds^2 = -N(x)^2 dt^2 + Psi(x)^2 (dx^2 + dy^2),
    N = 1 - eps*Phi,  Psi = 1 + eps*Phi   (weak-field GR form)

Null rays (kappa = 0) and timelike rays (kappa = 1, velocity v) launched
at impact parameter b past a Gaussian bump.  GR predicts

    theta(v) = theta_N (1 + v^2/c^2)   =>   theta_null/theta(v) = 2/(1+v^2/c^2)

PRE-REGISTERED BARS (corrected in flight, documented):
The first version of this script registered an algebraically INVERTED
prediction (2/(1+v^2/c^2)) and an impossible slow-ray bar; the measurements
matched the repo's own A5 formula all along.  The bars below are the
corrected ones, from A5: alpha_defl = (2GM/b)(1/v^2 + 1/c^2), hence
theta_null/theta(v) = 2v^2/(v^2+c^2).  (Referee F3: the honest label is
"PASS 4/4, bars corrected in-flight from the repo's A5.")

  G1  ratio theta_null/theta(v) matches 2v^2/(v^2+c^2) within 15% at
      v = 0.5c, 0.77c, 0.9c.
  G2  slow-ray ratio converges to A5 in the linear regime (EPS -> 0);
      the EPS = 0.05 value is nonlinear-regime (verified by the
      convergence run COMMITTED at the end of this script).
  G3  integrator validation (referee F4: with N = Psi the metric is
      conformally flat, so null-ray straightness is an exact IDENTITY,
      not a lattice test): pure-scale deformation bends null < 5% of cone.
  G4  sign control: flipped potential flips the deflection sign.
"""

import numpy as np
from scipy.integrate import solve_ivp

EPS = 0.05
W = 12.0
B_IMP = 30.0
X0, X1 = -150.0, 150.0

def Phi(x, y):
    return np.exp(-(x ** 2 + y ** 2) / (2 * W ** 2))

def fields(x, y, kind):
    p = Phi(x, y)
    if kind == "metric":
        return 1 - EPS * p, 1 + EPS * p
    if kind == "metric_flip":
        return 1 + EPS * p, 1 - EPS * p
    if kind == "cone":
        return 1 - EPS * p, np.ones_like(p)
    if kind == "scale":
        # c = N/Psi fixed at 1: N = Psi
        return 1 + EPS * p, 1 + EPS * p
    raise ValueError(kind)

def geodesic_rhs(lam, state, kind):
    t, x, y, ut, ux, uy = state
    N, Psi = fields(x, y, kind)
    h = 1e-5
    Nx = (fields(x + h, y, kind)[0] - fields(x - h, y, kind)[0]) / (2 * h)
    Ny = (fields(x, y + h, kind)[0] - fields(x, y - h, kind)[0]) / (2 * h)
    Px = (fields(x + h, y, kind)[1] - fields(x - h, y, kind)[1]) / (2 * h)
    Py = (fields(x, y + h, kind)[1] - fields(x, y - h, kind)[1]) / (2 * h)
    # Christoffels for ds^2 = -N^2 dt^2 + Psi^2 (dx^2 + dy^2)
    dut = -(2 * Nx / N) * ut * ux - (2 * Ny / N) * ut * uy
    dux = -(N * Nx / Psi ** 2) * ut ** 2 \
        - (Px / Psi) * (ux ** 2 - uy ** 2) - 2 * (Py / Psi) * ux * uy
    duy = -(N * Ny / Psi ** 2) * ut ** 2 \
        - (Py / Psi) * (uy ** 2 - ux ** 2) - 2 * (Px / Psi) * ux * uy
    return [ut, ux, uy, dut, dux, duy]

def bend(v, kind):
    """Deflection angle for a ray at physical velocity v (v=1: null).
    Integrates until x >= X1 (event), no fixed-time cutoff (the first
    version's 400-unit window stranded the slow rays mid-flight)."""
    y0 = B_IMP
    if v >= 1.0:                      # null, kappa = 0
        ut0, ux0, uy0 = 1.0, 1.0, 0.0
    else:                             # timelike, kappa = 1
        gv = 1 / np.sqrt(1 - v ** 2)
        ut0, ux0, uy0 = gv, gv * v, 0.0
    state0 = [0.0, X0, y0, ut0, ux0, uy0]

    def event(lam, s, *args):
        return s[1] - X1
    event.terminal = True
    # max_step is load-bearing: without it the adaptive solver steps clean
    # OVER the bump for slow rays (nfev=50, uy frozen at machine zero) --
    # diagnosed by direct comparison against Euler integration.
    sol = solve_ivp(geodesic_rhs, [0, 5000], state0, args=(kind,),
                    events=event, rtol=1e-9, atol=1e-12, max_step=5.0)
    s = sol.y[:, -1]
    return s[5] / s[4]

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 72)
print("GEODESIC BENDING CHECK -- the clean (1 + v^2/c^2) profile")
print("=" * 72)
print()

th_null = bend(1.0, "metric")
print(f"null deflection (metric):        {th_null:+.6f}")
rows = []
for v in [0.3, 0.5, 0.77, 0.9]:
    th_v = bend(v, "metric")
    ratio = th_null / th_v
    # CORRECTED prediction (the first version's formula was algebraically
    # inverted): the repo's own A5 gives alpha_defl = (2GM/b)(1/v^2+1/c^2),
    # so theta_null/theta(v) = 2v^2/(v^2+c^2).  The measured ratios matched
    # THIS formula to ~5% even before the correction.
    pred = 2 * v ** 2 / (v ** 2 + 1)
    rows.append((v, th_v, ratio, pred))
    print(f"v = {v:.2f}c: theta = {th_v:+.6f}   null/theta(v) = {ratio:.3f} "
          f"  A5 pred {pred:.3f}")
print()
# G2 regime note: at EPS = 0.05 the v=0.3c deflection is ~0.21 rad, beyond
# the linear regime the A5 formula describes.  The supplementary
# convergence run is COMMITTED below (referee F3 provenance fix).

# -----------------------------------------------------------------------------
# G2 supplementary: EPS convergence of the slow-ray ratio (committed run)
# -----------------------------------------------------------------------------
print("G2 supplementary (slow ray, perturbative regime; committed):")
g2_rows = []
EPS_MAIN = EPS
for eps_low in [0.05, 0.02, 0.01]:
    EPS = eps_low
    tn = bend(1.0, "metric")
    t3 = bend(0.3, "metric")
    g2_rows.append((eps_low, tn / t3))
    print(f"  EPS={eps_low}: ratio {tn / t3:.4f}   (A5 pred 0.165)")
EPS = EPS_MAIN
print()

th_cone = bend(1.0, "cone")
th_scale = bend(1.0, "scale")
th_flip = bend(1.0, "metric_flip")
print(f"Malament: theta(cone) = {th_cone:+.6f}, "
      f"theta(scale) = {th_scale:+.6f}")
print(f"sign control: theta(flip) = {th_flip:+.6f}")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
g1 = all(abs(r / p - 1) < 0.15 for _, _, r, p in rows[1:])
g2_measured = g2_rows[-1][1]   # EPS=0.01, committed convergence run above
g2 = abs(g2_measured / 0.165 - 1) < 0.15
checks = [
    ("G1: ratios match A5's 2v^2/(v^2+c^2) within 15% (v=0.5,0.77,0.9)",
     g1, "; ".join(f"{r:.2f}/{p:.2f}" for _, _, r, p in rows[1:])),
    ("G2: slow-ray ratio converges to A5 in the linear regime (EPS->0)",
     g2, f"{g2_measured:.3f} vs 0.165 at EPS=0.01 "
     f"({g2_rows[0][1]:.3f} at EPS=0.05, nonlinear)"),
    ("G3 (Malament): scale deformation bends null < 5% of cone",
     abs(th_scale) < 0.05 * abs(th_cone),
     f"{abs(th_scale):.2e} vs {abs(th_cone):.2e}"),
    ("G4: flipped potential flips the sign",
     th_null * th_flip < 0, f"{th_null:+.2e} vs {th_flip:+.2e}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<54s}  {value}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
