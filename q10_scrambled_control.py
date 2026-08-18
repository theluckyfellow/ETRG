#!/usr/bin/env python3
"""Reviewer control for q10_class_check.py: does the dephasing lemma ALSO pass
for a scrambled (random / even-odd) region?  If yes, the lemma is
region-agnostic and the two-interval PASS does not specifically support the
geometric class -- it supports "modular basis dephases for any region".
Protocol copied verbatim from q10_class_check.py except the region."""

import numpy as np

L = 200
N = 2 * L // 5
A_size = 40
eps_min, eps_max, num_eps = 1e-6, 1e-1, 35
w = 5.0
clip = 1e-15

rng = np.random.default_rng(11)

def binary_entropy(n):
    n = np.clip(n, clip, 1.0 - clip)
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def dh_dn(n):
    n = np.clip(n, clip, 1.0 - clip)
    return np.log((1.0 - n) / n)

h0 = np.zeros((L, L))
for i in range(L - 1):
    h0[i, i + 1] = h0[i + 1, i] = -0.5

def ground_state_correlation(h):
    _, eigvecs = np.linalg.eigh(h)
    occ = eigvecs[:, :N]
    return occ @ occ.T.conj()

def run(region_name, A_sites, i0):
    v = np.exp(-(((np.arange(L) - i0) / w) ** 2))
    C0 = ground_state_correlation(h0)[np.ix_(A_sites, A_sites)]
    n_k, U = np.linalg.eigh(C0)
    S0_fine = np.sum(binary_entropy(np.clip(n_k, clip, 1 - clip)))
    S0_mod = np.sum(binary_entropy(np.diag(U.T @ C0 @ U)))
    S0_site = np.sum(binary_entropy(np.diag(C0)))
    xi_k = dh_dn(n_k)

    epsilons = np.logspace(np.log10(eps_min), np.log10(eps_max), num_eps)
    S_fine, S_mod, S_site, pairing = [], [], [], []
    for eps in epsilons:
        C_e = ground_state_correlation(h0 + eps * np.diag(v))[np.ix_(A_sites, A_sites)]
        lam = np.clip(np.linalg.eigvalsh(C_e), clip, 1 - clip)
        S_fine.append(np.sum(binary_entropy(lam)))
        S_mod.append(np.sum(binary_entropy(np.diag(U.T @ C_e @ U))))
        S_site.append(np.sum(binary_entropy(np.diag(C_e))))
        pairing.append(np.sum(xi_k * np.diag(U.T @ (C_e - C0) @ U)))

    dS_fine = np.array(S_fine) - S0_fine
    dS_mod = np.array(S_mod) - S0_mod
    dS_site = np.array(S_site) - S0_site
    resid = np.abs(dS_mod - dS_fine)
    mask = epsilons <= 1e-2
    slope = np.polyfit(np.log10(epsilons[mask]), np.log10(resid[mask]), 1)[0]
    print(f"{region_name:>22s}: ratio_mod = {dS_mod[0]/dS_fine[0]:.6f}  "
          f"ratio_site = {dS_site[0]/dS_fine[0]:.4f}  slope = {slope:.4f}")

# Geometric (reproduces q10_class_check)
two_int = np.concatenate([np.arange(60, 80), np.arange(120, 140)])
run("two-interval (repro)", two_int, 60)

# Scrambled controls -- perturbation centered on a site IN the region
rand_region = np.sort(rng.choice(L, A_size, replace=False))
run("random region", rand_region, int(rand_region[0]))

even_odd = np.arange(60, 60 + 2 * A_size, 2)
run("even/odd (60..138)", even_odd, 60)
