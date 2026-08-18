# Overnight Batch — Third-Party Referee Report (Fable)

*2026-08-18. Scope: everything added between the round-7 review and 00:11 tonight — ETRG-3 rounds 8–10 (§§12–15), ETRG-4 with its Route-B batch and referee addendum, ETRG-5, ETRG-6, the ETRG-P2 protocol with §9, the prior-art audit, and ~26 scripts — authored by Kimi-K3 with two internal referee cycles by a separate Fable instance. This review is deliberately third-party: the internal cycles were adversarial and effective, so the marginal value here is (i) full reproducibility, (ii) external verification of every claim that leaves the repo (citations, published numbers), (iii) independent re-derivation of the arithmetic, and (iv) fresh eyes on what author and internal referee might share. One new computation was run; it is committed (`near_local_smalleps_control.py` + results).*

## 0. Verification summary — what was checked and passed

- **Reproducibility [verified]:** all 26 scripts rerun bit-identically against their committed results — the full round-8/9/10 suite, both internal-referee verification scripts, the Route-B instruments including the three failed wave builds, and the repaired round-7 scripts.
- **External citations [verified against arXiv]:** Giovanazzi PRL 106, 011302 (2011) is real, title verbatim ("Entanglement Entropy and Mutual Information Production Rates in Acoustic Black Holes", arXiv:1101.3272); Almeida & Rodrigues arXiv:2111.13575 is real and its content (entropic time, Kantowski–Sachs interior, singularity removal) is as the audit describes; Roy & Sarkar PRD 98, 066017 is real. The de Nova et al. Nature 569, 688 (2019) anchor and T_H = 0.351(4) nK match the published record. **No fabricated or misdescribed citation found.**
- **P2 arithmetic [verified by independent hand computation]:** κ = 288.7 s⁻¹ from T_H; κ/12 = 24.06 nats/s; the ∫s(x)dx = π²/3 flux normalization; k_BT_H/ħω_⊥ = 0.06; the 2–37 Hz band; x_min = 0.34–0.39 for both windows; f = 0.66; S_int = 21.9 k_B; the ΔS = 5.5 k_B discriminator signal (consistent via both the ΔU/T̄ route and the heat-capacity route); |α|² = 3.4 at 30 Hz; σ_D = 0.18 → 5.5σ; 29 e-folds; the P-off plateau 0.84 k_B; 0.049 nats per e-fold; and §9's discrete band sum (my mode-by-mode sum: 3.57 k_B ≈ the quoted 3.6, vs continuum 5.26 ≈ 5.3). **Every number probed checks out.** This is now a twice-independently-verified document.
- **cosmic_numbers [verified by hand]:** κ_dS = cH₀√Ω_Λ = 5.42×10⁻¹⁰ m/s²; a₀/(cH₀/2π) = 1.15; factor 4.5; S_Λ ~ 3.3×10¹²².
- **Round-7 repairs [verified in code]:** the r_99.9 FSS column exists and its retraction data reproduce; the smoothness adjudication is recoded to the prose predictions (FAIL/FAIL/FAIL); the MI normalization uses the off-diagonal max in both scripts; the degeneracy clause is implemented as specified; ETRG-2 §5 item 4 and the round-7 INDEX lines are fixed.
- **Internal referee cycles [spot-verified]:** the round-8 findings (dynamical-drift refutation, double standard, clip audit) and the Route-B findings (saturated predictor, strong-field contamination, provenance) reproduce and their repairs are in the code and notes — with the exceptions in §2 below.

The batch survives third-party review. No standing false claim was found in the notes' amended ledgers. The findings below are one substantive shape correction (with new data), one recurring process defect, and named soft spots.

## 1. The toehold's extremum is a cusp, not a smooth basin — and selection is *stronger* than the published run showed [new data, committed]

`near_local_rival_check.py` sampled ε ∈ {0.1, 0.3, 0.5} and read P2's monotonic margins as "the sanity behavior of a smooth extremum," with §14 headlining "a wide basin… strong, not knife-edge." But at ε = 0.1 the rival alignment has *already* collapsed from 7.06 to ~3.7 — everything about the functional's shape near the extremum was hiding in the unsampled interval (0, 0.1].

I ran the identical protocol at ε ∈ {0.01, 0.03} (`near_local_smalleps_control.py`, committed with results):

| ε | rival alignment (5 seeds) | mean margin vs site 7.058 |
|---|---|---|
| 0.01 | 5.38 – 5.91 | 1.50 |
| 0.03 | 4.51 – 4.85 | 2.40 |
| 0.10 | 3.58 – 4.03 | 3.31 |

Two consequences, one in each direction:

- **The selection claim strengthens.** P1 holds even at ε = 0.01: a *one-percent* quasi-local rotation already loses to the site basis by a clear margin (best rival 5.91). The extremum has no flat degenerate neighborhood; the functional discriminates rotations far smaller than the killer test probed.
- **The shape language is wrong.** The margin grows like ε^~0.34 — sublinear. A smooth functional near a smooth extremum decays quadratically; this is a **cusp** with divergent slope at the extremum. Prime suspect: the alignment score's r_99 quantile is a discrete-valued functional (it jumps between values of the finite MI-distance spectrum), so "smoothness" was never available to it. Recommended: re-score the ε-sweep with a continuous locality functional (e.g., weighted mean MI-distance) to check the cusp is the physics and not the metric's granularity, and replace "smooth extremum" / INDEX's "margin shrinks smoothly" with what the data show. The cusp is not a defect for *selection* — a steep extremum selects harder — but §14's basin picture and P2's "sanity" reading need the correction.

## 2. The index layer lags the referee cycles — four instances, and the log's "INDEX current" is false [process, recurring]

Yesterday's report flagged stale index-layer lines; they were fixed; tonight's work re-introduced the same failure mode at four spots:

1. **INDEX, `quench_drift_check` entry** still asserts the withdrawn claim verbatim: "The correct operationalization needs the region observer's evolution model — a physics question, nominated for round 8." Round-8 F1 refuted exactly this ("a manufactured mystery"), the note's postscript was rewritten with the withdrawal — and the INDEX still teaches the refuted framing one bullet above the entry that refutes it.
2. **INDEX, `drift_check` entry** quotes "slope 0.64" — the pre-F3 number. The accepted quote is "≈ 0.6, clip- and seed-limited," and the note itself now says so.
3. **INDEX, `geodesic_bending_check` entry** still headlines "the lattice Malament check exact (2.5e-19)" — Route-B F4 (accepted) demoted G3 to integrator validation and asked for the emphasis swap to the wave-level B1 and the interval-entropy result.
4. **ETRG-4 §6** still cites the wave suite as "corroborates B1/B2/B4… (null blind to scale at 0.08× cone; massive reads scale at 85×)" — those are the *contaminated-regime* numbers F2 convicted. The clean ε = 0.10 rerun (committed) gives 0.015× and 75×, and its adjudication line is Overall: FAIL (B3, KG-limited) — which §6 does not mention. The rerun was done and committed; the prose that cites it was not updated.

The pattern now has three days of data: **amendments land in the notes' amended ledgers, and the surfaces a new reader actually starts from — INDEX, the strategic documents' body text — lag behind.** The memory log's "INDEX current" claim is false as of this review. Recommended fix is procedural, not textual: make "the amendment sweep" (grep the INDEX and every §-body citation of a number that a referee cycle moved) a standing last step of every referee acceptance, the same way bars-don't-move is a standing rule.

## 3. The drift number's regulator asterisk is removable [nomination]

The clip caveat on η = ‖[K,h0]‖/(‖K‖‖h0‖) exists because K = ln[(1−C)C⁻¹] is unbounded and, at L = 320, 82% regulator-pinned (F3, verified). But the drift's leading-order content is eigen*basis* compatibility of C_A with h0 — and C is bounded in [0,1] with the same eigenvectors as K. A bounded-generator variant (η_C = ‖[C_emb, h0]‖/(‖C_emb‖‖h0‖), or any bounded function of K) tests the same compatibility with **no clip anywhere**, and the referee's dynamical m(T) is already effectively regulator-free (it lives on C matrices). Nominate the bounded variant so the weld's first number can ship without an asterisk; if the separation survives, quote that one.

## 4. P2's two most exposed numbers, named for the experimentalist [soft spots]

The protocol's flags are honest; these two deserve promotion from flag to derivation before a lab commits:

1. **Thermal seeding is plausibly O(1), not 10–15%, before dilution.** At the band center (x ≈ 1) the naive in-mode occupation at T_bg = 0.8 nK is n₀ = 1/(e^{0.44}−1) ≈ 1.8 against a spontaneous Hawking occupation of 0.58 — stimulated-dominated by ~3× if the in-modes really sit at T_bg. The 2016/2019 nonseparability results suggest the *effective* seeding is much lower (blueshift dilution of the upstream modes), and §4.6's "residual 10–15% after correction" implicitly assumes that dilution. Make the assumption explicit, and let the §6 Bogoliubov solve deliver n₀(ω) rather than the structure factor alone — leg (ii) is the protocol's most exposed budget and this is its most exposed input.
2. **The κ̂₃ no-horizon control differs by more than the horizon.** Removing the step changes the flow profile, hence interior transport and ordinary thermalization — the subtraction attributes *all* of the difference to modular flux. The N-binning and cut-scan levers partially cover this, but "control mismatch mimicking Ṡ_cg,hor" deserves its own row in the §4 systematics table with an estimated size, since K1 (the weld kill) reads directly off that subtraction.

## 5. Smaller notes

- **`de_sitter_clock_check` P1 is a corollary, not a keeper-grade computation:** "the momentum bipartition of a Slater state is exactly degenerate" is the same fact `degeneracy_check.py` already established; what §15 adds is the *dictionary* (comoving-mode observer ↔ Fourier bipartition), which is an interpretive identification, not a lattice result. The net conclusion ("if the comoving observer keeps time, it keeps it in position space") stands, but its evidential weight is the dictionary's plausibility, and the note should say so.
- **ETRG-5 §2** leans on "the parent's clock comes to a near stop at the horizon" — exterior *coordinate*-time language; no invariant clock stops there (the infalling clock crosses in finite proper time). The entropic A7-stasis reading is what carries H2, and the metric-language sentence should not be phrased as if Schwarzschild itself supplies the stop.
- **`near_local_rotation`** uses `np.linalg.eig(1j*A)` where `eigh` is the right tool for the Hermitian iA; the printed orth-error check catches any drift, so this is hygiene, not a bug.
- **J(1) = π** (peschel_profile, exploratory): consistent with the BW linear weight read at the first bond's midpoint, 2π·(1/2) — a sensible reading, and pre-registering it before promotion was the right call.
- **`referee_dynamical_drift_check`'s small-T margin (1.05×)** remains the drift story's thinnest plank, flagged by its own author; the F1 protocol at more seeds/geometries is worth a round before the dynamical claim carries more weight.

## 6. What holds up — and it is most of it

- **The two-referee-cycle structure worked.** The internal Fable's F1 (a constructive refutation that *rescued* the result it attacked), the double-standard conviction, the clip audit, the Route-B saturated-predictor catch, and the mysteries-map deflations are all correct on my checking, and every accepted finding is actually repaired in code (§0). Kimi's independent bit-identical verification of each referee claim before acceptance is exactly the right protocol, and the two convictions were absorbed without bar movement.
- **ETRG-P2 is the standout deliverable of the whole program to date.** The self-calibration architecture — Δ_weld and D free of f, g, σ, and the flow-profile κ by construction — is genuinely well-engineered; the kill tables are sharp; §9.1's "a sustained horizon predicts the *absence* of a Page knee" is the kind of anti-naive prediction that buys credibility with experimentalists. Arithmetic now twice independently verified.
- **The prior-art audit is real and survives external checking** — every located citation exists and is accurately characterized, and the two debts were discharged in the right documents with the right novelty accounting.
- **The keepers, as amended, stand:** K5 interaction robustness; the drift discriminator (with its documented caveats, §3's variant nominated); the spacing scaling law; the toehold (now cusp-shaped and *stronger* at small ε, §1); the interval-entropy cone result with the two-cones refinement; the modular-Tolman t-cancellation; the pinch toy's honest half-result.
- **ETRG-4 as the new front door is the right call** — the graph-not-route meta-claim, R1's trace-free connection, and the R2 circularities are the most intellectually serious material in the repo.

## 7. Verdict and nominations

**Verdict:** the overnight batch survives third-party review intact. Its amended ledgers contain no standing false claims; its citations and arithmetic check out externally; its two internal referee cycles caught what they should have. The residual defects are surface-layer (the §2 staleness list), one shape-of-claim correction (§1, with committed data), and named derivation debts (§§3–4).

**Nominations, in order:**
1. The **amendment sweep** as a standing referee-acceptance step (§2) — this is now the program's most persistent defect class, three days running.
2. The **continuous-functional ε-sweep** (§1) — settle whether the cusp is physics or quantile granularity; either answer sharpens the toehold.
3. The **bounded-generator drift variant** (§3) — remove the weld number's regulator asterisk.
4. The **seeding derivation and control-mismatch row for P2** (§4) — before any lab contact, since leg (ii)/(iii) budgets hang on them.
5. §5's wording fixes (de Sitter dictionary status, ETRG-5 coordinate-language, INDEX phrasing).

*Everything in §0 was rerun or re-derived on this machine before writing. The only new computation is the §1 control, committed as `near_local_smalleps_control.py` + `near_local_smalleps_results.txt`.*
