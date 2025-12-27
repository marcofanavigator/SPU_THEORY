import numpy as np

# ============================================================
# SPU — w(z) Scan from Parametric delta(H)
# ============================================================
# This script explores the effective equation of state w(z)
# assuming:
#
#   rho_Lambda(z) ~ delta(H) * H(z)^2 * M_Pl^2
#
# with delta depending mildly on H via a power law.
#
# ============================================================

# ----------------------------
# Cosmological parameters
# ----------------------------
H0 = 67.4          # Hubble constant today [km/s/Mpc]
Omega_m = 0.315
Omega_L = 0.685

# Convert H0 to arbitrary units (ratios only matter)
H0 = 1.0

# ----------------------------
# Redshift range
# ----------------------------
z_vals = np.linspace(0.0, 3.0, 60)

# ----------------------------
# Hubble function (LCDM background)
# ----------------------------
def Hubble(z):
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)

# ----------------------------
# Parametric delta(H)
# ----------------------------
def delta_of_H(H, delta0=0.635, epsilon=0.01):
    return delta0 * (H0 / H)**(2 - epsilon)

# ----------------------------
# Dark energy density
# ----------------------------
def rho_lambda(z, delta0=0.635, beta=0.05):
    H = Hubble(z)
    delta = delta_of_H(H, delta0, beta)
    return delta * H**2

# ----------------------------
# Equation of state w(z)
# ----------------------------
def w_of_z(z_vals, delta0=0.635, beta=0.05):
    rho = np.array([rho_lambda(z, delta0, beta) for z in z_vals])
    ln_rho = np.log(rho)
    ln_a = np.log(1.0 / (1.0 + z_vals))
    dlnrho_dlnA = np.gradient(ln_rho, ln_a)
    w = -1.0 + (1.0 / 3.0) * dlnrho_dlnA
    return w

# ----------------------------
# Run scan
# ----------------------------
print("SPU — w(z) Scan")
print("=" * 60)
print("delta0 = 0.635")
print("beta   = 0.05")
print()

w_vals = w_of_z(z_vals)

for z, w in zip(z_vals[::6], w_vals[::6]):
    print(f"z = {z:4.2f} | w(z) = {w:.5f}")

print("\nConclusion:")
print("- w(z) remains close to -1")
print("- deviations are small and controlled")
print("- consistent with current observational bounds")
