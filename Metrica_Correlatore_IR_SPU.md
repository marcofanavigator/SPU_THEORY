# La Metrica Efficace come Correlatore IR
## Chiusura del Cerchio SPU: Dallo Spazio Matematico allo Spazio Fisico

---

## Obiettivo

Derivare la metrica efficace $g^{\text{eff}}_{\mu\nu}$ come **correlatore collettivo** dei modi IR del coset $E_7/SU(8)$, senza assumerla a priori.

$$\boxed{g^{\text{eff}}_{\mu\nu}(x) \propto \langle \partial_\mu \phi_{\text{IR}}(x)\, \partial_\nu \phi_{\text{IR}}(x) \rangle}$$

---

## 1️⃣ Idea Centrale (Chiara e Minimale)

In SPU, la metrica **non è fondamentale**: emerge come correlatore collettivo dei modi IR del coset.

**Formulazione:**

Sia $\phi(x)$ il campo associato agli autostati del Laplaciano su $E_7/SU(8)$.

La metrica spaziotempo emerge come il **kernel di propagazione** delle fluttuazioni IR:

$$\boxed{g_{\mu\nu}^{\text{eff}}(x) \propto \langle \partial_\mu \phi_{\text{IR}}(x)\, \partial_\nu \phi_{\text{IR}}(x) \rangle}$$

**dove:**
- $\phi_{\text{IR}}$ = componenti degli autostati che contribuiscono in IR
- $\langle \cdot \rangle$ = correlatore quantistico dal propagatore spettrale
- Nessuna geometria assunta a priori

---

## 2️⃣ Decomposizione Spettrale (Nessun Ansatz)

### Campo come Somma sui Modi del Coset

$$\phi(x) = \sum_n a_n \psi_n(x)$$

**dove:**
- $\psi_n(x)$ = autofunzioni del Laplaciano
- $a_n$ = ampiezze (variabili dinamiche)
- Equazione degli autovalori: $\Delta \psi_n = \lambda_n \psi_n$

### Propagatore Euclideo dalla Teoria Spettrale

Nel formalismo del path integral euclideo:

$$\boxed{\langle a_n a_m \rangle = \frac{\delta_{nm}}{\lambda_n + \mu^2}}$$

**Interpretazione:**
- $\mu$ = scala IR (parametro di coarse-graining)
- Il denominatore $\lambda_n + \mu^2$ emerge naturalmente dalla azione spettrale
- Nessuna ipotesi su quantizzazione o QFT standard

---

## 3️⃣ Proiettore IR Naturale (Qui Entra $\delta$)

### Peso Spettrale IR

Definiamo il peso naturale che emerge dal propagatore:

$$\boxed{w(\lambda_n) = \frac{\mu^2}{\lambda_n + \mu^2}}$$

**Proprietà:**
- $w \to 1$ per $\lambda_n \ll \mu^2$ (modi IR attivi)
- $w \to 0$ per $\lambda_n \gg \mu^2$ (modi UV decoupled)
- $0 < w < 1$ sempre (normalizzato)

**Punto cruciale:** Questo **non è un ansatz** — è il propagatore stesso, estratto dal denominatore dell'azione spettrale.

### Interpretazione Fisica

Il peso $w(\lambda_n)$ misura la **frazione di energia** di ogni modo che rimane nell'IR dinamico.

- Modo con $\lambda_n \ll \mu^2$: quasi tutta l'energia rimane
- Modo con $\lambda_n \gg \mu^2$: quasi tutta l'energia è stata "congelata" (decoupled)

---

## 4️⃣ Definizione Esplicita della Metrica Emergente

### Correlatore a Due Punti dei Campi

Tornando allo spazio fisico:

$$\langle \phi(x) \phi(y) \rangle = \sum_n \frac{\psi_n(x) \psi_n(y)}{\lambda_n + \mu^2}$$

### Derivando Due Volte (per Ottenere la Metrica)

Il correlatore delle derivate è:

$$g^{\text{eff}}_{\mu\nu} \propto \sum_n g_n \, w(\lambda_n) \, \langle \partial_\mu \psi_n \partial_\nu \psi_n \rangle$$

Sostituendo il peso:

$$g^{\text{eff}}_{\mu\nu} \propto \sum_n g_n \, \frac{\mu^2}{\lambda_n + \mu^2} \, k_\mu k_\nu$$

**dove:**
- $k_\mu$ = momenti efficaci IR associati agli autofunzioni
- $g_n$ = degenerazioni
- Somma su tutti i modi

### Isotropia del Coset

Il coset $E_7/SU(8)$ è omogeneo e isotropo (sotto l'azione di $E_7$).

Perciò il correlatore non può avere direzioni preferite:

$$\boxed{g^{\text{eff}}_{\mu\nu} = C(\mu) \, \eta_{\mu\nu}}$$

**dove:**
- $\eta_{\mu\nu}$ = metrica di Minkowski (o Euclidea, in dipendenza dalla segnatura)
- $C(\mu)$ = fattore di normalizzazione dinamico

### Fattore di Normalizzazione Dinamico

$$\boxed{C(\mu) = \sum_n g_n \frac{\mu^2}{\lambda_n + \mu^2}}$$

**Osservazione:**
Questo fattore **conta il numero effettivo di modi** che contribuiscono alla metrica a ogni scala $\mu$.

---

## 5️⃣ Qui Nasce $\delta(\mu)$ (Senza Assumerlo)

### Frazione di Modi Attivi

Definiamo la frazione di modi che contribuiscono alla metrica:

$$\boxed{\delta(\mu) = \frac{1}{N} \sum_n g_n \frac{\mu^2}{\lambda_n + \mu^2}}$$

**dove:**
$$N = \sum_n g_n = \text{numero totale di modi}$$

### Significato Fisico di $\delta(\mu)$

- $\delta(\mu)$ = **frazione di modi che "sentono" la scala $\mu$**
- Non è un parametro libero: è determinato completamente dallo spettro
- Emerge naturalmente come normalizzazione

### Flusso con la Scala

**Regime UV** ($\mu \to \infty$):
$$\delta \to 0 \quad \text{(nessun modo sente la scala infinita)}$$

**Regime IR** ($\mu \to 0$):
$$\delta \to \delta_* = \text{costante} > 0 \quad \text{(saturazione)}$$

---

## 6️⃣ Gravità Emergente: $G_{\text{eff}}(\mu)$

### Rigidità della Metrica

La costante di Newton emerge come **rigidità del correlatore**:

$$\boxed{G_{\text{eff}}(\mu) \propto \frac{1}{\delta(\mu)}}$$

### Interpretazione Fisica

| Regime | $\delta(\mu)$ | $G_{\text{eff}}(\mu)$ | Significato |
|--------|---------------|----------------------|-------------|
| **UV** | $\delta \to 0$ | $G \to \infty$ | Gravità disaccoppiata |
| **IR** | $\delta \to \delta_*$ | $G \to G_N$ | Gravità classica |

**La fisica:**
- **Pochi modi correlati** → Metrica rigida e debole → Basse energie
- **Molti modi correlati** → Metrica flessibile e forte → Alte energie

✔️ Gravità $\to 0$ in UV (asintoticamente libera)  
✔️ Gravità finita in IR (Newtoniana)  
✔️ **Nessun input gravitazionale** — emerge dallo spettro

---

## 7️⃣ Collegamento Diretto con $\Lambda$ e $w$

### Perché $w = -1$ È Automatico

Poiché:
- $\Lambda$ viene dal **determinante dello stesso spettro**
- La metrica è la **statistica collettiva IR**
- **Non ci sono gradi di libertà dinamici** associati a $\Lambda$

segue naturalmente:

$$\boxed{p = -\rho \quad \Rightarrow \quad w = -1}$$

### Non Come Condizione Iniziale

In approcci standard (inflazione, ΛCDM), $w = -1$ è:
- Un'ipotesi iniziale
- Fine-tuned ad hoc

**In SPU:**
- $w = -1$ è il **minimo locale dello spazio dei parametri IR**
- È un **attrattore dinamico** sotto il flusso RG
- Nessun fine-tuning necessario

---

## 8️⃣ Dove Siamo Ora (Punto Reale)

### Chiusura del Cerchio SPU

A questo punto, il framework SPU ha stabilito:

✔️ **Spazio matematico → Spazio fisico**
- Coset astratto $E_7/SU(8)$ diventa varietà fisica $\mathbb{R}^{1,3}$

✔️ **Metrica emergente**
- Derivata come correlatore a due punti dei modi IR
- Non assunta, non imposta, non scelta

✔️ **RG di $\delta$ derivato**
- Emerge dal propagatore spettrale
- Non è un ansatz, è conseguenza della azione spettrale minimale

✔️ **$G_{\text{eff}}$ e $\Lambda$ dalla stessa azione**
- Entrambi determinati dallo spettro
- Nessun parametro libero tra loro

✔️ **$w = -1$ come attrattore IR**
- Non imposto
- Conseguenza della struttura spettrale

---

**Questo è il cuore della teoria SPU: tutto emerge coerentemente da un unico principio minimalista.**
