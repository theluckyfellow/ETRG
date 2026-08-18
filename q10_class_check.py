#!/usr/bin/env python3
"""
Q10-over-the-class check (round 7, item 3): does the dephasing lemma hold for
a TWO-INTERVAL region -- a non-contiguous member of the modular-local class?

The round-7 note claims Q10 is the exact-locality limit of P-select, i.e. one
modular generator serves the whole geometric class (unions of intervals).
The cheap, decisive test: rerun the Q10 dephasing lemma (q10_lattice_check.py)
with the region replaced by two disjoint intervals.  If coarse-graining in the
unperturbed modular basis still preserves the first law (ratio -> 1) while the
site basis fails, the lemma -- and the generator -- extends over the class.

Protocol identical to q10_lattice_check.py: free-fermion chain, filling 0.4,
smooth Gaussian potential perturbation, sweep eps, compare coarse/fine
entropy responses in modular vs site basis.
"""

import numpy as np

# -----------------------------------------------------------------------------
# Parameters (identical to q10_lattice_check.py except the region)
# -----------------------------------------------------------------------------
L = 200
N = 2 * L // 5          # filling 0.4 (away from half filling: PH symmetry
                        # would kill the first-order response)
A_size = 40
# Two disjoint blocks of 20, symmetric about the chain center
A1 = np.arange(60, 80)
A2 = np.arange(120, 140)
A_sites = np.concatenate([A1, A2])

eps_min = 1e-6
eps_max = 1e-1
num_eps = 35
i0 = A1[0]              # Gaussian centered at the left edge of block 1
w = 5.0
clip = 1e-15

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def dh_dn(n):
    n = np.clip(n, clip, 1.0 - clip)
    return np.log((1.0 - n) / n)

def ground_state_correlation(h):
    eigvals, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj()

# -----------------------------------------------------------------------------
# Free-fermion chain, open boundaries
# -----------------------------------------------------------------------------
h0 = np.zeros((L, L))
for i in range(L - 1):
    h0[i, i + 1] = h0[i + 1, i] = -0.5

v = np.exp(-(((np.arange(L) - i0) / w) ** 2))

C0_full = ground_state_correlation(h0)
C_A0 = C0_full[np.ix_(A_sites, A_sites)]

n_k, U = np.linalg.eigh(C_A0)

S0_fine = np.sum(binary_entropy(n_k))
S0_mod = np.sum(binary_entropy(np.diag(U.T @ C_A0 @ U)))
S0_site = np.sum(binary_entropy(np.diag(C_A0)))

xi_k = dh_dn(n_k)

# -----------------------------------------------------------------------------
# Sweep epsilon
# -----------------------------------------------------------------------------
epsilons = np.logspace(np.log10(eps_min), np.log10(eps_max), num_eps)

S_fine, S_mod, S_site, pairing = [], [], [], []

for eps in epsilons:
    C_eps_full = ground_state_correlation(h0 + eps * np.diag(v))
    C_Aeps = C_eps_full[np.ix_(A_sites, A_sites)]

    lam = np.clip(np.linalg.eigvalsh(C_Aeps), clip, 1.0 - clip)
    S_fine.append(np.sum(binary_entropy(lam)))

    C_mod = U.T @ C_Aeps @ U
    S_mod.append(np.sum(binary_entropy(np.diag(C_mod))))

    S_site.append(np.sum(binary_entropy(np.diag(C_Aeps))))

    dC = C_Aeps - C_A0
    pairing.append(np.sum(xi_k * np.diag(U.T @ dC @ U)))

S_fine = np.array(S_fine)
S_mod = np.array(S_mod)
S_site = np.array(S_site)
pairing = np.array(pairing)

dS_fine = S_fine - S0_fine
dS_mod = S_mod - S0_mod
dS_site = S_site - S0_site
residual = dS_mod - dS_fine

def loglog_slope(x, y, mask=None):
    if mask is None:
        mask = np.ones_like(x, dtype=bool)
    lx = np.log10(x[mask])
    ly = np.log10(np.abs(y[mask]))
    return np.polyfit(lx, ly, 1)[0]

small_mask = epsilons <= 1e-2
slope_resid = loglog_slope(epsilons, np.abs(residual), mask=small_mask)

ratio_mod = dS_mod / dS_fine
ratio_site = dS_site / dS_fine
pairing_ratio = pairing / dS_fine

# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------
print("=" * 75)
print("Q10-over-the-class: dephasing lemma on a TWO-INTERVAL region")
print("=" * 75)
print(f"Chain L = {L}, filling N = {N}")
print(f"Region A: sites {A1[0]}..{A1[-1]} UNION {A2[0]}..{A2[-1]} "
      f"(size {A_size}, non-contiguous)")
print(f"Perturbation: Gaussian onsite potential centered at i0={i0}, w={w}")
print()
print("Baseline entropies at eps=0:")
print(f"  S_A(0)    = {S0_fine:.10f}")
print(f"  S_mod(0)  = {S0_mod:.10f}")
print(f"  S_site(0) = {S0_site:.10f}")
print()
print("Smallest-eps data point:")
print(f"  eps            = {epsilons[0]:.3e}")
print(f"  pairing/dS_A   = {pairing_ratio[0]:.6f}  (predicted 1.0)")
print(f"  ratio_mod      = {ratio_mod[0]:.6f}  (predicted 1.0)")
print(f"  ratio_site     = {ratio_site[0]:.6f}  (predicted != 1.0)")
print(f"  residual slope = {slope_resid:.4f}  (predicted 2.0)")
print()
print("(Contiguous control, q10_lattice_check.py: ratio_mod 0.99992, "
      "ratio_site 4.216, slope 2.000)")
print()

# -----------------------------------------------------------------------------
# PASS / FAIL adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 60)
tols = {"mod_ratio": 0.05, "site_ratio": 0.05, "residual_slope": 0.2}
checks = [
    ("first law: pairing/dS_A -> 1",
     abs(pairing_ratio[0] - 1.0) < tols["mod_ratio"],
     f"{pairing_ratio[0]:.5f}"),
    ("coarse-modular ratio -> 1 (lemma extends over the class)",
     abs(ratio_mod[0] - 1.0) < tols["mod_ratio"], f"{ratio_mod[0]:.5f}"),
    ("coarse-site ratio != 1 (site basis still fails)",
     abs(ratio_site[0] - 1.0) > tols["site_ratio"], f"{ratio_site[0]:.5f}"),
    ("|S_mod - S_A| slope -> 2",
     abs(slope_resid - 2.0) < tols["residual_slope"], f"{slope_resid:.4f}"),
]
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print("-" * 60)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
