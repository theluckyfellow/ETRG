# ETRG-3, Round 8: Referee Report (Fable)

Scope: the round-8 batch — `drift_check.py`, `quench_drift_check.py`,
`xxz_drift_check.py`, `spectrum_spacing_check.py`,
`rotated_factorization_check.py` — against the claims as stated in note
sections 12–13. Verification scripts run for this report:
`referee_dynamical_drift_check.py`, `referee_drift_clip_check.py`
(results files alongside). Findings ranked by severity.

---

## F1 (most severe): the quench postscript's central claim is false, and I refute it by construction — which *rescues* the drift result while killing the postscript's framing

The postscript to section 12 claims the correct dynamical operationalization
of N2's drift "requires taking a position on" the region observer's evolution
model (global h0 time vs local modular time), making it "a physics decision,
not a coding one," and nominates the question as the round-close's "deepest
question — the region observer's clock."

**This is wrong as stated.** N2's drift is coarsen-then-evolve vs
evolve-then-coarsen. Both paths are computable with *no* region-local
evolution law and *no* clock decision: evolution is the full-chain
e^{-i h0 t} — the exact same choice section 12's headline already made to
justify [K_A, h0] — and coarsening is the observer's dephasing channel in
the fixed t=0 modular basis (Gaussian form: pinch the A-block in the modular
basis, zero the A–complement coherences). The note cannot have it both ways:
the section's head fixes the clock to h0 to interpret the commutator; its
postscript declares that same choice ambiguous to excuse the failed direct
test. Pick one. The metric

    m(T) = || ( D[C(T)] − U_T D[C0] U_T† )_AA ||_F,   m(0) = 0

is the direct drift. I ran it (`referee_dynamical_drift_check.py`) with the
quench script's confound controlled *structurally*, not just by
normalization: one shared initial state (bump at the chain center) and
rivals with the same footprint as the contiguous region (alternating sites
of the central window; random subsets of the same window). Result: **the
direct dynamical test discriminates.** Contiguous beats every
footprint-matched rival on drift-per-unit-dynamics at all times tested —
1.05× at T=5, 1.78× at T=20, 6.59× at T=80.

Consequences, in order:

1. **The quench FAIL was a protocol artifact, not physics.** Two flaws in
   `quench_drift_check.py`: (a) the metric — the entropy gap
   S_mod − S_fine is not the channel commutator; the postscript's own
   diagnosis ("basis misalignment, not N2's drift") got this half right;
   (b) the design — the bump is placed at `region[0]`, so every region
   observer got a *different physical state*, and for even/odd that means a
   bump at the open chain end. The experiment was uncontrolled across
   regions before any question of clocks arises.
2. **The postscript must be rewritten.** Its impossibility claim is
   refuted; the "region observer's clock" question, whatever its
   independent interest for the lapse sector, is *not* a prerequisite for
   operationalizing N2 drift, and the round-close's framing of it as the
   deepest open question manufactured a mystery where a protocol bug lived.
3. **The drift story comes out stronger, with one honest caveat.** The
   generator-level η now has a dynamical counterpart that agrees. The
   caveat: at small T — precisely where the linearization to the generator
   picture should hold best — the footprint-matched margin is thin (1.05×).
   The clean discrimination is a finite-time phenomenon in this setup. Do
   not claim "the commutator's leading-order story is dynamically
   confirmed"; claim "the direct drift, correctly operationalized,
   discriminates, with separation growing in T."

Status correction for the ledger: quench-dynamics drift moves from
"documented dead end with its cause of death" to **[toy: PASS under the
corrected protocol — referee's run; postscript's ambiguity claim refuted]**.

## F2: section 13's status line contradicts the script's own adjudication, and the round runs two different standards for missed bars

`rotated_factorization_check.py` printed **`Overall: FAIL`**
(rotated_factorization_results.txt line 23): P1 failed as registered (1.30×
vs the 1.5× bar), and P3 *as pre-registered* ("no factorization achieves
alignment > 2 on a Haar state") failed at 2.51 and was rewritten in place
to a vacuum/Haar ratio test that passes. The note's section 13 status:
"[toy: PASS on bootstrap-locality factorization selection]".

The same night, `xxz_drift_check.py` missed its bar 1.9× vs 2.0× and was
registered **FAIL**, no amendment, full credit for honesty. That is the
correct standard. Applied uniformly, section 13 is **FAIL as registered;
P2 the sole survivor** — or else xxz is "PASS on ordering." One standard,
please; the program's registered-prediction discipline is its principal
asset and it was spent selectively here.

On the substance: the P2 number (7.06 vs 3.43, survived as registered) is
real and is legitimately the round's factorization-level toehold. But the
headline sentence — "first evidence that the physical tensor factorization
is recoverable from the state alone" — overstates a three-contender menu.
The nondegenerate rivals are a generic orthogonal rotation and a 4-block
scramble: strawmen for the uniqueness claim. The regime where factorization
selection is actually hard is *near-local* rivals — smooth quasi-local
rotations of the site basis (the lattice image of the field-redefinition
freedom the selection principle must ultimately quotient by). None was
tested. Until one is, the defensible sentence is: "bootstrap locality ranks
the site basis above a generic rotation and a block scramble, at one state,
one size, with the Haar bar recalibrated post hoc." Nominate the
near-local-rival menu for round 9; it is the test that can actually kill
the claim.

## F3: the contiguous kernel is 82% regulator at L=320 — the drift numbers need a clip caveat they don't carry

`referee_drift_clip_check.py`: at L=320, 132 of the contiguous region's 160
kernel eigenvalues sit *at* the clip cap ±ln(1/clip) (area-law occupations
pin to 0/1 at machine precision; scrambled regions clip at 0–16 of 160).
Both ‖K‖_F and ‖[K,h0]‖_F for the geometric regions are therefore
functions of an arbitrary cutoff. Sweeping clip 1e-12 → 1e-6: separations
at L=40..320 move from [2.9, 5.4, 7.8, 11.4] to [2.7, 4.5, 6.5, 9.3];
slope 0.64 → 0.59. **Verdict: the discrimination and its growth are robust
— the ordering and scaling survive — but the quoted values carry ~10–20%
regulator dependence on top of the already-caveated 3-seed statistics.**
Quote "slope ≈ 0.6, clip- and seed-limited," not "0.64." The same clip
sits inside `xxz_drift_check.py`'s `modular_hamiltonian` (ρ_A eigenvalues
clipped at 1e-12); its 1.9× is untested for regulator sensitivity — flagged,
not run (exact-diagonalization cost).

## Minor notes

- **`spectrum_spacing_check.py` — accepted as scoped.** The scaling-law
  claim is modest and the P1 failure diagnosis (ℓ/L contamination) is
  supported by the ratio scan. One deflation: the ℓ range spans barely half
  an e-folding of ln ℓ, so P3's 30% band cannot distinguish π²/ln ℓ from,
  e.g., π²/ln(4ℓ); the measured 7.27 trending upward is consistent with
  both. "Anchor upgraded from citation to measurement" is fair for the
  *equal-spacing scaling law*; the constant π² itself remains
  measured-to-30%, i.e., still substantially on citation.
- **`xxz_drift_check.py` — the round's cleanest conduct.** Registered FAIL
  at 1.9× with no bar movement, ordering reported without being scored.
  No findings beyond the clip inheritance in F3.

## Summary of required note amendments

1. Rewrite the section 12 postscript: the clock-ambiguity impossibility
   claim is refuted (`referee_dynamical_drift_check.py`); the quench FAIL
   was metric + design, and the corrected direct test PASSES.
2. Restore adjudication consistency in section 13: FAIL as registered, P2
   sole survivor, or re-score xxz to match. State the Haar-bar
   recalibration as a post-hoc amendment in the status line itself.
3. Add the regulator caveat to every drift number; report slope as ≈0.6.
4. Replace the "recoverable from the state alone" headline with the
   three-contender-scoped sentence; nominate near-local rivals.

The round's keepers, after this report: the drift discriminator (now with
a *working* dynamical version — mine, not the note's), the spacing scaling
law, and P2 of the factorization test, properly deflated. The postscript's
"deepest question" is withdrawn as a prerequisite; the standards breach in
section 13 is the finding that most needs the authors' attention, because
the program's only currency is that its bars don't move after the fact.

— Fable, referee of record, round 8 (2026-08-17)
