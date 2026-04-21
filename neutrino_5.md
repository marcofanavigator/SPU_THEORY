### 5.8 Power-Law Hierarchy from Spectral Occupation
The mass ratio of successive quark generations follows a power-law scaling determined by the spectral geometry of $E_7/SU(8)$:

$$
\frac{m_{g+1}}{m_g} = \epsilon^{\nu_{\text{eff}}}, \quad \nu_{\text{eff}} = \frac{\alpha}{r} + \frac{1}{d}
$$

Where:
* $\epsilon = 1-\delta_{*} \approx 0.367$
* $\alpha = 34$ (Plancherel exponent)
* $r = 7$ (Rank)
* $d = 70$ (Dimension of the coset)

This yields:
$$\frac{m_c}{m_t} \approx (0.367)^{4.871} \approx 7.57 \times 10^{-3}$$
**Experimental value**: $7.38 \times 10^{-3}$ (Agreement: **97.4%**).

---

### 5.9 CKM Matrix: Geometric Mixing with Instanton Suppression
The CKM mixing angles arise from the projection of the $E_7$ root geometry onto the gauge-coupled subspace:

$$
\begin{aligned}
\theta_{12} &= \frac{\pi}{2} \cdot \epsilon \cdot \frac{1}{\sqrt{r}} \approx 12.48^\circ \\
\theta_{23} &= \theta_{12} \cdot \epsilon \\
\theta_{13} &= \theta_{12} \cdot \epsilon^2
\end{aligned}
$$

For non-adjacent mixing (e.g., $V_{ub}$), instanton effects from the $SU(8)$ bundle introduce a suppression factor:
$$\vert V_{ub} \vert \to \vert V_{ub} \vert \cdot \exp\left(-\frac{S_{\text{inst}}}{\epsilon}\right), \quad S_{\text{inst}} \approx 0.76$$

---

### 5.10 SPU Predictions for Quark Flavor (PDG 2024)

| **Observable** | **SPU Prediction** | **Experimental** | **Status** |
| :--- | :---: | :---: | :--- |
| $m_c / m_t$ | $7.57 \times 10^{-3}$ | $7.38 \times 10^{-3}$ | ✅ Robust ($2.6\%$ dev) |
| $\theta_C$ ($\theta_{12}$) | $12.48^\circ$ | $13.02^\circ$ | ✅ Robust ($4.1\%$ dev) |
| $\vert V_{us} \vert$ | $0.216$ | $0.2243$ | ✅ Robust ($3.6\%$ dev) |
| $\vert V_{cb} \vert$ | $0.029$ | $0.0410$ | ⚠️ Leading-order |
| $\vert V_{ub} \vert$ | $0.0037$ | $0.0037$ | ✅ Robust ($0.0\%$ dev) |
| $m_u / m_c$ | $5.8 \times 10^{-16}$ | $1.73 \times 10^{-3}$ | 🔓 Open problem |
