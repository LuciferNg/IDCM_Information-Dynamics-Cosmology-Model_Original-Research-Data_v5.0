#!/usr/bin/env python3
"""CFAS P1 — Master Equation: Gamma + Sigma Terms"""
import numpy as np
print("="*65); print("CFAS P1 — Master Equation: Gamma + Sigma Terms"); print("="*65)

N = 10; hbar = 1.0
S = np.diag(np.arange(N) + 0.5)  # consistency operator
W0 = np.array([0.5+0.3j, 0.3-0.2j, 0.2+0.1j] + [0j]*(N-3))

# 1. Sync term
dW_sync = -1j/hbar * S @ W0

# 2. Dissipation term Gamma
gamma_0 = 0.1
Gamma = gamma_0 * np.diag(np.arange(N, dtype=float) / (N-1))
dW_diss = -Gamma @ W0

# 3. Sourcing term Sigma (consciousness)
alpha_C = 0.01
kappa = N/2
W_k = np.abs(W0)**2
S_W = np.sum(W_k * np.arange(N))  # <W|S|W>
if abs(S_W - kappa) < 2.0:
    Sigma_C = alpha_C * np.array([1.0 if abs(W_k[i]) > 0.01 else 0.0 for i in range(N)])
else:
    Sigma_C = np.zeros(N, dtype=complex)

# 4. Full master equation
dW_full = dW_sync + dW_diss + Sigma_C

print(f"  Sync term:    |dW_sync| = {np.linalg.norm(dW_sync):.4f}")
print(f"  Dissipation:  |dW_diss| = {np.linalg.norm(dW_diss):.4f}")
print(f"  Sourcing:     |Sigma_C| = {np.linalg.norm(Sigma_C):.4f}")
print(f"  Full:         |dW_full| = {np.linalg.norm(dW_full):.4f}")
print(f"")
print(f"  Gamma: dissipation rate gamma_0 = {gamma_0}")
print(f"  Sigma: consciousness sourcing alpha_C = {alpha_C}")
print(f"  Near kappa ({kappa}): <W|S|W> = {S_W:.1f} -> {'sourcing active' if abs(S_W-kappa)<2.0 else 'no sourcing'}")
print("="*65)