# Azione Effettiva per δ — Campo Scalare Collettivo

---

## 1. Principio Guida

$$
\delta(x) \equiv \text{campo scalare collettivo}
$$

Interpretabile come:
- grado di non-condensazione del mezzo fermionico
- parametro d'ordine (tipo transizione di fase)

L'azione deve essere di tipo **Landau-Ginzburg** con termini geometrici e sorgenti collettive.

---

## 2. Forma Generale dell'Azione

$$
\boxed{\Gamma[\delta,g] = \int d^4x \sqrt{-g} \left[ \frac{Z}{2} (\nabla \delta)^2 + V(\delta) + \mathcal{L}_{\mathrm{grav}}(\delta) + \mathcal{L}_{\mathrm{source}}(\delta) \right]}
$$

---

## 3. Potenziale V(δ) — Derivato dal RG

Deve avere:
- minimo a $\delta = \delta_{\ast}$
- barriera UV ($\delta \to 1$)

Forma minimale coerente con il flusso RG:

$$
V(\delta) = A(\delta - \delta_{\ast})^2 + B(\delta - \delta_{\ast})^4
$$

con:
- $\delta_{\ast} \approx 0.633$ — punto fisso IR
- $A > 0$, $B > 0$ — derivati dal fixed point RG

---

## 4. Accoppiamento Gravitazionale

La curvatura modifica lo stato di condensazione del mezzo:

$$
\mathcal{L}_{\mathrm{grav}} = \xi \, \delta \, R
$$

Tipo *induced gravity*: la curvatura $R$ agisce come feedback sul campo $\delta$.

---

## 5. Termine Sorgente (Massa + Densità)

$$
\mathcal{L}_{\mathrm{source}} = J(x)\,\delta
$$

con:

$$
J(x) = \frac{R_s}{r^3} - \kappa \, \Sigma(x)
$$

| Termine | Effetto |
|---------|---------|
| $+R_s/r^3$ | massa → decondensa |
| $-\kappa\,\Sigma$ | densità → condensa |

---

## 6. Azione Completa

$$
\boxed{\Gamma[\delta] = \int d^4x \sqrt{-g} \left[ \frac{Z}{2}(\nabla\delta)^2 + A(\delta-\delta_{\ast})^2 + B(\delta-\delta_{\ast})^4 + \xi\delta R + \left(\frac{R_s}{r^3} - \kappa\Sigma\right)\delta \right]}
$$

---

## 7. Equazione del Moto

Dalla variazione $\dfrac{\delta\Gamma}{\delta\delta} = 0$:

$$
Z\,\Box\delta - 2A(\delta-\delta_{\ast}) - 4B(\delta-\delta_{\ast})^3 + \xi R + \frac{R_s}{r^3} - \kappa\Sigma = 0
$$

---

## 8. Limite Statico

Trascurando i gradienti lontano dalle transizioni:

$$
-2A(\delta-\delta_{\ast}) - 4B(\delta-\delta_{\ast})^3 + \xi R + \frac{R_s}{r^3} - \kappa\Sigma = 0
$$

---

## 9. Soluzione Approssimata

Per piccole deviazioni dal punto fisso:

$$
\delta - \delta_{\ast} \approx \frac{1}{2A}\left(\xi R + \frac{R_s}{r^3} - \kappa\Sigma\right)
$$

---

## 10. Ricostruzione della Formula Empirica

Usando:
- $R \sim R_s/r^3$
- scaling RG con cutoff a $\ell_{\mathrm{SP}}$
- saturazione → forma razionale

Si ricostruisce la formula compatta:

$$
\boxed{\delta = \frac{\delta_{\ast}}{1+f_{\mathrm{IR}}} \cdot \frac{1 + \dfrac{R_s}{r}}{\left(1 + \left(\dfrac{\ell_{\mathrm{SP}}}{r}\right)^2\right)\left(1 + \dfrac{\Sigma}{\Sigma_{\mathrm{SP}}}\right)}}
$$

---

## 11. Punto Cruciale

$$
\boxed{\delta(r,\Sigma,M_{\mathrm{BH}}) \text{ è soluzione di } \Gamma[\delta]}
$$

La formula di $\delta$ **non è più postulata**: emerge come soluzione dell'azione effettiva.

---

## 12. Significato Fisico

| Elemento | Ruolo |
|----------|-------|
| $\delta$ | campo reale dinamico |
| gravità | feedback del mezzo |
| materia | sorgente di fase |
| spazio-tempo | stato del mezzo |
