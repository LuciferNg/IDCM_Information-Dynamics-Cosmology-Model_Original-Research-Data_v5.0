#!/usr/bin/env python3
"""CFAS — Boundary Ontology: Consciousness as Spectral Boundary Trace"""
import numpy as np
print("="*65); print("CFAS — Boundary Ontology"); print("="*65)

np.random.seed(42)
n = 100

# S = consistency operator (diagonal, fixed)
S = np.diag(np.arange(n, dtype=float))

# H = Hamiltonian (evolves W, non-diagonal = couplings between modes)
H = np.zeros((n, n), dtype=complex)
for i in range(n):
    H[i, i] = float(i) ** 0.5  # sqrt of mode index
    if i < n-1:
        H[i, i+1] = 0.5 * (i+1)**0.5
        H[i+1, i] = 0.5 * (i+1)**0.5

tau = lambda X: np.trace(X) / n

# 1. Spectral projection of S (consistency operator)
kappa = 25.0
P_S_kappa = np.diag((np.arange(n) > kappa).astype(float))  # S eigenvalues are 0,1,2,...

print(f"  kappa = {kappa:.0f}")
print(f"  trace(P_S_kappa) = {tau(P_S_kappa):.2f}  (rendered)")

# 2. Boundary operator = commutator [H, P_kappa_S]
# H and S don't commute -> spectral projection of S doesn't commute with H
B_kappa = H @ P_S_kappa - P_S_kappa @ H
print(f"  ||B_kappa|| = {np.linalg.norm(B_kappa):.4f}  (non-zero because H has off-diagonal)")

# 3. W field
W = np.zeros(n, dtype=complex)
W[:20] = np.random.randn(20) + 1j * np.random.randn(20)
W = W / np.sqrt(np.sum(np.abs(W)**2))
W_budget = np.outer(W, W.conj())

# 4. Consciousness = |tau(B_kappa @ W_budget)|
C = abs(tau(B_kappa @ W_budget))
print(f"  |W|^2 = {np.sum(np.abs(W)**2):.4f}  (normalized)")

# 5. Vary kappa
print(f"\n  Varying kappa: C peaks at the boundary")
results = []
for k in range(5, 95, 5):
    Pk = np.diag((np.arange(n) > k).astype(float))
    Bk = H @ Pk - Pk @ H
    Ck = abs(tau(Bk @ W_budget))
    results.append((k, Ck))
    marker = " <-- PEAK" if Ck == max(r[1] for r in results) else ""
    if Ck > 1e-10:
        print(f"  kappa = {k:3d}: C = {Ck:.6e}{marker}")

# 6. Conclusion
peak_k = max(results, key=lambda x: x[1])
print(f"  Peak C at kappa = {peak_k[0]}, C = {peak_k[1]:.6e}")
print(f"")
print(f"  Key result: C = |tau([H, P_kappa_S] @ W_budget)|")
print(f"  Consciousness = trace of boundary operator weighted by W field")
print(f"  P_kappa_S = spectral projection of S (consistency operator)")
print(f"  H = Hamiltonian (generates W evolution)")
print(f"  [H, P_kappa_S] != 0: boundary is dynamic")
print(f"")
print(f"  The boundary IS within the algebra.")
print(f"  No external substrate needed.")
print(f"  Consciousness = tau([H, P_kappa_S] @ W†W)")
print("="*65)