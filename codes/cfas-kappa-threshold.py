#!/usr/bin/env python3
"""
CFAS — κ Derivation: Information-Theoretic Threshold (Corrected)

κ = 1/16 = 0.0625 from B/N_particles, NOT from generation spectrum.
"""

import numpy as np

print("=" * 65)
print("CFAS — κ: Information-Theoretic Threshold")
print("=" * 65)

B = 1.0  # total budget
N_particles = 16  # Weyl fermions per SM generation
kappa = B / N_particles

print(f"B = {B} (total budget)")
print(f"N_particles = {N_particles} (Weyl fermions per SM generation)")
print(f"κ = B/N_particles = {kappa:.4f} = 1/{N_particles}")

# Generation spectrum
alpha = 1.0
lambdas = np.exp(-alpha * np.arange(10))

print(f"\nCheck against generation spectrum:")
print(f"{'n':>3} | {'λ_n':>8} | {'|W|²':>8} | {'P = |W|²/B':>12} | {'Detectable?':>12}")
print(f"{'-'*3} | {'-'*8} | {'-'*8} | {'-'*12} | {'-'*12}")
for n in range(6):
    W_sq = lambdas[n]
    P = W_sq / B
    detectable = "✅" if P >= kappa else "❌"
    marginal = " ⚠️ MARGINAL" if 0.03 < P < kappa else ""
    print(f"{n:>3} | {lambdas[n]:>8.4f} | {W_sq:>8.4f} | {P:>12.4f} | {detectable:>12}{marginal}")

print(f"\n3rd gen: P = 0.050 < κ = {kappa:.4f} → marginal (factor {kappa/0.050:.2f})")
print(f"4th gen: P = 0.018 < κ = {kappa:.4f} → hidden (factor {kappa/0.018:.2f})")

print(f"\n" + "=" * 65)
print(f"κ = 1/{N_particles} = {kappa:.4f}")
print(f"Derived from B/N_particles, NOT from generation spectrum.")
print(f"= " * 22)