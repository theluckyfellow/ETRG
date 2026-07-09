# First-Pass Convergence Report

**Comparing the three blind constructive-challenge responses (DeepSeek-V4-Pro, GLM-5.2, Kimi-K2.7) against ETRG-0's S-claims.**
*July 2026. Companion to ETRG-0_referee_packet.md §"The constructive challenge."*

## What was asked and what came back

All three models were given the referee packet and responded to the constructive challenge: build your own entropic theory of time and gravity from Barontini's construction, passing the Newtonian, factor-of-two, interferometry, and one-null-cone gates. None of the three attacked the Q-checkpoints or the E-claims in this pass; all three built. That work remains open for later rounds.

## Convergence table

| Structural element | DeepSeek | GLM | Kimi | ETRG-0 |
|---|---|---|---|---|
| Bright/dark partition of a Ĥ\|Ψ⟩=0 universe | ✓ | ✓ | ✓ | A1–A2 |
| Time = entropy exchange across the partition | ✓ | ✓ | ✓ | A2 |
| g₀₀ / Newton from the temporal sector alone | ✓ | ✓ | ✓ | A4 |
| Spatial sector required for the factor of two | ✓ | ✓ | ✓ | A5 |
| Deflection law (1 + v²/c²) recovered explicitly | asserted | asserted | **derived** | A5 |
| Mechanism that locks the two sectors at equal strength | none (asserted) | none (asserted) | none (assumed, flagged) | S3 (asserted via shared modular generator) |

## Per-model verdicts

**DeepSeek** — identifies the geometric sector with the bright sector and Planck-scale microstates with the dark. The factor of two rests on the claim that for null particles "the separation between the global phase Ξ and the geometric Hamiltonian breaks down," so the pump couples to both sectors. This is asserted, not derived: nothing in the construction computes the relative weight of the two couplings, so the 2 could as well be 1.7. Referee-fatal as it stands.

**GLM** — same architecture; proposes the lock follows from conservation of total entropy: "any temporal gradient in the observed sector's entropy must be exactly balanced by a spatial gradient in the dark sector's entropy," hence 1 + 1 = 2. As stated this is a non-sequitur: S_obs + S_dark = const constrains the *sum of entropy changes*, not the ratio of *metric-sector amplitudes*, and no map from entropy gradients to g₀₀ vs g_ij amplitudes is given. The most confident-sounding and least defensible of the three passes.

**Kimi** — the most honest and most technically complete. Writes the isotropic weak-field metric with a single potential Ψ in both sectors *by assumption*, then correctly derives κ⟂(v) = −(1 + v²/c²)∇⟂Φ_N, giving Newton at v = 0 and the doubled deflection at v = c. Explicitly concedes in its caveat: "The factor of 2 is obtained because I assumed the temporal and spatial entropy gradients are equal — an assumption that is motivated by, but not proven by, the bipartite structure." Also proposes a genuinely new experimental idea: a second "spatial-clock" bright sector in a Barontini-class apparatus to emulate the (1 + v²/c²) interpolation — worth folding into the P-claims as a cheaper cousin of P2.

## The shared hole, and what it means

In the packet's outcome taxonomy this is **outcome (i), partial**: independent convergence on the ETRG-0 architecture — every model reinvented the bright/dark split, entropic time, a temporal sector for Newton, and a spatial sector for the factor of two — but *no model derived the lock*, and none produced either a competing mechanism (outcome ii) or an impossibility argument (outcome iii). The convergence is evidence the assembly is natural; the universal failure at the same joint is evidence that the lock is the actual scientific content of the hypothesis. Everything else is architecture.

That diagnosis motivated **ETRG-0_lock_note.md**, which attempts the missing derivation: the entropic input is natively a null-sector law; imposing it for all null directions forces γ = 1 and Newton's normalization jointly in the static weak field; and the temporal and spatial sectors are the thermality and variational faces of one boost/modular generator under one calibration constant.

## Salvage list (items worth keeping from the passes)

1. Kimi's explicit κ⟂(v) derivation — adopt as the packet's standard presentation of E8's equation of motion.
2. Kimi's "spatial-clock sector" cold-atom analogue — candidate P-claim (cheaper sibling of P2).
3. GLM's framing of mass as a local "entropy sink" — evocative but currently contentless; keep only if a future draft gives it an equation.
4. DeepSeek's observation that corrections to GR should appear "where ∂_τΓ is large" (fast entropy-flow transients) — a possible P-claim seed if it can be quantified.
