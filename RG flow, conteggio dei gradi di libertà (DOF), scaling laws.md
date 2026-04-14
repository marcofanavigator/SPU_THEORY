# Confronto Tecnico: SPU vs String Theory

## 1. RG Flow: struttura e fixed points

### SPU: RG non-lineare con saturazione collettiva
Il parametro chiave è:

$$\delta(\mu) = 1 - \frac{\sum_n g_n \, w(\lambda_n/\mu^2)}{\sum_n g_n}$$

con $w(x) = \frac{x}{1+x}$.

**Equazione di flusso (forma efficace)**
Dalla struttura spettrale discreta:

$$\mu \frac{d\delta}{d\mu} = \beta(\delta) \sim - A \, \delta (1 - \delta) + O(\delta^2/N_f)$$

* **$\delta = 0$**: UV (mezzo completamente non condensato)
* **$\delta \to \delta_* \approx 0.633$**: IR fixed point stabile

👉 Questo è un RG con saturazione logistica (non perturbativo, collettivo).

**Conseguenze**
* Flusso universale (insensibile ai dettagli UV)
* Emergenza scala: $\Lambda_{\mathrm{SP}} \sim \sqrt{N_f^{\mathrm{eff}}} \, M_{\mathrm{GUT}}$

### String Theory: RG conforme (worldsheet)
RG definito sulla worldsheet 2D:

$$\mu \frac{d g^i}{d\mu} = \beta^i(g)$$

**Condizione di consistenza:**
$\beta^i = 0 \to$ equazioni di Einstein emergono:
$$R_{\mu\nu} + O(\alpha') = 0$$

**Natura del flusso**
* RG = condizione di consistenza, non dinamica IR reale
* Fixed points = CFT (teorie conformi)

### ⚖️ Confronto RG
| Proprietà | SPU | String Theory |
| :--- | :--- | :--- |
| **Tipo di RG** | fisico, IR emergente | worldsheet, vincolo |
| **Fixed point** | IR non banale ($\delta_*$) | CFT ($\beta=0$) |
| **Dipendenza UV** | debole | forte (background) |
| **Dinamica collettiva** | sì | no |

👉 **Vantaggio SPU:** RG fisico reale, non solo consistenza matematica.

---

## 2. DOF Counting (gradi di libertà)

### SPU: DOF topologici finiti
$N_f^{\mathrm{nom}} = \dim H^*(E_7/SU(8)) = 128$

**Effettivi:**
$N_f^{\mathrm{eff}} = 128 - \delta \approx 127.37$

**Scaling effettivo:**
$N_{\mathrm{eff}}(\mu) \sim N_f^{\mathrm{eff}} \cdot \delta(\mu)$

👉 DOF limitati, discreti, topologici

### String Theory: DOF infiniti
**Spettro:**
$m_n^2 \sim \frac{n}{\alpha'}$

**Degenerazione:**
$\rho(n) \sim e^{\sqrt{n}} \to$ densità stati: $\rho(E) \sim e^{E / T_H}$ (Hagedorn)

**Implicazioni**
* DOF esponenzialmente crescenti
* Sistema quasi-termico intrinseco

### ⚖️ Confronto DOF
| Proprietà | SPU | String Theory |
| :--- | :--- | :--- |
| **Numero DOF** | finito (~128) | infinito |
| **Crescita** | polinomiale | esponenziale |
| **Origine** | topologia | oscillatori |
| **UV behavior** | controllato | Hagedorn |

👉 **Vantaggio SPU:** controllabilità e chiusura matematica.

---

## 3. Scaling Laws

### SPU: scaling collettivo non-estensivo
**Scala fondamentale:**
$\Lambda_{\mathrm{SP}} \sim \sqrt{N_f} \, M_{\mathrm{GUT}}$

**Planck scale:**
$M_{\mathrm{Pl}}^2 \sim \frac{N_f^{\mathrm{eff}}}{96\pi^2} M_{\mathrm{GUT}}^2 \cdot f_{\mathrm{IR}}$ con $f_{\mathrm{IR}} \sim 4.8$

**Vacuum energy (non-estensiva):**
$\rho_\Lambda \sim N_f^\alpha M_{\mathrm{GUT}}^4, \quad \alpha < 1$

👉 Soppressione naturale

### String Theory: scaling geometrico
**Azione efficace:**
$S \sim \frac{1}{g_s^2} \int d^{10}x \sqrt{g} \, R \to M_{\mathrm{Pl}}^2 \sim \frac{V_6}{g_s^2 \alpha'^4}$

**Vacuum energy:**
$\Lambda \sim \frac{1}{\alpha'^2} \to$ enorme senza tuning

### ⚖️ Confronto scaling
| Proprietà | SPU | String Theory |
| :--- | :--- | :--- |
| **Origine scala** | collettiva | geometrica |
| **Dipendenza** | $\sqrt{N_f}$ | $V_6, g_s$ |
| **$\Lambda$ naturale** | piccola | enorme |
| **Parametri liberi** | 0 | molti |

👉 **Vantaggio SPU:** scaling interno, non parametrico.

---

## 4. Sintesi matematica finale

### SPU (forma compatta)
$$
\begin{aligned}
M_{\mathrm{Pl}}^2 &\sim \frac{N_f}{96\pi^2} M_{\mathrm{GUT}}^2 \cdot f_{\mathrm{IR}} \\
\delta_* &\approx 0.633 \\
N_f &= 128 \\
f_{\mathrm{IR}} &\sim 4.8
\end{aligned}
$$

**Sistema:** chiuso, discreto, non perturbativo, senza parametri liberi.

### String Theory (forma compatta)
$$
\begin{aligned}
M_{\mathrm{Pl}}^2 &\sim \frac{V_6}{g_s^2 \alpha'^4} \\
\rho(E) &\sim e^{E/T_H} \\
\beta^i &= 0
\end{aligned}
$$

**Sistema:** continuo, infinito, dipendente da parametri, landscape-dominated.



