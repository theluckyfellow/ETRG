# ETRG-0 Addendum: The Lock Note

**Sharpening S3: the factor of two as a null-sector readout, and A4 as a projection of A5.**
*Version 0.2 — July 2026. Self-contained; companion to ETRG-0_referee_packet.md.*
*v0.1 → v0.2: revised after one adversarial round (DeepSeek-V4-Pro, GLM-5.2, Kimi-K2.7); adjudication appendix at the end. The central claims survived in weakened, more precise form; the "without Bianchi" novelty claim of v0.1 was wrong and is retracted.*

## Why this note exists

Three independent first-pass constructions (July 2026), each responding blind to the constructive challenge in the referee packet, converged on the same architecture: an entropic-time temporal sector giving Newton, a spatial sector needed for the light-bending factor of two, and the requirement that the two sectors be locked at equal strength. All three *assumed* the lock. One (Kimi) stated the gap explicitly: "the factor of 2 is obtained because I assumed the temporal and spatial entropy gradients are equal — motivated but not proven."

This note upgrades the lock from assumption to argument — with the scope of each claim now stated exactly.

## L-claims

**L1 (The entropic input supplies exactly the trace-free sector).** Every horizon-thermodynamic derivation of gravitational field equations feeds its entropic input through null surfaces: Jacobson's Clausius relation δQ = T δS on local Rindler horizons (1995), the entanglement first law on causal diamonds whose null boundaries carry the modular flow (FGHMV 2014, Jacobson 2016), and Padmanabhan's null-surface variational program (2010, 2014). The reason is structural: entropy, temperature, and geometry meet operationally *only* at causal horizons (Bisognano–Wichmann, Unruh). The raw output of the entropic input is the null-projected equation

$$R_{ab}\,k^a k^b \;=\; 8\pi G\, T_{ab}\,k^a k^b \qquad \text{for all null } k^a \text{ at every point,}$$

a manifestly covariant condition (the null cone is frame-independent; both sides are scalars for each k). By the null-curvature lemma (Hawking & Ellis §4.3), this is *algebraically equivalent* to the trace-free part of the Einstein equations,

$$R_{ab} - \tfrac{1}{4}R\,g_{ab} \;=\; 8\pi G\left(T_{ab} - \tfrac{1}{4}T\,g_{ab}\right),$$

i.e. the unimodular form of gravity, in which the trace sector is undetermined and the cosmological constant enters only as an integration constant once the Bianchi identity and energy conservation are invoked (as in Jacobson 1995's own reconstruction; cf. the unimodular literature, Weinberg 1989 review, Ellis et al. 2011, and Padmanabhan's repeated emphasis that Λ arises as an integration constant in the emergent-gravity paradigm). **The precise claim is therefore not that the entropic input is "less than" the Einstein equations by a differential step, but that it is exactly the trace-free sector and is structurally silent on the trace/Λ sector.** *Status: the equivalence is a known lemma; the localization of the entropic input at the trace-free sector, stated as such, is the framing this note contributes.*

**L2 (Light reads that sector directly).** Static weak field, source rest frame, isotropic gauge:

$$ds^2 = -(1+2\Phi/c^2)\,c^2dt^2 + (1-2\Psi/c^2)\,\delta_{ij}\,dx^i dx^j .$$

In the static case Φ and Ψ coincide with the gauge-invariant Bardeen potentials, so nothing below depends on the gauge choice. Linearized: R₀₀ = ∇²Φ/c², R₀ᵢ = 0, Rᵢⱼ = δᵢⱼ∇²Ψ/c² + ∂ᵢ∂ⱼ(Ψ−Φ)/c². For a null direction k = (1, n̂) (affine rescalings multiply both sides of L1's equation by λ² and cancel):

$$R_{ab}k^a k^b \;=\; \frac{1}{c^2}\left[\nabla^2(\Phi+\Psi) \;+\; n^i n^j\,\partial_i\partial_j(\Psi-\Phi)\right].$$

A light ray's total deflection is α = (1/c²)∫∇⟂(Φ+Ψ) dl — the lensing observable depends on exactly the potential combination the null-null law sources. Light bending is the *direct* observational readout of the trace-free sector; the trace sector, the only part of the field equations the entropic input does not supply, never enters the lensing integrand. *Status: standard GR algebra; verified symbolically twice, by independent implementations (17/17 checks in `lock_check.py`, incl. the geodesic interpolation a⟂ = −∇⟂Φ − (v²/c²)∇⟂Ψ and α = 4GM/c²b).*

**L3 (Corollary: in the static weak field, the trace-free sector suffices for γ = 1 and Newton jointly).** Impose the L1 law for all null directions through every point, with a static source in its rest frame (the frame in which PPN γ is defined) and potentials decaying at infinity. For dust, T_ab k^a k^b = ρc⁴ is direction-independent, so decomposing the direction-dependent geometric term into trace and traceless parts forces the traceless Hessian of (Ψ−Φ) to vanish pointwise; the only decaying solution of ∂ᵢ∂ⱼf = ⅓δᵢⱼ∇²f is f = 0, hence **Ψ = Φ** (γ = 1), and the isotropic remainder gives ∇²(Φ+Ψ) = 8πGρ, hence **∇²Φ = 4πGρ** — Newton's normalization. With anisotropic stress π_ij the same decomposition yields ∇²(Φ+Ψ) = 8πG(ρ+p) and [∂ᵢ∂ⱼ − ⅓δᵢⱼ∇²](Ψ−Φ) = 8πGπ_ij — *identical* to linearized GR, so the framework degrades exactly as GR does, neither better nor worse (adversarially confirmed, round 1).

Three honest deflations, from round 1: (i) given L1's equivalence lemma this corollary is elementary, not new mathematics; (ii) staticity, the rest frame, and asymptotic flatness are load-bearing hypotheses — the last is what excludes the Λ ambiguity here; (iii) the corollary adds no predictive content beyond linearized GR's trace-free sector. Its value is *locational*: it shows that everything light bending measures, including the Newtonian calibration it is compared against, lives inside the one sector the entropic input writes. *Status: proof checked symbolically and adversarially; survives as a corollary with stated hypotheses.*

**L4 (The inversion — an explanation, not a prediction).** With L1–L3 the traditional puzzle inverts. In any theory whose gravitational input is horizon thermodynamics, the primary object is the trace-free/null sector. Light — a null probe — reads that sector whole: α ∝ ∇⟂(Φ+Ψ). A slow body samples only the temporal projection, a = −∇Φ, which for isotropic-stress sources carries exactly half of Φ+Ψ. Nothing extra couples to fast particles; slow particles are the degenerate probe that hides half of the native structure. The measured 2:1 deflection ratio (1.75″ vs the 0.87″ of any pure clock-rate theory) is the sampling ratio of null versus timelike worldlines through one null-native law — the observational signature that the gravitational degrees of freedom being counted entropically live on null surfaces. This is offered as the *structural explanation* of the factor of two within the entropic program; it is emphatically not a new numerical prediction (the number is GR's), and any presentation that lets a reader believe otherwise fails packet checkpoint Q9. *Status: interpretation; checkable content is L1–L3.*

**L5 (One generator, two faces — exact at entanglement equilibrium, approximate elsewhere, with a stated deviation scale).** At a causal horizon with the field in (or infinitesimally near) the vacuum, the boost/modular generator K̂ plays both roles at once:

- *Thermality face (temporal sector):* the reduced state is thermal in K̂ (Bisognano–Wichmann) at the Unruh temperature; with Tolman–Ehrenfest, the position dependence of the modular temperature defines the lapse, √(−g₀₀) = T_∞/T(x) — axiom A4, derived rather than postulated *in this regime*.
- *Variational face (spatial sector):* δS = δ⟨K̂⟩ with the single calibration S = A/4Għ sources the spatial geometry (axiom A5).

One operator, one calibration constant, two projections: at entanglement equilibrium the sectors cannot be rescaled independently. **Scope restriction (round 1):** away from equilibrium the two faces draw on *different* operators — the thermality face on the full modular Hamiltonian K̂ = K̂_vac + ΔK̂ (nonlocal, non-geometric for excited states), the variational face on K̂_vac (through the vacuum-calibrated area law) — and the calibrations drift apart with fractional mismatch of order **ΔE·ℓ²_Planck/A** for excitation energy ΔE through a horizon of area A. For laboratory or astrophysical horizons this is ≲10⁻⁵⁸; for Planck-scale causal diamonds it is O(1). The lock is therefore an *equilibrium theorem with a quantified validity domain*, not an unconditional structural fact — this converts packet checkpoint Q7 from an open worry into a stated deviation scale, and marks where the framework's predictions could in principle depart from GR (strong non-equilibrium, Planck-scale diamonds). A further gap identified in round 1 and left open: the temporal sector's operational partition (Barontini's coarse-grained observed/unobserved split) and the spatial sector's partition (region/complement) are *different tensor factorizations*; the lock additionally requires that they coincide at horizons. Bisognano–Wichmann makes this plausible (the wedge algebra defines both) but it is not proven here — registered as new checkpoint **Q10** in the packet. *Status: theorem-grade at entanglement equilibrium; conjecture with stated deviation scale beyond it; Q10 open.*

**L6 (What is imported — the honest ledger, revised).** (a) The all-null-directions requirement is algebraically the trace-free Einstein equations (L1); the entropic derivation does not evade that content, it *is* that content — the retraction of v0.1's "without Bianchi" claim. What remains genuinely underived by the entropic input is the trace/Λ sector, recovered only via the Bianchi identity plus matter energy conservation, with Λ as an integration constant (the unimodular situation; partially defuses Q8's sting — Λ is unpredicted but unobstructed). (b) Asymptotic flatness excludes the Λ ambiguity in L3's regime. (c) The local-equilibrium, equation-of-state character of the Clausius input (Jacobson's own caveat) is inherited, now with L5's quantified deviation scale attached. (d) A Lorentzian causal structure — something for "null" to mean — is presupposed; A6's substrate question is untouched. (e) The coincidence of the two partitions (Q10) is assumed at horizons. The claim that survives all of this: *the specific metric sector that light bending measures is the sector the entropic law writes directly, and the 2:1 ratio is that law's structural signature.*

## Requested attacks (round 2, when budget allows)

1. **Q10:** prove or refute that the Barontini-type coarse-grained partition and the region/complement entanglement partition define the same modular structure at a causal horizon (they must, for L5's two faces to share one K̂).
2. **L5's deviation scale:** is ΔE·ℓ²_Planck/A the right scaling? An independent derivation (e.g. via relative entropy S(ρ‖ρ_vac) bounding the calibration drift) would firm up the validity domain.
3. **Prior art, second sweep:** L1's "trace-free localization" framing and L4's inversion — still unlocated in the literature after one sweep (nearest: Padmanabhan's null-surface program; Eddington 1920 for the classic space+time-curvature account). A targeted search of unimodular-gravity and emergent-gravity reviews could yet find it published.

## Appendix: Round-1 adjudication (July 2026)

| Attack | Source | Verdict | Disposition |
|---|---|---|---|
| "All null directions ≡ trace-free Einstein (Hawking–Ellis); 'without Bianchi' is vacuous" | GLM | **Sustained** | v0.1 novelty claim retracted; L1/L3/L6 rewritten around the trace-free localization, which is the defensible content |
| L3 proof gauge-dependent as written | GLM | Sustained (repairable) | Static Φ, Ψ are Bardeen potentials; gauge-invariance now stated in L2 |
| L5 conjecture presented as claim | GLM | Sustained | L5 restricted to entanglement equilibrium; remainder labeled conjecture with deviation scale |
| Temporal and spatial sectors use *different factorizations*; coincidence at horizons unproven | GLM | Sustained, new | Registered as Q10; the sharpest new vulnerability found in round 1 |
| "L3 frame-dependent, hence vacuous" (boosted-dust counterexample) | DeepSeek | **Overruled in part** | The null-cone quantification is frame-independent and the law covariant; the boost example varies the source while forgetting the metric's matching direction-dependence. Surviving residue: staticity/rest-frame/decay are load-bearing hypotheses, now stated in L3 |
| "Anisotropic stress: degradation parametric with GR ⇒ no novel content" | DeepSeek | Sustained as calculation; verdict recontextualized | The identical degradation was a *requested consistency check* and it passed; the no-new-predictions point was already conceded (Q9, L6) — L4 reworded so it cannot be misread as a numerical prediction |
| Lock decouples off-equilibrium; mismatch ~ ΔE·ℓ²_Planck/A | DeepSeek | **Sustained — most valuable finding of the round** | Q7 converted from open worry to quantified validity domain in L5 |
| 17/17 symbolic verification of L2/L3 algebra + geodesic interpolation + 4GM/c²b | Kimi | Confirmed | `lock_check.py`, committed c2883cb; independent of the local check `ricci_check.py` |

## References to add to the packet

T. Padmanabhan, Rep. Prog. Phys. 73, 046901 (2010) · T. Padmanabhan, Gen. Rel. Grav. 46, 1673 (2014) (null-surface variational principle; nearest prior lineage to L1) · Hawking & Ellis, *The Large Scale Structure of Space-Time*, §4.3 (null-curvature lemma) · S. Weinberg, Rev. Mod. Phys. 61, 1 (1989) and G. F. R. Ellis et al., Class. Quantum Grav. 28, 225007 (2011) (unimodular gravity; Λ as integration constant) · A. S. Eddington, *Space, Time and Gravitation* (1920) (the classic space+time-curvature account of the factor of two). Any prior statement of the L1 localization or L4 inversion found by reviewers supersedes this note's framing claims.
