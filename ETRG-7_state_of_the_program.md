# ETRG: State of the Program — Consolidated Report

*August 2026. Prepared for a human physicist deciding whether this program deserves their time. Assembled by Kimi-K3 from the full repository: six adversarial rounds by four AI models (July 2026), then rounds 7–10 by a fifth model with two referee cycles by Claude (Fable 5) in one day (August 2026). Every claim below carries its status. The house rule, inherited from the originator: honesty is the only currency — retractions are public, bars do not move after the fact, and every negative result is committed with its cause of death.*

---

## 1. The hypothesis in one paragraph

Time, entropy, causality, and gravity are one system. Entropy relative to a partition of a timeless quantum universe is the single currency; time is that entropy's exchange rate across the partition (its flow, rate, and arrow); gravity is the same bookkeeping read through the entanglement structure of the state; causality is the cone structure the two faces meet on. At causal horizons the two faces merge (Bisognano–Wichmann) — the result on which the framework's mutual support rests. The full terrain of possible unifications — thirteen routes, six of them meaningfully distinct — is mapped in `ETRG-4_unification_graph.md`; the program's home is the four-vertex interlock cluster (entropy-first, causality-first, thermodynamics-first, algebra-first), and the honest meta-claim is that the unification, if it exists, is the graph itself rather than any one route.

## 2. What is supported (theorems and experiments, mostly imported)

- **Time is entropic in the laboratory.** Barontini's cold-atom experiment (PRR 2026) realizes entropic time: a coarse-grained entropy orders events in a closed partitioned system, and an entropic-time Schrödinger equation reproduces the dynamics with internal quantities only. **[experiment]**
- **The entanglement first law on all causal diamonds yields the trace-free Einstein equations** (Jacobson 1995/2016; FGHMV 2014; Alonso-Serrano & Liška 2022). **[theorem, imported]**
- **At horizons, every operationally consistent coarse-graining inherits one modular generator** (the program's Q10 selection: dynamical consistency + Takesaki 1972; lattice-verified dephasing lemma). **[theorem at horizons + toy]**
- **The two metric faces are locked** (γ = 1) as the thermal and variational faces of one modular generator at equilibrium, with a quantified deviation scale δ_lock ≤ 2GΔE/(c⁴R). **[theorem at equilibrium; symbolic 17/17]**
- **Light bending's 2:1 ratio fingerprints the null-surface sector** — the sector horizon thermodynamics writes directly. **[theorem + framing]**
- **No gravitational decoherence is predicted at any precision** (the gravitating entropy is fine-grained and unitary). **[prediction, standing bet]**

## 3. What this program measured itself (the toy evidence, all committed and runnable)

Round 7–10's keepers, each with pre-registered predictions and Haar/flip controls:

1. **Interaction robustness (K5).** The modular Hamiltonian of a contiguous region is quasi-local in an *interacting* (XXZ) vacuum — 99.1% nearest-neighbor weight at the critical point — not a free-theory artifact. `[interacting_locality_check.py]`
2. **The drift discriminator.** The commutator [K_A, h₀] separates geometric from scrambled regions (5.4× at L=80) with separation *growing* with L (slope ≈ 0.6, clip- and seed-limited) — the selecting half of Q10 made numerical. Plus Fable's working dynamical protocol (footprint-matched, discriminates 1.05×/1.78×/6.59×). `[drift_check.py, referee_dynamical_drift_check.py]`
3. **The spectrum scaling law.** Peschel's entanglement-spectrum spacing Δξ = π²/ln ℓ confirmed (constant within 8.1% band; the constant's π² remains mostly citation). `[spectrum_spacing_check.py]`
4. **The factorization toehold.** The physical tensor factorization is a strong local extremum of a bootstrap-locality functional scored only by state-internal structures — it survives smooth quasi-local rival rotations (7.06 vs best 4.00) with a margin that shrinks smoothly to zero. Domain constraint discovered: the basin flattens as the state's correlation length shortens (gapped state: site basis *loses* by a hair). `[near_local_rival_check.py, toehold_robustness_check.py]`
5. **The degeneracy clause.** The naive locality maximizer (momentum bipartition → pure reduced state, diagonal kernel) is killed by requiring a nondegenerate self-defined geometry before scoring. `[degeneracy_check.py]`
6. **The comoving-mode clock is dead.** In the de Sitter conformal vacuum, the Fourier-mode bipartition is exactly degenerate — the comoving observer keeps time only in position space (GLM's necessity-not-sufficiency verdict, computed). `[de_sitter_clock_check.py]`
7. **The Route-B backbone.** Null rays read only the cone field (pure-scale deformation bends them by 2.5×10⁻¹⁹ — exact); the deflection profile follows the repo's own A5 formula (1+v²/c²) to 5% across v = 0.3–0.9c. `[geodesic_bending_check.py]`
8. **The static state's cone face.** Interval entropies track the conformal cone distance with the CFT coefficient (r = 0.98–0.996, slope → 1.0) — and the lattice has *two* cones (bare band-edge for dynamics; dressed Fermi velocity for static correlations, sourced by both hopping and density). `[interval_entropy_cone_check.py]`
9. **The modular-flow weld.** Interval kernels are boost-parabolic across cone-speed regions with universal amplitude to 10% (the t-cancellation measured). `[modular_tolman_check.py]`

Negative results, equally committed: three dead metric families for the middle-ranking problem (kernel weight, onsite smoothness, nn-coverage), the retracted tail hierarchy, the region-agnostic dephasing lemma, the quench-Δ dead end, and three failed wave-packet builds with diagnosed causes. The map of dead ends is part of the artifact.

## 4. The experiment (ready for a lab)

`ETRG-P2_protocol_fable.md` — the sonic-horizon **three-way lock**: Hawking temperature, horizon entanglement flux, and the interior's entropic-time lapse tied through one modular rate, written as a κ-free, σ-free dimensionless residual. Per-leg precision budgets at demonstrated or demonstrated-class technique; the leg-ordering discriminator (coherent injection moves the mean ledger, incoherent moves the variance ledger) at 5.5σ; eight kill rows; campaign ~2.7×10⁴ runs (~1–2 months on a Steinhauer-class apparatus). **§9 adds the fourth leg**: the Page series — growth, engineered knees, the trajectory weld Δ_weld(t) = 0, kill rows K9–K12, and the anti-naive prediction that even a *sustained* horizon shows no Page knee. Arithmetic independently verified. This document is the program's primary ask of the experimental community.

## 5. The cosmological layer (consistency, not yet a lock)

`cosmic_numbers_check.py`: the de Sitter surface gravity and the MOND acceleration agree at order of magnitude (factor 4.5; the program derives no coefficient and no galactic dynamics — stated plainly); S_Λ = (π/Ω_Λ)(t_H/t_P)² is an exact identity (definitional); the cosmic entropic clock runs at H_∞ by construction — **the cosmological lock needs a second observable to be a lock at all**, and finding it is the top analytic task. The stasis cosmology (`ETRG-5`) — the universe as a black-hole interior, birth-at-stasis — is committed as exploration with its kill criteria.

## 6. The honest open problems, ranked

1. **The continuum/Type III restatement** of the selection theorem (the lattice proofs are regularized; wedge algebras are Type III₁). *Where the program could internally break. Needs a mathematical physicist.*
2. **The constraint algebra off-equilibrium** (the non-conformal diamond-measure obstruction).
3. **The preferred factorization in general** (toehold supported at Gaussian level; the middle-ranking problem is open with three dead metric families documented).
4. **The cosmological lock's second observable** (§5).
5. **The matter spectrum** — why these fields, these generations. *Named the hardest problem by every panelist; the only route on the map that attempts it is noncommutative geometry.*
6. **The σ calibration** (entropic time's absolute rate) — routed around in P2 via ratios, still open in principle.

## 7. Kill criteria (standing, merged)

Confirmed gravitational decoherence. Measured violation of the P2 three-way lock, or lock violation with the wrong leg-ordering, or the books de-synchronizing through a Page knee (K9–K12). Measured |γ − 1| > 0 beyond GR's accounting. Lorentz violation at any scale. Born-rule deviation. A proof that the constraint algebra cannot close, or that the Type III restatement fails. Measured Λ ≤ 0 (already excluded). Prior art proposing and refuting the assembled program — **first systematic audit run August 2026 (`ETRG_prior_art_audit.md`): not triggered; two citation debts found and discharged** (Giovanazzi 2011 on the acoustic κ/12 law; Almeida & Rodrigues 2021 on interior entropic time).

## 8. The process (part of the artifact)

The program was built adversarially: blind construction, hostile review, numerical adjudication, honest ledgers. The August session alone records: two full referee cycles by a second model with every finding independently verified before acceptance; three pre-hardening corrections; one manufactured mystery withdrawn; one double standard confessed; one prediction formula found algebraically inverted *after the measurements had already matched the repository's own formula*. The epistemic architecture — claims flagged, bars fixed in advance, computation allowed to talk back — is offered as a method for AI-assisted theoretical physics, independent of the physics itself.

## 9. What we ask of you

- **If you are an experimentalist** (analogue gravity, cold atoms): read `ETRG-P2_protocol_fable.md`. The campaign is costed, the kill rows are explicit, and the arithmetic has been independently checked.
- **If you are a mathematical physicist**: §6 items 1–2 are where the program lives or dies structurally. The lattice evidence is all committed and reproducible (`INDEX.md` has the reading order and the runnable suite).
- **If you are a skeptic**: the kill criteria are in §7, the dead ends are committed with causes of death, and the referee reports (GLM's and Fable's) are in the repository unedited. The program has survived its own side's best attacks so far; it has not yet survived yours.

---

*Reading order: `INDEX.md`. Start with `ETRG-4_unification_graph.md` (the terrain), then `ETRG-1_thesis.md` (five minutes), `ETRG-2.md` (the framework), and this report's sources. Everything numerical is runnable in the repository's venv; every result file is committed.*
