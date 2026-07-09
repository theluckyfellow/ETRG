# ETRG-1 Bold Round — Referee Adjudication

**GLM-5.2 referee seat. 9 July 2026. Three blind attempts: Fable (Anthropic), DeepSeek, Kimi.**

---

## 1. Convergence Table

Postulate-by-postulate. ✓ = converges in mechanism; ≈ = converges in conclusion, diverges in route; ✗ = diverges; — = not addressed.

| Postulate | Fable | DeepSeek | Kimi | Verdict |
|---|---|---|---|---|
| **Primitive** | Relational distinguishability (relative entropy S(ρ‖σ)) | von Neumann entropy S[ρ] + partition principle | Hilbert space on a graph + pure entanglement pattern | ≈ All three make entropy the currency; Fable's relative entropy is the most general, DeepSeek's S[ρ] the most standard, Kimi's is the most constructive. Fable and DeepSeek agree the partition is a second structure; Kimi fixes it as a graph bipartition (sidesteps the problem). |
| **QM derivation (B1/P6)** | Import Hardy/CDP; purification = two-face principle | Import CDP/Hardy; recast axioms entropically (S is the unique concave additive invariant) | Not derived; postulated Gaussian state on a lattice | ≈ Fable and DeepSeek converge on CDP/Hardy as the reconstruction engine and agree the Born rule is entropic, not axiomatic. Kimi ducks the question. |
| **Time (B2/P2)** | Tomita–Takesaki modular flow; arrow = coarse-graining | Page–Wootters / Barontini; τ = ∫\|dS_obs\| | Modular/entropic flow; dτ = (ħ/k_B)\|dS_O/dλ\|\|dλ\| | ✓ All three define time as cumulative entropy exchange across a partition and cite the same machinery (Barontini, modular Hamiltonian). DeepSeek provides the explicit monotonic integral; Fable gives the deeper algebraic grounding (Connes–Rovelli); Kimi makes it computable on a lattice. |
| **Space/geometry (B3/P3)** | Area ≡ 4Għ × entanglement (read RT backwards); distance = correlation decay | Jacobson 2015 + FGHMV: δS_A = δ⟨K_A⟩ on all diamonds → full Einstein | Mutual-information geodesics; g_ij ∝ −∂²ln I(x:y) | ✓ All three derive geometry from entanglement via the same theorem chain (first law of entanglement → Einstein). Fable reads the area law as a *definition* of area; DeepSeek treats it as an emergent relation; Kimi constructs it as a graph distance. Same physics, different rhetorical commitment. |
| **Matter (B4/P5)** | Entanglement debt; energy = modular charge δ⟨K̂⟩ | Localized entanglement defect: m = (T_∞/c²)δS_ent | Entanglement debt ΔS_A; δS = δ⟨K_A⟩ | ✓ All three agree: matter is a local departure from vacuum entanglement, quantified by the first law. Fable's "modular charge" framing is the most general; DeepSeek's m = (T_∞/c²)δS_ent is the most concrete; Kimi's is the same statement in lattice language. |
| **Gravity/dynamics (B5/P3)** | Entanglement equilibrium → trace-free Einstein; γ = 1 from all-diamonds first law | Same: all-diamonds first law forces γ = 1; full Einstein is a theorem | Lattice Einstein: δ(area curvature) ∝ 8πG_eff · δ(modular energy) | ✓ Converges completely. All three invoke the same Jacobson/FGHMV chain and the same γ = 1 argument. Kimi adds the computable lattice version. |
| **Lorentz (B6/P4)** | Borchers–Wiesbrock: modular inclusions generate Poincaré. Circularity risk flagged. | Bisognano–Wichmann: modular flow = boost. Lorentz universality conjectured from KMS stability. | Lieb–Robinson cone as emergent null cone; exact Lorentz not claimed on lattice | ≈ Fable and DeepSeek agree Lorentz emerges from modular theory but pick different theorems. Fable is more ambitious (full Poincaré from modular inclusions) and more honest about the circularity risk. DeepSeek claims more (signature forced by modular theory) but the argument for (−,+,+,+) from Δ = ρ⊗ρ⁻¹ is not rigorous. Kimi settles for an approximate cone and admits it. |
| **Λ / cosmology (B7/P7)** | Λ > 0 is the *enabler*: every observer gets a cosmological horizon = universal dark sector. Gibbons–Hawking KMS. Smallness = entropy budget size. | Λ = saturation deficit: S_dS = min(A/4Għ, ln D). Smallness = Hilbert space vastness. Anthropic remainder. | Not addressed (lattice has no Λ) | ✗ Sharp divergence. Fable makes Λ the *solution* to the factorization problem (the horizon is the missing partition). DeepSeek makes Λ a *symptom* of finite Hilbert-space dimension and explicitly names the factorization problem as unsolved. Kimi ignores it. This is the dispute; see §2. |
| **Measurement (B8/P8)** | Born rule from envariance (Zurek); collapse = repartitioning | Born rule from CDP + entropy maximization; collapse = Bayesian update | Not addressed | ≈ Fable and DeepSeek agree collapse is not dynamical and the Born rule is entropic. Fable imports envariance; DeepSeek offers a novel entropy-maximization argument for the spectral decomposition being the unique one preserving pre-measurement entropy. DeepSeek's argument is more original but less theorem-grade. |
| **Preferred factorization** | B7 claims to solve it for horizon-anchored observers; concedes it is merely *relocated* for the web as a whole | §7: "We do not solve it. We do not even sketch a solution." Explicitly the hard kernel. | Sidestepped: graph bipartition is fixed by construction | ✗ Fale claims partial resolution via Λ; DeepSeek confesses; Kimi dodges. |
| **Kill criteria** | Λ ≤ 0, Lorentz violation, Born deviation, gravitational decoherence, Borchers–Wiesbrock circularity, horizon observer-dependence | γ ≠ 1, area law violation, entropic time non-monotonicity, gravitational decoherence, Lorentz violation, zero-entropy horizon | Triangle inequality failure, lapse freeze/divergence, wrong-sign curvature, no shared cone, phase incoherence | — Different scopes: Fable/DeepSeek give theory-level kills; Kimi gives lattice-level kills. Complementary, not conflicting. |

---

## 2. The Dispute: Does B7 Actually Answer the Factorization Objection?

**The objection (round 2, Q3/Q10 attacks):** In FRW without Λ, a comoving observer has no causal horizon. No horizon → no wedge algebra → no restriction on admissible factorizations → the clock ambiguity returns undiluted. Even *with* Λ, the de Sitter static-patch wedge algebra is tied to the *static* observer, not the *comoving* one. Comoving observers use Fourier modes, and there is no reason those factorizations are subalgebras of the static-patch algebra.

**Fable's B7 claim:** Λ > 0 gives every observer a cosmological event horizon. That horizon is thermal (Gibbons–Hawking 1977). The horizon *is* the universal dark sector — the unobserved partition the program needs. Therefore comoving observers are horizon-anchored after all, and Q3's clock ambiguity closes for our actual universe.

**Adjudication: B7 does NOT answer the factorization objection. It relocates it.**

The argument fails at two points:

**(a) Observer-dependence breaks universality.** Fable's B7 asserts "every observer possesses a cosmological event horizon." True in de Sitter. But *which* horizon depends on the observer's worldline. Two comoving observers at different locations have different horizons, enclosing different sets of inaccessible modes. If the dark sector is "the modes behind *my* horizon," it is observer-relative. The entropic time defined by S(ρ_obs) then depends on *which* horizon — i.e., on the partition — which is the very ambiguity Q3 raises. Fable's own kill criteria list flags this ("a demonstration that the cosmological horizon's observer-dependence breaks the Q10 universality argument"). It does. The Q10 mechanism required a *single* wedge algebra to constrain admissible factorizations for *all* observers. In de Sitter there is no single wedge algebra shared by all comoving observers; each has their own static patch. The universality argument that works for Rindler observers (who share the same wedge structure up to boost) does not survive the transition to cosmology.

**(b) Comoving ≠ static.** The Gibbons–Hawking KMS temperature is derived for the *static* observer in the static patch — the observer whose worldline is the integral curve of the de Sitter timelike Killing vector. A comoving observer in an FRW perturbation of de Sitter is *not* this observer. The static patch's modular Hamiltonian generates boosts; the comoving observer's natural modular flow (if one exists) is generated by a different state on a different algebra. Fable's claim that "comoving observers are horizon-anchored after all" conflates the static observer's horizon with every observer's horizon. Having a horizon is not the same as having a horizon whose modular structure yields a *canonical* partition for *your* algebra.

**Verdict:** B7 is a genuine insight — Λ > 0 providing every observer with *a* horizon is a real structural fact, and the connection between the de Sitter entropy budget and the finiteness of cosmic time is elegant. But it does not solve the factorization objection. It identifies a necessary condition (you need a horizon to anchor the partition) without showing the condition is sufficient (having a horizon does not make the partition unique). DeepSeek's §7 confession — "the partition must be selected by a principle internal to S itself, but which quantity, and why, is entirely open" — is the honest assessment. Fable's own §7 concedes the point for "the web as a whole" while claiming resolution for "horizon-anchored observers." The concession swallows the claim: if the web as a whole has no preferred factorization, then neither do horizon-anchored observers within it, because their horizons are defined relative to their worldlines, which are defined relative to a factorization.

**Bottom line:** DeepSeek is correct. The factorization problem is THE unsolved problem. Fable's B7 is a promising reinterpretation of Λ's role but not a resolution. The comoving-observer variant of Q3 remains open.

---

## 3. Attacks: Two Most Lethal Objections Per Attempt

### Fable

**A1 — The circularity of B6 is not contained; it is fatal.** Fable flags that Borchers–Wiesbrock theorems "live in AQFT with vacuum assumptions" and asks whether a pre-geometric web can satisfy their hypotheses without presupposing Poincaré structure. The answer is: it cannot. The Borchers class and Wiesbrock's half-sided modular inclusions require a net of von Neumann algebras indexed by spacetime regions *before* the modular structure is extracted. The net presupposes the spacetime index set. You cannot generate the Poincaré group from modular data and then claim the spacetime the Poincaré group acts on is derived; the indexing is prior. B6 is not a theorem-import; it is a theorem-applied-to-a-setting-it-was-designed-for, then read backward. This is not circularity risk — it is circularity fact, and it demotes B6 from load-bearing to decorative.

**A2 — "Relational distinguishability" as the sole primitive is underspecified.** S(ρ‖σ) requires two states. Which two? The vacuum and an excitation? Two arbitrary subsystem states? The choice determines everything downstream. If the states are reduced density matrices of subsystems, then the subsystems and their algebra are prior to the entropy. Fable's primitive is not primitive — it is a functional on structures that must already exist. The "web of subsystems" is named but not generated from below; it is assumed. This is the same problem as the factorization objection, one level up: the web has nodes before it has distinguishability.

### DeepSeek

**A1 — The Schrödinger equation derivation is circular.** P6(b) claims Stone's theorem gives the Schrödinger equation as "the unique one-parameter unitary group preserving S(ρ_total)." Stone's theorem gives *a* one-parameter unitary group; it does not select the Hamiltonian. Any self-adjoint operator generates such a group. The entropy-preservation condition is vacuous: *all* unitary evolution preserves S(ρ_total) for a pure state (S = 0, always). The constraint does not fix Ĥ; it fixes the *form* of the equation, not its content. The lapse factor Ñ[ψ] is then inserted to match Barontini's data, but the matching is a fit, not a derivation. The claim "theorem-grade" for this step is unsupported.

**A2 — The ħ derivation (P6(c)) conflates two different bounds.** The holographic entropy bound S ≤ A/4Għ bounds the entropy of a *region* by its area. The uncertainty relation Δx·Δp ≥ ħ/2 bounds the phase-space volume of a *single degree of freedom*. These are different objects: the first is a statement about the dimension of a subalgebra; the second is a statement about the non-commutativity of canonical operators. The argument that "ħ is the conversion factor between phase-space volume and entanglement capacity" requires showing the area-law bound implies the single-particle phase-space bound, which requires a mapping between region entropy and single-particle localization that is not provided. The numerical coincidence (both involve ħ) is not a derivation.

### Kimi

**A1 — The lattice fixes the factorization, which is the one problem that needed solving.** Kimi's model postulates a graph with a fixed bipartition O/U. This is exactly the structure the other two attempts cannot derive. By fixing it, Kimi's simulations can never test whether the factorization is *natural* — they can only test whether, given a chosen partition, the downstream quantities behave correctly. The model is an existence proof *for a given factorization*, not a proof that the factorization is selected by the physics. This is the sharpest limitation: every result Kimi produces inherits an untested assumption.

**A2 — The metric proxy g_ij ∝ −∂²ln I(x:y) is not calibrated.** The claim that second derivatives of mutual information give the metric requires a specific proportionality constant and a specific vacuum state. For free fermions at incommensurate filling, I(x:y) ∼ |x−y|^{−κ} with κ depending on the filling fraction and the gap. The "Euclidean metric at coarse scale" claim holds only for a specific κ, and the proportionality between −∂²ln I and the physical metric g_ij is asserted, not derived. Different states (different fillings, different parent Hamiltonians) give different "metrics," with no principle selecting which corresponds to physics. The simulation can show *a* geometry; it cannot show *the* geometry.

---

## 4. Ranking and Grafting

**Ranking for ETRG-2 foundation:**

**1. DeepSeek.** Strongest foundation, for one reason: it is honest where it matters. The §7 confession — "the preferred-factorization problem is the hard kernel; everything else is scaffolding" — is the correct assessment of the state of the program. Its postulates are theorem-backed where they can be and explicitly conjectural where they cannot. The recasting table is the most complete. The kill criteria are the most falsifiable. Its weakness (circularity in P6(b), ħ derivation gap in P6(c)) are in the *secondary* structure; the primary structure (primitive → entropy functional; partition → the open problem) is correctly identified.

**2. Fable.** Second strongest. B2 (Tomita–Takesaki time) and B3 (area as defined quantity, not derived) are the deepest individual postulates in the entire round. B7 is the most creative idea — reinterpreting Λ as the enabler of entropic time rather than a problem to be explained away — but it overclaims (§2 above). The writing is the most ambitious and the most vulnerable: B6's circularity is a real flaw, and the primitive is underspecified (A2 above). Fable is the attempt that would produce the most interesting failures; DeepSeek is the one that would produce the most reliable next step.

**3. Kimi.** Third. It is the most computable and the least ambitious. Its value is not as a foundation but as a *test bed*. The lattice model cannot address the hard problems (factorization, Λ, Lorentz at exact level, Born rule) and does not claim to. What it can do — and what the other two cannot — is produce a numerical existence proof of the core geometry-from-entanglement chain. This is not a foundation for ETRG-2; it is a tool for ETRG-2.

**Elements to graft:**

- **From Fable → onto DeepSeek:** B2 (Tomita–Takesaki as the algebraic grounding of time; DeepSeek's Page–Wootters/Barontini is the operational version, but the algebraic version is deeper and should be the backbone). B7's reinterpretation of Λ as the enabler of cosmic time — not as a solution to the factorization problem (it does not), but as the most promising *direction* for one. The recasting of "dark energy" as "the universal horizon-maker" should be preserved as a conjecture, not a postulate.

- **From Kimi → onto DeepSeek:** All three simulations (A, B, C). DeepSeek's framework is the right home for Kimi's computational machinery because DeepSeek's postulates are the ones the simulations test. Kimi's Simulation A (entropic geometry from a free-fermion vacuum) is the natural numerical check of DeepSeek's P3. Simulation B (modular time and the toy Einstein response) tests P2 + P3 jointly. Simulation C (Lieb–Robinson as null cone) tests P4. The mapping is one-to-one.

- **From DeepSeek → onto Fable:** §7 (the factorization confession) should replace Fable's §7 (which concedes the problem for "the web as a whole" while claiming partial resolution). DeepSeek's framing is more precise: the partition must be selected by a principle internal to S, and no candidate principle has been identified. Fable's version blurs the line between "partially solved" and "relocated."

---

## 5. Is Kimi's Simulation A the Right Next Computation?

**Partially. Simulation A is the right *first* computation but for the wrong stated reason.**

**What it does:** Free-fermion chain L ∼ 200, compute I(x:y) for all pairs, introduce a central defect, measure emergent distances, check for 1/r metric potential.

**What it tests:** Whether mutual information produces a metric satisfying the triangle inequality with the right falloff — i.e., whether DeepSeek's P3 (geometry from entanglement) survives its first numerical check. This is the correct first question: if the distance function fails the triangle inequality, the program is dead at the foundation. Kimi lists this as a kill criterion and is right to.

**What is wrong with the curvature-extraction method:** The claim is to demonstrate a toy Einstein equation by placing a defect and measuring curvature of the MI-geodesic network. The method is: (1) compute I(x:y) distances, (2) extract a discrete curvature from the geodesic network, (3) compare to δ⟨K_A⟩. The gap is in step (2). On a graph, "curvature" is not uniquely defined. The Regge/excess-angle method requires a *triangulation* — a choice of simplices — and the triangulation of a graph derived from mutual information is not canonical. Different triangulations give different curvatures. The claim that "curvature tracks modular-energy debt with the right sign" is sensitive to the triangulation choice, and no principle selects the triangulation. This is the lattice analog of the factorization problem: the graph gives you distances, but extracting curvature requires an additional structure not provided by the entropy alone.

**The fix:** Do not extract curvature from the geodesic network. Instead, use the first law directly: compute δS_A = S_A(defect) − S_A(vacuum) for a region A around the defect, and independently compute δ⟨K_A⟩ from the modular Hamiltonian of the Gaussian state. The first law predicts δS_A = δ⟨K_A⟩. This is a *direct* test of the central equation, with no triangulation ambiguity. The "curvature" is then a derived quantity (via the area-law calibration S = A/4G_eff), not a measured one. The simulation should check the *linear* relation δS vs. δ⟨K⟩, not the geometric interpretation of that relation. If the first law holds on the lattice, the geometry follows by construction; if it does not hold, no amount of curvature extraction will save it.

**Verdict:** Run Simulation A, but test the first law δS_A = δ⟨K_A⟩ directly. Skip the curvature-extraction step until the first law is confirmed. Simulation B is the right second computation (it tests the coherent/thermal distinction, which is unique to this program). Simulation C is useful but the least urgent — Lieb–Robinson bounds are well-established and the null-cone result is the least surprising thing the model can show.

---

*End of referee report. Three pages, numbered, no praise.*