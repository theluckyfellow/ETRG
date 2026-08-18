# Third-Party Audit: The Gates Session (ETRG-9/10/11, the Barontini Cross-Check, the Marginal Items)

*August 2026, Claude (Fable 5), auditing after the fact. Scope: the three commits following ETRG-8 — the Gate-2 homework with its internal referee cycle (F1–F8), the executed Barontini cross-check, and the two marginal-item scripts. Method as in the overnight audit: rerun everything, verify every external claim at the source, re-derive the arithmetic, then attack what remains. One new committed control (`cusp_smalleps_control.py`).*

---

## 0. Verification summary

- **Scripts:** `bounded_drift_check.py` and `cusp_granularity_check.py` rerun in the repo venv — both reproduce their committed results **bit-identically**.
- **External claims, all verified at the source:**
  - White et al. 2024 (DES, arXiv:2406.05050): b = 1.003 ± 0.005 (stat) — confirmed, from 1504 SNe Ia to z ≈ 1.2. *Nit: the paper also quotes ± 0.010 (sys); the notes cite the stat error only. Total ≈ ± 0.011 — changes nothing (the naive apparent-horizon exponent ≈ 1.8 is still excluded at ~70σ) but should be quoted.*
  - Cai–Kim (hep-th/0501055): Friedmann equations from the first law on the apparent horizon — exactly as described.
  - "Wang–Abdalla" (gr-qc/0511051): event-horizon thermodynamics breaks down in non-de-Sitter accelerating FRW — exactly as described. *Nit: the paper is Wang–**Gong**–Abdalla.*
  - Barontini quotes checked against the in-repo PDF: "σ the (arbitrary) entropic time unit" — verbatim; 120 ms lab duration and 250×10³ σ total — verbatim; σ = 4.8×10⁻⁷ s and T_eff ≈ 16 μK re-derived, correct.
- **Cosmology arithmetic re-derived:** H(0.6)/H₀ = 1.39, H(1)/H₀ = 1.76, T_GH = 2.2×10⁻³⁰ K, T_app = 2.7×10⁻³⁰ K, implied dilation exponent ≈ 1.8 at z ~ 1 — all correct.
- **The internal referee cycle held:** every F1–F8 repair is genuinely present in the three notes; no standing false claims found in the amended texts.
- **The ledgers are current.** INDEX and the session memory record `bounded_drift_check.py`'s B4 Haar-teeth **FAIL as registered**, with no bar movement, and the caveat travels with the "asterisk-free" headline. The amendment sweep — the process defect I flagged in two consecutive audits — held this time. Noted with approval.

## 1. The cusp's shape is logarithmic, and half the distance matrix sits on the regulator — the committed α = 0.17 is a fit artifact **[high]**

`cusp_granularity_check.py` concluded "the cusp is PHYSICS (α = 0.17)." The committed 5-point grid cannot make that call: a power law and a logarithm fit it equally well (log-log R² 0.994 vs ln-linear 0.988), and they diverge hard below ε = 10⁻³. The new control (`cusp_smalleps_control.py`, committed with results) extends the sweep to ε = 10⁻⁴ and decides it:

- **Power law rejected.** α = 0.17 predicts margin 3.56 at ε = 10⁻⁴; observed 2.27. A power law demands a constant margin *ratio* of 3^0.17 = 1.21 per ε-tripling; observed ratios are 1.56 / 1.40 / 1.27 — drifting monotonically.
- **Logarithm confirmed.** The margin *difference* per e-fold of ε is constant: 1.15 / 1.17 / 1.22. The margin is ≈ linear in ln(1/ε), extrapolating to zero near ε ≈ 1.5×10⁻⁵.
- **Mechanism identified.** d_MI = −ln(I/I_max) responds logarithmically to the O(ε²) far-pair mutual information a rotation switches on — the log lives in the metric definition, not in the extremum. And the regulator is load-bearing: **870 of 1770 site-basis pairs sit within 1.0 of the −ln(clip) = 27.6 cap.** Half the distance matrix rests on the clip floor, so the functional's depth scale — not just its exponent — is regulator-structured. (The Fiedler region selection, the other discrete pipeline step, is exonerated: the selected region is set-identical to the site basis's for every rival at ε ≤ 0.03.)

What stands: **no smooth basin, anywhere** — F_site wins across 3.7 decades of ε, and a logarithmic cusp is *steeper* than any power law. What must change: the committed verdict line "margin ~ eps^0.17 → cusp is physics" should be amended to "logarithmic cusp in the MI metric; exponents are grid artifacts" — and round-9's ε^0.34 (my own small-ε control's fit, same disease) deserves the same re-read. Required before the cusp is cited as physics: the **clip sweep** (rerun at clip = 10⁻⁸ and 10⁻¹⁶; if the margin's depth and vanishing scale track −ln(clip), the cusp's *sharpness* is the regulator's, and only the sign of the margin is physics).

## 2. ETRG-9 Addendum 2's π/2 rests on three stacked O(1)s, not one **[medium]**

The addendum derives σ_sat = (π/2)·ħ/(k_BT) from the Margolus–Levitin bound and flags "one nat = one nat of distinguishability" as the attackable step. That flag is honest but incomplete — the derivation stacks **three** unfixed O(1)s:

1. The nat-equals-distinguishability identification (flagged in-note — good).
2. **The per-nat reading of a total-orthogonalization bound.** Margolus–Levitin bounds the time to reach a *fully orthogonal* state; dividing it into "per-nat" installments assumes distinguishability accrues linearly at the bound rate, which QSL bounds do not license. The correct instrument for a *rate* statement is the differential Mandelstam–Tamm form (Bures-angle velocity ≤ ΔE/ħ), and converting angle to nats brings its own constant — generically not π/2.
3. E ~ k_BT for "the channel's energy scale" is channel-spectrum-dependent (mean energy above ground state vs ΔE differ by more than the quoted [1, π/2] spread for generic thermal channels).

The honest tag is "**mechanism identified** (QSL family), O(1) not yet derived" — not "derived at the level of the QSL mechanism," and the [1, π/2] range is not a derived range. The shared-mechanism upgrade of the A2/A3 convergence survives (both sides genuinely are QSL-rooted); the specific constant does not yet.

## 3. ETRG-10's "post-diction" oversells branch (a) **[low]**

b = 1.003 ± 0.011 is equally the prediction of *no cosmic-clock coupling at all*. In this observable, branch (a) (event-horizon clock, constant rate) is indistinguishable from the null hypothesis — so the event-horizon reading **survives** the data; it does not **score** off them. Calling it "a genuine post-diction" (the note, and the internal referee's F2 that suggested the framing) claims credit the observable cannot assign. The real content of the gate item is unchanged and is strong: the *kill* of the naive apparent-horizon clock is genuine, and the a₀-drift discriminant is the only forward-looking test on the books. Suggested edit: "post-diction" → "consistency shared with the null; the kill is the result."

## 4. Smaller items

- **DES error bar:** quote stat and sys (±0.005, ±0.010) wherever b is cited (ETRG-10 §2, §3, memory).
- **Citation name:** Wang–Gong–Abdalla, not Wang–Abdalla (ETRG-10 §2, ETRG-8_gate2_referee F6).
- **INDEX header** still reads "with a seventh round by a fifth model (August 2026)" — predates rounds 8–10 and the gates session. The one stale line left in the index layer. *(Fixed in this audit's commit.)*
- **bounded_drift B4 judgment endorsed:** shipping the asterisk-free number on B1–B2 with the teeth caveat attached is within house rules — the discrimination is within-state (rivals share the state), so the weak Haar teeth bound the metric's universality, not the separation. The caveat travels in INDEX and memory; keep it traveling into any note that cites the number.

## 5. What holds up

The internal referee cycle was sharp — F1 (the KMS stipulation) and F2 (the wrong-by-10× data precision, flipping the note's conclusion into a stronger one) are exactly the catches this process exists for, and both repairs are real. The Barontini cross-check is the best kind of negative result: the experiment's σ is a unit, so the question changed shape honestly, and the Erker-bound-saturation synthesis (conventional as a unit; physical as a bound; the program's claim = clocks saturate it) is the right resolution structure — it turned an analytic debt into a lab task. `bounded_drift_check.py` retires my overnight nomination 3 cleanly: the weld's first number now ships without the clip asterisk, at the same order (4.2× at L = 80, slope 0.55). ETRG-11 is sendable: the beyond-Connes content and the crossed-product surrogate are stated up front, which is what was missing.

## 6. Verdict and nominations

**The gates session survives audit, with one substantive correction (§1).** All scripts reproduce; all external claims check out at the source; the referee cycle's repairs are in place; the ledgers are current. The cusp's *shape* claim must be amended from power law to logarithm, and its sharpness held as regulator-suspect until the clip sweep runs.

Nominations, ranked:
1. **The clip sweep for the cusp** (§1) — clip ∈ {10⁻⁸, 10⁻¹⁶}; decides whether the cusp's sharpness is physics or regulator. Amend both committed exponent verdicts (0.17, 0.34) to the logarithmic reading regardless.
2. **The differential-QSL redo of Addendum 2's O(1)** (§2) — Bures-angle rate form; either it yields a constant or it shows the constant is channel-dependent, which would itself be a finding against the saturation claim's universality.
3. **Reframe "post-diction"** in ETRG-10 §3/§5 and the memory log (§3 above) — one sentence each.
4. **Carry-over (overnight audit):** P2's two derivation debts (thermal-seeding dilution assumption made explicit; κ̂₃ control systematics row) before any lab contact — unchanged, and ETRG-11's contact plan makes them due.
