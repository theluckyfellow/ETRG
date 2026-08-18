#!/usr/bin/env python3
"""
Sanity audit of the program's named equations (round 7, item 4).

Re-derive, with fresh eyes and sympy, the equations the program's claims
stand on.  Two of this repository's retractions were caught by exactly this
kind of re-check.  Scope note (referee section 9): this is a SANITY pass,
not an adversarial one -- both sides of each identity are typed by the same
hand, so what is confirmed is the arithmetic and the dimensional table, not
the physics assumptions.  Targets:

  1. delta_lock = S(rho||rho_vac)/S_BH <= 2 G DeltaE / (c^4 R)
     -- where does the factor of 2 come from?  Derive it.
  2. The deflection factor (1 + v^2/c^2) -- limits and dimensions.
  3. m = (T/c^2) delta S  -- DeepSeek's P5 mass relation, dimensions.
  4. S_Lambda = 3 pi / (Lambda G) (natural units) -- the de Sitter budget,
     from the horizon area, with full SI dimensional check.
"""

import sympy as sp

print("=" * 72)
print("AUDIT: the program's named equations, re-derived")
print("=" * 72)
print()

# -----------------------------------------------------------------------------
# 1. The delta_lock bound and its factor of 2
# -----------------------------------------------------------------------------
# Relative entropy: S(rho||rho_vac) = Delta<K> - DeltaS  <=  Delta<K>
# (monotonicity of the first-law pairing; the Casini bound).
# For a causal diamond / Rindler wedge of size R, the modular generator is
# the boost generator: K = (2 pi / (hbar c)) * (first moment of energy).
# Energy DeltaE localized at distance R from the edge:
#   Delta<K> = 2 pi R DeltaE / (hbar c)
# Bekenstein-Hawking entropy of the bounding area A = 4 pi R^2:
#   S_BH = k_B c^3 A / (4 G hbar) = pi k_B c^3 R^2 / (G hbar)
# Ratio (k_B = 1):
#   Delta<K>/S_BH = [2 pi R DeltaE / (hbar c)] / [pi c^3 R^2 / (G hbar)]
#                 = 2 G DeltaE / (c^4 R)
print("1. delta_lock factor-of-2 derivation")
print("-" * 72)
G, dE, c, R, hbar, kB, pi = sp.symbols(
    'G DeltaE c R hbar k_B pi', positive=True)
Delta_K = 2 * pi * R * dE / (hbar * c)
A = 4 * pi * R**2
S_BH = kB * c**3 * A / (4 * G * hbar)
ratio = sp.simplify(Delta_K / S_BH)
claimed = 2 * G * dE / (c**4 * R * kB)
print(f"  Delta<K>/S_BH (derived) = {ratio}")
print(f"  claimed bound           = {claimed}")
print(f"  difference              = {sp.simplify(ratio - claimed)}")
ok1 = sp.simplify(ratio - claimed) == 0
print(f"  factor of 2 = pi-cancellation of boost generator vs area law: "
      f"{'CONFIRMED' if ok1 else 'MISMATCH'}")
print()

# -----------------------------------------------------------------------------
# 2. Deflection factor (1 + v^2/c^2)
# -----------------------------------------------------------------------------
print("2. Deflection factor (1 + v^2/c^2)")
print("-" * 72)
v = sp.symbols('v', positive=True)
factor = 1 + (v / c)**2
rest = factor.subs(v, 0)
ultra = sp.limit(factor, v, c)
print(f"  v -> 0:  {rest}   (Newtonian / slow matter reads one face)")
print(f"  v -> c:  {ultra}   (light reads both faces: the measured 2:1)")
ok2 = (rest == 1 and ultra == 2)
print(f"  limits: {'CONFIRMED' if ok2 else 'MISMATCH'}")
print()

# -----------------------------------------------------------------------------
# 3. Dimensional checks (SI)
# -----------------------------------------------------------------------------
# sympy 1.18's unit system cannot resolve named PhysicalConstants, so the
# audit is done as raw exponent arithmetic on base SI dimensions.
print("3. Dimensional audit (SI base dimensions)")
print("-" * 72)
m_, kg, s_, K_ = sp.symbols('m kg s K', positive=True)   # meter, kilogram,
                                                         # second, kelvin
# Base-unit expansions
Si_G = m_**3 / (kg * s_**2)                 # gravitational constant
Si_J = kg * m_**2 / s_**2                   # joule (energy)
Si_c = m_ / s_                              # speed of light
Si_kB = Si_J / K_                           # Boltzmann constant
Si_hbar = Si_J * s_                         # reduced Planck constant
Si_Lambda = 1 / m_**2                       # cosmological constant

def exponents(expr):
    """Exponent vector (m, kg, s, K) of a product of base dimensions."""
    powers = expr.as_powers_dict()
    return tuple(sp.expand(powers.get(b, 0)) for b in (m_, kg, s_, K_))

checks = []

expr_a = Si_G * Si_J / (Si_c**4 * m_)       # G*DeltaE/(c^4 R)
checks.append(("G*DeltaE/(c^4 R) dimensionless",
               exponents(expr_a) == (0, 0, 0, 0), str(exponents(expr_a))))

expr_b = Si_J / Si_c**2                     # T*deltaS/c^2 (deltaS in k_B)
checks.append(("T*deltaS/c^2 has units of mass",
               exponents(expr_b) == (0, 1, 0, 0), str(exponents(expr_b))))

expr_c = Si_kB * Si_c**3 / (Si_Lambda * Si_G * Si_hbar)
# NOTE: S_Lambda is an ENTROPY -- in SI it carries units of k_B (J/K),
# exponent vector (2, 1, -2, -1).  An earlier version of this check demanded
# strict dimensionlessness and flagged the equation; the flag was the
# audit's bug, not the program's.  Entropy is dimensionless only in units
# where k_B = 1.
checks.append(("3 pi k_B c^3/(Lambda G hbar) has entropy units (J/K)",
               exponents(expr_c) == (2, 1, -2, -1), str(exponents(expr_c))))

expr_d = Si_kB * K_ / Si_hbar               # k_B T/hbar
checks.append(("k_B T/hbar has units of rate (1/time)",
               exponents(expr_d) == (0, 0, -1, 0), str(exponents(expr_d))))

for desc, ok, detail in checks:
    print(f"  {'ok ' if ok else 'BAD'}  {desc:<45s}  {detail}")
print()

# -----------------------------------------------------------------------------
# 4. The de Sitter budget from the horizon area
# -----------------------------------------------------------------------------
print("4. S_Lambda = 3 pi/(Lambda G) from the area law")
print("-" * 72)
Lam = sp.symbols('Lambda', positive=True)
R_dS = sp.sqrt(3 / Lam)                    # de Sitter horizon radius
A_dS = 4 * sp.pi * R_dS**2                 # horizon area
G_newton = sp.symbols('G', positive=True)
S_dS_G = sp.simplify(A_dS / (4 * G_newton))
print(f"  R_dS = sqrt(3/Lambda)  ->  A = {sp.simplify(A_dS)}")
print(f"  S = A/4G = {S_dS_G}   (claimed 3*pi/(Lambda*G))")
ok4 = sp.simplify(S_dS_G - 3 * sp.pi / (Lam * G_newton)) == 0
print(f"  {'CONFIRMED' if ok4 else 'MISMATCH'}")
print()

# -----------------------------------------------------------------------------
# Verdict
# -----------------------------------------------------------------------------
print("PASS / FAIL table:")
print("-" * 72)
all_checks = [("delta_lock factor of 2 derived", ok1, ""),
              ("deflection limits 1 and 2", ok2, "")] + \
             [(d, o, "") for d, o, _ in checks] + \
             [("de Sitter budget from area law", ok4, "")]
for desc, ok, _ in all_checks:
    print(f"  {'PASS' if ok else 'FAIL':>5s}  {desc}")
print("-" * 72)
print(f"Overall: {'PASS' if all(c[1] for c in all_checks) else 'FAIL'}")
