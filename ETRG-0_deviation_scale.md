I've read the relevant documents. Let me work through both questions carefully.

---

# ETRG-0: Dimensional Correction for Finding 3 & Coherent-State Lock Evasion

**Avis —2026-07-09**

---

## (1) Dimensional check and corrected scaling law

Finding 3 in `ETRG-0_lock_attacks.md` estimated the L5 lock-violation fraction as ΔE·ℓ²/A. This expression **is not dimensionless**. In SI, ΔE has units [ML²T⁻²], ℓ² is [L²], and A is [L²], yielding [ML²T⁻²] — an energy, not a pure number. In natural units (ħ = c = 1) the expression reduces to ΔE·ℓ²_P/A, which has units [L⁻¹] · [L²] / [L²] = [L⁻¹], still not dimensionless. The estimate is missing a factor of 1/(ħc) and a length scale; it implicitly confuses energy × Planck-area with a fractional mismatch.

### The correct dimensionless invariant

The natural dimensionless measure of how far a state ρ (of excitation energy ΔE, spatial extent R, near a horizon of area A) departs from vacuum is the **fraction of Bekenstein–Hawking entropy replaced by relative entropy**:

$$\boxed{\delta_{\mathrm{lock}} \;\equiv\; \frac{S(\rho\,\|\,\rho_{\mathrm{vac}})}{S_{\mathrm{BH}}},\qquad S_{\mathrm{BH}} = \frac{A}{4\ell_P^2}}$$

where ℓ²_P = Għ/c³.  S(ρ‖ρ_vac) is the quantum relative entropy, dimensionless and guaranteed non-negative by Klein's inequality. δ_lock = 0 exactly for ρ = ρ_vac and δ_lock > 0 otherwise, capturing the fractional degradation of the modular-generator calibration.

### Bounding the deviation

Casini's sharpened form of the Bekenstein bound (Casini 2008, arXiv:0804.2182) states:

$$S(\rho\,\|\,\rho_{\mathrm{vac}}) \;\le\; \frac{2\pi R\,\Delta E}{\hbar c}$$

where R is the radius of the smallest ball containing the excitation's support. This is the *quantum* Bekenstein bound — it bounds the relative entropy directly, not the entropy difference, and is theorem-grade in QFT.

Inserting into δ_lock:

$$\delta_{\mathrm{lock}} \;\le\; \frac{2\pi R\,\Delta E}{\hbar c} \cdot \frac{4\ell_P^2}{A} \;=\; \frac{8\pi\,\ell_P^2\,R\,\Delta E}{\hbar c\,A}$$

In natural units (ħ = c = 1, ℓ²_P = G):

$$\delta_{\mathrm{lock}} \;\le\; \frac{8\pi G\,R\,\Delta E}{A}.$$

For a spherical horizon where A = 4πR², this simplifies to the **corrected scaling law**:

$$\boxed{\delta_{\mathrm{lock}} \;\le\; \frac{2G\,\Delta E}{c^4 R} \quad(\text{SI}),\qquad \delta_{\mathrm{lock}} \;\le\; \frac{2\ell_P^2\,\Delta E}{R} \quad(\hbar=c=1)}$$

The dimensional defect in the original finding is repaired: the factor ℓ²/A is replaced by ℓ²_P/(RA) → G/R in natural units, restoring dimensionless proportionality. For macroscopic horizons (R≫ ℓ_P) the lock is exponentially robust; at R ∼ 10² ℓ_P with ΔE ∼ E_Planck the mismatch is O(1).

### Summary table

| Finding 3 (incorrect) | Corrected |
|---|---|
| ΔE·ℓ²/A ( ≠ dimensionless) | S(ρ‖ρ_vac)/S_BH ≤ 8πℓ²_P R ΔE/(ħcA) |
| Missing ħ, c, length scale | Bound via Casini, explicit G/R factor |
| Reference: heuristic E_vac ∼ A/ℓ² | Reference: Casini (2008), FGHMV (2014) |

---

## (2) Coherent-state lock evasion

Consider a coherent state |γ⟩ = D(γ)|0⟩ of a free scalar field, where D(γ) is the Weyl displacement operator. The reduced density matrix on a Rindler wedge is a Gaussian perturbation of the thermal vacuum ρ_vac (Bisognano–Wichmann). The key result: **relative entropy vanishes at linear order in the displacement**.

### Proof sketch (general argument, one line)

For ρ(ε) = ρ_vac + ε δρ with Tr[δρ] = 0, expand:

$$S\big(\rho(\varepsilon)\,\|\,\rho_{\mathrm{vac}}\big) \;=\; \varepsilon\,\mathrm{Tr}\big[\delta\rho\ln\rho_{\mathrm{vac}}\big] + \varepsilon\,\mathrm{Tr}\big[\delta\rho\big] + \mathcal{O}(\varepsilon^2) - \varepsilon\,\mathrm{Tr}\big[\delta\rho\ln\rho_{\mathrm{vac}}\big] \;=\;0\cdot\varepsilon + \mathcal{O}(\varepsilon^2),$$

where the cancellation follows because ρ_vac = e^{−K}/Z and the linear term is Tr[δρ K] − Tr[δρ] = 0 for any traceless perturbation (the first law of entanglement is exactly the statement that the linear term in S(ρ_vac + ε δρ ‖ ρ_vac) vanishes — it is δS − δ⟨K⟩ = 0, which is E7's content). For a coherent displacement the density-matrix perturbation δρ enters at O(|γ|), so the relative entropy scales as O(|γ|²).

### Explicit result for a coherent state

For a Gaussian coherent state with phase-space displacement vector **d**, the relative entropy to vacuum on the wedge reduces to (using the Gaussian-state relative-entropy formula, e.g. Šafránek & Fuentes 2016):

$$S(\rho_{\mathrm{coh}}\,\|\,\rho_{\mathrm{vac}}) \;=\; \frac{1}{2}\,\mathbf{d}^T V_{\mathrm{vac}}^{-1}\,\mathbf{d} \;+\; \mathcal{O}(|\gamma|^4),$$

where V_vac is the vacuum covariance matrix on the wedge. Since V⁻¹_vac ∼ (Unruh temperature)⁻¹ for the regularized wedge, the relative entropy is finite and **quadratic in the displacement amplitude** — not linear.

### Implication

The lock violation scales as:

$$\delta_{\mathrm{lock}}(\text{coherent}) \;\sim\; \frac{|\gamma|^2\,\hbar\omega}{T_U\,S_{\mathrm{BH}}} \;\sim\; \frac{|\gamma|^2}{S_{\mathrm{BH}}}$$

whereas a generic state at the same energy ΔE = |γ|²ħω would saturate the Casini bound and yield δ_lock ∼ ΔE/R (linear in energy). **Coherent states are quadratically suppressed**: they carry energy without linearly degrading the lock calibration. This is because coherent states preserve the *eigenvalue spectrum* of the reduced density matrix to first order; their effect is purely a unitary rotation in the wedge algebra, not a thermal redistribution.

### Which states *do* threaten the lock?

States that maximize S(ρ‖ρ_vac) per unit energy — Casini-bound-saturating states, e.g. a single Rindler-mode excitation above the Unruh thermal background — degrade the lock at linear order in ΔE. The natural classification is:

| State class | δ_lock scaling | Lock threat |
|---|---|---|
| Coherent (displaced vacuum) | O(|γ|²) ∼ O(ΔE²) | **Hidden at first order** |
| Single-mode excitation | O(ΔE) saturating bound | Maximal per unit energy |
| Thermal perturbation | O(ΔE) | Threatens lock linearly |

The structural moral: the L5 lock is *not* threatened by all energy-carrying states equally. Coherent excitations evade it at first order; the lock discriminates between "unitary-rotation" perturbations and "spectral" perturbations. This is a testable distinction: it implies that in the P2 sonic-horizon experiment, coherent-state preparations of the BEC should show locked thermality/lapse/entanglement even at macroscopic occupation numbers, while thermal-mode excitations at much lower energies should show measurable decoupling.
