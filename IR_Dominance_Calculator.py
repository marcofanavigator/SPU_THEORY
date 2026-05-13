#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IR_Dominance_Calculator.py
Calcolo del rapporto R(μ) = κ₃(μ)/κ₄(μ) e della scala di crossover μ*
nel framework SPU, basato sulla dominanza IR da geometria E₇/SU(8)

Dipendenze: numpy, matplotlib (opzionale per plotting)
Compatibile con SageMath: eseguire con `sage IR_Dominance_Calculator.py`
"""

import numpy as np
from typing import Tuple, Optional
import warnings

# =============================================================================
# PARAMETRI GEOMETRICI FISSI (da teoria dei gruppi)
# =============================================================================

# Casimir quadratici (normalizzazione: radice lunga² = 2)
C2_56 = 57/2        # C₂(E₇, fondamentale 56) ≈ 28.5
C2_27 = 26/3        # C₂(E₆, fondamentale 27) ≈ 8.667

# Scala di riferimento UV (GUT scale)
M_GUT = 1.8e16      # GeV

# Gap spettrale
DELTA_C2 = C2_56 - C2_27  # ≈ 19.833

# =============================================================================
# FUNZIONI PRINCIPALI
# =============================================================================

def running_ratio(mu: np.ndarray, R0: float, M0: float = M_GUT) -> np.ndarray:
    """
    Calcola il rapporto R(μ) = κ₃(μ)/κ₄(μ) secondo la formula RG:
    
    R(μ) = R₀ · [C₂(56) + μ²/M₀²] / [C₂(27) + μ²/M₀²]
    
    Parametri:
    ----------
    mu : array_like
        Scala di energia μ (GeV), può essere scalare o array
    R0 : float
        Rapporto UV iniziale κ₃⁰/κ₄⁰, deve soddisfare C₂(27)/C₂(56) < R₀ < 1
    M0 : float, optional
        Scala di riferimento (default: M_GUT)
    
    Returns:
    --------
    R : ndarray
        Rapporto R(μ) valutato alle scale richieste
    """
    mu = np.asarray(mu)
    x = (mu / M0)**2
    
    numerator = C2_56 + x
    denominator = C2_27 + x
    
    return R0 * numerator / denominator


def crossover_scale(R0: float, M0: float = M_GUT) -> Optional[float]:
    """
    Calcola la scala di crossover μ* dove R(μ*) = 1:
    
    μ*² = M₀² · [R₀·C₂(56) - C₂(27)] / [1 - R₀]
    
    Parametri:
    ----------
    R0 : float
        Rapporto UV iniziale
    M0 : float, optional
        Scala di riferimento
    
    Returns:
    --------
    mu_star : float or None
        Scala di crossover μ* (GeV), o None se non esiste
    """
    # Formula corretta derivata da R(μ*) = 1
    numerator = R0 * C2_56 - C2_27      # ✅ R₀·C₂(56) - C₂(27)
    denominator = 1 - R0                 # ✅ 1 - R₀
    
    if abs(denominator) < 1e-10:  # Evita divisione per zero
        warnings.warn("R₀ ≈ 1: crossover a μ → ∞ (quartico mai dominato)")
        return None
    
    mu2_star = M0**2 * numerator / denominator
    
    if mu2_star <= 0:
        # Interpretazione fisica: nessun crossover nel regime accessibile
        if R0 <= C2_27 / C2_56:
            warnings.warn(f"R₀ = {R0:.4f} ≤ {C2_27/C2_56:.3f}: cubic non domina mai in IR")
        elif R0 >= 1.0:
            warnings.warn(f"R₀ = {R0:.4f} ≥ 1.0: cubic domina già in UV (inconsistente)")
        else:
            warnings.warn(f"R₀ = {R0:.4f}: crossover a scale non fisiche (μ*² = {mu2_star:.3e})")
        return None
    
    return np.sqrt(mu2_star)


def check_consistency(R0: float) -> dict:
    """
    Verifica le condizioni di consistenza per il meccanismo di dominanza IR.
    
    Returns:
    --------
    dict con chiavi:
        'valid_range': bool, R₀ nel range ammissibile
        'mu_star_exists': bool, crossover scale esiste
        'mu_star_value': float or None, valore di μ*
        'IR_dominant': bool, κ₃ domina nell'IR (μ → 0)
        'UV_behavior': str, descrizione comportamento UV
    """
    result = {
        'valid_range': False,
        'mu_star_exists': False,
        'mu_star_value': None,
        'IR_dominant': False,
        'UV_behavior': None
    }
    
    # Range ammissibile per R₀
    R_min = C2_27 / C2_56  # ≈ 0.304
    R_max = 1.0
    
    result['valid_range'] = R_min < R0 < R_max
    
    if result['valid_range']:
        # Comportamento IR: μ → 0
        R_IR = R0 * C2_56 / C2_27
        result['IR_dominant'] = R_IR > 1  # κ₃ > κ₄ in IR
        
        # Crossover scale
        mu_star = crossover_scale(R0)
        result['mu_star_exists'] = mu_star is not None
        result['mu_star_value'] = mu_star
        
        # Comportamento UV: μ → ∞
        result['UV_behavior'] = f"R(μ→∞) = R₀ = {R0:.4f} < 1 → quartico domina in UV"
    
    return result


# =============================================================================
# PLOTTING (opzionale, richiede matplotlib)
# =============================================================================

def plot_running_ratio(R0_values: list, mu_range: Tuple[float, float] = None, 
                       save_path: str = None) -> None:
    """
    Genera plot di R(μ) vs μ/M₀ per diversi valori di R₀.
    
    Parametri:
    ----------
    R0_values : list of float
        Lista di valori R₀ da plottere
    mu_range : tuple, optional
        Intervallo di scale [μ_min, μ_max] in GeV
    save_path : str, optional
        Percorso per salvare il plot
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("⚠ matplotlib non disponibile: plotting disabilitato")
        return
    
    if mu_range is None:
        mu_range = (1e10, 1e18)  # Da 10 TeV a 100 EeV
    
    mu = np.logspace(np.log10(mu_range[0]), np.log10(mu_range[1]), 500)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(R0_values)))
    
    for R0, color in zip(R0_values, colors):
        R = running_ratio(mu, R0)
        label = f"R₀ = {R0:.3f}"
        ax.loglog(mu, R, label=label, color=color, linewidth=2)
        
        # Evidenzia crossover se esiste
        mu_star = crossover_scale(R0)
        if mu_star and mu_range[0] <= mu_star <= mu_range[1]:
            ax.axvline(mu_star, color=color, linestyle='--', alpha=0.5)
            ax.plot(mu_star, 1.0, 'o', color=color, markersize=8)
    
    # Linee di riferimento
    ax.axhline(1.0, color='gray', linestyle=':', alpha=0.7, label='R = 1 (crossover)')
    ax.axhline(C2_56/C2_27, color='red', linestyle=':', alpha=0.5, 
               label=f'R(μ→0) = C₂(56)/C₂(27) ≈ {C2_56/C2_27:.2f}')
    
    ax.set_xlabel(r'Scale $\mu$ [GeV]', fontsize=12)
    ax.set_ylabel(r'Ratio $\mathcal{R}(\mu) = \kappa_3(\mu)/\kappa_4(\mu)$', fontsize=12)
    ax.set_title('IR Dominance: Running of Cubic/Quartic Harmonics in SPU', fontsize=14)
    ax.legend(fontsize=10, loc='lower right')
    ax.grid(True, which='both', alpha=0.3)
    
    # Annotazioni fisiche
    ax.text(0.02, 0.98, 
            f'C₂(56) = {C2_56:.2f}\nC₂(27) = {C2_27:.2f}\nΔC₂ = {DELTA_C2:.2f}',
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✓ Plot salvato in: {save_path}")
    
    plt.show()


# =============================================================================
# ANALISI NUMERICA E REPORT
# =============================================================================

def generate_report(R0: float, M0: float = M_GUT) -> str:
    """
    Genera un report testuale completo per un dato valore di R₀.
    """
    cons = check_consistency(R0)
    
    report = []
    report.append("=" * 70)
    report.append("SPU IR DOMINANCE ANALYSIS REPORT")
    report.append("=" * 70)
    report.append(f"\nInput parameters:")
    report.append(f"  R₀ (UV ratio κ₃⁰/κ₄⁰) = {R0:.5f}")
    report.append(f"  M₀ (reference scale)  = {M0:.3e} GeV")
    report.append(f"  C₂(56) = {C2_56:.3f}, C₂(27) = {C2_27:.3f}, ΔC₂ = {DELTA_C2:.3f}")
    
    report.append(f"\nConsistency checks:")
    report.append(f"  ✓ R₀ in valid range ({C2_27/C2_56:.3f} < R₀ < 1): {cons['valid_range']}")
    
    if cons['valid_range']:
        R_IR = R0 * C2_56 / C2_27
        R_UV = R0
        report.append(f"\nAsymptotic behavior:")
        report.append(f"  UV (μ → ∞): R(μ) → {R_UV:.4f} {'< 1 → quartic dominates' if R_UV < 1 else '> 1 → cubic dominates'}")
        report.append(f"  IR (μ → 0):  R(μ) → {R_IR:.4f} {'> 1 → cubic dominates ✓' if R_IR > 1 else '< 1 → quartic dominates ✗'}")
        
        if cons['mu_star_exists']:
            mu_star = cons['mu_star_value']
            report.append(f"\nCrossover scale:")
            report.append(f"  μ* = {mu_star:.3e} GeV")
            report.append(f"  μ*/M₀ = {mu_star/M0:.3f}")
            report.append(f"  log₁₀(μ*/GeV) = {np.log10(mu_star):.2f}")
            
            # Confronto con scale fisiche
            if mu_star < 1e16:
                report.append(f"  → Crossover BELOW GUT scale (potenziale problema)")
            elif mu_star > 1e18:
                report.append(f"  → Crossover ABOVE Planck scale (dominanza IR ritardata)")
            else:
                report.append(f"  → Crossover in physical window [GUT, M_Pl] ✓")
        else:
            report.append(f"\n⚠ No physical crossover scale (κ₃ never dominates)")
    
    report.append(f"\nFalsification conditions:")
    report.append(f"  ✗ R₀ ≥ 1.0: cubic già domina in UV (inconsistente con E₇)")
    report.append(f"  ✗ R₀ ≤ {C2_27/C2_56:.3f}: cubic non domina mai in IR")
    report.append(f"  ✗ μ* < ℓₛₚ⁻¹ ~ 10³² GeV: dominanza IR non accessibile")
    
    report.append("\n" + "=" * 70)
    
    return "\n".join(report)


# =============================================================================
# FUNZIONE PRINCIPALE (esecuzione diretta)
# =============================================================================

def main():
    """Esecuzione di esempio con valori rappresentativi."""
    
    print("\n" + "🔷"*35)
    print("SPU IR DOMINANCE CALCULATOR")
    print("🔷"*35 + "\n")
    
    # Valori di test per R₀ (tutti nel range ammissibile)
    R0_test_values = [0.40, 0.55, 0.70, 0.85]
    
    print("Analisi per diversi valori di R₀:\n")
    
    for R0 in R0_test_values:
        print(generate_report(R0))
        print()
    
    # Generazione plot (se matplotlib disponibile)
    print("Generazione plot di R(μ) vs μ...")
    plot_running_ratio(
        R0_values=R0_test_values,
        mu_range=(1e12, 1e19),
        save_path="IR_dominance_running.png"
    )
    
    # Analisi di sensitività
    print("\n📊 Sensitivity analysis: μ* vs R₀")
    print("-" * 50)
    R0_scan = np.linspace(0.31, 0.99, 50)
    mu_stars = [crossover_scale(R0) for R0 in R0_scan]
    
    valid_pairs = [(R0, mu) for R0, mu in zip(R0_scan, mu_stars) if mu is not None]
    
    if valid_pairs:
        R0_valid, mu_valid = zip(*valid_pairs)
        print(f"  Range R₀ valido: [{min(R0_valid):.3f}, {max(R0_valid):.3f}]")
        print(f"  μ* varia da: {min(mu_valid)/M_GUT:.2f}×M₀ a {max(mu_valid)/M_GUT:.2f}×M₀")
        
        # Valore "naturale" stimato
        R0_natural = 0.65  # ipotesi ragionevole da dinamica del coset
        mu_star_nat = crossover_scale(R0_natural)
        if mu_star_nat:
            print(f"\n  Ipotesi R₀ ≈ {R0_natural:.2f} → μ* ≈ {mu_star_nat:.3e} GeV")
            print(f"  → log₁₀(μ*/GeV) ≈ {np.log10(mu_star_nat):.1f}")
    
    print("\n✅ Script completato. Per uso personalizzato:")
    print("   from IR_Dominance_Calculator import running_ratio, crossover_scale, check_consistency")
    print("   R = running_ratio(mu=1e15, R0=0.65)")
    print("   mu_star = crossover_scale(R0=0.65)")
    print("   cons = check_consistency(R0=0.65)")


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
