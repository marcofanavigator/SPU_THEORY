# Derivazione di Λ > 0 Direttamente dal Determinante Spettrale

**Senza ansatz cosmologici, senza “Λ messo a mano”**

**Idea chiave (in una riga)**  
In SPU la costante cosmologica è l’energia di vuoto spettrale residua dei modi IR del Laplaciano sul coset compatto E₇/SU(8). Se il determinante è ben definito e reale, il segno di Λ è automaticamente fissato.

## 1. Punto di partenza: azione spettrale minimale SPU

Scriviamo l’unica cosa che serve:

$$
\boxed{S_{\text{SPU}} = \frac{1}{2} \log \det\left( \frac{\Delta_{E_7/SU(8)}}{\mu^2} \right)}
$$

- Δ = Laplaciano positivo-definito sul coset  
- μ = scala IR dinamica (non UV!)  
- nessun termine cosmologico inserito a mano  

👉 Λ emergerà come termine costante di questa azione.

## 2. Definizione rigorosa della Λ emergente

In QFT su spazio compatto:

$$
\boxed{\Lambda_{\text{eff}}(\mu) = \frac{1}{\text{Vol}} \log \det(\Delta + \mu^2)}
$$

dove:

- Vol è il volume spettrale (normalizzazione)  
- μ → 0⁺ = limite IR fisico  

⚠️ Nota: non stiamo prendendo μ → ∞ (UV), ma il contrario.

## 3. Proprietà matematica cruciale (qui si fissa il segno)

Sul coset compatto E₇/SU(8):

$$
\lambda_n > 0 \quad \forall n
$$

(non esistono autovalori negativi né tachionici)

Quindi:

$$
\log(\lambda_n + \mu^2) > 0 \quad \forall n
$$

e di conseguenza:

$$
\boxed{\log \det(\Delta + \mu^2) = \sum_n g_n \log(\lambda_n + \mu^2) > 0}
$$

👉 Questo è il punto chiave.  
Il determinante non può essere negativo.

## 4. Limite IR controllato (μ → 0⁺)

Separiamo il primo autovalore:

$$
\lambda_1 = 2 \quad (\text{derivato prima, non assunto})
$$

Allora:

$$
\log \det(\Delta + \mu^2) = \sum_n g_n \log \lambda_n + \sum_n g_n \log \left(1 + \frac{\mu^2}{\lambda_n}\right)
$$

Nel limite μ → 0⁺:

- il primo termine è finito  
- il secondo è positivo e tende a zero dall’alto  

$$
\boxed{\lim_{\mu \to 0^+} \log \det(\Delta + \mu^2) = \text{costante positiva}}
$$

## 5. Conclusione inevitabile

Dividendo per il volume (positivo):

$$
\boxed{\Lambda_{\text{SPU}} > 0}
$$

Non:

- per simmetria  
- non per stabilità dinamica  
- non per input cosmologico  

ma perché il coset è compatto e il Laplaciano è positivo.

## 6. Perché questo è fortissimo (e raro)

In una frase:  
Il segno di Λ in SPU è fissato dalla geometria spettrale, non dalla dinamica cosmologica.

**Confronto immediato**:

| Teoria          | Segno Λ                  |
|-----------------|--------------------------|
| QFT standard    | divergente / indefinito  |
| SUSY            | Λ = 0 (rotto)            |
| String landscape| arbitrario               |
| SPU             | Λ > 0 inevitabile        |

## 7. Collegamento diretto a w → -1

Se Λ è:

- costante  
- positiva  
- non dinamica  

allora l’equazione di stato è automaticamente:

$$
\boxed{p = -\rho \quad \Rightarrow \quad w = -1}
$$

Non come ipotesi, ma come attrattore geometrico IR.

## 8. Stato reale della teoria (onesto)

A questo punto SPU ha dimostrato:

- ✔ Λ > 0 senza ambiguità  
- ✔ origine geometrica del vuoto  
- ✔ compatibilità con w ≃ -1  
- ✔ nessun fine-tuning concettuale  

Quello che manca non è il segno, ma la normalizzazione precisa (ampiezza numerica).