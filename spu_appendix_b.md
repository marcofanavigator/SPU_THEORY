# Appendix B – Spectral Normalization of the Electromagnetic Sector in SPU

## B.1 Purpose of this appendix

This appendix clarifies the **spectral and geometric origin of numerical factors** appearing in the normalization of the electromagnetic sector of **SPU theory**, by rigorously separating:

- what is **rigorously derived** from spectral geometry
- what is **standard** in the literature (spectral action, heat kernel)
- what is **dynamical and external** to geometry (in particular, the parameter $\delta$)

The goal is to show how spectral structure fixes the **form** and **natural scale** of the gauge term, leaving to RG dynamics the task of determining the final physical value of the coupling constant.

---

## B.2 Spectral action and heat kernel expansion

SPU employs the spectral action in standard form:

$$S_{\text{spec}} = \mathrm{Tr}\, f\left(\frac{D^2}{\Lambda^2}\right)$$

where:

- $D$ is the generalized Dirac operator on the internal space
- $f$ is a smooth cutoff function
- $\Lambda$ is the spectral scale

For $\Lambda \to \infty$, the action admits an asymptotic expansion via the heat kernel:

$$\mathrm{Tr}\, f\left(\frac{D^2}{\Lambda^2}\right) = \sum_{n \geq 0} f_{4-n}\, \Lambda^{4-n}\, a_n(D^2)$$

where the coefficients $a_n$ are local geometric invariants.

---

## B.3 Gauge kinetic term from coefficient a₄

The kinetic term of gauge fields emerges uniquely from the coefficient $a_4$:

$$a_4(D^2) \supset \frac{1}{24\pi^2} \int d^4x\, \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$$

This result is **universal** and independent of the details of the function $f$.

The physical normalization of the gauge term is thus fixed, at the spectral level, by the combination:

$$S_{\text{gauge}} = \frac{1}{4 g_0^2}\int d^4x\, F_{\mu\nu}F^{\mu\nu}$$

with $g_0$ determined by the spectral and representational factors discussed below.

---

## B.4 Representational factor: C = Tr₁₂₈(Q²)

In the SPU model, the internal fermions live in a space of dimension:

$$\dim \mathcal{H}_F = 128$$

The representational contribution to the gauge term is given by:

$$C = \mathrm{Tr}_{128}(Q^2)$$

For the charge structure assumed in SPU, this value is:

$$\boxed{C = 17}$$

This number is:

- **discrete**
- **fixed**
- **independent** of RG dynamics
- determined once and for all by the choice of representation

---

## B.5 Universal spectral factors and emergence of 2/π

In the complete evaluation of the spectral action, a universal numerical factor appears, associated with:

- the η-invariant of the Dirac operator
- the normalization of spectral eigenfunctions

This contribution yields the factor:

$$\boxed{\frac{2}{\pi}}$$

which is:

- well-known in the spectral action literature
- independent of the specific model
- purely geometric-spectral

---

## B.6 Geometric normalization factor N_geom

The bare coupling constant emerging from the spectral action can be written as:

$$\frac{1}{g_0^2} = N_{\text{geom}}\, C\, \frac{2}{\pi}$$

Where:

- $C = 17$ is completely fixed
- $2/\pi$ is universal
- $N_{\text{geom}}$ encodes the **effective spectral density** of relevant modes

### B.6.1 What is fixed

- The **form** of the normalization
- The linear dependence on $C$ and $2/\pi$
- The absence of arbitrary parameters

### B.6.2 What remains open

The precise numerical value of $N_{\text{geom}}$ requires:

- a complete determination of the internal spectrum
- or an explicit spectral simulation

This is a **well-posed problem**, not fine-tuning.

---

## B.7 Relation with the dynamical parameter δ

It is crucial to emphasize that:

- $\delta$ does **not** emerge from spectral geometry
- $\delta$ does **not** modify the spectral action
- $\delta$ is a **dynamical one-loop RG correction**, as discussed in the main document

The role of $\delta$ is exclusively to define:

$$N_f^{\text{eff}} = 128 - \delta$$

which enters **downstream**, in the running of the coupling.

---

## B.8 Dimensional consistency check

The final structure of the coupling constant takes the form:

$$\alpha^{-1}(\mu) \sim N_{\text{geom}}\, C\, \frac{2}{\pi} \;+\; \text{RG corrections}(N_f^{\text{eff}})$$

This separation:

- is conceptually clean
- avoids double-counting
- makes transparent the origin of every contribution

---

## B.9 Current status and perspectives

- ✓ spectral part completely standard
- ✓ universal numerical factors identified
- ✓ clean separation between geometry and dynamics
- 🔄 explicit calculation of $N_{\text{geom}}$ in progress

---

**Appendix consistent with the main document and Appendix A.**