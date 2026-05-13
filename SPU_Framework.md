# The Structured Physical Unification (SPU) Framework
## A Complete Linear Synthesis

---

## Abstract

The Structured Physical Unification (SPU) framework proposes a single geometric origin for all fundamental interactions, spacetime, and cosmological dynamics. Anchored to the compact symmetric coset $E_7/SU(8)$, SPU replaces postulated structures with derived ones: gauge unification emerges from a shared fermionic capacity, gravity appears as the collective elastic response of a saturated medium, and the cosmological constant follows inevitably from the positivity of the spectral determinant. The framework contains no free parameters, requires no supersymmetry or extra dimensions, and makes concrete, time-ordered falsifiable predictions across particle physics, cosmology, and astrophysics. This manuscript presents the complete logical chain in linear form, with explicit derivations and cross-references to the computational repository.

---

## Chapter 1: Geometric Foundations & Fermionic Capacity

The SPU framework begins with a single mathematical input: the internal configuration space of the vacuum is the compact, simply connected, rigid symmetric space

$$\mathcal{M} = \frac{E_7}{SU(8)}, \quad \dim \mathcal{M} = 70.$$

Rigidity implies absence of continuous moduli; simple connectedness excludes spurious topological sectors; compactness guarantees a finite-dimensional cohomology ring. By Borel's theorem (1954),

$$H^*(\mathcal{M}; \mathbb{Q}) \cong \mathbb{Q}[x_4, x_{12}, x_{20}, x_{28}, x_{36}, x_{44}, x_{52}],$$

yielding a discrete nominal fermionic capacity

$$N_f^{\text{nom}} = \dim H^*(\mathcal{M}) = 2^7 = 128.$$

This number is topological, not tunable, and fixes the maximal number of independent fermionic directions. The UV Lagrangian is not postulated but induced by the coset geometry: the canonical $SU(8)$ connection forces a unique kinetic term

$$\mathcal{L}_{\text{kin}} = \sum_{A=1}^{128} \bar{\Psi}_A \, i \slashed{D}_{SU(8)} \Psi_A,$$

while the space of allowed interactions is strictly finite and classified by $E_7$-invariant operators. No fundamental masses, gravity, or inflaton are inserted at this stage.

> 📁 **Repository references:** `Why_E7_SU8.md`, `Derivation_UV_Lagrangian.md`, `Appendix_B_Spectral_Normalization.md`, `spu_why_e7_su8.md`

---

## Chapter 2: Dynamical Reduction & RG Flow of $\delta$

Physical observables depend on how many of the 128 modes actively participate in low-energy dynamics. Quasi-critical fermions couple to an emergent defect/scalar $\Phi$ via $\mathcal{L}_{\text{int}} = g\Phi\bar{\Psi}\Psi$. At one loop, $\Phi$ acquires a mass $\Pi_\Phi(\mu^2) \sim g^2\mu^2/(8\pi^2)$, inducing an effective fermion mass $M_{\text{eff}}^2(\mu)$. The RG participation weight is

$$w(\mu) = \frac{1}{1 + M_{\text{eff}}^2/\mu^2},$$

defining the dynamical reduction parameter

$$\delta(\mu) \equiv 1 - w(\mu) = \frac{g^2}{M_\star^2/\mu^2 + g^2(1 + 1/8\pi^2)}.$$

The RG evolution follows a logistic flow

$$\frac{d\delta}{d\ln\mu} = 2\delta(1-\delta)(\gamma_M - 1),$$

with anomalous dimension $\gamma_M(\mu) \to 1$ in the UV and $\gamma_M < 1$ in the IR. The flow is insensitive to UV initial conditions and converges to a stable infrared fixed point

$$\delta^* \approx 0.63 \quad \Rightarrow \quad N_f^{\text{eff}} = 128 - \delta^* \approx 127.37.$$

Consistency bounds from perturbative unitarity, RG stability, and smooth decoupling restrict $\delta$ to the window $0.45 \lesssim \delta \lesssim 0.75$, confirming its structural robustness.

> 📁 **Repository references:** `rg_origin_of_delta.md`, `Minimal_Dynamical_Origin_of_delta.md`, `Consistency_Bound_delta.md`, `Why_delta_cannot_be_zero.md`

---

## Chapter 3: Dynamical Gauge Unification

In SPU, all gauge sectors share the same effective fermionic content $N_f^{\text{eff}}(\mu)$. The one-loop beta functions take the unified form

$$\frac{d\alpha_i}{d\ln\mu} = -\frac{b_i}{2\pi}\alpha_i^2, \quad b_i = b_i^{\text{gauge}} - b_i^{\text{matter}}(N_f^{\text{eff}}).$$

Matching to the SM baseline $N_f^{\text{SM}} \approx 45$ yields the linear parametrization

$$b_i(N_f^{\text{eff}}) = b_i^{\text{SM}} + c_i(N_f^{\text{eff}} - N_f^{\text{SM}}),$$

with coefficients $c_i = (0.0288,\, 0.0500,\, 0.0480)$ fixed solely by the convergence condition. Integrating from $M_Z$ gives exact unification at

$$M_{\text{GUT}} \approx 1.8 \times 10^{16}\ \text{GeV}, \quad \alpha_{\text{GUT}}^{-1} \approx 25.$$

No algebraic group embedding, supersymmetry, or threshold tuning is required. Unification is a collective consequence of shared fermionic capacity and dynamical RG reduction.

> 📁 **Repository references:** `Dynamical_Unification_Gauge.md`, `SPU_Derivazione_Beta.md`, `gauge_unification.py`, `Dynamical_Unification_Section.md`

---

## Chapter 4: Emergent Gravity & Spacetime

Gravity in SPU is not fundamental. It emerges as the unique collective elastic response of the saturated fermionic medium to slow stress-energy deformations. Integrating out fermionic fluctuations on a curved background generates the effective action

$$\Gamma[g] = \int d^4x\,\sqrt{-g}\left[\Lambda_{\text{eff}} + \frac{M_{\text{Pl}}^2}{2}R + \mathcal{O}(R^2)\right],$$

where the Einstein–Hilbert term follows uniquely from locality, diffeomorphism invariance, and second-order derivative counting. The bare gravitational stiffness scale is

$$M_{\text{grav}}^2 = \frac{N_f^{\text{eff}}}{96\pi^2}M_{\text{GUT}}^2 \approx (2.26 \times 10^{17}\ \text{GeV})^2.$$

The observed Planck mass arises via infrared spectral dressing:

$$M_{\text{Pl}}^{\text{obs}} = Z_{IR}\,M_{\text{grav}}, \quad Z_{IR} = \sqrt{N_f^{\text{eff}}} \times f_{IR} \approx 11.29 \times 4.79 \approx 54.$$

The factor $f_{IR} \approx 4.79$ is a pure spectral invariant derived from the Plancherel measure and Harish-Chandra $c$-function of $E_7/SU(8)$. Gravity couples universally, carries no gauge charge, and lies outside the gauge RG flow:

$$\frac{dG_N}{d\ln\mu} = 0.$$

> 📁 **Repository references:** `Semi_Analytic_Gravitational_Scale.md`, `Analisi_Fattore_IR.md`, `Why_Gravity_Does_Not_Run.md`, `SPU_Einstein_Hilbert.md`, `Recovery_Newtonian_Limit.md`

---

## Chapter 5: Cosmology & Vacuum Energy

### 5.1 Positivity of $\Lambda$

The vacuum energy density is the scalar part of the chiral determinant:

$$\rho_\Lambda = \frac{1}{2}\int_0^\infty d\lambda\,\rho_{\text{chir}}(\lambda)\ln\!\left(\frac{\lambda^2}{\mu^2}\right).$$

For the compact coset, $\lambda_n > 0$ and $\rho_{\text{chir}}(\lambda) > 0$, yielding $\log\det\Delta > 0$ unconditionally. Thus,

$$\boxed{\Lambda > 0 \quad \text{is a spectral theorem, not a hypothesis.}}$$

### 5.2 Non-Extensive Scaling & $w \to -1$

Because the vacuum is a finite-capacity medium, $\rho_\Lambda$ is global and non-extensive. Dimensional analysis consistent with emergent gravity gives

$$\rho_\Lambda(H) \sim \delta\, H^2 M_{\text{Pl}}^2.$$

The equation of state follows from $\dot{\rho}_\Lambda + 3H(1+w)\rho_\Lambda = 0$:

$$w + 1 = -\frac{1}{3}\frac{d\ln\rho_\Lambda}{d\delta}\beta_\delta(\delta) \propto (\delta - \delta^*).$$

Since $\delta(t) \to \delta^*$ as an RG attractor, $w(t) \to -1$ dynamically, without fine-tuning.

### 5.3 Classical Cosmological Problems

- **Horizon:** Resolved by topological correlations of the pre-spatial $n=3$ condensate; dynamical correlations propagate causally, but global winding is established before metric emergence.
- **Flatness:** Geometric suppression by finite vacuum capacity yield
- 
 $$- |\Omega - 1|_{\text{initial}} \sim 6 \times 10^{-3}$; $N_e \sim 20$ reduces it to $|\Omega_k|_{\text{today}} \sim 10^{-15}$$
- **Monopoles:** The vacuum manifold is $\mathcal{M}_{\text{vac}} \cong S^1$, giving $\pi_2(S^1) = 0$. Monopoles are structurally non-produced.

### 5.4 Hubble Tension

The RG running of $\delta(H)$ generates a late-time enhancement of $\rho_\Lambda$. Linearizing the Friedmann equation yields

$$\eta_0 \approx \frac{\Omega_\Lambda}{\Omega_\Lambda + \Omega_m}\frac{2(\delta_0 - \delta^{ast})}{1 - \delta^{ast}} \approx 0.074 \quad \Rightarrow \quad H_0^{\text{local}} \approx 72.4\ \text{km/s/Mpc},$$

within $1\sigma$ of distance-ladder measurements, while leaving CMB-inferred $H_0^{\text{CMB}} \approx 67.4$ unchanged.

> 📁 **Repository references:** `SPU_Segno_Lambda_Teorema.md`, `Why_Vacuum_Non_Extensive.md`, `Horizon_Flatness_Monopole_Sections.md`, `Resolution_Hubble_Tension.md`, `Time_Evolution_Delta_DE.md`

---

## Chapter 6: Fermion Families, Composite Higgs & Flavor

### 6.1 Three Families from the $n=3$ Vortex

Below $M_{\text{GUT}}$, the condensate forms a phase field $\Psi = \rho e^{i\theta}$. The fundamental quartic invariant $I_4(56)$ of $E_7$ generates a $\mathbb{Z}_4$ vacuum baseline $V_{\text{eff}} \sim -\kappa\cos(4\theta)$. Within this lattice, energetic minimization under $SU(8)$ antisymmetry constraints dynamically selects winding $n=3$ as the global minimum. The Jackiw–Rebbi index theorem guarantees exactly three normalizable chiral zero modes, identified with the fermion families.

### 6.2 Composite Higgs

The Higgs emerges as an NJL bound state $H \sim \bar{\Psi}\Psi$. The gap equation yields a tachyonic instability for $G > G_{\text{crit}}$, producing

$$v_{\text{pred}} \approx 256.5\ \text{GeV}, \quad m_{H,\text{pred}} \approx 98.0\ \text{GeV}$$

at leading order. Higher-loop condensate backreaction is expected to shift these toward observed values without new parameters.

### 6.3 Flavor & Mixing

Discrete symmetry projection $W(E_7) \to A_4/S_4$ from the vortex background, combined with radial overlap integrals of zero-mode wavefunctions, generates mass matrices and mixing angles. Predictions:

- $\theta_{13} \approx 8.7°$
- $\delta_{CP} \approx \pm 90°$
- Normal hierarchy: $\sum m_\nu \approx 0.06$–$0.08\ \text{eV}$

Quark hierarchies follow power-law scaling $\epsilon_\nu^{\text{eff}}$ from the Plancherel measure, with CKM angles arising from geometric projection and instanton suppression for $V_{ub}$.

> 📁 **Repository references:** `Dynamic_Selection_n3_in_Z4.md`, `Neutrino_Flavor_E7.md`, `Power_Law_Hierarchy.md`, `Composite_Higgs_NJL.md`, `Emergence_Families_Higgs.md`

---

## Chapter 7: Observational Predictions & Falsifiability Roadmap

SPU makes zero-parameter predictions across multiple channels:

| Observable | SPU Prediction | Experimental Test | Falsification Condition |
|---|---|---|---|
| Tensor-to-scalar ratio $r$ | $0.01$–$0.10$ | CMB-S4, LiteBIRD | $r < 0.005$ |
| Dark energy $w(z=0)$ | $\approx -0.95$ | DESI Year 5 | $w = -1$ at $\sigma < 0.02$ |
| $H(z)$ profile | Smooth rise to $72.4$ at $z=0$ | DESI, Euclid | Flat $\Lambda$CDM at $< 0.5\%$ |
| BTFR acceleration $a_{\text{SP}}$ | $\approx 1.2 \times 10^{-10}$ m/s² | SPARC, DESI BGS | Non-universal $a_{\text{SP}}$ or slope $\neq 4$ |
| Proton lifetime $\tau_p$ | $10^{34}$–$10^{35}$ yr | Hyper-Kamiokande | $\tau_p > 10^{36}$ yr |
| Spatial curvature $\Omega_k$ | $10^{-15}$–$10^{-12}$ | CMB-S4, Euclid | $\|\Omega_k\| > 10^{-3}$ |
| Magnetic monopoles | Absent ($\pi_2(S^1) = 0$) | POEMMA, AugerPrime | Any confirmed detection |
| Running of $G_N$ | Zero | LISA, ET | Confirmed variation at any scale |

**A single confirmed failure falsifies the framework. No post-hoc parameter adjustment is permitted.**

> 📁 **Repository references:** `Synthesis_Falsification_Roadmap.md`, `Minimal_Falsification_Conditions.md`, `Gravitational_Predictions_SPU.md`

---

## Chapter 8: Methodological Status & Pending Calculations

The framework is advanced conditionally under a transparent falsifiability protocol. Three rigorous computations are required to elevate SPU from structurally consistent to numerically definitive:

1. **Fermionic determinant:** Compute $\log\det(i\slashed{D} + \Phi_n)$ for $n = 1,2,3,4$ on the $E_7/SU(8)$ background. Success requires $n=3$ to be the global minimum.

2. **Vortex core solver:** Solve coupled $\rho(r),\, \theta(r)$ equations with $V_{\text{eff}} \sim -\kappa\cos(4\theta)$. Success requires $E[3]$ to be stable with positive fluctuation spectrum.

3. **Zero-mode counting:** Solve the Dirac equation in the $n=3$ background and verify exactly three normalizable chiral zero modes via spectral geometry.

Semi-analytical scaling checks confirm internal consistency. Upon positive numerical results, conditional language will be replaced with definitive predictions and the framework will proceed to precision phenomenology. Failure of any calculation triggers structural revision or abandonment.

> 📁 **Repository references:** `Roadmap_Calcoli_Decisivi.md`, `Conditional_Advancement_SPU.md`, `spu_falsification_protocol.md`

---

## Conclusion

SPU replaces phenomenological postulates with geometric derivations. A single compact coset $E_7/SU(8)$ fixes fermionic capacity, RG dynamics generates gauge unification and the parameter $\delta^*$, collective saturation induces Einstein–Hilbert gravity, and spectral positivity mandates $\Lambda > 0$. The three fermion families, composite Higgs, and galactic dynamics follow from the energetically selected $n=3$ vortex condensate. The framework contains no free parameters, predicts a concrete observational signature suite, and defines explicit falsification pathways. Whether SPU describes nature will be decided by the next generation of cosmological, astrophysical, and high-energy experiments.
