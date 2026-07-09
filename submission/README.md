# ETRG Submission Package

*July 2026. The review-ready outputs of the ETRG program. Each PDF opens with a provenance disclosure (AI-constructed, adversarially reviewed, human-directed); the accompanying repository preserves every claim's attack history.*

## The PDFs

| File | Contents | Send to |
|---|---|---|
| **ETRG_program_paper.pdf** | Thesis (v0.2) + the unified framework (ETRG-2) + figures | The main document — perspective/program submission (Foundations of Physics, GRG, SciPost Physics Core) |
| **ETRG_referee_packet.pdf** | The adversarial review packet: numbered claims, checkpoints, kill criteria | Circulate to physicists for attack — designed to be refuted |
| **ETRG_supplementary_notes.pdf** | The four technical notes with round-by-round adjudications | Supplementary material |
| **ETRG_panel_statements.pdf** | Four independent AI closing verdicts on the corpus | Supplementary material / provenance |
| **ETRG_experimental_protocol.pdf** | P1 and P2 specified with published apparatus numbers | The Birmingham / analogue-horizon approach — send with the program paper |
| **ETRG_essay.pdf** | The factor-of-two essay (~1,450 words) | Gravity Research Foundation / FQxI essay entries |

## Figures

`figures/` — publication figures generated from the committed simulation data by `../figures_submission.py`:
1. `fig1_deflection.png` — the factor of two as face-sampling
2. `fig2_toy_einstein.png` — lattice geometry curving under entanglement debt; the Rindler boost weight reproduced
3. `fig3_q10_lock.png` — the first-law lock is modular-basis-selective
4. `fig4_label_freeness.png` — the time label cannot leak into dynamics

## Rebuilding

```
python ../figures_submission.py
pandoc DOC.md -f markdown -t html5 --standalone --css=print.css -o DOC.html
chromium --headless --no-pdf-header-footer --print-to-pdf=DOC.pdf file://$PWD/DOC.html
```

*A visual overview lives at the project's Claude artifact (see repository notes). Before any journal submission: one sustained read by a human physicist — the panel's unanimous final recommendation.*
