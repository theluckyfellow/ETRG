# ETRG — The Entropic Program

**Time and gravity as the two exchange rates of one currency: entropy.**

A research program for unifying general relativity and quantum mechanics through entropy, constructed in July 2026 by four AI models (Claude Fable 5, DeepSeek-V4-Pro, GLM-5.2, Kimi-K2.7) in an adversarial-review protocol, directed by a human originator. Every claim in this repository carries its attack history — including retractions by all four models. The program's honest classification, reached independently by all four panelists: *a research program with a falsifiability agenda, not yet a physical theory* — and it says so on every title page.

## Start here

- **[INDEX.md](INDEX.md)** — the reading order for the whole repository.
- **[ETRG-1_thesis.md](ETRG-1_thesis.md)** — the thesis in four referee-hardened clauses (5 minutes).
- **[ETRG-2.md](ETRG-2.md)** — the unified framework: layer map with status flags, the hard kernel, the research agenda.
- **[submission/](submission/)** — six review-ready PDFs (program paper, referee packet, supplementary notes, panel statements, experimental protocol, essay) with figures and a regeneration recipe.
- **[SUBMISSION_ADVICE.md](SUBMISSION_ADVICE.md)** — who gets what, in what order.
- **[live_universe.html](live_universe.html)** — an interactive simulation of the entropic-time mini universe (exact quantum evolution in the browser; raise the barrier and watch time die). Open locally or serve statically.

## The one-paragraph version

The arrow of time is entropy exchange (now laboratory-realized: Barontini, PRR 8, L022047 (2026)). Gravity is entropy read twice: as *rates* — entropy exchange slows in a well, that gradient is time dilation, and slow matter falls by maximizing its own aging (Newton) — and as *bookkeeping across horizons* — fine-grained entanglement writes spatial curvature (Einstein, via the entanglement first law). The two faces are one modular generator under one calibration, provably locked at equilibrium, and the famous 2:1 light-bending ratio is the observational fingerprint of the null-surface sector that entropic input writes directly. The framework predicts no new weak-field numbers — it explains an old one — and stakes its falsifiable content on laboratory seams: a three-way sonic-horizon lock, stasis phenomenology on existing cold-atom apparatus, and a standing bet against gravitational decoherence.

## Reproducing the numerics

All lattice results regenerate from the committed scripts (`lock_check.py`, `q10_lattice_check.py`, `coherent_thermal_check.py`, `label_freeness_toy.py`, `toy_einstein.py`, `fss_q10.py`; Python with numpy/scipy/sympy/matplotlib). Results files (`*_results.txt`, `*_data.json`) are committed alongside.

## Provenance

Built on the mainstream literature — Jacobson (1995, 2016), Faulkner et al. (2014), Alonso-Serrano & Liška (2022), Bisognano–Wichmann, Tomita–Takesaki/Connes–Rovelli, Barontini (2026) — and honest about which joints are theorems, which are imports, which are toy-verified, and which are open. The included Barontini PDF is redistributed under its CC-BY 4.0 license. The next contributor should be human: see the research agenda in [ETRG-2.md](ETRG-2.md) §5.
