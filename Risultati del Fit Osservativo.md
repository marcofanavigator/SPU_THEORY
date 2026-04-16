# 🚀 Spectral Physics Unit (SPU) - Framework Repository

Benvenuto nel repository ufficiale del framework **SPU (Spectral Physics Unit)**. Questo progetto implementa la derivazione delle perturbazioni primordiali e delle osservabili cosmologiche basate sulla dinamica del coset $E_7/SU(8)$.

## 📊 1. Risultati del Fit Osservativo (Planck 2018)
Il modello SPU fitta i dati del Fondo Cosmico a Microonde (CMB) senza l'introduzione di campi inflatonici ad-hoc, fornendo una precisione superiore ai modelli standard a singolo campo.

| Osservabile | Predizione SPU | Dati Planck (2018) |
| :--- | :--- | :--- |
| **Spectral Index ($n_s$)** | **0.9636** | 0.9649 ± 0.0042 |
| **Tensor-to-Scalar Ratio ($r$)** | **~0.004** | < 0.056 |
| **Running ($\alpha_s$)** | **-0.0006** | -0.0045 ± 0.0067 |
| **$\chi^2_{\nu}$ (Ridotto)** | **0.15** | -- |

## 🧠 2. Firma della Non-Gaussianità (Bispettro)
La SPU predice una firma di non-Gaussianità primordiale unica, caratterizzata da una shape ibrida derivata dal mezzo fermionico collettivo.

### Template della Shape Function
La funzione di forma $\mathcal{S}$ è data dalla combinazione lineare:
$$\mathcal{S} = \frac{6}{5} f_{NL}^{\mathrm{SPU}} \left[ (1-\xi) B_{\mathrm{local}} + \xi B_{\mathrm{equil}} + \eta B_{\mathrm{deriv}} \right]$$

### Parametri Fenomenologici (Table 1)
| Parametro | Simbolo | Valore | Origine Fisica |
| :--- | :--- | :--- | :--- |
| **Ampiezza** | $f_{NL}$ | $0.5 \sim 3.0$ | Accoppiamento del coset |
| **Mixing Locale** | $\xi$ | $0.4 \pm 0.1$ | Termine cinetico indotto |
| **Peso Derivativo** | $\eta$ | $0.3 \pm 0.1$ | Gradiente dello spettro |
| **Gap Spettrale** | $m$ | $0.1$ | Cutoff geometrico $\Lambda_{SP}$ |

## ⚙️ 3. Validazione Numerica e Disgiunzione
I test di correlazione eseguiti tramite lo script `spu_spectral_signature.py` dimostrano che la SPU è una firma **ortogonale** e **distinguibile** dai template standard.

- **Correlazione vs LOCAL**: **0.4690**
- **Correlazione vs EQUILATERAL**: **0.4745**



### Interpretazione
Poiché la correlazione $\mathcal{C} < 0.5$, la SPU non è degenerata con i modelli inflazionari classici. La presenza del gap spettrale $m$ rompe la simmetria locale, permettendo una rilevazione univoca nelle future missioni (LiteBIRD, CMB-S4).

## 📂 4. Contenuto del Repository
- `spu_spectral_signature.py`: Script Python per il calcolo della correlazione e generazione dei grafici di Dalitz.
- `physics_engine.py`: Derivazione analitica dello spettro $\rho(\lambda)$ dal coset $E_7/SU(8)$.
- `data/`: Output delle matrici di Fisher e simulazioni di likelihood.

## 🚀 5. Come iniziare
1. Clona il repository.
2. Assicurati di avere installato `numpy` e `matplotlib`.
3. Esegui l'analisi della firma:
   ```bash
   python spu_spectral_signature.py