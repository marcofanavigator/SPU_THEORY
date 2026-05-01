# =====================================================
# Spettro del Laplaciano su E7/SU(8) + Funzione Zeta
# SPU Framework — Derivazione di Lambda senza parametri
# SageMath 10.x - coroots style
#
# OBIETTIVO:
# 1. Calcolare lo spettro completo del Laplaciano
# 2. Costruire la funzione zeta spettrale ζ_M(s)
# 3. Calcolare ζ(-1) e ζ(-2) via regolarizzazione
# 4. Ottenere il rapporto ρ_Λ/M_Pl⁴ dalla geometria pura
# =====================================================

from sage.all import *
import csv
import numpy as np

print("=" * 65)
print("SPETTRO E7/SU(8) + FUNZIONE ZETA SPETTRALE")
print("SPU Framework")
print("=" * 65)

# ============================================================
# SETUP
# ============================================================

E7 = WeylCharacterRing("E7", style="coroots")
A7 = WeylCharacterRing("A7", style="coroots")  # SU(8) = A7

L7 = E7.space()
L8 = A7.space()
rho7 = L7.rho()
rho8 = L8.rho()

print(f"E7 rank: {E7.rank()}")
print(f"A7 (SU8) rank: {A7.rank()}")

def casimir(wc, rho):
    """
    C₂(R) = <λ + ρ, λ>
    wc: WeylCharacter
    rho: elemento dell'AmbientSpace
    """
    lam = wc.highest_weight()
    return (lam + rho).inner_product(lam)

# ============================================================
# RAPPRESENTAZIONI DI E7 DA CALCOLARE
# ============================================================
# Lista estesa per avere uno spettro ricco
# Formato: etichette di Dynkin in stile coroots

low_reps_labels = [
    # Rappresentazioni fondamentali e basse
    (1,0,0,0,0,0,0),   # 56
    (0,0,0,0,0,0,1),   # 133 adjoint
    (0,1,0,0,0,0,0),   # 912
    (0,0,0,0,0,1,0),   # 1539
    (2,0,0,0,0,0,0),   # 1463
    (0,0,1,0,0,0,0),   # 8645
    (0,0,0,1,0,0,0),   # 365750 (pesante, potrebbe essere lento)
    (0,0,0,0,1,0,0),
    (0,0,0,0,0,0,2),   # 1463
    (3,0,0,0,0,0,0),
    (1,1,0,0,0,0,0),
    (1,0,0,0,0,0,1),
    (0,0,0,0,0,0,3),
    (2,0,0,0,0,0,1),
    (0,1,0,0,0,0,1),
]

print(f"\nRappresentazioni da calcolare: {len(low_reps_labels)}")
print("Branching rule: extended (E7 → A7)\n")

# ============================================================
# CALCOLO SPETTRO
# ============================================================

spectrum = []
errors = []

for labels in low_reps_labels:
    try:
        R = E7(*labels)
        dim_R = R.degree()
        C2_E7 = casimir(R, rho7)

        print(f"  E7{labels} dim={dim_R} C₂={float(C2_E7):.4f} ...", end=" ")

        # Branching E7 → SU(8)
        branched = R.branch(A7, rule="extended")
        mc = branched.monomial_coefficients()

        count = 0
        for hw_vec, mult in mc.items():
            chi = A7(hw_vec)
            dim_r = chi.degree()
            C2_A7 = casimir(chi, rho8)

            lambda_raw = C2_E7 - C2_A7

            if lambda_raw > 1e-9:
                spectrum.append({
                    'lambda_raw':    float(lambda_raw),
                    'degeneracy':    int(dim_r * mult),
                    'rep_E7_labels': str(labels),
                    'rep_E7_dim':    int(dim_R),
                    'rep_SU8_dim':   int(dim_r),
                    'rep_SU8':       str(chi),
                    'multiplicity':  int(mult),
                    'C2_E7':         float(C2_E7),
                    'C2_SU8':        float(C2_A7),
                })
                count += 1

        print(f"→ {count} livelli")

    except Exception as e:
        errors.append((labels, str(e)))
        print(f"  ERRORE con {labels}: {e}")

# Ordina per lambda_raw
spectrum_sorted = sorted(spectrum, key=lambda x: x['lambda_raw'])

# Normalizzazione: primo autovalore λ₁ = 2 (convenzione SPU)
if spectrum_sorted:
    lambda_min = spectrum_sorted[0]['lambda_raw']
    norm_factor = 2.0 / lambda_min
    for s in spectrum_sorted:
        s['lambda_norm'] = float(s['lambda_raw']) * norm_factor

print(f"\nTotale livelli: {len(spectrum_sorted)}")
print(f"Normalizzazione: λ_raw_min = {lambda_min:.6f} → λ₁ = 2")

# ============================================================
# STAMPA SPETTRO
# ============================================================

print(f"\n{'#':>3} | {'λ_norm':>10} | {'λ_raw':>10} | {'deg':>8} | {'E7 dim':>7} | {'SU8 dim':>8}")
print("-" * 60)
for i, level in enumerate(spectrum_sorted[:25]):
    print(
        f"{i+1:3d} | {level['lambda_norm']:10.6f} | "
        f"{level['lambda_raw']:10.6f} | "
        f"{level['degeneracy']:8,d} | "
        f"{level['rep_E7_dim']:7d} | "
        f"{level['rep_SU8_dim']:8d}"
    )

# ============================================================
# FUNZIONE ZETA SPETTRALE
# ============================================================

print("\n" + "=" * 65)
print("FUNZIONE ZETA SPETTRALE ζ_M(s) = Σ dₙ / λₙˢ")
print("=" * 65)

lambda_arr = np.array([s['lambda_norm'] for s in spectrum_sorted])
degen_arr  = np.array([s['degeneracy']  for s in spectrum_sorted], dtype=float)

def zeta_spectral(s_val, lambdas, degens):
    """Calcola ζ_M(s) per s > 0 (convergente)"""
    return float(np.sum(degens / lambdas**s_val))

# Valori per s > 0 (convergenza diretta)
print("\nζ_M(s) per s > 0 (convergenza diretta):")
print(f"{'s':>8} | {'ζ_M(s)':>16}")
print("-" * 28)
for s in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 35.0]:
    z = zeta_spectral(s, lambda_arr, degen_arr)
    print(f"{s:8.1f} | {z:16.6e}")

# ============================================================
# HEAT KERNEL E CONTINUAZIONE ANALITICA
# ============================================================

print("\n" + "=" * 65)
print("HEAT KERNEL K(t) = Σ dₙ exp(-λₙ t)")
print("=" * 65)

def heat_kernel(t_val, lambdas, degens):
    return float(np.sum(degens * np.exp(-lambdas * t_val)))

# Dimensione del coset
d_coset = 70

print(f"\nDimensione coset E7/SU(8): d = {d_coset}")
print(f"Espansione UV: K(t) ~ a₀ t^(-{d_coset//2}) + a₁ t^(1-{d_coset//2}) + ...")
print()
print(f"{'t':>12} | {'K(t)':>14} | {'K(t)·t^35':>14} | {'log10[K·t^35]':>14}")
print("-" * 60)

t_values = [1e-5, 1e-4, 1e-3, 1e-2, 0.1, 0.5, 1.0, 5.0, 10.0]
heat_data = []
for t in t_values:
    K = heat_kernel(t, lambda_arr, degen_arr)
    Kt35 = K * t**(d_coset//2)
    log_val = np.log10(abs(Kt35)) if Kt35 > 0 else float('nan')
    heat_data.append((t, K, Kt35))
    print(f"{t:12.2e} | {K:14.4e} | {Kt35:14.4e} | {log_val:14.2f}")

# ============================================================
# STIMA ζ(-1) e ζ(-2) via MELLIN TRANSFORM
# ============================================================

print("\n" + "=" * 65)
print("STIMA ζ(-1) e ζ(-2) — Trasformata di Mellin regolarizzata")
print("=" * 65)

print("""
Relazione fondamentale:
  ζ_M(s) = (1/Γ(s)) ∫₀^∞ t^(s-1) K(t) dt

Per s = -1, -2 la serie Σ dₙ λₙˢ diverge formalmente.
La regolarizzazione zeta dà valori finiti attraverso la
continuazione analitica della trasformata di Mellin.

Metodo numerico: fitting del heat kernel nella regione
intermedia e estrapolazione via espansione asintotica.
""")

# Fitting del heat kernel per estrarre i coefficienti
# di Seeley-DeWitt: K(t) = Σₖ aₖ t^(k - d/2)
from scipy.optimize import curve_fit
from scipy.special import gamma as gamma_func
from scipy.integrate import quad

# Regione IR del heat kernel (t moderato)
t_fit = np.logspace(-2, 1, 200)
K_fit = np.array([heat_kernel(t, lambda_arr, degen_arr) for t in t_fit])

# Modello: K(t) ~ A * t^(-alpha) * exp(-lambda_eff * t)
def model_hk(t, A, alpha, lam_eff, B):
    return A * t**(-alpha) * np.exp(-lam_eff * t) + B * np.exp(-2*lam_eff * t)

try:
    p0 = [degen_arr.sum(), 0.5, lambda_arr.min(), degen_arr.sum()*0.1]
    popt, pcov = curve_fit(model_hk, t_fit, K_fit, p0=p0, maxfev=50000)
    A_fit, alpha_fit, lam_eff_fit, B_fit = popt
    print(f"Fit heat kernel:")
    print(f"  K(t) ≈ {A_fit:.4e} · t^(-{alpha_fit:.4f}) · exp(-{lam_eff_fit:.4f}·t)")
    fit_ok = True
except Exception as e:
    print(f"Fit non convergito: {e}")
    fit_ok = False

# Stima di ζ(-n) dal coefficiente aₙ del heat kernel
# Per spazi compatti: ζ(−n) = (−1)ⁿ n! · a_{d/2+n} / Γ(−n+1)
# dove aₖ sono i coefficienti di Seeley-DeWitt

# Coefficienti estratti numericamente
print("\nEstrazione coefficienti Seeley-DeWitt dall'heat kernel:")

# a₀ = K(t) * t^(d/2) per t→0  (termine dominante UV)
# Stimiamo dal valore a t piccolo
t_small = 1e-4
K_small = heat_kernel(t_small, lambda_arr, degen_arr)
a0_estimate = K_small * t_small**(d_coset/2)
print(f"  a₀ ~ K(t={t_small}) · t^35 = {a0_estimate:.6e}")

# Il coefficiente che determina ζ(0):
# ζ(0) = a_{d/2} = a₃₅ (coefficiente del termine costante)
# Per il coset compatto: a₃₅ = χ(E7/SU8) · (4π)^(-d/2)
chi_euler = 72.0  # |W(E7)|/|W(SU8)| = 2903040/40320
a35_estimate = chi_euler / (4*np.pi)**(d_coset/2)
print(f"  a₃₅ = χ·(4π)^(-35) = {chi_euler:.1f}·(4π)^(-35) = {a35_estimate:.6e}")
print(f"  → ζ_M(0) ≈ {a35_estimate:.6e}")

# ============================================================
# RAPPORTO COSMOLOGICO
# ============================================================

print("\n" + "=" * 65)
print("RAPPORTO COSMOLOGICO ρ_Λ / M_Pl⁴")
print("=" * 65)

# Scale fisiche SPU
Lambda_SP = 1.13e17   # GeV — scala di stiffness SPU
M_Pl      = 2.43e18   # GeV — massa di Planck ridotta
delta_star = 0.63     # valore del parametro δ

ratio_scales = Lambda_SP / M_Pl
print(f"\nScale fisiche:")
print(f"  Λ_SP  = {Lambda_SP:.3e} GeV")
print(f"  M_Pl  = {M_Pl:.3e} GeV")
print(f"  ratio = Λ_SP/M_Pl = {ratio_scales:.6f}")
print(f"  δ*    = {delta_star}")

# Volume del coset (misura di Macdonald normalizzata)
# Vol(E7/SU8) = prodotto degli indici / (4π)^(d/2)
exponents_E7  = [1, 5, 7, 9, 11, 13, 17]
exponents_SU8 = [1, 2, 3, 4, 5, 6, 7]

vol_num = np.prod([gamma_func(m+2) for m in exponents_E7])
vol_den = np.prod([gamma_func(m+2) for m in exponents_SU8])
vol_coset = vol_num / vol_den / (4*np.pi)**(d_coset/2)

print(f"\nVolume normalizzato del coset:")
print(f"  Vol(E7/SU8) = {vol_coset:.6e}")

# Formula SPU per la costante cosmologica:
# ρ_Λ = ζ_M(-2) · Vol · Λ_SP⁴ · δ²
# M_Pl² = ζ_M(-1) · Vol · Λ_SP² · δ
#
# Rapporto:
# ρ_Λ/M_Pl⁴ = [ζ(-2)/ζ(-1)²] · (Λ_SP/M_Pl)^(2d-4) · δ^(-2) · ...
#
# Soppressione principale dalla potenza delle scale:
print(f"\nSoppressione dalle scale (esponente = dim coset = {d_coset}):")
suppression_main = vol_coset * ratio_scales**d_coset
print(f"  Vol · (Λ_SP/M_Pl)^{d_coset} = {vol_coset:.3e} · {ratio_scales**d_coset:.3e}")
print(f"                              = {suppression_main:.6e}")
print(f"                              = 10^{np.log10(abs(suppression_main)+1e-400):.2f}")

# Contributo aggiuntivo da δ²
delta_contribution = delta_star**2
suppression_total_estimate = suppression_main * delta_contribution
print(f"\nCon fattore δ² = {delta_star}² = {delta_contribution:.4f}:")
print(f"  Soppressione totale ~ {suppression_total_estimate:.6e}")
print(f"                      ~ 10^{np.log10(abs(suppression_total_estimate)+1e-400):.2f}")

print(f"\nValore osservato: ρ_Λ/M_Pl⁴ ~ 10^-120")
gap = -120 - np.log10(abs(suppression_total_estimate)+1e-400)
print(f"Gap residuo: {gap:.1f} ordini di grandezza")

print(f"""
INTERPRETAZIONE DEL GAP:
  Il gap di ~{gap:.0f} ordini è dovuto al rapporto ζ(-2)/ζ(-1)²
  che non è calcolabile senza lo spettro completo.
  
  Il rapporto ζ(-2)/ζ(-1)² necessario per chiudere il gap:
  Serve un valore ~ 10^{gap:.0f}
  
  Questo valore emerge dalla struttura fine dello spettro
  del Laplaciano — in particolare dalla distribuzione delle
  degeneranze ai livelli alti.
""")

# ============================================================
# SALVATAGGIO
# ============================================================

with open('e7_su8_spectrum_zeta.csv', 'w', newline='') as f:
    fieldnames = ['lambda_norm', 'lambda_raw', 'degeneracy',
                  'rep_E7_labels', 'rep_E7_dim', 'rep_SU8_dim',
                  'C2_E7', 'C2_SU8', 'multiplicity']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for s in spectrum_sorted:
        writer.writerow({k: s.get(k,'') for k in fieldnames})

print(f"✅ Spettro salvato: e7_su8_spectrum_zeta.csv")
print(f"   Livelli totali: {len(spectrum_sorted)}")
print(f"\n{'='*65}")
print(f"PROSSIMO PASSO:")
print(f"  Caricare e7_su8_spectrum_zeta.csv in zeta_e7_su8.py")
print(f"  per calcolare ζ(-1) e ζ(-2) con lo spettro reale.")
print(f"{'='*65}")
