import math

# Parametri
alpha_em = 1/137.035999084
delta = 0.016886811378560483
M_P = 1.220910e19  # GeV in unità naturali (ħ=c=1)

# Calcolo passo-passo
term = math.sqrt(alpha_em * delta)
print(f"√(α_em) = {math.sqrt(alpha_em):.6e}")
print(f"√(δ) = {math.sqrt(delta):.6e}")
print(f"√(α_em·δ) = {term:.6e}")

M_P2 = M_P * M_P
print(f"M_P = {M_P:.6e} GeV")
print(f"M_P² = {M_P2:.6e} GeV²")

G_calc = term / M_P2
print(f"\nG_calc = √(α·δ)/M_P² = {G_calc:.6e} GeV⁻²")
print(f"G_target = {6.708830e-39:.6e} GeV⁻²")
print(f"Fattore = G_target/G_calc = {6.708830e-39 / G_calc:.3f}")

# Fattore 4π?
print(f"\nSe includiamo 4π:")
G_with_4pi = G_calc * 4 * math.pi
print(f"G × 4π = {G_with_4pi:.6e}")
print(f"Fattore residuo = {6.708830e-39 / G_with_4pi:.3f}")
