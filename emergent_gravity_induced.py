import numpy as np

# ============================================================
# SPU — Induced Gravity from Fermionic Degrees of Freedom
# ============================================================

# ----------------------------
# Fixed SPU inputs
# ----------------------------

Nf_nominal = 128
delta = 0.635092496          # valore consistente SPU
Nf_eff = Nf_nominal - delta

M_GUT = 1.8e16               # GeV
mu_UV = M_GUT
mu_IR = M_GUT / 1e20         # IR dynamical scale (not tuned)

# ----------------------------
# Sakharov induced gravity
# ----------------------------

prefactor = 1.0 / (16 * np.pi**2)

Mpl_squared = (
    Nf_eff
    * prefactor
    * (mu_UV**2 - mu_IR**2)
)

Mpl_eff = np.sqrt(Mpl_squared)

# ----------------------------
# Observed Planck scale
# ----------------------------

Mpl_obs = 1.2209e19  # GeV

# ----------------------------
# Output
# ----------------------------

print("=" * 70)
print("SPU — Induced Emergent Gravity")
print("=" * 70)

print(f"Nf_eff           = {Nf_eff:.6f}")
print(f"mu_UV            = {mu_UV:.3e} GeV")
print(f"mu_IR            = {mu_IR:.3e} GeV")
print()
print(f"M_Pl (SPU)       = {Mpl_eff:.3e} GeV")
print(f"M_Pl (observed)  = {Mpl_obs:.3e} GeV")
print()
print(f"Ratio SPU / obs  = {Mpl_eff / Mpl_obs:.3f}")
print("=" * 70)
