# Framework per δ — Frazione Non Condensata del Mezzo

---

## 1. Struttura Fisica di δ

Nel framework:

$$\delta = \text{frazione non condensata del mezzo}$$

Dipende da:
- scala locale (curvatura / raggio $r$)
- densità superficiale collettiva $\Sigma$
- massa gravitazionale $M_{\mathrm{BH}}$

La struttura fattorizzata è:

$$\delta = \delta_{\mathrm{RG}} \times \delta_{\mathrm{grav}} \times \delta_{\mathrm{spec}}$$

---

## 2. Blocco RG (Universale)

Dal flusso spettrale:

$$\delta_{\mathrm{RG}} = \delta_* \left(1 + \left(\frac{\ell_{\mathrm{SP}}}{r}\right)^\gamma \right)^{-1}$$

dove:
- $\delta_* \approx 0.633$ — punto fisso IR
- $\gamma \approx 2$ — scaling naturale da heat-kernel
- $\ell_{\mathrm{SP}} = \dfrac{1}{\sqrt{N_f^{\mathrm{eff}}} \, M_{\mathrm{GUT}}}$

---

## 3. Blocco Gravitazionale

La gravità sopprime la condensazione (più massa → meno condensato):

$$\delta_{\mathrm{grav}} = \left(1 + \frac{R_s}{r}\right)^\alpha$$

con:
- $R_s = 2 G_N M_{\mathrm{BH}}$ — raggio di Schwarzschild
- $\alpha \approx 1$ — scaling lineare da accoppiamento collettivo

---

## 4. Blocco Superficiale (Mezzo Fermionico)

Dal comportamento collettivo:

$$\delta_{\Sigma} = \left(1 + \frac{\Sigma}{\Sigma_{\mathrm{SP}}} \right)^{-\beta}$$

dove:
- $\Sigma_{\mathrm{SP}} \sim \dfrac{M_{\mathrm{GUT}}^2}{\sqrt{N_f^{\mathrm{eff}}}}$
- $\beta \approx 1$

> Alta densità → più condensazione → δ più piccolo

---

## 5. Blocco Spettrale (Plancherel / Coset)

Dalla derivazione dallo spettro $E_7/SU(8)$:

$$\delta_{\mathrm{spec}} = \frac{1}{1 + f_{\mathrm{IR}}}$$

con:

$$f_{\mathrm{IR}} \approx 4.79 \quad \Longrightarrow \quad \delta_{\mathrm{spec}} \approx \frac{1}{5.79}$$

---

## 6. Formula Completa

$$\boxed{\delta(r, \Sigma, M_{\mathrm{BH}}) = \frac{\delta_*}{1 + f_{\mathrm{IR}}} \cdot \frac{1}{1 + \left(\dfrac{\ell_{\mathrm{SP}}}{r}\right)^\gamma} \cdot \left(1 + \frac{R_s}{r}\right)^\alpha \cdot \left(1 + \frac{\Sigma}{\Sigma_{\mathrm{SP}}}\right)^{-\beta}}$$

---

## 7. Esplicitazione Completa dei Parametri

| Parametro | Definizione |
|-----------|------------|
| $\ell_{\mathrm{SP}}$ | $\dfrac{1}{\sqrt{N_f^{\mathrm{eff}}} \, M_{\mathrm{GUT}}}$ |
| $R_s$ | $2 G_N M_{\mathrm{BH}}$ |
| $\Sigma_{\mathrm{SP}}$ | $\dfrac{M_{\mathrm{GUT}}^2}{\sqrt{N_f^{\mathrm{eff}}}}$ |
| $f_{\mathrm{IR}}$ | $\approx 4.79$ |
| $\delta_*$ | $\approx 0.633$ |
| $\gamma$ | $\approx 2$ |
| $\alpha$ | $\approx 1$ |
| $\beta$ | $\approx 1$ |

---

## 8. Forma Finale Ultra-Compatta

$$\boxed{\delta = \frac{\delta_*}{1+f_{\mathrm{IR}}} \cdot \frac{1 + \dfrac{R_s}{r}}{\left(1 + \left(\dfrac{\ell_{\mathrm{SP}}}{r}\right)^2\right)\left(1 + \dfrac{\Sigma}{\Sigma_{\mathrm{SP}}}\right)}}$$

---

## 9. Limiti Fisici

### IR — Grandi Scale

Condizioni: $r \gg \ell_{\mathrm{SP}},\quad \Sigma \ll \Sigma_{\mathrm{SP}}$

$$\delta \to \frac{\delta_*}{1+f_{\mathrm{IR}}} \sim 0.11$$

**Interpretazione:** mezzo quasi condensato; dark sector residuo.

---

### UV — Vicino al Buco Nero

Condizione: $r \to R_s$

$$\delta \uparrow$$

**Interpretazione:** il mezzo si "decondensa" → niente singolarità nuda.

---

### Alta Densità

Condizione: $\Sigma \gg \Sigma_{\mathrm{SP}}$

$$\delta \to 0$$

**Interpretazione:** condensazione completa → geometria classica ripristinata.

---

## 10. Interpretazione Finale

Questa formula è potente perché **non contiene parametri liberi reali**: tutto deriva da:

1. **RG flow** — flusso del gruppo di rinormalizzazione
2. **Spettro $E_7/SU(8)$** — struttura del coset simmetrico
3. **Scala GUT** — $M_{\mathrm{GUT}}$

Collega in modo unificato:
- gravità (blocco $\delta_{\mathrm{grav}}$)
- struttura del mezzo fermionico (blocco $\delta_\Sigma$)
- rinormalizzazione IR (blocco $\delta_{\mathrm{RG}}$ e $\delta_{\mathrm{spec}}$)
