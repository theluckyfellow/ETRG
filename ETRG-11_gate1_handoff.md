# ETRG-11: The Gate-1 Hand-off — Two Theorems the Program Needs, Stated for a Specialist

*August 2026, Kimi-K3. Gate 1 (ETRG-8) is where the program lives or dies, and it needs an algebraic-QFT specialist. This document is the hand-off: the two problems stated precisely, the technology they should be built on, the lattice evidence that motivates them, and what each outcome would mean. Written to be readable in fifteen minutes by someone who owns the Tomita–Takesaki machinery.*

---

## Problem 1a — The Type III restatement of the selection theorem

**The claim to prove or break.** The program's Q10 selection theorem (ETRG-0_Q10_note.md) and its factorization-selection principle (ETRG-3, the "toehold") are proven on lattice regularizations: at a causal horizon, every operationally consistent coarse-graining inherits one modular generator, and the physical tensor factorization is selected by locality of that generator in the state's own correlation geometry. Real wedge/diamond algebras are Type III₁: no density matrices, no entropies, no modular kernels as used on the lattice. **Task: restate (and prove or refute) the selection theorem in Tomita–Takesaki language.**

**Two things the specialist will hit in the first five minutes (referee F3 — the program's answers, stated up front):**

1. *"Modular-flow uniqueness is Connes' theorem."* True: in a Type III₁ factor all faithful normal states have cocycle-equivalent modular flows, so "one modular generator" risks being trivially true. **The beyond-Connes content the lattice theorem asserts is not flow-uniqueness but selection of the coarse-graining itself**: the claim is that dynamical consistency (books that do not drift under their own evolution) picks a *specific conditional expectation* onto the observer's subalgebra — the one whose existence Takesaki's theorem ties to modular invariance — and that this selected expectation is *local* in the state's correlation geometry. The lattice evidence (below) is evidence for the locality structure of the selected conditional expectation, not for the existence of a canonical flow, which Connes gives for free.
2. *"There is no tensor factorization in Type III."* True — and choosing the surrogate is the program's job, hereby assigned: **the crossed-product Type II factorization** (Witten 2021, arXiv:2112.12828; Chandrasekaran–Longo–Penington–Witten 2022, arXiv:2206.10780) is the program's chosen surrogate, with the split inclusion as fallback. The selection theorem to prove is then: *among crossed-product factorizations, the locality of the modular generator in the state's correlation geometry selects the horizon/diamond one.* Note for the specialist, because it is the cheapest hook in this document: **CLPW's de Sitter construction requires adjoining an observer's clock to make the algebra Type II — the technology already has a clock-first structure at its center, which is precisely the program's cosmological layer.**

**The lattice evidence it must reproduce.** The dephasing lemma (modular coarse-graining preserves the first law to 0.99992 where the site basis fails at 4.216 — `q10_lattice_check.py`); the drift discriminator (the modular generator's commutator with the physical Hamiltonian separates geometric from scrambled regions, separation growing with L — `drift_check.py`); the factorization extremum (the physical factorization is a cusp-shaped local extremum of a locality functional, surviving 1% quasi-local rotations — `near_local_rival_check.py`).

**Outcomes.** Proof → Gate 1a passes; the program's core is continuum-valid. Refutation (a consistent counterexample) → the kill criterion fires; that is a legitimate and valuable outcome.

## Problem 1b — Off-equilibrium integrability of the entanglement-equilibrium conditions

**The claim to prove or break.** The entanglement-first-law route to the trace-free Einstein equations is an equilibrium import (Jacobson; FGHMV; Alonso-Serrano & Liška). **The task, with the formalism named (referee F5):** prove or refute *second-order integrability/consistency of the entanglement-equilibrium conditions* in the non-conformal case — NOT the Dirac/ADM constraint algebra, which is a different object none of the cited works compute. Be warned fairly: the FHHPRV second-order machinery is CFT-specific, and **the non-conformal case does not exist in the literature** — this is a build, not a lookup. The named obstruction is the diamond measure in non-conformal spacetimes (ETRG-2, Layer G).

**The evidence it must respect.** The lock's deviation scale δ_lock = S(ρ‖ρ_vac)/S_BH ≤ 2GΔE/(c⁴R) (derived in-repo, `audit_equations.py`); the FHHPRV bilinear covariant correction (imported).

**Outcomes.** Integrability → the program has field equations of its own (Gate 1 complete in the weak sense). A proof that integrability fails → the program ends here, honestly.

## §Remainders — the Gate-2 items punted here (referee F7: now explicitly owned)

Two Gate-2 remainders were punted to "Gate 1b" by ETRG-9/ETRG-10 but are NOT part of Problem 1b above. They are owned here, assigned to the program itself (not the specialist):
1. **The state-dependent calibration σ(ħ, k_B, state)** — the off-equilibrium extension of ETRG-9's equilibrium scale.
2. **The clock-coupling convolution for δ(z)** — ETRG-10 branch (b)'s missing input (the off-equilibrium lapse applied to cosmic clock rates).

Neither blocks Gate 1; both block Gate 2's completion. They are listed in ETRG-8's scoreboard as Gate-2 remainders, not Gate-1 tasks.

## The hand-off package

- `ETRG-7_state_of_the_program.md` — the consolidated report (start here).
- `ETRG-0_referee_packet.md` — the claims with their attack history.
- `ETRG-3_modular_locality_note.md` — the selection principle with its full amendment record.
- The runnable suite (`INDEX.md` §Code) — every toy result cited above, bit-identical reproducible.

*Contact: the repository owner, via the GitHub repository (theluckyfellow/ETRG — issues open). The lattice does not care who proves the continuum; it will be waiting with its numbers.*
