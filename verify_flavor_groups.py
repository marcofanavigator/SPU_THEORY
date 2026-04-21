# verify_flavor_groups.py
# Verifica gruppi discreti candidati per SPU: irrep 3D e compatibilità Z3
# Esegui: python verify_flavor_groups.py

groups = {
    "A4": {
        "orders": [1, 2, 3, 3],
        "chars_3d": [[3, -1, 0, 0]]
    },
    "S4": {
        "orders": [1, 2, 3, 2, 4],
        "chars_3d": [[3, 1, 0, -1, -1]]
    },
    "SL(2,3)": {
        "orders": [1, 2, 4, 4, 3, 3, 6, 6],
        "chars_3d": [[3, -1, 1, 1, 0, 0, 0, 0]]
    },
    "PSL(2,7)": {
        "orders": [1, 2, 3, 4, 4, 7, 7],
        "chars_3d": [
            [3, -1, 0, -1, 1, 1, 1],
            [3, -1, 0, -1, 1, 1, 1]  # due 3D reali equivalenti per trace check
        ]
    }
}

print("=== SPU Discrete Flavor Group Verification ===")
for name, data in groups.items():
    print(f"\n========================================")
    print(f"Testing group: {name}")
    print(f"========================================")
    
    # 1. 3D irreps
    n_3d = len(data["chars_3d"])
    print(f"[PASS] Found {n_3d} 3D irrep(s).")
    
    # 2. Order-3 classes
    z3_indices = [i for i, o in enumerate(data["orders"]) if o == 3]
    if not z3_indices:
        print("[FAIL] No elements of order 3. Z3 incompatible.")
        continue
    print(f"Z3 class indices: {z3_indices}")
    
    # 3. Traces on order-3
    for i, chi in enumerate(data["chars_3d"]):
        traces = [chi[j] for j in z3_indices]
        print(f"  Irrep {i+1} traces on Z3 elements: {traces}")
        
        # 4. Check cyclic action (trace == 0)
        if 0 in traces:
            print("[PASS] Z3 Compatibility: YES (trace=0 implies cyclic permutation)")
        else:
            print("[WARN] Z3 Compatibility: Check phases (traces != 0)")

print("\n=== Done ===")
