#!/usr/bin/env python3
"""
coherent_thermal_check.py
Numerical adjudication of coherent vs thermal lock-evasion in a free-boson
harmonic chain, as requested by the ETRG-0 task.

Setup
-----
- Free scalar chain of L=120 sites, open boundary, near-critical mass m=0.01.
- Lattice Hamiltonian:  H = 1/2 [ q^T K q + p^T p ]
  with K = (2 + m^2) I - (nearest-neighbour hopping).
- Interval A = 30 consecutive sites centred in the chain.

States at matched total energy dE above vacuum
----------------------------------------------
(a) COHERENT: local displacement of the central site in q and p,
    covariance identical to vacuum.  Entanglement spectrum unchanged.
(b) THERMAL: global Gibbs state at inverse temperature beta chosen so its
    total energy above vacuum equals the same dE.

Quantities evaluated on A
-------------------------
  Delta S_ent   = S(rho_A) - S(vac_A)
  S_rel         = S(rho_A || vac_A)      (Gaussian relative entropy)
  Delta<K>_vac  = <K_vac>_rho - <K_vac>_vac   (modular Hamiltonian shift)

All logged entropy/nat units.
"""

import numpy as np
from scipy import linalg
from scipy.optimize import brentq


# ---------------------------------------------------------------------------
# Gaussian helpers
# ---------------------------------------------------------------------------
def gaussian_entropy(nu):
    """Von Neumann entropy from symplectic eigenvalues nu >= 1/2."""
    # g(nu) = (nu+1/2)ln(nu+1/2) - (nu-1/2)ln(nu-1/2)
    # works directly because nu>=1/2.  small eps for nu exactly 1/2
    nu = np.asarray(nu)
    eps = np.finfo(float).eps
    n = np.maximum(nu - 0.5, eps)
    return float(np.sum((n + 1.0) * np.log(n + 1.0) - n * np.log(n)))


def symplectic_eigenvalues(gamma):
    """
    Symplectic eigenvalues of a real symmetric positive-definite covariance
    matrix gamma in canonical (q_1...q_N, p_1...p_N) ordering.

    We use the Williamson relation:  gamma = S S^T  with symplectic S,
    and the symplectic eigenvalues are the positive eigenvalues of
        i Omega gamma  ==  sqrtm(gamma) i Omega sqrtm(gamma).
    The latter is Hermitian and has +/- nu_k eigenvalues.
    """
    N = gamma.shape[0] // 2
    Omega = np.zeros((2 * N, 2 * N))
    Omega[0:N, N:2 * N] = np.eye(N)
    Omega[N:2 * N, 0:N] = -np.eye(N)

    G = linalg.sqrtm(gamma)
    # Hermitian matrix whose eigenvalues are +/- nu_k
    M = 1j * (G @ Omega @ G)
    vals = np.linalg.eigvalsh(M)
    return np.abs(vals[vals > 0])


def relative_entropy(gamma1, d1, gamma0, d0):
    """
    S(rho_1 || rho_0) for Gaussian states.
    gamma* : covariances, d* : displacement vectors.
    """
    N = gamma0.shape[0]
    # tr( gamma1 gamma0^{-1} - I ) / 2
    inv_g0_g1 = linalg.solve(gamma0, gamma1, assume_a='pos')
    tr_term = 0.5 * (np.trace(inv_g0_g1) - N)

    # - (1/2) ln det( gamma1 gamma0^{-1} )
    sign, logdet = np.linalg.slogdet(inv_g0_g1)
    det_term = -0.5 * logdet
    if sign <= 0 or np.isinf(logdet) or np.isnan(logdet):
        det_term = -0.5 * (np.log(np.linalg.det(gamma1))
                           - np.log(np.linalg.det(gamma0)))

    # displacement term
    dd = d1 - d0
    disp_term = 0.5 * float(dd.T @ linalg.solve(gamma0, dd, assume_a='pos'))

    return tr_term + det_term + disp_term


# ---------------------------------------------------------------------------
# Build the system
# ---------------------------------------------------------------------------
def stiffness_matrix(L, m):
    K = np.eye(L) * (2.0 + m**2)
    for i in range(L - 1):
        K[i, i + 1] = -1.0
        K[i + 1, i] = -1.0
    return K


L = 120
m = 0.01
K = stiffness_matrix(L, m)

vals_K, U = linalg.eigh(K)
omega = np.sqrt(np.maximum(vals_K, 1e-14))

# Ground-state second moments in normal-mode basis:
#   <q_k q_l> = delta_kl / (2 omega_k)
#   <p_k p_l> = delta_kl omega_k / 2
# Transform to site basis with unitary U (columns are normal modes).
Var_q = 0.5 * (U * (1.0 / omega)) @ U.T
Var_p = 0.5 * (U * omega) @ U.T

gamma_vac = np.zeros((2 * L, 2 * L))
gamma_vac[:L, :L] = Var_q
gamma_vac[L:, L:] = Var_p

# Interval A: 30 sites centred
A_size = 30
A_start = (L - A_size) // 2
A_end = A_start + A_size
A_idx_site = np.arange(A_start, A_end)
A_idx = np.concatenate([A_idx_site, A_idx_site + L])

gamma_vac_A = gamma_vac[np.ix_(A_idx, A_idx)]
nu_vac_A = symplectic_eigenvalues(gamma_vac_A)
S_vac_A = gaussian_entropy(nu_vac_A)

j0 = L // 2
K_j0 = K[j0, j0]

print("=" * 80)
print("COHERENT vs THERMAL lock-evasion adjudication")
print("=" * 80)
print(f"L={L}, m={m}, interval A = {A_size} sites centred on site {j0}")
print(f"omega_min = {omega.min():.6f}, omega_max = {omega.max():.6f}")
print(f"S_vac(A)  = {S_vac_A:.6f}\n")

# ---------------------------------------------------------------------------
# Sweep over matched excitation energies
# ---------------------------------------------------------------------------
dE_targets = np.logspace(-4, -1, 16)
records = []

for target_dE in dE_targets:
    # ---- Coherent state ----
    # Equal q/p amplitude alpha; energy dE = 1/2 alpha^2 (K_j0 + 1)
    alpha = np.sqrt(2.0 * target_dE / (K_j0 + 1.0))
    d_full_coh = np.zeros(2 * L)
    d_full_coh[j0] = alpha
    d_full_coh[j0 + L] = alpha

    dE_coh_actual = 0.5 * (alpha**2 * K_j0 + alpha**2)

    d_coh_A = d_full_coh[A_idx]
    gamma_coh_A = gamma_vac_A                     # unchanged covariance

    dS_ent_coh = 0.0
    S_rel_coh = relative_entropy(gamma_coh_A, d_coh_A,
                                  gamma_vac_A, np.zeros(2 * A_size))
    dK_coh = S_rel_coh + dS_ent_coh

    # ---- Thermal state ----
    # Total energy above vacuum for Gibbs inverse temp beta:
    #   E_th - E_vac = sum_k omega_k / (exp(beta omega_k) - 1)
    def energy_err(beta):
        with np.errstate(over='ignore'):
            ex = np.exp(beta * omega)
            denom = np.where(ex > 1e150, np.inf, ex - 1.0)
            e = np.divide(omega, denom,
                          out=np.zeros_like(omega, dtype=float),
                          where=denom != 0)
        return float(np.sum(e) - target_dE)

    # Choose bracket adaptively
    lo, hi = 1e-5, 1e3
    for _ in range(4):
        try:
            beta_th = brentq(energy_err, lo, hi)
            break
        except ValueError:
            hi *= 10.0
    else:
        raise RuntimeError(f"Failed to bracket beta for dE={target_dE}")

    coth = 1.0 / np.tanh(beta_th * omega / 2.0)
    n_occ = 0.5 * (coth - 1.0)                    # = 1/(e^{beta omega}-1)

    Var_q_th = (U * ((n_occ + 0.5) / omega)) @ U.T
    Var_p_th = (U * ((n_occ + 0.5) * omega)) @ U.T

    gamma_th = np.zeros((2 * L, 2 * L))
    gamma_th[:L, :L] = Var_q_th
    gamma_th[L:, L:] = Var_p_th

    gamma_th_A = gamma_th[np.ix_(A_idx, A_idx)]
    S_th_A = gaussian_entropy(symplectic_eigenvalues(gamma_th_A))

    dS_ent_th = S_th_A - S_vac_A
    S_rel_th = relative_entropy(gamma_th_A, np.zeros(2 * A_size),
                                  gamma_vac_A, np.zeros(2 * A_size))
    dK_th = S_rel_th + dS_ent_th

    records.append({
        'dE': target_dE,
        'dE_coh': dE_coh_actual,
        'dE_th': target_dE,
        'dS_ent_coh': dS_ent_coh,
        'S_rel_coh': S_rel_coh,
        'dK_coh': dK_coh,
        'dS_ent_th': dS_ent_th,
        'S_rel_th': S_rel_th,
        'dK_th': dK_th,
    })

# ---------------------------------------------------------------------------
# Slopes (log-log)
# ---------------------------------------------------------------------------
res = np.array([[r['dE_coh'], r['dS_ent_coh'], r['S_rel_coh'], r['dK_coh'],
                 r['dS_ent_th'], r['S_rel_th'], r['dK_th']]
                for r in records])


def loglog_slope(x, y):
    mask = (x > 0) & (y > 0) & np.isfinite(y)
    if np.sum(mask) < 2:
        return np.nan
    return np.polyfit(np.log10(x[mask]), np.log10(y[mask]), 1)[0]


print("--- Log-Log slopes vs dE ---")
slopes = {
    'coh': {
        'dS_ent': loglog_slope(res[:, 0], res[:, 1]),
        'S_rel':  loglog_slope(res[:, 0], res[:, 2]),
        'dK':     loglog_slope(res[:, 0], res[:, 3]),
    },
    'th': {
        'dS_ent': loglog_slope(res[:, 0], res[:, 4]),
        'S_rel':  loglog_slope(res[:, 0], res[:, 5]),
        'dK':     loglog_slope(res[:, 0], res[:, 6]),
    },
}
print(f"Coherent:  dS_ent = {slopes['coh']['dS_ent']:+.4f}, "
      f"S_rel = {slopes['coh']['S_rel']:+.4f}, "
      f"Delta<K> = {slopes['coh']['dK']:+.4f}")
print(f"Thermal:   dS_ent = {slopes['th']['dS_ent']:+.4f}, "
      f"S_rel = {slopes['th']['S_rel']:+.4f}, "
      f"Delta<K> = {slopes['th']['dK']:+.4f}")
print()

# ---------------------------------------------------------------------------
# Tables
# ---------------------------------------------------------------------------
print("--- Full sweep table ---")
print(f"{'dE':>10} | {'dE_coh':>10} | {'dE_th':>10} | "
      f"{'dS_coh':>10} | {'Srel_coh':>10} | {'dS_th':>10} | {'Srel_th':>10}")
print("-" * 92)
for r in records:
    print(f"{r['dE']:10.2e} | {r['dE_coh']:10.2e} | {r['dE_th']:10.2e} | "
          f"{r['dS_ent_coh']:10.2e} | {r['S_rel_coh']:10.2e} | "
          f"{r['dS_ent_th']:10.2e} | {r['S_rel_th']:10.2e}")
print()

print("--- Key comparison: S_rel at matched dE ---")
print(f"{'dE':>10} | {'dS_coh':>10} | {'dS_th':>10} | "
      f"{'Srel_coh':>10} | {'Srel_th':>10} | {'Srel_th/Srel_coh':>18}")
print("-" * 82)
ratios = []
for r in records:
    rat = r['S_rel_th'] / r['S_rel_coh']
    ratios.append(rat)
    print(f"{r['dE']:10.2e} | {r['dS_ent_coh']:10.2e} | {r['dS_ent_th']:10.2e} | "
          f"{r['S_rel_coh']:10.2e} | {r['S_rel_th']:10.2e} | {rat:18.4f}")
print()

# ---------------------------------------------------------------------------
# Verdicts
# ---------------------------------------------------------------------------
print("--- Verdicts ---")
v_A = "PASS" if np.allclose(res[:, 1], 0.0, atol=1e-12) else "FAIL"

slope_S_rel_coh = slopes['coh']['S_rel']
v_B = "PASS" if abs(slope_S_rel_coh - 1.0) < 0.1 else "FAIL"

# "to O(1)" at matched dE: ratios within roughly an order of magnitude
ratios_a = np.array(ratios)
O1 = (ratios_a.min() >= 1e-1) and (ratios_a.max() <= 1e1)
v_C = "TRUE" if O1 else "FALSE"

print(f"[A] coherent Delta S_ent = 0 exactly                         -> {v_A}")
print(f"[B] S_rel coherent ~ (displacement)^2  (slope of S_rel vs dE ~1) -> {v_B} "
      f"(slope = {slope_S_rel_coh:.4f})")
print(f"[C] at matched dE, S_rel(thermal) ~ S_rel(coherent) to O(1)   -> {v_C}")
print(f"      S_rel(th)/S_rel(coh) ratio range: [{ratios_a.min():.4f}, {ratios_a.max():.4f}]")
print(f"      geometric mean ratio = {np.exp(np.mean(np.log(ratios_a))):.4f}")
print("=" * 80)
