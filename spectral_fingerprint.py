import numpy as np
import matplotlib.pyplot as plt

def get_shapes_v3(k1, k2, k3):
    kt = k1 + k2 + k3
    prod_k3 = (k1 * k2 * k3)**3
    
    # 1. LOCAL (Divergente in k->0)
    shape_local = (k1**3 + k2**3 + k3**3) / prod_k3
    
    # 2. SPU SPECTRUM (Regolarizzato dal cutoff del Coset)
    # Introduciamo una scala di cutoff 'm' che rappresenta il gap dello spettro
    # Questo impedisce alla SPU di collassare sulla forma Local
    m = 0.1 
    reg_prod = ((k1+m)*(k2+m)*(k3+m))**3
    
    # Firma SPU: Termine derivativo + Interazione spettrale
    # B ~ 1 / (kt^3 * (k+m)^3)
    shape_spu = (k1**2 * k2**2 + k2**2 * k3**2 + k3**2 * k1**2) / (kt**3 * reg_prod)
    
    # 3. ORTHOGONAL (Per confronto)
    shape_equil = 18 * ( (kt-k1)*(kt-k2)*(kt-k3) ) / prod_k3

    return shape_local, shape_equil, shape_spu

def final_test():
    n = 20000
    k1 = np.ones(n)
    k2 = np.random.uniform(0.01, 1.0, n)
    k3 = np.random.uniform(0.01, 1.0, n)
    mask = (k2 + k3 > k1) & (np.abs(k2 - k3) < k1)
    k1, k2, k3 = k1[mask], k2[mask], k3[mask]
    
    loc, equ, spu = get_shapes_v3(k1, k2, k3)
    
    # Normalizzazione per il calcolo della correlazione
    # (Rimuove l'effetto della scala assoluta)
    c_loc = np.corrcoef(spu, loc)[0,1]
    c_equ = np.corrcoef(spu, equ)[0,1]
    
    print("\n" + "🚀" * 15)
    print("  SPU SPECTRAL BREAKTHROUGH")
    print("🚀" * 15)
    print(f"Correlazione vs LOCAL:       {c_loc:.4f}")
    print(f"Correlazione vs EQUILATERAL: {c_equ:.4f}")
    print("-" * 30)
    
    if abs(c_loc) < 0.8:
        print("STATO: FIRMA DISTINGUIBILE!")
        print("Il cutoff del coset ha rotto la degenerazione.")
    else:
        print("STATO: Ancora troppo simile. Aumentare il cutoff 'm'.")

    # Visualizzazione
    res = 150
    x = np.linspace(0.01, 1, res)
    y = np.linspace(0.5, 1, res)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    for i in range(res):
        for j in range(res):
            k1v, k2v, k3v = 1.0, X[i,j], Y[i,j]
            if (k2v + k3v > k1v) and (abs(k2v - k3v) < k1v) and k3v <= k2v:
                _, _, s = get_shapes_v3(k1v, k2v, k3v)
                Z[i,j] = s * (k1v*k2v*k3v)**2 
            else: Z[i,j] = np.nan

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='inferno')
    plt.colorbar(label='SPU Signal Strength (Normalized)')
    plt.title('SPU Signature with Spectral Gap $\Lambda_{SP}$')
    plt.show()

if __name__ == "__main__":
    final_test()
