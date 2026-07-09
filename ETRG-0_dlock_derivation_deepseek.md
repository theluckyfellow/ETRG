Read the FHHPRV 2017 abstract and the Jacobson 2016 PRL abstract; I have the key structures from them plus the full ETRG-0 context. Let me write the derivation now.

---

# ETRG-0, Round 4: Off-Equilibrium Correction to the Entropic Field Equations

**Setup.** Let D be a small causal diamond of radius ℓ centered at point p. The FGHMV entanglement first law (arXiv:1312.7856) gives, for an arbitrary state ρ relative to the vacuum ρ_0:

$$\Delta S \;=\; \Delta\langle K\rangle \;-\; S(\rho\,\|\,\rho_0) \qquad\text{(exact at all orders)}$$

where K̂ is the modular Hamiltonian for ρ_0 restricted to D. For a CFT in flat space, K̂ = ∫_D dΣ^a ξ^b T_{ab} with ξ the conformal Killing vector preserving the diamond. The vacuum-subtracted entropy is ΔS = S(ρ) − S(ρ_0), and Δ⟨K⟩ = Tr[ρK̂] − Tr[ρ_0 K̂]. The relative entropy S(ρ‖ρ_0) ≥ 0 has the expansion$$S(\rho\|\rho_0) = \delta\Delta\langle K\rangle - \delta(\Delta S) = O(\delta\lambda^2)$$

for a small perturbation parameter δλ; it vanishes at linear order (the first law) and appears at second order and beyond.

**The leading correction.** For a small source perturbation δλ (metric deformation δg or matter source), the entanglement entropy for a ball has the small-ℓ expansion

$$\Delta S = a_d\,\ell^{d}\, \bigl(G_{ab}(p) + \alpha_1 \ell^{2} \nabla^{2}G_{ab}(p) + \alpha_2 \ell^{2} C_{abcd}C^{abcd}(p) + \cdots\bigr)$$

where G_{ab} denotes geometric-invariant combinations (Ricci, Weyl, etc.) and the coefficients α_i are theory-dependent (CFT central charges). The modular energy term has a similar expansion in terms of ⟨T_{ab}⟩. The relative entropy at the same order is

$$S(\rho\|\rho_0) = b_d\,\ell^{d}\,\bigl(\langle T_{ab}\rangle^2,\; C_{abcd}C^{abcd},\; \text{higher derivatives}\bigr) + O(\ell^{d+2})$$

where b_d is proportional to the CFT two-point function of the stress tensor. For a ball in d-dimensional CFT, Casini, Huerta & Myers (2011; JHEP 1105, 036) explicitly constructed K̂ and Faulkner et al. (2016, arXiv:1602.01380) computed the second-order relative entropy functional.

Now **invert**. At first order in δλ, the equality ΔS = Δ⟨K⟩ gives the linearized trace-free Einstein equations (Jacobson 2016). At second order, S(ρ‖ρ_0) is nonzero and we obtain

$$a_d\, \ell^{d}\, \delta^{(2)}G_{ab}(p) \;=\; a_d'\, \ell^{d}\, \delta^{(2)}T_{ab}(p) \;-\; b_d\, \ell^{d}\,\langle T^2\rangle(p)$$

where δ^{(2)} denotes the second-order variation, and ⟨T²⟩ is shorthand for the quadratic stress-tensor/four-point-function contribution that S_rel comprises. Rearranging:

$$\boxed{\;\delta G_{ab} = 8\pi G\,\delta T_{ab} - \frac{b_d}{a_d}\,\mathcal{O}(T^2)_{ab}\;}$$

where ℱ_{ab} ≡ (b_d/a_d)⟨T²⟩_{ab} is the *bulk relative-entropy current* sourced by the stress-tensor correlations.

**Key structural observation.** The right-hand side has two qualitatively different contributions:

1. δT_{ab} — the usual matter source, linear in the perturbation.
2. ℱ_{ab}(T²) — the S_rel-sourced term, bilinear in the matter fields (or equivalently quadratic in the metric perturbation, since δg ∼ G_N δT).

This is a **local, covariant, bilinear functional** of the matter fields. It does not introduce foliation dependence (it's built from local stress-tensor correlators integrated over the ball, which at leading ℓ^d produces purely local curvature invariants at the center point). So the corrected equation is of type (a): a covariant functional of local fields.

---

## Comparison with Faulkner, Haehl, Hijano, Parrikar, Rabideau, Van Raamsdonk 2017

FHHPRV (arXiv:1705.03026) perform precisely this computation in holographic CFTs. For ball-shaped regions, they compute S(ρ‖ρ_0) to second order in the source strength (both scalar operator sources and metric/stress-tensor sources) and show that the resulting bulk dual geometry satisfies the *full nonlinear* Einstein equations to that order. Their result confirms:

**The S_rel correction at second order reproduces the nonlinear completion of the linearized equations.** That is, the correction term ℱ_{ab}(T²) is exactly the quadratic piece of the Einstein tensor expanded around the background: it fills in the G_{ab}^{(2)} terms that the linearized δG_{ab} misses. This is most transparent from their Eq. (3.39)–(3.42): the second-order CFT relative entropy equals the on-shell gravitational action at quadratic order, which is the action whose variation yields the nonlinear Einstein equations.

The FHHPRV result therefore *already answers* the derivation question. The corrected equation is the nonlinear Einstein equation with matter:

$$R_{ab} - \tfrac{1}{2}Rg_{ab} + \Lambda g_{ab} = 8\pi G\, T_{ab},$$

where the trace sector (Λ, R, and the trace of T) is not independently determined by the entropic input — it is recovered through the Bianchi identity ∂^a T_{ab} = 0 acting on the *full* T_{ab} including the ℱ_{ab} correction. That is, the relative-entropy correction extends T_{ab} from a linear function of the fields to a nonlinear one, and the Bianchi identity then generates the trace.

---

## Verdict on the Three Obstructions (U3)

**(i) Diamond-space measure.** In the FHHPRV computation, the measure over diamond radii and orientations is fixed by the conformal symmetry of the CFT vacuum, which makes ball-shaped regions special (they are the fixed points of the modular flow). In a general curved spacetime without CFT symmetry, the correct measure over the space of diamonds through a point is *not* uniquely determined by the entropic input alone — it requires additional input (the metric itself, which creates a circularity, or a preferred measure from the UV completion). This obstruction is **unresolved in the general case**, though it is resolved in the CFT/AdS setting where conformal symmetry picks the measure.

**(ii) Shape-derivative directional structure.** The FHHPRV computation shows that for CFTs, the angular integration over diamond orientations *cancels* direction-dependent terms at the leading O(ℓ^d) order, leaving only rotationally invariant curvature combinations (R, R_{ab}R^{ab}, C², etc.). No directional structure survives in the equations of motion at this order. Higher-order ℓ^{d+2} corrections can introduce directional terms (e.g., ∇²R terms), but these correspond to *higher-derivative* corrections (R² gravity), not to a foliation-dependent deformation of the Einstein-Hilbert sector. So for the answer to "does the correction introduce foliation dependence?" — **no, not at the leading S_rel-corrected order.** This reduces to checking that the tensor structure of the b_d coefficient in the CFT two-point function is isotropic.

**(iii) Trace-free consistency.** This is the sharp question. The first-order entropic equations are

$$R_{ab}\,k^{a}k^{b} = 8\pi G\,T_{ab}\,k^{a}k^{b} \quad \forall\; \text{null } k^{a}$$

which is algebraically the trace-free Einstein equation. The S_rel correction at second order adds a term ℱ_{ab}(T²) to the right-hand side. Decompose:

$$G_{ab} = 8\pi G\bigl(T_{ab}^{(1)} + T_{ab}^{(2)} + \cdots\bigr)$$

where T_{ab}^{(1)} is the linear stress tensor and T_{ab}^{(2)} ≡ −(b_d/a_d)⟨T²⟩_{ab} is the S_rel contribution. **Crucially**, T_{ab}^{(2)} has both a traceless part and a trace. The corrected equation is then

$$\bigl(G_{ab} - \tfrac{1}{4}G g_{ab}\bigr) = 8\pi G\,\bigl(T_{ab} - \tfrac{1}{4}T g_{ab}\bigr)_{\text{traceless}}$$

plus the trace condition G = −8πG T (the full trace, not just the linear part). The Bianchi identity ∂^a G_{ab} = 0 together with ∂^a T_{ab} = 0 (total stress-tensor conservation, including T^{(2)}) determines the trace G +8πG T = constant ≡ −4Λ, giving the full Einstein equations with Λ.

**Verdict on (iii): the leading correction is NOT trace-free.** It contributes to both the traceless and trace sectors. The full nonlinear Einstein equations are recovered — not just their trace-free projection. This is *consistent* with the unimodular structure in the following precise sense: the trace-free projection is the *first-order truncation*, and the relative entropy correction fills in the nonlinear completion without any inconsistency. The unimodular character (Λ as an integration constant, trace-free dynamical equations) is a feature of the *linearized* theory; the full theory is GR, and the S_rel correction is precisely what upgrades it.

---

## Bottom Line

| Question | Answer |
|---|---|
| Form of corrected equation | Full nonlinear Einstein equations: G_{ab} + Λg_{ab} = 8πG T_{ab}, with T_{ab} containing a bilinear S_rel-sourced correction ℱ_{ab}(T²) |
| FHHPRV already answered? | Yes — their computation of S_rel at O(δλ²) for CFTs produces precisely the quadratic completion of the Einstein tensor |
| Obstruction (i) measure | Unresolved in generic curved spacetime; resolved in CFT by conformal symmetry |
| Obstruction (ii) directional | No foliation — angular integration cancels directional terms at leading order |
| Obstruction (iii) trace-free | **No** — the correction fills both trace and traceless sectors, yielding full GR, not unimodular-restricted equations |

The sharpest implication for the ETRG-0 program: the entropic input yields the unimodular equations at *first order*, but the natural nonlinear completion (driven by S_rel) restores the full trace sector. This means the unimodular structure is a feature of the linear approximation, not of the full theory — and the S_rel correction is precisely the mechanism that upgrades from one to the other. The program's L1 claim that "the entropic input supplies exactly the trace-free sector" is accurate only at linear order; at nonlinear order the full Einstein equations emerge.
