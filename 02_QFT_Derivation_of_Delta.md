# QFT Derivation of the Parameter δ

## Abstract
This document provides a standalone, technical derivation of the parameter $\delta$ used in the SPU framework. It collects the explicit quantum-field-theoretic and RG arguments that justify the appearance, definition, and expected magnitude of $\delta$.

## 1. Conceptual Role of δ
In SPU, the nominal number of fermionic degrees of freedom is fixed:
$$N_f^{\mathrm{nom}} = 128$$

However, physical observables depend on the **effective** number contributing to RG running:
$$N_f^{\mathrm{eff}}(\mu) = N_f^{\mathrm{nom}} - \delta(\mu)$$

The parameter $\delta$ therefore quantifies a **partial dynamical decoupling** of modes, not their absence.

## 2. Minimal Dynamical Ingredients
The SPU medium contains:
- **Quasi-critical fermionic modes** $\Psi^\star$
- **An emergent defect or scalar excitation** $\Phi$

The minimal interaction compatible with locality and symmetry is:
$$\mathcal{L}_{\text{int}} = g\,\Phi\,\bar\Psi^\star \Psi^\star$$
with:
- Coupling $g = O(1)$
- No fine-tuned mass scales

## 3. One-Loop Self-Energy of the Defect
At one loop, the defect $\Phi$ receives a fermionic self-energy correction:
$$\Pi_\Phi(p^2) = g^2 \int \frac{d^4 k}{(2\pi)^4} \frac{\mathrm{Tr}[(\slashed{k})(\slashed{k} + \slashed{p})]}{k^2 (k+p)^2}$$

For momenta $p^2 \sim \mu^2$, standard dimensional regularization yields:
$$\boxed{\Pi_\Phi(\mu^2) \simeq \frac{g^2}{8\pi^2}\,\mu^2}$$
This is a textbook QFT result.

## 4. Effective Defect Mass
Including the loop correction, the effective mass of the defect is:
$$M_{\Phi,\mathrm{eff}}^2(\mu) = M_\star^2 + \frac{g^2}{8\pi^2}\,\mu^2$$
where $M_\star \sim \mu$ is the bare mass scale.

## 5. Induced Mass for Quasi-Critical Modes
Integrating out the defect induces an effective mass for $\Psi^\star$:
$$M_{\mathrm{eff}}^2(\mu) \simeq \frac{g^2\,\mu^2}{M_{\Phi,\mathrm{eff}}^2(\mu)}$$
This suppresses the contribution of $\Psi^\star$ to RG running.

## 6. RG Weight Factor
The contribution of a massive mode to the RG $\beta$-functions is weighted by:
$$w(\mu) = \frac{1}{1 + M_{\mathrm{eff}}^2/\mu^2}$$
This motivates the definition:
$$\boxed{\delta(\mu) = 1 - w(\mu)}$$
Thus, $\delta$ measures how strongly a mode is dynamically suppressed.

## 7. Explicit Expression for δ
Substituting the expressions above yields:
$$\boxed{\delta(\mu) = \frac{g^2}{M_\star^2/\mu^2 + g^2\left(1 + \frac{1}{8\pi^2}\right)}}$$

This formula is:
- Continuous
- RG-based
- Independent of topology

## 8. Natural Size of δ
For natural parameters:
- $g \sim 1$
- $M_\star \sim (0.8\text{--}1)\,\mu$

One finds:
$$\delta \approx 0.55\text{--}0.65$$

No fine-tuning is required.

## 9. What δ Is Not
For completeness:
- ❌ $\delta$ is **not** a topological invariant
- ❌ $\delta$ does **not** arise from index theorems
- ❌ $\delta$ is **not** fixed by cohomology or group theory alone

## 10. Summary
- **Topology** fixes a discrete capacity: $N_f^{\mathrm{nom}} = 128$
- **Dynamics** fixes the effective reduction: $\delta$
- **RG** connects this structure to observables

This derivation provides the technical backbone for the use of $\delta$ in the SPU framework.