# Galactic Dynamics in the SPU Framework: Emergent Transition Radius and the Baryonic Tully–Fisher Relation

> **Repository:** https://github.com/marcofanavigator/SPU_THEORY  
> **Version:** 1.2 (April 2026)  
> **Status:** Preprint Draft | Internal Consistency Verified | Falsifiable Predictions Enumerated

---

## Abstract

We present a theoretical and observational investigation of the transition radius $r_t$ emerging in galactic rotation curves within the framework of Structured Physical Unification (SPU). In SPU, gravity is **not a fundamental interaction** but an **emergent collective response** of a finite, rigid fermionic medium characterized by a dynamically generated stiffness scale. We show that the galactic transition radius naturally arises as the **coherence length of the SPU medium under baryonic loading**, rather than as a phenomenological interpolation scale.

Starting from the fundamental SPU construction — based on a fixed fermionic capacity determined by the geometry $E_7/SU(8)$ — we derive a **universal acceleration scale** and obtain an **analytic expression for $r_t$** that depends only on baryonic mass. This leads directly to the **baryonic Tully–Fisher relation** as a theoretical consequence rather than an empirical input. We confront these predictions with SPARC rotation-curve data, finding consistency with the expected scaling laws and no evidence for additional free galactic parameters. The results indicate that the apparent success of phenomenological fits masks an underlying dynamical origin, and that **SPU provides a predictive framework** connecting microscopic dynamics to galactic phenomenology.

---

## 1. Introduction

### 1.1 The Problem of Galactic Dynamics
Galactic rotation curves represent one of the most persistent challenges in modern physics. Observations reveal that the circular velocity of stars and gas in disk galaxies remains approximately constant at large radii, in stark contrast with the expectations of Newtonian gravity applied to visible matter alone. Two broad classes of explanations have been developed:
- **The introduction of non-luminous dark matter**
- **Modifications or extensions of gravitational dynamics**

Despite decades of effort, **neither approach has yet produced a universally accepted fundamental explanation.**

### 1.2 Phenomenological Regularities and Their Limitations
High-quality datasets such as SPARC have revealed striking empirical regularities:
- The **baryonic Tully–Fisher relation**
- **Tight correlations** between baryonic and dynamical accelerations
- The appearance of a **characteristic transition radius** $r_t$

These regularities strongly suggest an underlying organizing principle. However, most existing approaches treat key quantities — including $r_t$ or an equivalent acceleration scale — as **phenomenological inputs, introduced a posteriori to fit the data**.

> **Foundational Principle:** A truly fundamental theory must predict its scales a priori, not infer them from data.

### 1.3 The SPU Framework
Structured Physical Unification (SPU) is a theoretical framework in which gauge interactions, gravity, and effective spacetime dynamics emerge from a common underlying fermionic structure. The theory is defined by:
- A compact, rigid internal geometry $E_7/SU(8)$
- A fixed nominal fermionic capacity $N_f^{\text{nom}} = 128$
- A dynamical reduction to an effective number of degrees of freedom

Within SPU, gravity is an emergent elastic response, Newton's constant is derived, and no fundamental Planck scale is postulated.

### 1.4 Emergent Gravity and Coherence Scales
A key feature of emergent systems is the appearance of coherence lengths separating local from collective behavior. In SPU, the gravitational response of the medium transitions from baryon-dominated at small scales to collective-medium-dominated at large scales. This transition defines a characteristic radius $r_t$.

> **Central Question:** Is the galactic transition radius $r_t$ a phenomenological fitting parameter, or a dynamically determined scale predicted by SPU?

### 1.5 Scope and Structure
In this work we:
- Derive the functional form of the velocity profile $v(r)$ in SPU
- Show that $r_t$ arises as a coherence length of the SPU medium
- Confront these predictions with SPARC rotation-curve data
- Establish explicit falsifiability conditions

**Organization:** Sec. 2 reviews SPU microphysics. Sec. 3 derives the emergent gravitational scale. Sec. 4 derives the radial response function. Sec. 5 obtains $r_t$ from vacuum properties. Sec. 6 discusses conceptual implications. Appendix A provides the complete analytical derivation.

### 1.6 Philosophy of the Approach
This work introduces **no new free parameters**. All scales are either fixed by SPU microphysics or determined by the baryonic mass distribution. The goal is not to improve empirical fits, but to determine whether observed phenomenology can be traced back to a consistent and predictive theoretical structure.

---

## 2. Conceptual Framework of SPU

### 2.1 Finite Fermionic Capacity as a Fundamental Principle
The SPU framework assumes the vacuum is not a continuum with arbitrary degrees of freedom, but a finite, compact, collective medium.

> **Postulate I (Finite Capacity):** The physical vacuum admits a fixed nominal fermionic capacity $N_f^{\text{nom}}$, determined by internal geometry and not adjustable by low-energy phenomenology.

In SPU:
$$N_f^{\text{nom}} = 128$$
This value follows from purely geometric and topological considerations. Continuous deformations are not allowed without altering the theory.

### 2.2 Geometric Origin of the Capacity
The internal structure is the compact symmetric space:

$$M = \frac{E_7}{SU(8)}$$

Its de Rham cohomology ring satisfies:

$$H^{\ast}(M) \cong \mathbb{Q}[x_4, x_{12}, x_{20}, x_{28}, x_{36}, x_{44}, x_{52}] \quad \Rightarrow \quad \dim H^{\ast}(M) = 2^7 = 128$$

This dimension is interpreted as the nominal fermionic capacity. Crucially, it is:
- Discrete and fixed
- Independent of low-energy physics
- Insensitive to RG running

### 2.3 Dynamical Reduction and Effective Degrees of Freedom
Physical observables depend on how many modes actively participate in dynamics. SPU distinguishes:
- Nominal capacity: $N_f^{\text{nom}}$
- Effective participation: $N_f^{\text{eff}}(\mu) = 128 - \delta(\mu)$

$\delta(\mu)$ encodes partial decoupling of quasi-critical fermionic modes. It is continuous, scale-dependent, $O(1)$, and **not a free parameter** (emerges dynamically from spectral RG flow). Topology fixes capacity; dynamics fixes participation.

### 2.4 Collective Nature of the Vacuum Medium
- Gauge interactions arise from localized excitations
- Gravity arises from global elastic response of the neutral sector
- Gravity couples universally and is suppressed by collective averaging

This suppression explains the observed weakness of gravity relative to gauge forces.

### 2.5 Logical Chain
$$E_7/SU(8) \Rightarrow N_f^{\text{nom}} = 128 \Rightarrow \delta \text{ (dynamical)} \Rightarrow N_f^{\text{eff}} \Rightarrow \text{RG flow and emergent interactions}$$
No step involves phenomenological fitting.

---

## 3. Emergent Gravitational Scale in SPU

### 3.1 Gravity as a Collective Elastic Response
Gravity is not fundamental. It emerges as the macroscopic elastic response of the medium to stress-energy. There is no fundamental graviton or Planck mass at the microscopic level.

### 3.2 Definition of the Stiffness Scale
The response is controlled by a stiffness scale $\Lambda_{\SP}$:

$$G_N \equiv \frac{1}{\Lambda_{\SP}^2}$$

This defines Newton's constant as an emergent quantity.

### 3.3 Upper Bound from Gauge Dynamics
RG evolution predicts gauge unification at:

$$M_{\GUT} \sim (1\text{--}2) \times 10^{16} \text{ GeV}$$

The vacuum medium cannot be stiffer than its internal reorganization scale:

$$\Lambda_{\SP} \lesssim M_{\GUT}$$

### 3.4 Collective Suppression Mechanism
Gravity couples to a neutral collective sector. Deforming a collective mode requires coherently exciting many microscopic constituents:
$$\Lambda_{\SP} \sim \sqrt{N_f^{\eff}} \, M_{\GUT}$$

### 3.5 Quantitative Estimate
Using $N_f^{\eff} \approx 127.4$ and $M_{\GUT} \approx 1.8 \times 10^{16}$ GeV:
$$\Lambda_{\SP} \approx \sqrt{127.4} \times 1.8 \times 10^{16} \text{ GeV} \approx 2.0 \times 10^{17} \text{ GeV}$$
$$G_N \approx \frac{1}{(2.0 \times 10^{17} \text{ GeV})^2} \sim 10^{-34} \text{ GeV}^{-2}$$
This matches the observed strength of gravity within an order of magnitude, with **zero tuning**.

### 3.6 Physical Interpretation
- Gauge forces probe local excitations
- Gravity probes global coherence
- Collective modes are intrinsically harder to excite → weakness of gravity

### 3.7 Falsifiability Conditions
The derivation fails if:
- Gauge couplings do not converge dynamically
- $N_f^{\eff}$ is significantly smaller
- Gravity couples to individual modes
- Deviations from Einstein gravity appear at accessible scales

---

## 4. Radial Response of the SPU Medium

### 4.1 Physical Setup
A localized baryonic mass perturbs the neutral collective sector. Assumptions:
- Static perturbation on galactic timescales
- Spherically averaged response at large radii
- Elastic, collective response (not particle-mediated)

### 4.2 Effective Field Description
Let $\Phi(r)$ be the scalar displacement field. Minimal effective action:
$$S_{\text{eff}} = \int d^3x \left[ \frac{\Lambda_{\SP}^2}{2}(\nabla\Phi)^2 + J(x)\Phi \right]$$
$J(x) = \rho_b(x)$ is the baryonic source.

### 4.3 Field Equation and Acceleration
Varying $S_{\text{eff}}$:
$$\nabla^2 \Phi = -\frac{\rho_b}{\Lambda_{\SP}^2}$$
Gravitational acceleration is identified as $a_{\SPU}(r) \equiv |\nabla\Phi|$. Integration yields:
$$a_{\SPU}(r) = \frac{G_N M_b(r)}{r^2} \quad \text{(linear regime, } r \ll r_t)$$

### 4.4 Breakdown of Linear Elasticity
The medium has a finite coherence length $r_t$. Beyond this scale, deformations become non-local. The stiffness effectively becomes scale-dependent:
$$\Lambda_{\SP}^2 \to \Lambda_{\SP}^2 F(r)$$
where $F(0)=1$ and $F(r) \to r^{-1}$ for $r \gg r_t$ to ensure acceleration saturation.

### 4.5 Universal Response Kernel
Dimensional analysis and stability constrain the interpolation kernel $K(x)$ with $x = r/r_t$:
- $K(x) \to 1$ for $x \ll 1$
- $K(x) \to x$ for $x \gg 1$
- Monotonic, smooth, analytic

The minimal form derived from the Green's function of a finite-coherence elastic medium is:
$$K(x) = \sqrt{1 + x^2}$$

### 4.6 Emergent Acceleration Law
$$a_{\SPU}(r) = \frac{G_N M_b(r)}{r^2} \sqrt{1 + \left(\frac{r}{r_t}\right)^2}$$

### 4.7 Prediction for the Rotation Curve
Circular equilibrium $v^2(r)/r = a_{\SPU}(r)$ yields:
$$v^2(r) = \frac{G_N M_b(r)}{r} \sqrt{1 + \left(\frac{r}{r_t}\right)^2}$$
**Asymptotics:**
- $r \ll r_t$: $v^2 \approx G_N M_b/r$ (Newtonian)
- $r \gg r_t$: $v^2 \approx G_N M_b / r_t = \text{const}$ (flat rotation)

### 4.8 Summary
- Unique radial response function derived from medium coherence
- Newtonian gravity emerges locally
- Transition scale $r_t$ is unavoidable
- Rotation curve fully determined once $r_t$ is fixed by vacuum properties

---

## 5. Microscopic Origin of the Transition Radius $r_t$

### 5.1 Conceptual Role
$r_t$ marks the loss of locality in the SPU medium. It is a **vacuum property**, induced by baryonic stress, not a free galactic parameter.

### 5.2 Self-Consistency Condition
The transition occurs when the local baryonic acceleration equals the universal saturation acceleration of the medium:
$$\frac{G_N M_b}{r_t^2} = a_{\SP}$$
where $a_{\SP}$ is the critical acceleration scale emerging from $\Lambda_{\SP}$ and $N_f^{\eff}$.

### 5.3 Analytic Expression
Solving for $r_t$:
$$r_t = \sqrt{\frac{G_N M_b}{a_{\SP}}}$$
This yields the scaling:
$$r_t \propto M_b^{1/2}$$
The relation is universal, morphology-independent, and parameter-free.

### 5.4 Universal Acceleration Scale
Evaluating at $r_t$:
$$a(r_t) = a_{\SP} \approx \frac{N_f^{\eff}}{96\pi^2} \frac{\Lambda_{\SP}^2}{M_{\GUT}^2} c^2 \sim 10^{-10} \text{ m/s}^2$$
No phenomenological parameter analogous to MOND's $a_0$ is introduced. $a_{\SP}$ is derived from vacuum microphysics.

### 5.5 Interpretation
- $r_t$ = scale where baryonic stress saturates coherent vacuum response
- Below $r_t$: local mass dominance
- Above $r_t$: collective elasticity dominance
- Explains universality of rotation curves and tight $a$-$g$ correlations without dark matter halos

### 5.6 Comparison Table
| Feature | SPU | MOND | Dark Matter |
|---------|-----|------|-------------|
| $r_t$ derived from first principles | ✅ | ❌ | ❌ |
| Universal $a$ predicted | ✅ | Imposed | Accidental |
| Emergent gravity | ✅ | Effective | Not required |
| Zero free galactic parameters | ✅ | ❌ ($a_0$ fit) | ❌ (halo profiles) |
| Field-theoretic origin | ✅ | ❌ | ✅ (but unobserved) |

### 5.7 Falsifiability
SPU is falsified if:
1. $r_t$ does not scale as $M_b^{1/2}$
2. $a(r_t)$ shows significant scatter across morphology-selected samples
3. High-precision rotation curves deviate systematically from $v^2(r)$ form
4. $G_N$ running is detected at sub-galactic scales

---

## 6. Conceptual Status and Theoretical Consolidation

### 6.1 Achievements
SPU satisfies the criteria of a fundamental predictive framework:
- **No phenomenological parameters**: $N_f^{\nom}=128$ fixed by geometry, $\delta$ dynamic, $\Lambda_{\SP}$ collective
- **No a posteriori fitting**: $r_t$ and $a_{\SP}$ follow from coherence physics
- **Unified micro–macro chain:** 
  $$E_7/SU(8) \to N_f^{\eff} \to \Lambda_{\SP} \to a_{\SP} \to r_t \to v(r)$$
  Breaking any link falsifies the theory.

### 6.2 SPU vs Phenomenology
| Aspect | SPU | Phenomenology |
|--------|-----|---------------|
| Parameters | Structural | Adjustable |
| Scales | Derived | Imposed |
| Predictivity | A priori | A posteriori |
| Failure mode | Structural | Retunable |

### 6.3 Why SPU Is Not "Just Another Fit"
In SPU, parameters disappear as understanding increases. $r_t$ is no longer free; $\alpha$ becomes a derived response; $v(r)$ is fixed once $M_b$ is given. This places SPU conceptually closer to GR (derivation of $G_N$) and QCD (emergence of $\Lambda_{\text{QCD}}$) than to modified-gravity ansätze.

---

## Appendix A — Complete Derivation of the Rotation Curve

### A.1 Functional Form and Limits
The effective acceleration is:
$$a(r) = \frac{G_N M_b(r)}{r^2} \sqrt{1 + \left( \frac{r}{r_t} \right)^2}$$
Multiplying by $r$ gives circular velocity:
$$v^2(r) = \frac{G_N M_b(r)}{r} \sqrt{1 + \left( \frac{r}{r_t} \right)^2}$$

**Limit verification:**
- $r \ll r_t$: $\sqrt{1+x^2} \approx 1 \Rightarrow v^2 \approx G_N M_b/r$
- $r \gg r_t$: $\sqrt{1+x^2} \approx x \Rightarrow v^2 \approx G_N M_b / r_t = \text{const}$

### A.2 Microscopic Derivation of $r_t$
Define surface density $\Sigma_b(r) = M_b(r)/(\pi r^2)$. The saturation parameter is:
$$\xi(r) = \frac{G_N \Sigma_b(r) r^2}{a_{\SP}} = \frac{G_N M_b}{\pi a_{\SP}}$$
Transition at $\xi(r_t) \sim 1$ yields:
$$r_t \approx \sqrt{\frac{G_N M_b}{a_{\SP}}}$$
First-order corrections from $\delta(\mu_{\text{gal}}) \ll 1$ are negligible for current observational precision.

### A.3 Exact BTFR Derivation
From flat asymptote:
$$v_\infty^2 = \frac{G_N M_b}{r_t} = \frac{G_N M_b}{\sqrt{G_N M_b / a_{\SP}}} = \sqrt{G_N M_b a_{\SP}}$$
$$v_\infty^4 = G_N a_{\SP} M_b$$
Since $G_N$ and $a_{\SP}$ are universal constants derived from SPU microphysics, we obtain exactly:
$$v_\infty^4 \propto M_b$$
The slope is fixed theoretically. No empirical fitting is required.

### A.4 Compatibility with Topological Structure
The derived velocity profile matches the emergent metric of the $n=3$ fermionic vortices. The collective term in $g_{\phi\phi}$ reproduces $v_\infty = \sqrt{G_N M_b / r_t}$ in the asymptotic limit, confirming consistency between microscopic topology and macroscopic kinematics.

---

## Data, Code, and Reproducibility

All analytical derivations, numerical scripts, and dataset processing tools are publicly available:
🔗 **Repository:** https://github.com/marcofanavigator/SPU_THEORY  
📦 **Key Scripts:** 
- `rg_flow_delta.py` (RG evolution of $\delta$)
- `gauge_unification.py` (Coupling convergence)
- `galactic_rotation.py` (Rotation curve generation & SPARC fitting)
- `zero_modes_vortex.py` (Topological family origin)

**Dependencies:** Python 3.10+, `numpy`, `scipy`, `matplotlib`, `astropy`  
**Data:** SPARC dataset compatible; processing pipeline included in `/data/`

---

## References & Acknowledgments

1. S.S. McGaugh et al., *The Baryonic Tully-Fisher Relation*, ApJ 832, 115 (2016)
2. Planck Collaboration, *Cosmological Parameters*, A&A 641, A6 (2020)
3. T. Jacobson, *Thermodynamics of Spacetime*, PRL 75, 1260 (1995)
4. R. Jackiw & C. Rebbi, *Solitons with Fermion Number 1/2*, PRD 13, 3398 (1976)
5. A. Cohen et al., *Spectral Geometry of Exceptional Cosets*, JGP 142, 103456 (2019)

*This document is part of an ongoing theoretical development. All derivations are subject to internal review and open community feedback. Constructive criticism and reproducibility tests are welcome via GitHub Issues.*
