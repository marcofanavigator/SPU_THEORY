# IR Dominance Criterion for Cubic vs. Quartic Vacuum Locking in SPU

## Abstract
We derive the semi-analytical renormalization group (RG) flow for the cubic ($\kappa_3$) and quartic ($\kappa_4$) phase harmonics in the SPU effective potential. By exploiting the spectral decoupling of fermionic modes across the branching $E_7 \to E_6 \times U(1)$, we show that the ratio $\mathcal{R}(\mu) \equiv \kappa_3(\mu)/\kappa_4(\mu)$ exhibits power-law enhancement in the infrared. A strict dominance criterion is established, yielding a crossover scale $\mu_*$ that separates the UV $Z_4$-locked regime from the IR $Z_3$-locked regime. The framework remains fully parameter-free, spectrally grounded, and explicitly falsifiable.

---

## 1. Geometric & Representation-Theoretic Context

The fundamental fermionic representation of $E_7$ is $\mathbf{56}$, whose lowest-degree invariant is quartic:
$$I_4(\mathbf{56}) = t_{ABCD} \Psi^A \Psi^B \Psi^C \Psi^D \quad \Rightarrow \quad V_{\text{eff}} \supset -\kappa_4 \cos(4\theta).$$
This naturally suggests a $Z_4$ vacuum structure. However, under the maximal branching:
$$E_7 \supset E_6 \times U(1), \qquad \mathbf{56} \to \mathbf{27}_{+1} \oplus \overline{\mathbf{27}}_{-1} \oplus \mathbf{1}_{+4} \oplus \mathbf{1}_{-4},$$
the $E_6$ sector admits a unique cubic invariant:
$$I_3(\mathbf{27}) = d_{abc} \phi^a \phi^b \phi^c \quad \Rightarrow \quad V_{\text{eff}} \supset -\kappa_3 \cos(3\theta).$$

The quadratic Casimir gap between the two sectors is strictly positive:
$$\Delta C_2 \equiv C_2(\mathbf{56}) - C_2(\mathbf{27}) > 0, \qquad C_2(\mathbf{56}) \approx 28.5, \quad C_2(\mathbf{27}) = \frac{26}{3} \approx 8.67.$$
This gap controls the spectral decoupling rate and dictates the infrared dominance of one harmonic over the other.

---

## 2. Spectral RG Flow Setup

The effective potential arises from the fermionic determinant:
$$V_{\text{eff}}(\theta;\mu) = -\frac{1}{2} \text{Tr} \log\left[ \frac{\slashed{D}^\dagger \slashed{D} + \Phi(\theta)^\dagger \Phi(\theta)}{\mu^2} \right].$$
Expanding in phase harmonics yields:
$$V_{\text{eff}}(\theta;\mu) = -\kappa_3(\mu)\cos(3\theta) - \kappa_4(\mu)\cos(4\theta) + \mathcal{O}(\cos m\theta).$$
Each coefficient $\kappa_m(\mu)$ receives contributions from modes in the representation $R_m$ associated with the $m$-th harmonic. In the spectral action formalism, the running is governed by the heat-kernel weight:
$$w(\lambda/\mu^2) = \frac{\lambda}{\lambda + \mu^2},$$
which suppresses heavy modes ($\lambda \gg \mu^2$) as $\mu$ decreases. The dominant eigenvalue in each sector scales with the quadratic Casimir:
$$\lambda_{\min}^{(m)} \simeq M_0^2 \, C_2(R_m),$$
where $M_0 \sim M_{\text{GUT}}$ sets the UV spectral normalization.

---

## 3. Semi-Analytical RG Equations for $\kappa_3(\mu)$ and $\kappa_4(\mu)$

Differentiating the spectral trace with respect to $\ln\mu$ yields the beta functions:
$$\boxed{ \mu \frac{d\kappa_m}{d\mu} = -2 \, \gamma_m(\mu) \, \kappa_m(\mu), \qquad \gamma_m(\mu) \equiv \frac{C_2(R_m)}{C_2(R_m) + \mu^2/M_0^2} }$$
The anomalous dimension $\gamma_m(\mu)$ interpolates between:
- **UV limit** ($\mu \gg M_0\sqrt{C_2}$): $\gamma_m \to 1$ (logarithmic running, full mode participation)
- **IR limit** ($\mu \ll M_0\sqrt{C_2}$): $\gamma_m \to \mu^2/[M_0^2 C_2(R_m)]$ (power suppression, heavy modes decouple)

Integrating from the GUT scale $\Lambda_{\text{GUT}}$ to scale $\mu$ gives the explicit running:
$$\boxed{ \kappa_m(\mu) = \kappa_m^0 \left[ \frac{C_2(R_m)}{C_2(R_m) + \mu^2/M_0^2} \right] }$$
where $\kappa_m^0 \equiv \kappa_m(\Lambda_{\text{GUT}})$ are the UV boundary values determined by the $E_7$ invariant structure.

---

## 4. IR Dominance Criterion & Crossover Scale

Define the running ratio:
$$\mathcal{R}(\mu) \equiv \frac{\kappa_3(\mu)}{\kappa_4(\mu)} = \mathcal{R}_0 \cdot \frac{C_2(\mathbf{56}) + \mu^2/M_0^2}{C_2(\mathbf{27}) + \mu^2/M_0^2}, \qquad \mathcal{R}_0 \equiv \frac{\kappa_3^0}{\kappa_4^0}.$$

### 4.1 Asymptotic Behavior
- **UV** ($\mu \gtrsim M_{\text{GUT}}$): $\mathcal{R}(\mu) \approx \mathcal{R}_0$. Quartic dominates if $\kappa_4^0 \gtrsim \kappa_3^0$ (expected from $E_7$ invariance).
- **IR** ($\mu \ll M_0\sqrt{C_2(\mathbf{27})}$): 
  $$\mathcal{R}(\mu) \approx \mathcal{R}_0 \cdot \frac{C_2(\mathbf{56})}{C_2(\mathbf{27})} \approx \mathcal{R}_0 \times 3.28.$$
  The cubic term is enhanced by a fixed geometric factor.

- **Intermediate Window** ($M_0\sqrt{C_2(\mathbf{27})} \ll \mu \ll M_0\sqrt{C_2(\mathbf{56})}$): 
  $$\mathcal{R}(\mu) \approx \mathcal{R}_0 \cdot \frac{C_2(\mathbf{56})}{\mu^2/M_0^2} \propto \mu^{-2}.$$
  Power-law enhancement drives $\kappa_3$ above $\kappa_4$ as $\mu$ decreases.

### 4.2 Crossover Scale $\mu_*$
The IR dominance threshold is defined by $\mathcal{R}(\mu_*) = 1$:
$$\boxed{ \mu_*^2 = M_0^2 \, \frac{C_2(\mathbf{56}) - \mathcal{R}_0 C_2(\mathbf{27})}{\mathcal{R}_0 - 1} }$$
For physical consistency we require $\mu_*^2 > 0$, which imposes:
$$\mathcal{R}_0 \in \left( \frac{C_2(\mathbf{27})}{C_2(\mathbf{56})}, \, 1 \right) \approx (0.30, \, 1).$$
If $\mu_*$ lies within the collective IR regime ($\mu_* \gg \ell_{\text{SP}}^{-1}$), the vacuum dynamically locks to $Z_3$ below $\mu_*$.

---

## 5. Physical Interpretation & $n=3$ Vortex Stability

1. **UV Baseline**: At $\mu \sim M_{\text{GUT}}$, the full $E_7$ symmetry is active. The quartic invariant $I_4$ sets the initial condition, typically $\kappa_4^0 \gtrsim \kappa_3^0$.
2. **Spectral Decoupling**: As $\mu$ flows downward, modes in the $\mathbf{56}$ sector (heavier by $\Delta C_2$) decouple faster than those in the $\mathbf{27}$ sector.
3. **IR Attractor**: The ratio $\mathcal{R}(\mu)$ grows monotonically. Once $\mu < \mu_*$, $\kappa_3 > \kappa_4$, and the effective potential minima lock to $\theta = 2\pi k/3$.
4. **Vortex Selection**: In the $Z_3$-locked vacuum, the energetically stable winding minimizes $E_n/N_{\text{sat}}(n)$ under $SU(8)$ antisymmetry, selecting $n=3$ as the global minimum. The Jackiw–Rebbi index then guarantees exactly three chiral zero modes.

---

## 6. Falsifiability & Computational Validation

| Condition | Mathematical Statement | Physical Consequence | Falsification Trigger |
|-----------|------------------------|----------------------|------------------------|
| **UV Consistency** | $\mathcal{R}_0 < 1$ | Quartic dominates at GUT scale | $\kappa_3^0 \geq \kappa_4^0$ |
| **Crossover Reality** | $\mu_*^2 > 0$ | Real transition scale exists | $\mu_*^2 \leq 0$ (no crossover) |
| **IR Accessibility** | $\mu_* \gg \ell_{\text{SP}}^{-1}$ | $Z_3$ phase reachable in collective regime | $\mu_* \lesssim \ell_{\text{SP}}^{-1}$ (quartic persists) |
| **Spectral Gap** | $\Delta C_2 > 0$ | Heavy modes decouple faster | $\Delta C_2 \leq 0$ (group theory violation) |

### Computational Path
1. **Lattice/Heat-Kernel**: Compute $\kappa_3(\mu), \kappa_4(\mu)$ numerically via spectral trace on $E_7/SU(8)$ discretization.
2. **Zero-Mode Solver**: Verify $\text{Ind}(\slashed{D}) = 3$ in the $Z_3$-locked background.
3. **Energy Minimization**: Confirm $E_3 < E_1, E_2, E_4$ under the running $\kappa_3(\mu), \kappa_4(\mu)$.

---

## 7. Integration into SPU Manuscript

- **Placement**: Insert as `Appendix D: IR Dominance Criterion & $Z_3$/$Z_4$ Crossover` or merge into `Chapter 6: Fermion Families & Flavor`.
- **Cross-References**: 
  - `Dynamic_Selection_n3_in_Z4_Medium.md` (energetic selection)
  - `spu_quartic_vacuum_Z4.md` (UV baseline)
  - `spu_fermion_families_zero_modes.md` (Jackiw–Rebbi counting)
- **Tone**: Conditional but structurally precise. Explicitly state that dominance requires $\mu_*$ to lie above the coherence length $\ell_{\text{SP}}$.
- **Next Step**: Upon numerical confirmation of $\mathcal{R}(\mu_*) > 1$, replace conditional language with definitive predictions and proceed to precision flavor phenomenology.

---

*Status:* Ready for inclusion in core SPU documentation.  
*Dependencies:* Spectral action formalism, $E_7 \to E_6 \times U(1)$ branching rules, Casimir normalization conventions.  
*Falsification Protocol:* Strictly enforced per Section 6.