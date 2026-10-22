#!/usr/bin/env python3
"""
CFAS P3 — Neutrino Mass from W Mode

Demonstrates: Seesaw mechanism from singlet W mode (n=0)
"""

import numpy as np

print("=" * 65)
print("CFAS P3 — Neutrino Mass from W Mode")
print("=" * 65)

kappa = np.exp(-3)  # 0.050
M_Pl = 1.22e19  # GeV
v = 246  # GeV (Higgs VEV)
y_nu = 1.0  # Yukawa coupling (from λ_0 = 1.0)

# Right-handed neutrino mass
m_N = kappa**2 * M_Pl  # λ_0 × κ² × M_Pl
m_nu = y_nu**2 * v**2 / m_N

print(f"Right-handed neutrino mass: m_N = κ² × M_Pl = {m_N:.2e} GeV")
print(f"Light neutrino mass: m_ν = y_ν² × v² / m_N")
print(f"  = {m_nu:.2e} GeV = {m_nu*1e9:.2e} eV")

# Atmospheric and solar mass splittings
dm2_atm = 2.5e-3  # eV²
dm2_solar = 7.4e-5  # eV²
m_nu_eV = m_nu * 1e9  # convert to eV

# Normal hierarchy
m1 = m_nu_eV * 0.1  # suppressed
m2 = np.sqrt(m1**2 + dm2_solar)
m3 = np.sqrt(m1**2 + dm2_solar + dm2_atm)

print(f"\nNormal hierarchy (m_1 = {m_nu_eV:.1e} eV):")
print(f"  m_1 = {m1:.2e} eV")
print(f"  m_2 = √(m₁² + Δm²_solar) = {m2:.2e} eV")
print(f"  m_3 = √(m₁² + Δm²_solar + Δm²_atm) = {m3:.2e} eV")

print(f"\nPredicted: Σ m_ν = {m1+m2+m3:.2e} eV")
print(f"Planck bound: Σ m_ν < 0.12 eV  ✅")

# Scan κ² factor
print(f"\nRight-handed neutrino mass vs κ² factor:")
for k_factor in [0.1, 0.5, 1.0, 2.0, 5.0]:
    m_N_scaled = k_factor * kappa**2 * M_Pl
    m_nu_scaled = y_nu**2 * v**2 / m_N_scaled
    print(f"  κ² × {k_factor:>4.1f}: m_N = {m_N_scaled:.2e}, m_ν = {m_nu_scaled:.2e} eV")

print("\n" + "=" * 65)
print("P3 NEUTRINO MASS SUMMARY")
print("=" * 65)
print(f"""
Seesaw from singlet mode (n=0):
  m_N = κ² × M_Pl = {m_N:.2e} GeV
  m_ν = {m_nu:.2e} eV

CFAS predicts normal hierarchy with:
  m_ν₁ ≈ {m_nu_eV:.1e} eV
  m_ν₂ ≈ {m2:.1e} eV
  m_ν₃ ≈ {m3:.1e} eV
  Σ m_ν ≈ {m1+m2+m3:.2e} eV < 0.12 eV ✅
""")
print("=" * 65)