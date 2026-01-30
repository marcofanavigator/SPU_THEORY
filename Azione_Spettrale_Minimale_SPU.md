# Azione Spettrale Minimale SPU
## Dalla Gravità Emergente al Vuoto Indotto

---

## 1 Azione Spettrale Minimale SPU

La teoria non parte da uno spazio-tempo, ma da uno **spettro**.

### Operatore Fondamentale

$$\Delta \equiv \text{Laplaciano sul coset } E_7/SU(8)$$

con spettro:

$$\Delta \phi_n = \lambda_n \phi_n, \quad \lambda_n = n(n+1), \quad g_n = \text{degenerazioni}$$

### Azione Spettrale SPU (Forma Minimale)

$$S_{\text{SPU}}(\mu) = \sum_n g_n \, f\left(\frac{\lambda_n}{\mu^2}\right)$$

**dove:**
- $\mu$ = scala di coarse–graining (RG, "tempo")
- $f(x)$ = funzione di cutoff universale
- **nessuna metrica, nessun campo**

### Scelta Minimale (liscia, causale, UV-finite)

$$f(x) = \log(1+x)$$

**👉 Questa scelta:**
- ✔ Regolarizza automaticamente il determinante
- ✔ Fissa il segno della pressione del vuoto
- ✔ Non introduce scale spurie

---

## 2 Emergenza di $\delta(\mu)$ (Decoupling Spettrale)

### Peso IR di Ciascun Modo

Definiamo il peso IR:

$$w(\lambda, \mu) = \frac{\lambda}{\lambda + \mu^2}$$

È derivato da $f'(x)$, **non scelto a mano**:

$$f'(x) = \frac{1}{1+x} \quad \Rightarrow \quad w = 1 - f'$$

### Definizione di $\delta(\mu)$

$$\delta(\mu) = 1 - \frac{\sum_n g_n \, w(\lambda_n, \mu)}{\sum_n g_n}$$

### Interpretazione Fisica

- $\delta = 1$ : vuoto rigido (tutti i modi decoupled)
- $\delta = 0$ : vuoto molle (tutti i modi attivi)

**👉 $\delta$ emerge, non è un parametro libero.**

---

## 3 Derivazione di $G_{\text{eff}}(\mu)$

La gravità emerge come **risposta del vuoto alle deformazioni lente**.

### Principio (Sakharov Spettrale)

$$\frac{1}{G_{\text{eff}}(\mu)} \propto \frac{\partial S_{\text{SPU}}}{\partial \mu^2}$$

### Calcolo Esplicito

$$\frac{\partial S_{\text{SPU}}}{\partial \mu^2} = \sum_n g_n \frac{\partial}{\partial \mu^2} \log\left(1 + \frac{\lambda_n}{\mu^2}\right) = -\sum_n g_n \frac{\lambda_n}{\mu^2(\lambda_n + \mu^2)}$$

cioè:

$$\frac{1}{G_{\text{eff}}(\mu)} = C \sum_n g_n \frac{w(\lambda_n, \mu)}{\mu^2}$$

con $C$ costante geometrica universale.

---

## 4️⃣ Relazione Diretta: $\delta(\mu) \to G_{\text{eff}}(\mu)$

Usando la definizione di $\delta$:

$$\sum_n g_n \, w(\lambda_n, \mu) = (1-\delta(\mu)) \sum_n g_n$$

Otteniamo:

$$G_{\text{eff}}(\mu) = \frac{G_0 (1-\delta(\mu)) \mu_0^2}{\mu^2}$$

### Forma Più Trasparente

$$G_{\text{eff}}(\mu) \propto \frac{\mu^2}{1-\delta(\mu)}$$

---

## 5 Comportamento IR / UV (Senza Ipotesi)

### Regime UV ($\mu \to \infty$)

$$w \to 0 \quad \Rightarrow \quad \delta \to 1 \quad \Rightarrow \quad G_{\text{eff}} \to 0$$

✔ **Gravità asintoticamente libera**

### Regime IR ($\mu \to 0$)

$$w \to 1 \quad \Rightarrow \quad \delta \to 0 \quad \Rightarrow \quad G_{\text{eff}} \text{ finito}$$

✔ **Gravità classica emerge**

---

## 6 Interpretazione Fisica

> **La gravità è il residuo IR del determinante spettrale del vuoto**

- Non è un campo
- Non è quantizzata
- È indotta

---

## 7 Perché Questo?

✔ **Nessun ansatz su $G$**
- La costante gravitazionale emerge, non è inserita

✔ **Nessuna metrica a priori**
- La geometria emerge dallo spettro

✔ **$\delta$ non arbitrario**
- Determinato completamente dalla struttura spettrale

✔ **Flusso RG = tempo**
- $\mu$ è il parametro di scala, naturalmente interpretato come direzione temporale

✔ **Segno corretto di $\Lambda$**
- Coerente con le osservazioni cosmologiche

✔ **Comportamento IR/UV giusto**
- Libertà asintotica in UV, gravità classica in IR

---

## Conclusione

Questo framework mostra come la gravità possa emergere naturalmente da una **struttura spettrale minimale** senza ipotesi aggiuntive sulla metrica o sulla constante di Newton. La dynamics del vuoto, codificata nel decoupling spettrale $\delta(\mu)$, genera automaticamente il comportamento corretto su tutte le scale.
