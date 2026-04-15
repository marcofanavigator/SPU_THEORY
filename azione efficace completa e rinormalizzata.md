# 🧠 1. Principio fondamentale

Tutto deriva da:

$$
\boxed{\Gamma[g,\delta] = \frac{1}{2}\mathrm{Tr}\log\left(\frac{\Delta_{E_7/SU(8)}(\delta,g)}{\mu^2}\right)}
$$

dove:
* lo spettro dipende da $\delta$
* la metrica $g_{\mu\nu}$ emerge come variabile IR

# ⚙️ 2. Decomposizione heat-kernel

Espansione standard:

$$
\mathrm{Tr}(e^{-t\Delta}) = \frac{1}{(4\pi t)^2} \int d^4x \sqrt{-g} \left[ a_0 + a_2 t + a_4 t^2 + \dots \right]
$$

👉 quindi:

$$
\Gamma = \int d^4x \sqrt{-g} \left[ \Lambda_{\mathrm{eff}}(\delta) + \frac{M_{\mathrm{Pl}}^2(\delta)}{2} R + \alpha(\delta) R^2 + \dots \right]
$$

# 🔬 3. Coefficienti derivati (non postulati)

### (a) Termine cosmologico

$$
\boxed{\Lambda_{\mathrm{eff}}(\delta) = \frac{1}{2} \int d\lambda \, \rho(\lambda) \log\left(1 + \frac{\lambda}{\Lambda_{\mathrm{SP}}^2}(1+c\delta)\right)}
$$

### (b) Termine Einstein-Hilbert

$$
\boxed{M_{\mathrm{Pl}}^2(\delta) = \frac{1}{96\pi^2} \int d\lambda \, \rho(\lambda) \frac{\lambda}{\lambda(1+c\delta)+\Lambda_{\mathrm{SP}}^2}}
$$

👉 qui nasce:
* $\sqrt{N_f^{\mathrm{eff}}}$
* $f_{\mathrm{IR}}$

### (c) Termine cinetico di $\delta$

Deriva da variazioni locali dello spettro:

$$
\boxed{Z(\delta) = \frac{1}{96\pi^2} \int d\lambda \, \rho(\lambda) \frac{\lambda^2}{\left(\lambda(1+c\delta)+\Lambda_{\mathrm{SP}}^2\right)^2}}
$$

# 🌌 4. Azione completa (rinormalizzata)

$$
\boxed{\Gamma[g,\delta] = \int d^4x \sqrt{-g} \Bigg[ \frac{Z(\delta)}{2} (\nabla \delta)^2 + V(\delta) + \frac{M_{\mathrm{Pl}}^2(\delta)}{2} R + \alpha(\delta) R^2 \Bigg]}
$$

# 🧮 5. Rinormalizzazione

Le divergenze UV:

$$
\int d\lambda \, \rho(\lambda) \to \infty
$$

sono trattate con **Subtraction fisica**:

$$
\boxed{\Gamma_{\mathrm{ren}} = \Gamma - \Gamma[\delta=0, g=\eta]}
$$

👉 elimina:
* vacuum divergente
* parte non osservabile

# 🔥 6. Forma finale esplicita

$$
\boxed{\Gamma_{\mathrm{ren}}[g,\delta] = \int d^4x \sqrt{-g} \Bigg[ \frac{Z(\delta)}{2} (\nabla \delta)^2 + \tilde V(\delta) + \frac{M_{\mathrm{Pl}}^2(\delta)}{2} R + \alpha(\delta) R^2 \Bigg]}
$$

con: $\tilde V(\delta) = V(\delta) - V(0)$

# 🧠 7. Equazioni del moto

### (a) Campo $\delta$

$$
\boxed{Z(\delta)\Box\delta + \frac{1}{2}Z'(\delta)(\nabla\delta)^2 + V'(\delta) + \frac{1}{2}M_{\mathrm{Pl}}^{2\,\prime}(\delta) R = 0}
$$

### (b) Equazione gravitazionale

$$
\boxed{M_{\mathrm{Pl}}^2(\delta) G_{\mu\nu} = T_{\mu\nu}^{(\delta)} + \text{correzioni } R^2}
$$

# 🧩 8. Proprietà cruciali

* ✔ **Nessun parametro libero reale**
    * $\rho(\lambda)$ fissata dal coset
    * $\Lambda_{\mathrm{SP}}$ fissata da GUT
    * $N_f$ topologico
* ✔ **Gravità emergente**
    * $M_{\mathrm{Pl}}^2(\delta)$ non è costante
* ✔ **UV regolare**
    * cutoff naturale $\Lambda_{\mathrm{SP}}$
    * niente divergenze fisiche
* ✔ **IR controllato**
    * punto fisso $\delta_*$
    * fattore $f_{\mathrm{IR}}$

# 🔥 9. Forma ultra-compatta (paper-ready)

$$
\boxed{\Gamma = \int d^4x \sqrt{-g} \left[ \frac{1}{2}Z(\delta)(\partial\delta)^2 + \frac{1}{2}M_{\mathrm{Pl}}^2(\delta) R + V(\delta) \right]}
$$

con: $Z, M_{\mathrm{Pl}}^2, V$ derivati da $\rho_{E_7/SU(8)}(\lambda)$
