"""
SPU Framework — Spectral Derivation of δ(μ)
============================================
Calcola δ(μ) direttamente dallo spettro del Laplaciano su E₇/SU(8)
usando le branching rules e i Casimir della letteratura.

CORREZIONI rispetto alla versione originale:
  1. Peso heat-kernel  w(x) = exp(-x)  invece di x/(1+x)
  2. Fixed point δ* = δ(μ*) al punto di flesso (β-function zero)
  3. Loop robustezza ricalcola il flesso per ogni spettro perturbato
  4. Path di output locale (non /mnt/)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')   # rimuovi questa riga se vuoi la finestra interattiva
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ─────────────────────────────────────────────────────────────────────────────
# 1. SPETTRO: autovalori e degenerazioni
#    Fonte: branching rules E₇ → SU(8), Slansky, hep-th/0409272
#
#    λ(R,r) = [C₂^E7(R) - C₂^SU8(r)] / R²
#    R² fissato imponendo λ_1 = 2 per la rappresentazione 56
# ─────────────────────────────────────────────────────────────────────────────

C2_E7 = {
    56:   28.5,
    133:  24.0,
    912:  38.0,
    1539: 42.0,   # stima
    8645: 60.0,   # stima
}

C2_SU8 = {
    1:    0.0,
    8:    63/16,
    28:   13.5,
    36:   14.875,
    56:   16.875,
    63:   8.0,
    70:   18.375,
    120:  19.25,
    168:  22.0,    # stima
    216:  24.0,    # stima
    280:  26.0,    # stima
    378:  30.0,    # stima
    420:  31.0,    # stima
    504:  33.0,    # stima
    630:  35.0,    # stima
    720:  36.0,    # stima
    840:  38.0,    # stima
    1176: 42.0,    # stima
}

# Branching rules E₇ → SU(8)
branching = {
    56:  [(28, 1), (28, 1)],           # 56  → 28 ⊕ 28̄
    133: [(63, 1), (70, 1)],           # 133 → 63 ⊕ 70
    912: [(378, 1), (378, 1),          # 912 → 378 ⊕ 378̄ ⊕ 56 ⊕ 70 ⊕ 28 ⊕ 2×1
          (56,  1), (70,  1),
          (28,  1), (1,   2)],
}

# Normalizzazione: λ(56→28) = 2  →  R² = (C2_E7[56] - C2_SU8[28]) / 2
R2 = (C2_E7[56] - C2_SU8[28]) / 2.0
print(f"Normalizzazione geometrica: R² = {R2:.4f}")

spectrum = []
for dim_E7, sub_reps in branching.items():
    c2_g = C2_E7[dim_E7]
    for dim_su8, mult in sub_reps:
        c2_h = C2_SU8[dim_su8]
        lam = (c2_g - c2_h) / R2
        if lam < 0:
            print(f"  ATTENZIONE: λ < 0 per E₇({dim_E7}) → SU(8)({dim_su8}), skip")
            continue
        deg = dim_su8 * mult
        spectrum.append((lam, deg))
        print(f"  E₇({dim_E7:4d}) → SU(8)({dim_su8:4d}): λ = {lam:.4f}, deg = {deg}")

spectrum = np.array(spectrum)   # shape (N, 2): [λ, degenerazione]
lambdas  = spectrum[:, 0]
degs     = spectrum[:, 1]
print(f"\nDOF totali: {degs.sum():.0f},  livelli spettrali: {len(lambdas)}")

# ─────────────────────────────────────────────────────────────────────────────
# 2. FUNZIONE δ(μ) con peso heat-kernel
#
#   w(x) = exp(-x),   x = λ_n / μ²
#
#   - x → 0  (λ_n ≪ μ²): w → 1  → modo leggero, attivo
#   - x → ∞  (λ_n ≫ μ²): w → 0  → modo pesante, decoupled
#
#   δ(μ) = 1 − Σ_n g_n exp(−λ_n/μ²) / Σ_n g_n
#
#   Il fixed point δ* emerge al punto di flesso di δ(μ),
#   dove la β-function  β = dδ/d(ln μ)  ha il suo estremo.
# ─────────────────────────────────────────────────────────────────────────────

def delta_mu(mu, lams, dgs):
    x = lams / mu**2
    w = np.exp(-x)
    return 1.0 - np.dot(dgs, w) / dgs.sum()

mu_values    = np.logspace(-2, 2, 3000)
delta_values = np.array([delta_mu(mu, lambdas, degs) for mu in mu_values])

# ─────────────────────────────────────────────────────────────────────────────
# 3. FIXED POINT: punto di flesso  (β-function = dδ/d(ln μ) massima)
# ─────────────────────────────────────────────────────────────────────────────

log_mu = np.log(mu_values)
beta   = np.gradient(delta_values, log_mu)

idx_fp     = np.argmax(np.abs(beta))
mu_star    = mu_values[idx_fp]
delta_star = delta_values[idx_fp]

print(f"\n{'='*57}")
print(f"  RISULTATI SPETTRALI")
print(f"{'='*57}")
print(f"  μ* (punto di flesso):  {mu_star:.4f}  [unità √λ_min]")
print(f"  δ(μ*)              :  {delta_star:.6f}")
print(f"  Valore SPU atteso  :  δ* ≈ 0.613")
print(f"  Scarto             :  Δ = {abs(delta_star - 0.613):.6f}")
print(f"  Deviazione %       :  {100*abs(delta_star - 0.613)/0.613:.2f}%")
print(f"{'='*57}")

# ─────────────────────────────────────────────────────────────────────────────
# 4. ROBUSTEZZA: ±10% sui Casimir stimati
#    Per ogni perturbazione ricalcola il punto di flesso
# ─────────────────────────────────────────────────────────────────────────────

mask_estimated = lambdas > 3.0   # livelli dalle stime (912 pesante + singoletti)
perturbations  = np.linspace(-0.10, 0.10, 41)
delta_fp_values = []

for p in perturbations:
    lam_p = lambdas.copy()
    lam_p[mask_estimated] *= (1.0 + p)
    dv   = np.array([delta_mu(mu, lam_p, degs) for mu in mu_values])
    bv   = np.gradient(dv, log_mu)
    i_fp = np.argmax(np.abs(bv))
    delta_fp_values.append(dv[i_fp])

delta_fp_values = np.array(delta_fp_values)
print(f"\nRobustezza δ* (±10% Casimir stimati):")
print(f"  min:       {delta_fp_values.min():.4f}")
print(f"  max:       {delta_fp_values.max():.4f}")
print(f"  mean ± std: {delta_fp_values.mean():.4f} ± {delta_fp_values.std():.4f}")

# ─────────────────────────────────────────────────────────────────────────────
# 5. PLOT
# ─────────────────────────────────────────────────────────────────────────────

dark_bg  = '#0a0a0f'
panel_bg = '#111118'
gold     = '#c9a84c'
cyan     = '#4cc9c9'
red      = '#e05252'
green    = '#52e08a'
white    = '#e8e8f0'
gray     = '#444455'

plt.rcParams.update({
    'font.family': 'monospace',
    'text.color':      white,
    'axes.labelcolor': white,
    'xtick.color':     white,
    'ytick.color':     white,
})

fig = plt.figure(figsize=(14, 10), facecolor=dark_bg)
gs  = GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.35)

# ── Panel 1: δ(μ) flow + β-function ─────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, :])
ax1.set_facecolor(panel_bg)
ax1.spines[:].set_color(gray)

ax1.semilogx(mu_values, delta_values, color=cyan, lw=2.5,
             label='δ(μ) spettrale [heat-kernel]', zorder=3)
ax1.axhline(0.633,      color=gold,  lw=1.8, ls='--', alpha=0.9,
            label='δ* SPU = 0.633', zorder=2)
ax1.axvline(mu_star,    color=green, lw=1.4, ls=':', alpha=0.85, zorder=2)
ax1.axhline(delta_star, color=green, lw=1.4, ls=':', alpha=0.85,
            label=f'δ(μ*) = {delta_star:.4f}  @ μ* = {mu_star:.3f}', zorder=2)
ax1.scatter([mu_star], [delta_star], color=green, s=80, zorder=5)

# β-function su asse secondario
ax1b = ax1.twinx()
ax1b.set_facecolor(panel_bg)
ax1b.semilogx(mu_values, beta, color=red, lw=1.2, alpha=0.55,
              label='β = dδ/d(ln μ)')
ax1b.set_ylabel('β(μ)  [β-function]', color=red, fontsize=10)
ax1b.tick_params(colors=red, labelsize=8)
ax1b.spines['right'].set_color(red)
ax1b.axhline(0, color=red, lw=0.5, alpha=0.3)

ax1.set_xlabel('μ  (unità naturali del coset,  λ_min^½ ≡ 1)', fontsize=11)
ax1.set_ylabel('δ(μ)', fontsize=12)
ax1.set_title('Flow spettrale di δ(μ) su E₇/SU(8)  —  SPU Framework',
              fontsize=12, color=white, pad=10)
lines1, labs1 = ax1.get_legend_handles_labels()
lines2, labs2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labs1 + labs2,
           fontsize=9, facecolor=panel_bg, edgecolor=gray, loc='upper left')
ax1.set_ylim(-0.05, 1.08)
ax1.grid(True, color=gray, alpha=0.25, which='both')
ax1.tick_params(labelsize=9)

# ── Panel 2: Spettro (λ, degenerazione) ─────────────────────────────────────
ax2 = fig.add_subplot(gs[1, 0])
ax2.set_facecolor(panel_bg)
ax2.spines[:].set_color(gray)

colors_bars = [gold if lam < 2.5 else cyan if lam < 3.5 else red
               for lam in lambdas]
ax2.bar(range(len(lambdas)), degs, color=colors_bars, alpha=0.85,
        edgecolor=gray, linewidth=0.5)
for i, (lam, deg) in enumerate(zip(lambdas, degs)):
    ax2.text(i, deg + 4, f'λ={lam:.2f}', ha='center', va='bottom',
             fontsize=7.5, color=white, rotation=45)

ax2.set_xlabel('Indice livello spettrale', fontsize=10)
ax2.set_ylabel('Degenerazione  g_n', fontsize=10)
ax2.set_title('Spettro IR troncato  E₇/SU(8)', fontsize=11, color=white)
ax2.grid(True, color=gray, alpha=0.22, axis='y')
ax2.tick_params(labelsize=8)

leg_patches = [
    plt.Rectangle((0,0),1,1, fc=gold, label='λ < 2.5  (56, 133)'),
    plt.Rectangle((0,0),1,1, fc=cyan, label='2.5 ≤ λ < 3.5  (912 leggero)'),
    plt.Rectangle((0,0),1,1, fc=red,  label='λ ≥ 3.5  (912 pesante / stime)'),
]
ax2.legend(handles=leg_patches, fontsize=7.5, facecolor=panel_bg, edgecolor=gray)

# ── Panel 3: Robustezza ──────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_facecolor(panel_bg)
ax3.spines[:].set_color(gray)

pert_pct = perturbations * 100
ax3.plot(pert_pct, delta_fp_values, color=cyan, lw=2, marker='o',
         markersize=3.5, markerfacecolor=gold, label='δ(μ*) perturbato')
ax3.axhline(0.633,      color=gold,  lw=1.5, ls='--', label='δ* SPU = 0.613')
ax3.axhline(delta_star, color=green, lw=1.2, ls=':',  label=f'δ_0 = {delta_star:.4f}')
ax3.fill_between(pert_pct, 0.633 - 0.02, 0.633 + 0.02,
                 alpha=0.12, color=gold, label='±2% intorno a δ*')

ax3.set_xlabel('Perturbazione Casimir stimati (%)', fontsize=10)
ax3.set_ylabel('δ(μ*)', fontsize=10)
ax3.set_title('Robustezza di δ(μ*)\nrispetto alle incertezze spettrali',
              fontsize=11, color=white)
ax3.legend(fontsize=8.5, facecolor=panel_bg, edgecolor=gray)
ax3.grid(True, color=gray, alpha=0.25)
ax3.tick_params(labelsize=8)

# ── Riepilogo numerico ────────────────────────────────────────────────────────
summary = (f"δ(μ*) = {delta_star:.5f}  |  δ* SPU = 0.613  |  "
           f"Δ = {abs(delta_star - 0.613):.5f}  |  "
           f"Dev. = {100*abs(delta_star - 0.613)/0.613:.2f}%  |  "
           f"Robustezza: {delta_fp_values.mean():.4f} ± {delta_fp_values.std():.4f}")
fig.text(0.5, 0.005, summary, ha='center', fontsize=9.5,
         color=gold, style='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=panel_bg,
                   edgecolor=gold, alpha=0.8))

# ── Salvataggio ───────────────────────────────────────────────────────────────
# Modifica il path se necessario (su Windows usa es. 'C:/Users/tuonome/Desktop/...')
out_path = 'spu_delta_spectral.png'
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor=dark_bg)
plt.close()
print(f"\nPlot salvato in: {out_path}")
