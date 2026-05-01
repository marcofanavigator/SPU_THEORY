# =====================================================
# DEEP SPECTRUM ANALYSIS: E7/SU(8) — h=4
# SPU Framework — Convergenza della Costante Cosmologica
#
# Obiettivo: calcolare 2000+ livelli spettrali per
# verificare la convergenza del gap verso zero.
#
# Progressione documentata:
#   h=2 (25 liv):  gap = -21.9 ordini (senza ζ ratio)
#   h=3 (445 liv): gap = -15.1 ordini (con ζ ratio reale)
#   h=4 (target):  gap previsto ~ -8 ordini
#   h→∞ (N~5000):  gap → 0  (convergenza completa)
#
# Uso: sage spu_deep_spectrum_h4.sage
# Tempo stimato: 30-120 minuti (dipende dal PC)
# RAM stimata: 4-16 GB con il filtro dim < 1_000_000
# =====================================================

from sage.all import *
from itertools import permutations
import numpy as np
import csv
import time

print("=" * 65)
print("DEEP SPECTRUM ANALYSIS: E7/SU(8) — h=4")
print("SPU Framework — Convergenza Costante Cosmologica")
print("=" * 65)

# ============================================================
# SETUP
# ============================================================

E7 = WeylCharacterRing("E7", style="coroots")
A7 = WeylCharacterRing("A7", style="coroots")

L7 = E7.space()
L8 = A7.space()
rho7 = L7.rho()
rho8 = L8.rho()

def casimir(wc, rho):
    """C₂(R) = <λ+ρ, λ> — Casimir quadratico"""
    lam = wc.highest_weight()
    return (lam + rho).inner_product(lam)

# ============================================================
# PARAMETRI
# ============================================================

max_h       = 4          # altezza massima dei pesi di Dynkin
dim_limit   = 1_000_000  # limite dimensione rep (RAM safety)
save_every  = 50         # salva checkpoint ogni N rappresentazioni

print(f"\nParametri:")
print(f"  max_h     = {max_h}")
print(f"  dim_limit = {dim_limit:,}")
print(f"  Branching rule: extended (E7 → A7/SU8)")

# ============================================================
# ESPLORAZIONE PESI DI DYNKIN
# ============================================================

spectrum   = []
processed  = set()
n_reps     = 0
n_skipped  = 0
n_errors   = 0
t_start    = time.time()

print(f"\nEsplorazione pesi fino a altezza {max_h}...")
print(f"{'Rep':>6} | {'Labels':>30} | {'dim E7':>10} | {'Livelli':>8} | {'Tempo':>8}")
print("-" * 70)

for h in range(1, max_h + 1):
    print(f"\n--- Altezza h={h} ---")

    # Genera tutte le partizioni di (h+7) in 7 parti ≥ 1
    # poi sottrae 1 da ciascuna → etichette di Dynkin in [0, h]
    for p in Partitions(h + 7, length=7, min_part=1):
        labels = tuple([x - 1 for x in p])

        # Esplora tutte le permutazioni (rappresentazioni distinte)
        for lab in set(permutations(labels)):
            if lab in processed:
                continue
            processed.add(lab)

            try:
                # Costruisci la rappresentazione E7
                R = E7(*lab)
                dim_R = R.degree()

                # Filtro RAM: salta rep troppo grandi
                if dim_R > dim_limit:
                    n_skipped += 1
                    continue

                C2_E7 = casimir(R, rho7)
                t_rep = time.time()

                # Branching E7 → SU(8)
                branched = R.branch(A7, rule="extended")
                mc = branched.monomial_coefficients()

                count = 0
                for hw_vec, mult in mc.items():
                    chi    = A7(hw_vec)
                    C2_SU8 = casimir(chi, rho8)
                    lam    = C2_E7 - C2_SU8

                    if lam > 1e-7:
                        spectrum.append({
                            'lambda_raw': float(lam),
                            'deg':        int(chi.degree() * mult),
                            'labels':     str(lab),
                            'dim_E7':     int(dim_R),
                            'dim_SU8':    int(chi.degree()),
                            'mult':       int(mult),
                            'C2_E7':      float(C2_E7),
                            'C2_SU8':     float(C2_SU8),
                        })
                        count += 1

                n_reps += 1
                elapsed = time.time() - t_rep

                # Log ogni rappresentazione
                print(f"{n_reps:6d} | {str(lab):>30} | {dim_R:10,d} | {count:8d} | {elapsed:7.1f}s")

                # Checkpoint intermedio ogni save_every rep
                if n_reps % save_every == 0:
                    _sorted = sorted(spectrum, key=lambda x: x['lambda_raw'])
                    with open(f'spu_checkpoint_h{max_h}_{n_reps}.csv', 'w', newline='') as f:
                        w = csv.DictWriter(f, fieldnames=list(_sorted[0].keys()))
                        w.writeheader()
                        w.writerows(_sorted)
                    print(f"  >>> Checkpoint salvato: {len(spectrum)} livelli <<<")

            except Exception as e:
                n_errors += 1
                # Silenzioso per non intasare l'output
                continue

# ============================================================
# ELABORAZIONE FINALE
# ============================================================

print(f"\n{'='*65}")
print(f"ELABORAZIONE COMPLETATA")
print(f"  Rappresentazioni elaborate: {n_reps}")
print(f"  Rappresentazioni saltate (dim > {dim_limit:,}): {n_skipped}")
print(f"  Errori: {n_errors}")
print(f"  Livelli spettrali trovati: {len(spectrum)}")
print(f"  Tempo totale: {(time.time()-t_start)/60:.1f} minuti")

if not spectrum:
    print("ERRORE: nessun livello trovato.")
    exit(1)

# Ordina e normalizza
spectrum.sort(key=lambda x: x['lambda_raw'])
lambda_min  = spectrum[0]['lambda_raw']
norm_factor = 2.0 / lambda_min  # λ₁ = 2 (convenzione SPU)

for s in spectrum:
    s['lambda_norm'] = s['lambda_raw'] * norm_factor

lambdas = np.array([s['lambda_norm'] for s in spectrum])
degens  = np.array([s['deg']         for s in spectrum], dtype=float)

print(f"\nSpettro normalizzato (λ₁ = 2):")
print(f"  λ_min_raw = {lambda_min:.6f} → λ₁ = 2")
print(f"  λ_max     = {lambdas.max():.4f}")
print(f"  Deg. totale = {degens.sum():.4e}")

# ============================================================
# PRIMI LIVELLI
# ============================================================

print(f"\n{'#':>4} | {'λ_norm':>10} | {'λ_raw':>10} | {'deg':>10} | {'E7 dim':>10} | {'SU8 dim':>8}")
print("-" * 60)
for i, s in enumerate(spectrum[:30]):
    print(f"{i+1:4d} | {s['lambda_norm']:10.6f} | {s['lambda_raw']:10.6f} | "
          f"{s['deg']:10,d} | {s['dim_E7']:10,d} | {s['dim_SU8']:8,d}")

# ============================================================
# FUNZIONE ZETA SPETTRALE
# ============================================================

print(f"\n{'='*65}")
print(f"FUNZIONE ZETA SPETTRALE ζ_M(s)")
print(f"{'='*65}")

print(f"\n{'s':>6} | {'ζ_M(s)':>16} | {'log10':>8}")
print("-" * 36)
zeta = {}
for s_val in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 35.0]:
    z = float(np.sum(degens / lambdas**s_val))
    zeta[s_val] = z
    print(f"{s_val:6.1f} | {z:16.6e} | {np.log10(abs(z)+1e-400):8.2f}")

# ============================================================
# HEAT KERNEL
# ============================================================

print(f"\n{'='*65}")
print(f"HEAT KERNEL K(t) = Σ dₙ exp(-λₙ t)")
print(f"{'='*65}")

print(f"\n{'t':>10} | {'K(t)':>14} | {'K(t)·t^35':>14} | {'log10':>8}")
print("-" * 52)
for t in [1e-4, 1e-3, 1e-2, 0.1, 0.5, 1.0, 5.0]:
    exps = -lambdas * t
    mask = exps > -700
    Kt   = float(np.sum(degens[mask] * np.exp(exps[mask])))
    Kt35 = Kt * t**35
    log_v = np.log10(abs(Kt35) + 1e-400)
    print(f"{t:10.2e} | {Kt:14.4e} | {Kt35:14.4e} | {log_v:8.2f}")

# ============================================================
# RAPPORTO COSMOLOGICO
# ============================================================

print(f"\n{'='*65}")
print(f"RAPPORTO COSMOLOGICO ρ_Λ / M_Pl⁴")
print(f"{'='*65}")

# Parametri fisici SPU
L_SP      = 1.13e17   # GeV — scala stiffness
M_Pl      = 2.43e18   # GeV — massa Planck ridotta
delta_star = 0.63     # parametro saturation deficit
d          = 70       # dim coset E7/SU(8)
Vol        = 3.7543e-5 # volume Macdonald normalizzato

r = L_SP / M_Pl

# Soppressione geometrica IR
geo_supp = Vol * (r**d) * (delta_star**2)

# Zeta ratio — la componente critica
z1 = float(np.sum(degens / lambdas**1))
z2 = float(np.sum(degens / lambdas**2))
zeta_ratio = z2 / (z1**2) if abs(z1) > 1e-300 else float('nan')

# Rapporto finale
final_ratio = geo_supp * zeta_ratio
log_final   = np.log10(abs(final_ratio) + 1e-400)
gap         = log_final - (-120)

print(f"\nParametri:")
print(f"  Λ_SP/M_Pl  = {r:.6f}")
print(f"  δ*         = {delta_star}")
print(f"  Vol        = {Vol:.4e}")
print(f"  d          = {d}")

print(f"\nComponenti del rapporto:")
print(f"  ζ_M(1)                = {z1:.6e} = 10^{np.log10(abs(z1)+1e-400):.2f}")
print(f"  ζ_M(2)                = {z2:.6e} = 10^{np.log10(abs(z2)+1e-400):.2f}")
print(f"  ζ ratio = ζ(2)/ζ(1)² = {zeta_ratio:.6e} = 10^{np.log10(abs(zeta_ratio)+1e-400):.2f}")
print(f"  Geo supp = Vol·r^70·δ²= {geo_supp:.6e} = 10^{np.log10(geo_supp+1e-400):.2f}")

print(f"\n{'='*65}")
print(f"RISULTATO FINALE")
print(f"{'='*65}")
print(f"  ρ_Λ/M_Pl⁴ (SPU, N={len(spectrum)}) = 10^{log_final:.2f}")
print(f"  ρ_Λ/M_Pl⁴ (osservato)               = 10^-120")
print(f"  GAP RESIDUO                          = {gap:.2f} ordini")

# Progressione storica
print(f"\nProgressione della convergenza:")
print(f"  {'N livelli':>10} | {'log10(ρ/M⁴)':>12} | {'Gap':>8}")
print(f"  {'-'*36}")
print(f"  {'25':>10} | {'~-98.10':>12} | {'-21.9':>8}  (spettro approx)")
print(f"  {'445':>10} | {'-104.94':>12} | {'-15.1':>8}  (h=3, SageMath)")
print(f"  {len(spectrum):>10} | {log_final:>12.2f} | {gap:>8.2f}  (h={max_h}, questo calcolo)")

# Formula IR (documento semi-analitico)
print(f"\nVerifica formula IR: ρ_Λ = δ* · H₀² · M_Pl²")
H0_GeV   = 1.5e-42  # GeV
rho_IR   = delta_star * H0_GeV**2 * M_Pl**2
print(f"  ρ_Λ (IR formula) = {rho_IR:.4e} GeV⁴")
print(f"  ρ_Λ (osservato)  = 6.0e-47 GeV⁴")
print(f"  Rapporto         = {rho_IR/6e-47:.4f}")

# ============================================================
# SALVATAGGIO CSV FINALE
# ============================================================

output_file = f'spu_spectrum_h{max_h}_final.csv'
with open(output_file, 'w', newline='') as f:
    fieldnames = ['lambda_norm', 'lambda_raw', 'deg', 'labels',
                  'dim_E7', 'dim_SU8', 'mult', 'C2_E7', 'C2_SU8']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for s in spectrum:
        writer.writerow({k: s[k] for k in fieldnames})

print(f"\n✅ Spettro salvato: {output_file}")
print(f"   ({len(spectrum)} livelli, {degens.sum():.2e} stati totali)")
print(f"\n{'='*65}")
print(f"PROSSIMI PASSI:")
print(f"  1. Se gap < 10: eseguire h=5 per conferma convergenza")
print(f"  2. Calcolare coefficiente C dalla formula IR")
print(f"  3. Aggiornare documento spu_cosmological_constant_revised.md")
print(f"{'='*65}")
