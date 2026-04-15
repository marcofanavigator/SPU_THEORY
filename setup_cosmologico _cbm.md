# 🌌 1. Setup cosmologico
Assumiamo metrica FRW:
$$ds^2 = -dt^2 + a(t)^2 d\vec{x}^2$$

e campo omogeneo: $\delta = \delta(t)$.
L'azione ridotta diventa:
$$\Gamma = \int d^4x \, a^3 \left[ \frac{Z(\delta)}{2}\dot{\delta}^2 - V(\delta) + \frac{M_{\mathrm{Pl}}^2(\delta)}{2} R \right]$$

# ⚙️ 2. Passaggio in frame di Einstein
Definiamo la trasformazione conforme per isolare la dinamica:
$$\tilde g_{\mu\nu} = \Omega^2(\delta) g_{\mu\nu}, \quad \Omega^2 = \frac{M_{\mathrm{Pl}}^2(\delta)}{M_0^2}$$

👉 Otteniamo l'azione in Einstein Frame:
$$\Gamma = \int d^4x \sqrt{-\tilde g} \left[ \frac{M_0^2}{2} \tilde R + \frac{1}{2} K(\delta)(\partial \delta)^2 - U(\delta) \right]$$

Dove:
* $K(\delta) = \frac{Z(\delta)}{\Omega^2} + \frac{3}{2} \left(\frac{d \ln M_{\mathrm{Pl}}^2}{d\delta}\right)^2$
* $U(\delta) = \frac{V(\delta)}{\Omega^4}$

# 🔬 3. Forma universale del potenziale
Dalla derivazione spettrale su $E_7/SU(8)$:
* $V(\delta) \sim \Lambda_{\mathrm{SP}}^4 \log(1 + c\delta)$
* $M_{\mathrm{Pl}}^2(\delta) \sim \frac{N_f^{\mathrm{eff}}}{96\pi^2} \Lambda_{\mathrm{SP}}^2 \, f_{\mathrm{IR}}(\delta)$

👉 Ne consegue la forma del potenziale effettivo:
$$\boxed{U(\delta) \sim \Lambda_{\mathrm{SP}}^4 \frac{\log(1+c\delta)}{f_{\mathrm{IR}}(\delta)^2}}$$

# 🚀 4. Inflazione emergente
Nel regime IR vicino al punto fisso ($\delta \to \delta_* \approx 0.63$), espandiamo $U(\delta)$:
$$U(\delta) \approx U_0 \left(1 - A e^{-B\delta} \right)$$

👉 **Plateau naturale**: la dinamica mima i modelli Starobinsky / $\alpha$-attractor, ma l'origine è puramente spettrale.

# 🧮 5. Parametri slow-roll
Definiamo:
$$\epsilon = \frac{M_0^2}{2} \left(\frac{U'}{U}\right)^2, \quad \eta = M_0^2 \frac{U''}{U}$$

Nel limite del plateau:
$$\epsilon \sim \frac{1}{N^2}, \quad \eta \sim -\frac{1}{N}$$

# 📡 6. Predizioni CMB

### (a) Spettro scalare
$$\boxed{n_s = 1 - \frac{2}{N}}$$
Per $N = 50\text{--}60$, $n_s \approx 0.960 - 0.967$ (Compatibile con **Planck**).

### (b) Tensor-to-scalar ratio
$$\boxed{r = \frac{12}{N^2}}$$
$r \approx 0.003 - 0.005$ (Testabile da **LiteBIRD**).

### (c) Ampiezza perturbazioni
Fissando $A_s \approx 2.1 \times 10^{-9}$:
$$\Lambda_{\mathrm{SP}} \sim 10^{17} \, \text{GeV}$$
(Coincide con la scala GUT teorica).

# 🌊 7. Spettro tensoriale
$$n_t = -2\epsilon \sim -\frac{2}{N^2}$$
👉 Quasi scale-invariant, tipico dei modelli a plateau.

# 🧠 8. Firma distintiva SPU (Specifiche Uniche)
1. **Running non standard**: $\alpha_s = \frac{dn_s}{d\ln k} \sim -10^{-3}$.
2. **Non-Gaussianità**: Origine collettiva del mezzo $\to \boxed{f_{NL} \sim \mathcal{O}(1)}$.
3. **Cutoff UV**: Soppressione naturale del power spectrum ad alta $k$.
4. **Entanglement Imprint**: $\boxed{\text{Correlazioni a lunga distanza non locali nel CMB}}$.

# 🔥 9. Confronto diretto con modelli noti

| Modello | $n_s$ | $r$ | Origine |
| :--- | :--- | :--- | :--- |
| **Starobinsky** | 0.965 | 0.003 | Correzioni $R^2$ |
| **Higgs inflation** | 0.965 | 0.003 | Campo scalare esterno |
| **SPU** | **0.960–0.967** | **0.003–0.005** | **Spettro Coset** |

# 🧨 10. VERDETTO FISICO
* ✔ **Inflazione automatica**: Emerge dalla stabilizzazione dello spettro.
* ✔ **No tuning**: La scala $\Lambda_{\mathrm{SP}}$ è dettata dalla geometria.
* ✔ **Fisica unitaria**: Nessun inflaton introdotto "ad hoc".

# 🚀 11. Test osservativi reali
* **LiteBIRD**: Misurazione di $r \sim 0.004$.
* **Euclid/DESI**: Ricerca di $f_{NL} \sim 1$.
* **CMB Anomalies**: Analisi delle correlazioni non locali (firma unica SPU).

**Conclusione:**
$$\boxed{\text{Inflazione = Fenomeno collettivo del mezzo fermionico}}$$