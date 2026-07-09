# ETRG-0 Lock Note — Three Findings

**Date:** 2026-07-09
**Target:** ETRG-0_lock_note.md, L3 and L5
**Format:** Three numbered findings, most lethal first.

---

## Finding 1 — L3 normalization is frame-dependent; the isotropy mini-theorem is vacuous in the form stated (FATAL)

### The problem

L3 writes the null vector as k = (1, n̂) and imposes R_ab k^a k^b = 8πG T_ab k^a k^b "for all null n̂ at every point." But the coordinate components k^a = (1, n̂) are not affinely parameterized; they are a *convenient coordinate representation* of null directions. The physical content of the null-null equation is that it holds for *null vectors at fixed affine normalization*. Choosing k^0 = 1 everywhere is a choice of normalization that is not Lorentz-invariant and conflates direction with normalization.

The claim that the source T_ab k^a k^b is "n̂-independent" for dust in the static frame relies on the coordinate normalization k^0 = 1. Under a boost, this normalization mixes with the spatial direction.

### The explicit counter-calculation

Take the static dust source: T_ab = ρ u_a u_b with u^a = (1, 0, 0, 0). In the rest frame, T_ab k^a k^b = ρ (u·k)^2. Crucially, this equals ρ *only because k^0 = 1*. If we use an affinely parameterized null vector with components k^a = λ(1, n̂) — the physically correct normalization — then T_ab k^a k^b = ρ λ², and the λ² factor is common to all directions and drops out of direction-dependence. So in the dust rest frame, the direction-independence holds regardless of normalization choice.

The real problem appears under a boost. Apply a Lorentz boost along the x-axis with velocity v. The dust 4-velocity becomes u'^a = γ(1, v, 0, 0) with γ = 1/√(1-v²). Now the null vector in the new coordinates becomes k'^a = γ(λ − λv n_x, λ n_x − λv, λ n_y, λ n_z) with λ arbitrary.

The contraction T_ab k'^a k'^b = ρ (u'·k')² = ργ²λ²(1 − v n_x)².

This is **manifestly direction-dependent** when v ≠ 0: the source term depends on n_x. The "isotropy of the null law" premise of L3 — that the source side of R_ab k^a k^b = 8πG T_ab k^a k^b is n̂-independent — is true *only in the dust rest frame*, not in general.

### What this means for L3

The isotropy mini-theorem's proof that ∇²(Ψ−Φ) = 0 (hence Ψ = Φ) relied specifically on the source term being n̂-independent *in the static weak-field frame*. This is fine for a static isolated source in its rest frame. But it means:

1. **The L3 proof is not covariant.** The conclusion Ψ = Φ is frame-dependent, not a general validation of the lock. It works in one frame by construction and fails in others where the isotropy premise is false.

2. **The "lock" is bought by restricting to the source rest frame**, which is tantamount to assuming staticity — the very regime where standard GR already enforces γ = 1. There is no demonstration that the lock *emerges* from entropic reasoning; it is imposed by the choice of frame.

3. **The affine normalization factor λ enters the equation** as a common multiplicative factor on both sides and cancels — so that aspect is benign. The genuine problem is the velocity/boost dependence.

### Verdict

L3's isotropy argument is correct as a consistency check (Ψ = Φ follows from the null law in the static dust rest frame), but it does not establish the lock as a structural consequence of the entropic framework. It merely confirms that the null law is consistent with the known static weak-field limit of GR — which is not in dispute. The claim that "no Bianchi identity and no wholesale import of the Einstein equations is needed" is misleading: the bound of staticity + asymptotic flatness *is* doing the work, and the result is frame-bound, not frame-invariant.

---

## Finding 2 — Anisotropic stress degrades Ψ = Φ identically to standard GR; no independent prediction

### The calculation

In standard GR, the linearized Einstein equations for a general stress-energy tensor give (in the Newtonian gauge, c = G = 1):

∇²Φ = 4π(ρ + 3p − 3σ̈) ... or more directly, the trace and traceless decompositions:

∇²(Φ + Ψ) = 8π ρ  [from R_00 + δ^ij R_ij, or equivalently from the null-null contraction summed over directions]

∂_i ∂_j (Φ − Ψ) − (1/3)δ_ij ∇²(Φ − Ψ) = 8π π_ij  [the anisotropic stress part]

where π_ij is the traceless part of the spatial stress tensor T_ij.

Now, starting from the entropic null law R_ab k^a k^b = 8πG T_ab k^a k^b:

With a general stress tensor, T_ab k^a k^b is:

T_ab k^a k^b = T_00 k^0 k^0 + 2 T_0i k^0 k^i + T_ij k^i k^j

With k^a = (1, n̂) in the static frame and T_0i = 0:

T_ab k^a k^b = ρ + T_ij n^i n^j

Decompose T_ij = p δ_ij + π_ij where π_ij is traceless (π^i_i = 0):

T_ab k^a k^b = ρ + p + π_ij n^i n^j

The n^i n^j term multiplying π_ij is direction-dependent. Following the same trace/traceless split as L3:

The isotropic part: ∇²(Φ + Ψ) = 8π(ρ + p) — this is the GR result from the trace, correct.

The traceless part: [∂_i ∂_j − (1/3)δ_ij ∇²](Ψ − Φ) = 8π π_ij — this is EXACTLY the standard GR equation for the anisotropic stress sourcing Φ − Ψ.

Therefore Ψ − Φ ≠ 0 whenever π_ij ≠ 0, and the deviation is identical to standard GR.

### The implication for L3

The entropic null law does not independently force Ψ = Φ when anisotropic stress is present. The Ψ = Φ result of L3 is a special case of *isotropic* stress (perfect fluid/dust), which is already the standard GR result.

**Crucially, this means the entropic framework contributes zero new predictive content beyond what the linearized Einstein equations already say.** Even in the static weak field, the null law is not an independent constraint that produces γ = 1 — it is equivalent to a subset of the Einstein equations that, when combined with matter properties (isotropic stress), gives the same answer GR gives.

The framework does not independently *predict* γ = 1; it recovers γ = 1 in the regime where GR also gives γ = 1, and it recovers γ ≠ 1 in the regime where GR gives γ ≠ 1. The lock is therefore not a derivation but a restatement.

### Verdict

L3's "mini-theorem" demonstrates that the null law is not internally inconsistent with the static, isotropic weak-field limit of GR. It does not demonstrate that the entropic structure provides any independent reason for γ = 1. The degradation under anisotropic stress is parametric with standard GR, confirming this is equivalence-class physics, not novel constraint.

---

## Finding 3 — L5 decoupling: the modular generator's two faces give inconsistent calibrations away from exact equilibrium

### The claim under attack

L5 claims that K̂ — the modular/boost generator at a causal horizon — unifies the temporal and spatial sectors because:

- **Thermality face:** defines √(−g_00) = T_∞/T(x) = the lapse (axiom A4)
- **Variational face:** δS = δ⟨K̂⟩ with S = A/4Għ sources spatial geometry (axiom A5)

And that "One operator, one calibration constant (η = 1/4Għ; operationally one σ), two projections" prevents independent rescaling.

### The failure mode

This lock holds *only* when the state is exactly the vacuum restricted to the causal domain — i.e., when Bisognano–Wichmann applies exactly, the modular flow is geometric (a pure boost), and the state is exactly thermal in that boost. Away from this idealization, the two faces draw their calibrations from different physical structures that need not agree.

### Constructing the decoupling scenario

Consider a Rindler wedge in a nearly-flat background, but with the quantum field in a *slightly non-vacuum* state — specifically, a state with a small but nonzero energy flux through the horizon, mimicking the early stages of black hole formation or a collapsing shell that has not yet settled.

**Physical setup:** A thin null shell of energy ΔE falls through the Rindler horizon at some advanced time. Before the shell, the state is the Minkowski vacuum restricted to the wedge — Bisognano–Wichmann applies, the modular Hamiltonian is the boost generator K̂_B, and the state is exactly thermal at the Unruh temperature T_U = a/2π.

After the shell passes, the state is no longer the vacuum. The modular Hamiltonian K̂ now differs from K̂_B:

K̂ = K̂_B + ΔK̂

where ΔK̂ encodes the energy flux. The correction ΔK̂ is *nonlocal* — it is not a simple geometric operator. This is the well-known fact that modular flow for non-vacuum states is not a local geometric diffeomorphism (the "non-geometric modular flow" problem).

**The two calibrations diverge quantitatively:**

**(a) Thermality face:** The local temperature T(x) is defined by the KMS condition with respect to K̂. For the out-of-equilibrium state, T(x) is not simply T_U/√(−g_00) with a constant T_U. The Tolman relation T(x)√(−g_00) = const holds only in stationary equilibrium. After the shell, the state is non-stationary, the temperature is position- and time-dependent in a non-factorizable way, and the lapse computed from T_∞/T(x) differs from the equilibrium value by an amount proportional to ΔE/E_vac, where E_vac is the vacuum energy in the wedge (formally divergent, but regulated to the Planck scale).

Specifically, for a Rindler wedge regularized with a cutoff at distance ℓ (e.g., ℓ ~ ℓ_Planck), the vacuum energy in the wedge scales as E_vac ~ A/ℓ² where A is the horizon area. The fractional correction to the temperature from the shell is:

δT/T ~ ΔE / E_vac ~ ΔE · ℓ² / A

For a macroscopic horizon (stellar mass), this is negligible. But for a small diamond or an early-universe horizon, the correction can be O(1).

**(b) Variational face:** The entanglement first law δS = δ⟨K̂⟩ for a small causal diamond relies on the state being an "entanglement equilibrium" state (Jacobson 2016). For the exact vacuum, δ⟨K̂⟩ = 0 by construction when the diamond is in equilibrium. The derivation of the Einstein equations from this setup uses the *vacuum* modular Hamiltonian to relate δ⟨K̂⟩ to the Einstein tensor.

After the shell, the modular Hamiltonian is not the vacuum one. Writing:

δS = δ⟨K̂_vac⟩ + δ⟨ΔK̂⟩

The second term δ⟨ΔK̂⟩ is not captured by the geometric derivation because ΔK̂ is nonlocal and state-dependent. The area law calibration S = A/4Għ comes from the UV structure of the vacuum entanglement; it is not re-derived for each state.

**The gap:** The two faces now use *different* K̂:

- Thermality face uses the full K̂ = K̂_vac + ΔK̂ (because the thermal state is defined with respect to the actual modular Hamiltonian)
- Variational face effectively uses K̂_vac (because the derivation of Einstein's equations from δS = δ⟨K̂⟩ assumes the vacuum modular Hamiltonian is geometric)

**Quantitative mismatch:** The lapse computed from the thermality face is L_thermal = T_∞/T(x) with T from the full K̂. The spatial metric from the variational face comes from δ⟨K̂_vac⟩. If ΔK̂ contributes differently to the two faces, the calibrations differ.

For the shell scenario, the temperature correction is δT ~ (ΔE/E_vac) T_U. The corresponding lapse shift is δL/L ~ −δT/T. The variational derivation, using K̂_vac, gives no corresponding shift in the spatial sector because δ⟨K̂_vac⟩ depends only on the geometry, not on the state's energy content (to first order, the area variation dominates). The mismatch per unit time is:

|δL_thermal − δL_variational| / L ~ ΔE · ℓ² / A

**Numerical example:** Take a causal diamond of size L ~ 1 m (laboratory scale). The regulated vacuum energy in the diamond is E_vac ~ L³/ℓ⁴_Planck · (ħc/L) ~ (L/ℓ_Planck)² · E_Planck. With ℓ_Planck ~ 1.6 × 10⁻³⁵ m and E_Planck ~ 1.2 × 10¹⁹ GeV: E_vac ~ 10⁶⁸ GeV. A perturbation of ΔE ~ 1 J ~ 6 × 10⁹ GeV gives δT/T ~ 10⁻⁵⁸ — unobservably small.

**But:** for a very small diamond (L ~ 10² ℓ_Planck) and a state with O(1) excitation above the vacuum, the mismatch is O(1). This means the lock *can* fail at the Planck scale, and the only thing making it hold at macroscopic scales is the enormous hierarchy between the Planck scale and the energy scale of ordinary matter — which is a contingent fact about our universe, not a structural feature of the framework.

### Why this is lethal to L5

L5 claims the lock is "structural" — that it follows from "one operator, one calibration." But the actual physics is:

1. The two faces use different K̂ operators in practice (full vs. vacuum modular Hamiltonian)
2. The equality of their calibrations holds only for the exactly equilibrium (vacuum) state
3. The size of the mismatch scales as ΔE · ℓ²_Planck / A, which is small at macroscopic scales only because of the Planck hierarchy
4. There is no *in-principle* mechanism preventing the two faces from decoupling; the "lock" is approximate and contingent on the state being near-equilibrium

This is the same problem as Q7 in the referee packet, now quantified.

### Verdict

L5 does not prove a structural lock. It demonstrates that the two faces coincide for the vacuum state — which is already known because Bisognano–Wichmann applies to the vacuum. Away from equilibrium, the two calibrations diverge, with the mismatch scaling as ΔE · ℓ²_Planck / A. The lock is an equilibrium approximation, not a theorem, and L5 overstates its scope.

---

## Summary

| # | Target | Finding | Lethality |
|---|--------|---------|-----------|
| 1 | L3 normalization | Isotropy premise holds only in dust rest frame; mini-theorem is frame-bound, not covariant | Fatal to the claim of independent derivation |
| 2 | L3 non-dust | Ψ = Φ degradation is parametric with GR; no novel constraint; the framework restates GR, doesn't predict γ = 1 | Fatal to the claimed novel content |
| 3 | L5 decoupling | Modular generator's two faces give different calibrations away from equilibrium; mismatch scales as ΔE·ℓ²_Planck/A; lock is an approximation | Fatal to the structural-lock claim |
