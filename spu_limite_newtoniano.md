# SPU: Recupero del Limite Newtoniano da Einstein–Hilbert

---

## Punto di Partenza (già stabilito)

In SPU, nel regime IR:

$$S_{\text{eff}}[g] \;=\; \int d^4x\,\sqrt{-g}\, M_{\text{Pl}}^2\, R \;+\; S_{\text{matter}}[g,\psi]$$

con:
- $M_{\text{Pl}}$ emergente
- Accoppiamento universale
- Nessun campo gravitazionale extra

Da qui discendono le **equazioni di Einstein classiche**.

---

## Le Approssimazioni Necessarie per il Limite Newtoniano

Il limite newtoniano non è un limite ontologico, ma un **limite cinetico e geometrico**. Servono quattro approssimazioni, tutte fisicamente motivate in SPU.

---

## 1. Approssimazione di Campo Debole (Weak-Field Expansion)

### Matematica

Si espande la metrica attorno a Minkowski:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \qquad |h_{\mu\nu}| \ll 1$$

### Significato Fisico in SPU

- Il mezzo fermionico è **poco deformato**
- Le perturbazioni sono **elastiche**, non plastiche
- Siamo a lunghezze $\gg \ell_{\mathrm{SP}}$

👉 **Questa approssimazione fallirebbe vicino a singolarità, ma SPU non le ammette → il regime è ben definito.**

---

## 2. Approssimazione Non Relativistica (Slow-Motion Limit)

### Matematica

Per le sorgenti:

$$v \ll c, \qquad p \ll \rho$$

quindi lo stress–energy si riduce a:

$$T_{00} \approx \rho, \qquad T_{0i} \approx 0, \qquad T_{ij} \approx 0$$

### Significato Fisico in SPU

- Le eccitazioni del mezzo sono **quasi statiche**
- Non si propagano **modi tensoriali dinamici** (onde gravitazionali)
- Il mezzo **risponde quasi istantaneamente**

---

## 3. Approssimazione Quasi-Statica (Neglect of Time Derivatives)

### Matematica

Si trascurano le derivate temporali rispetto a quelle spaziali:

$$\partial_t h_{\mu\nu} \ll \partial_i h_{\mu\nu}$$

### Significato Fisico in SPU

- L'RG è **congelato**
- Il mezzo fermionico è in **equilibrio locale**
- Non stiamo eccitando il **settore collettivo dinamico**

👉 **Questa approssimazione è naturale in SPU perché:**
- La gravità **non è propagazione UV**
- È una **risposta IR** del mezzo

---

## 4. Identificazione del Potenziale Newtoniano

### Matematica

Nel gauge newtoniano:

$$g_{00} = -(1 + 2\Phi), \qquad g_{ij} = (1 - 2\Phi)\delta_{ij}$$

con $|\Phi| \ll 1$.

Inserendo questa forma nelle equazioni di Einstein linearizzate si ottiene:

$$\nabla^2 \Phi = 4\pi G_N \rho$$

### Significato Fisico in SPU

- $\Phi$ è la **deformazione scalare** del mezzo
- L'accelerazione è una **forza elastica efficace**
- $G_N$ misura la **compliance del medium**

---

## Riassunto Compatto delle Approssimazioni

| Approssimazione | Contenuto Matematico | Significato in SPU |
|---|---|---|
| **Campo debole** | $\|h_{\mu\nu}\| \ll 1$ | Mezzo poco deformato |
| **Non relativistico** | $v \ll c$ | Nessun modo dinamico |
| **Quasi-statica** | $\partial_t \ll \partial_x$ | Equilibrio collettivo |
| **IR regime** | $\lambda \gg \ell_{\mathrm{SP}}$ | Spazio continuo valido |

**Nessuna approssimazione è arbitraria:** tutte discendono dal fatto che stai lavorando molto al di sotto della scala SPU.

---

## Perché NON Servono altre Ipotesi

Importante: **non servono in SPU:**
- Assunzioni su particelle test
- Gravitoni
- Quantizzazione del campo
- Correzioni MOND
- Termini non locali

Il limite newtoniano è **automatico** una volta che:

1. L'azione EH domina
2. Il mezzo è nel **regime elastico IR**

---

## Risposta Finale (da Tenere Fissa)

Il limite newtoniano in SPU si ottiene applicando le stesse **approssimazioni cinematiche e geometriche** valide in GR (campo debole, moto lento, quasi-staticità), **giustificate fisicamente** dal fatto che la gravità è una **risposta collettiva elastica del mezzo fermionico** a scale molto maggiori di $\ell_{\mathrm{SP}}$.

### Conseguenza Cruciale

La **compatibilità totale** di SPU con il limite newtoniano non è un'aggiunta posteriore, ma una **conseguenza diretta** della struttura dell'emergenza gravitazionale in SPU: non si postula, si **deriva**.

---

## Mappa Concettuale

```
SPU (mezzo fermionico saturo)
         ↓
    Azione EH emerge
         ↓
    Equazioni di Einstein
         ↓
    Approssimazioni (h ≪ 1, v ≪ c, ∂_t ≪ ∂_x)
         ↓
    Equazione di Poisson
         ↓
    Gravità Newtoniana
```

Ogni passaggio è **fisicamente motivato** e **non postulato**.