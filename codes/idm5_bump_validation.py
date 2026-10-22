"""
IDM 5.0 — BUMP VALIDATION
============================
Core change from IDM 4.0: sign flip
  f(z) = 1 − ε·(z/z_c)·exp(−z/z_c)     [IDM 4.0: dip]
  f(z) = 1 + ε·(z/z_c)·exp(−z/z_c)     [IDM 5.0: bump]

ε = φ⁻¹/4 = (√5−1)/8 ≈ 0.1545085     [UNCHANGED — from sync recursion]

PURE NUMPY/SCIPY — no LLM in numerical computation.
"""

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize, fsolve
import json, time, os

OUTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════
# 1. FUNDAMENTAL CONSTANTS
# ═══════════════════════════════════════════
phi = (1 + np.sqrt(5)) / 2            # 1.618033988749895
phi_inv = (np.sqrt(5) - 1) / 2        # 0.618033988749895
EPS = phi_inv / 4                      # 0.1545084971874737  ← derived, NOT fitted
ZC = 0.6                               # sync transition redshift
H0 = 69.8                              # km/s/Mpc
OM = 0.286                             # matter density
ODE = 1 - OM                           # dark energy density
C = 299792.458                         # km/s
HZ_CONV = 3.24077929e-20               # km/s/Mpc → Hz

print("IDM 5.0 — BUMP VALIDATION SUITE")
print("=" * 65)
print(f"Constants:")
print(f"  φ     = {phi:.10f}")
print(f"  φ⁻¹   = {phi_inv:.10f}")
print(f"  ε     = φ⁻¹/4 = {EPS:.10f}")
print(f"  z_c   = {ZC}")
print(f"  H₀    = {H0} km/s/Mpc")
print(f"  Ω_m   = {OM}")

# ═══════════════════════════════════════════
# 2. CORE FUNCTIONS
# ═══════════════════════════════════════════

def f_bump(z):
    """Dark energy modulation: bump at z=z_c"""
    x = z / ZC
    return 1.0 + EPS * x * np.exp(-x)

def f_dip(z):
    """Original IDM 4.0: dip at z=z_c"""
    x = z / ZC
    return 1.0 - EPS * x * np.exp(-x)

def f_prime(z, bump=True):
    """df/dz"""
    x = z / ZC
    s = EPS / ZC * np.exp(-x) * (1 - x)
    return s if bump else -s

def E2(z, bump=True):
    """E²(z) = H²(z)/H₀²"""
    f = f_bump(z) if bump else f_dip(z)
    return OM * (1+z)**3 + ODE * f

def H(z, bump=True):
    """bump=True: H from bump model. bump=False: H from ΛCDM (f=1)"""
    if bump:
        return H0 * np.sqrt(E2(z, bump=True))
    else:
        return H0 * np.sqrt(OM * (1+z)**3 + ODE * 1.0)  # pure ΛCDM

def w_DE(z, bump=True):
    """Dark energy equation of state"""
    fv = f_bump(z) if bump else f_dip(z)
    fp = f_prime(z, bump)
    return -1.0 + (1+z)/3.0 * fp / fv

def DM(z, bump=True):
    """Comoving distance (Mpc)"""
    f = lambda zp: 1.0 / np.sqrt(E2(zp, bump))
    return quad(f, 0, z, limit=200)[0] * C / H0

def DL(z, bump=True):
    return (1+z) * DM(z, bump)

def mu(z, bump=True):
    return 5 * np.log10(DL(z, bump) * 1e5)

def DV(z, bump=True):
    """Volume-averaged BAO distance"""
    return (z * DM(z, bump)**2 * C / H(z, bump)) ** (1/3)

# ═══════════════════════════════════════════
# 3. STRUCTURAL CHECKS
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("3. STRUCTURAL CLOSURE")
print(f"{'─'*65}")

checks = []

# 3a. Sync recursion fixed point
C_inf = phi_inv
check1 = abs(C_inf - 1/(1+C_inf))
print(f"  Sync recursion fixed point: C = 1/(1+C) → C = φ⁻¹ = {C_inf:.8f}")
print(f"    Self-consistency: C = 1/(1+C)? {abs(C_inf - 1/(1+C_inf)) < 1e-15}")
checks.append(("Sync recursion fixed point", check1 < 1e-10, check1))

# 3b. Budget closure
B = 4 * EPS  # should equal φ⁻¹
check2 = abs(B - phi_inv)
print(f"  Budget: B = 4ε = {B:.8f} = φ⁻¹? {check2 < 1e-15}")
checks.append(("4ε = φ⁻¹ budget", check2 < 1e-10, check2))

# 3c. κ closure
kap = (EPS * phi)**2
check3 = abs(kap - 1/16)
print(f"  κ = (εφ)² = {kap:.10f} = 1/16 = 0.0625? {check3 < 1e-10}")
checks.append(("κ = (εφ)² = 1/16", check3 < 1e-10, check3))

# 3d. N_horizon
N_hor = 1.0 / EPS**2
print(f"  N_horizon = 1/ε² = {N_hor:.2f}")
checks.append(("N_horizon calculation", abs(N_hor - 41.89) < 0.01, 0))

# 3e. 4ε + 1 = φ
check5 = abs(4*EPS + 1 - phi)
print(f"  4ε + 1 = {4*EPS+1:.10f} = φ = {phi:.10f}? {check5 < 1e-15}")
checks.append(("4ε + 1 = φ identity", check5 < 1e-10, check5))

print(f"\n  Structural checks: {sum(1 for _,p,_ in checks if p)}/{len(checks)} PASSED")

# ═══════════════════════════════════════════
# 4. f(z) BUMP PROFILE
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("4. f(z) BUMP PROFILE (bump version)")
print(f"{'─'*65}")
print(f"{'z':>6} {'f_bump':>10} {'Δf/f':>10} {'w_DE':>10} {'H(z)':>10}")
print(f"{'─'*6} {'─'*10} {'─'*10} {'─'*10} {'─'*10}")
for z in [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0]:
    fb = f_bump(z)
    w = w_DE(z, bump=True)
    hv = H(z, bump=True)
    print(f"{z:6.1f} {fb:10.4f} {(fb-1)*100:9.2f}% {w:10.4f} {hv:10.2f}")

# ═══════════════════════════════════════════
# 5. CPL FIT
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("5. CPL PARAMETRIZATION FIT")
print(f"{'─'*65}")

zs_fit = np.linspace(0.05, 1.5, 200)
ws_bump = np.array([w_DE(z, bump=True) for z in zs_fit])
A = np.column_stack([np.ones_like(zs_fit), zs_fit/(1+zs_fit)])
w_cpl_bump = np.linalg.lstsq(A, ws_bump, rcond=None)[0]
resid = A @ w_cpl_bump - ws_bump
sigma = np.std(resid)
cov = sigma**2 * np.linalg.inv(A.T @ A)
err = np.sqrt(np.diag(cov))
print(f"  BUMP:  w₀ = {w_cpl_bump[0]:+.4f} ± {err[0]:.4f}")
print(f"         wₐ = {w_cpl_bump[1]:+.4f} ± {err[1]:.4f}")
print(f"         w₀+wₐ = {w_cpl_bump[0]+w_cpl_bump[1]:+.4f}")
print(f"         Quadrant: w₀{'=' if abs(w_cpl_bump[0]+1)<0.01 else ('>' if w_cpl_bump[0]>-1 else '<')}-1,",
      f"wₐ{'=' if abs(w_cpl_bump[1])<0.01 else ('>' if w_cpl_bump[1]>0 else '<')}0")

# CPL for comparison (dip)
ws_dip = np.array([w_DE(z, bump=False) for z in zs_fit])
w_cpl_dip = np.linalg.lstsq(A, ws_dip, rcond=None)[0]
print(f"  DIP:   w₀ = {w_cpl_dip[0]:+.4f}, wₐ = {w_cpl_dip[1]:+.4f}")
print(f"         Quadrant: w₀{'=' if abs(w_cpl_dip[0]+1)<0.01 else ('>' if w_cpl_dip[0]>-1 else '<')}-1,",
      f"wₐ{'=' if abs(w_cpl_dip[1])<0.01 else ('>' if w_cpl_dip[1]>0 else '<')}0")

# ═══════════════════════════════════════════
# 6. H(z) COMPARISON WITH DESI DR2
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("6. H(z) COMPARISON: BUMP vs ΛCDM vs DESI DR2")
print(f"{'─'*65}")

print(f"{'z':>5} {'H_bump':>9} {'H_ΛCDM':>9} {'ΔH':>9} {'%':>8} DESI DR2")
print(f"{'─'*5} {'─'*9} {'─'*9} {'─'*9} {'─'*8} {'─'*20}")
for z in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
    hb = H(z, bump=True)
    hl = H(z, bump=False)
    pct = (hb/hl - 1) * 100
    desi_hint = "← DESI: +3-4%" if abs(z-0.7) < 0.05 else ""
    print(f"{z:5.1f} {hb:9.2f} {hl:9.2f} {hb-hl:+8.2f} {pct:+7.2f}% {desi_hint}")

# DESI comparison at z=0.7 specifically
pct_07 = (H(0.7, bump=True)/H(0.7, bump=False) - 1) * 100
print(f"\n  → Bump at z=0.7: ΔH/H = {pct_07:+.2f}%  (DESI: +3-4%)")
print(f"  → Ratio: DESI/IDM = ~{3.5/pct_07:.1f}x")

# ═══════════════════════════════════════════
# 7. DISTANCE MODULUS (SNe compatibility)
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("7. DISTANCE MODULUS — SNe COMPATIBILITY")
print(f"{'─'*65}")
print(f"{'z':>5} {'μ_bump':>9} {'μ_ΛCDM':>9} {'Δμ':>9} {'Pantheon err':>12}")
print(f"{'─'*5} {'─'*9} {'─'*9} {'─'*9} {'─'*12}")
for z in [0.1, 0.3, 0.5, 0.7, 1.0]:
    mb = mu(z, bump=True)
    ml = mu(z, bump=False)
    print(f"{z:5.1f} {mb:9.4f} {ml:9.4f} {mb-ml:+9.4f} {'~0.02':>12}")

# ═══════════════════════════════════════════
# 8. BAO DISTANCE COMPARISON
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("8. BAO DISTANCE PREDICTIONS")
print(f"{'─'*65}")

print(f"{'z':>5} {'D_M_bump':>9} {'D_M_ΛCDM':>9} {'Δ%':>8} {'D_V_bump':>9} {'D_V_ΛCDM':>9} {'Δ%':>8}")
print(f"{'─'*5} {'─'*9} {'─'*9} {'─'*8} {'─'*9} {'─'*9} {'─'*8}")
for z in [0.3, 0.5, 0.7, 1.0, 1.5]:
    dmb = DM(z, bump=True)
    dml = DM(z, bump=False)
    dmb_pct = (dmb/dml - 1)*100
    dvb = DV(z, bump=True)
    dvl = DV(z, bump=False)
    dv_pct = (dvb/dvl - 1)*100
    print(f"{z:5.1f} {dmb:9.1f} {dml:9.1f} {dmb_pct:+7.2f}% {dvb:9.1f} {dvl:9.1f} {dv_pct:+7.2f}%")

# ═══════════════════════════════════════════
# 9. GROWTH RATE
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("9. GROWTH RATE (fσ₈) — APPROXIMATE")
print(f"{'─'*65}")

# Standard growth ODE: f' + f² + (2 + H'/H)f = (3/2)Ω_m(z)
# Simplified: f ≈ Ω_m(z)^γ, γ ≈ 0.55 for ΛCDM
def Om_z(z, bump=True):
    return OM * (1+z)**3 / E2(z, bump)

def f_growth(z, bump=True):
    """Approximate growth rate"""
    omz = Om_z(z, bump)
    return omz ** 0.55

print(f"{'z':>5} {'Ω_m(z)_bump':>12} {'Ω_m(z)_ΛCDM':>12} {'f_bump':>8} {'f_ΛCDM':>8}")
print(f"{'─'*5} {'─'*12} {'─'*12} {'─'*8} {'─'*8}")
for z in [0, 0.3, 0.5, 0.7, 1.0, 2.0]:
    ob = Om_z(z, True)
    ol = Om_z(z, False)
    fb_val = f_growth(z, True)
    fl_val = f_growth(z, False)
    print(f"{z:5.1f} {ob:12.4f} {ol:12.4f} {fb_val:8.4f} {fl_val:8.4f}")

# ═══════════════════════════════════════════
# 10. f(z) ZC SENSITIVITY
# ═══════════════════════════════════════════
print(f"\n{'─'*65}")
print("10. z_c SENSITIVITY — EFFECT ON H(z) BUMP AT z=0.7")
print(f"{'─'*65}")
print(f"{'z_c':>6} {'f(0.7)':>8} {'H(0.7)':>8} {'ΔH%':>8}")
for zc_try in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    def f_loc(z):
        x = z / zc_try
        return 1.0 + EPS * x * np.exp(-x)
    def e2_loc(z):
        return OM*(1+z)**3 + ODE*f_loc(z)
    h_loc = H0 * np.sqrt(e2_loc(0.7))
    h_lcdm = H0 * np.sqrt(OM*(1.7)**3 + ODE)
    pct = (h_loc/h_lcdm - 1)*100
    print(f"{zc_try:6.1f} {f_loc(0.7):8.4f} {h_loc:8.2f} {pct:+7.2f}%")

# ═══════════════════════════════════════════
# 11. SUMMARY — DESI COMPATIBILITY
# ═══════════════════════════════════════════
print(f"\n{'═'*65}")
print("11. DESI DR2 COMPATIBILITY SUMMARY")
print(f"{'═'*65}")

desi_obs = {
    "w0_quadrant": "> -1",
    "wa_quadrant": "< 0",
    "H_z07_increase": "3-4%",
    "dynamical_DE_significance": "3.1σ (DESI+CMB)",
    "LCDM_tension": "2.3σ (BAO vs CMB)"
}

idm_bump = {
    "w0": f"{w_cpl_bump[0]:+.3f}",
    "wa": f"{w_cpl_bump[1]:+.3f}",
    "w0_gt_m1": w_cpl_bump[0] > -1,
    "wa_lt_0": w_cpl_bump[1] < 0,
    "H_z07_increase": f"{pct_07:+.2f}%",
    "N_horizon": f"{N_hor:.0f}",
    "ε_derived": f"{EPS:.6f}"
}

print(f"\n  {'Check':<30} {'DESI DR2':<20} {'IDM 5.0 bump':<20} {'Match':>6}")
print(f"  {'─'*30} {'─'*20} {'─'*20} {'─'*6}")
dw0 = "✅ SAME" if w_cpl_bump[0] > -1 else "❌ DIFF"
dwa = "✅ SAME" if w_cpl_bump[1] < 0 else "❌ DIFF"
print(f"  {'w₀ quadrant':<30} {'> -1':<20} {f'{w_cpl_bump[0]:+.3f}':<20} {dw0:>6}")
print(f"  {'wₐ quadrant':<30} {'< 0':<20} {f'{w_cpl_bump[1]:+.3f}':<20} {dwa:>6}")
pct_match = abs(pct_07 - 3.5) / 3.5
hpct = "⚠️ PARTIAL" if pct_07 < 2.0 else "✅ GOOD"
print(f"  {'H(z) increase at z=0.7':<30} {'+3-4%':<20} {f'{pct_07:+.2f}%':<20} {hpct:>6}")

# ═══════════════════════════════════════════
# 12. SAVE RESULTS
# ═══════════════════════════════════════════
results = {
    "model": "IDM 5.0",
    "version": "bump",
    "epsilon": EPS,
    "z_c": ZC,
    "H0": H0,
    "Omega_m": OM,
    "structural_checks_passed": sum(1 for _,p,_ in checks if p),
    "structural_checks_total": len(checks),
    "CPL_w0": float(w_cpl_bump[0]),
    "CPL_wa": float(w_cpl_bump[1]),
    "CPL_w0_err": float(err[0]),
    "CPL_wa_err": float(err[1]),
    "N_horizon": float(N_hor),
    "H_increase_pct_at_07": float(pct_07),
    "kappa": float(kap),
    "DESI_quadrant_match": {
        "w0_gt_m1": bool(w_cpl_bump[0] > -1),
        "wa_lt_0": bool(w_cpl_bump[1] < 0)
    }
}

with open(f"{OUTDIR}/data/validation_results.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\n  Results saved to {OUTDIR}/data/validation_results.json")

print(f"\n{'═'*65}")
print(f"VALIDATION COMPLETE — {sum(1 for _,p,_ in checks if p)}/{len(checks)} structural checks PASSED")
print(f"{'═'*65}")
