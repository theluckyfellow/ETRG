# ETRG-5: The Stasis Cosmology — Black Hole Interiors as Born Causality

*August 2026, Kimi-K3, developing the originator's hypothesis (offered freely: "not required, but maybe true and maybe helpful"): assume we are inside a 4D black hole — and where the causality of the parent universe comes to a near stop, a new causality is born. Placed on the unification graph (ETRG-4): this is a Route-B/F-adjacent cosmology built from Route-A machinery. It is the most speculative document in this repository; it contains no theorems, and every load-bearing step is flagged. Its defense for inclusion: the kinematic skeleton of the hypothesis is already mathematics, and its entropic reading connects to three results this program already owns.*

---

## 1. The hypothesis, stated precisely

**H1.** Our universe is the interior of a black hole formed in a parent universe.
**H2.** At the horizon, the parent's causality comes to a near stop — the lapse degenerates.
**H3.** At that degeneracy, a new causality is born: the interior's cone structure, with its own time.

## 2. The kinematic skeleton is already mathematics

The interior of a Schwarzschild black hole **is** a cosmology — the Kantowski–Sachs anisotropic universe. For r < 2M,

$$ds^2 = -\Big(\frac{2M}{r}-1\Big)^{-1} dr^2 + \Big(\frac{2M}{r}-1\Big) dt^2 + r^2 d\Omega^2 ,$$

and the signs of the first two coefficients have flipped relative to the exterior: **r is timelike, t is spacelike.** The interior is a homogeneous anisotropic cosmos whose "time" is the parent's radial coordinate, born at r = 2M (the horizon) and ending at r = 0 (the singularity), with one direction expanding and the angular two contracting. The role exchange r ↔ t at the horizon *is* "a new causality born where the old one stops" — stated in coordinates rather than poetry. *(Overnight-referee precision: no invariant clock stops at the horizon — an infalling clock crosses in finite proper time; "the parent's clock comes to a near stop" is exterior coordinate-time language. What carries H2 in this framework is the A7 entropic-stasis reading of §3, not the Schwarzschild metric's coordinate behavior.)* Meanwhile the parent's exterior time dilation diverges at the horizon in coordinate slicing. H2 and H3, in Schwarzschild, are not conjectures; they are the metric. **[import: established GR]**

The part of H1–H3 that is *not* established: that the interior is habitable-by-observers, that anything like a long-lived cosmos fits between horizon and singularity (the Schwarzschild interior's total proper duration is ~πM — microseconds for stellar M), and that the singularity is avoidable (Popławski's torsion bounce **[import: ECSK gravity, speculative]**; Smolin's cosmological natural selection **[import: speculative]**). The entropic reading below exists to offer a different mechanism for the birth — not a bounce, but a *repartitioning*.

## 3. The entropic reading: stasis, then a new book

This program already owns three pieces that the hypothesis assembles:

1. **The horizon is a stasis point of the parent's entropic time (A7).** The entropic lapse diverges where entropy exchange stalls; duration information across a stasis is irrecoverable from inside — "the internal analogue of a horizon," in A7's exact words. H2 is A7 read cosmologically: the parent's entropic clock does not merely slow at the horizon; its bookkeeping *closes*. **[experiment-anchored at the stasis phenomenology level: Barontini; Demo 1]**
2. **The two entropy faces merge at the horizon (the lock).** At the stasis, coarse and fine bookkeeping coincide (Bisognano–Wichmann): the one place the parent's books balance exactly is the place they end. **[theorem at horizons]**
3. **A new causality is a new modular flow (Routes A/F).** In the entropic framework, a causality *is* a state on an algebra generating its flow (Tomita–Takesaki; Q10's selection). A new causality being born is therefore not a metric event but a **repartitioning event**: the interior sector's state on its own algebra, generating its own entropic time — a new book opening where the parent's book closed. The role exchange r ↔ t is the kinematic shadow of the new flow's generator being built from the parent's *radial* modular structure rather than its *temporal* one. **[conjecture — the assembly; each piece flagged separately]**

Read H1–H3 entropically and the mechanism needs no singularity traversal and no bounce: the birth happens *at the horizon*, in the bookkeeping, not through r = 0. The singularity becomes the interior cosmos's own eventual stasis — its heat death, not its parent's obstacle.

## 4. The de Sitter version: our own far future

If the parent is anything like de Sitter, the hypothesis gains a second reading aimed at *us*. Every comoving observer in a Λ > 0 universe has a cosmic horizon; the far future approaches that horizon's stasis as the tick budget (S_Λ = 3π/ΛG, B7) is spent. H2–H3 then say: **at the cosmic stasis, a new causality is born — the interior of the cosmic horizon** — and "we are in a 4D black hole" inverts into "our universe is what a born causality looks like from inside." The recasting table's last row ("heat death: the clock's budget spent; time ends as it began — entropically") becomes a birth announcement rather than an obituary. **[conjecture stacked on conjecture — flagged accordingly; B7's adjudicated status (necessity, not sufficiency) applies with full force]**

## 5. What would make it wrong

- **Stasis phenomenology fails** in Barontini-class systems (A7 dies; the entropic reading of H2 goes with it). This is the hypothesis's only near-term experimental exposure, and it is shared with the parent program.
- **Measured Λ ≤ 0** kills the de Sitter version (already excluded; the version stands).
- **A proof that no consistent modular structure exists for the interior sector** — e.g., that the interior algebra cannot support a state whose flow is geometric (the singularity's Type III pathologies are the named danger) — kills H3's entropic form.
- **Prior art proposing and refuting the assembly** (the standing repository criterion). Nearest neighbors: Popławski (bounce, different mechanism); Smolin (selection, different claim); AdS black-hole interior holography (different setting); **Almeida & Rodrigues 2021 (arXiv:2111.13575)** — the Schwarzschild/Kantowski–Sachs interior quantized with an entropic time correlated to cosmic time, with singularity removal in semiclassical analysis (adjacent: interior-as-cosmology with entropic time exists; different mechanism — covariant integral quantization, not stasis-and-repartitioning; found in the August 2026 prior-art audit, ETRG_prior_art_audit.md). None located that proposes the *stasis-and-repartitioning* mechanism.

## 6. What would make it useful (even if not true)

The hypothesis is offered "not required, but maybe helpful," and it earns its keep three ways: (i) it gives the program's stasis phenomenology a *cosmological* meaning — stasis points stop being edge cases and become the birth canal of sectors; (ii) it reframes the Λ budget conjecture (B7) from eschatology to genealogy; (iii) it nominates a class of lattice toys — degeneracy/pinch geometries — that the MI-geometry machinery can actually run (§7).

## 7. The nominated toy — outcome (`pinch_geometry_check.py`, exploratory)

Three chains (uniform / pinched hopping t(x) ∝ tanh²((x−x₀)/w) / hard cut), ground-state MI geometry:

- **(a) the pinch is real [PASS]:** the MI-metric bond length at the degeneracy is 32× the bulk median — the geometry closes its throat exactly where the cone collapses.
- **(b) two independent domains [PASS, and stronger than expected]:** cross-MI across the degeneracy is exactly zero, and the left/right mutual information vanishes entirely (0.000 vs 2.325 uniform, 0.612 for a hard cut) — the tanh² profile cuts a *wide* stasis moat, cleaner than a bond cut. Each side is a fully independent causal domain with a new edge. The "near stop" is illustrated; the two new domains exist.
- **(c) horizon modes [FAIL — expectation wrong]:** no new near-zero entanglement modes appear at the degeneracy (14 = 14 = 14). The frozen-mode count is set by the bulk dimer structure, not the pinch. The toy's "birth" clause is not illustrated: the new domains were always there as subsystems; nothing dynamical is born at the stasis in a static ground state. What the toy cannot say is whether a *quench* through a stasis (a time-dependent pinch) writes new modular structure — nominated, not run.

**Honest summary:** the stasis half of the hypothesis has a lattice image (pinch, moat, two domains); the birth half does not yet. A static lattice can show causality stopping; showing a new one *starting* needs dynamics.

---

*Status: exploration. Nothing here is a claim; the Schwarzschild-interior mathematics is established, the entropic assembly is conjecture, the de Sitter reading is conjecture squared. The originator's instruction stands: maybe true, maybe helpful, grind on.*
