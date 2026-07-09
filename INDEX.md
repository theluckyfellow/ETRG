# ETRG Repository Index — Reading Order

*A program for unifying general relativity and quantum mechanics through entropy, constructed and adversarially reviewed by four AI models over six rounds (July 2026). Start at the top; depth increases downward.*

## Start here

1. **ETRG-1_thesis.md** — the thesis in four clauses, referee-hardened (v0.2). Five minutes.
2. **ETRG-2.md** — the unified framework: layer map with status flags, the hard kernel, the research agenda, kill criteria. The main deliverable.
3. **ETRG-0_referee_packet.md** — the original adversarial review packet (v0.2): S/E/P/Q claims, kill criteria, steelmanned objections. Self-contained.

## The four technical notes (the program's results)

4. **ETRG-0_lock_note.md** — the factor of two: the entropic input is the trace-free sector; light reads it directly; the two-face lock with deviation scale. (v0.2, adjudication appendix.)
5. **ETRG-0_Q10_note.md** — partition selection at horizons: dynamical consistency + Takesaki forces one modular generator; lattice-verified dephasing lemma. (v0.2.)
6. **ETRG-0_unimodular_clock_note.md** — Q1/constraint algebra in layers; the four-volume clock the trace sector makes available. (v0.2.)
7. **ETRG-0_label_freeness_note.md** — why the entropic time label cannot deform the dynamics; the modular-normalization rule; toy-verified. (v0.2.)

## The bold round (full-unification attempts, blind protocol)

8. **ETRG-1_bold_fable.md** · **ETRG-1_bold_deepseek.md** · **ETRG-1_bold_kimi.md** — three independent attempts; convergence on ~5/8 postulates.
9. **ETRG-1_bold_referee.md** — GLM's cross-review: convergence table, six attacks, the Λ/factorization adjudication, the ETRG-2 grafting instructions.

## Panel verdicts

10. **ETRG-1_closing_fable.md** · **ETRG-0_closing_statement_glm.md** · **ETRG-1_closing_kimi.md** · **ETRG-1_closing_deepseek.md** — four independent closing statements; convergent verdict: research program with a falsifiability agenda; recruit a human physicist.

## Code and numerics (all runnable; results committed)

- **files/etrg_demos.py** — Demos 1–3: entropic time, clock-rate gravity, first law + boost structure (round 0).
- **lock_check.py** — 17/17 symbolic verification of the lock note's weak-field algebra.
- **q10_lattice_check.py** — the dephasing lemma: modular coarse-graining preserves the first law (0.99992), site basis breaks it (4.216).
- **coherent_thermal_check.py** + **q3_coherent_thermal_results.txt** — coherent vs incoherent excitations; the leg dichotomy; quantum relative entropy via the modular matrix.
- **label_freeness_toy.py** + **r4_toy_results.txt** — state-channel vs label-channel feedback; the leak made visible and step-independent.
- **toy_einstein.py** + **toy_einstein_results.txt** — the computable universe's centerpiece: MI-geometry curving in response to entanglement debt.

## Raw adversarial records (provenance)

- **DeepSeekFirstPass / GLMFirstPass / KimiFirstPass** + **FIRSTPASS_convergence.md** — round 0.
- **ETRG-0_lock_attacks.md**, **ETRG-0_q10_attacks.md**, **ETRG-0_deviation_scale.md**, **ETRG-0_dlock_derivation_deepseek.md**, **ETRG-0_r4_referee_glm.md**, **ETRG-0_unimod_attacks_deepseek.md**, **ETRG-0_unimod_referee_glm.md** — rounds 1–4, as received.
- **files/ETRG-0.md** — the original axiomatization (A1–A7) that started it all.
- **1h9j-df4k.pdf** — Barontini, "Testing the problem of time with cold atoms" (the motivating experiment).

*Git history preserves the full round-by-round evolution, including every retraction.*
