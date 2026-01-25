# Fissazione del Segno di Λ in SPU e Collegamento a δ*

## 1 Fissare il Segno di Λ in SPU (Λ > 0)

### Punto Chiave

In SPU, Λ non è un input cosmologico, ma un **termine costante dell'azione efficace IR**, derivante da:

$$S_{\text{eff}} = -\log \det \mathcal{O}_{\text{SPU}}$$

dove $\mathcal{O}$ è l'operatore cinetico/interazione dei modi non protetti del coset $E_7/SU(8)$.

### Perché il Segno è Positivo (senza ambiguità)

#### (a) Natura dello Spettro

Nel sotto-coset fisico:
- Gli autovalori $\lambda_i$ di $\mathcal{O}$ sono **positivi**
- Non esiste simmetria $\lambda \leftrightarrow -\lambda$
- Non c'è supersimmetria → nessuna cancellazione

Quindi:
$$\log \det \mathcal{O} = \sum_i \log \lambda_i > 0$$

👉 **Il termine costante dell'azione è positivo**

#### (b) Non-Estensività (punto cruciale)

**In QFT standard:**
$$\rho_\Lambda \propto N_{\text{dof}} \Lambda_{\text{UV}}^4$$

**In SPU:**
- I gradi di libertà **non sono indipendenti**
- Sono correlati dal coset
- La riduzione $128 \to 128-\delta$ è **dinamica**

**Risultato:**
$$\rho_\Lambda \text{ non scala linearmente}$$

👉 Non può annullarsi  
👉 Non diverge  
👉 Resta positiva

#### (c) Conclusione sul Segno

$$\boxed{\Lambda_{\text{SPU}} > 0 \quad \text{necessariamente}}$$

**Non per:**
- Scelta
- Tuning
- Osservazione

**Ma per struttura microscopica.**

---

## 2 Collegamento Diretto Λ ↔ δ*

### Origine Comune

Lo stesso determinante produce:

| Termine | Effetto |
|---------|---------|
| $\Lambda_{\text{UV}}^4$ | Costante cosmologica |
| $\Lambda_{\text{UV}}^2 R$ | Gravità emergente |
| Log-corrections | RG flow di $\delta$ |

👉 **Un solo oggetto, tre fenomeni**

### Dipendenza Funzionale

Dopo RG flow:
$$N_f^{\text{eff}} = 128 - \delta^*$$

e quindi:
$$\Lambda_{\text{eff}} \propto F(128 - \delta^*)$$

con:
- $F'(N_f^{\text{eff}}) < 0$
- $\delta = 0$ → Λ enorme (UV instabile)
- $\delta = \delta^*$ → Λ finita

👉 **δ* è ciò che rende Λ fisicamente accettabile.**

### Interpretazione Fisica 

> L'universo accelera perché **non possiede abbastanza gradi di libertà fermionici indipendenti** per cancellare l'energia del vuoto.

**Questo è nuovo.** Non esiste in nessun paradigma standard.

---

## 3 Perché Questo Chiude un Cerchio Concettuale

Con questi due punti :

- ✔️ **Segno di Λ fissato** (strutturalmente)
- ✔️ **Collegamento a RG flow** (via δ*)
- ✔️ **Origine comune con la gravità** (stesso determinante)
- ✔️ **Assenza totale di ansatz cosmologici** (tutto emerge microscopicamente)

E soprattutto:

$$\boxed{\delta^* \text{ diventa il parametro centrale di tutta la fisica IR}}$$

---

## Appendice: Notazione Essenziale

- **SPU**: Struttura fisica dell'universo
- **E₇/SU(8)**: Coset fondamentale
- **Λ**: Costante cosmologica efficace
- **δ**: Riduzione dinamica dei gradi di libertà (128 → 128−δ)
- **δ***: Valore fisico di δ determinato da RG flow
- **Nf^eff**: Numero effettivo di fermioni indipendenti
- **ℒ**: Operatore cinetico/interazione
- **Seff**: Azione efficace infrarossi