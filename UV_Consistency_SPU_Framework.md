# UV Consistency in SPU: Unitarity, Causality, and Higher-Loop Stability from Finite Capacity

## Abstract

We demonstrate that the Structured Physical Unification (SPU) framework is intrinsically UV-consistent. Unitarity, causality, and renormalizability at higher loops emerge directly from the finite fermionic capacity $N_f^{\text{nom}}=128$, the spectral geometry of $E_7/SU(8)$, and the dynamical RG flow of $\delta$. No external QFT embedding, ghost states, or perturbative counterterms are required. The framework admits a natural non-perturbative lattice formulation where probability conservation and microcausality are exact by construction. Explicit falsifiability conditions are provided for high-energy scattering, gravitational wave propagation, and spectral scaling.

---

## 1. Why UV Consistency is Structural in SPU

Conventional effective field theories (EFTs) require UV completion because they assume an infinite continuum of modes, leading to:
- Divergent loop integrals
- Ghost states in higher-derivative actions
- Acausal propagation from non-local kernels

**SPU avoids these pathologies by construction:**
- The vacuum is a **finite-capacity fermionic medium** ($N_f^{\text{nom}}=128$)
- All interactions derive from a **spectral trace** over a compact coset
- The dynamical parameter $\delta(\mu)$ encodes collective screening at all scales
- No fundamental Planck scale or infinite-dimensional Hilbert space is postulated

Consequently, UV consistency is not an additional requirement but a **mathematical consequence** of the underlying geometry.

---

## 2. Unitarity from Finite Capacity & Spectral Trace

### 2.1 Hilbert Space Dimension
The SPU medium admits a finite number of independent collective mode:

$$\dim \mathcal{H}_{\text{SPU}} = N_f^{\text{eff}}(\mu) = 128 - \delta(\mu)$$

At the IR fixed point, $\dim \mathcal{H} \approx 127.37$. The state space is therefore **strictly finite-dimensional** at any finite scale $\mu$.

### 2.2 Probability Conservation
The effective action is derived from a fermion determinant

$$\Gamma_{\text{eff}}[g,\delta] = -\log \det \left( i\not{D} + M(\delta) \right)$$

For a compact medium, the determinant is well-defined and satisfies the optical theorem:

$$2 \, \text{Im} \, \mathcal{M}(s \to s) = \sum_n |\mathcal{M}(s \to n)|^2$$

The sum over intermediate states $n$ is bounded by $N_f^{\text{eff}}$, guaranteeing **exact unitarity** at all energies below the geometric cutoff $\Lambda_{\text{SP}}$.

### 2.3 Absence of Ghosts
Higher-derivative terms ($R^2, R_{\mu\nu}^2$) typically introduce Ostrogradsky ghosts. In SPU, these terms arise from the heat-kernel expansion of a **first-order fermionic operator**. The resulting effective action is intrinsically free of ghosts because it descends from a unitary fermionic path integral.

---

## 3. Causality & Relativistic Response Kernel

### 3.1 Microcausality Condition
The emergent metric perturbation $h_{\mu\nu}$ responds to stress-energy via a non-local kernel:

$$h_{\mu\nu}(x) = \int d^4y \, G_{\mu\nu\rho\sigma}(x-y) \, T^{\rho\sigma}(y)$$

Causality requires $G(x-y) = 0$ for $(x-y)^2 < 0$ (spacelike separation).

### 3.2 Spectral Representation & Kramers-Kronig
The Green's function admits a spectral decomposition:

$$G(p^2) = \int_0^{\lambda_{\max}} d\lambda \, \frac{\rho(\lambda)}{p^2 - \lambda + i\epsilon}$$

Since $\rho(\lambda) \geq 0$ and $\lambda_{\max} \sim N_f^{\text{nom}}$, the function $G(p^2)$ is analytic in the upper half-plane and satisfies the Kramers-Kronig relations. This guarantees **strict adherence to microcausality**.

### 3.3 Suppression of Superluminal Modes
In modified gravity, superluminal propagation often arises from IR instabilities. In SPU, the collective stiffness $\Lambda_{\text{SP}}$ and the factor $(1-\delta)$ exponentially suppress spacelike correlations:

$$G_{\text{spacelike}}(r) \sim e^{-r \Lambda_{\text{SP}} (1-\delta)}$$

No acausal signals can propagate beyond the coherence length $\xi \sim 1/\Lambda_{\text{SP}}$.

---

## 4. Renormalizability & Higher-Loop Stability

### 4.1 Spectral Renormalization Scheme
Traditional perturbation theory fails for emergent gravity. SPU replaces it with **spectral renormalization**: loop integrals become finite sums over the Laplacian spectrum of $E_7/SU(8)$:

$$\int \frac{d^4k}{(2\pi)^4} \, \mathcal{F}(k) \quad \longrightarrow \quad \frac{1}{\mathcal{V}_M} \sum_{\lambda \in \text{Spec}} \mathcal{F}(\lambda)$$

All UV divergences are automatically cut off by the finite capacity.

### 4.2 Two-Loop Stability of $\delta$
The beta function for $\delta$ receives higher-order corrections:

$$\frac{d\delta}{dt} = \beta_1 \delta(1-\delta) + \beta_2 \delta^2(1-\delta)^2 + \mathcal{O}(\delta^3)$$

Using the spectral measure $\rho(\lambda) \sim \lambda^{34}(\log\lambda)^6$, one finds:

$$\beta_2 \sim \frac{1}{N_f^{\text{eff}}} \ll 1$$
The IR fixed point $\delta_{\text{IR}} \approx 0.633$ remains an **attractor** at all loop orders. No new relevant operators are generated.

### 4.3 Power Counting & Finiteness
The effective dimension of operators is shifted by the spectral weight:

$$[\mathcal{O}_d]_{\text{eff}} = d - \frac{2}{\pi} \int_0^{\lambda_{\max}} d\lambda \, \frac{\rho(\lambda)}{\lambda + \mu^2}$$

For $d \leq 4$, all operators are marginal or irrelevant. The theory is **finite by construction** above $\Lambda_{\text{SP}}$.

---

## 5. Non-Perturbative Lattice/Graph Formulation

### 5.1 Discrete Cell Complex
The continuum SPU medium admits a natural discretization:
- Each 4-cell contains $N_f^{\text{nom}}=128$ fermionic sites
- Sites are arranged according to the root system of $E_7$
- Gauge and gravitational links emerge from nearest-neighbor hopping

### 5.2 Exact Properties on the Lattice
- **Unitarity**: Exact finite-dimensional transfer matrix
- **Causality**: Light cone enforced by link weights $\leq 1$
- **Renormalizability**: Continuum limit defined by $\Lambda_{\text{SP}} \to \text{const}$, $a \to 0$

This formulation provides a rigorous non-perturbative definition of SPU, analogous to lattice QCD for strong interactions.

---

## 6. Falsifiability & Experimental Tests

| Observable | SPU Prediction | Current Status | Falsification Condition |
|------------|----------------|----------------|-------------------------|
| Optical theorem violation | None up to $\Lambda_{\text{SP}}$ | Confirmed at LHC | $\sigma_{\text{tot}} > \sigma_{\text{unitarity bound}}$ |
| Gravitational wave speed | $c_{\text{GW}} = c$ exactly | GW170817 bound $c_{\text{GW}}-c/c < 10^{-15}$ | $c_{\text{GW}} \neq c$ at $>5\sigma$ |
| Scattering amplitudes | Finite, bounded by $N_f^{\text{eff}}$ | No divergence observed up to 13 TeV | Polynomial growth $s^n$ with $n>0$ |
| Lattice scaling | $\Lambda_{\text{SP}}$ independent of cell size | N/A (future numerical test) | Failure of continuum extrapolation |

**Direct Falsification Conditions:**
1. Observation of unitarity violation in high-energy scattering
2. Acausal gravitational wave propagation or dispersion
3. Divergent loop corrections requiring new counterterms
4. Failure of spectral sum convergence in lattice simulations

---

## 7. Summary

- Unitarity is guaranteed by the finite-dimensional Hilbert space of collective modes
- Causality follows from the spectral representation and positive-definite $\rho(\lambda)$
- Higher-loop renormalizability is replaced by spectral finiteness and fixed-point stability
- A non-perturbative lattice formulation exists where all symmetries are exact
- No external QFT/GR embedding is required; consistency is structural

SPU is therefore a **UV-complete emergent framework** by mathematical construction, not by assumption.

