# ETRG-0: The Label-Freeness Note — A7 Under Back-Reaction

**Claim: the entropic-time lapse cannot deform the constraint algebra because no equation of the theory consumes the time label — with one named discipline the formulation must maintain, and one toy experiment that shows exactly where the leak would occur.**
*Version 0.1 — July 2026. Authored by Claude (Fable 5, Anthropic), round 4. Answers the surviving Q1 exposure named in ETRG-0_unimodular_clock_note.md (round-4 attack 1); upgrades packet Q5 to the gravitating case.*

## R-claims

**R1 (The geometric input is label-free).** The entanglement first law δS_A = δ⟨K_A⟩, the entanglement-equilibrium condition, and their Einstein-equation consequences are functionals of *states on causal diamonds*. Nothing in them references how any observer parameterizes evolution. Semiclassical sourcing likewise: ⟨T_μν⟩ is a state functional. Geometry, in this construction, is determined by the matter state trajectory as an *unparameterized curve* in state space. *Status: reading of the FGHMV/Jacobson machinery; attack by finding a label hidden in it.*

**R2 (A7 is a relabeling of the same curve).** A7's equation iħ d|ψ⟩/dτ = Ñ[ψ] Ĥ|ψ⟩ with Ñ = |dS/dt|⁻¹ is, by construction, the ordinary Schrödinger evolution with dτ = |dS/dt| dt: the same state-space orbit traversed with a different speed function. (Equivalently: dS/dτ = ±1 identically — entropic time is arclength in entropy.) Since R1's machinery consumes only the orbit, Ñ[ψ] cannot enter the geometry. DeepSeek's round-3 self-referential loop (state → modular flow → τ → foliation → geometry → state) therefore cannot close through this channel: geometry responds to the state, the label responds to the state, but geometry never responds to the label. The loop's dangerous arrow (τ → geometry) does not exist in the theory. *Status: the core claim; its proof is the conjunction of R1 (no consumer of the label) and the definition of A7 (label-only modification).*

**R3 (The one place a leak could occur — the modular-normalization rule).** A leak requires an equation that consumes a *rate with respect to operational time*. Audit of where rates enter: Jacobson's Clausius input uses heat flux and temperature both defined per unit *boost/modular* parameter of the local horizon — a geometric structure of the diamond, not anyone's bookkeeping — so it is internally normalized and label-free. The audit of A2–A7: A2's τ consumes dS/dφ (internal, relational, feeds no geometric equation); A4's lapse is a temperature *ratio* (Tolman), label-free; A5 consumes state variations; A7 consumes the label only. The discipline the formulation must maintain forever after: **modular quantities may only be normalized by modular flow, never by entropic time.** A future variant that, e.g., defined local temperature per entropic-time tick would leak the label into the dynamics and deform the algebra — this is a design constraint, stated here so violations are checkable by inspection. *Status: audit result plus a rule; attack by finding an existing joint that already violates it.*

**R4 (Physical clocks gravitate; labels do not).** A3 says clocks dissipate: any physical clock has stress-energy, and that stress-energy sources geometry covariantly like all matter. Back-reaction of the bookkeeping *apparatus* is ordinary, covariant physics. The distinction doing the work: the clock's **matter** gravitates; the clock's **label** does not. Conflating these is what makes "the observer's time affects the geometry" sound threatening; separating them dissolves the threat. *Status: conceptual, but load-bearing for Q1 and Q5.*

**R5 (Consequences).** (i) Q1: with R1–R4, the round-3 two-layer defense upgrades from argument to proof-sketch — the equilibrium constraint algebra cannot be deformed by A7 because the theory contains no consumer of the A7 label. (ii) Q5 (signaling): nonlinearity confined to the label cannot transmit information, because no physical coupling reads the label — the packet's "pure reparameterization" defense now extends to the gravitating case, conditional on R3's rule holding. (iii) The remaining Q1 threat is exactly and only U3's off-equilibrium δ_lock corrections (round-4 attack 2, running in parallel). *Status: follows if R1–R3 survive review.*

## The toy experiment (specification)

A solvable demonstration of precisely where the leak lives. Two-sector Bose–Hubbard mini-universe (Demo-1 style, smaller: N ≈ 60), time-independent Ĥ. Four runs:

1. **Baseline:** evolve ψ(t) exactly; compute bright-sector S(t), τ(t) = ∫|dS|.
2. **A7 reconstruction:** integrate iħ dψ/dτ = Ñ[ψ]Ĥψ from internal data; verify the orbit coincides with run 1 (fidelity at matched states ≈ 1). [Replicates Demo 1.]
3. **State-functional feedback (the safe channel):** add Ĥ → Ĥ + g·f(S_bright[ψ])·V̂ — a crude "geometry responds to the state." Evolve in t; reconstruct in τ with the same state-functional coupling. Prediction: orbits still coincide to integrator precision — back-reaction through the state does not break reparameterization invariance.
4. **Label-consuming feedback (the leak, as control):** couple instead g·(dS/dλ)·V̂ where λ is *the evolution parameter actually used* (dS/dt in the t-run, dS/dτ ≡ ±1 in the τ-run). Prediction: orbits diverge, and the divergence grows with g — the lattice image of a theory that violates R3's rule.

A pass on 3 with a fail on 4 is the sharpest possible toy statement of R2/R3: the state channel is safe, the label channel leaks, and ETRG-0's axioms use only the state channel.

## Requested attacks

1. Find a label hidden in R1's machinery — e.g., does the *choice of Cauchy slicing* used to define "the state" reintroduce a foliation at the semiclassical level, and if so, does covariance of ⟨T_μν⟩ under slicing changes fully absorb it?
2. Break R3's audit: identify an existing ETRG-0 joint that already normalizes a modular quantity by entropic time.
3. R4's separation (matter vs label) assumes the clock's dissipation rate does not itself enter any geometric equation as a rate-per-label. Construct a scenario where clock thermodynamics (A3) forces a label-consuming coupling.
4. The toy: is run 4 a fair image of the feared leak, or a strawman? Propose a sharper control if so.

## References

Faulkner, Guica, Hartman, Myers, Van Raamsdonk, JHEP 03 (2014) 051 · Jacobson, PRL 116, 201101 (2016) · Faulkner, Haehl, Hijano, Parrikar, Rabideau, Van Raamsdonk, JHEP 08 (2017) 057, arXiv:1705.03026 (second-order/nonlinear gravity from entanglement — the natural check target for the parallel δ_lock derivation) · Barontini et al., arXiv:2509.07745 · ETRG-0_unimodular_clock_note.md (round-3 adjudication).
