#!/usr/bin/env python3
"""
Referee verification for the Route-B batch (Fable, 2026-08-17).

Three independent checks:

PART 1 -- The structure question (mi_decomposition_check D1).
  Claim under test: "the equal-time MI geometry encodes the scale face
  only; the cone face lives in the dynamics."  Counter-hypothesis
  (inhomogeneous-CFT, Dubail-Stephan-Viti-Calabrese 2017): the ground
  state of a chain with varying hopping IS a curved-space CFT vacuum,
  and interval entropies read the CONFORMAL cone distance
      d_conf(x1,x2) = sum 1/v_F(x),   v_F(x) = 2 t(x) sin(pi n(x)),
  so   Delta S(interval) = (1/3) Delta ln d_conf   for intervals whose
  endpoints sit outside the deformation.  If that prediction fits, the
  static state DOES carry a cone face -- the dressed (v_F) cone -- and
  D1 failed because (a) its predictor saturates over the pair sample and
  (b) -ln(nearest-neighbor MI) graph distance is the wrong observable.
  Central differencing (+eps vs -eps) per the fss_q10 lesson.

PART 2 -- spacetime_malament sign anomaly.
  In the committed results, metric-null deflection (+0.046) has the
  OPPOSITE sign to cone-null (-0.016), though null rays read only
  c = N/Psi and metric is cone+scale with c ~ 1 - 2 eps Phi (same sign,
  ~2x magnitude expected).  Hypothesis: EPS = 0.35 puts the metric run
  in the strong-field regime (c dips to 0.3; focus/caustic crossing).
  Test: rerun cone & metric null at EPS = 0.10.

PART 3 -- geodesic G2 provenance.
  The committed script scores G2 on a hard-coded 0.160 attributed to an
  uncommitted EPS=0.01 run.  Reproduce it here (EPS = 0.02 and 0.01).
"""

import numpy as np
from scipy.integrate import solve_ivp

# =============================================================================
# PART 1: static state vs conformal cone distance
# =============================================================================
L = 200
FILL = 2 * L // 5
I0 = L // 2
W = 6.0
EPS = 0.3
EPS_P = 0.1239          # Kimi's debt-matched potential strength
CLIP = 1e-14
RS = list(range(5, 55, 5))

PhiArr = np.exp(-(((np.arange(L) - I0) / W) ** 2))

def hamiltonian(cone_mod=0.0, pot_mod=0.0):
    h = np.zeros((L, L))
    for i in range(L - 1):
        t = 0.5 * (1 - cone_mod * 0.5 * (PhiArr[i] + PhiArr[i + 1]))
        h[i, i + 1] = h[i + 1, i] = -t
    h += np.diag(pot_mod * PhiArr)
    return h

def correlation(h):
    _, V = np.linalg.eigh(h)
    occ = V[:, :FILL]
    return occ @ occ.T.conj()

def h_ent(n):
    n = np.clip(np.real(n), CLIP, 1 - CLIP)
    return -n * np.log(n) - (1 - n) * np.log(1 - n)

def S_interval(C, r):
    sites = list(range(I0 - r, I0 + r + 1))
    return float(np.sum(h_ent(np.linalg.eigvalsh(C[np.ix_(sites, sites)]))))

def t_site(cone_mod):
    """Site-averaged hopping field."""
    tb = np.array([0.5 * (1 - cone_mod * 0.5 * (PhiArr[i] + PhiArr[i + 1]))
                   for i in range(L - 1)])
    ts = np.empty(L)
    ts[0], ts[-1] = tb[0], tb[-1]
    ts[1:-1] = 0.5 * (tb[:-1] + tb[1:])
    return ts

def lda_density(cone_mod, pot_mod):
    """LDA filling n(x) at fixed total number: mu solves sum n = FILL."""
    ts = t_site(cone_mod)
    V = pot_mod * PhiArr
    def total(mu):
        arg = np.clip((V - mu) / (2 * ts), -1.0, 1.0)
        return np.sum(np.arccos(arg) / np.pi) - FILL
    lo, hi = -2.0, 2.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if total(mid) > 0:
            hi = mid
        else:
            lo = mid
    mu = 0.5 * (lo + hi)
    arg = np.clip((V - mu) / (2 * ts), -1.0, 1.0)
    return np.arccos(arg) / np.pi, ts

def d_conf(cone_mod, pot_mod, r, dressed=True):
    """Conformal cone distance across the interval [I0-r, I0+r]."""
    n, ts = lda_density(cone_mod, pot_mod)
    v = 2 * ts * (np.sin(np.pi * n) if dressed else 1.0)
    return float(np.sum(1.0 / v[I0 - r: I0 + r]))

def central_dS(kind):
    """(S(+eps) - S(-eps))/2 per interval, for one deformation type."""
    if kind == "cone":
        Cp = correlation(hamiltonian(cone_mod=+EPS))
        Cm = correlation(hamiltonian(cone_mod=-EPS))
    else:
        Cp = correlation(hamiltonian(pot_mod=+EPS_P))
        Cm = correlation(hamiltonian(pot_mod=-EPS_P))
    return np.array([(S_interval(Cp, r) - S_interval(Cm, r)) / 2 for r in RS])

def central_pred(kind, dressed):
    """(1/3)(ln d_conf(+eps) - ln d_conf(-eps))/2 per interval."""
    out = []
    for r in RS:
        if kind == "cone":
            dp = d_conf(+EPS, 0.0, r, dressed)
            dm = d_conf(-EPS, 0.0, r, dressed)
        else:
            dp = d_conf(0.0, +EPS_P, r, dressed)
            dm = d_conf(0.0, -EPS_P, r, dressed)
        out.append((np.log(dp) - np.log(dm)) / 2 / 3.0)
    return np.array(out)

def fit(y, x):
    r = float(np.corrcoef(y, x)[0, 1])
    slope = float(np.polyfit(x, y, 1)[0])
    return r, slope

print("=" * 78)
print("PART 1: does the STATIC state read the cone?  Interval entropy vs")
print("        conformal distance (inhomogeneous-CFT prediction)")
print("=" * 78)

# D1 predictor saturation, quantified
kimi_pred = np.array([d_conf(EPS, 0, r, dressed=False)
                      - d_conf(0, 0, r, dressed=False) for r in RS])
sat = kimi_pred / kimi_pred[-1]
print("\nD1's predictor (Delta cone distance) across its own pair sample,")
print("normalized to the r=50 value:")
print("  " + "  ".join(f"r={r}:{s:.4f}" for r, s in zip(RS, sat)))
n_same = int(np.sum(np.abs(sat - 1) < 0.001))
print(f"  -> {n_same}/{len(RS)} sample points identical to 0.1%: the Pearson")
print("     bar was scored against a saturated (near-constant) predictor.")

dS_cone = central_dS("cone")
dS_pot = central_dS("pot")
pred_cone_bare = central_pred("cone", dressed=False)
pred_cone_vF = central_pred("cone", dressed=True)
pred_pot_vF = central_pred("pot", dressed=True)

print("\nMeasured Delta S (central-differenced) vs (1/3) Delta ln d_conf:")
print(f"{'r':>4s} {'dS_cone':>10s} {'pred_vF':>10s} {'dS_pot':>10s} "
      f"{'pred_vF':>10s}")
for k, r in enumerate(RS):
    print(f"{r:>4d} {dS_cone[k]:>10.5f} {pred_cone_vF[k]:>10.5f} "
          f"{dS_pot[k]:>10.5f} {pred_pot_vF[k]:>10.5f}")

r_cb, s_cb = fit(dS_cone, pred_cone_bare)
r_cv, s_cv = fit(dS_cone, pred_cone_vF)
r_pv, s_pv = fit(dS_pot, pred_pot_vF)
print(f"\ncone deformation:  vs bare-c pred   r = {r_cb:+.4f}, slope {s_cb:+.3f}")
print(f"                   vs v_F pred      r = {r_cv:+.4f}, slope {s_cv:+.3f}")
print(f"potential (scale): vs v_F pred      r = {r_pv:+.4f}, slope {s_pv:+.3f}")
print("   (bare-c pred for the potential deformation is identically ZERO --")
print(f"    measured dS_pot is not: max |dS_pot| = {np.max(np.abs(dS_pot)):.4f})")

# =============================================================================
# PART 2: spacetime_malament metric-sign anomaly -- weak-field rerun
# =============================================================================
print()
print("=" * 78)
print("PART 2: wave-packet metric/cone sign consistency vs EPS")
print("=" * 78)

LX, LY = 160, 80
DX, DT = 1.0, 0.35
WW, B_IMP, C0 = 12.0, 14, 1.0
T_STEPS, X_MEAS = 340, 120
Xg, Yg = np.meshgrid(np.arange(LX), np.arange(LY), indexing='ij')
cxg, cyg = LX // 2, LY // 2
Phi2 = np.exp(-((Xg - cxg) ** 2 + (Yg - cyg) ** 2) / (2 * WW ** 2))

def fields2(kind, eps):
    if kind == "flat":
        return C0 * np.ones((LX, LY)), np.ones((LX, LY))
    if kind == "cone":
        return C0 * (1 - eps * Phi2), np.ones((LX, LY))
    if kind == "metric":
        return C0 * (1 - eps * Phi2), 1 + eps * Phi2
    raise ValueError(kind)

def grad_x(f):
    return (np.roll(f, -1, 0) - np.roll(f, 1, 0)) / (2 * DX)

def grad_y(f):
    return (np.roll(f, -1, 1) - np.roll(f, 1, 1)) / (2 * DX)

def lap(f):
    return (np.roll(f, 1, 0) + np.roll(f, -1, 0)
            + np.roll(f, 1, 1) + np.roll(f, -1, 1) - 4 * f) / DX ** 2

def run2(kind, eps):
    N, Psi = fields2(kind, eps)
    x0, y0 = 20, LY // 2 + B_IMP
    k0 = 0.6
    env = np.exp(-((Xg - x0) ** 2) / (2 * 6.0 ** 2)
                 - ((Yg - y0) ** 2) / (2 * 3.0 ** 2))
    phi = env * np.cos(k0 * Xg)
    phi_t = C0 * k0 * env * np.sin(k0 * Xg)
    edge = np.minimum.reduce([Xg, Yg, LX - 1 - Xg, LY - 1 - Yg])
    damp = np.clip((8 - edge) / 8, 0, 1) * 0.15
    Nx, Ny = grad_x(N), grad_y(N)
    for _ in range(T_STEPS):
        gx, gy = grad_x(phi), grad_y(phi)
        div = (Nx * gx + Ny * gy) + N * lap(phi)
        phi_t = (phi_t + DT * (N / Psi ** 2) * div) * (1 - damp)
        phi = phi + DT * phi_t
    w = np.abs(phi) ** 2
    w[:X_MEAS, :] = 0
    w[edge < 8] = 0
    tot = w.sum()
    return ((w * Yg).sum() / tot, (w * Xg).sum() / tot) if tot else (0., 0.)

def defl2(kind, eps):
    cy_d, cx_d = run2(kind, eps)
    cy_f, cx_f = run2("flat", eps)
    return (cy_d - cy_f) / max(cx_f - 20, 1.0)

for eps in (0.35, 0.10):
    tc = defl2("cone", eps)
    tm = defl2("metric", eps)
    consistent = tc * tm > 0
    print(f"EPS = {eps:.2f}: theta_cone = {tc:+.5f}  theta_metric = {tm:+.5f}"
          f"  ratio metric/cone = {tm / tc:+.2f}"
          f"  [{'consistent' if consistent else 'SIGN ANOMALY'}]"
          f"  (expected: same sign, ratio ~ +2)")

# =============================================================================
# PART 3: geodesic G2 hard-coded numbers -- reproduce
# =============================================================================
print()
print("=" * 78)
print("PART 3: geodesic G2 provenance (claimed 0.154 @ EPS=0.02, 0.160 @ 0.01)")
print("=" * 78)

WG, BG, X0G, X1G = 12.0, 30.0, -150.0, 150.0

def bend(v, eps):
    def flds(x, y):
        p = np.exp(-(x ** 2 + y ** 2) / (2 * WG ** 2))
        return 1 - eps * p, 1 + eps * p
    def rhs(lam, s):
        t, x, y, ut, ux, uy = s
        N, Psi = flds(x, y)
        h = 1e-5
        Nx = (flds(x + h, y)[0] - flds(x - h, y)[0]) / (2 * h)
        Ny = (flds(x, y + h)[0] - flds(x, y - h)[0]) / (2 * h)
        Px = (flds(x + h, y)[1] - flds(x - h, y)[1]) / (2 * h)
        Py = (flds(x, y + h)[1] - flds(x, y - h)[1]) / (2 * h)
        dut = -(2 * Nx / N) * ut * ux - (2 * Ny / N) * ut * uy
        dux = -(N * Nx / Psi ** 2) * ut ** 2 \
            - (Px / Psi) * (ux ** 2 - uy ** 2) - 2 * (Py / Psi) * ux * uy
        duy = -(N * Ny / Psi ** 2) * ut ** 2 \
            - (Py / Psi) * (uy ** 2 - ux ** 2) - 2 * (Px / Psi) * ux * uy
        return [ut, ux, uy, dut, dux, duy]
    if v >= 1.0:
        s0 = [0.0, X0G, BG, 1.0, 1.0, 0.0]
    else:
        gv = 1 / np.sqrt(1 - v ** 2)
        s0 = [0.0, X0G, BG, gv, gv * v, 0.0]
    def event(lam, s):
        return s[1] - X1G
    event.terminal = True
    sol = solve_ivp(rhs, [0, 5000], s0, events=event,
                    rtol=1e-9, atol=1e-12, max_step=5.0)
    s = sol.y[:, -1]
    return s[5] / s[4]

for eps, claimed in ((0.02, 0.154), (0.01, 0.160)):
    ratio = bend(1.0, eps) / bend(0.3, eps)
    ok = abs(ratio - claimed) < 0.005
    print(f"EPS = {eps:.2f}: ratio null/theta(0.3c) = {ratio:.4f}  "
          f"claimed {claimed:.3f}  [{'REPRODUCED' if ok else 'MISMATCH'}]"
          f"   (A5 linear prediction 0.165)")
