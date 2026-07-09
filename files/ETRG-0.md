# ETRG-0: Entropic-Time Relational Gravity, version 0

**A minimal axiomatized bridge between quantum mechanics and spacetime, with every joint verified numerically, verified by cited experiment, or flagged open.**

*Built July 2026, grounded in G. Barontini, "Testing the problem of time with cold atoms," Phys. Rev. Research (2026), arXiv:2509.07745, and the entanglement-geometry program (Jacobson, Faulkner et al., Ryu–Takayanagi, Van Raamsdonk).*

---

## 0. What this is, and what it is not

This document does not solve quantum gravity. It does something more modest and more checkable: it stitches together, with explicit axioms and explicit bridge equations, a single self-consistent framework in which (i) time is not fundamental but emerges as an entropic, relational parameter inside a globally stationary quantum state, and (ii) spacetime geometry is not fundamental but emerges from the entanglement structure of that same state. The stitching is honest about which joints are theorems, which are experimental facts, which are numerical demonstrations performed in the companion code (`etrg_demos.py`), and which are open conjectures. The framework is falsifiable at several points, and Section 7 states the experiments that would kill it.

The guiding thesis, in one sentence: **there is one fundamental currency — entropy relative to a partition — and both time and gravity are exchange rates of that currency.** Coarse-grained entropy exchange between subsystems supplies the flow and arrow of time; fine-grained entanglement entropy across surfaces supplies the geometry through which that time flows. At horizons, the two provably merge (Bisognano–Wichmann), which is why the framework hangs together at all.

## 1. The problem being solved

Canonical quantum gravity delivers the Wheeler–DeWitt constraint, Ĥ|Ψ⟩ = 0: the wavefunction of a closed universe is an energy eigenstate and therefore stationary. Nothing happens. Yet things manifestly happen. This is the problem of time (DeWitt 1967; for the modern treatment see Henneaux's 2024–25 Collège de France lectures on the WDW equation). Separately, general relativity delivers geometry as fundamental, yet every thermodynamic probe of that geometry — black hole entropy proportional to *area*, Unruh temperature proportional to *acceleration*, Einstein's equations derivable as an *equation of state* (Jacobson 1995) — insists that geometry is bookkeeping for something microscopic and entropic. ETRG-0 takes both hints at face value and builds the minimal structure containing them.

Two distinct entropies appear, and keeping them distinct until they provably merge is the discipline of the whole construction. The **coarse-grained entropy** S_cg is what an observer with limited resolution assigns to a subsystem; it can grow, it defines an arrow, and it is what Barontini measures. The **fine-grained entanglement entropy** S_ent = −Tr(ρ_A ln ρ_A) is exact, reversible, obeys an area law in the vacuum, and is what gravitates. They are the same functional evaluated with different states and partitions, and for the reduced state of a causal horizon they coincide exactly — the Rindler wedge vacuum is thermal (Bisognano–Wichmann 1976), so the horizon's thermodynamic entropy *is* its entanglement entropy (Bianchi–Myers 2012). A single-entropy ontology with two operational faces.

## 2. Axioms

**A1 (Timelessness).** The universe is a closed quantum system in a stationary state satisfying a Hamiltonian constraint,

$$\hat{H}\,|\Psi\rangle = 0 .$$

No external time parameter exists. *Status: postulate, standard in canonical quantum gravity.*

**A2 (Partition and entropic time).** Physics is done relative to a tensor factorization into an observed and an unobserved sector, Ĥ = Ĥ_obs + Ĥ_hid + Ĥ_coupling (Barontini's bright/dark split). Time for the observed sector is defined by entropy exchange across the coupling. With a clock variable φ inside the observed sector, following Barontini Eq. (3),

$$\tau(\lambda) \;=\; \frac{\sigma}{k_B}\int_\lambda \frac{dS}{d\varphi}\,|d\varphi| ,$$

and for a symmetric bipartition the unsigned variant τ = (σ/k_B)∫|dS| is equivalent within monotonic branches. Time *flows* when entropy flows; time *stalls* when exchange stalls; time *ends* if the coupling is switched off. *Status: verified experimentally (Barontini 2026) and numerically here (Demo 1).*

**A3 (Clocks cost entropy).** Any physical device that resolves τ into ticks must dissipate; tick resolution is bounded by entropy production per tick (Erker et al. 2017). This makes A2 not merely a definition but an operational necessity: the only readable times are entropic times. *Status: theorem in quantum thermodynamics, laboratory-supported.*

**A4 (Lapse from equilibrium; the time–time metric).** In global equilibrium, temperature and clock rate trade off along the Tolman–Ehrenfest relation T(x)√(−g₀₀(x)) = const. ETRG-0 inverts the reading: the local rate at which proper time exchanges against the global entropic/thermal time (Rovelli–Smerlak thermal time) *defines* the lapse,

$$\sqrt{-g_{00}(x)} \;=\; \frac{d\tau_{\text{proper}}(x)}{dt} \;=\; \frac{T_\infty}{T(x)} \;\equiv\; n(x),$$

and matter follows maximal aging through the resulting clock-rate field, giving the local law

$$\mathbf{a} \;=\; -\,c^2\,\nabla \ln n(\mathbf{x}) \;\approx\; -\nabla \Phi ,$$

which is Newtonian gravity. In quantum language the rest energy is modulated by the local clock rate, V = mc²(n(x) − 1), and Ehrenfest steering of the matter wave reproduces free fall — the mechanism confirmed by neutron interferometry (Colella–Overhauser–Werner 1975, qBounce). *Status: the Tolman–Ehrenfest and thermal-time ingredients are established; their use as a *definition* of the lapse is the postulate. Verified numerically here (Demo 2).*

**A5 (Spatial geometry from entanglement; fixes γ = 1).** A4 alone is Nordström's trap: a pure clock-rate (scalar) theory predicts half the observed light deflection because it supplies g₀₀ but not g_ij. The spatial metric comes from the fine-grained side. The vacuum entanglement of small causal diamonds obeys the first law

$$\delta S_A \;=\; \delta\langle \hat{K}_A\rangle ,$$

with modular Hamiltonian K_A; for diamonds/wedges the modular flow is geometric — the boost, with weight β(x) = 2π(R² − x²)/2R (Bisognano–Wichmann) — and calibrating S = A/4Għ, the first law applied to all diamonds yields the full Einstein equations (Jacobson 2015; linearized: Faulkner, Guica, Hartman, Myers, Van Raamsdonk 2014). Einstein's equations force the PPN parameter γ = 1: spatial curvature equals temporal curvature, doubling light bending to the observed 1.75″ and matching Cassini's |γ − 1| ≲ 2×10⁻⁵. The unified weak-field equation of motion, derived from the γ-metric geodesics, is

$$\mathbf{a} \;=\; -\left(1+\gamma\frac{v^2}{c^2}\right)\nabla\Phi \;+\; \frac{(1+\gamma)}{c^2}\,2(\mathbf{v}\cdot\nabla\Phi)\,\mathbf{v},\qquad \alpha_{\text{defl}} = \frac{2GM}{b\,v^2}\Big(1+\gamma\frac{v^2}{c^2}\Big),$$

so slow matter is blind to γ while light feels (1 + γ). *Status: theorem-grade within its assumptions (Jacobson/Faulkner); the two lattice-checkable pillars — the first law itself and the parabolic boost structure of the vacuum modular Hamiltonian — are verified numerically here (Demo 3).*

**A6 (Null structure and universality).** Causal cones are the propagation fronts of entanglement, not a property of any particular field. All massless excitations therefore share one cone: gravitational waves and light arrive together (GW170817: Δv/c ≲ 10⁻¹⁵), lensing is achromatic, SN1987A neutrinos kept pace. Because the entropy that gravitates is fine-grained and the dynamics unitary, no species- or mass-dependent decoherence accompanies free fall — which is why neutron interferometers see a clean unitary phase, the observation that falsifies coarse-grained (dissipative) entropic-gravity mechanisms of the Verlinde-2011 type while leaving ETRG-0 untouched. *Status: experimentally anchored.*

**A7 (Matter sector: the entropic-time Schrödinger equation).** Observed-sector dynamics is generated in entropic time with a lapse that is itself an internal functional of the state:

$$i\hbar\,\frac{d|\psi\rangle}{d\tau} \;=\; \tilde{N}[\psi]\,\hat{H}_{\text{obs}}\,|\psi\rangle, \qquad \tilde{N}[\psi] = \left|\frac{dS[\psi]}{dt}\right|^{-1},$$

reducing to ordinary quantum mechanics wherever entropy exchange is steady. Points of stasis (dS → 0) are **coordinate singularities of entropic time**: the lapse diverges, and duration information is genuinely lost to the internal observer — the internal analogue of a horizon. *Status: verified experimentally (Barontini's effective τ-Schrödinger equation reproduces his data) and numerically here (Demo 1), including quantified behavior at stasis points.*

## 3. The loop, closed

Read the axioms as a single circuit. A1 removes time. A2 restores it as entropy exchange relative to a partition, and A3 guarantees nothing finer was ever available. A4 promotes the *spatial variation* of that exchange rate to the time–time metric component, recovering Newton by maximal aging. A5 supplies the spatial metric from the entanglement first law, promoting Newton to Einstein and locking γ = 1. A6 makes the causal cones universal, protecting the construction from every differential-propagation test. A7 closes the loop by writing quantum dynamics itself in the emergent time, so that the matter whose entanglement builds the geometry is the same matter that evolves through it. The two entropies meet at horizons, where Bisognano–Wichmann makes the entanglement across the cut literally thermal at the Unruh temperature k_BT = ħa/2πc — one formula in which a (geometry, A4-side) and S_ent (A5-side) appear as two descriptions of the same modular flow.

## 4. Numerical verification (companion code: `etrg_demos.py`)

**Demo 1 — Entropic time in a closed two-sector mini-universe (A1–A3, A7).** An exact-diagonalization Bose–Hubbard analogue of Barontini's experiment: N = 120 atoms, bright/dark modes coupled by tunneling J across a "barrier," global state evolving unitarily under a time-independent Hamiltonian. The bright sector undergoes bang/crunch cycles; its entanglement entropy S(t) tracks the exchange; τ = ∫|dS| orders every event. With the barrier low, τ grows to 90.5 with a persistent arrow; raising the barrier (J → J/200 at fixed interaction) freezes τ at 0.61 — time nearly stops when exchange stops. The entropic-time Schrödinger equation of A7, propagated using *only* internal quantities (the measured τ increments and the state-derived lapse Ñ[ψ], with dS/dt computed from ṗₙ = 2 Im ψₙ*(Hψ)ₙ — no lab clock anywhere in the loop), reproduces the bright fraction with RMS error 0.058 and reconstructs 98.3% of the universe's total duration; stasis-point regularization touches 4.1% of steps and is the dominant error source, exactly as the coordinate-singularity reading predicts. *(fig1_entropic_time.png)*

**Demo 2 — Newtonian free fall from a pure clock-rate field (A4).** A 2D matter wave propagates through V = mc²(n(x) − 1) with a uniform clock-rate gradient. The packet centroid arcs on the Newtonian parabola with maximum deviation 2.1×10⁻⁴ over the full flight — the Colella–Overhauser–Werner mechanism in silico: gravity as differential aging of wavefronts, no force field anywhere in the Hamiltonian beyond the rest-clock modulation. *(fig2_clockrate_gravity.png)*

**Demo 3 — The two lattice pillars under "first law ⇒ Einstein" (A5).** On a free-fermion chain at incommensurate filling: (a) perturbing the Hamiltonian by ε and comparing the exact entanglement change of an interval against Tr(δC K) gives signal slope 1.00 and remainder slope 2.00 across three decades — the first law δS_A = δ⟨K_A⟩ holds with the theoretically exact O(ε²) remainder; (b) the reduced vacuum of an interval commutes with the *parabolically weighted* boost operator T = Σᵢ (i+1)(ℓ−1−i)/2 (c†ᵢcᵢ₊₁ + h.c.) to machine zero, ‖[ρ_A, T]‖_rel = 1.3×10⁻¹⁷, against 7.7×10⁻³ for a uniform-weight control — the lattice avatar of the Rindler boost weight β(x) ∝ (R² − x²)/2R, with the boost diagonal in the modular eigenbasis to 1.3×10⁻¹². *(fig3_first_law.png)*

## 5. Experimental checkpoint table

| Checkpoint | ETRG-0 requirement | Status |
|---|---|---|
| Newtonian limit | a = −c²∇ln n from A4 maximal aging | ✓ (Demo 2; classical tests) |
| Light deflection 1.75″ | γ = 1 forced by A5 | ✓ (Eddington → VLBI) |
| Cassini Shapiro delay | γ − 1 = (2.1 ± 2.3)×10⁻⁵ | ✓ (A5 gives exactly 1) |
| Neutron/atom interferometry (COW, qBounce) | gravity enters as unitary phase, no decoherence | ✓ (fine-grained S_ent is reversible) |
| GW170817 multimessenger | one null cone for all massless fields | ✓ (A6) |
| Clock thermodynamics | tick precision costs entropy | ✓ (Erker et al.; A3) |
| Barontini oscillating universe | τ orders events, stalls with barrier, τ-Schrödinger works | ✓ (arXiv:2509.07745; Demo 1) |
| Tolman–Ehrenfest gradient | T√(−g₀₀) constant in equilibrium | ✓ (established GR thermodynamics; A4) |

## 6. Falsifiable predictions

**P1 (Stasis phenomenology).** In any Barontini-class partitioned closed system, entropic time is the unique internal ordering parameter, its lapse is expressible as a functional of the observed-sector state alone, and stasis points behave as coordinate singularities: duration information across them is irrecoverable internally, with reconstruction error concentrated there and scaling with the fraction of stalled exchange (our Demo 1 quantifies the pattern: 98.3% duration recovery with errors localized at the 4.1% regularized steps). A barrier-height sweep should show total τ collapsing smoothly to zero with the coupling — testable now on the Birmingham apparatus.

**P2 (The seam experiment: two entropies, one horizon).** In a flowing BEC with a sonic horizon (Steinhauer geometry), ETRG-0 requires the *coarse* and *fine* entropies to lock together at the horizon: the Hawking phonon temperature extracted from density–density correlations must equal ħ/2πk_B times the modular (boost) rate that simultaneously sets the interior's entropic-time lapse, and the entanglement entropy across the horizon must obey the area law (with the 1D logarithmic correction) with a coefficient fixed by the same analogue surface gravity. Measuring T_H, S_ent, and dτ/dt independently in one apparatus and finding the predicted lock — or breaking it — is the sharpest near-term test of the whole stitching. This is, to our knowledge, the underexplored seam: entropic-*time* experiments (Barontini) and entanglement-*geometry* theory (RT/Jacobson) have never been coupled in a single measurement.

**P3 (No anomalous gravitational decoherence).** Because the gravitating entropy is fine-grained and the dynamics unitary, ETRG-0 predicts *no* excess dephasing in matter-wave interferometry attributable to gravity, at any improved precision — in direct contrast to dissipative/coarse-grained entropic-gravity models. Continued coherence in next-generation qBounce and atom-fountain experiments confirms ETRG-0; detection of gravity-correlated decoherence kills it.

**P4 (Adjacent, cautious).** If geometry is entanglement, metric fluctuations should inherit entanglement fluctuations, in the spirit of the Verlinde–Zurek proposal for interferometric holographic noise. ETRG-0 is compatible with, but does not yet sharpen, that prediction; we flag it as the natural next quantitative target.

## 7. Open problems (the honest list)

The **preferred-factorization problem**: A2 assumes a bright/dark split, but Ĥ|Ψ⟩ = 0 does not distinguish one tensor factorization from another; what selects the partition relative to which entropy flows is unsolved here as everywhere. **Exact Lorentz invariance**: entanglement cones on a lattice are Lieb–Robinson cones, approximately but not exactly relativistic; the continuum limit that makes A6 exact is assumed, not derived. **De Sitter and the cosmological constant**: the theorem-grade machinery of A5 lives most comfortably in AdS; our universe's positive Λ remains the standing embarrassment of the entire entanglement-geometry program, inherited intact by ETRG-0. **Stasis singularities**: A7's coordinate singularities are regularized, not resolved; whether a refined internal time (e.g., Barontini's signed clock-field construction, or a modular-flow time) extends smoothly through them is open. **The Born rule and the experiencing observer**: ETRG-0, like every Everett-adjacent relational construction, describes correlations, not the selection of outcomes. **Deriving A4**: the equilibrium-lapse postulate should ultimately follow from A5's modular structure (Bisognano–Wichmann already hints at it, since modular flow *is* boost flow at a horizon); closing A4 into A5 would reduce the axiom count by one and is the most tractable theoretical next step. Finally, the **calibration constant σ** relating entropy flow to seconds is fixed empirically per system; a first-principles σ = σ(ħ, k_B, T) would make A2 parameter-free.

## 8. Relation to prior art

ETRG-0 is deliberately a stitching of load-bearing results, most of them established: DeWitt (1967) for the constraint; Page–Wootters (1983) and Rovelli–Smerlak thermal time for relational/thermal clocks; Tolman–Ehrenfest (1930) for the temperature–lapse lock; Bisognano–Wichmann (1976) and Unruh (1976) for modular flow = boost = temperature; Bekenstein (1973), Hawking (1975), Bombelli et al. (1986), Srednicki (1993) for entropy-as-area; Jacobson (1995, 2015), Ryu–Takayanagi (2006), Van Raamsdonk (2010), Maldacena–Susskind (2013), Faulkner et al. (2014) for entanglement ⇒ geometry; Verlinde (2011, 2016) for entropic force, retained here only in its fine-grained form; Erker et al. (2017) for clock thermodynamics; Colella–Overhauser–Werner (1975), qBounce, and GW170817 (Abbott et al. 2017) as the experimental gates; Eisler–Peschel (2017) and the Slepian commuting-operator structure for the lattice modular Hamiltonian used in Demo 3; Steinhauer (2016, 2019) for the analogue-horizon platform of P2; and Barontini (2026, arXiv:2509.07745) for the experimental entropic-time construction that motivated the whole assembly, with the Wheeler–DeWitt framing per Henneaux's 2024–25 Collège de France course. What is new here is not any single joint but the explicit closed loop, the γ = 1 repair of the clock-rate sector by the entanglement sector, the internal-lapse formulation Ñ[ψ] = |dS/dt|⁻¹ with its stasis-singularity phenomenology, and the P2 seam experiment tying the two entropies together at one horizon.

---

*Companion code: `etrg_demos.py` (numpy/scipy/matplotlib; runs in ~1 minute). Figures: `fig1_entropic_time.png`, `fig2_clockrate_gravity.png`, `fig3_first_law.png`. Version 0 means version 0: rename, fork, and break it.*
