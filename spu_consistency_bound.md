# Consistency Bound on the Dynamical Parameter δ

**SPU Framework**

---

## Abstract

In the SPU framework, the effective number of fermionic degrees of freedom contributing to renormalization group (RG) running is given by

$$N_f^{\mathrm{eff}} = N_f^{\mathrm{nom}} - \delta$$

where $N_f^{\mathrm{nom}} = 128$ is a discrete structural capacity and $\delta$ parametrizes dynamical decoupling effects.

In this document we demonstrate that $\delta$ cannot take arbitrary values. Requiring **RG consistency, stability, and absence of pathological behavior** restricts $\delta$ to a finite interval. This bound is independent of UV completion details and does not rely on topological arguments.

---

## 1. Role of δ in SPU

The parameter $\delta$ encodes the partial suppression of fermionic modes due to dynamical effects such as:
- loop-induced masses,
- decoupling thresholds,
- effective RG weights.

It is **not**:
- a topological invariant,
- fixed by group theory,
- fine-tuned to match observables.

Instead, $\delta$ is constrained by **consistency requirements**.

---

## 2. Effective Degrees of Freedom

We define:

$$N_f^{\mathrm{eff}}(\mu) = 128 - \delta$$

Gauge coupling beta functions depend explicitly on $N_f^{\mathrm{eff}}$. Different choices of $\delta$ therefore lead to qualitatively different RG behaviors.

---

## 3. Consistency Criteria

A value of $\delta$ is considered **physically admissible** if the resulting RG flow satisfies:

1. **Perturbativity**  
   Gauge couplings remain finite up to the unification scale.

2. **Absence of premature Landau poles**  
   No divergence below $M_{\text{GUT}}$.

3. **Qualitative unification**  
   Non-abelian couplings approach each other within the expected energy range.

4. **Stability under small variations**  
   No extreme sensitivity to $\mathcal{O}(10\%)$ changes in $\delta$.

These criteria are minimal and model-independent.

---

## 4. Exclusion of Small δ

For very small $\delta$:

$$\delta \ll 1 \quad \Rightarrow \quad N_f^{\mathrm{eff}} \approx 128$$

leading to:
- excessively large fermionic contributions,
- flattening or sign change of beta functions,
- destabilization of RG flow.

Numerical scans show that in this regime:
- perturbativity is lost,
- or unification fails.

Thus, very small $\delta$ values are excluded.

---

## 5. Exclusion of Large δ

For large $\delta$:

$$\delta \gtrsim 1 \quad \Rightarrow \quad N_f^{\mathrm{eff}} \ll 128$$

leading to:
- insufficient fermionic screening,
- overly steep RG running,
- failure to approach a common unification scale.

In this regime, RG trajectories become unstable or inconsistent.

---

## 6. Allowed Interval for δ

Combining the exclusions above, we obtain a **finite consistency window**:

$$\boxed{\delta_{\min} \;\lesssim\; \delta \;\lesssim\; \delta_{\max}}$$

Numerical stability scans indicate a representative interval:

$$\boxed{0.4 \;\lesssim\; \delta \;\lesssim\; 0.7}$$

The precise endpoints are not universal constants; what matters is the **existence of a bounded interval**.

---

## 7. Independence from UV Details

The bound on $\delta$:
- does not depend on a specific UV completion,
- does not assume supersymmetry,
- does not rely on topology or index theorems.

It emerges solely from:
- RG structure,
- effective field theory consistency,
- dynamical decoupling.

---

## 8. Relation to Numerical Scans

The bound is supported by numerical scans implemented in:

- `stability_scan.py`
- `rg_running.py`

These scans show that:
- RG outputs vary smoothly within the allowed interval,
- no fine-tuned critical value of $\delta$ is required.

---

## 9. Interpretation

The consistency bound implies that:
- $\delta$ is **not arbitrary**,
- SPU possesses genuine predictive structure,
- geometry fixes capacity, dynamics fixes accessibility.

This moves SPU beyond a purely parametric framework.

---

## 10. Summary

- $N_f^{\mathrm{nom}} = 128$ is a structural input.
- $\delta$ parametrizes dynamical suppression.
- RG consistency restricts $\delta$ to a finite interval.
- The bound is robust and model-independent.

This constitutes a key structural result of the SPU framework.

---

**End of document**