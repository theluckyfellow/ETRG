---

## 1. Prior Art on U4

**The specific bridge that U4 makes — from a thermodynamic/entropic derivation of gravity (Jacobson lineage) to unimodular four-volume time (Henneaux-Teitelboim / Unruh-Wald) as a problem-of-time resolution — appears to be novel. The two halves exist separately in the literature; nobody has connected them.**

Here is what each relevant party does and does not do:

**Alonso-Serrano & Liška (2020, arXiv:2008.04805; 2021 review arXiv:2112.06301; 2024, arXiv:2409.06645):** These establish the first half — thermodynamic derivations of gravity (Clausius entropy / entanglement equilibrium / causal-diamond thermodynamics) yield unimodular gravity (more precisely, Weyl transverse gravity), not full GR. The cosmological constant emerges as an integration constant; energy-momentum conservation is weakened. **They do not discuss the problem of time, the Henneaux-Teitelboim clock, four-volume as evolution parameter, or any quantum-gravitational frozen-formalism issue.** Their focus is on the classical field equations and the cosmological constant problem.

**Smolin (2009, arXiv:0904.4841; 2010, arXiv:1008.1759):** These establish the second half — unimodular gravity, when quantized (in Plebański/Ashtekar/LQG formulations), yields Schrödinger evolution in a physical time variable equal to elapsed four-volume, addressing the frozen-formalism problem. Smolin explicitly reviews the Unruh-Wald-Sorkin proposal and discusses "the problems of time" in the title. **But his starting point is unimodular gravity as a theory chosen for its cosmological-constant-problem resolution, not a thermodynamic/entropic derivation.** The thermodynamic input is absent.

**Barvinsky & Kamenshchik (2017, arXiv:1705.09470):** Generalized unimodular gravity with a dark fluid, spatially open cosmology, initial conditions. No connection to thermodynamic derivations of gravity or to the problem of time.

**Padmanabhan:** His emergent-spacetime program (e.g., "Gravity and Spacetime: An Emergent Perspective," and the equipartition/degrees-of-freedom papers) treats gravity as thermodynamic/emergent but does not invoke unimodular structure, four-volume time, or the Henneaux-Teitelboim clock. No InspireHEP result connects Padmanabhan to "cosmic time" or "emergent time" in the unimodular sense.

**InspireHEP combined searches** for "thermal time AND unimodular," "entropic time AND unimodular," "unimodular AND problem of time," "relational time AND unimodular," "four-volume AND time AND entropic AND unimodular," "frozen formalism AND unimodular AND evolution" — all return **zero results**.

**Connes-Rovelli thermal time hypothesis:** Searches for "thermal time AND cosmological constant AND unimodular" also return zero. The thermal time hypothesis (von Neumann algebra flow) is a separate lineage from the Unruh-Wald four-volume clock; nobody appears to have connected them to unimodular gravity jointly.

**Bottom line:** The two ingredients (thermodynamics → unimodular field equations; unimodular Hamiltonian structure → four-volume clock → frozen-formalism alleviation) exist in disjoint literatures. U4's framing — "the entropic input's silence on the trace generates the clock" — is, to the best of my knowledge, not in the literature. Whether it is a *correct* bridge is a separate question from whether it has been made before.

---

## 2. Three Strongest Referee Objections (Most Important First)

### Objection 1: U5 is not well-posed — the two clocks live in incompatible frameworks, and the "monotone relation" conjecture conflates a state-dependent quantum-information quantity with a classical Hamiltonian parameter.

τ (entropic time) is operationally defined via coarse-graining, relative entropy, and KMS/modular structure in the FGHMV quantum-information setup. It is a state-dependent flow parameter that tracks entropy exchange between fine-grained and coarse-grained descriptions. Its definition requires a quantum state ρ and a reference state ρ_vac.

T (unimodular time) is the conjugate variable to Λ in the Henneaux-Teitelboim constraint algebra. It is a *global* parameter of the classical Hamiltonian theory, defined by ∫√(−g) d⁴x over the entire spacetime. It does not depend on any quantum state; it is a coordinate on the reduced phase space after gauge-fixing the conformal mode.

The conjecture dT/dτ = f(σ; state) presupposes that both quantities can be simultaneously defined and compared in the same regime. But:
- **τ is not defined in the classical unimodular Hamiltonian framework** — it comes from a different formalism (relative entropy on causal diamonds, quantum-information coarse-graining).
- **T is not defined in the quantum-information framework** — it requires the Henneaux-Teitelboim phase-space structure, which the entropic derivation does not produce (see Objection 3 below).
- The Tolman argument ("entropy production per unit four-volume is fixed by local temperature") assumes a spacetime with a well-defined thermal state and a temperature field. In the unimodular framework, T is the variable that *replaces* the Hamiltonian constraint; using it as a coordinate against which to measure entropy production is circular if the goal is to show the two clocks are related.

The conjecture is not false — it is not reachable as a well-posed claim because the two sides are not defined in the same theoretical framework. At best, in a semiclassical limit where both might be approximated, one could look for a numerical coincidence, but the conjecture as stated is a category error.

### Objection 2: The toy-model test in U5 is vacuous — "four-volume" in a Bose-Hubbard mini-universe is not a geometric quantity, and any choice is arbitrary.

U5 proposes testing in a "Barontini-class two-sector simulation" (Bose-Hubbard lattice). The note itself flags this: "what is 'four-volume' in a Bose-Hubbard mini-universe?" But it does not resolve the flag. A Bose-Hubbard model has a discrete lattice, no metric, no determinant of a four-metric, and no continuum spacetime. The "integrated observable 'size' of the bright sector" is a number of sites or a particle-number integrated over a discrete time — it is not a four-volume in any sense that carries the Hamiltonian content of the Henneaux-Teitelboim construction.

The entropic time τ in such models is defined via entanglement/entropy contrast between sectors — a quantum-information quantity with no geometric interpretation. Comparing it to an arbitrary "size" analogue of four-volume cannot falsify the conjecture in a meaningful way, because both quantities are analogues of unclear status, and the relation between them depends on which analogue you choose. The test cannot fail for the right reason; it can only fail because the analogue was wrong. This is not a cheap test of U5 — it is a test of nothing.

### Objection 3: U4's core inference is invalid — the entropic derivation's "silence on the trace" does not produce the Henneaux-Teitelboim clock; it merely permits a choice of Hamiltonian formulation, and the clock is an extra choice, not a structural consequence.

U4 claims: "the entropic derivation produces, from one input: (i) the trace-free field equations, and (ii) by its very silence on the trace, an integration constant with a global clock attached."

This conflates two things:
- The entropic derivation (Jacobson/Alonso-Serrano/Liška) shows that the *equations of motion* are the trace-free Einstein equations, with Λ undetermined. This is a statement about the Lagrangian/field-equation level.
- The Henneaux-Teitelboim structure is a specific *Hamiltonian formulation* that exploits the trace-undetermination to promote the zero-mode of the Hamiltonian constraint to a true Hamiltonian with T = ∫√(−g) d⁴x as its conjugate. This is a statement about the phase-space structure.

Classical equivalence of equations of motion does not imply equivalence of Hamiltonian structures. The trace-free equations can equally well be formulated as Weyl transverse gravity (which is what Alonso-Serrano & Liška actually advocate), which has *different* local symmetries (Weyl + transverse diffeomorphisms) and a *different* Hamiltonian structure. Weyl transverse gravity does not carry the Henneaux-Teitelboim four-volume clock. So the "clock" is not generated by the entropic input's silence — it is generated by *choosing* the Henneaux-Teitelboim formulation over the Weyl transverse formulation. The entropic input is neutral between them. U4's language ("the structure of what it cannot write is itself a clock") makes a choice sound like a logical consequence.

This matters for the note's rhetorical structure: U4 presents the clock as a *bonus* delivered automatically by the entropic derivation. It is not automatic. It requires an additional Hamiltonian-formulation choice that the entropic derivation does not determine.

---

## 3. Does U4 Survive Kuchař 1991?

**No — more of U4 is dead than the note admits.**

Kuchař's 1991 critique ("The Problem of Time in Canonical Quantization of Gravity," PRD 43, 3332) is not merely about the *scope* of the unimodular resolution (global vs. local, one problem vs. several). It has a deeper thrust that U4's "honest import" does not fully engage:

**Kuchař's structural argument:** The problem of time is not a single problem but a cluster — frozen formalism, multiple-choice, observables, Hilbert space inner product, semiclassical limit. Unimodular time addresses *only* the frozen formalism. But Kuchař's point is not just "you haven't solved the others." His point is that the unimodular *reformulation changes the theory* — the constraint algebra is different, the gauge group is reduced (volume-preserving diffeomorphisms vs. full diffeomorphisms), and the Dirac observables are different objects. By choosing unimodular gravity, you are not merely choosing a clock; you are choosing a *different theory* with a different set of unsolved problems. You cannot fall back to full GR's Hamiltonian structure when you need many-fingered time or the standard Dirac observables.

**What U4 admits:** "T is one global time, not a local many-fingered one — it alleviates the frozen-formalism problem, not the multiple-choice problem." This is honest about scope but does not acknowledge the structural point. The note frames the unimodular clock as an *addition* to the entropic derivation's toolkit. But if the entropic derivation forces unimodular structure (as U1 claims, citing Hojman-Kuchař-Teitelboim), then it also *forces* the unsolved problems that come with it — the different gauge group, the different observables, the different Hilbert space. These are not optional side-effects; they are the theory. The note frames the clock as a benefit ("produces a clock") when the same forcing can equally be read as a *limitation* ("locks you into a theory where the other problems of time cannot be addressed by the standard tools").

**What U4 does not admit:** The "honest import" of Kuchař's caveat is framed as if the unimodular resolution is a *partial* success (frozen formalism solved, others open). But Kuchař's deeper argument is that the unimodular resolution is not a partial success — it is a *trade*: you trade the frozen formalism for a different set of structural problems that may be harder, not easier. Specifically:
- The problem of observables becomes *more* difficult, not less, because the reduced gauge group means fewer constraints and more quantities need to be checked for gauge invariance.
- The global time T is not measurable by any local observer — it requires knowledge of the entire spacetime. This makes the "physical" evolution formal, not operational.
- The semiclassical limit is not obviously better: the Schrödinger equation in T is a *different* equation from the Wheeler-DeWitt equation, and recovering local physics from it is a nontrivial problem that Kuchař raised and that has not been fully resolved.

**Net assessment:** U4's Kuchař import survives in the narrow sense that it correctly states what T does (alleviates frozen formalism) and does not do (local many-fingered time, multiple-choice). But it is dead in the broader sense that it frames the unimodular structure as a clock-delivering bonus while not acknowledging that the same structure forecloses the standard routes to solving the other problems of time. The note says "Kuchař's caveat is imported intact" — but it imports only the *scope* caveat, not the *structural* caveat that the unimodular reformulation may make the overall problem-of-time situation worse, not better, by locking you into a theory whose remaining problems are harder than the one it solves. Combined with Objection 3 above (the clock is not forced by the entropic input but requires an additional Hamiltonian-formulation choice), U4's claim that the entropic derivation "produces" the clock overstates what the derivation delivers and understates what it costs.
