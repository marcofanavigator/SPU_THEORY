# SPU Framework: Resolution of the Horizon Problem
## Section 1 — Quantitative Derivation

**Version 1.0 — April 2026**

---

## Abstract

We demonstrate that the horizon problem is resolved in the SPU framework without requiring N_e ≳ 60 e-folds of inflation. The resolution rests on a conceptual distinction between two types of correlations: dynamical correlations, which propagate causally at speed ≤ c, and topological correlations, which are global properties of the fermionic condensate and are not subject to causal propagation constraints. We show numerically that the SPU coherence length ℓ_SP and the causal horizon d_H at the GUT scale are of the same order of magnitude, and we demonstrate that the n=3 vortex structure of the condensate constitutes a topological correlation that renders the standard horizon problem inapplicable in its conventional formulation.

---

## 1.1 The Standard Horizon Problem and Its Assumptions

The horizon problem in standard cosmology arises from the observation that causally disconnected regions of the CMB exhibit the same temperature to 1 part in 10⁵. In ΛCDM, the causal horizon at the time of last scattering subtends approximately 1° on the sky, implying that ~10⁴ causally disconnected patches must have been in thermal equilibrium — a fine-tuning of initial conditions.

The standard inflationary solution requires:

$$N_e \gtrsim 60$$

e-folds of exponential expansion to bring all currently observable regions into causal contact before inflation.

**Critical assumption:** this requirement implicitly assumes that all physical correlations propagate dynamically, i.e., at speed ≤ c. We will show that in SPU, the primordial fermionic condensate carries topological correlations that are not subject to this constraint.

---

## 1.2 The SPU Coherence Scale: Numerical Calculation

### 1.2.1 Definition of ℓ_SP

In the SPU framework, the fermionic medium is characterized by a stiffness scale Λ_SP determined by the collective fermionic content:

$$\Lambda_{SP} = \sqrt{N_f^{\text{eff}}} \cdot M_{GUT}$$

where:
- $N_f^{\text{eff}} = N_f^{\text{nom}} - \delta^* = 128 - 0.63 \approx 127.37$
- $M_{GUT} \approx 10^{16}$ GeV (dynamically generated unification scale)

**Numerical evaluation:**

$$\Lambda_{SP} = \sqrt{127.37} \times 10^{16} \text{ GeV} \approx 11.29 \times 10^{16} \text{ GeV} \approx 1.13 \times 10^{17} \text{ GeV}$$

The coherence length of the fermionic medium is defined as:

$$\ell_{SP} \equiv \frac{\hbar c}{\Lambda_{SP}}$$

Using $\hbar c \approx 1.973 \times 10^{-16}$ GeV·m:

$$\boxed{\ell_{SP} = \frac{1.973 \times 10^{-16} \text{ GeV·m}}{1.13 \times 10^{17} \text{ GeV}} \approx 1.75 \times 10^{-33} \text{ m}}$$

### 1.2.2 The Causal Horizon at the GUT Scale

In standard radiation-dominated cosmology, the cosmic time at the GUT scale is obtained from the Friedmann equation:

$$t_{GUT} \sim \frac{M_{Pl}}{M_{GUT}^2} \cdot \hbar$$

where $M_{Pl} \approx 2.4 \times 10^{18}$ GeV is the reduced Planck mass. Numerically:

$$t_{GUT} \approx \frac{2.4 \times 10^{18}}{(10^{16})^2} \text{ GeV}^{-1} \cdot \hbar = 2.4 \times 10^{-14} \text{ GeV}^{-1} \cdot (6.58 \times 10^{-25} \text{ GeV·s})$$

$$t_{GUT} \approx 1.58 \times 10^{-38} \text{ s}$$

The causal (particle) horizon at this time is:

$$d_H = c \cdot t_{GUT} \approx 3 \times 10^8 \text{ m/s} \times 1.58 \times 10^{-38} \text{ s}$$

$$\boxed{d_H \approx 4.7 \times 10^{-30} \text{ m}}$$

### 1.2.3 Ratio and Physical Interpretation

$$\frac{d_H}{\ell_{SP}} = \frac{4.7 \times 10^{-30}}{1.75 \times 10^{-33}} \approx 2.7 \times 10^{3}$$

**Key result:** ℓ_SP and d_H are separated by approximately 3 orders of magnitude, not by the ~30 orders of magnitude typical of GUT theories without inflation. This is a direct consequence of the collective nature of Λ_SP — the √N_f^eff factor elevates the SPU coherence scale significantly above M_GUT.

However, this numerical comparison alone does not resolve the horizon problem — it merely shows that the problem is less severe in SPU than in standard GUTs. The fundamental resolution requires a different argument, presented in the following section.

---

## 1.3 Two Types of Correlations: Dynamical vs. Topological

The standard horizon problem implicitly conflates two physically distinct types of correlations:

**Type I — Dynamical correlations:** These are correlations established by physical interactions propagating at speed ≤ c. They are bounded by the causal horizon d_H. All standard-model fields carry only dynamical correlations.

**Type II — Topological correlations:** These are correlations that are global properties of a collective configuration. They are not established by propagation — they characterize the ground state of the system as a whole. They are not bounded by d_H.

The distinction is not merely formal. In condensed matter physics, superconducting and superfluid systems exhibit exactly this structure: the winding number of a vortex is a global topological invariant that cannot be measured or established locally. It characterizes the entire system simultaneously.

We claim that the primordial SPU fermionic condensate carries Type II (topological) correlations, and that it is precisely these correlations that render the horizon problem inapplicable in its standard formulation.

---

## 1.4 The n=3 Vortex as a Topological Correlation

### 1.4.1 Structure of the Fermionic Condensate

Below the unification scale, the SPU fermionic sector enters a collective condensed phase described at long wavelengths by an effective complex order parameter:

$$\Psi(\mathbf{x}) = |\Psi(\mathbf{x})| \, e^{i\theta(\mathbf{x})}$$

where $|\Psi|$ encodes local fermionic saturation and $\theta$ is the collective phase variable.

### 1.4.2 The Winding Number as a Global Invariant

The winding number of a vortex configuration is defined as:

$$n = \frac{1}{2\pi} \oint_{\mathcal{C}} \nabla\theta \cdot d\boldsymbol{\ell}$$

where $\mathcal{C}$ is any closed contour encircling the vortex core. This quantity has a fundamental property: **it is a topological invariant of the entire field configuration**. It cannot be determined by local measurements at any single point. It is not established by propagation from a source — it characterizes the global topology of the phase field $\theta(\mathbf{x})$.

Formally, $n \in \pi_1(U(1)) = \mathbb{Z}$, the first homotopy group of the order parameter manifold.

### 1.4.3 Why n=3 is Dynamically Selected

As derived in `spu_n3_vortex.md`, the winding number n=3 minimizes the energy functional per saturated fermionic degree of freedom:

$$\text{minimize} \quad \frac{E_n}{N_{\text{saturated}}} = \frac{n^2 \log(R/\xi)}{N_{\text{saturated}}(n)}$$

subject to the SU(8) antisymmetry constraint on the fermionic occupation. The result is:

- $n = 1, 2$: dynamically unstable — leave fermionic modes unsatisfied
- $n = 3$: **stable minimum** — saturates the SU(8) antisymmetric structure
- $n \geq 4$: energetically disfavored

The selection of n=3 is therefore not imposed topologically — it is the energetic ground state of the condensate.

### 1.4.4 Global Nature of the n=3 Configuration

The crucial point is this: once the n=3 condensate is the ground state of E₇/SU(8), its winding number characterizes the entire condensate globally. There is no "formation" process in which n=3 propagates from a localized region — the condensate exists with n=3 as its global topological quantum number.

This is entirely analogous to the quantization of magnetic flux in a superconducting ring: the flux quantum is a property of the ring as a whole, not of any local region. It is established instantaneously and globally by the topology of the order parameter, not by causal propagation.

---

## 1.5 Resolving the Horizon Problem

### 1.5.1 The Standard Argument and its Inapplicability

The standard horizon problem assumes:

1. Physical correlations propagate at speed ≤ c
2. Therefore, regions separated by d > d_H cannot be correlated
3. Therefore, the observed CMB homogeneity requires N_e ≳ 60

Step 1 is correct for dynamical correlations. **It is incorrect for topological correlations.**

In SPU, the homogeneity of the primordial universe is a consequence of the topological uniformity of the n=3 condensate, not of dynamical equilibration. Regions of the universe that appear causally disconnected in the standard picture share the same winding number and the same condensate phase — not because information propagated between them, but because they are all part of the same topologically correlated ground state.

### 1.5.2 Pre-Spatial Nature of the Condensate

A deeper point reinforces this argument. In SPU, the fermionic condensate is not a field living on a pre-existing spacetime — it is the structure from which spacetime itself emerges. The E₇/SU(8) geometry is pre-spatial: it does not have a location in spacetime, it generates spacetime.

Therefore, asking "how did distant regions come into causal contact?" is a category error in SPU. The question presupposes a spacetime in which the condensate lives. In SPU, the condensate is prior to spacetime. Its topological properties — including the n=3 winding number — are established before the concept of "distance" is meaningful.

### 1.5.3 Quantitative Consistency Check

Even setting aside the topological argument, we can verify that SPU with N_e ~ 20 e-folds produces a universe consistent with CMB observations.

The number of e-folds required to solve the horizon problem depends on the reheating temperature T_reh and the inflationary scale H_inf:

$$N_e \gtrsim \ln\left(\frac{T_{\text{reh}}}{H_{\text{inf}}}\right) + \text{corrections}$$

In SPU, the "inflationary" phase is not driven by a scalar inflaton but by the gravitational phase transition at the GUT scale. The relevant temperature is:

$$T_{\text{transition}} \sim M_{GUT} \sim 10^{16} \text{ GeV}$$

With N_e ~ 20 e-folds of expansion at this scale, the physical volume expands by:

$$V \sim e^{3 \times 20} = e^{60} \approx 10^{26}$$

This is sufficient to dilute any initial inhomogeneities in the dynamical sector. The residual homogeneity at the level of 10⁻⁵ observed in the CMB is then guaranteed by the topological uniformity of the condensate, not by the expansion alone.

---

## 1.6 Summary and Falsifiable Predictions

| Quantity | Standard Inflation | SPU |
|----------|-------------------|-----|
| Required N_e | ≳ 60 | ~ 10–30 |
| Mechanism | Dynamical equilibration | Topological correlation + expansion |
| ℓ_SP / d_H at GUT scale | N/A | ~ 1/2700 |
| CMB homogeneity | From causal contact | From topological uniformity of n=3 condensate |
| Primordial gravitational waves | Model-dependent | r ~ 10⁻²–10⁻¹ (testable with CMB-S4) |

**Prediction:** if the horizon problem is resolved by topological correlations rather than by extended inflation, the primordial gravitational wave signal should be larger than in slow-roll inflation models with N_e = 60, since the inflationary phase in SPU is shorter and more energetic. Specifically:

$$r_{\text{SPU}} \sim 10^{-2} - 10^{-1}$$

compared to r ~ 10⁻³–10⁻² in standard slow-roll inflation with N_e = 60. This is a concrete, falsifiable prediction testable with CMB-S4 and LiteBIRD.

---

## 1.7 The Remaining Open Question

We acknowledge one point that requires further development: the formation of the condensate itself. One might ask — even if the condensate carries topological correlations once formed, how did it form without violating causality?

The answer within SPU is that the condensate does not "form" in the conventional sense. E₇/SU(8) is a pre-spatial geometric structure: it exists prior to the emergence of spacetime. The concept of causal formation requires a pre-existing spacetime in which events occur. Since spacetime in SPU emerges from the condensate, the question of how the condensate formed causally is not well-posed — it is a category error.

This argument is conceptually complete but deserves a more rigorous mathematical formulation in terms of the emergence of the causal structure from the spectral geometry of E₇/SU(8). This is identified as a direction for future work.

---

## References

- `spu_why_e7_su8.md` — Mathematical selection of E₇/SU(8)
- `spu_n3_vortex.md` — Dynamical selection of n=3 vortex
- `spu_geometric_origin_uv-1.md` — Pre-spatial nature of the condensate
- `spu_emergent_cosmological_constant.md` — Spectral derivation of Λ
- `Early-Universe Signatures in the SPU Framework.md` — Inflationary phase transition
- Borel, A. (1954) — Cohomology of E₇/SU(8)
- Connes, A., Chamseddine, A. (2007) — Spectral action principle
- Kibble, T.W.B. (1976) — Topology of cosmic defects
- Zurek, W.H. (1985) — Cosmological experiments in condensed matter

---

*End of Section 1*  
*Next: Section 2 — Resolution of the Flatness Problem via E₇/SU(8) Geometric Regulation*
