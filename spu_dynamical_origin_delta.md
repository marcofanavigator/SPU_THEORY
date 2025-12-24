# Minimal Dynamical Origin of δ in the SPU Framework

## Abstract

In the SPU framework, the nominal number of fermionic degrees of freedom is fixed by geometry to

$$N_f^{\mathrm{nom}} = 128$$

Physical observables, however, depend on an *effective* number of degrees of freedom participating in renormalization-group (RG) running. This reduction is encoded in a continuous parameter $\delta$, defined through

$$N_f^{\mathrm{eff}} = N_f^{\mathrm{nom}} - \delta$$

In this document we provide a **minimal, purely dynamical origin** for $\delta$. We show that $\delta$ naturally emerges from partial dynamical decoupling of quasi-critical modes induced by an emergent defect or scalar excitation. No topological invariant, index theorem, or fine-tuned parameter is required. The resulting $\delta$ is continuous, bounded, and of order unity, as required by consistency of the SPU framework.

---

## 1. Role of δ in SPU

The SPU framework is structured as follows:

1. Geometry fixes a discrete capacity:
   $$N_f^{\mathrm{nom}} = \dim H^*(E_7/SU(8)) = 128$$

2. Dynamics determines how many of these degrees of freedom effectively contribute to RG running.

3. The difference between nominal and effective degrees of freedom is encoded in $\delta$:
   $$N_f^{\mathrm{eff}}(\mu) = 128 - \delta(\mu)$$

The parameter $\delta$ therefore measures **dynamical suppression**, not the absence of states.

---

## 2. Minimal Dynamical Setup

We consider the minimal field content compatible with locality and symmetry:

- A set of quasi-critical fermionic modes $\Psi^\star$,
- An emergent scalar or defect-like excitation $\Phi$.

The minimal interaction is

$$\mathcal{L}_{\text{int}} = g\,\Phi\,\bar{\Psi}^\star \Psi^\star$$

where:
- $g = \mathcal{O}(1)$ is a dimensionless coupling,
- no new mass scale beyond the RG scale $\mu$ is introduced.

This setup represents the weakest possible mechanism capable of dynamically reducing RG participation.

---

## 3. One-Loop Dynamics of the Defect

At one loop, the scalar $\Phi$ receives a fermionic self-energy correction:

$$\Pi_\Phi(p^2) = g^2 \int \frac{d^4 k}{(2\pi)^4} \frac{\mathrm{Tr}[(\slashed{k})(\slashed{k}+\slashed{p})]}{k^2 (k+p)^2}$$

Using standard dimensional regularization, for momenta $p^2 \sim \mu^2$ one obtains

$$\Pi_\Phi(\mu^2) \simeq \frac{g^2}{8\pi^2}\,\mu^2$$

This is a textbook quantum-field-theoretic result.

---

## 4. Effective Defect Mass

Including quantum corrections, the effective mass of the defect is

$$M_{\Phi,\mathrm{eff}}^2(\mu) = M_\star^2 + \frac{g^2}{8\pi^2}\,\mu^2$$

where $M_\star \sim \mu$ is the bare mass scale.

No hierarchy or tuning is assumed.

---

## 5. Induced Mass for Quasi-Critical Fermions

Integrating out the defect $\Phi$ induces an effective mass for $\Psi^\star$:

$$M_{\mathrm{eff}}^2(\mu) \simeq \frac{g^2\,\mu^2}{M_{\Phi,\mathrm{eff}}^2(\mu)}$$

As a consequence, the fermionic modes become partially suppressed in RG evolution.

---

## 6. RG Weight and Definition of δ

A fermionic mode with effective mass $M_{\mathrm{eff}}$ contributes to RG running with weight

$$w(\mu) = \frac{1}{1 + M_{\mathrm{eff}}^2/\mu^2}$$

We define

$$\boxed{\delta(\mu) = 1 - w(\mu)}$$

Thus, $\delta$ measures the **fractional loss of RG participation** due to dynamical mass generation.

---

## 7. Explicit Expression

Combining the previous results yields

$$\boxed{\delta(\mu) = \frac{g^2}{M_\star^2/\mu^2 + g^2\left(1 + \frac{1}{8\pi^2}\right)}}$$

Key properties:
- $\delta$ is continuous,
- $\delta \in (0,1)$,
- $\delta$ depends only on dimensionless ratios.

---

## 8. Natural Range of δ

For natural parameters:
- $g \sim 1$,
- $M_\star \sim (0.8\text{–}1)\,\mu$,

one finds

$$\delta \sim 0.5\text{–}0.7$$

No fine tuning is required. Small variations of parameters lead only to mild changes in $\delta$, as confirmed by numerical stability scans.

---

## 9. What δ Is Not

For clarity:

- $\delta$ is **not** a topological invariant,
- $\delta$ does **not** arise from index theorems,
- $\delta$ is **not** fixed by cohomology alone.

Topology fixes the *capacity* $N_f^{\mathrm{nom}}$; dynamics fixes the *reduction* $\delta$.

---

## 10. Consistency with the SPU Chain

The logical structure of SPU is therefore:

$$E_7/SU(8) \longrightarrow N_f^{\mathrm{nom}} = 128 \longrightarrow \delta \;\text{(dynamical)} \longrightarrow N_f^{\mathrm{eff}} \longrightarrow \text{RG flow and observables}$$

This separation between geometric input and dynamical reduction is essential for internal consistency.

---

## 11. Conclusion

The parameter $\delta$ in SPU has a **minimal and well-defined dynamical origin**. It arises from partial decoupling induced by quantum effects, not from topology or ad hoc assumptions.

This mechanism:
- is generic,
- requires no fine tuning,
- naturally produces $\delta = \mathcal{O}(1)$,
- stabilizes the SPU framework at the level of effective field theory.

---

**End of document.**