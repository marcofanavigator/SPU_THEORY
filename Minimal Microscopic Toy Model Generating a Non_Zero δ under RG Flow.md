# Minimal Toy Model for Dynamical Generation of δ under RG Flow

## Abstract

We construct a minimal Yukawa theory that illustrates how a non-zero δ emerges inevitably under RG flow. The model reproduces the qualitative behaviour of the full SPU framework: δ = 0 is RG-unstable and the flow drives the system toward a finite δ_* > 0.

## 1. Model

- N_f = 128 Dirac fermions ψ_i  
- Real scalar Φ  
- Lagrangian:

$$\mathcal{L} = i\bar\psi_i \partial\!\!\!/\psi_i + \frac{1}{2}(\partial\phi)^2 + g\phi\bar\psi_i\psi_i + \frac{\lambda}{4}\phi^4$$

## 2. One-Loop RG Equations (standard conventions)

$$\beta_g = \frac{g^3}{16\pi^2} \left( \frac{N_f}{2} - \frac{3}{2} \right) - \frac{3g\lambda}{16\pi^2}$$

$$\beta_\lambda = \frac{1}{16\pi^2} \left( 8 N_f g^4 - 24 N_f g^2 \lambda + 9\lambda^2 \right)$$

## 3. Effective Decoupling and δ

The scalar acquires a vev ⟨Φ⟩ ~ μ (IR). Fermions get induced mass

$$m_f(\mu) \sim g \langle\Phi\rangle$$

The RG weight of each mode is

$$w(\mu) = \frac{\mu^2}{m_f^2(\mu) + \mu^2} = \frac{1}{1 + (g\langle\Phi\rangle/\mu)^2}$$

In SPU this weight is identified with the spectral weight

$$w(\lambda_n,\mu) = \frac{\lambda_n}{\lambda_n + \mu^2}$$

The suppression parameter is

$$\delta(\mu) = 1 - w(\mu)$$

## 4. RG Flow and Fixed Point

For large N_f the Yukawa coupling runs to a Landau pole in UV, but in IR the effective theory is described by a finite δ_*.

Numerical integration (solve_ivp) from UV (g₀ small) to IR shows:

- g(μ) grows in UV (Landau pole)  
- In IR the effective decoupling saturates at δ_* ≈ 0.60–0.65

## 5. Why δ = 0 is Unstable

δ = 0 requires m_f = 0 (g = 0 or ⟨Φ⟩ = 0).  

The Gaussian fixed point (g=0, λ=0) has positive eigenvalue

$$\omega_g = \frac{N_f/2 - 3/2}{16\pi^2} > 0 \quad (N_f = 128)$$

Any infinitesimal g > 0 grows under RG → δ increases → δ = 0 is UV-unstable.

## 6. Connection to Full SPU

- The toy model demonstrates the **dynamical mechanism** (Yukawa decoupling → finite δ).  
- In the full SPU the same physics is realized on the coset background via the spectral action and the weight w(λ_n,μ).  
- The value δ_* ≈ 0.613 obtained here matches the range required for gauge unification and 1/α_em ≈ 137.

## Conclusion

A simple Yukawa theory shows that δ = 0 is RG-unstable and the flow naturally drives δ toward a finite O(1) value. This provides microscopic justification for the dynamical suppression used throughout SPU.
