# ETRG Repository Index — Reading Order

*A program for unifying general relativity and quantum mechanics through entropy, constructed and adversarially reviewed by four AI models over six rounds (July 2026), with a seventh round by a fifth model (August 2026). Start at the top; depth increases downward.*

## Start here

1. **ETRG-7_state_of_the_program.md** — the consolidated report: the hypothesis, what's supported, what's toy-measured, the experiment, the open problems, the kill criteria, and the ask. Twenty minutes; the document to hand a physicist first.
2. **ETRG-4_unification_graph.md** — the map of the whole terrain: time, entropy, causality, gravity as four vertices; the six edges with their binding theorems; the three four-way meeting points; the six routes (and which are genuinely different); the originator's intuition developed as Route B — with Fable's referee addendum correcting Route B's kinematics (the originator's sentence is dynamical: entropy sources cone focusing; the lock note is that sentence in trace-free dress).
3. **ETRG-1_thesis.md** — the thesis in four clauses, referee-hardened (v0.2). Five minutes.
4. **ETRG-2.md** — the unified framework: layer map with status flags, the hard kernel, the research agenda, kill criteria. The main deliverable.
5. **ETRG-0_referee_packet.md** — the original adversarial review packet (v0.2): S/E/P/Q claims, kill criteria, steelmanned objections. Self-contained.

## The four technical notes (the program's results)

5. **ETRG-0_lock_note.md** — the factor of two: the entropic input is the trace-free sector; light reads it directly; the two-face lock with deviation scale. (v0.2, adjudication appendix.)
6. **ETRG-0_Q10_note.md** — partition selection at horizons: dynamical consistency + Takesaki forces one modular generator; lattice-verified dephasing lemma. (v0.2.)
7. **ETRG-0_unimodular_clock_note.md** — Q1/constraint algebra in layers; the four-volume clock the trace sector makes available. (v0.2.)
8. **ETRG-0_label_freeness_note.md** — why the entropic time label cannot deform the dynamics; the modular-normalization rule; toy-verified. (v0.2.)

## Round 7 (the hard kernel attacked)

9. **ETRG-3_modular_locality_note.md** — a candidate selection principle for the preferred factorization: the physical partitions make the state's modular generator local in the geometry the state itself defines. Class selection + tail hierarchy, lattice-verified; welds Q10 to Bisognano–Wichmann as the exact-locality limit. (Kimi-K3, August 2026.)
10. **ETRG-3_referee_fable.md** — Fable's review of round 7: the weld's numerics shown region-agnostic, the trivial-maximizer degeneracy found, the region-vs-factorization scope limit named. The note's §11 accepts the report after independent verification; verdicts amended in place.
11. **ETRG-3_round8_referee_fable.md** — Fable's review of the round-8 batch: the quench postscript's escape clause refuted by a working dynamical drift protocol (committed); a double standard in §13's adjudication convicted; clip-regulator dependence found in the drift numbers. Accepted after bit-identical verification; note amended.
12. **ETRG-P2_protocol_fable.md** — the flagship experiment with numbers: the three-way lock as a κ-free, σ-free residual; per-leg precision budgets; the leg-ordering discriminator at 5.5σ; eight kill rows; ~2.7×10⁴ runs, one to two months wall-clock. Arithmetic independently verified (Kimi-K3). **§9 adds the fourth leg (Fable): the Page series — growth, engineered knees, the trajectory weld Δ_weld(t) = 0, kill rows K9–K12; and the correction that a sustained horizon predicts the ABSENCE of a Page knee.**
13. **ETRG-5_stasis_cosmology.md** — the originator's black-hole hypothesis developed: the universe as a black-hole interior (Kantowski–Sachs role exchange), the horizon as A7 stasis, a new causality as a repartitioning event; the de Sitter far-future reading. Exploration, no theorems; pinch toy committed.
14. **ETRG-6_mysteries_map.md** — what the hypothesis explains if true: nine mysteries, each with its evidence angle; the three buildable ones; the MOND caution. With `cosmic_numbers_check.py` and Fable's referee addendum (§§1,7,9 relabeled reinterpretations; R1/R2 honesty fixes, applied).
15. **ETRG_prior_art_audit.md** — the first systematic prior-art pass (a standing kill criterion, never before run): the assembled program survives; two citation debts found and discharged (Giovanazzi 2011 — the acoustic κ/12 proposal; Almeida & Rodrigues 2021 — interior entropic time).
16. **ETRG_overnight_referee_fable.md** — Fable's third-party review of the whole August batch: all 26 scripts bit-identical, citations and P2 arithmetic externally verified, verdict "survives intact." One new committed computation (the small-ε toehold control — the extremum is a cusp, selection stronger than shown); the amendment-sweep process rule nominated and applied.
17. **ETRG-8_path_to_theory.md** — the gap analysis: what separates the program from a physical theory. Three gates — structural closure (the Type III restatement on crossed-product technology; constraint-algebra closure off-equilibrium), a number of its own (no-Page-knee is nearest; the cosmological second observable; the σ calibration), and experimental contact (P2's own rows at risk). With the calibration that GR needs no matter spectrum either, and the sequencing: one algebraic-QFT specialist is the highest-leverage act available.

## The bold round (full-unification attempts, blind protocol)

18. **ETRG-1_bold_fable.md** · **ETRG-1_bold_deepseek.md** · **ETRG-1_bold_kimi.md** — three independent attempts; convergence on ~5/8 postulates.
19. **ETRG-1_bold_referee.md** — GLM's cross-review: convergence table, six attacks, the Λ/factorization adjudication, the ETRG-2 grafting instructions.

## Panel verdicts

20. **ETRG-1_closing_fable.md** · **ETRG-0_closing_statement_glm.md** · **ETRG-1_closing_kimi.md** · **ETRG-1_closing_deepseek.md** — four independent closing statements; convergent verdict: research program with a falsifiability agenda; recruit a human physicist.

## Code and numerics (all runnable; results committed)

- **files/etrg_demos.py** — Demos 1–3: entropic time, clock-rate gravity, first law + boost structure (round 0).
- **lock_check.py** — 17/17 symbolic verification of the lock note's weak-field algebra.
- **q10_lattice_check.py** — the dephasing lemma: modular coarse-graining preserves the first law (0.99992), site basis breaks it (4.216).
- **coherent_thermal_check.py** + **q3_coherent_thermal_results.txt** — coherent vs incoherent excitations; the leg dichotomy; quantum relative entropy via the modular matrix.
- **label_freeness_toy.py** + **r4_toy_results.txt** — state-channel vs label-channel feedback; the leak made visible and step-independent.
- **toy_einstein.py** + **toy_einstein_results.txt** — the computable universe's centerpiece: MI-geometry curving in response to entanglement debt.
- **modular_locality_check.py** + **modular_locality_results.txt** — round 7: modular locality at L=80; class selection vs maximal scrambling, Haar teeth. (The deep-tail result is flagged in-script as retracted at scale.)
- **fss_locality.py** + **fss_locality_results.txt** — round-7 scaling audit: the class separation does NOT scale for random scrambling (K1 partially triggered; claim scoped down); maximal scrambling is caught with growing separation (28× at L=320); the tail hierarchy is retracted as a finite-size artifact (r_99.9 column committed; ratio inverts at L=320).
- **q10_class_check.py** + **q10_class_results.txt** — the dephasing lemma on a two-interval region (0.99991). **Region-agnostic** — see the scrambled control; does not discriminate the geometric class.
- **q10_scrambled_control.py** + **q10_scrambled_control_results.txt** — Fable's reviewer control: the lemma passes for random (1.000006) and even/odd (0.999984) regions too; the weld's numerical support is void.
- **interacting_locality_check.py** + **interacting_locality_results.txt** — K5's first verdict: XXZ exact diagonalization; the interacting modular Hamiltonian is quasi-local for contiguous regions (99.1% nn weight at Δ=1), not a Gaussian artifact. Round 7's keeper.
- **audit_equations.py** + **audit_equations_results.txt** — sanity audit of the program's named equations: δ_lock's factor of 2 = π-cancellation of boost generator vs area law; all dimensional checks pass.
- **smoothness_check.py** + **smoothness_results.txt** — the pre-registered smoothness rescue, dead on arrival (FAIL/FAIL/FAIL after referee-tightened adjudication); second dead metric family for the middle-ranking problem.
- **degeneracy_check.py** + **degeneracy_results.txt** — Fable's trivial maximizer verified (momentum bipartition: S_A ≈ 0, diagonal kernel) and the nondegenerate-geometry clause kills it (mode MI metric degenerate; site MI metric nondegenerate).
- **peschel_profile_check.py** + **peschel_profile_results.txt** — the quantitative weld check, failed as operationalized (nn-parabola r = 0.50); exploratory: staggered bulk, full-range envelope r ≈ 0.9, universal edge bond J(1) = π.
- **drift_check.py** + **drift_results.txt** — the selecting half of Q10: the commutator [K_A, h0] discriminates geometric from scrambled regions (5.4× at L=80) with separation GROWING with L (slope ≈ 0.6, clip- and seed-limited); Haar teeth 17×. The weld's first discriminating number.
- **quench_drift_check.py** + **quench_drift_results.txt** — the naive dynamical drift version, failed: entropy-based Δ measures basis misalignment; random regions drift less (drive-strength confound documented). **The escape clause it proposed ("requires the region observer's evolution model") was refuted by Fable's F1 — the working dynamical protocol is `referee_dynamical_drift_check.py`; the "region observer's clock" framing is withdrawn.**
- **xxz_drift_check.py** + **xxz_drift_results.txt** — interacting drift: FAIL as pre-registered (1.9× vs 2× bar) but the ordering is perfect (contiguous < two-interval < scrambled < Haar); plausibly a small-size effect; DMRG extension nominated.
- **spectrum_spacing_check.py** + **spectrum_spacing_results.txt** — the exact-lattice weld check: Peschel's entanglement-spectrum spacing Δξ = π²/ln ℓ confirmed (constant within 8.1% band, trending to π²; Haar non-uniform). The weld's anchor upgraded from citation to measurement. Uniformity caveat: tracks ℓ/L ratio (finite-complement).
- **rotated_factorization_check.py** + **rotated_factorization_results.txt** — the first factorization-level test: FAIL as pre-registered (P1 blunt, P3 bar miscalibrated); P2 survives — bootstrap locality ranks the site basis first (7.06 vs 3.43); the exact momentum factorization is exactly degenerate (clause kills it). Round-9 killer test nominated: near-local rivals.
- **referee_dynamical_drift_check.py** + results, **referee_drift_clip_check.py** + results — Fable's round-8 verification scripts: the working dynamical drift protocol (footprint-matched rivals, shared state; discriminates 1.05×/1.78×/6.59× at T=5/20/80) and the clip-sensitivity audit of the drift commutator.
- **near_local_rival_check.py** + **near_local_rival_results.txt** — the round-9 killer test: smooth quasi-local rotations of the site basis (the hard regime). F_site beats every rival (7.06 vs best 4.004); Haar teeth. The physical factorization is a strong CUSP-shaped extremum of the bootstrap-locality functional (overnight referee: a 1% rotation already loses — `near_local_smalleps_control.py` — but "smooth basin" was the wrong shape; continuous functional nominated) — the hard kernel's first hardened toehold.
- **toehold_robustness_check.py** + **toehold_robustness_results.txt** — toehold robustness: L-scaling PASS (wins at L=40 and 120); state-independence FAIL (gapped state: site loses by a hair) — the principle's power tracks the state's correlation range. Domain constraint discovered.
- **factorization_drift_check.py** + **factorization_drift_results.txt** — drift across factorizations: the commutator is a coarse discriminator only (vetoes gross scrambling 9.5×, flat among near-local rivals); the fine structure lives in the alignment.
- **pinch_geometry_check.py** + **pinch_geometry_results.txt** — the ETRG-5 toy: a hopping pinch (cone collapse) closes the MI-geometry throat (32× bond) and splits the chain into two fully independent causal domains (I(left:right) = 0, cleaner than a hard cut); the horizon-mode expectation fails — a static lattice shows causality stopping, not a new one starting.
- **de_sitter_clock_check.py** + **de_sitter_clock_results.txt** — the comoving-observer computation: the Fourier-mode bipartition is exactly degenerate (no entropic clock for the comoving-mode observer — GLM's verdict computed); sine-vs-parabola discrimination of the static-patch kernel inconclusive at ℓ/L = 1/2; P3 bar miscalibrated, documented.
- **geodesic_bending_check.py** + **geodesic_bending_results.txt** — the Route-B kinematic instrument, PASS 4/4 (bars corrected in-flight from the repo's A5): the A5 deflection profile (1+v²/c²) measured to 5% across v = 0.3–0.9c; G3 (conformally-flat null straightness) is integrator validation per referee F4 — the nontrivial Malament evidence is the wave-level B1 (`spacetime_malament_check.py` at ε=0.10) and `interval_entropy_cone_check.py`. Solver step-size artifact diagnosed by Euler cross-check.
- **spacetime_malament_check.py** + results, **dirac_malament_check.py** + results, **lattice_light_bending.py** + results — the three failed wave-packet builds, committed with their causes of death (measurement bias, sign bug, dispersion); the geodesic version is the reference.
- **mi_decomposition_check.py** + **mi_decomposition_results.txt** — the Route-B structure question, first attempt: D1 FAIL (predictor saturated, wrong observable — referee F1); D3 PASS (quench front tracks the bare cone at r = 0.9995).
- **interval_entropy_cone_check.py** + **interval_entropy_cone_results.txt** — the static state's cone face, done right: ΔS of defect-spanning intervals tracks (1/3)Δln d_conf at r = 0.98–0.996 with slope → 1.0 (the curved-CFT law measured); the potential deformation is distance-structured too — the lattice has two cones, and density sources the dressed one.
- **ETRG-4_routeB_referee_fable.md** + **referee_routeB_check.py** + results — Fable's Route-B review: D1's conclusion refuted by the interval-entropy operationalization (verified bit-identical); wave suite's strong-field contamination isolated; geodesic header/provenance fixed; map nits applied.
- **modular_tolman_check.py** + **modular_tolman_results.txt** — the cone × modular-flow weld: interval kernels are parabolic in slow/medium/fast cone regions (r = 0.94–0.96) with universal amplitude to 10% (the t-cancellation measured); the cone enters the modular structure through the conformal coordinate.
- **cosmic_numbers_check.py** + **cosmic_numbers_results.txt** — the consistency layer: de Sitter surface gravity vs MOND a₀ (factor 4.5; a₀ vs cH₀/2π at 1.15); S_Λ = (π/Ω_L)(t_H/t_P)² exactly; the cosmic entropic clock rate ≡ H_inf (definitional — the lock needs a second observable).

## Raw adversarial records (provenance)

- **DeepSeekFirstPass / GLMFirstPass / KimiFirstPass** + **FIRSTPASS_convergence.md** — round 0.
- **ETRG-0_lock_attacks.md**, **ETRG-0_q10_attacks.md**, **ETRG-0_deviation_scale.md**, **ETRG-0_dlock_derivation_deepseek.md**, **ETRG-0_r4_referee_glm.md**, **ETRG-0_unimod_attacks_deepseek.md**, **ETRG-0_unimod_referee_glm.md** — rounds 1–4, as received.
- **files/ETRG-0.md** — the original axiomatization (A1–A7) that started it all.
- **1h9j-df4k.pdf** — Barontini, "Testing the problem of time with cold atoms" (the motivating experiment).

*Git history preserves the full round-by-round evolution, including every retraction.*
