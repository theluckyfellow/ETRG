#!/usr/bin/env python3
"""
Q10 lattice check: free-fermion chain, interval A, modular coarse-graining.

Verify predictions of ETRG-0_Q10_note.md:
  - Coarse-modular entropy S_mod uses the unperturbed modular-mode basis U.
  - Coarse-site entropy S_site uses the site basis.
  - Fine entropy S_A uses the full spectrum of C_A(eps).

Tests:
  1. (S_mod - S_mod(0)) / (S_A - S_A(0)) -> 1 as eps -> 0.
  2. (S_site - S_site(0)) / (S_A - S_A(0)) -> something != 1.
  3. log-log slope of |S_mod - S_A| vs eps -> 2 (second-order residual).
"""

import numpy as np

# -----------------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------------
L = 200
# Away from half filling: at half filling the hopping chain is particle-hole
# symmetric and a pure potential perturbation is PH-odd, so S(eps) = S(-eps)
# and the entire first-order response vanishes -- the round-2 run at N = L/2
# probed only the second-order regime and could not test the lemma.
N = 2 * L // 5          # filling 0.4
A_size = 40
A_start = (L - A_size) // 2
A = slice(A_start, A_start + A_size)

eps_min = 1e-6
eps_max = 1e-1
num_eps = 35
i0 = A_start            # Gaussian centered at the left edge of A
w = 5.0
clip = 1e-15

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def binary_entropy(n):
    """h(n) = -n log n - (1-n) log(1-n), with safe clipping."""
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def dh_dn(n):
    """Derivative of binary entropy: log((1-n)/n)."""
    n = np.clip(n, clip, 1.0 - clip)
    return np.log((1.0 - n) / n)

def ground_state_correlation(h):
    """h is a real symmetric LxL single-particle Hamiltonian.
    Returns the LxL correlation matrix C_ij = <c_i^+ c_j> for the Slater ground
    state of N fermions.
    """
    eigvals, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]        # N lowest single-particle orbitals
    return occ @ occ.T.conj()

# -----------------------------------------------------------------------------
# Free-fermion chain Hamiltonian
# H0 = -(1/2) sum_i (c_i^+ c_{i+1} + c_{i+1}^+ c_i), open boundaries
# -----------------------------------------------------------------------------
h0 = np.zeros((L, L), dtype=np.float64)
for i in range(L - 1):
    h0[i, i + 1] = -0.5
    h0[i + 1, i] = -0.5

# Smooth on-site perturbation potential, Gaussian localized near the left edge of A
v = np.exp(-(((np.arange(L) - i0) / w) ** 2))

# Ground state of the unperturbed Hamiltonian
C0_full = ground_state_correlation(h0)
C_A0 = C0_full[A, A]

# Diagonalize the restriction to get the modular modes at epsilon = 0
n_k, U = np.linalg.eigh(C_A0)
# eigh returns ascending order; n_k are in [0,1], symmetrized around 1/2 for a
# contiguous interval of a critical chain. Keep as is.

S0_fine = np.sum(binary_entropy(n_k))
S0_mod = np.sum(binary_entropy(np.diag(U.T @ C_A0 @ U)))   # should equal S0_fine
S0_site = np.sum(binary_entropy(np.diag(C_A0)))

# Modular first-law pairing weights
xi_k = dh_dn(n_k)                  # = modular eigenvalues of K_A

# -----------------------------------------------------------------------------
# Sweep epsilon
# -----------------------------------------------------------------------------
epsilons = np.logspace(np.log10(eps_min), np.log10(eps_max), num_eps)

S_fine = []
S_mod = []
S_site = []
pairing = []

for eps in epsilons:
    h_eps = h0 + eps * np.diag(v)
    C_eps_full = ground_state_correlation(h_eps)
    C_Aeps = C_eps_full[A, A]

    # Fine entropy: full spectrum of C_A(eps)
    lam = np.linalg.eigvalsh(C_Aeps)
    lam = np.clip(lam, clip, 1.0 - clip)
    S_fine.append(np.sum(binary_entropy(lam)))

    # Coarse-modular entropy: dephase in the unperturbed modular basis
    C_mod = U.T @ C_Aeps @ U
    n_mod = np.diag(C_mod)
    S_mod.append(np.sum(binary_entropy(n_mod)))

    # Coarse-site entropy: dephase in the site basis (just diagonal entries)
    n_site = np.diag(C_Aeps)
    S_site.append(np.sum(binary_entropy(n_site)))

    # First-law pairing: Tr[(C_Aeps - C_A0) * dS/dC at C_A0]
    dC = C_Aeps - C_A0
    delta_mod = U.T @ dC @ U
    pairing.append(np.sum(xi_k * np.diag(delta_mod)))

S_fine = np.array(S_fine)
S_mod = np.array(S_mod)
S_site = np.array(S_site)
pairing = np.array(pairing)

dS_fine = S_fine - S0_fine
dS_mod = S_mod - S0_mod
dS_site = S_site - S0_site
residual = dS_mod - dS_fine         # S_mod - S_A after subtracting equal S(0)

# -----------------------------------------------------------------------------
# Log-log analysis
# -----------------------------------------------------------------------------
def loglog_slope(x, y, mask=None):
    """Return slope and intercept from a least-squares fit to log10 data,
    restricted by a boolean mask if provided."""
    if mask is None:
        mask = np.ones_like(x, dtype=bool)
    lx = np.log10(x[mask])
    ly = np.log10(np.abs(y[mask]))
    slope, intercept = np.polyfit(lx, ly, 1)
    return slope, intercept

# Overall slopes over [eps_min, eps_max]
slope_fine, _ = loglog_slope(epsilons, dS_fine)
slope_mod, _ = loglog_slope(epsilons, dS_mod)
slope_site, _ = loglog_slope(epsilons, dS_site)

# Residual slope: use small-eps half to stay in perturbative regime
small_mask = epsilons <= 1e-2
slope_resid, _ = loglog_slope(epsilons, np.abs(residual), mask=small_mask)

# Ratios approaching eps -> 0
ratio_mod = dS_mod / dS_fine
ratio_site = dS_site / dS_fine

# Use lowest-eps data point as the limiting ratio.  We may still be in the crossover
# for extremely small eps if the first-order entropy change falls below numerical
# precision; inspect the output.
ratio_mod_limit = ratio_mod[0]
ratio_site_limit = ratio_site[0]

# Pairing / fine ratio at first order
pairing_ratio = pairing / dS_fine

# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------
print("=" * 75)
print("Q10 lattice check: modular coarse-graining for a perturbed free-fermion chain")
print("=" * 75)
print(f"Chain length L = {L}, half filling N = {N}")
print(f"Interval A: sites {A.start}..{A.stop - 1} (size {A_size})")
print(f"Perturbation: Gaussian onsite potential centered at i0={i0}, width w={w}")
print(f"Epsilon range: [{eps_min:.0e}, {eps_max:.0e}], {num_eps} log-spaced points")
print()
print("Baseline entropies at eps=0:")
print(f"  S_A(0)   = {S0_fine:.10f}")
print(f"  S_mod(0) = {S0_mod:.10f}")
print(f"  S_site(0)= {S0_site:.10f}")
print()

print("Log-log slopes of |delta S| vs epsilon (over full range):")
print(f"  fine  |dS_A/dln eps| slope = {slope_fine:.4f}")
print(f"  mod   |dS_mod/dln eps| slope = {slope_mod:.4f}")
print(f"  site  |dS_site/dln eps| slope = {slope_site:.4f}")
print()

print(f"Residual |S_mod - S_A| slope (eps <= 1e-2) = {slope_resid:.4f} (predicted 2.0)")
print()

print("Ratios (coarse/fine) as epsilon -> 0:")
print(f"  modular limit  = {ratio_mod_limit:.6f} (predicted 1.0)")
print(f"  site limit     = {ratio_site_limit:.6f} (predicted != 1.0)")
print()

print("Smallest-eps data point:")
print(f"  eps           = {epsilons[0]:.3e}")
print(f"  dS_A          = {dS_fine[0]:.6e}")
print(f"  dS_mod        = {dS_mod[0]:.6e}")
print(f"  dS_site       = {dS_site[0]:.6e}")
print(f"  pairing       = {pairing[0]:.6e}")
print(f"  pairing/dS_A  = {pairing_ratio[0]:.6f}")
print(f"  ratio_mod     = {ratio_mod[0]:.6f}")
print(f"  ratio_site    = {ratio_site[0]:.6f}")
print()

# Detailed table
print("Detailed sweep:")
print("-" * 95)
print(f"{'eps':>10s}  {'dS_A':>12s}  {'dS_mod':>12s}  {'dS_site':>12s}  "
      f"{'pairing':>12s}  {'r_mod':>8s}  {'r_site':>8s}")
print("-" * 95)
for i, eps in enumerate(epsilons):
    print(f"{eps:10.3e}  {dS_fine[i]:12.5e}  {dS_mod[i]:12.5e}  {dS_site[i]:12.5e}  "
          f"{pairing[i]:12.5e}  {ratio_mod[i]:8.5f}  {ratio_site[i]:8.5f}")
print("-" * 95)

# -----------------------------------------------------------------------------
# PASS/FAIL adjudication
# -----------------------------------------------------------------------------
print()
print("PASS / FAIL table:")
print("-" * 60)

tols = {
    "mod_ratio": 0.05,
    "site_ratio": 0.05,
    "residual_slope": 0.2,
}

pass_mod = abs(ratio_mod_limit - 1.0) < tols["mod_ratio"]
pass_site = abs(ratio_site_limit - 1.0) > tols["site_ratio"]
pass_resid = abs(slope_resid - 2.0) < tols["residual_slope"]
pass_firstlaw = abs(pairing_ratio[0] - 1.0) < tols["mod_ratio"]

results = [
    ("first law: pairing/dS_A -> 1", pass_firstlaw, f"{pairing_ratio[0]:.5f}"),
    ("coarse-modular ratio -> 1", pass_mod, f"{ratio_mod_limit:.5f}"),
    ("coarse-site ratio != 1", pass_site, f"{ratio_site_limit:.5f}"),
    ("|S_mod - S_A| slope -> 2", pass_resid, f"{slope_resid:.4f}"),
]

for desc, passed, value in results:
    status = "PASS" if passed else "FAIL"
    print(f"  {status:>5s}  {desc:<35s}  value = {value}")

print("-" * 60)

overall = "PASS" if all(r[1] for r in results) else "FAIL"
print(f"Overall: {overall}")
