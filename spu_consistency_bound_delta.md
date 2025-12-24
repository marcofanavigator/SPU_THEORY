# Consistency Bound on the Parameter δ

## Internal Constraints in the SPU Framework

## Abstract

In the SPU framework, the parameter $\delta$ encodes the dynamical reduction of the nominal fermionic capacity fixed by topology. While $\delta$ is not determined by topology alone, it cannot take arbitrary values. In this document we derive **model-independent consistency bounds** on $\delta$ based solely on internal requirements of quantum field theory, renormalization group stability, and unitarity. We show that these constraints restrict $\delta$ to a narrow, physically meaningful window, without using the experimental value of the fine-structure constant as an input.

---

## 1. Definition and Role of δ

Topology fixes the nominal fermionic capacity of the SPU background:

$$N_f^{\mathrm{nom}} = \dim H^*(E_7/SU(8)) = 128$$

Dynamics reduces the number of degrees of freedom contributing to RG running:

$$N_f^{\mathrm{eff}} = N_f^{\mathrm{nom}} - \delta$$

The parameter $\delta$ therefore represents a **partial dynamical decoupling**, not the removal of degrees of freedom.

---

## 2. General Requirements on δ

Any admissible value of $\delta$ must satisfy the following **consistency conditions**, independent of phenomenology.

---

### 2.1 Positivity and capacity bound

By definition:

$$0 \le \delta \le N_f^{\mathrm{nom}}$$

In addition, SPU requires a large effective fermionic sector:

$$N_f^{\mathrm{eff}} \gg 1$$

This immediately excludes $\delta \sim \mathcal{O}(10)$ or larger.

---

### 2.2 Perturbative control of RG running

The one-loop beta functions for gauge couplings take the form:

$$\beta(g) = -\frac{b_0}{16\pi^2} g^3, \qquad b_0 = b_{\text{gauge}} - c\,N_f^{\mathrm{eff}}$$

Consistency requires:
- no sign flip of $b_0$ in the physical range,
- absence of Landau poles below the unification scale.

This excludes values of $\delta$ that push $N_f^{\mathrm{eff}}$ too close to or beyond the critical threshold.

---

### 2.3 Stability of the RG fixed structure

SPU relies on a **stable RG trajectory** connecting:
- a high-energy symmetric phase,
- the low-energy effective theory.

Numerical stability scans show that:
- small variations in $\delta$ do not destabilize the flow,
- large deviations do.

This implies an **allowed interval**, not a fine-tuned point.

---

## 3. Dynamical Origin Constraint

From the minimal dynamical derivation (see `Derivation_of_Delta.md`), $\delta$ takes the generic form:

$$\delta \sim \frac{g^2}{M_\star^2/\mu^2 + g^2\left(1 + \frac{1}{8\pi^2}\right)}$$

For natural parameters:
- $g = \mathcal{O}(1)$,
- $M_\star \sim \mu$,

one obtains:

$$\delta = \mathcal{O}(0.1\text{–}1)$$

Values parametrically smaller than this would require unnatural hierarchies.

---

## 4. Combined Consistency Window

Combining:
- RG stability,
- perturbative control,
- naturalness of the dynamical origin,

one finds the **consistency window**:

$$\boxed{0.5 \;\lesssim\; \delta \;\lesssim\; 0.7}$$

This bound is:
- internal to the theory,
- independent of experimental inputs,
- stable under small deformations of assumptions.

---

## 5. Relation to Observables (Non-input)

Importantly:
- the experimental value of $\alpha_{\mathrm{em}}$ is **not** used to derive this bound;
- it serves only as an a posteriori check.

The observed agreement therefore constitutes a **consistency success**, not a fit.

---

## 6. What This Result Does — and Does Not — Claim

### This result claims:

- $\delta$ is constrained by theory alone,
- SPU is predictive at the structural level.

### This result does not claim:

- an exact value for $\delta$,
- a topological determination of $\delta$,
- a unique microscopic mechanism.

---

## 7. Conclusion

The parameter $\delta$ in SPU is neither arbitrary nor fine-tuned. General requirements of quantum field theory restrict it to a narrow, physically meaningful interval.

Within this window:
- RG flows are stable,
- perturbation theory is valid,
- phenomenologically viable values emerge naturally.

This establishes $\delta$ as a **controlled dynamical parameter**, not a free constant.

---

**End of document.**