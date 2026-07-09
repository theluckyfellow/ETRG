<div class="titlepage">

# Experimental Protocol: P1 and P2 with Numbers

**Two near-term tests of the entropic program, specified against published apparatus parameters**

*July 2026 · The ETRG Program · prepared for review*

<p class="prov">Provenance disclosure: this document was constructed by four AI models
(Claude Fable 5 — synthesis and implementation; DeepSeek-V4-Pro — derivations; GLM-5.2 —
refereeing; Kimi-K2.7 — numerics) in an adversarial-review protocol, with a human
originator (B. Kloosterman) supplying the thesis and direction. Every claim's attack
history, including retractions by all four models, is preserved in the accompanying
repository. Numerical results are reproducible from committed scripts. Treat accordingly.</p>

</div>

## ETRG Experimental Protocol: P1 and P2 with Numbers

*The two near-term experiments, specified against published apparatus parameters. July 2026. Prepared by Claude (Fable 5) from Barontini, Phys. Rev. Research 8, L022047 (2026) and the Technion analogue-horizon literature (Steinhauer, Nat. Phys. 12, 959 (2016); de Nova, Golubkov, Kolobov & Steinhauer, Nature 569, 688 (2019)). All precision targets are order-of-magnitude estimates from quoted uncertainties, flagged as such; nothing here has been vetted by an experimentalist, and that vetting is the point of circulating it.*

## P1 — Stasis phenomenology and the internal lapse (Birmingham apparatus, as built)

**What already exists.** The published experiment: a ²⁴,⁰⁰⁰-atom ⁸⁷Rb condensate in a conservative dipole trap (2π×(25, 70, 70) Hz), partitioned by an 8 μm optical barrier into bright/dark sectors, imaged every 2 ms over 120 ms; entropic time τ computed from the coarse-grained bright-sector entropy with ~5% relative 1σ per point; a barrier sweep V = 0 → 1 (barrier scale H^max/k_B ≈ 255 nK) under which total accumulated τ falls from ≈250 kσ to ≈40 kσ with the V ≃ 1 case evolving toward "heat death." The qualitative content of P1's barrier sweep is therefore *already in Fig. 2 of the published Letter*. What follows sharpens it into three quantitative tests.

**P1.a — The collapse curve.** A dense sweep (10–15 barrier values concentrated near the cyclic → heat-death transition, between the published V = 0.6 and V = 1 points) to extract the functional form τ_total(V). ETRG's reading (time = entropy exchange, no residual clock) predicts smooth collapse to a plateau set only by residual exchange, with no threshold discontinuity. **Precision estimate:** with ~5% per-point uncertainty and ~60 frames per run, a single run determines τ_total to roughly 5%/√60 ≈ 0.7% (statistical); 3–5 repetitions per barrier value suffice for a clean curve. Order of ~50 runs total — days of machine time, not months.

**P1.b — The internal-lapse reconstruction on real data.** The companion numerics (Demo 1) propagate the entropic-time Schrödinger equation using *only* internal quantities — the measured τ increments and the state-derived lapse — recovering 98.3% of total duration with errors concentrated at the 4.1% of steps flagged as stasis. The published dataset already contains everything needed to repeat this on experimental data: reconstruct the evolution from Eq. (6) of the Letter using the measured Λ(τ) pump, and compare duration recovery against the laboratory record as a function of V. **Prediction:** duration-recovery fraction degrades with the fraction of stalled-exchange steps, and reconstruction error concentrates at the measured stasis points ("wiggles" of dS·dφ sign change already noted in the Letter). A falsifying outcome: reconstruction errors distributed uniformly rather than at stasis.

**P1.c — Stasis resolution.** The 2 ms sampling gives ~5 frames across each turning point, where the entropic-time coordinate is singular. Upsampling to 1 ms in ±6 ms windows around turning points (doubling only ~20% of frames) should halve the stasis-regularization error if ETRG's coordinate-singularity reading is right — and should *not* help if the wiggles reflect physical entropy backflow instead. This distinguishes coordinate artifact from physics with a modest imaging change.

## P2 — The three-way lock (Steinhauer-class analogue horizon)

**The claim under test.** At a sonic horizon of analogue surface gravity κ, three independently measurable quantities must be set by one modular rate: (i) the Hawking phonon temperature T_H = ħκ/2πk_B, (ii) the entanglement entropy across the horizon (1D area law with log correction, coefficient fixed by the same κ), and (iii) the interior sector's entropic-time lapse (Barontini construction transplanted to the interior/exterior partition, rate anchored by the same κ). Any pairwise disagreement outside errors breaks the lock and falsifies S1.

**Leg (i) — established.** Thermal Hawking radiation and its temperature were measured from density–density correlations (Nature 569, 688 (2019)), with the measured temperature agreeing with the surface-gravity prediction at the ~10–20% level over on the order of 10⁴ experimental repetitions. This leg needs no development — only re-measurement concurrent with legs (ii) and (iii) in the same configuration.

**Leg (ii) — the hard leg.** The 2016 entanglement observation demonstrated nonseparability of Hawking pairs from the same correlation functions. Upgrading nonseparability to an *entanglement-entropy coefficient* requires reconstructing the phonon covariance matrix across the cut (density–density correlations plus phase-sector information via interference or modulation techniques) and extracting symplectic eigenvalues — the same Gaussian-state pipeline used in this program's lattice numerics, applied to measured covariances. **Precision estimate:** the target is the area-law coefficient to ±20%, which the correlation-function statistics of a ~10⁴-shot campaign should support if the phase-sector reconstruction is achievable at all; that reconstruction is the protocol's principal experimental risk, and an experimentalist's judgment on it is the single most valuable piece of feedback this document could receive.

**Leg (iii) — new but cheap.** Partition the condensate at the horizon: interior = bright, exterior = dark. From the same absorption images used for leg (i), compute the interior's coarse-grained entropy series S(t) and entropic time τ, exactly as in the Birmingham analysis (~5% per-point entropy uncertainty transfers directly). The lock prediction: dτ/dt is set by the modular rate of the horizon, i.e., by the same κ measured in leg (i). A few percent precision on the lapse rate over a ~100 ms record is realistic on Birmingham-demonstrated methods.

**The lock test.** With legs at ~10–15%, ~20%, and ~5%, a three-way consistency test at the **20% level** is achievable with existing techniques; a 10% test requires roughly a 4× larger campaign on leg (ii). Even the 20% version is, to our knowledge, the first proposed measurement tying an analogue horizon's temperature, entanglement, and an interior relational clock through one rate.

**The leg-resolved discriminator (round-3 form).** Two matched-energy injections into the inflow region: a *coherent* drive (Bragg pulse or phase imprint — spectrum-preserving) and an *incoherent* heating pulse (amplitude noise) calibrated to deposit equal energy (verified via released-energy/breathing-mode amplitude). **Prediction:** the entanglement-entropy leg is exactly blind to the coherent injection (ΔS_ent = 0 within the noise floor) and responds at linear order to the incoherent one, while the temperature/modular-energy legs respond to both. Observing the *reverse* ordering — coherent injection shifting the entropy leg while incoherent does not — falsifies the modular mechanism specifically. This discriminator is the cheapest new physics in the protocol: it reuses leg (ii)'s measurement with two extra preparation sequences.

## Honest scoping

These are analogue experiments. A confirmed lock supports the modular mechanism in a system where the microphysics is known and is evidence the *stitching* (coarse entropic time locked to fine entanglement structure through one rate) is consistent physics; it is not a test of gravity. A broken lock falsifies S1's claim that the two entropy faces are one bookkeeping — unless the failure traces to the analogue system missing the relevant sector, which is why the leg-resolved discriminator (whose prediction is mechanism-specific, not gravity-specific) matters most. A negative on P1.b/P1.c, by contrast, would strike directly at the entropic-time infrastructure on which everything else stands.
