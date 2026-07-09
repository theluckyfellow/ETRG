from sympy import *

print("=" * 70)
print("lock_check.py: linearized static metric verification")
print("ds^2 = -(1+2*Phi) dt^2 + (1-2*Psi)(dx^2+dy^2+dz^2), c=G=1")
print("All quantities to first order in Phi, Psi.")
print("=" * 70)

# ------------------------------------------------------------------
# SETUP
# ------------------------------------------------------------------
t, x, y, z = symbols("t x y z", real=True)
coords = [t, x, y, z]
Phi = Function("Phi")
Psi = Function("Psi")
phi = Phi(x, y, z)
psi = Psi(x, y, z)

nx, ny, nz = symbols("nx ny nz", real=True)
v, M, b, l = symbols("v M b l", positive=True, real=True)

def d(F, mu):
    return diff(F, coords[mu])

# ------------------------------------------------------------------
# Linearized metric perturbation and flat inverse
# ------------------------------------------------------------------
# h_{00} = -2 Phi, h_{ij} = -2 Psi delta_{ij}, other components zero.
delta_3 = eye(3)


def h(mu, nu):
    if mu == 0 and nu == 0:
        return -2 * phi
    if mu >= 1 and nu >= 1:
        return -2 * psi * delta_3[mu - 1, nu - 1]
    return 0


def eta_inv(rho, sigma):
    if rho != sigma:
        return 0
    return -1 if rho == 0 else 1


def dh(mu, nu, lam):
    return diff(h(mu, nu), coords[lam])


# Linearized Christoffel: Gamma^rho_{mu nu} = 1/2 eta^{rho sigma}
#   ( d_mu h_{nu sigma} + d_nu h_{mu sigma} - d_sigma h_{mu nu} )
Gamma = MutableDenseNDimArray.zeros(4, 4, 4)
for rho in range(4):
    for mu in range(4):
        for nu in range(4):
            val = 0
            for sigma in range(4):
                val += eta_inv(rho, sigma) * (
                    dh(nu, sigma, mu) + dh(mu, sigma, nu) - dh(mu, nu, sigma)
                )
            Gamma[rho, mu, nu] = Rational(1, 2) * val

# Linearized Riemann: keep derivatives of Christoffels only
# (Products of Christoffels are O(Psi^2/Phi^2) and drop.)
Riem = MutableDenseNDimArray.zeros(4, 4, 4, 4)
for rho in range(4):
    for sigma in range(4):
        for mu in range(4):
            for nu in range(4):
                Riem[rho, sigma, mu, nu] = (
                    diff(Gamma[rho, sigma, nu], coords[mu])
                    - diff(Gamma[rho, sigma, mu], coords[nu])
                )

# Ricci_ab = R^c_{a c b}
Ric = MutableDenseNDimArray.zeros(4, 4)
for a in range(4):
    for b in range(4):
        Ric[a, b] = sum(Riem[c, a, c, b] for c in range(4))

lap_phi = d(d(phi, 1), 1) + d(d(phi, 2), 2) + d(d(phi, 3), 3)
lap_psi = d(d(psi, 1), 1) + d(d(psi, 2), 2) + d(d(psi, 3), 3)
d2_phi = [[d(d(phi, i), j) for j in range(4)] for i in range(4)]
d2_psi = [[d(d(psi, i), j) for j in range(4)] for i in range(4)]

grad_phi = Matrix([diff(phi, x), diff(phi, y), diff(phi, z)])
grad_psi = Matrix([diff(psi, x), diff(psi, y), diff(psi, z)])

pf = []
labels = []


def check(label, expr, expected_zero=True):
    labels.append(label)
    pf.append(simplify(expr) == 0)


# ------------------------------------------------------------------
# (1) Ricci tensor components
# ------------------------------------------------------------------
check("R_00 = Lap(Phi)", Ric[0, 0] - lap_phi)
check("R_01 = 0", Ric[0, 1])
check("R_02 = 0", Ric[0, 2])
check("R_03 = 0", Ric[0, 3])
for i in range(1, 4):
    for j in range(1, 4):
        target = delta_3[i - 1, j - 1] * lap_psi + d2_psi[i][j] - d2_phi[i][j]
        check(f"R_{i}{j} target", Ric[i, j] - target)

# ------------------------------------------------------------------
# (2) Null contraction  R_ab k^a k^b  with k=(1,n-hat)
# ------------------------------------------------------------------
k = Matrix([1, nx, ny, nz])
Rkk = sum(Ric[a, b] * k[a] * k[b] for a in range(4) for b in range(4))

target2 = (
    lap_phi
    + lap_psi
    + (d2_psi[1][1] - d2_phi[1][1]) * nx**2
    + (d2_psi[2][2] - d2_phi[2][2]) * ny**2
    + (d2_psi[3][3] - d2_phi[3][3]) * nz**2
    + 2 * (d2_psi[1][2] - d2_phi[1][2]) * nx * ny
    + 2 * (d2_psi[1][3] - d2_phi[1][3]) * nx * nz
    + 2 * (d2_psi[2][3] - d2_phi[2][3]) * ny * nz
)

# Difference vanishes when |n|=1; substitute that relation for z.
diff2 = simplify(Rkk - target2)
check("R_ab k^a k^b (n^2=1)", diff2.subs(nz**2, 1 - nx**2 - ny**2))

# Concrete unit vectors
def contract_Rkk(nvec):
    ka = [1] + list(nvec)
    return sum(Ric[a, b] * ka[a] * ka[b] for a in range(4) for b in range(4))


def target_for_n(nvec):
    lp = lap_phi + lap_psi
    s = 0
    for i in range(1, 4):
        for j in range(1, 4):
            s += (d2_psi[i][j] - d2_phi[i][j]) * nvec[i - 1] * nvec[j - 1]
    return lp + s


check("R_ab k^a k^b n=x-hat", contract_Rkk([1, 0, 0]) - target_for_n([1, 0, 0]))
check("R_ab k^a k^b n=y-hat", contract_Rkk([0, 1, 0]) - target_for_n([0, 1, 0]))
check(
    "R_ab k^a k^b n=45deg",
    contract_Rkk([1 / sqrt(2), 1 / sqrt(2), 0]) - target_for_n([1 / sqrt(2), 1 / sqrt(2), 0]),
)

# ------------------------------------------------------------------
# (3) Coordinate-time geodesic -> transverse coordinate acceleration
# ------------------------------------------------------------------
e1, e2, e3 = symbols("e1 e2 e3", real=True)
e_vec = Matrix([e1, e2, e3])
u = Matrix([1, v * e1, v * e2, v * e3])

# For parameter t, a^mu = -Gamma^mu_ab u^a u^b + Gamma^0_ab u^a u^b u^mu.
# (The second term is the reparameterization correction because t is not affine.)
a = Matrix.zeros(4, 1)
for mu in range(4):
    g0 = sum(Gamma[0, alpha, beta] * u[alpha] * u[beta] for alpha in range(4) for beta in range(4))
    gm = sum(Gamma[mu, alpha, beta] * u[alpha] * u[beta] for alpha in range(4) for beta in range(4))
    a[mu] = -gm + g0 * u[mu]
a_spatial = Matrix([a[i] for i in range(1, 4)])

# Dot the spatial acceleration with explicit perpendicular unit vectors
# and compare with a_perp = - Grad_perp(Phi) - v^2 Grad_perp(Psi).
expected_acc = -(grad_phi + v**2 * grad_psi)


def transverse_check(e_in, perp):
    a_sub = a_spatial.subs({e1: e_in[0], e2: e_in[1], e3: e_in[2]})
    exp_sub = expected_acc  # independent of e
    dot_a = sum(perp[i] * a_sub[i] for i in range(3))
    dot_t = sum(perp[i] * exp_sub[i] for i in range(3))
    return simplify(dot_a - dot_t)


for name, e_in, perp in [
    ("e=x-hat, perp=y", [1, 0, 0], [0, 1, 0]),
    ("e=x-hat, perp=z", [1, 0, 0], [0, 0, 1]),
    ("e=y-hat, perp=x", [0, 1, 0], [1, 0, 0]),
    ("e=y-hat, perp=z", [0, 1, 0], [0, 0, 1]),
    ("e=45deg xy, perp=z", [1 / sqrt(2), 1 / sqrt(2), 0], [0, 0, 1]),
]:
    check("a_perp " + name, transverse_check(e_in, perp))

# Explicit v-cases requested in the prompt (e along x-hat, perp along y)
check(
    "a_perp(v=0, e=x-hat, perp=y)",
    transverse_check([1, 0, 0], [0, 1, 0]).subs(v, 0),
)
check(
    "a_perp(v=1, Psi=Phi, e=x-hat, perp=y)",
    transverse_check([1, 0, 0], [0, 1, 0]).subs({v: 1, psi: phi}),
)

# ------------------------------------------------------------------
# (4) Photon deflection by a point mass: Phi=Psi=-M/r
# ------------------------------------------------------------------
# Light travels along x at impact parameter b in the y direction.
r_expr = sqrt(x**2 + y**2 + z**2)
Phi_pm = -M / r_expr
Psi_pm = -M / r_expr

# Transverse gradient of (Phi+Psi) evaluated on the unperturbed ray (z=0,y=b,x=l).
grad_perp_sum = diff(Phi_pm + Psi_pm, y).subs({z: 0, y: b, x: l})
alpha = integrate(grad_perp_sum, (l, -oo, oo))
check("photon deflection integral", simplify(alpha - 4 * M / b))

# ------------------------------------------------------------------
# Summary
# ------------------------------------------------------------------
print()
print("PASS / FAIL table")
print("-" * 70)
for label, ok in zip(labels, pf):
    print(f"{'PASS' if ok else 'FAIL':6}  {label}")
print("-" * 70)
print(f"Overall: {'ALL PASS' if all(pf) else 'SOME FAIL'}")
