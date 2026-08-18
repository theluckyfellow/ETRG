#!/usr/bin/env python3
"""
Cosmic numbers check (ETRG-6, evidence angle 1) -- the consistency layer.

Computes, with measured cosmological parameters, the numbers the
hypothesis puts in relation, and checks which candidate locks are
numerically consistent TODAY.  No curve fitting, no dynamics claims --
arithmetic with flagged inputs.

Relations checked:
  R1  the de Sitter surface gravity vs the MOND acceleration:
      kappa_dS = c H0 (asymptotic) vs a_0 = 1.2e-10 m/s^2 (measured,
      McGaugh et al. 2016).  Also the Unruh acceleration a_U = 2 pi c k_B
      T_GH / hbar with T_GH the Gibbons-Hawking temperature.
  R2  the tick budget: S_Lambda = 3 pi k_B c^3 / (Lambda G hbar) and the
      number of cosmic 'ticks' if the current Hubble time is one
      coherence time: S ~ (t_H / t_P)^2 (the holographic scaling).
  R3  the Gibbons-Hawking temperature and the entropic-time rate:
      kappa = 2 pi k_B T_GH / hbar vs H0 -- the candidate cosmological
      lock's rate identity (does the cosmic entropic clock run at the
      Hubble rate?).
"""

import numpy as np

# SI constants (exact where applicable)
c = 299792458.0
G = 6.67430e-11
hbar = 1.054571817e-34
kB = 1.380649e-23

# Measured cosmological parameters (Planck 2018 class)
H0 = 67.4e3 / 3.085677581e22          # 67.4 km/s/Mpc -> 1/s
Omega_L = 0.685
Lambda = 3 * Omega_L * H0 ** 2 / c ** 2
a_0_measured = 1.2e-10                # m/s^2, McGaugh-Lelli-Schombert 2016

print("=" * 72)
print("COSMIC NUMBERS CHECK -- the consistency layer")
print("=" * 72)
print()
print(f"inputs: H0 = {H0:.3e} 1/s (67.4 km/s/Mpc), "
      f"Omega_L = {Omega_L}, Lambda = {Lambda:.3e} 1/m^2")
print()

# R1: de Sitter surface gravity vs MOND a_0
R_dS = np.sqrt(3 / Lambda)
kappa_dS = c ** 2 / R_dS               # surface gravity (acceleration)
H_inf = np.sqrt(Lambda / 3) * c        # asymptotic Hubble rate
T_GH = hbar * H_inf / (2 * np.pi * kB)  # Gibbons-Hawking temperature
# the acceleration whose Unruh temperature is T_GH: a = 2 pi k_B T c / hbar
a_U = 2 * np.pi * kB * T_GH * c / hbar
print("R1: the acceleration scales")
print(f"  R_dS            = {R_dS:.3e} m  ({R_dS / 3.085677581e22 / 1e3:.2f} Gly)")
print(f"  kappa_dS = c^2/R_dS = {kappa_dS:.3e} m/s^2")
print(f"  c H_inf         = {c * H_inf:.3e} m/s^2")
print(f"  Unruh accel of T_GH = {a_U:.3e} m/s^2 (identical to kappa_dS")
print(f"      by construction -- the 2pi is the Unruh convention)")
print(f"  MOND a_0 (measured) = {a_0_measured:.3e} m/s^2")
print(f"  ratio kappa_dS / a_0 = {kappa_dS / a_0_measured:.2f}")
print(f"  note: a_0 vs c H_0 / (2 pi) = {c * H0 / (2 * np.pi):.3e}, "
      f"ratio {a_0_measured / (c * H0 / (2 * np.pi)):.2f}")
print()

# R2: the tick budget
S_Lambda = 3 * np.pi * kB * c ** 3 / (Lambda * G * hbar)
t_H = 1 / H0
t_P = np.sqrt(hbar * G / c ** 5)
S_nats = S_Lambda / kB
print("R2: the entropy budget")
print(f"  S_Lambda = {S_nats:.3e} nats")
print(f"  (t_H/t_P)^2 = {(t_H / t_P) ** 2:.3e}")
print(f"  ratio = {S_nats / (t_H / t_P) ** 2:.3f}  "
      f"(= pi/Omega_L = {np.pi / Omega_L:.3f} identically: "
      f"S_Lambda = (pi/Omega_L)(t_H/t_P)^2)")
print()

# R3: the cosmic entropic clock rate
T_GH = hbar * H_inf / (2 * np.pi * kB)  # Gibbons-Hawking temperature
kappa_rate = 2 * np.pi * kB * T_GH / hbar
print("R3: the candidate lock's rate identity")
print(f"  T_GH = {T_GH:.3e} K")
print(f"  modular rate 2 pi k_B T_GH / hbar = {kappa_rate:.3e} 1/s")
print(f"  H_inf = {H_inf:.3e} 1/s")
print(f"  ratio = {kappa_rate / H_inf:.4f} (predicted 1.0 by construction:")
print(f"  this is the DEFINITION of T_GH -- the content is that the")
print(f"  cosmic entropic clock, if it exists, runs at the Hubble rate)")
print()

# The one non-tautological number: how long is the budget in Hubble times?
N_ticks = S_nats
print("The budget vs the age:")
print(f"  S_Lambda = {N_ticks:.2e} nats;  universe age ~ 1.0 Hubble times")
print(f"  at one nat per Hubble time, the budget lasts {N_ticks:.2e} Hubble times")
print(f"  -- the observed smallness of Lambda = the budget is enormous")
print(f"     (10^122), so the clock does not run out; the B7 reading is")
print(f"     that a LONG history REQUIRES the tiny Lambda, not that the")
print(f"     budget is nearly spent.")
print()

print("CONSISTENCY SUMMARY (flags, not verdicts):")
print("-" * 72)
print(f"  R1: the de Sitter surface gravity and the MOND scale agree to")
print(f"      a factor {kappa_dS / a_0_measured:.1f} (and a_0 vs cH_0/2pi: "
      f"{a_0_measured / (c * H0 / (2 * np.pi)):.2f})")
print(f"      -- order-of-magnitude coincidence, coefficient UNDERIVED;")
print(f"      the convention freedom (1, 2pi, 1/2pi, sqrt(Omega_L)) spans")
print(f"      an order of magnitude and both ratios are of equal standing.")
print(f"      The program supplies the scale, NOT the dynamics.")
print(f"  R2: S_Lambda = (pi/Omega_L)(t_H/t_P)^2 -- an algebraic IDENTITY")
print(f"      of the definitions (exact for any parameter values);")
print(f"      definitional, like R3.  10^122 constrains nothing by itself.")
print(f"  R3: rate identity is definitional; the cosmological lock needs")
print(f"      a SECOND observable beyond H_inf to be a lock at all.")
