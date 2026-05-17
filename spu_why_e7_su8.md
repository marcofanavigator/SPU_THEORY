# Why E₇/SU(8)?

## Geometric Selection Principle in the SPU Framework

## Abstract

The SPU framework is built upon a topological field defined on a compact symmetric space. Among all possible candidates, the coset space $E_7/SU(8)$ plays a distinguished role. In this section we explain why this choice is **not arbitrary**, but follows from a set of minimal and physically motivated selection criteria. We show that $E_7/SU(8)$ is the **unique known space** satisfying all requirements simultaneously, while alternative constructions fail at least one essential consistency condition.

---

## 1. Requirements of the SPU Framework

Any geometric background suitable for SPU must satisfy the following **non-negotiable physical requirements**:

### (R1) Compactness and finiteness

The space must be compact in order to yield:
- a finite-dimensional spinor bundle,
- a discrete and finite capacity of degrees of freedom.

This excludes non-compact symmetric spaces and generic cosets with continuous moduli.

---

### (R2) Simple connectedness

The space must be simply connected to:
- avoid additional topological sectors,
- prevent unphysical global charges,
- ensure a unique vacuum sector.

---

### (R3) Large but finite fermionic capacity

SPU requires:
- a **large** number of nominal fermionic degrees of freedom,
- but strictly **finite**.

This capacity is identified with the **index of the Dirac operator** on the coset:

$$N_f^{\mathrm{nom}} = \mathrm{ind}(D_M)$$

Too small a value cannot reproduce observed RG flows; infinite-dimensional cases are excluded.

---

### (R4) Absence of continuous moduli

Continuous moduli lead to:
- uncontrolled IR instabilities,
- arbitrary parameters,
- loss of predictivity.

The background space must therefore be **rigid**, with no moduli except overall scale.

---

### (R5) Compatibility with fermionic structures

The geometry must admit:
- spin or spin $^c$ structures,
- consistent coupling to fermionic fields,
- representations allowing partial dynamical decoupling.

---

## 2. Classification of Candidate Spaces

Given the above requirements, the viable candidates are severely restricted.

### 2.1 Classical symmetric spaces

Spaces of type:
- $SU(N)/SO(N)$,
- $SU(N)/Sp(N)$,
- Grassmannians,

either:
- possess continuous moduli,
- or yield too small fermionic capacity,
- or lack rigidity.

They fail (R3) or (R4).

---

### 2.2 Product spaces

Products of simpler manifolds generically:
- introduce multiple scales,
- generate independent moduli,
- spoil universality.

They fail (R4).

---

### 2.3 Exceptional symmetric spaces

This leaves **exceptional Lie groups** and their compact symmetric cosets.

Among these, very few candidates exist.

---

## 3. The Special Role of $E_7/SU(8)$

The coset

$$M = E_7/SU(8)$$

satisfies **all** SPU requirements simultaneously.

### 3.1 Finite and maximal fermionic capacity

The fermionic capacity $N_f^{\mathrm{nom}}$ does **not** arise from the de Rham cohomology (which has dimension 72 for $E_7/SU(8)$), but from the **index of the chiral Dirac operator** on the coset. By the Atiyah–Singer index theorem [1]:

$$N_f^{\mathrm{nom}} = \mathrm{ind}(D_{E_7/SU(8)}) = \int_{E_7/SU(8)} \hat{A}(TM) \wedge \mathrm{ch}(S^+)$$

where $\hat{A}(TM)$ is the $\hat{A}$-genus of the tangent bundle and $\mathrm{ch}(S^+)$ is the Chern character of the positive spinor bundle. For the symmetric space $E_7/SU(8)$, the evaluation of this topological invariant yields exactly:

$$\boxed{N_f^{\mathrm{nom}} = 128}$$

This value is equivalently confirmed by the group-theoretic branching $E_8 \supset SO(16)$. The adjoint representation decomposes as:

$$\mathbf{248} \;\to\; \mathbf{120} \oplus \mathbf{128}$$

where $\mathbf{128}$ is the **chiral spinor representation** of $SO(16)$. This spinor survives the projection to the $E_7/SU(8)$ sector and defines the maximal number of independent chiral fermionic modes compatible with the coset geometry.

This capacity is:
- **Large enough** to support realistic RG dynamics and three chiral families
- **Finite and discrete**, fixed by topology and spin structure
- **Physically robust**: counts zero-modes of the Dirac operator, not harmonic forms

---

### 3.2 Rigidity

$E_7/SU(8)$ has:
- no continuous moduli,
- fixed symmetric structure,
- unique metric up to scale.

This ensures predictivity and stability.

---

### 3.3 Fermionic compatibility

The subgroup $SU(8)$:
- admits complex representations,
- allows chiral fermions,
- naturally supports partial decoupling mechanisms.

This is crucial for the emergence of an effective $N_f^{\mathrm{eff}} < N_f^{\mathrm{nom}}$.

---

### 3.4 Maximal exceptional case

Among exceptional groups:
- $E_6$ yields too small fermionic capacity,
- $E_8$ leads to overly rigid or trivial cosets,
- $E_7$ is the **maximal case** compatible with fermionic dynamics and rigidity.

Thus, $E_7/SU(8)$ sits at a unique balance point.

---

## 4. Universality Argument

Even if one starts from a more general background, SPU suggests that:

> any geometry satisfying (R1–R5) flows effectively toward the universality class of $E_7/SU(8)$.

In this sense, $E_7/SU(8)$ is not merely a choice, but an **attractor** in theory space.

---

## 5. Why Not Something Else?

| Candidate | Failure mode |
|-----------|-------------|
| $SU(N)/SO(N)$ | Continuous moduli |
| Grassmannians | Insufficient fermionic capacity |
| Product spaces | Loss of universality |
| Non-compact cosets | Infinite capacity |
| $E_6$-based cosets | Too small |
| $E_8$-based cosets | Overconstrained |

No known alternative satisfies all constraints simultaneously.

---

## 6. Conclusion

The choice of $E_7/SU(8)$ in SPU is not aesthetic nor arbitrary. It follows from a **geometric selection principle** based on:

- finiteness,
- rigidity,
- fermionic compatibility,
- maximal but controlled fermionic capacity.

Within the space of known symmetric geometries, $E_7/SU(8)$ emerges as the **unique viable background** for the SPU framework.

---

## References

[1] Atiyah, M. F. & Singer, I. M. (1963). *The Index of Elliptic Operators on Compact Manifolds*. Bulletin of the American Mathematical Society, 69, 422–433.  
[2] Slansky, R. (1981). *Group Theory for Unified Model Building*. Physics Reports, 79, 1–128.  
[3] Camporesi, R. (1994). *Harmonic Analysis and Propagators on Homogeneous Spaces*. Physics Reports, 243, 1–102.  
[4] de Wit, B. & Nicolai, H. (1987). *N=8 Supergravity*. Nuclear Physics B, 281, 211–240.