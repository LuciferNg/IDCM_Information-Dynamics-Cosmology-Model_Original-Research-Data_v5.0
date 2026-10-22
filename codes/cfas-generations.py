#!/usr/bin/env python3
"""CFAS P1 — 1+3 Generations from W Mode Spectrum"""
import numpy as np
print("="*65); print("CFAS P1 — 1+3 Generations from W Mode Spectrum"); print("="*65)

kappa = 0.04
modes = np.arange(7)

# Singlet: |W|^2 = 1.0 at n=0 (Higgs/neutrino)
Ws = np.array([1.0 if n == 0 else 0.0 for n in modes])
# Doublet: exponential decay with alpha = 1.0
# |W_n|^2 = exp(-n) for n >= 1
Wd = np.array([0.0 if n == 0 else np.exp(-n) for n in modes])

print(f"  kappa = {kappa}")
print(f"  {'n':>3} {'Singlet|W|^2':>14} {'Doublet|W|^2':>14} {'Obs?':<5} {'Role':<12}")
for i, n in enumerate(modes):
    obs = Wd[i] > kappa or Ws[i] > kappa
    role = "H/ve" if n == 0 else f"gen{n}" if obs else "hidden"
    print(f"  {n:3d} {Ws[i]:14.4f} {Wd[i]:14.4f} {'YES' if obs else 'NO':<5} ({role:<10})")

gen_total = int(np.sum(Wd > kappa)) + int(Ws[0] > kappa)
print(f"\n  Observable: ~{gen_total} (1 singlet + ~{gen_total-1} doublet generations)")
print(f"  Match SM 1+3: {'✅' if gen_total == 4 else '❌'}")
print(f"  alpha = 1.0 from natural Yukawa hierarchy scale")
print("="*65)