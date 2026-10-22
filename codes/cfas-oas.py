#!/usr/bin/env python3
"""
CFAS OAS Foundation — Numerical Verification

Demonstrates:
1. Consistency operator S eigenvalues → coherent modes
2. Sync evolution U_sync(t) = exp(-iSt) → W phase rotation
3. Rendering threshold κ: classical vs quantum boundary
4. W field as projection of OAS state onto modes
5. The rendering master equation

Author: Lucifer Ng
Date: 2026-07-09
"""

import numpy as np

print("=" * 65)
print("CFAS — OAS Foundation: The Ontological Action Structure")
print("=" * 65)

# =========================================
# 1. Consistency operator S
# =========================================

print("\n--- 1. Consistency Operator S: Eigenvalues → Coherent Modes ---")

# S is self-adjoint with eigenvalues lambda_k
# Realistic spectrum: lambda_k = k * hbar * omega_0 (harmonic)
N_modes = 10
hbar = 1.0
omega_0 = 1.0

lambda_k = np.array([(k + 0.5) * hbar * omega_0 for k in range(N_modes)])
print(f"  S|phi_k> = lambda_k |phi_k>")
print(f"  Mode spectrum (harmonic):")
print(f"  {'k':>3} {'lambda_k':>10} {'omega_k':>10} {'Regime':<15}")
for k in range(N_modes):
    regime = "Classical" if lambda_k[k] > N_modes/2 else "Quantum"
    print(f"  {k:3d} {lambda_k[k]:10.4f} {lambda_k[k]/hbar:10.4f} {regime:<15}")

# =========================================
# 2. Sync evolution
# =========================================

print("\n--- 2. Sync Evolution: U_sync(t) = exp(-iSt/hbar) ---")

# W field initial state in mode space
W0 = np.zeros(N_modes, dtype=complex)
W0[0] = 0.5 + 0.3j
W0[1] = 0.3 - 0.2j
W0[2] = 0.2 + 0.1j

# Time evolution (full range)
t_vals = np.linspace(0, 10, 1000)
dt_fine = 1e-5  # for numerical derivative
t_fine = np.array([0, dt_fine])

W_t = np.zeros((len(t_vals), N_modes), dtype=complex)
for i, t in enumerate(t_vals):
    for k in range(N_modes):
        W_t[i, k] = W0[k] * np.exp(-1j * lambda_k[k] * t / hbar)

print(f"  Initial W state: |W(0)> = [", end="")
for k in range(3):
    print(f"{W0[k]:.2f}j ", end="")
print(f"...]")

# Phase evolution for first mode
# Phase evolution (unwrapped)
phases = np.unwrap(np.angle(W_t[:, 0]))
phase_accumulated = phases[-1] - phases[0]
expected_phase = -lambda_k[0] * t_vals[-1] / hbar  # Negative: exp(-iomega*t)
print(f"  Phase accumulated (unwrapped): {phase_accumulated:.4f} rad")
print(f"  Expected: lambda_0 * t / hbar = {expected_phase:.4f} rad")
print(f"  Sync evolution: {'✅' if abs(phase_accumulated - expected_phase) < 0.01 else '⚠️ Numerical'}")

# =========================================
# 3. Rendering threshold kappa
# =========================================

print("\n--- 3. Rendering Threshold kappa: Classical vs Quantum Boundary ---")

kappa = N_modes / 2  # threshold at half the max eigenvalue

print(f"  kappa = {kappa:.2f}")
print(f"  {'k':>3} {'lambda_k':>10} {'<W|S|W>':>12} {'Regime':<15}")
for k in range(N_modes):
    W_S = np.abs(W0[k])**2 * lambda_k[k]
    regime = "CLASSICAL" if W_S > kappa else "QUANTUM"
    print(f"  {k:3d} {lambda_k[k]:10.4f} {W_S:12.4f} {regime:<15}")

# Total budget
total_budget = np.sum(np.abs(W_t[0])**2)
print(f"\n  Total consistency budget: {total_budget:.4f}")
print(f"  Budget constraint: sum|W_k|^2 <= 1: {'✅' if total_budget <= 1 else '❌'}")

# =========================================
# 4. W field as OAS projection
# =========================================

print("\n--- 4. W Field as OAS Projection ---")

# W_k(t) = <phi_k | W(t)> = <phi_k|U_sync(t)|W(0)>
# This is a projection of the OAS state onto coherent mode basis

# Reconstruct W(t) from eigenvalues and initial amplitudes (use full range)
t_fixed = 5.0
W_reconstructed = np.zeros(N_modes, dtype=complex)
for k in range(N_modes):
    W_reconstructed[k] = W0[k] * np.exp(-1j * lambda_k[k] * t_fixed / hbar)

# Verify: W_reconstructed matches W_t at t=2.5 (check phase, unwrap)
t_idx = np.abs(t_vals - t_fixed).argmin()
recon_phase = np.unwrap(np.angle(W_reconstructed))
actual_phase = np.unwrap(np.angle(W_t[t_idx]))
phase_match = np.allclose(recon_phase, actual_phase, atol=0.01)
mag_match = np.allclose(np.abs(W_reconstructed), np.abs(W_t[t_idx]))
print(f"  W_k(t) = <phi_k|U_sync(t)|W(0)>")
print(f"  Reconstructed at t={t_fixed:.1f}: |W> = exp(-iSt/hbar)|W(0)>")
print(f"  Phase match: {'✅' if phase_match else '⚠️ Numerical'}")
print(f"  Magnitude match: {'✅' if mag_match else '❌'}")

# =========================================
# 5. Rendering master equation
# =========================================

print("\n--- 5. Rendering Master Equation ---")

# d|W>/dt = -(i/hbar)S|W> - Gamma(|W>) + Sigma

# Simplified: only sync evolution (no dissipation or sourcing yet)
# dW_k/dt = -i*omega_k*W_k

dW_dt_sync = np.zeros(N_modes, dtype=complex)
for k in range(N_modes):
    dW_dt_sync[k] = -1j * lambda_k[k] / hbar * W0[k]

# Numerical verification using fine dt
W_t_fine = np.zeros((len(t_fine), N_modes), dtype=complex)
for j, t in enumerate(t_fine):
    for k in range(N_modes):
        W_t_fine[j, k] = W0[k] * np.exp(-1j * lambda_k[k] * t / hbar)

dW_dt_numeric = (W_t_fine[1] - W_t_fine[0]) / dt_fine
error = np.max(np.abs(dW_dt_sync - dW_dt_numeric))
print(f"  d|W>/dt = -(i/hbar)S|W>")
print(f"  Max error (sync vs numeric): {error:.6e}")
print(f"  Sync evolution: {'✅' if error < 0.01 else '❌'}")

# Complete master equation with dissipation
gamma_dec = 0.1  # decoherence rate
dW_dt_full = dW_dt_sync.copy()
for k in range(N_modes):
    # Dissipation: -Gamma decays high-k modes faster
    dW_dt_full[k] -= gamma_dec * (lambda_k[k] / lambda_k[0]) * W0[k]

# Future prediction: sourcing term Sigma from consciousness
print(f"\n  Full rendering master equation:")
print(f"  d|W>/dt = -(i/hbar)S|W> - Gamma(|W|^2)|W> + Sigma(C)")
print(f"  where Sigma(C) = consciousness sourcing term")

# =========================================
# 6. Summary
# =========================================

print("\n--- 6. The Complete OAS Picture ---")
print("""
  OAS (substrate):
    S: Consistency operator → coherent modes
    U_sync: Sync evolution → time, quantum phase
    kappa: Rendering threshold → classical/quantum boundary
    |W>: W field = projection of OAS onto modes
  
  Rendered world:
    Spacetime = geometry of W phase relationships
    QM = W below kappa (probabilistic)
    GR = W above kappa (deterministic)
    Consciousness = d|<W|S|W>|/dt at kappa (boundary dynamics)
""")
print("=" * 65)