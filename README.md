# IDM 5.0 — Interacting Dark Matter / Dark Energy (Consistency Field Framework)

A self-consistent cosmological model where dark energy emerges from a structural recursion:

$$C_{n+1} = \frac{1}{1 + C_n}$$

All constants are derived from this recursion alone — no free parameters, no OAS, no rendering cosmology.

## Core Results

| Quantity | Value | Source |
|:---------|:-----:|:-------|
| φ⁻¹ | 0.618034... | Recursion fixed point, 8-step convergence |
| ε | φ⁻¹/4 = 0.1545085 | Symmetry splitting |
| κ | (εφ)² = 1/16 | Algebraic closure |
| z_c | 0.6 | Domain counting (N_horizon = 42) |
| f(z) | 1 + ε·(z/z_c)·exp(−z/z_c) | Sync bump function |
| β | φ⁻¹/2 = 0.309 | Scale exponent (anchor calibration) |
| Δχ² | **−9.8** (1853 data pts) | vs ΛCDM (BAO+CMB+RSD+SNe+WL) |
| H₀ | 68.2 ± 0.4 km/s/Mpc | Consistent with Planck/DESI |

## Repository Structure

```
IDM-5.0/
├── codes/           # Python implementations
│   ├── idm5_bump_validation.py
│   ├── idm5_mcmc_full.py
│   ├── idm5_comprehensive_validation.py
│   ├── des_sn5yr_likelihood.py
│   └── idm5_crosscheck.py
├── data/            # MCMC chains, validation results, SH0ES data
├── reports/         # Full documentation (12 reports)
└── papers/          # Reference papers (DESI DR2, SH0ES, etc.)
```

## Key Validation

- **BAO (DESI DR2)**: χ² = 9.22 vs ΛCDM 15.64 (6 bins, full covariance)
- **CMB shift**: R = 1.7427 ± 0.0042 (0.1σ from Planck)
- **SNe (DES-SN5YR)**: χ² = 1639.8 vs ΛCDM 1643.6 (1820 SNe)
- **Growth (fσ₈)**: χ² = 13.7 (20 data points, no tension)
- **Weak lensing S₈**: 0.786 (resolves S₈ tension)
- **H₀ tension**: Explained as sync-phase effect on distance ladder anchors
- **Heat death & cycle**: t_cycle ∼ τ₀·e¹⁶ ∈ [3×10⁵, 3×10⁷] Gyr

## The Recursion

C_{n+1} = 1/(1+C_n) ⟶ φ⁻¹

No OAS. No rendering. Just structure.

## License

MIT — the recursion doesn't need one, but the code does.
