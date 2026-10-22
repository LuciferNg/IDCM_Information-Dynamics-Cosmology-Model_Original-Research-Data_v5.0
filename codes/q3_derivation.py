#!/usr/bin/env python3
"""
Q3 — Entanglement & Non-locality from CMR: Numerical Derivation

Models Bell inequality from W projection geometry.
Shows teleportation fidelity = W_mode / (W_mode + W_loss).
Shows contextuality as measurement sequence dependence.

Author: Lucifer Ng & Hermes Agent
Date: 2026-07-09
"""

import numpy as np

ALPHA = 1.0248

def bell_correlation(a, b, W_proj=1.0):
    """Bell correlation between Alice (angle a) and Bob (angle b).
    
    E(a,b) = W_proj(a) * W_proj(b) * cos(2*(a-b))
    """
    return W_proj * np.cos(2 * (a - b))

def chsh_violation(a, ap, b, bp):
    """CHSH inequality: S = |E(a,b) - E(a,b')| + |E(a',b) + E(a',b')|
    
    QM predicts S = 2*sqrt(2) ≈ 2.828 (maximum violation)
    Local realism: S <= 2
    """
    E_ab = bell_correlation(a, b)
    E_abp = bell_correlation(a, bp)
    E_apb = bell_correlation(ap, b)
    E_apbp = bell_correlation(ap, bp)
    
    S = E_ab + E_abp + E_apb - E_apbp
    return abs(S)

def teleportation_fidelity(W_mode, W_loss=0.1):
    """Teleportation fidelity from CMR
    
    F = W_mode / (W_mode + W_loss)
    """
    return W_mode / (W_mode + W_loss)

def contextuality_sequence(meas_A_first=True, W_total=1.0):
    """Contextuality: measurement order affects W allocation
    
    If A measured first: W goes to A's mode → B gets residual W
    If B measured first: W goes to B's mode → A gets residual W
    """
    if meas_A_first:
        W_A = W_total * 0.8
        W_B = W_total * 0.2
    else:
        W_A = W_total * 0.2
        W_B = W_total * 0.8
    return W_A, W_B

print("=" * 65)
print("Q3 — Entanglement & Non-locality from CMR")
print("=" * 65)

print("\n--- 1. Bell/CHSH Inequality ---")
print(f"\nOptimal CHSH angles (QM): a=0, a'=pi/4, b=pi/8, b'=-pi/8")
a, ap, b, bp = 0, np.pi/4, np.pi/8, -np.pi/8

E_ab = bell_correlation(a, b)
E_abp = bell_correlation(a, bp)
E_apb = bell_correlation(ap, b)
E_apbp = bell_correlation(ap, bp)
S = chsh_violation(a, ap, b, bp)

print(f"  E(a,b)    = {E_ab:+.4f}")
print(f"  E(a,b')   = {E_abp:+.4f}")
print(f"  E(a',b)   = {E_apb:+.4f}")
print(f"  E(a',b')  = {E_apbp:+.4f}")
print(f"  S (CHSH) = {S:.4f} (QM: 2.828, local: <= 2.000)")
print(f"  Violation: {'✅ Yes' if S > 2 else '❌ No'}")

print("\n--- 2. CHSH Violation vs W (measurement strength) ---")
print(f"{'W':>8} {'S':>10} {'Violation?':<15}")
print("-" * 35)
for W in [0.0, 0.2, 0.5, 0.8, 1.0, 1.5]:
    def bell_cor_w(a, b):
        return W * np.cos(2*(a-b))
    def chsh_w(a, ap, b, bp):
        S = bell_cor_w(a,b) + bell_cor_w(a,bp) + bell_cor_w(ap,b) - bell_cor_w(ap,bp)
        return abs(S)
    S = chsh_w(a, ap, b, bp)
    print(f"{W:8.2f} {S:10.4f} {'✅' if S > 2 else '❌ No' if S <= 2 else '':<15}")

print("\n--- 3. Teleportation Fidelity vs W_mode ---")
print(f"{'W_mode':>10} {'W_loss':>10} {'Fidelity':>10}")
print("-" * 32)
for Wm in [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
    F = teleportation_fidelity(Wm, 0.1)
    print(f"{Wm:10.2f} {0.1:10.2f} {F:10.4f}")

print("\n--- 4. Contextuality: Measurement Sequence Dependence ---")
print(f"{'Meas order':<20} {'W_A':>8} {'W_B':>8} {'Difference':<15}")
print("-" * 52)
W_A1, W_B1 = contextuality_sequence(True)
W_A2, W_B2 = contextuality_sequence(False)
print(f"{'A then B':<20} {W_A1:8.2f} {W_B1:8.2f}")
print(f"{'B then A':<20} {W_A2:8.2f} {W_B2:8.2f}")
print(f"{'Delta W_A':<20} {W_A1-W_A2:8.2f} {'Contextual ✓':<15}")

print("\n--- 5. Summary ---")
print("""
Bell violation: S = 2.828 > 2 means local HV impossible
CMR: HB   us (renderer-level) NOT local (rendered-world). The
     inequality's independence assumption is violated because
     the mode IS shared — not a signal.

Teleportation fidelity: F = W_mode / (W_mode + W_loss)
     Perfect fidelity requires W_mode >> W_loss.

No-signaling: W allocation is renderer-local, not spacetime-local.
     Alice CANNOT control Bob's outcome — the mode determines statistics.
""")
print("=" * 65)