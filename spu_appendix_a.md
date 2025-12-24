# Appendix A – Spectral Derivation and Role of δ in SPU Theory

## A.1 Purpose of this appendix

This appendix clarifies the **spectral, topological, and dynamical** role of fermionic contributions in SPU theory, with particular emphasis on the parameter $\delta$.

The objectives are:

- rigorously separate **discrete spectral structure** and **dynamical RG corrections**
- clarify the correct physical meaning of numerical factors emerging in the fermionic determinant
- eliminate any ambiguity regarding the origin of $\delta$

---

## A.2 Fermionic determinant and effective action

Consider a Euclidean Dirac operator coupled to a gauge field:

$$\mathcal{D} = i\slashed{D}$$

The one-loop effective action is given by:

$$\Gamma_{\text{eff}} = -\log \det \mathcal{D}$$

which can be regularized via heat-kernel representation:

$$\log \det \mathcal{D} = -\int_0^\infty \frac{ds}{s}\, \mathrm{Tr}\, e^{-s \mathcal{D}^2}$$

This procedure is standard in QFT and independent of specific topological assumptions.

---

## A.3 Heat kernel expansion and gauge term

The asymptotic expansion for $s \to 0$ produces the Seeley–DeWitt coefficients:

$$\mathrm{Tr}\, e^{-s \mathcal{D}^2} \sim \sum_{n \geq 0} a_n\, s^{(n-d)/2}$$

In four dimensions, the term relevant for the running of $\alpha$ is:

$$a_2 \supset c\, \int d^4x\, F_{\mu\nu}F^{\mu\nu}$$

which generates the standard contribution to the electromagnetic beta-function.

---

## A.4 η-invariant and spectral structure

In the presence of a non-trivial global structure, the fermionic determinant includes a spectral phase described by the **Atiyah–Patodi–Singer η-invariant**:

$$\eta(\mathcal{D}) = \sum_{\lambda \neq 0} \mathrm{sign}(\lambda)\, |\lambda|^{-s}\bigg|_{s\to 0}$$

The η-invariant is a **spectral-topological** quantity that:

- depends only on the global spectrum of the operator
- takes discrete values (integers or known rationals)
- does not generate continuous free parameters

---

## A.5 Origin of the universal factor 2/π

In the regularized determinant, the η-invariant contribution enters in the form:

$$\Gamma_\eta = i\, \frac{\pi}{2}\, \eta(\mathcal{D})$$

It follows that the overall spectral weight of fermionic modes is naturally normalized by a factor:

$$\boxed{\frac{2}{\pi}}$$

This factor is:

- universal
- independent of dynamics
- fixed by spectral theory

---

## A.6 Role of discrete structure (128)

In the SPU context, the number:

$$N_f^{\text{nom}} = 128$$

represents the **discrete spectral multiplicity** of the fundamental fermionic modes in the model.

This value:

- is fixed by the internal structure of the theory
- does not depend on RG running
- is not modified by perturbative corrections

---

## A.7 Fundamental clarification: what δ is NOT

It is crucial to emphasize that:

- $\delta$ is **not** a topological invariant
- $\delta$ is **not** computable via the Atiyah–Singer index theorem
- $\delta$ does **not** emerge from the η-invariant
- $\delta$ is **not** fixed to a universal value

Any interpretation of $\delta$ as a purely topological quantity is incorrect.

---

## A.8 Correct origin of δ: RG dynamics

The parameter $\delta(\mu)$ instead arises from **dynamical one-loop effects**, as shown in the main body of work.

In the presence of quasi-critical modes coupled to an emergent scalar defect, a portion of the fermionic contributions to the beta-function becomes attenuated.

Formally:

$$N_f^{\text{eff}}(\mu) = N_f^{\text{nom}} - \delta(\mu)$$

where $\delta(\mu)$ is a continuous function of the RG scale.

---

## A.9 Final spectral–dynamical combination

The overall contribution of fermions to the effective determinant can be written as:

$$\eta_{\text{eff}}(\mu) = \frac{2}{\pi}\Big[128 - \delta(\mu)\Big]$$

Where:

- $128$ is fixed by the discrete spectral structure
- $2/\pi$ is a universal factor from the η-invariant
- $\delta(\mu)$ encodes the dynamical RG reduction of fermionic contributions

---

## A.10 Conclusion of this appendix

This formulation:

- ✓ preserves the correct spectral content of the theory
- ✓ eliminates conceptual ambiguities
- ✓ makes SPU coherent with standard QFT and RG
- ✓ definitively clarifies the physical role of $\delta$

$$\boxed{\text{Spectral structure} \;+\; \text{RG dynamics} \;\Rightarrow\; N_f^{\text{eff}}(\mu)}$$