# SPU Framework  
**Symmetry–Phase–Unification**

---

## Abstract

SPU (Symmetry–Phase–Unification) is a theoretical framework that explores how the structure of quantum field theory and renormalization group (RG) dynamics may be constrained by an underlying high-dimensional symmetry background.  

The framework is built around a compact symmetric space based on the coset $E_7 / SU(8)$, which fixes a *nominal capacity* of fermionic degrees of freedom.  

Physical observables, however, depend on an *effective* number of active modes.  
This reduction is described by a dynamical parameter $\delta$, arising from standard quantum-field-theoretic effects (mass generation and partial decoupling), not from topology.

The purpose of SPU is **not** to fine-tune parameters, but to demonstrate that:
- the RG flow of gauge couplings is **structurally constrained**,
- predictions are **stable under variations of dynamical inputs**,
- no critical or finely tuned values are required.

This repository provides the theoretical structure, analytical derivations, and numerical support scripts.

---

## 1. Conceptual Overview

SPU is organized as a logical chain:

1. **Geometric capacity**
   - A high-symmetry background based on $E_7 / SU(8)$
   - Fixes a discrete nominal number of fermionic degrees of freedom

2. **Dynamical reduction**
   - Interactions generate partial decoupling of modes
   - Encoded in a continuous parameter $\delta$

3. **Renormalization group flow**
   - Gauge couplings depend on the *effective* number of modes
   - Stability, not fine tuning, is the guiding principle

---

## 2. Geometric Input

The geometric background is the compact symmetric space:

$$
M = \frac{E_7}{SU(8)}
$$

with properties:
- $\dim(E_7) = 133$
- $\dim(SU(8)) = 63$
- $\dim(M) = 70$

The de Rham cohomology of this space has total dimension:

$$
\dim H^\ast(M) = 128
$$

In SPU this number is interpreted as a **nominal fermionic capacity**:

$$
N_f^{\mathrm{nom}} = 128
$$

No claim is made that this number directly fixes physical observables.

(See **Appendix A** for details.)

---

## 3. Effective Degrees of Freedom

Physical running depends on an *effective* number of fermionic modes:

$$
N_f^{\mathrm{eff}}(\mu) = N_f^{\mathrm{nom}} - \delta(\mu)
$$

where:
- $\delta$ is **continuous**
- $\delta$ is **scale-dependent in principle**
- $\delta$ parametrizes partial dynamical decoupling

Importantly:
- $\delta$ is **not topological**
- $\delta$ is **not fixed by group theory**
- $\delta$ is **not an index-theorem invariant**

---

## 4. Origin of the Parameter $\delta$

The parameter $\delta$ arises from standard QFT mechanisms:

- loop-induced masses,
- defect or mediator fields,
- suppression of RG contributions from massive modes.

A minimal model involves:
- quasi-critical fermions,
- an emergent scalar or defect field,
- Yukawa-type interactions.

At one loop, this leads to a smooth suppression factor for RG contributions.

A detailed derivation is provided in **Appendix B**:  
> *Derivation of $\delta$: RG and QFT Analysis*

---

## 5. Renormalization Group Structure

Gauge coupling running follows standard one-loop RG equations:

$$
\beta(g) = -\frac{b_0}{16\pi^2} g^3
$$

with coefficients depending on $N_f^{\mathrm{eff}}$.

SPU does **not** modify RG equations.  
It constrains **inputs**, not the formalism.

---

## 6. Numerical Stability

Numerical scans show that:
- variations of $\delta$ at the 10–20% level
- induce only small, smooth changes in RG outputs
- no critical value of $\delta$ is required

This demonstrates:
- absence of fine tuning,
- robustness of the framework.

(See `stability_scan.py`.)

---

## 7. What SPU Does *Not* Claim

For clarity, SPU does **not** claim:
- that $\delta$ is a topological invariant;
- that $\delta$ is uniquely fixed;
- that physical constants are derived with arbitrary precision;
- that new RG equations are introduced.

SPU is a **structural and dynamical framework**, not a numerological model.

---


## 8. Interpretation and Outlook

SPU suggests that:
- symmetry and geometry may constrain *how many* degrees of freedom exist,
- dynamics determines *how many are active*,
- RG flow translates this structure into observable physics.

The framework is compatible with standard QFT and RG methods and is intended as a basis for further refinement, not as a final predictive theory.

---

## References

Standard references on:
- Lie groups and symmetric spaces
- Renormalization group methods
- Quantum field theory

are sufficient to follow all derivations.

## ⚖️ License

MIT License - See [LICENSE](./LICENSE)

---

## 📧 Contact

**Lead Researcher:** Marco Fanavigator  
**Email:** marcofa@protonmail.com  
**Zenodo:** 0.5281/zenodo.17962427

---

> **"In physics, we don't just ask 'does it work?' We ask 'why is it true?'"**  
> 
> SPU is an attempt at the second question.  
> **And the observations show it works.**
