#!/usr/bin/env python3
"""
Interacting drift check (round 8) -- PRE-REGISTERED.

drift_check.py established that eta = ||[K_A, h0]|| / (||K_A|| ||h0||)
discriminates geometric from scrambled regions for FREE fermions, with
growing separation.  interacting_locality_check.py (K5) established that
quasi-locality of K_A survives interactions.  This check welds the two:
does the DRIFT discrimination survive interactions?

System: XXZ chain, L = 14, open boundaries, exact diagonalization in the
Sz = 0 sector (dim 3432), Delta = 1 (critical) and Delta = 2 (gapped).
K_A = -ln rho_A from the full (non-Gaussian) reduced density matrix,
embedded as K_A (x) Identity on the complement.  eta is the normalized
commutator with the FULL physical Hamiltonian -- the same metric as
drift_check.py, boundary leakage included.

PRE-REGISTERED PREDICTIONS:
  P1  Delta = 1: eta(contiguous) beats every scrambled rival by > 2x
      (smaller system than the free case -- less headroom, honest bar).
  P2  Delta = 2: same.
  P3  Haar-random pure state (in the sector): eta(contiguous) NOT small
      (teeth).
  P4  two-interval: reported, not judged.
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from itertools import combinations

L = 14
REGION = 7
clip = 1e-12
rng = np.random.default_rng(7)

# -----------------------------------------------------------------------------
# Sz = 0 sector machinery
# -----------------------------------------------------------------------------
UP = L // 2
basis = []
for ones in combinations(range(L), UP):
    v = 0
    for i in ones:
        v |= (1 << i)
    basis.append(v)
basis = np.array(basis, dtype=np.int64)
DIM = len(basis)
index_of = {v: i for i, v in enumerate(basis)}

def xxz_sector_hamiltonian(delta):
    """H = sum (SxSx + SySy + delta SzSz) in the Sz=0 sector, real sparse."""
    rows, cols, vals = [], [], []
    for i, v in enumerate(basis):
        for b in range(L - 1):
            b1 = (v >> b) & 1
            b2 = (v >> (b + 1)) & 1
            if b1 == b2:
                # Sz Sz diagonal: (+1/2)(+1/2) or (-1/2)(-1/2) = +1/4
                rows.append(i); cols.append(i); vals.append(delta * 0.25)
            else:
                rows.append(i); cols.append(i); vals.append(-delta * 0.25)
                # flip-flop: (S+ S- + S- S+)/2 -> matrix element 1/2
                w = v ^ (1 << b) ^ (1 << (b + 1))
                j = index_of[w]
                rows.append(i); cols.append(j); vals.append(0.5)
    H = sparse.csr_matrix((vals, (rows, cols)), shape=(DIM, DIM))
    return H

def region_complement_indices(region):
    """For each sector basis state, its region-bits and complement-bits
    packed as integers."""
    region = list(region)
    complement = [i for i in range(L) if i not in region]
    reg = np.zeros(DIM, dtype=np.int64)
    comp = np.zeros(DIM, dtype=np.int64)
    for k, b in enumerate(region):
        reg |= ((basis >> b) & 1) << k
    for k, b in enumerate(complement):
        comp |= ((basis >> b) & 1) << k
    return reg, comp

def reduced_density_sector(psi, region):
    reg, comp = region_complement_indices(region)
    n_reg = 2 ** len(region)
    rho = np.zeros((n_reg, n_reg))
    # group basis rows by complement bits
    order = np.argsort(comp, kind='stable')
    comp_sorted = comp[order]
    boundaries = np.flatnonzero(np.r_[True, comp_sorted[1:] != comp_sorted[:-1]])
    for start in boundaries:
        rows = order[comp_sorted == comp_sorted[start]]
        block = psi[rows]
        ra = reg[rows]
        # outer product accumulated into region space
        np.add.at(rho, (ra[:, None], ra[None, :]),
                  np.outer(block, block))
    return rho

def modular_hamiltonian(rho):
    evals, evecs = np.linalg.eigh(rho)
    evals = np.clip(evals, clip, None)
    return -(evecs * np.log(evals)) @ evecs.T

def embed_sector(K_A, region):
    """K_A (x) I_complement restricted to the sector, as a dense real matrix."""
    reg, comp = region_complement_indices(region)
    K_full = K_A[reg[:, None], reg[None, :]]
    K_full[comp[:, None] != comp[None, :]] = 0.0
    return K_full

# -----------------------------------------------------------------------------
# Regions
# -----------------------------------------------------------------------------
contiguous = np.arange(3, 10)
even_odd = np.arange(0, L, 2)
two_interval = np.array([2, 3, 4, 8, 9, 10, 11])
random_regions = [np.sort(rng.choice(L, REGION, replace=False)) for _ in range(2)]
candidates = [("contiguous", contiguous), ("even/odd", even_odd),
              ("two-interval", two_interval)]
candidates += [(f"random #{k + 1}", r) for k, r in enumerate(random_regions)]

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 72)
print("INTERACTING DRIFT CHECK -- does [K_A, H] discriminate under interactions?")
print("=" * 72)
print()

results = {}
for delta in [1.0, 2.0]:
    H = xxz_sector_hamiltonian(delta)
    evals, evecs = eigsh(H, k=1, which='SA')
    psi = evecs[:, 0]
    psi /= np.linalg.norm(psi)
    H_dense = H.toarray()
    norm_H = np.linalg.norm(H_dense, 'fro')
    print(f"Delta = {delta} ({'critical' if delta == 1.0 else 'gapped'}), "
          f"ground energy {evals[0]:.6f}")
    print("-" * 72)
    for name, region in candidates:
        rho_A = reduced_density_sector(psi, region)
        K_A = modular_hamiltonian(rho_A)
        K_full = embed_sector(K_A, region)
        comm = K_full @ H_dense - H_dense @ K_full
        eta = float(np.linalg.norm(comm, 'fro')
                    / (np.linalg.norm(K_full, 'fro') * norm_H))
        results[(delta, name)] = eta
        print(f"  {name:>14s}  eta = {eta:.5f}")
    print("-" * 72)
    print()

# Haar control: random pure state in the sector, contiguous region
psi_rand = rng.standard_normal(DIM)
psi_rand /= np.linalg.norm(psi_rand)
H_dense = xxz_sector_hamiltonian(1.0).toarray()
norm_H = np.linalg.norm(H_dense, 'fro')
rho_A = reduced_density_sector(psi_rand, contiguous)
K_A = modular_hamiltonian(rho_A)
K_full = embed_sector(K_A, contiguous)
comm = K_full @ H_dense - H_dense @ K_full
eta_haar = float(np.linalg.norm(comm, 'fro')
                 / (np.linalg.norm(K_full, 'fro') * norm_H))
print(f"Haar control (sector, contiguous, D=1): eta = {eta_haar:.5f} "
      f"(vacuum: {results[(1.0, 'contiguous')]:.5f})")
print()

# -----------------------------------------------------------------------------
# Adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
checks = []
for delta, tag in [(1.0, "P1"), (2.0, "P2")]:
    c = results[(delta, "contiguous")]
    rivals = [results[(delta, n)] for n in
              ["even/odd", "two-interval", "random #1", "random #2"]]
    best = min(rivals)
    checks.append((f"{tag}: D={delta} contiguous beats every rival by > 2x",
                   best / c > 2.0, f"separation {best / c:.1f}x"))
checks.append(("P3: Haar control NOT drift-free (> 3x vacuum)",
               eta_haar > 3 * results[(1.0, "contiguous")],
               f"{eta_haar:.5f} vs {results[(1.0, 'contiguous')]:.5f}"))
for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<52s}  {value}")
print()
print(f"P4 (reported, not judged): two-interval eta "
      f"D=1: {results[(1.0, 'two-interval')]:.5f}, "
      f"D=2: {results[(2.0, 'two-interval')]:.5f} vs contiguous "
      f"{results[(1.0, 'contiguous')]:.5f}, {results[(2.0, 'contiguous')]:.5f}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
