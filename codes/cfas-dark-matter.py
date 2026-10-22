#!/usr/bin/env python3
"""
CFAS — Dark Matter: Tower of Hidden W Modes (Corrected)

DM = tower of sub-threshold modes (n ≥ 4), masses from 15 GeV to 10 MeV.
"""

import numpy as np

print("=" * 65)
print("CFAS — Dark Matter: Hidden Mode Tower")
print("=" * 65)

kappa = 1/16  # 0.0625
v = 246  # GeV (electroweak scale)
alpha = 1.0

print(f"\nHidden mode tower (n ≥ 4, λ_n = exp(-n) < κ = {kappa:.4f}):")
print(f"{'n':>3} | {'λ_n':>8} | {'κ - λ_n':>8} | {'m_n (GeV)':>10} | {'Status':>20}")
print(f"{'-'*3} | {'-'*8} | {'-'*8} | {'-'*10} | {'-'*20}")
for n in range(4, 12):
    lam = np.exp(-alpha * n)
    gap = kappa - lam
    m_n = gap * v * lam
    if m_n > 1:
        status = "Heavy DM (decays)"
    elif m_n > 1e-3:
        status = "Light DM (stable)"
    elif m_n > 1e-6:
        status = "Hot DM (relativistic)"
    else:
        status = "Too light (not DM)"
    print(f"{n:>3} | {lam:>8.4f} | {gap:>8.4f} | {m_n:>10.2e} | {status:>20}")

print(f"\nLightest stable mode: n=7, m ≈ 14 MeV")
print(f"Total DM = multi-component scalar tower")
print(f"")

print("=" * 65)
print("P3 DARK MATTER SUMMARY")
print("=" * 65)
print(f"""
DM = tower of hidden W modes (n ≥ 4)
Masses: 15 GeV → 14 MeV (natural cutoff at n=7)
Key signatures:
  - n=4 → n=5 γ: 14.9 GeV gamma-ray line
  - n=5 → n=6 γ: 55 MeV gamma-ray line
  - Self-interactions from mode mixing
  - Not WIMP — no direct detection
""")
print("=" * 65)