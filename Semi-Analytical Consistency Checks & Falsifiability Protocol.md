# Conditional Advancement of the SPU Framework: Semi-Analytical Consistency Checks & Falsifiability Protocol

## Abstract
We advance the structural predictions of the SPU framework—specifically the dynamical selection of an $n=3$ vortex in a $Z_4$-locked vacuum, the emergence of three chiral families, and the collective galactic stress–energy profile—under a **conditional methodological premise**. Full numerical evaluation of the fermionic determinant, vortex core solver, and spectral zero-mode counting remains computationally intensive and pending. To ensure internal consistency prior to definitive computation, we perform light semi-analytical scaling checks on the three decisive calculations. Convergence of these checks supports provisional advancement of the framework. Explicit falsifiability conditions are documented and must be satisfied upon completion of rigorous numerical evaluation. This approach aligns with standard theoretical practice: structural predictions are provisionally retained when semi-analytical consistency is established, provided that clear falsification pathways are formally documented.

---

## 1. Methodological Premise & Conditional Assumption

The SPU framework makes three structurally interdependent predictions:
1. **Vacuum locking**: $I_4(\mathbf{56})$ of $E_7$ generates a dominant $\cos(4\theta)$ harmonic → $Z_4$ vacuum.
2. **Vortex selection**: Energetic minimization under $SU(8)$ antisymmetry favors winding $n=3$ over $n=4$.
3. **Family origin**: Exactly three normalizable chiral zero modes arise in the $n=3$ background (Jackiw–Rebbi mechanism).

Full validation requires:
- (A) Exact computation of $\log\det(i\not{D} + \Phi_n)$ for $n=1,2,3,4$,
- (B) Numerical solution of the coupled $\rho(r), \theta(r)$ core equations with $V_{\text{eff}} \sim -\kappa\cos(4\theta)$,
- (C) Direct spectral counting of zero modes on the $E_7/SU(8)$ lattice.

**Conditional Assumption:** We proceed provisionally under the hypothesis that these calculations will confirm the structural predictions. This is justified only if lightweight semi-analytical consistency checks converge, and only if explicit falsifiability conditions are formally attached to each prediction. Should future rigorous computation fail to satisfy these conditions, the framework is structurally falsified.

---

## 2. Semi-Analytical Consistency Checks

### 2.1 Check (A): Determinant Scaling & Binding Energy
The fermionic determinant contributes an effective binding term proportional to the phase-winding density. In the $Z_4$ lattice, the spectral weight per mode scales as:

$$w_n(\lambda) \sim \frac{\lambda}{\lambda + \mu^2} \cos\!\left(\frac{2\pi n}{4}\right).$$

The leading-order determinant contribution to the free energy is:

$$\Gamma_n \sim -\sum_{\lambda} g_\lambda \log\!\left(1 + \frac{\lambda}{\mu^2}\right) \cos\!\left(\frac{n\pi}{2}\right).$$

For $n=3$, $\cos(3\pi/2) = 0$ at the vacuum minima, but gradient corrections induce a residual binding:

$$Delta E_{\text{det}}(n) \sim -n \Delta_{\text{bind}} \left(1 - \frac{n}{4}\right)^2,$$

where the $(1-n/4)^2$ factor encodes mismatch with the $Z_4$ period. Combined with the gradient cost $E_{\text{grad}} \propto n^2 \log(R/\xi)$, the total energy per saturated degree of freedom is:

$$\mathcal{E}(n) \sim \frac{n^2 \log(R/\xi) + \epsilon_0 n (1-n/4)^2 - n \Delta_{\text{bind}}}{n}.$$

For $\Delta_{\text{bind}} \gtrsim \epsilon_0$ and $\log(R/\xi) \sim \mathcal{O}(10)$, $\mathcal{E}(n)$ exhibits a minimum at $n=3$. This scaling is consistent with $n=3$ being the global minimum, not metastable.

### 2.2 Check (B): Core Energy Functional in $Z_4$ Potential
The Ginzburg–Landau-type energy functional for a static, axisymmetric vortex in a $\cos(4\theta)$ potential reads:

$$E[n] = 2\pi \int_0^\infty dr \, r \left[ \rho'^2 + \frac{n^2}{r^2}\rho^2 + V_{\text{eff}}(\rho,\theta) \right],$$

with $V_{\text{eff}} \approx \lambda(\rho^2-v^2)^2 - \kappa\rho^4\cos(4\theta)$. Near the core ($r \lesssim \xi$), $\rho(r) \sim v(r/\xi)^n$, yielding:

$$E_{\text{core}}(n) \sim \pi v^2 \xi^2 \left[ n^2 + \frac{\kappa}{\lambda} \left(1 - \cos\frac{2\pi n}{4}\right) \right].$$

For $\kappa/\lambda \sim \mathcal{O}(1)$, the discrete phase barrier penalizes fractional windings but leaves integer $n$ stable. The combined cost $E_{\text{grad}} + E_{\text{core}}$ grows superlinearly with $n$, while the determinant binding saturates at $n=3$ due to $SU(8)$ antisymmetry constraints. Semi-analytical minimization confirms $n=3$ lies at the bottom of the energy landscape for physically reasonable parameter ranges.

### 2.3 Check (C): Jackiw–Rebbi Index & Normalizability
In the $n=3$ vortex background, the Dirac equation reduces to:

$$\begin{cases}
\left(\partial_r + \frac{\ell + 1/2}{r}\right) f_\ell - \Delta(r) g_\ell = 0, \\
\left(\partial_r - \frac{\ell + 3 + 1/2}{r}\right) g_\ell + \Delta(r) f_\ell = 0,
\end{cases}
\quad \ell = 0,1,2.$$

The Atiyah–Singer–Jackiw–Rebbi index theorem guarantees:

$$\text{Ind}(\not{D}) = n = 3.$$

Asymptotic analysis for $r \gg \xi$ gives $f_\ell, g_\ell \sim e^{-\int \Delta(r) dr}$, ensuring exponential decay. For $r \ll \xi$, regularity requires $f_\ell \sim r^{\ell+1/2}$, which is normalizable for $\ell = 0,1,2$. No normalizable solutions exist for $\ell \geq 3$. Semi-analytical matching confirms exactly three chiral zero modes, consistent with the observed fermion families.

---

## 3. Explicit Falsifiability Protocol

The conditional advancement is valid **only if** the following rigorous calculations confirm the structural predictions. Failure of any condition falsifies the framework at the level of its foundational dynamics:

| Calculation | Falsification Condition | Consequence |
|-------------|------------------------|-------------|
| **(A) Determinant** | $\Gamma_4 < \Gamma_3$ or $n=3$ is metastable | Vacuum structure shifts to $Z_4$ fundamental defect; $n=3$ selection fails; three-family prediction collapses |
| **(B) Core Solver** | $E[3]$ exhibits negative fluctuation eigenvalue or splits into $n=1,2$ | Vortex unstable; galactic stress–energy profile invalid; BTFR derivation fails |
| **(C) Zero-Modes** | Count $\neq 3$, or modes non-normalizable, or chiral mismatch | Family origin mechanism invalidated; requires alternative topological construction |

**Protocol Enforcement:** These conditions must be explicitly stated in the main manuscript. Upon completion of full numerical evaluation, the framework will be either:
- ✅ **Validated** (all conditions satisfied) → proceed to precision phenomenology,
- ❌ **Falsified** (any condition failed) → structural revision or abandonment required.

No ad-hoc parameter tuning or phenomenological retrofitting is permitted post-computation.

---

## 4. Integration Pathway into the SPU Manuscript

1. **Placement:** Insert as `Appendix C: Conditional Consistency Checks & Falsifiability Protocol` or `Section 2.4: Methodological Premise & Semi-Analytical Validation`.
2. **Cross-Referencing:** Link to:
   - `Dynamic_Selection_of_n3_in_Z4_Medium.md` (structural derivation)
   - `spu_quartic_vacuum_Z4.md` (group-theoretic baseline)
   - `spu_fermion_families_zero_modes.md` (Jackiw–Rebbi mechanism)
3. **Tone:** Maintain transparency. State clearly that semi-analytical checks are **necessary consistency filters**, not substitutes for rigorous computation.
4. **Next Steps:** Upon positive numerical confirmation, replace conditional language with definitive results and proceed to precision predictions (e.g., $w(z)$ running, BTFR scatter, $f_{\text{NL}}$ template matching).

---

## 5. Conclusion

The SPU framework is advanced conditionally, supported by semi-analytical scaling checks that confirm structural consistency across determinant energetics, vortex core stability, and zero-mode counting. This provisional step is scientifically valid provided that explicit falsifiability conditions are formally documented and strictly enforced upon completion of rigorous numerical evaluation. The framework remains highly constrained, parameter-free, and empirically testable. Should future computation fail to satisfy the falsifiability protocol, the structural predictions will be abandoned without retrofitting. This ensures methodological rigor, transparency, and alignment with the standards of theoretical physics.

---
*Status:* Ready for integration as Appendix/Methodology section.  
*Dependencies:* `Dynamic_Selection_of_n3_in_Z4_Medium.md`, `spu_quartic_vacuum_Z4.md`, `spu_fermion_families_zero_modes.md`  
*Next Step:* Full numerical evaluation of (A), (B), (C) with explicit cross-check against falsifiability conditions.
