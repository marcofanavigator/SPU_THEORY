# La Metrica Efficace come Correlatore IR  
## Chiusura del Cerchio SPU: Dallo Spazio Matematico allo Spazio Fisico

### Obiettivo
Derivare la metrica efficace $g^{\text{eff}}_{\mu\nu}$ come **correlatore collettivo** dei modi IR del coset $E_7/SU(8)$, senza assumerla a priori.

$$
\boxed{g^{\text{eff}}_{\mu\nu}(x) \propto \langle \partial_\mu \phi_{\text{IR}}(x)\, \partial_\nu \phi_{\text{IR}}(x) \rangle}
$$

### 1. Idea Centrale (Chiara e Minimale)
In SPU, la metrica **non è fondamentale**: emerge come correlatore collettivo dei modi IR del coset.

**Formulazione**:
Sia $\phi(x)$ il campo associato agli autostati del Laplaciano su $E_7/SU(8)$.  
La metrica spaziotempo emerge come il **kernel di propagazione** delle fluttuazioni IR:

$$
\boxed{g_{\mu\nu}^{\text{eff}}(x) \propto \langle \partial_\mu \phi_{\text{IR}}(x)\, \partial_\nu \phi_{\text{IR}}(x) \rangle}
$$

dove:
- $\phi_{\text{IR}}$ = componenti degli autostati che contribuiscono in IR,
- $\langle \cdot \rangle$ = correlatore quantistico dal propagatore spettrale,
- Nessuna geometria assunta a priori.

### 2. Decomposizione Spettrale (Nessun Ansatz)
**Campo come somma sui modi del coset**:

$$
\phi(x) = \sum_n a_n \psi_n(x)
$$

dove:
- $\psi_n(x)$ = autofunzioni del Laplaciano,
- $a_n$ = ampiezze (variabili dinamiche),
- $\Delta \psi_n = \lambda_n \psi_n$.

**Propagatore Euclideo dalla teoria spettrale**:

$$
\boxed{\langle a_n a_m \rangle = \frac{\delta_{nm}}{\lambda_n + \mu^2}}
$$

**Interpretazione**:
- $\mu$ = scala IR (parametro di coarse-graining),
- Il denominatore $\lambda_n + \mu^2$ emerge naturalmente dall'azione spettrale,
- Nessuna ipotesi su quantizzazione o QFT standard.

### 3. Proiettore IR Naturale (Qui Entra δ)
**Peso spettrale IR** (corretto per coerenza con flusso RG di SPU):

$$
\boxed{w(\lambda_n) = \frac{\lambda_n}{\lambda_n + \mu^2}}
$$

**Proprietà**:
- $w \to 0$ per $\mu \to \infty$ (UV: modi alti decoupled),
- $w \to 1$ per $\mu \to 0$ (IR: modi bassi attivi),
- $0 < w < 1$ sempre (normalizzato).

**Punto cruciale**: Questo peso **non è un ansatz** — è il propagatore normalizzato, estratto dal denominatore dell'azione spettrale.

**Interpretazione fisica**:
Il peso $w(\lambda_n)$ misura la **frazione di contributo IR** di ogni modo: modi bassi dominano in IR, modi alti sono congelati in UV.

### 4. Definizione Esplicita della Metrica Emergente
**Correlatore a due punti dei campi**:

$$
\langle \phi(x) \phi(y) \rangle = \sum_n \frac{\psi_n(x) \psi_n(y)}{\lambda_n + \mu^2}
$$

**Derivando due volte (per ottenere la metrica)**:
Il correlatore delle derivate è:

$$
g^{\text{eff}}_{\mu\nu} \propto \sum_n g_n \, w(\lambda_n) \, \partial_\mu \psi_n(x) \, \partial_\nu \psi_n(x)
$$

dove:
- $g_n$ = degenerazioni,
- Somma su tutti i modi.

**Isotropia del coset**:
Il coset $E_7/SU(8)$ è omogeneo e isotropo (sotto l'azione di $E_7$).  
Perciò il correlatore non ha direzioni preferite:

$$
\boxed{g^{\text{eff}}_{\mu\nu} = C(\mu) \, \eta_{\mu\nu}}
$$

dove:
- $\eta_{\mu\nu}$ = metrica di Minkowski (o Euclidea, a seconda della segnatura),
- $C(\mu)$ = fattore di normalizzazione dinamico.

**Fattore di normalizzazione dinamico**:

$$
\boxed{C(\mu) = \sum_n g_n \frac{\mu^2}{\lambda_n + \mu^2}}
$$

**Osservazione**: Questo fattore conta il numero effettivo di modi che contribuiscono alla metrica a ogni scala $\mu$.

### 5. Qui Nasce δ(μ) (Senza Assumerlo)
**Definizione di δ(μ) come soppressione dinamica** (coerente con SPU precedente):

$$
\boxed{\delta(\mu) = 1 - \frac{1}{N} \sum_n g_n w(\lambda_n) = 1 - \frac{1}{N} \sum_n g_n \frac{\lambda_n}{\lambda_n + \mu^2}}
$$

dove $N = \sum_n g_n$ (numero totale di modi).

**Significato fisico**:
- δ(μ) = **frazione di modi decoupled** (soppressione media),
- Emerge naturalmente come complemento del peso IR,
- Non è un parametro libero: determinato dallo spettro.

**Flusso con la scala** (corretto):
- **Regime UV** ($\mu \to \infty$): w → 0 → δ → 1 (decoupling quasi totale),
- **Regime IR** ($\mu \to 0$): w → 1 → δ → 0 (modi bassi attivi, soppressione minima).

### 6. Gravità Emergente: G_eff(μ)
**Rigidità della metrica**:
La costante di Newton emerge come inversa della rigidità del correlatore IR:

$$
\boxed{G_{\text{eff}}(\mu) \propto \frac{\mu^2}{\delta(\mu)}}
$$

**Interpretazione fisica**:

| Regime | δ(μ)     | G_eff(μ)              | Significato                          |
|--------|----------|-----------------------|--------------------------------------|
| **UV** | δ → 1    | G_eff → 0             | Gravità debole/asintoticamente libera|
| **IR** | δ → 0    | G_eff → costante finita| Gravità classica (Newtoniana)        |

**La fisica**:
- Pochi modi attivi (δ basso) → metrica rigida → G finito in IR,
- Molti modi decoupled (δ alto) → metrica flessibile → G piccolo in UV,
- Nessun input gravitazionale: emerge dallo spettro.

### 7. Collegamento Diretto con Λ e w
**Perché w = -1 è automatico**:
- Λ deriva dal **determinante dello stesso spettro** (residuo IR positivo),
- La metrica è la **statistica collettiva IR**,
- Non ci sono gradi di libertà dinamici indipendenti per Λ → p = -ρ automaticamente (attrattore dinamico nel flusso RG).

In SPU:
- w = -1 è il **minimo locale dello spazio dei parametri IR**,
- È un **attrattore dinamico** sotto il flusso RG,
- Nessun fine-tuning necessario.

### 8. Dove Siamo Ora (Punto Reale)
**Chiusura del cerchio SPU**:
- **Spazio matematico → Spazio fisico**: coset astratto $E_7/SU(8)$ diventa varietà fisica $\mathbb{R}^{1,3}$,
- **Metrica emergente**: derivata come correlatore a due punti dei modi IR,
- **RG di δ derivato**: emerge dal propagatore spettrale,
- **G_eff e Λ dalla stessa azione**: entrambi determinati dallo spettro,
- **w = -1 come attrattore IR**: conseguenza della struttura spettrale.

**Questo è il cuore della teoria SPU: tutto emerge coerentemente da un unico principio minimalista.**

### Conclusione
La metrica dello spaziotempo non è **postulata**, ma **derivata** come **correlatore quantistico** dei modi fondamentali del vuoto. Questo cambio di prospettiva trasforma la gravità da problema irrisolto della fisica quantistica a **conseguenza naturale della struttura spettrale del vuoto**.
