# w(t) in SPU: Equazione di Stato come Funzione Indotta di δ(t)

## 1 Che cos'è davvero w in SPU 

In cosmologia standard:
$$w = \frac{p}{\rho}$$

è definito a livello macroscopico.

**In SPU invece:**
- w non è fondamentale
- Emerge dalla dipendenza temporale dell'energia del vuoto
- Che a sua volta dipende da δ(t)

 **In SPU:**
$$\boxed{w(t) \;\text{è una funzione indotta da}\; \delta(t)}$$

---

## 2 Relazione Generale (senza ansatz)

Per qualsiasi fluido cosmologico:
$$\dot{\rho} + 3H(1+w)\rho = 0$$

Da cui:
$$w = -1 - \frac{1}{3H}\frac{d \ln \rho}{dt}$$

**Questa identità è esatta, non dipende dal modello.**

---

## 3 Energia del Vuoto in SPU

In SPU:
$$\rho_\Lambda(t) = \rho_\Lambda\bigl(\delta(t)\bigr)$$

con proprietà già dimostrate:

1. $\rho_\Lambda(\delta)$ è liscia
2. $\frac{d\rho_\Lambda}{d\delta} < 0$
3. $\rho_\Lambda$ è finita solo vicino a $\delta^*$

---
4 RG Flow di δ (ingrediente cruciale)
 
:
$$\frac{d\delta}{d\ln\mu} = \beta_\delta(\delta)$$

con:
$$\beta_\delta(\delta^*) = 0, \quad \beta_\delta'(\delta^*) < 0$$

👉 **δ* è un attrattore IR**

Ora, in cosmologia:
$$\mu \sim H$$

quindi:
$$\dot{\delta} = \beta_\delta(\delta)\,H$$

---

## 5 Derivazione Diretta di w


$$\frac{d\ln\rho_\Lambda}{dt} = \frac{1}{\rho_\Lambda} \frac{d\rho_\Lambda}{d\delta} \dot{\delta}$$

$$= \frac{1}{\rho_\Lambda} \frac{d\rho_\Lambda}{d\delta} \beta_\delta(\delta)\,H$$

Inserendo nella definizione di w:

$$\boxed{ w = -1 - \frac{1}{3} \frac{d\ln\rho_\Lambda}{d\delta} \beta_\delta(\delta) }$$

**Questa è l'equazione centrale.**

---


6 Analisi Vicino al Punto Fisso

Espandiamo vicino a δ*:

$$\beta_\delta(\delta) \simeq -\gamma(\delta - \delta^*) \quad (\gamma > 0)$$

$$\frac{d\ln\rho_\Lambda}{d\delta} \simeq \text{costante}$$

Allora:
$$w + 1 \;\propto\; (\delta - \delta^*)$$

---

## 7 Attrattore Dinamico (qui sta il punto)

Poiché:
$$\delta(t) \;\longrightarrow\; \delta^* \quad \text{per } t \to \infty$$

segue necessariamente che:
$$\boxed{ w(t) \;\longrightarrow\; -1 }$$

**Indipendentemente da:**
- Condizioni iniziali
- Valore iniziale di w
- Parametrizzazioni

👉 Non è un valore imposto  
👉 Non è un fine tuning  
👉 **È un attrattore RG**

---

## 8 Perché Questo è Concettualmente Enorme

Nessuna teoria standard ha questo:

| Teoria | Perché w ≈ −1? |
|--------|---|
| **ΛCDM** | Per definizione |
| **Quintessenza** | Per tuning del potenziale |
| **EFT DE** | Parametrizzazione |
| **SPU** | RG + spettro microscopico |

**SPU dice:**
> L'universo accelera perché il numero effettivo di gradi di libertà fermionici deve rilassarsi verso δ*.

---

## Riepilogo Concettuale

### Struttura Logica

1. **Microscopica:** RG flow di δ verso δ* (attrattore)
2. **Termodinamica:** ρ_Λ(δ) dipende da δ
3. **Cinematica cosmologica:** w emerge da ρ̇_Λ
4. **Macroscopia:** w(t) → −1 automaticamente

### Predizioni Osservabili

- **Lungo transizione:** $w(z)$ varia lentamente
- **Oggi:** $w_0 \approx -1$ (con deviazione misurabile)
- **Domani:** effetti a redshift moderato da test precisi

### Il Punto Filosofico

In SPU non chiediamo "perché w = −1?"

Chiediamo "perché δ → δ*?"

E la risposta è: **perché è un punto fisso stabile dell'RG flow.**

---

## Notazione Essenziale

- **w**: Equazione di stato (parameter di densità)
- **δ(t)**: Funzione dinamica di riduzione dei gradi di libertà
- **δ***: Valore di equilibrio (attrattore IR)
- **β_δ(δ)**: Funzione beta dell'RG flow
- **H**: Parametro di Hubble
- **ρ_Λ**: Densità di energia del vuoto efficace
- **μ**: Scala di rinormalizzazione (cosmologicamente ~ H)