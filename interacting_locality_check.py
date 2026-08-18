#!/usr/bin/env python3
"""
Interacting modular-locality check (round 7, item 2): K5's verdict.

All round-7 numerics so far are free fermions -- Gaussian states, where the
modular Hamiltonian is quadratic by construction and quasi-locality might be
a free-theory artifact.  Kill criterion K5: if class selection fails for an
INTERACTING vacuum, P-select is exactly that artifact.

System: XXZ spin chain, L = 14, open boundaries,
    H = sum_i (Sx_i Sx_{i+1} + Sy_i Sy_{i+1} + Delta Sz_i Sz_{i+1})
at Delta = 1 (Heisenberg point, critical) and Delta = 2 (gapped control).
Exact diagonalization (2^14 Hilbert space, sparse).

For a region A of 7 sites, the modular generator K_A = -ln rho_A is NOT
quadratic; locality is measured in the Pauli basis:
    K_A = sum_P c_P P,   c_P = Tr(K_A P) / 2^7
and each Pauli string P has a RANGE = spread of lattice coordinates of its
support.  A local generator has weight concentrated on short-range strings.

Prediction (if P-select survives interactions): contiguous region -> weight
on short-range strings; scrambled regions of the same size -> long-range
weight.  Teeth control: a Haar-random pure state must show NO locality.
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

rng = np.random.default_rng(7)

L = 14
REGION = 7
clip = 1e-12

# -----------------------------------------------------------------------------
# Pauli machinery
# -----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = [I2, SX, SY, SZ]

# Change-of-basis matrix M[p, (i,j)] = P_p[j, i], so that
# c[p_1..p_n] = (1/2^n) sum M[p_1,(i_1,j_1)] ... K[(i..),(j..)]
M = np.array([[P[j, i] for i in range(2) for j in range(2)] for P in PAULIS])
# index convention: flattened (i,j) with i the ROW of K, j the COLUMN;
# P[j,i] picks out Tr(K P) = sum_{ij} K_{ij} P_{ji}

def pauli_coefficients(K, n):
    """All 4^n Pauli coefficients of the Hermitian operator K on n sites,
    via FFT-style butterfly (tensordot along each qubit axis)."""
    T = K.reshape([2] * (2 * n))
    # group (i_1, j_1, ..., i_n, j_n): axes (0,2,4,...,2n-2) are rows i_k,
    # axes (1,3,...,2n-1) are cols j_k -> permute to interleave per site
    perm = []
    for k in range(n):
        perm += [k, n + k]
    T = T.transpose(perm).reshape([4] * n)
    for axis in range(n):
        T = np.tensordot(M, T, axes=([1], [axis]))
        T = np.moveaxis(T, 0, axis)
    return T / (2 ** n)

def string_ranges(n, region_lattice_pos):
    """range[p_1..p_n] = spread of lattice positions of the support."""
    ranges = np.zeros([4] * n)
    for idx in np.ndindex(*([4] * n)):
        support = [region_lattice_pos[k] for k in range(n) if idx[k] != 0]
        ranges[idx] = (max(support) - min(support)) if len(support) > 1 else 0
    return ranges

def locality_spectrum(K, region):
    """Return (ranges, weights) arrays over non-identity Pauli strings."""
    n = len(region)
    C = pauli_coefficients(K, n)
    R = string_ranges(n, list(region))
    W = np.abs(C) ** 2
    W[(0,) * n] = 0.0
    return R.flatten(), W.flatten()

def r_quantile(R, W, q):
    order = np.argsort(R)
    Rs, Ws = R[order], W[order]
    cum = np.cumsum(Ws)
    total = cum[-1]
    if total == 0:
        return 0.0
    return float(Rs[np.searchsorted(cum, q * total)])

# -----------------------------------------------------------------------------
# XXZ chain
# -----------------------------------------------------------------------------
def xxz_hamiltonian(L, delta):
    sx = sparse.csr_matrix(SX / 2)
    sy = sparse.csr_matrix(SY / 2)
    sz = sparse.csr_matrix(SZ / 2)
    idop = sparse.eye(2, format='csr')

    def onsite(op, i):
        ops = [idop] * L
        ops[i] = op
        out = ops[0]
        for o in ops[1:]:
            out = sparse.kron(out, o, format='csr')
        return out

    H = sparse.csr_matrix((2 ** L, 2 ** L), dtype=complex)
    Sxs = [onsite(sx, i) for i in range(L)]
    Sys = [onsite(sy, i) for i in range(L)]
    Szs = [onsite(sz, i) for i in range(L)]
    for i in range(L - 1):
        H += Sxs[i] @ Sxs[i + 1] + Sys[i] @ Sys[i + 1] \
            + delta * Szs[i] @ Szs[i + 1]
    return H

def ground_state(H):
    evals, evecs = eigsh(H, k=1, which='SA')
    psi = evecs[:, 0]
    return psi / np.linalg.norm(psi)

def reduced_density(psi, region, L):
    T = psi.reshape([2] * L)
    complement = [i for i in range(L) if i not in region]
    perm = list(region) + complement
    T = T.transpose(perm).reshape(2 ** len(region), -1)
    return T @ T.conj().T

def modular_hamiltonian(rho):
    evals, evecs = np.linalg.eigh(rho)
    evals = np.clip(evals, clip, None)
    return -(evecs * np.log(evals)) @ evecs.conj().T

# -----------------------------------------------------------------------------
# Regions (all size 7)
# -----------------------------------------------------------------------------
contiguous = np.arange(3, 10)
even_odd = np.arange(0, L, 2)
two_interval = np.array([2, 3, 4, 8, 9, 10, 11])
random_regions = [np.sort(rng.choice(L, REGION, replace=False))
                  for _ in range(2)]

candidates = [("contiguous", contiguous), ("even/odd", even_odd),
              ("two-interval", two_interval)]
candidates += [(f"random #{k + 1}", r) for k, r in enumerate(random_regions)]

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 78)
print("INTERACTING MODULAR-LOCALITY CHECK (K5) -- XXZ chain, exact diag")
print("=" * 78)
print(f"L = {L}, region size {REGION}, Pauli-basis locality of K_A = -ln rho_A")
print()

results = {}
for delta in [1.0, 2.0]:
    print(f"Delta = {delta} ({'critical Heisenberg' if delta == 1.0 else 'gapped'})")
    print("-" * 78)
    print(f"{'region':>14s}  {'r_50':>6s}  {'r_99':>6s}  {'w(r<=1)':>8s}  "
          f"{'w(r<=2)':>8s}")
    print("-" * 78)
    psi = ground_state(xxz_hamiltonian(L, delta))
    for name, region in candidates:
        rho_A = reduced_density(psi, region, L)
        K_A = modular_hamiltonian(rho_A)
        R, W = locality_spectrum(K_A, region)
        r50 = r_quantile(R, W, 0.50)
        r99 = r_quantile(R, W, 0.99)
        w1 = float(W[R <= 1].sum() / W.sum())
        w2 = float(W[R <= 2].sum() / W.sum())
        results[(delta, name)] = (r99, w1)
        print(f"{name:>14s}  {r50:6.1f}  {r99:6.1f}  {w1:8.3f}  {w2:8.3f}")
    print("-" * 78)
    print()

# Teeth control: Haar-random pure state, contiguous region
psi_rand = (rng.standard_normal(2 ** L) + 1j * rng.standard_normal(2 ** L))
psi_rand /= np.linalg.norm(psi_rand)
rho_A = reduced_density(psi_rand, contiguous, L)
K_A = modular_hamiltonian(rho_A)
R, W = locality_spectrum(K_A, contiguous)
haar_w1 = float(W[R <= 1].sum() / W.sum())
haar_r99 = r_quantile(R, W, 0.99)
print(f"Teeth control: Haar-random state, contiguous region: "
      f"r_99 = {haar_r99:.1f}, w(r<=1) = {haar_w1:.3f}")
print()

# -----------------------------------------------------------------------------
# PASS / FAIL adjudication
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 70)
checks = []
for delta in [1.0, 2.0]:
    c99, cw1 = results[(delta, "contiguous")]
    rivals = [results[(delta, n)] for n in
              ["even/odd", "two-interval", "random #1", "random #2"]]
    rival_r99 = min(r[0] for r in rivals)
    checks.append((f"D={delta}: contiguous r_99 strictly smallest",
                   c99 < rival_r99, f"{c99:.1f} vs best rival {rival_r99:.1f}"))
    checks.append((f"D={delta}: contiguous nn-dominated (w(r<=1) > 0.5)",
                   cw1 > 0.5, f"{cw1:.3f}"))
checks.append(("teeth: Haar state NOT short-range (w(r<=1) < 0.2)",
               haar_w1 < 0.2, f"{haar_w1:.3f}"))

for desc, passed, value in checks:
    print(f"  {'PASS' if passed else 'FAIL':>5s}  {desc:<56s}  {value}")
print("-" * 70)
print(f"Overall: {'PASS' if all(c[1] for c in checks) else 'FAIL'}")
