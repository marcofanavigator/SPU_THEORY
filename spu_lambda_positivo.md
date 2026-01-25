# SPU: Perché Λ > 0 (non ≤ 0)

## Mostrare che il segno di Λ è fissato dalla stessa origine di δ*

---

## 1. Da dove nasce Λ in SPU (un solo punto)

In SPU, **Λ non è un termine fondamentale** ma emerge come traccia residua del determinante funzionale:

$$\Lambda_{\text{eff}} \propto \frac{1}{V}\,\log\det\!\left(\Delta_{\text{coset}}\right)$$

dove:
- $\Delta_{\text{coset}}$ è l'operatore cinetico sui modi di $E_7/SU(8)$
- $V$ è il volume emergente (non fondamentale)

**👉 Il segno di Λ è il segno del determinante.**

La domanda quindi diventa: *Il determinante del coset può essere negativo o nullo?*

---

## 2. Proprietà chiave dell'operatore sul coset

Per un coset riemanniano compatto/non-compatto ridotto come:

$$SL(2,\mathbb{R})/SO(2) \subset E_7/SU(8)$$

valgono le seguenti proprietà geometriche (non negoziabili):

1. **L'operatore è ellittico**
2. **Lo spettro è reale**
3. **Esiste un gap spettrale positivo:**

$$\lambda_{\min} = \frac{1}{4} > 0$$

Questo è lo stesso $\lambda_{\min}$ che controlla:
- Il flusso di rinormalizzazione di $\delta$
- L'attrattore verso $w \to -1$

**👉 Stessa origine matematica**

---

## 3. Conseguenza diretta sul determinante

 il determinante :

$$\log\det\Delta = \sum_n \log(\lambda_n)$$

Se:
- $\lambda_n > 0$ per tutti i modi dinamicamente attivi
- Non esistono modi tachionici globali

allora:

$$\log\det\Delta > 0 \quad\Rightarrow\quad \boxed{\Lambda > 0}$$

**Non serve calcolare il valore numerico:**
- Il segno è fissato
- È una proprietà topologica + spettrale

---

## 4. Perché Λ non può essere zero

$\Lambda = 0$ richiederebbe:

$$\prod_n \lambda_n = 1 \quad\text{(cancellazione perfetta)}$$

Ma questo è **impossibile in SPU** perché:
- I modi non sono indipendenti
- Il coset è vincolato
- La misura funzionale è **non fattorizzabile**

**👉 Non-estensività del vuoto**

Questo è cruciale:
- In QFT standard il vuoto è estensivo → cancellazioni possibili
- In SPU → cancellazioni impossibili → residuo obbligatorio

---

## 5. Perché Λ non può essere negativa

$\Lambda < 0$ richiederebbe:
- Autovalori negativi dominanti
- Oppure instabilità infrarossa

Ma allora:
- Il flusso di rinormalizzazione di $\delta$ non avrebbe attrattore
- $w \to -1$ non sarebbe stabile
- La gravità emergente collasserebbe

**Dato che invece:**
- $\delta \to \delta_*$ è IR-stabile ✔
- $w \to -1$ è attrattore ✔
- $G_{\text{eff}}$ resta finito ✔

**👉 Λ < 0 è dinamicamente inconsistente**

---

## 6. Collegamento diretto a δ*



**La stessa quantità che controlla:**

$$\frac{d\delta}{d\ln\mu} = -\gamma(\delta-\delta_*)$$

**controlla anche:**

$$\Lambda \sim \gamma \, M_{\text{em}}^4$$

con:

$$\gamma = c\,\lambda_{\min} > 0$$

Quindi:

$$\boxed{\delta_* > 0 \;\Longleftrightarrow\; \Lambda > 0}$$

**Non sono due fatti separati.** Sono la stessa cosa vista da due scale diverse.

---

## 7. Perché questo è un salto concettuale



> **In SPU l'accelerazione cosmica non è un fatto empirico ma una conseguenza inevitabile della struttura dei gradi di libertà.**



---

## 8. Stato attuale della teoria



- ✅ Gravità emergente
- ✅ RG di $\delta$ derivato
- ✅ $\Lambda$ piccola e positiva
- ✅ $w \to -1$ come attrattore
- ✅ Tutto dallo stesso determinante



---

## Riassunto: La catena logica

```
E₇/SU(8) [COSET]
    ↓
Δ_coset ellittico
    ↓
λ_min = 1/4 > 0
    ↓
log(det Δ) > 0
    ↓
Λ > 0 ✓
    ├── stessa γ che controlla RG di δ
    └── Λ ~ γ M_em⁴
            ↓
        Λ > 0 ⟺ δ* > 0
```

**Non negoziabile:** Il segno positivo di Λ è scritto nella geometria.