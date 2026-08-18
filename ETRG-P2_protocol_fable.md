# ETRG-P2: The Three-Way Lock With Numbers

*Deliverable for agenda item 5 of ETRG-2.md §5 — "the P2 protocol with numbers: required precisions on T_H, S_ent, and lapse for a Steinhauer-class apparatus, at stated confidence." Constructive protocol prepared by Claude (Fable 5), August 2026. This document supersedes the P2 section of ETRG_experimental_protocol.md at the quantitative level; every change of assessment is flagged in §8. House rules apply — each number carries a flag: **[measured]** published apparatus value; **[derived]** derived in this document from flagged inputs; **[estimate]** order-of-magnitude, defended but not demonstrated; **[contingent]** depends on an undemonstrated capability; **[open]** could not derive. Nothing here has been vetted by an experimentalist; obtaining that vetting remains the point of the document.*

---

## 0. Scales and baseline apparatus

One clarification first. "A rubidium condensate at ~100 nK" (the brief's phrase) spans four distinct temperatures, three orders of magnitude apart, and the protocol lives at the coldest one:

| Scale | Value | Flag |
|---|---|---|
| BEC transition temperature T_c | ~10²  nK | [estimate — sets the "100 nK" folklore number] |
| Chemical potential μ/k_B | ≈ 8 nK | [measured: Steinhauer 2016] |
| Bulk phonon temperature T_bg | ≈ 0.8 nK | [measured class: Technion phonon thermometry] |
| Hawking temperature T_H | 0.351(4) nK | [measured: de Nova et al., Nature 569, 688 (2019)] |

Baseline apparatus (Steinhauer-class, values representative of the 2016–2021 Technion configuration; every derived number below must be recomputed from the actual profile of whatever apparatus runs this):

- N ≈ 8×10³ ⁸⁷Rb atoms, quasi-1D, radial confinement ω_⊥ = 2π×123 Hz **[measured]**
- Sound speeds c_out ≈ 0.57 mm/s (subsonic exterior), c_in ≈ 0.25 mm/s (supersonic interior) **[measured class]**
- Healing length ξ ≈ 2 μm **[measured class]**
- Analysis windows L_ext ≈ 100 μm, L_int ≈ 50 μm **[estimate]**
- Horizon quasi-stationary for T_obs ≈ 100 ms **[measured class: Kolobov et al. 2021 stationarity window]**
- Destructive absorption imaging; demonstrated ensembles ~10⁴ runs per configuration (7.4×10³ in the 2019 campaign) **[measured]**

Derived scales:

- **The modular rate:** κ = 2πk_B T_H/ħ = **288 s⁻¹** **[derived from measured T_H]**. One boost e-fold = 1/κ = 3.5 ms; the stationary window holds 29 e-folds.
- **Single channel:** k_B T_H/ħω_⊥ = 0.06 — transverse modes frozen out; exactly one phonon channel crosses the horizon **[derived]**.
- **Dispersion:** k_B T_H/μ ≈ 0.04 — the thermal band sits far below the dispersive knee; Planckian corrections to the spectrum are exponentially small over the band that carries the entropy **[derived]**.
- **Thermal band:** the entropy-flux integrand s(x), x = ħω/k_BT_H, has support mainly in x ∈ (0.3, 5), i.e. ω/2π ≈ 2–37 Hz **[derived]**. At these frequencies the thermal wavelength is 10–80 μm: the band contains only ~5–15 resolvable modes on each side of the cut. This is the single most important experimental fact in the protocol — the entropy legs are few-mode measurements, not field-theoretic continua.

---

## 1. (a) The lock as a single dimensionless residual

### 1.1 One rate, three readings

The near-horizon state is thermal with respect to the boost/modular generator at dimensionless modular temperature 1/2π; the surface gravity κ converts boost angle to laboratory time. The lock is the claim that three operationally independent books all read this one conversion rate:

1. **Spectrally** — the Hawking phonon spectrum is thermal at T_H = ħκ/2πk_B.
2. **As fine-grained bookkeeping** — the entanglement entropy across the horizon grows at the rate the modular flux dictates (the κ/12 law, §1.2).
3. **As coarse-grained clockwork** — the interior sector's Barontini-style observational entropy, the thing whose increments *are* entropic time, advances at the same rate (the Q10 weld).

### 1.2 The κ/12 law [derived]

Each horizon mode pair (Hawking quantum ω outside, partner inside) is produced in a two-mode squeezed vacuum whose single-side reduction is thermal with occupation n(ω) = 1/(e^{ħω/k_BT_H} − 1). The entanglement entropy per pair is s(n) = (n+1)ln(n+1) − n ln n, and the stationary flux over one 1D channel is

  Ṡ_ent = ∫ (dω/2π) s(n(ω)) = (k_B T_H/2πħ) ∫₀^∞ s(x) dx = (k_B T_H/2πħ)·(π²/3) = **π k_B² T_H / 6ħ**.

Substituting T_H = ħκ/2πk_B:

  **Ṡ_ent = κ/12  (nats per second, per channel).**

Equivalently, in fully dimensionless form: **a sonic horizon writes one-twelfth of a nat of entanglement per boost e-fold per channel.** This is the number all three legs must share. For the baseline apparatus: κ/12 = **24 nats/s = 2.4 nats per 100 ms window** [derived].

The law is standard two-mode-squeezing QFT **[import]** — it is not an ETRG novelty, and the program's claims do not rest on the coefficient (see §1.4 and §6). In the acoustic setting specifically it is **Giovanazzi's κ/12 proposal (PRL 106, 011302, 2011)**, which also proposed the number-fluctuation measurement channel that leg (ii) machinery uses — so leg (ii)'s observable class has 2011 prior art, and this protocol's novelty is the *lock* (third leg, residual, ordering), not the flux measurement (prior-art audit, ETRG_prior_art_audit.md). Two real-geometry corrections multiply it:

- **f — the infrared window factor.** s(x) diverges logarithmically as x → 0; the finite system cuts the integral at x_min = πħc/(L k_B T_H) ≈ 0.4 for the baseline geometry (both sides give x_min ≈ 0.34–0.39). Sharp-cutoff estimate: f = 1 − (2x_min + x_min ln(1/x_min))/(π²/3) ≈ **0.65 ± 0.10** **[derived, sharp-cutoff approximation; the ±0.10 is the honesty band for the soft-window correction]**. Longer condensates push f toward 1.
- **g — the greybody/Bogoliubov transmission factor**, the band-averaged mode-conversion efficiency of the actual flow profile. Literature analogy for waterfall profiles suggests g ≈ **0.9 ± 0.1** **[estimate — NOT derived here; requires a numerical Bogoliubov solve of the measured profile, §6]**.

Net predicted flux for the baseline: **Ṡ_lock = f·g·κ/12 ≈ 14 ± 3 k_B/s ≈ 1.4 nats per 100 ms** [derived from flagged inputs]. Against the interior's total thermal phonon entropy S_int ≈ (π/3)k_B(k_BT_bg/ħ)(L_int/c_in) ≈ 22 k_B at 0.8 nK [derived], the lock signal is a **~6% secular growth of the interior's entropy over the stationary window** — small but not heroic.

### 1.3 The three estimators and the residual

All three estimators are built from the *same* absorption-image ensembles (this drives the systematics cancellations of §4):

- **κ̂₁ ≡ 2πk_B T_H^meas/ħ** — T_H from the thermal fit to the Fourier-space Hawking–partner correlation spectrum (the demonstrated 2019 analysis, re-run concurrently).
- **κ̂₂ ≡ 12 Ḃ_fine / (f g k_B)** — with **Ḃ_fine ≡ İ/2**, the mutual-information flux across the cut divided by two, computed per mode pair from the Gaussian triple (n_H(ω), n_P(ω), |c(ω)|): local occupations from the mean-subtracted structure factor on each side, cross-correlation |c| = |⟨b_H b_P⟩| from the correlation-tongue Fourier amplitude — the same three observables the 2016/2019 nonseparability analyses already measured. For pure pairs İ/2 is exactly the entanglement-entropy flux; thermal seeding degrades the identification computably (§4.6). Log-negativity is reported alongside as the entanglement witness.
- **κ̂₃ ≡ 12 Ṡ_cg,hor / (f g k_B)** — the *horizon-attributed* interior coarse rate: the Barontini construction transplanted to the interior phonon sector. Operationally: mean-subtracted occupational entropy S_cg(t) = Σ_k s(n̄_k(t)) over the interior's horizon-adapted phonon modes, from ensemble variances at scanned hold times; Ṡ_cg,hor = (slope with horizon on) − (slope of the matched no-horizon control). The entropic-time lapse is dτ/dt = σ·Ṡ_cg; the calibration σ (agenda item 6, **[open]**) cancels in every ratio below, so the lock test does not wait on it.

**The residual.** The lock is the statement that (κ̂₁, κ̂₂, κ̂₃) ∝ (1, 1, 1). Define

  **Δ_lock ≡ √[ (1/3) Σ_{i<j} ln²(κ̂_i/κ̂_j) ]  — the lock predicts Δ_lock = 0.**

Only two of the three log-ratios are independent, and they carry different epistemic weight:

- **Δ_rate ≡ ln(κ̂₂/κ̂₁)** — the *spine*. Standard acoustic QFT predicts Δ_rate = 0 too; this residual is the in-situ proof that the Gaussian pipeline and the f·g corrections are under control, not an ETRG discriminator.
- **Δ_weld ≡ ln(κ̂₃/κ̂₂)** — the *program's* residual: coarse books = fine books at the horizon (Q10). Its decisive property: **f, g, σ, and the flow-profile κ all cancel exactly** — Δ_weld compares two entropy rates over the same cut, same band, same images. It is a theory-coefficient-free number.

**Decision statistic.** One-rate fit: χ² = Σᵢ (ln κ̂ᵢ − ln κ̄)²/σᵢ² minimized over κ̄, 2 degrees of freedom; the lock is rejected at 3σ if χ² > 11.8. The discrimination *from* the null (three unlocked rates) is carried by the tests of §2.4 and §3, since the null is the unconstrained superset.

### 1.4 What the residual does not need

No independently measured surface gravity (the flow-profile κ, with its velocity-derivative systematics, becomes an optional fourth cross-check rather than an input). No absolute entropy calibration σ. No f or g in Δ_weld. No phase-sensitive interferometric reconstruction in the baseline pipeline (§8, change of assessment). This is the lock's structural self-calibration: it is a ratio of readings of one rate, not a set of absolute measurements.

---

## 2. (b) Per-leg precision budgets

### 2.1 Leg (i) — T_H (spectral reading)

- **Demonstrated:** T_H = 0.351(4) nK statistical — 1.1% — from 7.4×10³ runs **[measured]**; agreement with the flow-profile prediction at the ~10% level. Dominant systematics: correlation-window and fit-band choices, ~5–10% **[estimate]**.
- **Requirement here:** σ(ln κ̂₁) ≤ 0.10. **Met by demonstrated technique at ~10⁴ runs.** Status: **demonstrated**.

### 2.2 Leg (ii) — Ṡ_ent (fine-grained reading)

- **Statistical floor [derived]:** ~5–10 informative mode pairs in the thermal band; per-pair triple (n_H, n_P, |c|) at ~10–15% relative from ~10⁴ runs (the 2019 campaign's demonstrated per-mode precision class); entropy-weighted average over pairs → σ_stat(Ṡ)/Ṡ ≈ 5–8%. Stationarity converts the flux spectrum into the rate without multiplying the ensemble by time bins (a subsampled 3-bin stationarity check costs ~30% more runs).
- **Systematics [estimate]:** Gaussianity assumption, mode-window definition, thermal-seeding correction (§4.6): 10–15%.
- **Requirement:** σ(ln κ̂₂) ≤ 0.20. **Budget: 15–20% total at ~10⁴ runs — meets the requirement without margin.** Status: **demonstrated-class observables, contingent pipeline** — the covariance-based entropy extraction has not been performed on horizon data; it is the same Gaussian machinery as this repository's lattice suite applied to measured correlations, and §8 explains why this is a milder contingency than the phase-sector reconstruction the July protocol document assumed.

### 2.3 Leg (iii) — Ṡ_cg (coarse-grained clock reading)

- **Signal:** Ṡ_lock ≈ 14 ± 3 k_B/s above the technical baseline; the no-horizon control measures the baseline directly.
- **Statistical floor [derived]:** per hold-time bin, ~10 interior modes with occupations from ensemble variances: σ_n/n ≈ √(2/M) ≈ 8% at M = 300 shots/bin; σ per mode s(n): ~0.07 k_B; per-bin σ_S ≈ 0.25 k_B, inflated ×2 for correlated imaging noise → 0.5 k_B. Slope over 10 bins spanning 100 ms: σ(Ṡ) ≈ 5.5 k_B/s at 3×10³ runs; **σ(Ṡ) ≈ 4–5 k_B/s at 5×10³ runs**, ~3σ on the weld detection; the matched horizon-off control doubles the count.
- **Requirement:** detect Ṡ_cg,hor > 0 at ≥3σ (σ ≤ 4.7 k_B/s) and σ(ln κ̂₃) ≤ 0.25–0.33.
- **Budget: ~1×10⁴ runs including controls.** Status: **demonstrated-class** (structure-factor thermometry + destructive hold-time scans are standard; the Barontini analysis transplants at the ensemble level). Note the transplant refinement: the tracked sector is the interior *phonon field*, mean-subtracted — the bulk atom-number partition entropy is dominated by transport and buries a 14 k_B/s signal by orders of magnitude (§8).

### 2.4 The 3σ arithmetic

| Quantity | Lock prediction | Null | Required (3σ) | Achievable (est.) | Runs | Status |
|---|---|---|---|---|---|---|
| T_H | 0.351 nK | (free) | ≤10% | ~1% stat, 5–10% syst | 10⁴ | demonstrated |
| Ṡ_ent (κ̂₂) | 14±3 k_B/s | (free) | ≤20% | 15–20% | 10⁴ (same images as leg i) | contingent pipeline |
| Ṡ_cg,hor (κ̂₃) | 14±3 k_B/s | **0** (no weld) | σ ≤ 4.7 k_B/s | 4–5 k_B/s | 10⁴ incl. controls | demonstrated-class |
| Ordering D (§3) | 1 | 0 | σ_D ≤ 0.33 | ≈ 0.18 | 4×10³ | demonstrated-class |

- **Weld discrimination:** the no-weld null (coarse books blind to the horizon flux) is rejected at ≥3σ by the leg-(iii) detection alone; consistency κ̂₃ = κ̂₂ is then tested by Δ_weld with σ(Δ_weld) ≈ √(0.20² + 0.25²) ≈ 0.32 → a 3σ weld violation is any factor ≥ e^{0.96} ≈ **2.6** between the two books.
- **Pairwise rate-mismatch sensitivity at 3σ [derived from the budgets]:** factor **2.0** (legs i–ii), **2.2** (i–iii), **2.6** (ii–iii). Any leg pair unlocked by a factor ≥2.6 is detected; the sharpest pair resolves a factor 2.
- **Campaign total:** ~2.7×10⁴ runs (stationary ensemble 10⁴, hold-scans + controls 10⁴, ordering configs 4×10³, onset fine-bins 3×10³) ≈ **3.5× the 2019 campaign's ensemble**; at a 20 s cycle this is ~6 days of pure cycling, realistically **one to two months wall-clock** **[estimate — duty-cycle assumption, §6]**.
- What this cannot do at 3σ: resolve a subtle (≤30%) leg mismatch — that requires per-leg budgets at the ≤7% level, which leg (ii) does not support with current technique **[honest limit]**.

---

## 3. (c) The leg-ordering protocol with expected signal sizes

**The operational core, stated once:** a coherent injection is a phase-space *displacement* — it moves ensemble-*mean* observables and leaves every covariance, hence every Gaussian entropy, exactly unchanged; an incoherent injection of equal energy moves the *variances*. The lock's claim that geometry and clocks read the entropy ledger is therefore the claim that **the entropy legs read the variance ledger and are exactly blind to the mean ledger**. Destructive imaging measures both ledgers simultaneously: the mean ledger is the ensemble-averaged density profile, the variance ledger is the mean-subtracted fluctuation statistics. The discriminator needs no new measurement capability — only two extra preparation sequences.

**Configurations (interleaved shot-by-shot):**

| Config | Preparation | Ensemble |
|---|---|---|
| C0 | horizon, no injection (reference) | shared with leg iii |
| C1 | + coherent injection: Bragg pulse / phase imprint into an interior mode, ω/2π ≈ 30 Hz | ~10³ |
| C2 | + incoherent injection: matched-energy broadband noise pulse (projected speckle intensity noise or trap-bottom noise burst, 10–100 Hz band) | ~10³ |
| C3 | no horizon, either injection (control for injection-only entropy) | ~10³ each |

**Matched energy, with numbers [derived]:** deposit E = k_B × 4.9 nK into the interior — the incoherent version raises the interior phonon temperature 0.8 → 1.0 nK. Then:

- **Incoherent signal:** ΔS = ΔU/T̄ ≈ **5.5 k_B** rise in both entropy books (S ∝ T for the 1D phonon gas: 22 → 27 k_B).
- **Coherent signal:** the same energy is a coherent phonon of |α|² ≈ **3.4 quanta at 30 Hz** — visible as an ensemble-mean density oscillation of measurable amplitude, decaying at the mode's damping rate. Predicted entropy-book response: **0**, with a floor set by mean-subtraction imperfection, estimated ±0.2 k_B and measured directly on config C0 **[estimate + in-situ measurement]**.
- **Both configs** move the energy legs identically (that is the matching verification: mean-subtracted variance thermometry + time-of-flight released energy agree on E to ~10%); T_H itself should move in neither (the injections do not touch the flow profile) — a free consistency check.
- **Noise floor:** per-config σ(ΔS) ≈ 0.7 k_B at ~10³ runs [derived from the leg-(iii) per-bin budget]. The discriminator statistic D ≡ (ΔS_inc − ΔS_coh)/ΔS_pred has σ_D ≈ √2·0.7/5.5 ≈ **0.18**: the lock's D = 1 sits **≈5.5σ** from the both-legs-are-calorimeters null D = 0. Energy-matching error at 10% shifts the null by 0.1 — negligible against the separation.
- **The dial:** all signals scale linearly upward with E until T approaches μ/k_B; E = k_B×15 nK triples the separation if floors disappoint, at the cost of a warmer interior.

**The time window [honest constraint]:** the coherent zero is exact for Gaussian dynamics; phonon–phonon (Beliaev/Landau) damping eventually thermalizes the coherent mode and moves its energy into the variance ledger. At T_bg ≈ 0.8 nK ≪ μ/k_B both processes are strongly suppressed and the damping time is expected ≫ 100 ms **[estimate — not derived; the mode's own measured amplitude decay in C1 supplies τ_damp from the same data, self-calibrating the window]**. Measure ΔS at t_delay = 10–30 ms ≪ τ_damp.

**Bonus prediction — the ledger balances late:** as t → few×τ_damp, ΔS_coh(t) must rise to meet ΔS_inc, at the rate set by the measured amplitude decay. A coherent excitation whose energy *never* appears in the entropy books at the measured damping rate breaks the bookkeeping identity (kill row K5). This late-time check turns the damping systematic into a second signature.

**Ordering outcomes:** lock — ΔS_coh = 0, ΔS_inc = 5.5 k_B (D = 1). Reversed — coherent moves the books, incoherent does not (D < 0): falsifies the modular mechanism specifically. Both-move (D ≈ 0 with common shift): entropy legs are calorimeters; the leg-resolved content of the lock is dead.

---

## 4. (d) Dominant systematics, and how the lock self-calibrates

1. **Surface-gravity determination.** Traditional κ extraction differentiates a fitted velocity profile at the sonic point — the noisiest operation in the analogue-gravity literature. *Self-calibration:* κ never enters; κ̂₁ (a spectral fit) is the rate reference, and the residuals are ratios. The profile-derived κ is demoted to an optional fourth reading.
2. **Absolute entropy calibration (σ).** *Cancels* — every test is a rate ratio; leg (iii) is reported in nats/s, and the "lapse" interpretation multiplies by σ downstream of all decisions.
3. **f and g (window and greybody).** Enter Δ_rate only; both computable from the same dataset's measured profile and band **[g: open until the Bogoliubov solve, §6]**. *Cancel exactly in Δ_weld and in D* — the program-critical residuals are immune to the two least-derived theory factors.
4. **Imaging calibration drift and stray light.** Both entropy legs and the spectrum are extracted from the *same interleaved image ensembles*; slow drifts are common-mode in the ratios at first order. Interleaving C0–C3 shot-by-shot extends this to the discriminator.
5. **Atom-number day-to-day variation.** κ ∝ c ∝ √n: number drift smears every absolute rate. *Self-calibration — the N-binning lever:* bin all runs by measured atom number; the lock predicts all three κ̂ᵢ co-vary across bins (ratios flat, absolutes moving together). A systematic mimicking one leg will not track the others. The worst cold-atom systematic becomes an internal consistency test at zero cost.
6. **Thermal seeding of the in-modes** (T_bg > T_H). Stimulated pair production inflates occupations: n_out = n₀ + (1+2n₀)|β|², degrading the pure-pair identification İ/2 = Ṡ_ent. *Mitigation:* n₀(ω) is measured directly (pre-formation structure factor); the per-mode correction is computable Gaussian algebra; the correction is largely common to both entropy books (partial cancellation in Δ_weld); the discriminator is differential and immune. Residual after correction: folded into leg (ii)'s 10–15% systematic **[estimate]**.
7. **Cut-position ambiguity** (horizon located to ~ξ). Both books share the cut. *Self-calibration:* scan the analysis cut ±5 μm; the lock predicts a plateau in Δ_weld (both legs shift together); a spurious signal localized in one book will not plateau.
8. **Correlation-analysis windowing** (leg i's historical soft spot). Shared with the published 2019 analysis; vary the band and require plateau, as there.
9. **Correlated imaging noise** (the floor-inflation that P1's 0.7% lesson taught). All statistical floors above carry an explicit ×2 inflation; the actual autocorrelation is measured from injection-free ensembles and replaces the guess **[estimate until measured]**.
10. **Slow non-stationarity** (horizon ramp, inner-horizon formation late in the window — seen in 2021). Restrict to the stationarity-verified window via the 3-bin subsample; the onset measurement (§5, row K6) uses only the first 20 ms.
11. **Partition-choice circularity** — the round-7/8 lesson from this repository's lattice work: consistency checks that pass for *any* partition carry no selection content. *Control at zero experimental cost:* recompute S_cg(t) from the same covariance data in deliberately scrambled interior mode bases. The lock (Q10's selection content) predicts the horizon-adapted basis's books tick at f·g·κ/12 and scrambled-basis books fail to show the clean rate — the laboratory analogue of `drift_check.py`'s geometric-vs-scrambled discrimination (round 8, PASS). If every basis ticks identically, the weld's selection claim is empty at horizons (row K7).

---

## 5. (e) Kill criteria

| # | Measured outcome | Verdict | What dies |
|---|---|---|---|
| K1 | Ṡ_cg,hor consistent with **zero** at 3σ while κ̂₂ confirms the fine flux | **KILL** | The Q10 weld — coarse clock books and fine entanglement books are *not* one structure at a real horizon. T1/T2's stitching falsified; the program's central identification fails where it was proven most defensible. |
| K2 | **Reversed ordering:** coherent injection moves the mean-subtracted entropy books beyond the damping-window accounting, and/or matched incoherent injection does not (D significantly < 1, or < 0) | **KILL** | The modular mechanism specifically — geometry/clocks do not read the variance ledger. This is the mechanism-specific falsifier; no appeal to analogue-system deficiency survives it, because the prediction is about the bookkeeping, not about gravity. |
| K3 | **Both entropy books move equally** under matched coherent and incoherent injections (D ≈ 0, common shift ≈ 5.5 k_B) | **KILL** (of the leg-resolved content) | The entropy legs are calorimeters; the three-way lock collapses to energy conservation and loses its discriminating power. The program is not contradicted but loses its flagship laboratory test. |
| K4 | Lock ratios hold on average but **fail to co-vary under N-binning** (κ̂ᵢ move independently across atom-number bins) | **KILL** | "One rate" as a structural fact — the agreement was numerical coincidence at one operating point, not a lock. |
| K5 | **The ledger never balances:** coherent-injection energy fails to appear in the entropy books at the independently measured damping rate | **KILL** | The bookkeeping identity (entropy books ↔ energy flow through one rate) that T2 rests on. |
| K6 | Coarse rate matches f·g·κ/12 at late times but **onset lags** the horizon formation by ≫ 1/κ = 3.5 ms (e.g. > 30 ms, resolved by 2 ms bins over the first 20 ms) | **Downgrade, not kill** | The weld's *identity* claim — books that equilibrate into agreement are a thermalization shadow, not one structure. The lock survives as consistency; Q10's laboratory support does not. |
| K7 | **Scrambled-basis books tick identically** to the horizon-adapted basis (§4.11) | **Downgrade, not kill** | Q10's selection content at horizons — "every partition's clock runs at κ" would make the weld trivially true and empty, mirroring the round-7 region-agnostic lesson. |
| K8 | Δ_rate ≠ 0 at 3σ with f, g, and seeding corrections exhausted | **Suspend, not kill** | Not an ETRG-specific failure — legs i–ii locking is shared with standard acoustic QFT. This outcome indicts the pipeline or the analogue system (and would be its own headline); no lock inference in either direction until resolved. |
| — | **What does NOT kill:** common-mode offsets in all three absolute rates (calibration, not lock failure); leg-(ii) pipeline proving infeasible (program untested, not falsified — say so plainly); discrepancies within the ±35% f·g theory band pending the profile computation. | — | — |

A clean run — K1–K8 all passing — is, to our knowledge, the first measurement tying an analogue horizon's temperature, its entanglement flux, and an interior relational clock through one rate at stated confidence, and the first laboratory instance of the coarse/fine weld the program's Q10 theorem asserts. Honest scoping from the July document carries over unchanged: this corroborates the *stitching*, not gravity.

---

## 6. What we could not derive

1. **g**, the band-averaged greybody factor: requires a numerical Bogoliubov scattering solve on the measured flow profile. Bounded 0.8–1.0 by literature analogy **[estimate]**; cancels in Δ_weld and D, so no program-critical test waits on it.
2. **f** beyond the sharp-cutoff approximation: the soft-window correction needs the actual mode functions; ±0.10 honesty band assigned.
3. **τ_damp**, the coherent-mode damping time at 0.8 nK in the flowing quasi-1D geometry: no reliable formula at this temperature and geometry; the protocol measures it in situ (C1 amplitude decay) rather than assuming it.
4. **The correlated-noise inflation factor** on all statistical floors: taken as ×2 by fiat; must be replaced by the measured image-noise autocorrelation.
5. **σ(ħ, k_B, T)** — the absolute entropic-time calibration (agenda item 6): open; deliberately routed around via ratio tests.
6. **The interior geometry numbers** (L_int, c_in, hence S_int = 22 k_B and the 5.5 k_B discriminator signal): representative, not measured for this purpose; formulas provided so the actual apparatus substitutes its own.
7. **Cycle time and duty cycle** for the campaign-length estimate: assumed 20 s and ~30% uptime **[estimate]**.
8. **The κ/12 coefficient's robustness** to non-universal mode normalization in the specific waterfall geometry: if an O(1) correction exists it moves Δ_rate only; Δ_weld and D are coefficient-free by construction.

---

## 7. Statistical decision summary

Three-sigma discrimination of the lock from its null decomposes as:

1. **Weld existence** (vs. K1's null): Ṡ_cg,hor > 0 at ≥3σ — leg-(iii) budget, ~10⁴ runs.
2. **Weld identity:** |Δ_weld| < 3σ(Δ_weld) ≈ 0.96, i.e. books equal within a factor 2.6 at 3σ; onset within the first ~2 bins (K6).
3. **Ordering** (vs. K2/K3's nulls): D = 1 at ≈5.5σ separation from D = 0 — the strongest single test in the protocol.
4. **Spine:** Δ_rate = 0 within ~20–25% (shared-QFT consistency; gates inference, K8).
5. **Structure:** N-binning covariance (K4) and scrambled-basis control (K7) from the same data, no extra runs.

The combined one-rate χ² (2 dof, reject above 11.8) summarizes 1–4; rows 3 and 1 are where the program's specific content stands or falls.

---

## 8. Changes of assessment relative to ETRG_experimental_protocol.md (July 2026)

1. **Leg (ii) risk downgraded — the principal change.** The July document made phase-sector interferometric reconstruction the gate for any entanglement-entropy number and named it the protocol's principal risk. This document observes that the *rate* κ̂₂ requires only the Gaussian pair triple (n_H, n_P, |c|) per mode — all three demonstrated observables of the 2016/2019 correlation analyses — under an explicit, testable Gaussianity assumption. Phase-sector reconstruction is upgraded from *required* to *desirable for model-independence*. The contingency does not vanish; it shrinks from "undemonstrated measurement" to "undemonstrated analysis pipeline on demonstrated measurements."
2. **Leg (iii) estimator sharpened.** "Interior = bright sector, Birmingham analysis verbatim" would drown a 14 k_B/s signal in bulk-transport entropy. The transplant is refined to the interior *phonon* sector, mean-subtracted — which is also exactly the operationally-consistent coarse-graining class Q10 selects, making the estimator choice principled rather than convenient.
3. **The discriminator made operational.** "Coherent leaves the entropy leg untouched" is sharpened to the mean-ledger/variance-ledger statement, which standard destructive imaging already measures both sides of; expected signals (5.5 k_B vs 0 ± 0.7 k_B) and the damping window are now explicit, and the late-time ledger balance is added as a second signature.
4. **The lock rewritten κ-free and σ-free.** The July χ²-on-one-κ formulation implicitly required the flow-profile surface gravity and an entropy-to-time calibration; both are now eliminated by the ratio structure.
5. **Numbers replace targets.** "~20% consistency test" becomes: factor-2.0–2.6 pairwise mismatch sensitivity at 3σ, a 3σ weld detection, and a 5.5σ ordering separation, at a stated campaign size (~2.7×10⁴ runs, ~3.5× the 2019 ensemble).

*Provenance: κ/12 law, window factor f, all signal sizes, precision budgets, and the residual structure derived in this document from the flagged inputs; two-mode-squeezing thermality and the Gaussian entropy machinery are imports; the weld's discrimination hierarchy (§4.11, K7) incorporates the round-7/8 lattice lessons (region-agnostic passes are empty; geometric-vs-scrambled drift is the discriminating form). Numerical cross-checks of the arithmetic in this document would be a natural next lattice task but do not exist yet — the derivations above are closed-form and checkable by hand.*

---

## 9. The fourth leg: the Page series — Fable addendum

*Added August 2026 (Fable), at the originator's direction, extending ETRG-6 §2 (the information-paradox entry) into this protocol: the entanglement-entropy TIME SERIES across the horizon. Same house rules and flags as §§0–8. The section corrects one piece of ETRG-6 §2's optimism on the way in (§9.1); scope is stated in §9.6.*

### 9.1 The correction first: a sustained horizon has no Page turnover

ETRG-6 §2 calls the Page curve "in principle measurable in an analogue horizon." The two-face bookkeeping itself says: **not in the standard configuration.** The Page decline requires the reservoir's coarse book to shrink — in gravity, evaporation shrinks the hole. The analogue horizon is externally sustained: the flow profile is imposed by the trap, nothing back-reacts, and the interior's book only grows. Over the 100 ms window the accumulated flux (≈1.4 nats) sits an order of magnitude below the interior's standing book (≈22 k_B, slack ×15): the capacity bound never binds. **For the sustained horizon the two-face prediction is monotonic linear growth with no turnover — the *absence* of a Page knee is the prediction, and a spontaneous turnover would be evidence against the bookkeeping, not for it** (row K9). A Page-shaped series must be engineered by squeezing the reservoir from outside (§9.3). This paragraph stands as a correction to ETRG-6 §2's flag.

The structural statement, all configurations. Let Ŝ_fine(t) be the horizon-attributed entanglement across the cut (the κ̂₂ machinery, İ/2 per hold-time bin) and Ŝ_cg,int(t) the interior coarse book (the κ̂₃ machinery), both as excesses over matched no-horizon controls. The two-face claim, time-resolved:

  **Ŝ_fine(t) = Ŝ_cg,int(t) at every t — Δ_weld(t) = 0 through growth, knee, and fall — with common shape min( ∫₀ᵗ f·g·κ dt′/12 , capacity(t) ).**

The min-envelope is the two-face reading of the Page/island structure: the fine book tracks the lower of flux-accumulation and coarse capacity **[import at the level of form]**. The inequality S_vN ≤ S_obs is a theorem (observational entropy bounds von Neumann entropy from above), so the bound itself cannot fail; the falsifiable content is *saturation* — one book, not two, at a horizon — which is Q10's weld promoted from a rate identity to a trajectory identity **[derived at the idealized level; estimator caveats §9.5]**.

### 9.2 P-stat — the growth phase (runs mostly on already-budgeted data)

Predicted shape **[derived]**:

- onset within 1/κ = 3.5 ms (K6's fine bins already watch this);
- linear thereafter: slope f·g·κ/12 = 14 ± 3 k_B/s ≡ 0.049 nats per boost e-fold; 29 e-folds in the window → endpoint 1.4 nats;
- curvature zero; no saturation and no decline anywhere in the window.

Estimator and cost: the leg-(iii) hold scans already collect time-binned ensembles; Ŝ_fine(t) is a *new analysis* (the Gaussian triple per bin) of the same images, plus ~3×10³ extra runs to fill late-window bins **[estimate]**. Per-bin σ ≈ 0.3 k_B at 10³ runs/bin **[derived, ×2 correlated-noise inflation as in §2.3]**.

Sensitivity **[derived]**: a mid-window stall shows as a late-bin deficit of 0.4–0.7 k_B per bin → ≈4σ combined over the last four bins. Honest limit: a smooth ≤20% bend is *not* resolvable at this budget. Super-linear late growth is the 2021-class inner-horizon stimulation — truncate the window, not a kill; note it has the wrong sign to fake a Page fall (stimulation raises occupations, a turnover lowers entanglement).

### 9.3 P-off and P-ramp — the engineered knees

**P-off (horizon shutoff — the cheap knee).** Ramp the step away at t_off ≈ 60 ms, leaving both regions intact. The flux stops; the pairs already created keep their entanglement — nothing returns the partners. Prediction: rise at 14 k_B/s → plateau at ≈0.84 k_B, knee sharp to ~1/κ = 3.5 ms; post-shutoff slope 0, with continued 14 k_B/s growth excluded at ~3σ from ~8×10³ runs **[derived from the §2.3 slope budget]**. This is itself an anti-naive prediction worth publishing: **even killing the horizon produces no Page decline in the analogue** — the decline needs the interior *region* dismantled, not the horizon. Post-shutoff continued rise at the flux rate: estimator artifact or thermalization contamination — suspend. Post-shutoff decline: entropy leaving without carriers — feeds K11.

**P-ramp (reservoir squeeze — the full curve) [contingent].** Start with a short interior, L_int(0) ≈ 12 μm — standing book 3.6 k_B by discrete band sum (8 thermal-band modes at 0.8 nK; the continuum formula's 5.3 k_B overestimates at this length) **[derived]**. Hold 40 ms; then sweep the terminating wall to shrink L_int → 4 μm ≈ 2ξ over the final 60 ms. The mode ladder ω_k(t) = kπc_in/L_int(t) climbs out of the thermal band; the band count falls 8 → 2; the sharp-band capacity template S_cap(t) = Σ_k s(n(x_k(t))) collapses 3.6 → ≈0.7 k_B **[derived as template; [estimate] beyond the sharp band]**.

What the mode dynamics does with the squeezed entropy is **not derived here** — three outcomes, all covered:

1. **Expulsion across the cut** (non-adiabatic conversion at the shrinking end): the Page fall proper. Total interior book falls ~3 k_B over the final ~30 ms (≈100 k_B/s, ~7× the growth slope — a 10σ cumulative feature at per-bin σ 0.3–0.4 k_B); the horizon-attributed *excess* falls ~0.5–1 k_B (≈3σ at 10³ runs/bin; ≈5σ with post-knee bins at 3×10³) **[derived from template + budgets]**. Carrier accounting is the signature: the fall must reappear as a late pulse in exterior-band occupations, arriving over the c_out-crossing time 10–30 ms — ETRG-6 §2's "reconciling, not escaping" made watchable.
2. **Adiabatic heating** (per-mode entropy conserved as ω rises): no fall, books rise together, the squeeze failed to squeeze — configuration failure, suspend not kill.
3. **Conversion to non-phonon interior carriers**: the tracked books fall while total entanglement hides in the particle sector — the main interpretive risk (K12), checked by interior time-of-flight spectra **[open]**.

The two-face content is outcome-independent: **whichever branch runs, the two books must track each other through it.** Δ_weld(t) = 0 is the prediction in all three branches, and it is template-free, f·g-free, and piston-free (both books see the same injections).

Wall-speed constraint **[honest]**: sweeping 8 μm in 60 ms is 0.13 mm/s ≈ 0.5 c_in — the wall is a Mach-0.5 piston injecting its own excitations. Control C-ramp-0 (same sweep, no horizon) measures the piston book and is subtracted; Δ_weld(t) is immune (common-mode), but the Page *shape* rides on the subtraction. If piston injection ≳ signal, the configuration fails — suspend. A 200 ms stationarity window would halve the wall Mach **[contingent on apparatus]**. Dial: a steeper profile (T_H → 0.7 nK) doubles the flux and the excess-curve amplitude **[estimate]**.

**Precision summary [derived unless flagged]:**

| Series feature | Prediction | Achievable (est.) | Runs |
|---|---|---|---|
| P-stat slope | 14 ± 3 k_B/s, linear | σ ≈ 4–5 k_B/s; stall ≈ 4σ; 20% bend unresolved | shared + 3×10³ |
| P-off knee | plateau 0.84 k_B at t_off, knee ≤ 3.5 ms | continued rise excluded ~3σ | 8×10³ |
| P-ramp fall, total book | ~3 k_B over final 30 ms | ~10σ cumulative | 2×10⁴ incl. control |
| P-ramp fall, excess book | 0.5–1 k_B | ~3σ (5σ with post-knee bins) | — same data |
| Book synchrony Δ_weld(t) | 0 throughout | 3σ per bin at 1.3 k_B split; lag ≥ 2 bins (~15 ms) resolvable | same data |

### 9.4 Kill rows (extending the §5 table)

| # | Measured outcome | Verdict | What dies |
|---|---|---|---|
| K9 | P-stat: Ŝ_fine saturates or declines at ≥3σ while κ̂₁, κ̂₂ hold steady | **KILL** | The weld as a *dynamical* identity — books that agree on rates but not on integrals are two books. |
| K10 | Any configuration: the books de-synchronize through a knee — Δ_weld(t) = 0 before, \|Ŝ_fine − Ŝ_cg,int\| ≥ 1.3 k_B (3σ) at/after, or a sustained lag ≥ ~15 ms between the books' falls | **KILL** | The two-face identity exactly where ETRG-6 §2 spends it: if the faces separate at the turnover, "the Page curve is the two books reconciling" is false *as structure*, whatever gravity does. |
| K11 | The books fall with no matching carrier flux into the exterior band (and no K12 particle sector found) | **KILL** | The bookkeeping identity — entropy cannot leave the ledger without carriers. |
| K12 | Interior TOF shows the squeezed entropy parked in non-phonon carriers | **Confound, not kill** | The phonon-sector books reconcile while total entanglement hides; the Page claim is untested until the particle sector is included in both books. |

### 9.5 Estimator honesty

- İ/2 = entanglement flux is exact for pure pairs; thermal seeding (T_bg > T_H) makes the series a corrected estimate — the §4.6 per-mode correction applies per bin; residual 10–15% **[estimate]**, largely common-mode between the books (partial cancellation in Δ_weld(t)).
- During the ramp the analysis basis must follow the instantaneous mode ladder computed from the measured L_int(t) — the same contingency class as the leg-(ii) pipeline, now time-dependent.
- The capacity template is sharp-band and serves *timing prediction only* — every kill row above is template-free.

### 9.6 Budget and scope

Addition to the campaign: P-stat ≈ 3×10³ (mostly reanalysis), P-off ≈ 8×10³, P-ramp ≈ 2×10⁴ with control → campaign total ~5–6×10⁴ runs ≈ **7–8× the 2019 ensemble**; wall-clock roughly 3 months at the §2.4 duty-cycle assumption **[estimate]**. The ladder is deliberately graded: P-stat is demonstrated-class analysis of budgeted data, P-off adds one ramp on demonstrated controls, P-ramp is [contingent] and is the only rung that shows a fall.

Scope, stated plainly: this leg tests none of the gravitational machinery — no islands, no replica wormholes, no back-reaction (the flow is imposed, not sourced by the phonons). What it tests is the claim ETRG-6 §2 actually makes: that a horizon keeps **one book read two ways**, through a full rise-and-fall cycle, with reconciliation by physical carrier flow. K10 is that claim's laboratory exposure — and if the two books separate at the knee, no appeal to "it's only an analogue" survives, because the claim was about bookkeeping, not about gravity.

*Provenance: shapes, templates, and budgets derived here from §0–§2 inputs; the min-envelope is imported at the level of form from the Page/island literature; mode conversion at the moving wall, the piston spectrum, and the seeding-corrected estimator at few-k_B amplitudes are this section's [open] items.*
