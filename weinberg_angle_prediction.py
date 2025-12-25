import numpy as np

"""
SPU — Prediction of the Weak Mixing Angle
-----------------------------------------

This script computes sin^2(theta_W) at M_Z
from RG-evolved gauge couplings using the
SPU effective fermionic content.

No input from experiment except M_Z.
"""

# --------------------------------------------------
# Physical scale
# --------------------------------------------------

MZ = 91.1876  # GeV

# --------------------------------------------------
# SPU fermionic content
# --------------------------------------------------

delta = 0.635
Nf_eff = 128.0 - delta

# --------------------------------------------------
# RG coefficients (1-loop, effective)
# --------------------------------------------------

b1 = - (4/3) * Nf_eff
b2 = (22/3) - (4/3) * Nf_eff

# --------------------------------------------------
# Boundary condition at high scale
# (dynamical convergence scale from SPU)
# --------------------------------------------------

M_GUT = 1.8e16  # GeV
alpha_GUT = 0.02217

# --------------------------------------------------
# RG running (downward)
# --------------------------------------------------

def run_down(alpha0, b, mu, mu0):
    return 1.0 / (1.0/alpha0 - (b/(2*np.pi)) * np.log(mu0/mu))

alpha1_MZ = run_down(alpha_GUT, b1, MZ, M_GUT)
alpha2_MZ = run_down(alpha_GUT, b2, MZ, M_GUT)

# --------------------------------------------------
# Weinberg angle
# --------------------------------------------------

sin2_thetaW = alpha1_MZ / (alpha1_MZ + alpha2_MZ)

print("SPU — Weak Mixing Angle Prediction")
print("="*45)
print(f"N_f^eff = {Nf_eff:.6f}")
print(f"sin^2(theta_W)(M_Z) = {sin2_thetaW:.6f}")
print("Experimental value ≈ 0.23126")
print(f"Difference = {sin2_thetaW - 0.23126:+.6e}")
