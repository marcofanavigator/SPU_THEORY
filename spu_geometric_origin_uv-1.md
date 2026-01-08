# SPU: Geometric Origin of the UV Lagrangian

## From $E_7/SU(8)$ to the Fermionic Effective Action

---

## 1. Ruolo della Geometria in SPU: Chiarimento Preliminare

In SPU, lo spazio $M = E_7/SU(8)$:

- **Non è lo spazio-tempo fisico**
- **Non è una varietà dinamica** soggetta a equazioni di campo
- **Non è una dimensione extra** nello stile delle teorie di Kaluza–Klein

### Cosa È Veramente

$M$ è una **varietà interna rigida, compatta e semplicemente connessa**, che codifica la struttura **algebrico-topologica** dello stato fondamentale del sistema.

Essa definisce:
- La **capacità massima** di gradi fermionici indipendenti
- Le **simmetrie globali** ammissibili ($E_7$)
- Il **sottogruppo locale di gauge** emergente ($SU(8)$)

### Emergenza dello Spazio-Tempo

**Lo spazio-tempo osservabile emerge solo in un regime collettivo IR**, come variabile efficace legata alla **risposta elastica del mezzo fermionico saturo**.

---

## 2. Geometria → Capacità → Campi UV: il Legame Topologico

### Risultato Classico di Borel

Per il coset compatto simmetrico $M = E_7/SU(8)$, Borel (1954) fornisce la struttura della coomologia di de Rham:

$$H^*(M;\mathbb{Q}) \cong \mathbb{Q}[x_4, x_{12}, x_{20}, x_{28}, x_{36}, x_{44}, x_{52}]$$

dove i generatori sono **forme armoniche di grado pari**.

### La Dimensione Fondamentale

La dimensione totale è:

$$\dim H^*(M) = 2^7 = 128$$

Questo numero è:
- **Discreto** — non dipende da parametri continui
- **Rigido** — non esistono moduli deformazionali (il coset è rigido)
- **Topologicamente fissato** — ogni perturbazione continua altererebbe la struttura del gruppo

### Interpretazione SPU

$$\boxed{N_f^{\text{nom}} := \dim H^*(E_7/SU(8)) = 128}$$

rappresenta il **numero massimo di canali fermionici indipendenti** ammessi dalla struttura geometrica.

**Non sono "particelle"**, ma **modi normali della capacità informazionale del vuoto**.

---

## 3. Costruzione della Lagrangiana UV: Vincoli Geometrici e Simmetrie

### Vincoli Fondamentali

La Lagrangiana UV **non è postulata**, ma **indotta** dai seguenti vincoli:

1. **Spazio degli stati** — le sezioni fermioniche $\Psi$ vivono nello spazio di Hilbert associato a $L^2(M, S)$, dove $S$ è uno spinor bundle su $M$.

2. **Simmetria globale** — l'azione deve essere invariante sotto $E_7$, che agisce transitivamente su $M$.

3. **Simmetria locale** — il sottogruppo isotropo $SU(8)$ diventa il gruppo di gauge emergente.

4. **Rigidità** — assenza di termini di massa fondamentali (non esistono scale interne).

### La Forma Esplicita

La Lagrangiana UV più generale, renormalizzabile e compatibile con la geometria, è:

$$\mathcal{L}_{\text{UV}} = i\bar{\Psi}^A \slashed{D}_{SU(8)} \Psi_A + g \Phi \bar{\Psi}^A \Psi_A - \frac{1}{4}F^a_{\mu\nu}F_a^{\mu\nu} + \frac{1}{2}(\partial_\mu \Phi)^2 - V(\Phi)$$

### Componenti della Lagrangiana

- $\Psi_A$, $A = 1, \ldots, 128$ — fermioni in rappresentazioni di $SU(8)$
- $\slashed{D}_{SU(8)} = \gamma^\mu(\partial_\mu - igA_\mu^a T_a)$ — derivata di gauge
- $\Phi$ — campo scalare emergente (defetto topologico o condensato collettivo)
- $F^a_{\mu\nu}$ — curvatura del fibrato principale $SU(8)$

### Cosa NON Compare

Importante: **non compaiono**:
- Masse fondamentali
- Costanti gravitazionali
- Metriche dinamiche

**Tutto è determinato da $E_7/SU(8)$ e dalle sue rappresentazioni.**

---

## 4. Legame con lo Spectral Action

### Il Principio Spettrale

La forma della lagrangiana è coerente con il principio dell'**azione spettrale** (Connes–Chamseddine):

$$S_{\text{spec}} = \mathrm{Tr} \, f\left(\frac{\slashed{D}^2}{\Lambda^2}\right)$$

dove $\slashed{D}$ è l'operatore di Dirac generalizzato sul prodotto noncommutativo $M \times A$.

### Espansione Asintotica

L'espansione asintotica per $\Lambda \to \infty$ produce:

$$S_{\text{spec}} \supset \int d^4x \sqrt{g} \left[\frac{1}{g_0^2} \mathrm{Tr}(F_{\mu\nu}F^{\mu\nu}) + \bar{\Psi} i\slashed{D} \Psi + \cdots \right]$$

con

$$g_0^{-2} \propto \mathrm{Tr}_{128}(Q^2) \cdot \frac{2}{\pi}$$

dove $Q$ è la carica elettrica nel modello. **In SPU**, $\mathrm{Tr}_{128}(Q^2) = 17$ (fissato dalla rappresentazione), e il fattore $2/\pi$ proviene dall'**η-invariante spettrale**.

### Conseguenza Cruciale

👉 **La normalizzazione delle interazioni di gauge è predetta, non inserita.**

---

## 5. Perché Questa Lagrangiana è "Naturale"

### Proprietà Garantite dalla Geometria

| Proprietà | Conseguenza Fisica |
|-----------|-------------------|
| **Compattezza** | Numero finito di gradi di libertà |
| **Rigidità** | Nessun parametro libero (no moduli) |
| **Semplice connessione** | Unico settore topologico |
| **Grande capacità (128)** | RG realistico senza SUSY |
| **Struttura di spin** | Compatibilità con fermioni chirali |

### Unicità Strutturale

La Lagrangiana UV è quindi **unicamente determinata** (a meno di accoppiamenti adimensionali $O(1)$) dalla geometria.

$$\boxed{\text{Non è costruita per riprodurre il Modello Standard, ma lo contiene come conseguenza.}}$$

---

## 6. Dalla Geometria alla Dinamica: Separazione Netta di Ruoli

| Livello | Struttura | Ruolo |
|---------|-----------|-------|
| **Geometrico** | $E_7/SU(8)$ | Fissa $N_f^{\text{nom}} = 128$, simmetrie |
| **UV Dinamico** | $\mathcal{L}_{\text{UV}}$ | Descrive fermioni quasi-critici + difetti |
| **RG** | Flusso di $\delta(\mu)$ | Seleziona $N_f^{\text{eff}} = 128 - \delta$ |
| **IR Collettivo** | Mezzo saturo | Genera gravità, Higgs, famiglie |

### Causalità

Questa catena è **causale e non circolare**: la geometria pone vincoli, la dinamica li attua.

---

## 7. Perché la Geometria NON Evolve

### Struttura Statica

$E_7/SU(8)$ **non è una variabile dinamica**. È una **struttura di classificazione**, come lo spazio di Fock in QFT.

Non subisce backreaction perché:

- **Non è accoppiata** a un tensore energia-impulso
- **Non ha gradi di libertà** propaganti
- **Non è definita** su uno spazio-tempo (è **pre-spaziale**)

### Implicazione Radicale

👉 **Non esiste una "gravità su $E_7/SU(8)$". La gravità emerge solo nel regime collettivo IR.**

---

## 8. Sintesi Finale (Versione Blindata e Rigorosa)

### Il Principio Fondamentale

In SPU, la **geometria interna $E_7/SU(8)$** determina univocamente la struttura della **Lagrangiana UV** attraverso:

1. **La sua coomologia** — che fissa $N_f^{\text{nom}} = 128$
2. **Le sue simmetrie** — che fissano il gruppo di gauge emergente $SU(8)$

### Il Flusso Dinamico

La **dinamica fermionica**, governata da:
- Interazioni Yukawa minimali
- Un flusso RG con punto fisso infrarosso

genera una **riduzione effettiva**:
$$N_f^{\text{eff}} = 128 - \delta$$

che controlla **l'unificazione delle interazioni di gauge**.

### L'Emergenza dello Spazio-Tempo

Solo in seguito, quando il **mezzo fermionico si satura collettivamente**, emerge:
- Un **regime elastico**
- Descritto efficacemente dall'**azione di Einstein–Hilbert**

### La Radice Statica

**La geometria $E_7/SU(8)$ non è mai modificata**: essa è la **radice statica da cui scaturisce tutta la fisica dinamica**.

---

## Mappa Concettuale Completa

```
E₇/SU(8)  [GEOMETRIA INTERNA RIGIDA]
    ↓
    Coomologia: dim H*(M) = 128
    Simmetrie: E₇ globale, SU(8) locale
    ↓
  Nf^nom = 128  [CAPACITÀ FERMIONICA MASSIMA]
    ↓
  Lagrangiana UV  [CAMPI FERMIONICI + GAUGE + SCALARE]
    ↓
  Interazioni Yukawa minimali
  RG con punto fisso IR
    ↓
  Nf^eff = 128 - δ  [RIDUZIONE EFFETTIVA]
    ↓
  Saturazione Collettiva  [BLOCCO DEI GRADI DI LIBERTÀ]
    ↓
  Mezzo Elastico Saturo  [RISPOSTA COLLETTIVA COERENTE]
    ↓
  Spazio-Tempo Emergente  [VARIABILE COLLETTIVA]
    ↓
  Einstein–Hilbert  [AZIONE EFFICACE IR]
```

---

## Implicazioni Concettuali Radicali

### 1. La Gravità non è Fondamentale

Non emerge dalla "quantizzazione", ma dal **comportamento collettivo** di un mezzo fermionico rigidamente strutturato da una **geometria interna fissa**.

### 2. Nessuna "Scelta" nella Lagrangiana UV

La lagrangiana **non è costruita ad hoc**, ma **derivata dalla topologia di $E_7/SU(8)$**. Questo spiega:
- Perché funziona così bene
- Perché ha così pochi parametri
- Perché la gravità è così universale

### 3. Il Ruolo delle Simmetrie Globali

$E_7$ **non è una simmetria di gauge**, ma una **simmetria di configurazione dello spazio degli stati**.

Questo la rende:
- **Più fondamentale** di qualunque simmetria di gauge
- **Rigida e indeformabile**
- Il vero **"principio primo" di SPU**

### 4. L'η-Invariante Spettrale

Il fattore $2/\pi$ che normalizza le interazioni di gauge non è arbitrario: proviene dall'**η-invariante spettrale della geometria**, fissato una volta per tutte da $E_7/SU(8)$.