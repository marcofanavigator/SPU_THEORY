# SPU Framework  
## Symmetry–Phase–Unification  

[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17962427.svg)](https://doi.org/10.5281/zenodo.17962427)  
[MIT License](LICENSE) • [Contact](mailto:marcofa@protonmail.com)

---

## Abstract

SPU (Symmetry–Phase–Unification) è un framework teorico minimale dove le interazioni di gauge del Modello Standard, la gravità e la costante cosmologica emergono dinamicamente da un mezzo fermionico comune radicato nel coset simmetrico **E₇ / SU(8)**.

L'unificazione avviene **senza**:
- gruppi di grande unificazione (GUT)
- supersimmetria
- dimensioni extra
- gravità quantistica fondamentale

Tutte le scale e i coupling emergono da:
- capacità geometrica fermionica
- soppressione dinamica dei modi via effetti QFT
- flusso RG sullo spettro discreto del Laplaciano del coset

La teoria è spettrale: partendo dall'operatore di Laplace–Beltrami sul coset compatto, la gravità e lo spazio-tempo emergono come risposta collettiva IR. È UV-finita, falsificabile e robusta.

---

## Principi Fondamentali

### 1. Capacità Geometrica Fermionica

Il coset E₇ / SU(8) ha dimensione coomologica 128, fissando la capacità nominale:

$$N_f^{\mathrm{nom}} = \dim H^*(E_7/SU(8)) = 128$$

### 2. Soppressione Dinamica dei Modi

Il decoupling QFT standard riduce i modi attivi:

$$N_f^{\mathrm{eff}}(\mu) = 128 - \delta(\mu)$$

dove $\delta(\mu) \sim 0.5$–$0.7$ a basse energie.

### 3. Emergenza Spettrale

Gravità, spazio-tempo e $\Lambda$ emergono dalla proiezione IR dello spettro del coset.

---

## Fondazione Geometrica e Spettrale

Lo spazio simmetrico compatto è

$$M = E_7 / SU(8)$$

con:
- $\dim(E_7) = 133$
- $\dim(SU(8)) = 63$
- $\dim(M) = 70$ (reale)

L'operatore fondamentale è il Laplace–Beltrami $\Delta$ su $M$, con spettro discreto $\{\lambda_n, g_n\}$. Primo autovalore normalizzato:

$$\lambda_1 = 2$$

### Azione spettrale minimale:

$$S_{\mathrm{SPU}}(\mu) = \sum_n g_n \log\left(1 + \frac{\lambda_n}{\mu^2}\right)$$

---

## Soppressione Dinamica δ(μ)

### Peso IR:

$$w(\lambda_n, \mu) = \frac{\lambda_n}{\lambda_n + \mu^2}$$

### Soppressione:

$$\delta(\mu) = 1 - \frac{1}{N} \sum_n g_n w(\lambda_n, \mu) \quad (N = \sum g_n)$$

### Flusso:

- **UV** ($\mu \to \infty$): $w \to 0$ → $\delta \to 1$ (decoupling)
- **IR** ($\mu \to 0$): $w \to 1$ → $\delta \to 0$ (modi attivi)

Vedi `docs/derivation_delta.md`.

---

## Unificazione di Gauge Emergente

### RG one-loop standard:

$$\beta(g_i) = -\frac{b_0}{16\pi^2} g_i^3$$

con $b_0$ da $N_f^{\mathrm{eff}}$. Convergenza a:

$$M_{\mathrm{GUT}} \sim 10^{16}\,\mathrm{GeV}$$

**senza SUSY**.

### Predizioni:

- $1/\alpha_{\mathrm{em}} \approx 137$
- $\tau_p \sim 10^{34}$–$10^{35}$ anni
- $r \sim 0.03$

---

## Gravità Emergente e Spazio-Tempo

### Gravità da correlatore IR:

$$g^{\mathrm{eff}}_{\mu\nu}(x) \propto \langle \partial_\mu \phi_{\mathrm{IR}}(x) \partial_\nu \phi_{\mathrm{IR}}(x) \rangle$$

### Costante di Newton:

$$G_{\mathrm{eff}}(\mu) \propto \frac{\mu^2}{\delta(\mu)}$$

Comportamento:
- $G_{\mathrm{eff}} \to 0$ (libertà asintotica UV)
- $G_{\mathrm{eff}} \to G_N$ (classica IR)

### Spazio-tempo:

Proiezione IR $56 \to 8$ modi leggeri → $\mathbb{R}^{1,3}$.

---

## Costante Cosmologica Emergente

$$\Lambda(\mu) = \mu^4 \sum_n g_n \log\left(1 + \frac{\lambda_n}{\mu^2}\right)$$

**Limite IR:** $\Lambda \to 0^+$ (positiva, lenta). Equazione di stato $w \to -1$ come attrattore RG.

---

## Validazione Numerica

### Script disponibili:

- `fixed_point_delta.py` — punto fisso di δ
- `rg_running.py` — evoluzione dei gauge
- `stability_scan.py` — scansioni di robustezza
- `spectral_sum.py` — somme sui modi (approssimazione di Weyl)

### Stabilità:

Variazione δ 10–20% → cambio output <5%.

---

## Confronto e Falsificabilità

### Differisce da:

- **GUT**: nessun embedding
- **Stringhe**: nessun landscape
- **Asymptotic safety**: nessuna gravità UV

### Predizioni falsificabili:

| Predizione | Valore | Esperimento |
|---|---|---|
| No running di G | — | Test precision gravity |
| $r$ (tensor-to-scalar) | $\sim 0.03$ | CMB-S4 |
| Vita protone | $\sim 10^{34}$–$10^{35}$ yr | Hyper-K |
| $\Lambda$ dinamica | — | Euclid/DESI |

**Fallimento falsifica SPU.**

---

## License

**MIT** — vedi [LICENSE](LICENSE)

---

## Contact

**Marco Fanavigator**  
marcofa@protonmail.com  
Zenodo: https://doi.org/10.5281/zenodo.17962427

---

## Citazione

> "In physics, we don't just ask 'does it work?' We ask 'why is it true?'"  
> SPU asks the second question — and the structure answers naturally.
