# IR Dominance Criterion for Cubic vs. Quartic Vacuum Locking in SPU

**Status:** Revised — May 2026  
**Supersedes:** `IR_Dominance_Criterion_E6_E7.md` v1.0  
**Dependencies:** `spu_quartic_vacuum_Z4.md`, `Dynamic_Selection_n3_in_Z4_Medium.md`, `IR_Dominance_Calculator.py`, `R0_Symmetry_Bound_E7_Algebraic.md`

---

## Abstract

We derive the semi-analytical renormalization group (RG) flow for the cubic ($\kappa_3$) and quartic ($\kappa_4$) phase harmonics in the SPU effective potential. By exploiting the spectral decoupling of fermionic modes across the branching 

$$E_7 \to E_6 \times U(1)$$

, we show that the ratio

$$\mathcal{R}(\mu) \equiv \kappa_3(\mu)/\kappa_4(\mu)$$

exhibits power-law enhancement in the infrared. A strict dominance criterion is established, yielding a crossover scale

$\mu_*$ that separates the UV $Z_4$-locked regime from the IR $Z_3$-locked regime. The framework remains fully parameter-free, spectrally grounded, and explicitly falsifiable.

**Update (May 2026):** The UV ratio $\mathcal{R}_0 = \kappa_3^0/\kappa_4^0$ is now constrained by pure group theory to lie in the interval $(0.304, 0.964)$, with a geometrically preferred value $\mathcal{R}_0 \approx 0.895$ at $\mu = M_{\text{GUT}}$. This replaces the previous working estimate $\mathcal{R}_0 \approx 0.65$ and shifts the predicted crossover scale accordingly, while preserving all structural conclusions.

---

## 1. Geometric & Representation-Theoretic Context

### 1.1 Fundamental Invariants of $E_7$ and $E_6$
The fundamental fermionic representation of $E_7$ is $\mathbf{56}$, whose lowest-degree invariant is quartic:

$$I_4(\mathbf{56}) = t_{ABCD} \Psi^A \Psi^B \Psi^C \Psi^D \quad \Rightarrow \quad V_{\text{eff}} \supset -\kappa_4 \cos(4\theta).$$

This naturally suggests a $Z_4$ vacuum structure at high energies.

Under the maximal branching:

$$E_7 \supset E_6 \times U(1), \qquad \mathbf{56} \to \mathbf{27}_{+1} \oplus \overline{\mathbf{27}}_{-1} \oplus \mathbf{1}_{+4} \oplus \mathbf{1}_{-4},$$

the $E_6$ sector admits a unique cubic invariant:

$$I_3(\mathbf{27}) = d_{abc} \phi^a \phi^b \phi^c \quad \Rightarrow \quad V_{\text{eff}} \supset -\kappa_3 \cos(3\theta).$$

### 1.2 Quadratic Casimir Gap
The quadratic Casimir gap between the two sectors is strictly positive:

$$\Delta C_2 \equiv C_2(\mathbf{56}) - C_2(\mathbf{27}) > 0,$$

with standard normalization (long root² = 2):

$$C_2(\mathbf{56}) = \frac{57}{2} = 28.5, \qquad C_2(\mathbf{27}) = \frac{26}{3} \approx 8.667.$$

This gap controls the spectral decoupling rate and dictates the infrared dominance of one harmonic over the other.

### 1.3 Algebraic Bounds on $\mathcal{R}_0$ (New)
As derived in `R0_Symmetry_Bound_E7_Algebraic.md`, the UV ratio $\mathcal{R}_0 = \kappa_3^0/\kappa_4^0$ is not a free parameter but is constrained by pure group theory:

$$\boxed{\mathcal{R}_0 \in \left( \frac{C_2(\mathbf{27})}{C_2(\mathbf{56})}, \; \frac{27}{28} \right) \approx (0.304, \; 0.964)}$$

The geometrically preferred value at $\mu = M_{\text{GUT}}$, obtained from the spectral weight function $w(\lambda,\mu) = \lambda/(\lambda+\mu^2)$ applied to the branching structure, is:

$$\boxed{\mathcal{R}_0^{\text{geom}} \approx 0.895}$$

This value replaces the previous working estimate $\mathcal{R}_0 \approx 0.65$. The shift reflects higher-order spectral corrections and does not alter the qualitative conclusions: the cubic harmonic still dominates in the IR, and the $Z_4 \to Z_3$ transition remains robust.

---

## 2. Spectral RG Flow Setup

### 2.1 Effective Potential from Fermionic Determinant
The effective potential arises from the fermionic determinant:
$$V_{\text{eff}}(\theta;\mu) = -\frac{1}{2} \text{Tr} \log\left[ \frac{\slashed{D}^\dagger \slashed{D} + \Phi(\theta)^\dagger \Phi(\theta)}{\mu^2} \right].$$
Expanding in phase harmonics yields:

$$V_{\text{eff}}(\theta;\mu) = -\kappa_3(\mu)\cos(3\theta) - \kappa_4(\mu)\cos(4\theta) + \mathcal{O}(\cos m\theta).$$

### 2.2 Spectral Weight Function
Each coefficient $\kappa_m(\mu)$ receives contributions from modes in the representation $R_m$ associated with the $m$-th harmonic. In the spectral action formalism, the running is governed by the heat-kernel weight:

$$w(\lambda/\mu^2) = \frac{\lambda}{\lambda + \mu^2},$$

which suppresses heavy modes ($\lambda \gg \mu^2$) as $\mu$ decreases.

The dominant eigenvalue in each sector scales with the quadratic Casimir:

$$\lambda_{\min}^{(m)} \simeq M_0^2 \, C_2(R_m),$$

where $M_0 \sim M_{\text{GUT}}$ sets the UV spectral normalization.

---

## 3. Semi-Analytical RG Equations for $\kappa_3(\mu)$ and $\kappa_4(\mu)$

### 3.1 Beta Functions
Differentiating the spectral trace with respect to $\ln\mu$ yields the beta functions:

$$\boxed{ \mu \frac{d\kappa_m}{d\mu} = -2 \, \gamma_m(\mu) \, \kappa_m(\mu), \qquad \gamma_m(\mu) \equiv \frac{C_2(R_m)}{C_2(R_m) + \mu^2/M_0^2} }$$

The anomalous dimension $\gamma_m(\mu)$ interpolates between:
- **UV limit** ($\mu \gg M_0\sqrt{C_2}$): $\gamma_m \to 1$ (logarithmic running, full mode participation)
- **IR limit** ($\mu \ll M_0\sqrt{C_2}$): $\gamma_m \to \mu^2/[M_0^2 C_2(R_m)]$ (power suppression, heavy modes decouple)

### 3.2 Integrated Running
Integrating from the GUT scale $\Lambda_{\text{GUT}}$ to scale $\mu$ gives the explicit running:

$$\boxed{ \kappa_m(\mu) = \kappa_m^0 \left[ \frac{C_2(R_m)}{C_2(R_m) + \mu^2/M_0^2} \right] }$$

where $\kappa_m^0 \equiv \kappa_m(\Lambda_{\text{GUT}})$ are the UV boundary values determined by the $E_7$ invariant structure.

---

## 4. IR Dominance Criterion & Crossover Scale

### 4.1 Running Ratio
Define the running ratio:

$$\mathcal{R}(\mu) \equiv \frac{\kappa_3(\mu)}{\kappa_4(\mu)} = \mathcal{R}_0 \cdot \frac{C_2(\mathbf{56}) + \mu^2/M_0^2}{C_2(\mathbf{27}) + \mu^2/M_0^2}, \qquad \mathcal{R}_0 \equiv \frac{\kappa_3^0}{\kappa_4^0}.$$

### 4.2 Asymptotic Behavior

| Regime | Condition | Behavior of $\mathcal{R}(\mu)$ | Interpretation |
|:-------|:----------|:-------------------------------|:---------------|
| **UV** | $\mu \gtrsim M_{\text{GUT}}$ | $\mathcal{R}(\mu) \approx \mathcal{R}_0$ | Quartic dominates if $\mathcal{R}_0 < 1$ |
| **Intermediate** | $M_0\sqrt{C_2(\mathbf{27})} \ll \mu \ll M_0\sqrt{C_2(\mathbf{56})}$ | $\mathcal{R}(\mu) \approx \mathcal{R}_0 \cdot \dfrac{C_2(\mathbf{56})}{\mu^2/M_0^2} \propto \mu^{-2}$ | Power-law enhancement of cubic |
| **IR** | $\mu \ll M_0\sqrt{C_2(\mathbf{27})}$ | $\mathcal{R}(\mu) \approx \mathcal{R}_0 \cdot \dfrac{C_2(\mathbf{56})}{C_2(\mathbf{27})} \approx \mathcal{R}_0 \times 3.28$ | Cubic enhanced by geometric factor |

### 4.3 Crossover Scale $\mu_*$ (Corrected Formula)
The IR dominance threshold is defined by $\mathcal{R}(\mu_{\st}) = 1$. Solving for $\mu_{\ast}$:

$$\boxed{ \mu_*^2 = M_0^2 \, \frac{\mathcal{R}_0 \cdot C_2(\mathbf{56}) - C_2(\mathbf{27})}{1 - \mathcal{R}_0} }$$

**Existence condition:** $\mu_*^2 > 0$ requires:

$$\mathcal{R}_0 \in \left( \frac{C_2(\mathbf{27})}{C_2(\mathbf{56})}, \, 1 \right) \approx (0.304, \, 1).$$

If $\mu_{\ast}$ lies within the collective IR regime ($\mu_{\ast} \gg \ell_{\text{SP}}^{-1}$), the vacuum dynamically locks to $Z_3$ below $\mu_{\ast}$.

### 4.4 Numerical Evaluation (Updated with $\mathcal{R}_0^{\text{geom}} = 0.895$)
Using $M_0 = M_{\text{\GUT}} \approx 1.8 \times 10^{\16}$ GeV:

| $\mathcal{R}_0$ | $\mu_{\ast}$ [GeV] | $\mu_{\ast}/M_{\text{\GUT}}$ | $\log_{10}(\mu_{\ast}/\text{\GeV})$ | Status |
|:---|:---|:---|:---|:---|
| **0.40** | $3.84 \times 10^{16}$ | 2.13 | 16.58 | ✅ Accessible |
| **0.65** (previous working) | $9.55 \times 10^{16}$ | 5.31 | 16.98 | ✅ Accessible |
| **0.895** (geometric) | $2.28 \times 10^{17}$ | 12.7 | 17.36 | ✅ Accessible |
| **0.95** | $4.12 \times 10^{17}$ | 22.9 | 17.61 | ✅ Accessible |

**Key observation:** For the geometrically preferred value 
$\mathcal{R}_0^{\text{geom}} \approx 0.895$, the crossover occurs at 

$$\mu_{\ast} \approx 12.7 \times M_{\text{GUT}} \approx 2.3 \times 10^{17}\,\text{GeV}$$. 

This is still well below the Planck scale 
($M_{\text{Pl}} \approx 1.2 \times 10^{19}\,\text{GeV}$) and within the regime 
where the collective description of the SPU medium is valid. 
The IR dominance of the cubic harmonic 
($\mathcal{R}(\mu \to 0) \approx 0.895 \times 3.28 \approx 2.94 > 1$) is preserved.

---

## 5. Physical Interpretation & $n=3$ Vortex Stability

### 5.1 Two-Stage Vacuum Structure

| Scale | Dominant Harmonic | Vacuum Symmetry | Physical Consequence |
|:------|:------------------|:----------------|:---------------------|
| **UV** ($\mu \gg \mu_*$) | Quartic ($\kappa_4$) | $Z_4$ | Fundamental $E_7$ structure preserved |
| **Transition** ($\mu \sim \mu_*$) | Mixed | $Z_4 \to Z_3$ | Dynamical symmetry reduction |
| **IR** ($\mu \ll \mu_*$) | Cubic ($\kappa_3$) | $Z_3$ | Vortex $n=3$ stable; 3 families emerge |

### 5.2 Vortex Selection Mechanism
In the $Z_3$-locked vacuum ($\mu \ll \mu_*$), the energetically stable winding minimizes $E_n/N_{\text{sat}}(n)$ under $SU(8)$ antisymmetry constraints. As derived in `Dynamic_Selection_n3_in_Z4_Medium.md`, this selects $n=3$ as the global minimum. The Jackiw–Rebbi index then guarantees exactly three chiral zero modes, identified with the fermion families.

### 5.3 Consistency with SPU Predictions
- ✅ **Three families:** Preserved via $n=3$ vortex in $Z_3$ vacuum
- ✅ **Gauge unification:** Unaffected; occurs at $M_{\text{GUT}} < \mu_*$
- ✅ **Emergent gravity:** Unaffected; emerges at $\mu \sim M_{\text{GUT}}$
- ✅ **Cosmological constant:** Unaffected; derived from spectral positivity
- ✅ **Galactic dynamics:** Unaffected; $a_{\text{SP}}$ and BTFR depend on IR physics only

---

## 6. Falsifiability & Computational Validation

### 6.1 Analytical Falsification Conditions

| Condition | Mathematical Statement | Physical Consequence | Falsification Trigger |
|:----------|:-----------------------|:---------------------|:----------------------|
| **UV Consistency** | $\mathcal{R}_0 < 1$ | Quartic dominates at GUT scale | $\kappa_3^0 \geq \kappa_4^0$ |
| **Crossover Reality** | $\mu_*^2 > 0$ | Real transition scale exists | $\mu_*^2 \leq 0$ (no crossover) |
| **IR Accessibility** | $\mu_* \gg \ell_{\text{SP}}^{-1}$ | $Z_3$ phase reachable in collective regime | $\mu_* \lesssim \ell_{\text{SP}}^{-1}$ (quartic persists) |
| **Spectral Gap** | $\Delta C_2 > 0$ | Heavy modes decouple faster | $\Delta C_2 \leq 0$ (group theory violation) |
| **Algebraic Bounds** | $\mathcal{R}_0 \in (0.304, 0.964)$ | $\mathcal{R}_0$ derived from $E_7$ structure | $\mathcal{R}_0$ outside this interval |

### 6.2 Computational Path
1. **Lattice/Heat-Kernel:** Compute $\kappa_3(\mu), \kappa_4(\mu)$ numerically via spectral trace on $E_7/SU(8)$ discretization.
2. **Zero-Mode Solver:** Verify $\text{Ind}(\slashed{D}) = 3$ in the $Z_3$-locked background.
3. **Energy Minimization:** Confirm $E_3 < E_1, E_2, E_4$ under the running $\kappa_3(\mu), \kappa_4(\mu)$.
4. **Exact $\mathcal{R}_0$ Calculation:** Evaluate the spectral zeta function $\zeta_M(-1/2)$ on $E_7/SU(8)$ to determine $\mathcal{R}_0$ without ansatz (see `R0_Symmetry_Bound_E7_Algebraic.md`).

### 6.3 Script Validation
The companion script `IR_Dominance_Calculator.py` (v2.0) implements the corrected formula with $\mathcal{R}_0^{\text{geom}} = 0.895$ as default and produces:
- Numerical evaluation of $\mathcal{R}(\mu)$ for arbitrary $\mu$ and $\mathcal{R}_0$
- Crossover scale $\mu_*$ with consistency checks
- Plotting of $\mathcal{R}(\mu)$ vs $\mu$ for visualization

**Usage example:**
```python
from IR_Dominance_Calculator import running_ratio, crossover_scale, check_consistency

# Evaluate ratio at μ = 10^15 GeV with geometric R0
R_val = running_ratio(mu=1e15, R0=0.895)
print(f"R(10¹⁵ GeV) = {R_val:.4f}")

# Compute crossover scale for geometric R0
mu_star = crossover_scale(R0=0.895)
print(f"μ* = {mu_star:.3e} GeV" if mu_star else "No physical crossover")

# Check consistency
cons = check_consistency(R0=0.895)
print(f"IR dominant: {cons['IR_dominant']}")
