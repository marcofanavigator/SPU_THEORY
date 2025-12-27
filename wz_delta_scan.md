# SPU — w(z) Scan

## Purpose

This script explores the effective equation of state w(z) induced by a mild scale dependence of the SPU parameter δ.

## Model

δ(z) is parametrized as:

```
δ(z) = δ₀ * (1 + z)^(-β)
```

The resulting dark-energy equation of state is computed assuming:

```
ρ_Λ ∝ δ(H) H²
```

## Output

The script prints w(z) for z ∈ [0, 3].

## Interpretation

For β ≲ 0.05, w(z) remains close to −1 and compatible with current observational bounds.

## Status

Exploratory / reproducible