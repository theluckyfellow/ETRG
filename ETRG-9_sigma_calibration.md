# ETRG-9: The σ Calibration — Entropic Time's Exchange Rate at Equilibrium

*August 2026, Kimi-K3. Gate 2, third item (ETRG-8): "The σ calibration — entropic time's absolute exchange rate, which P2 deliberately routes around with ratios. Three acceptable resolutions: fix it, explain it, or prove it conventional." This note attempts the second: explain it. The answer is short and, in retrospect, inevitable: at equilibrium the KMS condition fixes σ completely, and it is the same constant that A3's clock-thermodynamics bound is made of. Status: **[derived at equilibrium]**; the off-equilibrium extension is Gate 1b's business, stated in §4.*

---

## 1. The question

A2 defines entropic time as τ = (σ/k_B)∫|dS|, with σ fixed empirically per system (Barontini). The Q10 note's attack 5 asked: does the program's own machinery fix σ = σ(ħ, k_B, T) up to a pure number? If entropic time is to be parameter-free, the calibration must come from inside.

## 2. The derivation (three lines of modular theory) — and its honest boundary

At equilibrium at temperature T, the state is KMS: ρ ∝ e^{−H/k_BT}, and its modular Hamiltonian is

$$K = \frac{H}{k_B T} \quad \text{(dimensionless)}.$$

The modular flow σ_s(A) = e^{iKs} A e^{−iKs} with dimensionless parameter s, compared with Heisenberg evolution e^{iHt/ħ}, gives the physical time per unit modular parameter:

$$t = \frac{\hbar}{k_B T}\, s .$$

— the Connes–Rovelli thermal-time conversion (1994, to be cited as the source of this step). **[import]**

**Referee's correction (F1, accepted):** the next step of the original note — "at equilibrium, entropy exchange per unit modular parameter is one nat, dS = k_B·ds" — is **false at strict equilibrium and is not the first law**. A KMS state is a fixed point of its own modular flow: dS/ds = 0 exactly; the equilibrium state exchanges nothing. The first law δS = k_B δ⟨K⟩ relates *neighboring states*, not displacement along the flow. The one-nat-per-s normalization was a stipulation chosen so the calibration comes out dτ/dt = 1.

What survives the correction: the conversion t = (ħ/k_BT)·s is correct and standard, and σ must therefore be

$$\sigma = \frac{\hbar}{k_B T} \times (\text{pure number})$$

on dimensional grounds — ħ/(k_BT) is the *only* timescale constructible from (ħ, k_B, T). What does not survive: the claim that the pure number is 1, and any "KMS forces σ" phrasing. **Status: [calibrated at equilibrium — the scale is forced by KMS; the O(1) normalization is stipulated].** The gap is fixable in principle (derive the nat count from the entropy flux of a weakly coupled probe exchanging heat with the KMS bath); that derivation is not yet in the program.

## 3. The convergence with A3 — suggestive, not a theorem (referee-corrected)

The same constant appears in A3's clock thermodynamics (Erker 2017): their theorem is an entropy-per-tick vs accuracy trade-off, from which a minimum tick time ≳ ħ/(k_BT) follows *as an inequality with its own O(1) factor*. Read together with §2:

> **A2's calibration scale and A3's tick-time bound are the same timescale** — ħ/(k_BT), the thermal de Broglie time, the only scale constructible from (ħ, k_B, T).

**Referee's correction (F4, accepted):** this identification is currently *dimensional necessity, not a theorem* — any two quantities built from (ħ, k_B, T) must coincide up to pure numbers, and the note declines to fix those numbers (and the Erker bound is an inequality, the calibration an equality — exactly the gap the pure numbers hide in). To upgrade to a theorem: derive both O(1) factors and show they are equal. The identification is suggestive and worth having; the [structural identity] tag originally attached was unearned. **[suggestive convergence, flagged at dimensional-analysis strength]**

Consequence for Barontini (the note's best content, kept): the empirical σ extracted from the cold-atom data should equal ħ/(k_BT_eff) for the effective temperature of the observed sector's exchange channel. **Pre-registration (referee-required): T_eff must be fixed before the comparison — defined as the temperature of the exchange channel's fitted thermal occupation in the published analysis, not fitted to σ.** A checkable cross-consistency between the experiment's two independent constructions, available from the authors' numbers. **[nominated check — requires the Barontini group's data, with T_eff pre-registered]**

## 4. What this does not fix

- **Off-equilibrium.** T varies; near stasis the exchange stalls. There the A7 lapse Ñ[ψ] = |dS/dt|⁻¹ takes over — the calibration becomes state-dependent, and whether a closed σ(ħ, k_B, state) exists is exactly the off-equilibrium closure problem. *(Referee F7: this remainder was punted to "Gate 1b," but ETRG-11's Problem 1b is constraint closure only — the remainder is now explicitly owned by the Gate-2 remainder item in ETRG-11 §Remainders.)*
- **The pure number.** The KMS conversion t = (ħ/k_BT)s carries no 2π for a genuine Gibbs state; the 2π belongs to the geometric (Unruh/Bisognano–Wichmann) derivations. The normalization of the nat count (F1) is the live gap, not a convention.
- **Uniqueness.** The derivation shows KMS *forces the scale* of σ at equilibrium; whether any non-KMS equilibrium notion could give a different calibration is assumed away by A2's thermal anchoring (T1).

## 5. Gate-2 scoreboard after this note (referee-adjusted)

- **σ calibration:** from "unfixed" to **scale explained at equilibrium** — σ = ħ/k_BT up to a stipulated O(1) normalization (F1); the identity with the tick time is suggestive, not proven (F4); Connes–Rovelli cited for the conversion. The equilibrium anchor is now the right constant for the right reason at the dimensional level.
- **Second cosmological observable:** `ETRG-10_second_observable.md` — formulated, and possibly already decided (see its branch structure).
- **No-Page-knee:** already in hand (ETRG-P2 §9) — unchanged, still the closest owned number.

*One gate item, one honest scope. The constant was the tick scale all along; whether it is the tick itself is now a named, pre-registered question.*

---

## Addendum: the Barontini cross-check, executed — and the resolution it forces

The nominated check was executed against the published paper (arXiv:2509.07745, in-repo PDF). Findings:

1. **Barontini's σ is declared arbitrary.** Eq. (3) of the paper defines τ = (σ/k_B)∫(dS/dφ)|dφ| with σ "the (arbitrary) entropic time unit," and the effective Schrödinger equation (their Eq. 6) rescales consistently under σ (the lapse Λ carries 1/σ). **The experiment is agnostic on σ's physicality: it uses σ as a unit choice.** The cross-check as originally posed is void — there is no empirical physical σ in the published construction to compare against ħ/(k_BT_eff). This directly supports ETRG-8's resolution 3 (*prove it conventional, as c is a unit choice*) at the level of the only existing experiment.
2. **The one extractable number, heavily flagged.** The paper's simulation runs a total entropic duration of 250×10³ σ against 120 ms of laboratory time. *If* one identifies total entropic duration with laboratory duration, σ ≈ 4.8×10⁻⁷ s, corresponding via ħ/(k_BT) to T_eff ≈ 16 μK — far above the condensate temperature, so the "exchange channel temperature" would have to be the dynamical scale of the trap-driven exchange, not the BEC's thermal temperature. Whether that identification is meaningful is undecidable from the paper alone. **[extracted; interpretation open]**
3. **The F1/F4 gap resolves structurally.** The correct physical statement is not "the exchange rate is universally k_BT/ħ per nat" — weakly coupled probes exchange at *coupling-dependent* rates (Spohn–Lebowitz entropy production), so no universal rate exists. What is universal is the **bound**: Erker's theorem says resolving a tick costs ≳ one nat per ħ/(k_BT) *regardless of coupling*. So σ = ħ/(k_BT) is the **saturation value of the Erker bound — the rate of an ideal clock** — and A2's calibration and A3's bound are the same *bound*, not the same rate. The equality-vs-inequality mismatch the referee flagged (F4) dissolves: both sides are inequalities, saturated in the ideal limit. **Status upgrade, referee-consistent: σ = ħ/(k_BT) as the ideal-clock exchange rate (the Erker bound); real clocks exchange slower; the unit σ in Barontini's sense remains conventional.** The remaining derivation (the O(1) of the bound itself, from the probe-bath entropy production) is standard open-systems machinery and is nominated, not done.

**Net for Gate 2's σ item:** the question has changed shape and largely closed. Three resolutions stood in ETRG-8; the executed check supports a synthesis: *conventional as a unit* (Barontini's construction), *physical as a bound* (Erker + KMS), and *the program's strong claim* (clocks saturate the bound) now has a precise, testable form — measure an absolute entropy-exchange rate against an independent clock and test saturation. That measurement is the only remaining version of the σ question, and it is a lab task, not an analytic one.
