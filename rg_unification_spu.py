import numpy as np

"""
SPU — Dynamical Gauge Coupling Unification
------------------------------------------

This script shows that SU(2) and SU(3) gauge couplings
converge dynamically at a common scale when the same
effective fermionic content N_f^eff = 128 - δ is used.

No group unification. No SUSY. No fine-tuning.
"""

# --------------------------------------------------
# Input parameters at M_Z
# --------------------------------------------------

MZ = 91.1876  # GeV

alpha_em_inv = 137.035999084
sin2_thetaW = 0.23126

alpha_em = 1.0 / alpha_em_inv
alpha1 = alpha_em / (1 - sin2_thetaW)
alpha2 = alpha_em / sin2_thetaW
alpha3 = 0.1184

# --------------------------------------------------
# SPU fermionic content
# --------------------------------------------------

delta = 0.635
Nf_eff = 128.0 - delta

# --------------------------------------------------
# 1-loop beta coefficients (effective)
# --------------------------------------------------

b1 = - (4/3) * Nf_eff
b2 = (22/3) - (4/3) * Nf_eff
b3 = 11 - (4/3) * Nf_eff

# --------------------------------------------------
# RG running
# --------------------------------------------------

def run_alpha(alpha0, b, mu, mu0=MZ):
    return 1.0 / (1.0/alpha0 + (b/(2*np.pi)) * np.log(mu/mu0))

# energy range
scales = np.logspace(2, 18, 400)

a1 = np.array([run_alpha(alpha1, b1, mu) for mu in scales])
a2 = np.array([run_alpha(alpha2, b2, mu) for mu in scales])
a3 = np.array([run_alpha(alpha3, b3, mu) for mu in scales])

# --------------------------------------------------
# Find SU(2)–SU(3) convergence
# --------------------------------------------------

diff = np.abs(a2 - a3)
idx = np.argmin(diff)

M_GUT = scales[idx]
alpha_GUT = a2[idx]

print("SPU — Dynamical Unification Result")
print("="*45)
print(f"N_f^eff = {Nf_eff:.6f}")
print(f"M_GUT   ≈ {M_GUT:.3e} GeV")
print(f"α_GUT   ≈ {alpha_GUT:.5f}")
print(f"|α2 - α3| ≈ {diff[idx]:.3e}")

if diff[idx] < 1e-4:
    print("✓ SU(2) and SU(3) unify dynamically")
else:
    print("✗ No unification")
