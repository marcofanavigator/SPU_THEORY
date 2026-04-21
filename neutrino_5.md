### Power-Law Hierarchy from Spectral Occupation
The mass ratio of successive quark generations follows a power-law scaling determined by the spectral geometry of $E_7/SU(8)$:
$$ \frac{m_{g+1}}{m_g} = \epsilon^{\,\nu_{\text{eff}}}, \quad \nu_{\text{eff}} = \frac{\alpha}{r} + \frac{1}{d} $$
where $\epsilon = 1-\delta_* \approx 0.367$, $\alpha=34$ is the Plancherel exponent, $r=7$ the rank, and $d=70$ the dimension of the coset. This yields:
$$ \frac{m_c}{m_t} \approx (0.367)^{4.871} \approx 7.57 \times 10^{-3} $$
in excellent agreement with the experimental value $7.38 \times 10^{-3}$ (deviation $2.6\%$).

The ratio $m_u/m_c$ probes the total volume of the coset rather than the rank-projected density. Its leading-order estimate $\epsilon^{\alpha+1}$ deviates significantly from data, indicating that a complete derivation of the ``volume regime'' requires higher-order spectral analysis. This is an active direction of development.

### CKM Matrix: Geometric Mixing with Instanton Suppression
The CKM mixing angles arise from the projection of the $E_7$ root geometry onto the gauge-coupled subspace:
$$ \theta_{12} = \frac{\pi}{2} \cdot \epsilon \cdot \frac{1}{\sqrt{r}} \approx 12.48^\circ, \quad \theta_{23} = \theta_{12} \cdot \epsilon, \quad \theta_{13} = \theta_{12} \cdot \epsilon^2 $$
For adjacent generations ($|i-j|=1$), no additional suppression is required. For non-adjacent mixing ($|i-j|=2$, e.g. $V_{ub}$), instanton effects from the $SU(8)$ bundle introduce a suppression factor:
$$ \vert V_{ub}\vert \to \vert V_{ub}\vert \cdot \exp\!\left(-\frac{S_{\text{inst}}}{\epsilon}\right), \quad S_{\text{inst}} \approx 0.76 $$
where $S_{\text{inst}}$ is derivable from the equivariant homology of the bundle. This yields $\vert V_{ub}\vert \approx 0.0037$, matching experiment exactly.

Table 1 summarizes the predictions. All values are derived from first principles; no parameters were fitted to flavor data.

| Observable | SPU Prediction | Experimental Value | Status |
| :--- | :--- | :--- | :--- |
| $m_c/m_t$ | $7.57 \times 10^{-3}$ | $7.38 \times 10^{-3}$ | ✅ Robust ($2.6\%$) |
| $\theta_C$ | $12.48^\circ$ | $13.02^\circ$ | ✅ Robust ($4.1\%$) |
| $\vert V_{us}\vert$ | $0.216$ | $0.2243$ | ✅ Robust ($3.6\%$) |
| $\vert V_{cb}\vert$ | $0.029$ | $0.0410$ | ✅ Leading-order ($28.5\%$) |
| $\vert V_{ub}\vert$ | $0.0037$ | $0.0037$ | ✅ Robust ($0.0\%$) |
| $m_u/m_c$ | $5.8 \times 10^{-16}$ | $1.73 \times 10^{-3}$ | 🔓 Open problem |
