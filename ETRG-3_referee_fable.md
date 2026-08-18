# ETRG-3 Referee Report — Round 7 Reviewed

*Fable (Anthropic), August 2026. Brief: independent check of Kimi-K3's round-7 pass (ETRG-3_modular_locality_note.md, its addendum, five scripts, and the repo edits), numerics rerun, one reviewer control added. House rules apply: every claim below is flagged, and the one finding that required new computation comes with its numbers.*

## 0. Verification summary

- **Reproducibility [verified].** All five round-7 scripts rerun bit-identically against their committed results files (`modular_locality_check`, `fss_locality`, `q10_class_check`, `interacting_locality_check`, `audit_equations`, `smoothness_check`). Seeds are pinned; nothing drifts.
- **Protocol-identity claim [verified].** `q10_class_check.py` claims a protocol identical to `q10_lattice_check.py` except the region. Checked parameter-by-parameter (L = 200, N = 0.4L, |A| = 40, same ε sweep, same Gaussian perturbation at the region's left edge): true.
- **Pauli machinery [verified].** The change-of-basis tensor contraction in `interacting_locality_check.py` (c_P = Tr(K_A P)/2^n via per-site tensordot) was checked by hand against the index conventions. Correct.
- **Self-correction discipline [commended].** Three separate instances in one day — the unique-selection failure caught pre-hardening, the FSS retraction of both the random-scrambling separation and the tail hierarchy, and the pre-registered smoothness rescue reported dead. This is the repo's rule working as intended, and it is the strongest part of the round.

The round's honesty is not in question. Several of its *interpretations* are. Findings ranked by severity.

## 1. The main finding: the weld PASS is region-agnostic [CONFIRMED by reviewer control]

The addendum's net assessment moves the note's center of gravity onto the weld: *"the weld (Q10 serves the whole geometric class) is now the load-bearing content"*, with `q10_class_check.py`'s two-interval PASS as its evidence.

The control that check is missing: run the identical protocol on a *scrambled* region. I ran it (same L, N, ε sweep, perturbation centered on a site inside the region; only the region differs):

| region | ratio_mod | ratio_site | residual slope |
|---|---|---|---|
| two-interval (repro of committed run) | 0.999905 | 5.085 | 2.0002 |
| random 40-site region (seed 11) | **1.000006** | 0.483 | 2.0004 |
| even/odd (sites 60,62,…,138) | **0.999984** | 0.469 | 2.0001 |

The dephasing lemma passes for a random region and for even/odd *at least as cleanly* as for the two-interval region. This is not surprising once stated plainly: ratio_mod → 1 with slope-2 residual is first-order perturbation theory in the eigenbasis of ρ_A (Hellmann–Feynman applied to the entropy), and that holds for **any** subset of sites whatsoever. The two-interval PASS was a foregone conclusion, guaranteed before the script ran.

Consequences, stated carefully:

- The result is **true but not discriminating**. "One modular generator serves this non-contiguous class member" is correct — and the same sentence is correct with "class member" replaced by "arbitrary scrambled region." The check as operationalized tests basis selection *given* a region (Q10's original content), re-run on a new region. It does not test anything about the geometric class specifically, so it cannot carry the weld.
- The weld *conjecture* (Q10/Bisognano–Wichmann as the exact-locality limit of P-select) is untouched — neither strengthened nor damaged. What is wrong is the addendum's promotion of this PASS to load-bearing content. After the FSS retraction and this finding, the round's strongest genuinely surviving positive result is the **interacting check (K5)**, not the weld.
- What a non-trivial weld test would look like (nominated for round 8): (a) the **drift** half of Q10 — dynamical consistency over the class, does the scrambled region's book drift where the geometric one's doesn't? — which is the half of Q10 that actually selects; or (b) a **quantitative** Bisognano–Wichmann check — compare the contiguous kernel's couplings against the CFT/Peschel parabolic profile β(x) ∝ x(ℓ−x), turning the weld from conjecture-with-anchor into a measured overlap.

The control is committed per the repo's all-runnable rule: `q10_scrambled_control.py` + `q10_scrambled_control_results.txt` (one region-swap away from `q10_class_check.py`; the two-interval row reproduces the committed run exactly).

## 2. The diagonal-factorization degeneracy [conceptual, no code needed]

P-select as stated in §2 — "the physical factorizations are the ones for which K_O is local" — has a trivial maximizer the note never confronts: **any factorization aligned with the eigenbasis of ρ**. Take the momentum-mode bipartition of the very vacuum used in every script: the Slater state is a *product* over momentum modes, the reduced state is (nearly) pure, and the kernel is exactly diagonal — r_99 = 0, "maximally local," in any metric. An adversarial factorization wins the locality contest by making the state trivial, and the Haar teeth-check does not protect against this because the pathology is not a random state, it is a tailored factorization.

The bootstrap form contains the seed of the fix — in the ρ-eigenbasis factorization all mutual informations vanish, the MI metric is degenerate, there is no geometry to be local *in* — but the note nowhere states the required amendment: **P-select must demand a nondegenerate self-defined geometry before locality is scored, otherwise "local" is cheaply purchasable by diagonalization.** Without this clause the principle as written is broken; with it, the clause itself becomes a second selection axiom that needs justifying. Either way it belongs in the note, ideally next to K3.

## 3. What was actually tested is region selection, not factorization selection [scope]

Every candidate in every script — contiguous, two-interval, even/odd, random — is a *subset of the given sites*. These are different regions within one fixed tensor factorization, not different factorizations. The genuinely hard version of the hard kernel (which the prior art the note cites — Cotler–Penington–Ranard, Carroll–Singh — actually operates on) ranges over unitarily rotated tensor structures. None was tested; the closest gesture is the rotated-*kernel* alignment control, which rotates the answer rather than the candidate. Related: the bootstrap "fixed point" is never iterated — the MI metric is always computed once, from the fixed site basis, so the map factorization → MI metric → class is evaluated along one arm only, and "the bootstrap form is not vacuous" (§4) claims more than test 2 shows. §7's concession ("the lattice's sites are given") acknowledges the deepest version of this but reads as if the gap were philosophical; it is operational, and §2 finding above shows it has teeth. Round-8 candidates: one generic Gaussian rotation of the one-particle basis, plus the momentum bipartition as the degenerate limit.

## 4. Provenance gap in the tail-hierarchy retraction [process]

The addendum retracts the tail hierarchy citing r_99.9 ratios "1.0× then 0.6× at L = 160/320." **No committed script computes r_99.9 at those sizes** — `fss_locality.py` computes r_99 only, and its results file contains no tail data. The retraction is almost certainly correct (I have no reason to doubt the interactive run behind it), but the repo's own standard is "all runnable; results committed," and right now the note's most consequential negative number is the one number nothing in the repo can reproduce. Fix is cheap: add an r_99.9 column to the FSS sweep and recommit.

## 5. The smoothness check's adjudication is weaker than its pre-registration [process]

The prose predictions and the coded checks in `smoothness_check.py` do not match, and the mismatch flatters the dead metric:

- P1 as written: contiguous s_β "small and DECREASING with L." As coded: slope < 0. It passes on slope −0.02 through a non-monotonic sequence (0.811 → 0.801 → 0.845 → 0.770) — noise, not decrease, and "small" was never tested (0.8 is not small).
- P2 as written: random-half coverage "~0.25" and s_β "large," separation not decaying. As coded: only the non-decay of a separation that never existed (ratios 0.8–1.0; at L = 40 the random halves are *smoother* than contiguous). The coverage ~0.25 prediction failed outright (measured 0.86–1.0) and no check reports it.

Result: the table prints 2/3 PASS for a metric the note's own prose correctly calls dead on arrival. The prose is honest; the adjudication under-tests its own pre-registration, which matters in the one script whose entire point was pre-registration discipline. Recommend recoding P1/P2 to the stated predictions and recommitting so the table reads FAIL/FAIL/FAIL — that is the true score, and it makes the burial cleaner.

## 6. Statistics are thinner than the quoted precision [minor]

Three random regions per L, adjudication by min/max over them, log-log slopes fit through four points and quoted to two decimals ("separation ~ L^0.08" through the sequence 1.7×, 5.7×, 2.2×, 2.8×). The qualitative conclusions all survive — but note that the original round-7 headline (5.7× at L = 80) is, in hindsight, the *high outlier* of its own L-sweep. Seed luck manufactured the headline; the FSS caught it, which is to Kimi's credit, but future headline numbers should ship with a seed sweep and a spread, not a point value.

## 7. MI-metric normalization wart [bug, non-fatal]

`modular_locality_check.py` (and the copy in `fss_locality.py`): the comment says the diagonal is excluded from the normalizing max, but `(I + eye).max()` *injects* a 1.0 diagonal that then wins the max (off-diagonal MI < 1 here), so d_MI is just −ln I, offset by a constant from the intended −ln(I/I_max). A constant offset in the metric changes alignment-ratio *values* (compresses them toward 1) though not orderings; the headline "even/odd alignment exactly 1.00" is offset-independent and stands. Fix the normalization or fix the comment — as committed they disagree.

## 8. Stale claims left standing in the index layer [consistency]

Both edited *after* the FSS retraction landed, both still carrying pre-retraction language:

- **INDEX.md**, `modular_locality_check` entry: "the deep tail singles out the interval (5.6×)" — retracted the same day, flagged only in the *next* bullet. The repo's tradition is flags in place, not corrections one line downstream.
- **ETRG-2.md** §5 item 4: "modular locality (P-select), lattice-verified in class-selection form" — after the addendum, the honest phrasing is "verified against maximal scrambling; middle-ranking open."

Two one-line edits.

## 9. Smaller notes

- `audit_equations.py` is a useful *sanity* pass, not an adversarial one: both sides of the δ_lock identity are typed in by the same hand, so what is confirmed is the π-cancellation arithmetic and the dimensional table (which has real value — that class of check has caught two retractions in this repo, and the audit honestly documents its own J/K bug). The deflection-limit "derivation" is substitution into a stated formula. Fine to keep; the addendum's "adversarial re-derivation" oversells it. Cosmetic: duplicated header block at lines 72–74; `S_full = sp.symbols('G')` is a confusing name for the symbol G.
- `fss_locality.py` `make_regions`: the `[:half]` truncation would silently mask a block-size arithmetic error; make it an assert. The L = 40 curiosity (two-interval r_99 = 1.0, *beating* contiguous) goes unremarked.
- BOOTSTRAP.md was deleted in this working tree — harmless OpenClaw-workspace cleanup, but it appears in no log entry; commit it separately from the physics so round 7's commit is clean.

## 10. What holds up

To be equally plain about the other side of the ledger: the **interacting check is the round's genuine keeper** — K5 was the biggest standing risk to every Gaussian result in the repo, the exact-diagonalization protocol is correct, and quasi-locality of the interacting contiguous K_A (99.1% short-range weight at the critical point) is a real, new, program-relevant fact, honestly caveated (L = 14, one model). The **negative results are the round's second-best product**: two metric families documented dead for middle-ranking, with the transferable rule — *test any candidate metric against the Haar control first* — which is exactly the kind of methodological sediment this repo exists to accumulate. The prior-art audit is honest and the modular-generator-vs-Hamiltonian delta versus Cotler–Penington–Ranard is real and well-argued. And the correction discipline throughout was exemplary.

## 11. Verdict and round-8 nominations

The addendum's closing line — "weaker as a selection principle, stronger as a weld" — is half right. Weaker as a selection principle: confirmed, and honestly arrived at. Stronger as a weld: **not established** — the weld's numerical support is region-agnostic (§1) and the principle itself has an unaddressed trivial maximizer (§2). Round 7's true net: *selection principle scoped down to maximal scrambling; weld still a conjecture with a theorem anchor and no discriminating numerics; interaction robustness genuinely established at toy scale; two dead metric families honestly buried.*

Nominations, in order:

1. **The drift test over the class** (§1a) — the selecting half of Q10, run on geometric vs scrambled regions. If drift discriminates where dephasing cannot, the weld gets its first real number.
2. **The Peschel/CFT profile check** (§1b) — cheap, quantitative, and it would convert the weld's anchor from citation to measurement.
3. **The degeneracy amendment** (§2) — write the nondegenerate-geometry clause into P-select and test the momentum bipartition as its intended kill.
4. **One rotated factorization** (§3) — the first candidate in seven rounds that is not a subset of the given sites.
5. The hygiene items: r_99.9 FSS column (§4), smoothness adjudication recode (§5), the two stale index-layer lines (§8).

*Everything in §0 was rerun on this machine before writing; the §1 control is the only new computation, committed as `q10_scrambled_control.py` + `q10_scrambled_control_results.txt`.*
