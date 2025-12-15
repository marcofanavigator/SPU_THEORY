#!/usr/bin/env python3
"""
plot_unification_1loop.py

Calcola e visualizza il running 1-loop dei tre gauge couplings (alpha_i)
usa la formula esatta 1-loop:
  1/alpha(Q) = 1/alpha(MZ) + (b0 / (2*pi)) * ln(Q / MZ)

Input: valori sperimentali a MZ e coefficienti b0 (user-provided)
Output: grafico log(Q) vs alpha, stampa valori a M_GUT, calcolo Landau-pole U(1).
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
from scipy.optimize import brentq

# -----------------------------
# INPUT (dai tuoi risultati)
MZ = 91.2  # GeV
alpha1_MZ = 0.05844115  # U(1)_Y (GUT-normalized as used)
alpha2_MZ = 0.03365000  # SU(2)
alpha3_MZ = 0.11840000  # SU(3)

# one-loop beta coefficients (user-provided / convention used in your script)
# Using the same sign/convention you used: 1/alpha(Q) = 1/alpha(MZ) + (b0/(2pi)) ln(Q/MZ)
b1 = 4.1000
b2 = 3.1667
b3 = 7.0000

# reported M_GUT from your run (we will also compute it by solving alpha2=alpha3)
M_GUT_reported = 3.162e16

# -----------------------------
# helper functions
def inv_alpha_at_Q(inv_alpha_MZ, b0, Q):
    return inv_alpha_MZ + (b0/(2.0*pi)) * math.log(Q / MZ)

def alpha_at_Q(alpha_MZ, b0, Q):
    inv = inv_alpha_at_Q(1.0/alpha_MZ, b0, Q)
    return 1.0 / inv

# compute running arrays
Q_min = MZ
Q_max = 1e18
Qs = np.logspace(math.log10(Q_min), math.log10(Q_max), 1200)

alph1 = np.array([alpha_at_Q(alpha1_MZ, b1, Q) for Q in Qs])
alph2 = np.array([alpha_at_Q(alpha2_MZ, b2, Q) for Q in Qs])
alph3 = np.array([alpha_at_Q(alpha3_MZ, b3, Q) for Q in Qs])

# Compute M_GUT by solving equality of alpha2 and alpha3 (1-loop closed form)
# Solve 1/alpha2(Q)=1/alpha3(Q) => 1/alpha2_MZ + (b2/2pi) ln(Q/MZ) = 1/alpha3_MZ + (b3/2pi) ln(Q/MZ)
# => ln(Q/MZ) * ( (b2-b3)/(2pi) ) = 1/alpha3_MZ - 1/alpha2_MZ
num = 1.0/alpha3_MZ - 1.0/alpha2_MZ
den = (b2 - b3) / (2.0*pi)
if den == 0:
    print("b2 == b3, cannot solve analytically")
    M_GUT_solved = None
else:
    lnQ = num / den
    M_GUT_solved = MZ * math.exp(lnQ)

# Compute alpha values at M_GUT_solved (if exists)
if M_GUT_solved and M_GUT_solved > 0 and np.isfinite(M_GUT_solved):
    a1_at_gut = alpha_at_Q(alpha1_MZ, b1, M_GUT_solved)
    a2_at_gut = alpha_at_Q(alpha2_MZ, b2, M_GUT_solved)
    a3_at_gut = alpha_at_Q(alpha3_MZ, b3, M_GUT_solved)
else:
    a1_at_gut = a2_at_gut = a3_at_gut = None

# Compute Landau pole for U(1): solve 1/alpha1(Q) -> 0  => ln(Q_pole/MZ) = - (2pi)/(b1*alpha1_MZ)
if b1 * alpha1_MZ > 0:
    lnQpole = - (2.0 * pi) / (b1 * alpha1_MZ)
    Q_pole = MZ * math.exp(lnQpole)
    if lnQpole > 0:
        # positive log means Q_pole > MZ ; otherwise it's < MZ (unphysical here)
        pass
else:
    Q_pole = math.inf  # no pole in this convention

# -----------------------------
# Print concise summary (to compare with your output)
print("\n=== SUMMARY (1-loop) ===")
print("M_Z = {:.3f} GeV".format(MZ))
print("Reported M_GUT = {:.3g} GeV".format(M_GUT_reported))
if M_GUT_solved:
    print("Solved    M_GUT = {:.3g} GeV".format(M_GUT_solved))
else:
    print("Solved    M_GUT = None")

if a1_at_gut is not None:
    print("\nAlpha at M_GUT (solved):")
    print(" alpha1(M_GUT) = {:.8f}".format(a1_at_gut))
    print(" alpha2(M_GUT) = {:.8f}".format(a2_at_gut))
    print(" alpha3(M_GUT) = {:.8f}".format(a3_at_gut))
    print(" |alpha2-alpha3| = {:.8e}".format(abs(a2_at_gut - a3_at_gut)))
else:
    print("Could not compute alphas at M_GUT")

print("\nLandau pole U(1) (1-loop): Q_pole = {}".format("inf (no pole)" if (not np.isfinite(Q_pole) or Q_pole>1e50) else "{:.3g} GeV".format(Q_pole)))

# -----------------------------
# Plot
plt.figure(figsize=(8,5))
plt.loglog(Qs, alph1, label=r'$\alpha_1$ (U(1)_Y)')
plt.loglog(Qs, alph2, label=r'$\alpha_2$ (SU(2)_L)')
plt.loglog(Qs, alph3, label=r'$\alpha_3$ (SU(3)_c)')

# markers
plt.axvline(MZ, color='k', linestyle=':', linewidth=0.8, label=r'$M_Z$')
if M_GUT_solved:
    plt.axvline(M_GUT_solved, color='gray', linestyle='--', linewidth=1.0, label=r'$M_{GUT}$ (solved)')
    plt.scatter([M_GUT_solved], [a2_at_gut], color='C1', s=40)
    plt.scatter([M_GUT_solved], [a3_at_gut], color='C2', s=40)

# cosmetic
plt.xlabel('Q [GeV] (log scale)')
plt.ylabel(r'$\alpha(Q)$')
plt.title('1-loop running of gauge couplings (exact 1-loop formula)')
plt.xlim(MZ*0.9, Q_max)
plt.ylim(1e-3, 0.5)
plt.legend()
plt.grid(which='both', linestyle=':', linewidth=0.5)
plt.savefig('unification_1loop_plot.png', dpi=200)
print("\nSaved plot to unification_1loop_plot.png")
plt.show()
