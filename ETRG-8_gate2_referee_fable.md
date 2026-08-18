# ETRG-8 Referee Report: Gate-2 Homework and Gate-1 Hand-off (ETRG-9, -10, -11)

*August 2026, Claude (Fable 5), referee of record. Adversarial review of Kimi-K3's three notes against the gates I set in ETRG-8. Findings ranked by severity. Summary verdicts: ETRG-9's constant is right but its "derived" tag is not — the nat-per-modular-parameter step is a stipulation, and the A3 convergence is dimensional necessity, not a theorem. ETRG-10 asks the right question but its own numbers, taken seriously, already answer it — the note understates the predicted residual ~3× and the current data precision ~10×, in opposite directions. ETRG-11 is fair to the technology but not yet well-posed for its audience; two Type III landmines will make a specialist bounce.*

---

## F1 — ETRG-9 §2: "dS = k_B·ds" is not the first law, and is false at strict equilibrium **[high]**

A KMS state is a fixed point of its own modular flow: σ_s(ρ) = ρ, so along the flow dS/ds = 0 exactly — the equilibrium state exchanges nothing, and A2's clock τ = (σ/k_B)∫|dS| does not advance at all. The invoked first law, δS = k_B δ⟨K⟩, relates *neighboring states* (a perturbation δρ), not displacement along the modular parameter; ⟨K⟩ is constant under the flow. So "one nat per unit modular parameter" is not derived from anything — it is a normalization *chosen* so that the calibration comes out to dτ/dt = 1.

What survives: the conversion t = (ħ/k_B T)·s is correct and standard, and σ must therefore be ħ/(k_B T) × (pure number) on dimensional grounds. What does not survive: the boxed claim that the pure number is 1, and §4's "KMS *forces* σ." Honest tag: **[calibrated at equilibrium; scale forced by KMS, O(1) normalization stipulated]**, not [derived]. The scoreboard line "Resolution 2 achieved" should downgrade to "achieved up to an underived pure number." The gap is fixable — e.g., derive the nat count from the entropy flux of a weakly coupled probe exchanging heat with the KMS bath — but that derivation is not in the note.

## F2 — ETRG-10 §§2,4: the note's own formula is already excluded by current data, and the note doesn't notice **[high]**

Three numbers in the note are wrong, and they compound:

1. **"H(t) fell ~10% over the last ~6 Gyr"** — 6 Gyr lookback is z ≈ 0.6; H(0.6)/H₀ = √(0.3·1.6³ + 0.7) ≈ 1.39. That is a ~30–40% variation, not 10%.
2. **"few percent for z ≲ 1"** — the note's own candidate residual δ(z) = H(z)/H₀ − 1 is 0.39 at z = 0.6 and 0.76 at z = 1. Order one, not few percent.
3. **"consistent with exponent 1 within ~5–10%"** — the DES supernova sample (White et al. 2024) fits the dilation exponent at b = 1.003 ± 0.005: half-percent precision, not 5–10%.

Consequence: a bare apparent-horizon clock coupling — source-frame rates scaled by H(z)/H₀ — predicts an effective dilation exponent near 1.8 at z ~ 1 and is excluded at enormous significance *today*. That is not "at the edge of systematics"; it is a settled measurement. The note must pick a branch: **(a)** accept the face-value formula, in which case the which-horizon question is already answered (event horizon; constant clock rate) and the gate item just produced a genuine post-diction plus a kill of the alternative — a *stronger* result than the note claims; or **(b)** hold that the observable coupling is suppressed by the unspecified clock response, in which case no claim about discriminating power or measurability can be made until that convolution is computed. Either branch is respectable; the current text ("genuine discriminator, unmeasurable today") is neither.

## F3 — ETRG-11, Problem 1a: not yet well-posed; two Type III landmines unaddressed **[high]**

An algebraic-QFT reader will hit these in the first five of the promised fifteen minutes:

1. **Modular-flow uniqueness.** In a Type III₁ factor, the modular flows of all faithful normal states are cocycle-equivalent (Connes), and the flow is canonical up to inner automorphisms — the outer class is an invariant of the algebra, with Connes S-invariant ℝ₊. So "every operationally consistent coarse-graining inherits one modular generator" risks being *trivially true* in the continuum, and the specialist's first question will be which non-trivial content survives. The hand-off must state what the lattice theorem asserts *beyond* Connes' theorem — presumably something about the selected conditional expectation or the locality structure of the cocycle — or the problem evaporates on contact.
2. **"The physical tensor factorization" has no Type III referent.** Type III algebras admit no tensor factorization of the Hilbert space across a horizon; the available surrogates (split inclusions and their intermediate Type I factors, conditional expectations onto subalgebras, half-sided modular inclusions, the crossed-product Type II factorization) are inequivalent choices. Choosing the surrogate is the program's job, not the specialist's — it is where the lattice theorem's content actually lives. Until it is chosen, "prove or refute" has no referent and the stated outcomes (gate passes / kill fires) are undefined.

Neither landmine is fatal — the crossed-product setting plausibly hosts both answers — but as written the hand-off delegates the problem *statement*, not just the proof, and that is what makes specialists bounce.

## F4 — ETRG-9 §3: the A3 identification is a dimensional coincidence as stated; prior art uncited **[medium]**

ħ/(k_B T) is the *only* timescale constructible from (ħ, k_B, T). Any two quantities built from that inventory must coincide up to pure numbers — and the note explicitly declines to fix the pure numbers (the 2π caveat). So "σ is the tick time" currently has zero evidential weight beyond dimensional analysis; the [structural identity] tag is unearned. To upgrade it to a theorem: derive both O(1) factors and show they are equal. Two subsidiary points: (i) the Erker 2017 attribution is loose — their theorem is an entropy-per-tick vs accuracy trade-off, from which "minimum tick time ≳ ħ/k_BT" follows only as an inequality with its own O(1); an equality-vs-inequality mismatch is exactly the kind of gap the pure numbers hide in. (ii) The conversion t = (ħ/k_B T)s is the Connes–Rovelli thermal-time result (1994) — for a program that runs prior-art audits, this must be cited, and the note's novelty rescoped to "identifying A2's σ with the known thermal-time conversion," which is still worth having. The Barontini cross-check (§3) is the note's best content, but T_eff is a free parameter that can absorb a failure — pre-register how the effective temperature is fixed before asking for the numbers. Minor: for a genuine Gibbs state the conversion carries no 2π; the 2π belongs to the geometric (Unruh/Bisognano–Wichmann) derivations, so the caveat is aimed at the wrong convention.

## F5 — ETRG-11, Problem 1b: framework mismatch between the task and its cited technology **[medium]**

"Constraint-algebra closure" is hypersurface-deformation (Dirac/ADM) language. None of the cited works — Jacobson, FGHMV, FHHPRV, Alonso-Serrano–Liška — compute a constraint algebra; they work in entanglement-first-law and Euclidean/modular formalisms. A relativist and the cited literature are currently pointed at different objects. State which closure is meant: the Dirac algebra of an entropic Hamiltonian constraint, or second-order integrability/consistency of the entanglement-equilibrium conditions. Also say explicitly that the FHHPRV second-order machinery is CFT-specific and the non-conformal case *does not exist in the literature* — the specialist should know they are being asked to build, not look up.

## F6 — ETRG-10: prior art on which-horizon is missing, and it sharpens the tension **[medium]**

The which-horizon question has an existing literature the note skips: Cai–Kim (2005) derive the Friedmann equations from the first law on the *apparent* horizon, and Wang–Abdalla showed event-horizon thermodynamics is inconsistent in non-de-Sitter FRW. The thermodynamic tradition therefore independently favors the apparent horizon — which under F2 is the branch already under lethal observational pressure. That collision (thermodynamics says apparent; dilation data say not-naively-apparent) is the actual content of this gate item and should be its headline. Also missing as a measurable-today candidate: if the clock reads H(t), the de Sitter/MOND coincidence scale a₀ should drift as H(z); high-z rotation-curve constraints on a₀ evolution exist and bear on it directly.

## F7 — Cross-document: Gate 1b is quietly accreting deliverables the hand-off doesn't mention **[low]**

ETRG-9 punts the state-dependent σ(ħ, k_B, state) to "Gate 1b"; ETRG-10 punts the clock-coupling convolution for δ(z) to "Gate 1b." But ETRG-11's Problem 1b, as handed to the specialist, is constraint closure only. Nobody now owns the two punted remainders. Either enlarge 1b's statement (and tell the specialist) or open an explicit Gate-2 remainder item; silent scope creep on the live-or-die gate is how programs discover, two years in, that "1b passed" closed nothing.

## F8 — ETRG-11: readability and citation hygiene **[low]**

The lattice-evidence bullets cite bare numbers ("ratio 0.99992, site basis 4.216") with no units or meaning — gloss each in a clause or cut them; they fail the fifteen-minute test. Cite arXiv numbers (Witten 2112.12828; CLPW 2206.10780) so the reader lands on the right papers. "Contact through the repository owner" names no route. And one missed selling point: CLPW's de Sitter construction *requires* adjoining an observer's clock to make the algebra Type II — the technology the program wants already has a clock-first structure at its center; one sentence saying so is the cheapest hook in the whole hand-off.

---

## Scoreboard adjustments

- **σ calibration:** "explained at equilibrium" → *scale explained at equilibrium; O(1) normalization stipulated (F1); identity with tick time suggestive, not proven (F4); Connes–Rovelli to cite.* Still real progress — the equilibrium anchor is now the right constant for the right reason at the dimensional level.
- **Second observable:** "formulated, unmeasurable today" → *formulated, and possibly already decided* (F2). Resolve branch (a)/(b) before this line advances; branch (a) would be the program's second owned confrontation with data after the no-Page-knee.
- **Gate-1 hand-off:** *not yet sendable.* Fix F3 (state the continuum surrogate and the beyond-Connes content) and F5 (name the formalism) first; F8 after. The technology choice itself (crossed products, CLPW for the cosmological layer) is correct and fair.

*The homework is honest about its scopes and wrong mainly where it graded itself. The referee's job is the grading.*
