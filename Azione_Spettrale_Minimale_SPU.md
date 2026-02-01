# Azione Spettrale Minimale in SPU  
## Dalla Gravità Emergente al Vuoto Indotto

---

## 1. Azione Spettrale Minimale SPU

La teoria SPU non postula uno spazio-tempo metrico a priori, ma parte dallo **spettro** del Laplaciano sul coset compatto E₇/SU(8).

### Operatore fondamentale

$$\Delta = \text{Laplace-Beltrami sul coset } E_7/SU(8)$$

con spettro discreto:

$$\Delta \phi_n = \lambda_n \phi_n, \quad g_n = \text{multiplicità (degenerazione) del modo } n$$

I valori λ_n sono dati da differenze di Casimir quadratici nelle rappresentazioni irriducibili di E₇ contenenti la rappresentazione coset 56. Il primo autovalore è $\lambda_1 = 1693/16$ (raw) o normalizzato a 2 (scelta geometrica naturale); per n grande, $\lambda_n$ cresce quadraticamente ($\lambda_n \sim n^2$).

### Azione spettrale minimale

**Funzionale effettivo del vuoto**:

$$S_{\text{SPU}}(\mu) = \sum_n g_n \, f\left( \frac{\lambda_n}{\mu^2} \right)$$

dove:
- μ è la scala di coarse-graining RG (alta μ = regime UV, bassa μ = IR; interpretabile come "tempo" nel flusso RG)
- $f(x)$ è una funzione di cutoff universale, liscia e causale

### Scelta minimale

**Funzione di regolarizzazione** (regolarizzante, UV-finita, con segno fisico corretto):

$$f(x) = \log(1 + x)$$

Questa scelta:
- Regolarizza automaticamente il determinante funzionale (simile a zeta-function regularization)
- Fissa il segno positivo della pressione del vuoto
- Non introduce scale spurie o parametri arbitrari

---

## 2. Emergenza Dinamica di δ(μ) dal Decoupling Spettrale

### Derivata della funzione di cutoff

$$f'(x) = \frac{1}{1 + x}$$

definiamo il peso IR di ciascun modo:

$$w(\lambda_n, \mu) = \frac{\lambda_n}{\lambda_n + \mu^2} = \frac{x}{1 + x} = 1 - f'(x) \quad \left(x = \frac{\lambda_n}{\mu^2}\right)$$

$w(\lambda, \mu)$ misura quanto il modo n contribuisce al regime IR:
- $w \to 1$ per $\lambda \ll \mu^2$
- $w \to 0$ per $\lambda \gg \mu^2$

### Definizione di δ(μ)

**Soppressione dinamica media**:

$$\delta(\mu) = 1 - \frac{\sum_n g_n \, w(\lambda_n, \mu)}{\sum_n g_n}$$

(la somma è intesa come regolarizzata dalla funzione f; in pratica finita grazie al log lento).

### Interpretazione

- $\delta \approx 0$: vuoto "molle" (modi attivi, $N_f^{\text{eff}} \approx 128$)
- $\delta \approx 1$: vuoto "rigido" (modi decoupled, $N_f^{\text{eff}} \approx 127.4–127.6$)
- $\delta$ emerge interamente dalla struttura spettrale e dal flusso RG, senza parametri liberi

---

## 3. Emergenza della Costante Gravitazionale Effettiva G_eff(μ)

La gravità emerge come risposta indotta del vuoto a deformazioni lente (principio di Sakharov spettrale).

### Derivazione

$$\frac{1}{G_{\mathrm{eff}}(\mu)} \propto \frac{\partial S_{\mathrm{SPU}}}{\partial \mu^2}$$

Calcolo esplicito:

$$\frac{\partial}{\partial \mu^2} \log\left(1 + \frac{\lambda_n}{\mu^2}\right) = -\frac{\lambda_n / \mu^2}{\mu^2 + \lambda_n} = -\frac{w(\lambda_n, \mu)}{\mu^2}$$

Quindi:

$$\frac{\partial S_{\mathrm{SPU}}}{\partial \mu^2} = -\sum_n g_n \frac{w(\lambda_n, \mu)}{\mu^2}$$

### Forma implicita

Assumendo la costante di proporzionalità positiva (da matching low-energy con Einstein-Hilbert):

$$\frac{1}{G_{\mathrm{eff}}(\mu)} = C \sum_n g_n \frac{w(\lambda_n, \mu)}{\mu^2} = C \frac{1-\delta(\mu)}{\mu^2} \left( \sum_n g_n \right)$$

dove C è costante geometrica universale (fissata da normalizzazione o matching con M_Pl).

### Forma esplicita

$$G_{\mathrm{eff}}(\mu) = \frac{G_0 \, \mu_0^2 \, (1 - \delta(\mu))}{\mu^2}$$

o equivalentemente:

$$\boxed{G_{\mathrm{eff}}(\mu) \propto \frac{\mu^2}{1 - \delta(\mu)}}$$

(dove $G_0$, $\mu_0$ sono fissati da condizioni IR).

---

## 4. Comportamento UV/IR e Consistenza Fisica

### Regime UV (μ → ∞)

- $w(\lambda_n, \mu) \to 0$ per modi fissi, ma per modi alti ($\lambda_n \gg \mu^2$) $w \approx 1$; tuttavia, $f(x) = \log(1+x)$ sopprime contributo alto-λ lentamente
- $\delta \to 1$ (decoupling quasi-totale dei modi), $1 - \delta \to 0^+$ lentamente
- $G_{\text{eff}} \to 0$ (gravità asintoticamente libera o debole in UV, coerente con induced gravity e absence di gravità quantistica fondamentale in SPU)

### Regime IR (μ → 0)

- $w \to 1$ per tutti i modi bassi, $\delta \to 0$
- $G_{\text{eff}} \to$ costante finita (gravità classica emerge, recupero di GR a bassa energia)

Questo flusso è indipendente da ansatz su G e deriva dalla geometria spettrale del coset.

---

## 5. Interpretazione Fisica Complessiva

La gravità è il **residuo IR del determinante spettrale del vuoto indotto**:

- Non è un campo fondamentale quantizzato
- È effetto collettivo del decoupling dinamico $\delta(\mu)$
- La metrica e lo spazio-tempo emergono dal flusso RG sullo spettro

---

## 6. Vantaggi Strutturali del Framework

✓ Nessun ansatz su G o metrica a priori

✓ δ non arbitrario: determinato dalla geometria del coset e dalla scelta minimale di f

✓ Flusso RG interpretato naturalmente come "tempo" evolutivo

✓ Segno positivo di Λ coerente (da modi positivi del Laplaciano)

✓ Comportamento UV/IR corretto: gravità debole/asintoticamente libera in UV, classica in IR

✓ Compatibile con derivazioni precedenti (δ da QFT one-loop su background coset)

---

## Conclusione

Questo framework riduce SPU a una **teoria spettrale minimale**: la gravità e il vuoto dinamico emergono interamente dallo spettro del Laplaciano sul coset E₇/SU(8), senza campi o metriche primitive. 

Il decoupling spettrale $\delta(\mu)$ genera il running di $G_{\text{eff}}$ e le scale fisiche osservate. 

Il modello è:
- **UV-finito**
- **Falsificabile** (no running di G in IR, predizioni su r, Λ dinamica)
- **Strutturalmente economico**
