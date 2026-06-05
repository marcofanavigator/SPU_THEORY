# 🧠 1. Variabile fisica: Curvature Perturbation
Passiamo alla variabile osservabile gauge-invariant, la perturbazione della curvatura:
$$\zeta = -\frac{H}{\dot{\delta}} \varphi, \quad \text{con } \varphi = \delta - \bar\delta$$

$\zeta$ ha la proprietà fondamentale di rimanere costante su scale super-horizon, preservando le informazioni dell'epoca inflazionaria.

# ⚙️ 2. Azione Quadratica e Modo di Fourier
L'azione al secondo ordine per le fluttuazioni è:
$$S^{(2)} = \int dt\, d^3x \, a^3 \left[ \frac{K}{2} \dot\varphi^2 - \frac{K}{2a^2} (\nabla \varphi)^2 \right]$$

In Fourier space, i modi $\varphi_k$ evolvono come:
$$\varphi_k(\tau) = \frac{H}{\sqrt{2K k^3}} (1 + ik\tau)e^{-ik\tau}$$

# 🔬 3. Azione Cubica Completa (Interazioni)
Dalla derivazione spettrale SPU, emergono tre operatori di interazione non lineari:
$$S^{(3)} = \int dt\, d^3x \, a^3 \left[ A \varphi \dot\varphi^2 + B \varphi (\nabla \varphi)^2 + C \varphi^3 \right]$$

Dove i coefficienti $A, B, C$ sono **derivati analiticamente** dallo spettro $\rho(\lambda)$:
* $A, B \propto K'(\delta_*)$
* $C \propto U'''(\delta_*)$

# 🧮 4. Il Bispettro e la Shape Function
Il bispettro $B(k_1, k_2, k_3)$ quantifica la correlazione a tre punti:
$$\boxed{B(k_1, k_2, k_3) = \frac{(2\pi)^4 \mathcal{P}_\zeta^2}{\prod_i k_i^3} \mathcal{S}(k_1, k_2, k_3)}$$

### La Shape Function $\mathcal{S}$ in SPU:
Sommando i contributi del formalismo *in-in*, otteniamo la struttura ibrida:

$\boxed{\mathcal{S} = \alpha \frac{\sum_{i<j} k_i^2 k_j^2}{k_t^3} + \beta \frac{\sum_i k_i^2 (\vec{k}_j \cdot \vec{k}_k)}{k_t^3} + \gamma \frac{1}{k_t^3}}$

(con $$k_t = k_1 + k_2 + k_3$$ )

# 📊 5. Limiti e Firme Osservative

1.  **Limite Squeezed ($k_1 \ll k_2, k_3$):
2.  ** Presenta una lieve violazione della *consistency relation* di Maldacena ($\Delta_{\mathrm{SPU}} \neq 0$), segnale di una dinamica che non è puramente a singolo campo standard.
3.  **Limite Equilatero ($k_1 = k_2 = k_3$):** Ampiezza massima data dalla combinazione lineare dei coefficienti spettrali.
4.  **Limite Folded ($k_1 \approx k_2 + k_3$):** Esibisce un **enhancement moderato**, firma del "mezzo collettivo".

# 📈 6. Confronto tra Modelli

| Modello | Shape Prevalente | Parametri Liberi |
| :--- | :--- | :--- |
| **Slow-roll** | Quasi-Locale (minima) | Molti |
| **DBI Inflation** | Equilatera | 1 ($c_s$) |
| **Multi-field** | Locale | Variabili |
| **SPU** | **Ibrida Strutturata** | **0 (Dettati dal Coset)** |

# 🔥 7. Verdetto: Il Fingerprint del Mezzo Fermionico
La forma del bispettro in SPU non è arbitraria. Poiché $\alpha, \beta, \gamma$ dipendono da $\frac{d}{d\delta}\log \rho(\lambda)$, ogni picco o avvallamento nel bispettro primordiale è una **mappa diretta della densità di stati nel coset $E_7/SU(8)$**.

$$\boxed{\text{L'universo primordiale conserva memoria del mezzo fermionico sottostante}}$$
