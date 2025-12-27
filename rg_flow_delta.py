import numpy as np

# ============================================================
# RG FLOW OF delta IN THE SPU FRAMEWORK
# ============================================================

# --- Physical setup ---
# logarithmic RG scale: t = ln(mu / mu0)
t_UV = 0.0          # UV scale (reference)
t_IR = -30.0        # IR scale (many orders of magnitude)
N_steps = 5000

# initial condition for delta at UV
delta_UV = 0.05     # small but non-zero (delta=0 is unstable)

# RG grid
t_grid = np.linspace(t_UV, t_IR, N_steps)
dt = t_grid[1] - t_grid[0]

# container
delta = np.zeros(N_steps)
delta[0] = delta_UV

# ------------------------------------------------------------
# Anomalous dimension model
# ------------------------------------------------------------
# gamma_M -> 1 at the quasi-conformal regime
# simple smooth approach from UV to IR

def gamma_M(t):
    return 1.0 - 0.35 * np.exp(t / 5.0)


# ------------------------------------------------------------
# RG beta function for delta
# ------------------------------------------------------------

def beta_delta(delta, t):
    """
    RG beta function for delta:
    d(delta)/dt = 2 * delta * (1 - delta) * (gamma_M - 1)
    """
    return 2.0 * delta * (1.0 - delta) * (gamma_M(t) - 1.0)

# ------------------------------------------------------------
# RG integration (Euler method)
# ------------------------------------------------------------

for i in range(1, N_steps):
    delta[i] = delta[i-1] + beta_delta(delta[i-1], t_grid[i-1]) * dt
    
    # enforce physical bounds
    if delta[i] < 0.0:
        delta[i] = 0.0
    if delta[i] > 1.0:
        delta[i] = 1.0

# ------------------------------------------------------------
# Output summary
# ------------------------------------------------------------

print("SPU — RG Flow of delta")
print("=" * 60)
print(f"delta(UV) = {delta_UV:.6f}")
print(f"delta(IR) = {delta[-1]:.6f}")
print("------------------------------------------------------------")
print("Fixed-point behavior:")
print(f"delta_IR ~ {delta[-1]:.3f}")
print("=" * 60)

# Optional: save data
np.savetxt(
    "delta_rg_flow.dat",
    np.column_stack([t_grid, delta]),
    header="t = ln(mu/mu0)    delta(t)"
)
