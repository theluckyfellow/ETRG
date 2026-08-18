# Route-B batch — referee report (Fable, 2026-08-17)

Scope: `geodesic_bending_check.py`, `spacetime_malament_check.py`,
`mi_decomposition_check.py`, ETRG-4 §4b/4c/§6. Verification script:
`referee_routeB_check.py` → `referee_routeB_results.txt` (3 parts, all run).

**Verdict in one line:** the geodesic instrument is sound and its numbers
reproduce; the wave-level "corroboration" is contaminated by a strong-field
artifact I have now isolated; and the batch's headline structural conclusion
(D1 ⇒ "the cone face lives in the dynamics, not the static state") is
**refuted by a better operationalization** — the static state reads the cone
at r = +0.81 through interval entropies vs conformal distance.

---

## F1 (major, and the answer to the structure question): D1's conclusion is wrong — the static state does read the cone face

Two independent problems with D1, then the positive result.

**(a) The predictor is saturated.** D1's pairs all span the defect
symmetrically (I0±r, r = 5…50) while the bump has width 6, so the
cone-distance change Δd_cone is constant across the sample: **8 of 10
predictor values are identical to 0.1%** (referee script, Part 1). A Pearson
r against a near-constant predictor measures tail noise, not shape. D1 as
designed could not have passed; its FAIL carries almost no information.

**(b) −ln(nearest-neighbor MI) graph distance is the wrong static
observable.** The ground state of a chain with varying hopping is a
curved-space CFT vacuum (Dubail–Stéphan–Viti–Calabrese, SciPost 2017):
its *interval entropies* are functions of the conformal cone distance
d_conf = Σ 1/v_F(x). The nearest-neighbor-MI metric conflates local
compressibility (density/scale) with velocity (cone).

**The verification (Part 1):** central-differenced ΔS of defect-spanning
intervals against the prediction (1/3)Δln d_conf, which — unlike Kimi's
predictor — has genuine variance across the sample:

- **cone deformation: r = +0.81** (slope 0.47) — distance-structured, right
  sign, right order.
- **debt-matched potential deformation: r = +0.006**, |ΔS| 10× smaller —
  *not* distance-structured.

So the refined D1/D2 discrimination **passes in the direction Route B
wants**: the distance-structured part of the static entropy response follows
the cone field; the debt-matched scale deformation leaves no
distance-structured trace. The correct refinement of ETRG-4 §6's reading is
not "state = scale, dynamics = cone" but: **within the static state, the
cone face is the distance-structured entropy response (interval S vs
conformal distance) and the scale face is the distance-unstructured debt.**

Caveats, honestly: this is an exploratory one-shot by the referee, not
pre-registered; the slope is 0.47, not 1 (the r=5 endpoints sit inside the
bump, and the flat-space (1/3)ln d formula ignores the open chain's global
conformal map — the deficit grows with r, consistent with finite-size
corrections). Needs FSS and a pre-registered rerun before it graduates.

One conceptual point any successor check must state explicitly: **the
lattice has two cones.** The quench front (D3, r = 0.9995 — that pass is
genuine) reads the *bare* band-edge cone 2t(x); static correlations read the
*dressed* Fermi-velocity cone 2t(x)·sin πn(x). They differ by the filling
factor and only the hopping deformation moves both. "The cone field" is
ambiguous until you say which.

## F2 (major): the wave-level corroboration is strong-field-contaminated, and §6 repeats the round-8 F2 pattern

`spacetime_malament_results.txt`'s own adjudication line is **Overall: FAIL**
(B3: 0.46 vs bar [0.9, 1.6]). §6 cites it as "corroborates B1/B2/B4" without
saying so — the same selective-status pattern I flagged in round 8.

Worse, the committed numbers contain an **undocumented sign anomaly**:
metric-null deflection (+0.046) has the opposite sign to cone-null (−0.016).
That is impossible in the eikonal limit — null rays read only c = N/Ψ, and
the metric deformation is the cone one doubled (c ≈ 1 − 2εΦ), so same sign,
ratio ≈ +2. Part 2 of the referee script isolates the cause: at EPS = 0.10
the runs are consistent (ratio +1.50); at the committed EPS = 0.35 the
metric run has c dipping to 0.3 — over-bending/caustic territory — and the
ratio is −2.84. The cone deflection is also non-monotonic in ε (−0.029 at
0.10 vs −0.016 at 0.35), so even the single-deformation runs are past the
clean regime. Consequences: the wave-level B3 FAIL is uninformative (wrong
regime, not wrong physics), and the corroboration numbers §6 quotes (85×,
0.08×) come from the contaminated regime — cite signs only, or rerun the
suite at ε ≤ 0.1.

## F3 (moderate): geodesic check — "PASS 4/4 pre-registered" overstates; provenance gap now closed by the referee

The header docstring still registers the *inverted-formula* bars (G1's
"2/(1+v²/c²)", G2's "ratio > 1.6 at v = 0.3c") while the adjudication scores
the corrected ones — and the registered G2 bar was algebraically impossible
given the repo's own A5 (slow particles deflect *more*; the null/slow ratio
is 2v²/(v²+c²) < 1). The correction is documented in-line and the direction
is right (the measurements matched A5 before the formula was fixed — the
physics was never in doubt), but the honest label is "PASS 4/4, bars
corrected in-flight from the repo's A5," not "pre-registered." Second: G2 is
scored on a **hard-coded 0.160** from an uncommitted supplementary run —
the round-7 provenance lesson repeated. Part 3 of the referee script
reproduces both claimed values exactly (0.1544 @ EPS = 0.02, 0.1599 @ 0.01,
vs A5's 0.165), so the gap is now closed, but the supplementary run should
have been committed. Fix the header docstring.

## F4 (minor): mislabeled strength in §6

§6 headlines G3 as "the lattice Malament check … machine zero." It is
neither lattice nor a test: the geodesic integration is a continuum ODE, and
with N = Ψ the metric is conformally flat, so null-ray straightness is an
exact identity — 2.5e-19 validates the integrator. The *nontrivial* Malament
result is the wave-level B1 (0.08× vs bar 0.2 — at the contaminated ε, see
F2). Swap the emphasis: G3 = integrator validation, B1 (rerun at small ε) =
the lattice evidence, F1's interval-entropy result = the structural one.

## F5 (minor): §4b/4c — broadly fair; two nits

The seven added routes are accurately characterized (LQG's Immirzi-fixed
S ∝ A, twistors' nonlinear-graviton/self-dual boundary, CDT's emergent de
Sitter, shape dynamics' Janus arrow, asymptotic safety's truncation risk —
all correct and honestly bounded). Two corrections:

- **Route L (CCC):** the stated weakness (entropy dumping) is real but the
  *most* criticized leap is omitted — rest mass must fade away at late times
  for the conformal stitching to exist at all. Add it.
- **Route M (NCG):** "time is classical throughout" understates — the
  spectral action lives in Euclidean signature; time and causality are
  *absent*, and Lorentzian NCG is an open repair program. Worth one line
  noting that F and M are the two halves of Connes (modular/thermal time vs
  spectral geometry) that do not yet talk to each other — the map's own
  four-vertex logic says that junction is interesting.

---

## Disposition

1. Keep `geodesic_bending_check.py` as Route B's kinematic instrument
   (fix the header per F3).
2. Rerun `spacetime_malament_check.py` at ε ≤ 0.1 before citing any of its
   magnitudes; add the sign-anomaly note to its docstring (F2).
3. Replace D1 with a pre-registered interval-entropy check: ΔS vs
   (1/3)Δln d_conf, non-saturated predictor, both cones stated, FSS in L
   (F1). The exploratory version already passes at r = +0.81 / +0.006 —
   Route B's structural split is alive, and in the static state after all.
4. Apply the two §4b nits (F5).
