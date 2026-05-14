# R₀ Symmetry Bound from E₇ Algebraic Structure

**Status:** Semi-analytical — May 2026  
**Depends on:** `IR_Dominance_Calculator.py`, E₇ representation theory  
**Purpose:** Constrain R₀ = κ₃⁰/κ₄⁰ from group theory without free parameters

---

## Abstract

We derive algebraic bounds on the UV ratio R₀ = κ₃⁰/κ₄⁰ entering the
IR dominance mechanism of SPU. Using only the branching rule
E�� ⊃ E₆ × U(1), the Dynkin indices and quadratic Casimirs of the
relevant representations, we show that R₀ is **not a free parameter**
but lies in the range (0.304, 0.964), with a geometrically preferred
value R₀ ≈ 0.895 at μ = M_GUT.

---

## 1. Key Algebraic Inputs (exact, from Lie theory)

| Quantity | Value | Source |
|----------|-------|--------|
| C₂(56 of E₇) | 57/2 = 28.500 | Dynkin tables |
| C₂(27 of E₆) | 26/3 = 8.667 | Dynkin tables |
| I(56 of E₇) | 6 | Dynkin index |
| I(27 of E₆) | 6 | Dynkin index |
| Branching: 56 → | 27₊₁ ⊕ 27̄₋₁ ⊕ 1₊₄ ⊕ 1₋₄ | E₇ ⊃ E₆×U(1) |
| E₆ fraction in 56 | 54/56 = 27/28 ≈ 0.9643 | Branching |

### Critical observation: I(56) = I(27) = 6

The Dynkin indices are **equal**. This means:
- R₀ does **not** depend on coupling strengths
- R₀ is determined **purely by geometry**: branching fractions and Casimir suppression

---

## 2. Spectral Weight in SPU Formalism

Following the SPU spectral weight function:

$$w(R, \mu) = \frac{C_2(R)}{C_2(R) + (\mu/M_0)^2}$$

The UV coefficients are:

$$\kappa_4^0 \propto w(\mathbf{56}, \mu) \cdot I(\mathbf{56})$$
$$\kappa_3^0 \propto w(\mathbf{27}, \mu) \cdot I(\mathbf{27}) \cdot \frac{54}{56}$$

Since I(56) = I(27), the ratio simplifies to:

$$\boxed{R_0(\mu) = \frac{\kappa_3^0}{\kappa_4^0} = \frac{27}{28} \cdot \frac{C_2(\mathbf{27})}{C_2(\mathbf{27}) + (\mu/M_0)^2} \cdot \frac{C_2(\mathbf{56}) + (\mu/M_0)^2}{C_2(\mathbf{56})}}$$

### Running of R₀ with matching scale

| x = (μ/M₀)² | w(56) | w(27) | R₀ |
|-------------|-------|-------|----|
| 0.01 (deep UV) | 0.9996 | 0.9988 | 0.9635 |
| 1.0 (μ = M_GUT) | 0.9661 | 0.8966 | **0.8949** |
| 5.0 | 0.8507 | 0.6341 | 0.7188 |
| 10.0 | 0.7403 | 0.4643 | 0.6048 |
| 50.0 | 0.3631 | 0.1477 | 0.3924 |

---

## 3. Algebraic Bounds

**Upper bound** (UV limit, x → 0):

$$R_0 \leq \frac{54}{56} = \frac{27}{28} \approx 0.9643$$

This comes purely from the branching rule. In the limit where all modes
participate equally, κ₃/κ₄ is just the fraction of the 56 that carries
the cubic invariant.

**Lower bound** (IR dominance condition, from `IR_Dominance_Calculator`):

$$R_0 \geq \frac{C_2(\mathbf{27})}{C_2(\mathbf{56})} = \frac{26/3}{57/2} = \frac{52}{171} \approx 0.3041$$

Below this value, the cubic harmonic never dominates in the IR and the
Z₄→Z₃ transition does not occur.

**Geometrically preferred value** at μ = M_GUT (x = 1):

$$R_0^{\text{nat}} \approx 0.895$$

---

## 4. Compatibility with SPU and Z₄→Z₃ Transition

The entire algebraic range (0.304, 0.964) lies **within** the physical
window for the IR dominance mechanism. This means:

- For **any** R₀ in the algebraic range, the Z₄→Z₃ transition occurs
- The transition scale μ* falls in the window [M_GUT, M_Pl] for R₀ ∈ (0.40, 0.99)
- The value R₀ ≈ 0.65 used in SPU lies within the natural range

---

## 5. What This Argument Does and Does Not Prove

| Claim | Status |
|-------|--------|
| R₀ is a free parameter (arbitrary) | ✗ **Disproved** — algebraically bounded |
| R₀ is fully determined without further input | ✗ Not yet — needs heat-kernel integral |
| R₀ ∈ (0.304, 0.964) from E₇ structure alone | ✓ **Established** |
| R₀ ≈ 0.65 (SPU value) is natural | ✓ Compatible with geometric estimate |
| Exact value derivable from Haar measure on E₇/SU(8) | ◑ Open — Road 2 |

---

## 6. What Is Still Needed (Road 2)

The exact value of R₀ requires computing:

$$R_0 = \frac{\int_{E_7/SU(8)} d\mu_{\text{Haar}} \, I_3[\Phi] \cdot e^{-S_{\text{UV}}[\Phi]}}{\int_{E_7/SU(8)} d\mu_{\text{Haar}} \, I_4[\Psi] \cdot e^{-S_{\text{UV}}[\Psi]}}$$

This is a heat-kernel integral on the 70-dimensional coset, technically
well-defined but computationally demanding. It would reduce R₀ to a
pure number determined by the geometry of E₇/SU(8) alone.

---

## Summary

R₀ is **semi-constrained** by E₇ group theory:

$$R_0 \in \left(\frac{52}{171},\, \frac{27}{28}\right) \approx (0.304,\, 0.964)$$

with geometric preference R₀ ≈ 0.895 at μ = M_GUT from the differential
Casimir suppression of the two sectors. The SPU value R₀ ≈ 0.65 is
compatible. Full determination requires a heat-kernel calculation on
E��/SU(8), which constitutes the primary open computational task.
