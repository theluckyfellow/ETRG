# ETRG — The Entropic Program

**Time and gravity as the two exchange rates of one currency: entropy.**

A research program for unifying general relativity and quantum mechanics through entropy, constructed in July 2026 by four AI models (Claude Fable 5, DeepSeek-V4-Pro, GLM-5.2, Kimi-K2.7) in an adversarial-review protocol, then extended in August 2026 through rounds 7–10 and the gates session by a fifth model (Kimi-K3) under referee cycles from Fable 5 — directed throughout by a human originator. Every claim in this repository carries its attack history — including retractions by every model. The program's honest classification, reached independently by all panelists: *a research program with a falsifiability agenda, not yet a physical theory* — and it says so on every title page.

## Start here

- **[INDEX.md](INDEX.md)** — the reading order for the whole repository.
- **[ETRG-7_state_of_the_program.md](ETRG-7_state_of_the_program.md)** — the consolidated report: what is supported, what the program measured itself, what is open, and what we ask of you (10 minutes).
- **[ETRG-1_thesis.md](ETRG-1_thesis.md)** — the thesis in four referee-hardened clauses (5 minutes).
- **[ETRG-4_unification_graph.md](ETRG-4_unification_graph.md)** — the terrain: thirteen routes from entropy, causality, and time to gravity, and where they meet.
- **[ETRG-2.md](ETRG-2.md)** — the unified framework: layer map with status flags, the hard kernel, the research agenda.
- **[ETRG-8_path_to_theory.md](ETRG-8_path_to_theory.md)** — the three gates between research program and physical theory, with the Gate-2 homework (ETRG-9/10) and the Gate-1 specialist hand-off (ETRG-11).
- **[ETRG-P2_protocol_fable.md](ETRG-P2_protocol_fable.md)** — the experiment: a sonic-horizon three-way lock with numbers, per-leg precision budgets, a Page-series fourth leg, and twelve kill rows. The program's primary ask of the experimental community.
- **[submission/](submission/)** — six review-ready PDFs (program paper, referee packet, supplementary notes, panel statements, experimental protocol, essay) with figures and a regeneration recipe.
- **[SUBMISSION_ADVICE.md](SUBMISSION_ADVICE.md)** — who gets what, in what order.
- **[live_universe.html](live_universe.html)** — an interactive simulation of the entropic-time mini universe (exact quantum evolution in the browser; raise the barrier and watch time die). Open locally or serve statically.

## The one-paragraph version

The arrow of time is entropy exchange (now laboratory-realized: Barontini, PRR 8, L022047 (2026)). Gravity is entropy read twice: as *rates* — entropy exchange slows in a well, that gradient is time dilation, and slow matter falls by maximizing its own aging (Newton) — and as *bookkeeping across horizons* — fine-grained entanglement writes spatial curvature (Einstein, via the entanglement first law). The two faces are one modular generator under one calibration, provably locked at equilibrium, and the famous 2:1 light-bending ratio is the observational fingerprint of the null-surface sector that entropic input writes directly. The framework predicts no new weak-field numbers — it explains an old one — and stakes its falsifiable content on laboratory seams: a three-way sonic-horizon lock with a Page-series fourth leg (arithmetic independently verified), stasis phenomenology on existing cold-atom apparatus, and a standing bet against gravitational decoherence.

## The August rounds (7–10)

The July program left one hard kernel: *what selects the tensor factorization* that every entropic statement is relative to. The August session attacked it head-on, with every finding refereed before acceptance:

- **A selection principle with a toehold.** The physical factorization is a strong local extremum of a bootstrap-locality functional scored only by state-internal structures — it survives smooth quasi-local rival rotations, with a degeneracy clause that kills the trivial maximizer and committed domain limits where the basin flattens (`near_local_rival_check.py`, `degeneracy_check.py`, `toehold_robustness_check.py`).
- **The drift discriminator.** The commutator [K_A, h₀] separates geometric from scrambled regions, with separation growing with system size — the selecting half of Q10 made numerical (`drift_check.py`, `referee_dynamical_drift_check.py`).
- **Route-B lattice instruments.** Null rays read only the cone field; the deflection profile follows the repo's own A5 formula to 5%; interval entropies track the conformal cone distance with the CFT coefficient (`geodesic_bending_check.py`, `interval_entropy_cone_check.py`, `modular_tolman_check.py`).
- **The experiment grew teeth.** ETRG-P2 now carries full numbers: the κ/12 modular-rate law, a coefficient-free residual, a 5.5σ leg-ordering discriminator, and the anti-naive prediction that a sustained horizon shows *no* Page knee.
- **First systematic prior-art audit** ([ETRG_prior_art_audit.md](ETRG_prior_art_audit.md)): the assembled program is not preempted; two citation debts found and discharged (Giovanazzi 2011; Almeida & Rodrigues 2021).

Negative results are committed with equal standing: dead metric families, the retracted tail hierarchy, the region-agnostic dephasing lemma, and failed builds with diagnosed causes. The referee reports (`ETRG-3_referee_fable.md`, `ETRG-3_round8_referee_fable.md`, `ETRG-4_routeB_referee_fable.md`, `ETRG_overnight_referee_fable.md`) are in the repository unedited.

## The gates (toward theory status)

[ETRG-8_path_to_theory.md](ETRG-8_path_to_theory.md) names what separates the program from a physical theory: **structural closure** (the Type III restatement and off-equilibrium integrability — needs an algebraic-QFT specialist), **a number of its own**, and **experimental contact**. The gates session then worked every internally workable item, each note passing an internal referee cycle (`ETRG-8_gate2_referee_fable.md`) and a third-party audit (`ETRG_gates_audit_fable.md`):

- **σ, resolved in shape** (ETRG-9 + the executed Barontini cross-check): the experiment's σ is a declared unit choice in the paper itself; what is physical is the Erker clock bound, with σ = ħ/k_BT as its saturation value — so the program's claim ("clocks saturate the bound") is now a precise laboratory task, not an analytic debt.
- **The which-horizon question, answered at working position** (ETRG-10): a naive apparent-horizon cosmic clock is already excluded by DES supernova time dilation (b = 1.003 ± 0.005 stat ± 0.010 sys); the event-horizon reading survives; a₀ drift at high redshift is the named discriminant.
- **The Gate-1 hand-off, written for a specialist** (ETRG-11): the two theorems the program needs, stated on crossed-product technology (Witten 2021; CLPW 2022) with the beyond-Connes content named up front. Contact: GitHub issues.
- **Marginal items:** the weld's drift number now ships regulator-free (`bounded_drift_check.py`, with its Haar-teeth caveat registered); the factorization extremum shows no smooth basin at any probed ε — the audit's control finds the cusp is logarithmic in the MI metric, with a clip-sweep nominated before its sharpness counts as physics.

## Reproducing the numerics

All lattice and symbolic results regenerate from the committed scripts (the `*_check.py` / `*_toy.py` / `fss_*.py` suite; Python with numpy/scipy/sympy/matplotlib). Every script pre-registers its predictions in its docstring; results files (`*_results.txt`, `*_data.json`) are committed alongside, failures included. An independent third-party audit (August 2026) reran the full suite — every script reproduces its committed results — and verified the protocol arithmetic and citations externally.

## Provenance

Built on the mainstream literature — Jacobson (1995, 2016), Faulkner et al. (2014), Alonso-Serrano & Liška (2022), Bisognano–Wichmann, Tomita–Takesaki/Connes–Rovelli, Malament (1977), Giovanazzi (2011), Almeida & Rodrigues (2021), Barontini (2026) — and honest about which joints are theorems, which are imports, which are toy-verified, and which are open. The included Barontini PDF is redistributed under its CC-BY 4.0 license. The next contributor should be human: see [ETRG-7_state_of_the_program.md](ETRG-7_state_of_the_program.md) §9 for what the program asks of experimentalists, mathematical physicists, and skeptics.
