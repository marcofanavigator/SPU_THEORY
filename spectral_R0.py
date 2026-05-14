#!/usr/bin/env python3
"""
spectral_R0.py — Road 2: Spectral calculation of R₀ on E₇/SU(8)
SPU Theory — May 2026

Usage: python3 spectral_R0.py [--plot]
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Dati algebrici esatti ──────────────────────────────────────────
C2_56  = 57/2      # Casimir C₂(56 di E₇)
C2_27  = 26/3      # Casimir C₂(27 di E₆)
C2_912 = 39.5      # Casimir C₂(912 di E₇)  [approx]
C2_28  = 9.0       # Casimir C₂(28 di SU(8))
C2_36  = 35/4      # Casimir C₂(36 di SU(8))

# Autovalori del laplaciano sui due settori
lambda_quartic = C2_56  - C2_28   # = 19.5
lambda_cubic   = C2_912 - C2_36   # = 30.75

# Branching
frac_E6 = 54/56    # = 27/28

# Scala GUT
M_GUT = 1.8e16     # GeV

# ── Formula chiusa per R₀(μ) ──────────────────────────────────────
def R0_spectral(mu_over_M0):
    """
    Calcola R₀(μ) dalla formula spettrale chiusa su E₇/SU(8).
    
    R₀(μ) = (27/28) × [C₂(27)/(C₂(27)+x)] × [(C₂(56)+x)/C₂(56)]
    con x = (μ/M₀)²
    
    Bounds esatti:
      - UV (x→0): R₀ → 27/28 ≈ 0.9643
      - IR (x→∞): R₀ → (117/399) ≈ 0.2932
    """
    x = mu_over_M0**2
    w56 = C2_56 / (C2_56 + x)
    w27 = C2_27 / (C2_27 + x)
    return frac_E6 * w27 / w56

def mu_match_for_R0(R0_target):
    """
    Calcola μ/M₀ tale che R₀(μ) = R0_target.
    Richiede R0_target ∈ (0.2932, 0.9643).
    """
    from scipy.optimize import brentq
    R0_min = frac_E6 * C2_27/C2_56   # ≈ 0.2932
    R0_max = frac_E6                   # ≈ 0.9643
    if not (R0_min < R0_target < R0_max):
        raise ValueError(f"R0_target={R0_target:.4f} fuori dal range ({R0_min:.4f}, {R0_max:.4f})")
    root = brentq(lambda ratio: R0_spectral(ratio) - R0_target, 1e-6, 1000)
    return root

# ── Report ────────────────────────────────────────────────────────
def main():
    print("=" * 62)
    print("SPECTRAL CALCULATION OF R₀ ON E₇/SU(8) — Road 2")
    print("=" * 62)

    print(f"""
Laplacian eigenvalues:
  λ_quartic = C₂(56_E₇) − C₂(28_SU8) = {C2_56:.3f} − {C2_28:.3f} = {lambda_quartic:.3f}
  λ_cubic   = C₂(912_E₇) − C₂(36_SU8) = {C2_912:.3f} − {C2_36:.4f} = {lambda_cubic:.4f}
  λ₄/λ₃    = {lambda_quartic/lambda_cubic:.4f}  (quartic sector lighter ✓)

Exact bounds (group theory):
  UV (μ→0):  R₀ → 27/28        = {27/28:.6f}
  IR (μ→∞):  R₀ → 117/399      = {117/399:.6f}
  Physical window: ({C2_27/C2_56:.4f}, {27/28:.4f})
""")

    print(f"  {'μ/M₀':>8} {'R₀(μ)':>10}  {'Note'}")
    print("  " + "-"*45)
    test_vals = [(0.01, "deep UV"), (0.10, ""), (0.50, ""),
                 (1.00, "μ = M_GUT"), (1.41, "√2 × M_GUT"),
                 (2.76, "← SPU R₀=0.65"), (3.16, ""), (10.0, "")]
    for ratio, note in test_vals:
        r = R0_spectral(ratio)
        print(f"  {ratio:>8.3f} {r:>10.4f}  {note}")

    print()
    spu_r0 = 0.65
    mu_spu = mu_match_for_R0(spu_r0)
    print(f"SPU value R₀=0.65 corresponds to:")
    print(f"  μ_match = {mu_spu:.4f} × M_GUT  =  {mu_spu * M_GUT:.3e} GeV")
    print(f"  log₁₀(μ_match/GeV) = {np.log10(mu_spu * M_GUT):.3f}")
    print()
    print("Physical interpretation:")
    print(f"  μ_match ≈ 2.76 × M_GUT coincides with the dynamical scale")
    print(f"  at which E₇ → E₆ × U(1) branching completes — consistent")
    print(f"  with the Z₄ condensate formation scale from IR_Dominance.")

    # Optional plot
    import sys
    if '--plot' in sys.argv:
        try:
            import matplotlib.pyplot as plt
            ratios = np.logspace(-2, 2, 400)
            R0_vals = [R0_spectral(r) for r in ratios]
            fig, ax = plt.subplots(figsize=(9, 5))
            ax.semilogx(ratios, R0_vals, 'b-', linewidth=2.5, label='R₀(μ) — spectral formula')
            ax.axhline(0.65, color='red', ls='--', lw=1.5, label='SPU R₀ = 0.65')
            ax.axhline(27/28, color='gray', ls=':', lw=1.2, label='Upper bound 27/28')
            ax.axhline(117/399, color='gray', ls='-.', lw=1.2, label='Lower bound 117/399')
            ax.axhline(C2_27/C2_56, color='orange', ls=':', lw=1.2,
                       label='IR dominance lower (0.304)')
            ax.axvline(mu_spu, color='red', ls=':', alpha=0.5)
            ax.fill_between(ratios, C2_27/C2_56, 27/28, alpha=0.07, color='green',
                            label='Physical window')
            ax.set_xlabel('μ/M₀', fontsize=12)
            ax.set_ylabel('R₀(μ)', fontsize=12)
            ax.set_title('R₀(μ) — Spectral Calculation on E₇/SU(8)', fontsize=13)
            ax.legend(fontsize=9)
            ax.grid(True, which='both', alpha=0.25)
            ax.set_ylim(0.15, 1.05)
            plt.tight_layout()
            plt.savefig('R0_spectral_road2.png', dpi=180)
            print("\nPlot salvato: R0_spectral_road2.png")
        except ImportError:
            print("matplotlib non disponibile.")

if __name__ == '__main__':
    main()
