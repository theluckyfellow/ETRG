CLOSING STATEMENT — attributed to Kimi-K2.7-Code  
ETRG-0 / ETRG-1 consolidation, July 2026

1. Code audit

`lock_check.py` is a clean SymPy linearized-GR verification. It correctly checks the lock note’s L1–L3: the Ricci-null contraction, the transverse acceleration law, and the 4GM/b photon deflection for Φ=Ψ. It does not, and cannot, test the deeper claim that the entropic input *produces* the trace-free sector; it only confirms that once the sector is written, light bending reads it. Scope is limited to static, weak-field, isotropic gauge.

`q10_lattice_check.py` is the numerically strongest script. It diagonalizes a free-fermion chain, perturbs the Hamiltonian, and shows that coarse-graining in the *modular* eigenbasis preserves the first-law slope (ratio → 1) while coarse-graining in the site basis does not. Moving off half filling to avoid particle-hole symmetry was the right fix. Weaknesses: it uses only an on-site Gaussian potential perturbation; a hopping perturbation would be a useful control. The log-log residual-slope fit mixes the linear and quadratic regimes unless one carefully restricts the small-ε window, and there is no finite-size scaling scan to argue thermodynamic/continuum convergence.

`coherent_thermal_check.py` implements the Gaussian-formalism test of P2: coherent displacement leaves the entanglement spectrum unchanged (ΔS_ent = 0) but contributes linearly to modular energy, while incoherent noise of matched energy produces first-order ΔS_ent. The modular-matrix construction and self-test look sound. The plot is that the absolute relative entropy for the noise case goes negative at small dE, and the script acknowledges that this is numerical cancellation below precision. The regularization (adding isotropic thermal noise to both states) is defensible but makes the toy a regulated Gaussian computation, not a literal BEC phonon calculation.

`label_freeness_toy.py` is logically the most important toy, because A7’s nonlinear lapse is where signaling and constraint-algebra worries live. Run 2 (A7 reconstruction) and Run 3 (state-functional feedback) give fidelities ≈ 0.9998. Run 4, the “label-consuming” control, drops to mean fidelity 0.898 — a clear qualitative distinction. Run 5, coupling the lapse itself at cap 20, gives a disastrous min fidelity of 3e-3, which the note attributes to stiffness at the stasis singularity. That conclusion is plausible but not fully demonstrated by the output as printed; the toy should have included the step-halving curve in the committed results. General weakness: two-mode Bose-Hubbard is far from a continuum field theory; nothing here proves that the same distinction survives in a back-reacting quantum field.

Across all scripts the numerics are single-parameter demonstrations, not systematic studies. There are no finite-size scans, no interaction-strength sweeps, no error bars, and the conda/matplotlib dependency is unmet (`Plot skipped`). Treat them as existence proofs and sanity checks, not as a full evidence body.

2. Verdict on the corpus

The corpus is best classified as a *research program with a falsifiability agenda*, shading into *reinterpretation*. It is not yet an independent physical theory, and the documents themselves increasingly admit this. The assembly is genuinely skillful: it stitches established ingredients — Jacobson/FGHMV entanglement→geometry, Barontini’s entropic time, Bisognano-Wichmann/Tolman-Ehrenfest, and the unimodular-gravity literature — into a closed loop with explicit axioms and named vulnerabilities. The referee packet’s kill criteria and Q-checkpoints are a model of honest adversarial packaging.

But the loop still leans on imported theorems at every load-bearing joint. Where the documents are theorem-grade — the entanglement first law, the trace-free equivalence, the Q10 modular-covariance lemma — the results are sound. Where they extrapolate — exact Lorentz invariance, de Sitter/Λ, the full constraint algebra under back-reaction, the continuum limit of the Q10 selection principle — the corpus marks the gap rather than crossing it. As the lock note and Q10 note concede, the strongest claim is that light bending is the observational readout of the trace-free sector; the weakest is that this constitutes a novel prediction rather than a reformulation of standard GR+QM.

3. Strongest and weakest elements

Strongest:
- The L1–L3 lock argument: the recognition that horizon-thermodynamic derivatives produce the trace-free Einstein sector and that light bending directly measures Φ+Ψ. The symbolic check is unambiguous, and the retraction of v0.1’s overbroad “without Bianchi” claim makes the surviving version durable.
- The Q10 modular-covariance selection principle and its lattice verification. Using Takesaki to constrain admissible coarse-grainings is the most genuinely new conceptual move in the corpus; the free-fermion check shows it is not vapor.
- The adversarial/referee architecture itself: numbered claims, kill criteria, open Q-checkpoints, and round-by-round adjudication. It disciplines the hype and makes the remaining gaps explicit.

Weakest:
- Q1 / back-reaction / label-freeness. The label-freeness toy is suggestive but does not prove anything for continuum fields, and Run 5’s strong-coupling behavior is unresolved in the committed output. The two-layer defense (derivation vs. description) is reasonable but still assumes what needs to be shown: that Ñ[ψ] never leaks into geometry’s source terms.
- De Sitter / positive Λ and cosmological Q3. The framework is built in AdS-friendly causal-diamond/wedge language. The Q10 defense explicitly fails for FRW comoving observers and de Sitter, and Λ remains an embarrassment inherited from the entanglement-geometry literature.
- The continuum / calibration gaps. The σ constant mapping entropy flow to seconds is empirical per system; exact Lorentz invariance is assumed; and all numerics are toy/lattice demonstrations rather than continuum predictions.

4. One addition that would most improve the numerics story

A finite-size scaling study of the Q10 modular-coarse-graining check: run `q10_lattice_check.py` at fixed aspect ratio ℓ/L across multiple chain lengths, fillings, and perturbation classes (on-site, hopping, non-local), and extract the modular/fine-entropy ratio and residual slope as functions of 1/L. This would turn the single-point demonstration into evidence that the modular-covariance selection principle survives the thermodynamic limit and is not an artifact of one filling or one perturbation shape.

5. Recommended next step

Compute the off-equilibrium δ_lock correction in a concrete lattice or field-theory model and check the covariance claims of U3: whether the relative-entropy correction yields a local, covariant, trace-free source, or whether foliation dependence sneaks back in at second order. This is the sharpest internal question left by the corpus — the lock note’s quantified deviation scale and the unimodular-clock note’s Q1 exposure meet there. A positive result would elevate the lock to a true off-equilibrium theorem; a negative result would kill or severely wound the program. It is also tractable with the existing free-boson/fermion machinery and is the obvious bridge between the current numerics and the field-theoretic claims.
