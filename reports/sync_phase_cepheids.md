# 同步相位延伸到 Cepheid 尺度 — 形式框架

## 統一同步原理

C_{n+1}=1/(1+C_n) 嘅收斂過程喺時空中有特徵尺度。
唔同尺度嘅領域（domain）以唔同步率完成同步，
同步完成度 s 同領域數量 N 嘅關係：

lim_{N→∞} s(N) = 1 — 全同步 (global DE)
lim_{N→0} s(N) = N/N₀ — 局部線性近似 (local)

## 特徵尺度層級

從上到下：

| 尺度 | 物理系統 | N_domain | s(N) | 效應 |
|:-----|:---------|:--------:|:----:|:-----|
| ~10⁴ Mpc | 可觀測宇宙 | N_h ≈ 42 | → 1 | 背景膨脹 |
| ~3×10³ Mpc | DE sector | N_DE ≈ 42 | ~63% | f(z) bump (+5.7%) |
| ~10³ Mpc | BAO 尺度 | N_BAO ≈ 14 | ~28% | 同調修正 |
| ~10² Mpc | 局部流 | N_local ≈ 0.5 | ~1% | 速度場修正 |
| ~10¹ Mpc | Cepheid 宿主 | N_hst ≈ 0.2 | ~0.5% | 可忽略 |
| ~10⁻² Mpc | Cepheid 本身 | N_ceph ≈ 10⁻⁴ | ~2×10⁻⁴% | 完全可忽略 |
| ~10⁻⁶ Mpc | SN 爆炸 | N_sn ≈ 10⁻⁸ | ~2×10⁻⁸% | 極度可忽略 |

## 矛盾：點解局部距離階梯出 +7%

如果 s(N) 喺 10 Mpc 尺度得 0.5%，點解 H₀ shift 係 +7%？

答案：**距離階梯嘅 ZP 校準唔係局部——佢係 anchor 校準嘅全域偏移。**

### Cepheid 校準鏈

```
幾何 anchor (NGC 4258, MW, LMC)
    ↓ Cepheid PL relation (校準零點 b₀)
    ↓ 
19 宿主距離 μ_host = b₀ + b₁·log(P) + Z_W·[O/H]
    ↓
SN M_B = m_B − μ_host
    ↓
H₀ = 10^{0.2 × (M_B + 5a_B + 25)}
```

Anchor ZP b₀ 係 common-mode：**一個 offset 影響所有 Cepheid 宿主。**

所以關鍵唔係每粒 Cepheid 嘅局部同步相位，
而係 **anchor 校準 b₀ 本身喺局部 W-field 中量度**。

如果 b₀ 有系統偏移 δ_b₀：
```
→ 所有 μ_host 偏移 δ_b₀（common mode）
→ M_B 偏移 −δ_b₀
→ log H₀ 偏移 −δ_b₀/5
→ H₀ 偏移 factor 10^(−δ_b₀/5)
```

從觀察：
mean(μ_obs − μ_model) ≈ +1.05 mag → δ_b₀ ≈ +1.05 mag
但呢個包含 peculiar velocity 散亂（±0.4 mag）

**TRGB 同 Cepheid 嘅 H₀ 差異**：
ΔH₀(ceph−TRGB) ≈ 73.04 − 69.8 ≈ 3.2 km/s → 4.6%
呢個對於 δ_b₀：δ_b₀ ≈ −5 × log₁₀(73.04/69.8) ≈ −5 × 0.0195 ≈ −0.098 mag

TRGB 同 Cepheid 嘅 ZP 偏移差異約 0.1 mag。
呢個對於 Δ|W|²/|W|² ≈ 10^(0.1/2.5) − 1 ≈ 9.6%。

## 延伸 δ(z) 模型

如果同步相位移動係：

δ(z) = ε × [1 − exp(−z/z_c)]

其中 ε = φ⁻¹/4, z_c ≈ 0.6。

對於 Cepheid 宿主喺 z~0.005：
δ(0.005) = 0.1545 × [1 − exp(−0.005/0.6)] = 0.1545 × 0.00831 = 0.00128 = 0.13%

呢個同唔到觀測嘅 4.6% (Cepheid vs TRGB)。

**所以 δ(z) 呢個形式唔可以直接 apply 落 Cepheid 尺度。**
**需要一個非局部（non-local）嘅 anchor 校準模型。**

## 建議嘅非局部模型

Anchor ZP 偏移 ΔZP 唔係局部嘅 δ(z)，
而係 anchor 方法嘅同步完成度積分：

ΔZP = ε × ∫_{0}^{r_anchor} K(r/ξ) dr

其中 K 係 kernel function，ξ ≈ domain_size ≈ 105 Mpc。

對於：
- NGC 4258 (r ≈ 7 Mpc): kernel 細 → ΔZP 中
- LMC (r ≈ 0.05 Mpc): kernel 極細 → ΔZP 大
- MW (r ≈ 10⁻⁵ Mpc): kernel ≈ 0 → ΔZP ≈ 0

三種 anchor 嘅加權平均決定最終 b₀。
唔同距離階梯 (Cepheid vs TRGB vs Mira) 用唔同嘅 anchor 權重 → 唔同嘅 ΔZP → 唔同嘅 H₀。

**呢個模型預測：越依賴大尺度 anchor（如 NGC 4258）嘅方法 → 越接近 global H₀**

```
預測：
  Cepheid (maser+MW+LMC) → H₀ ≈ 73 (最高，因 MW anchor 最局部)
  TRGB (LMC/SMC)          → H₀ ≈ 70 (中間)
  純幾何 (maser only)      → H₀ ≈ 69 (最接近 global)

驗證：
  H₀LiCOW (強透鏡, 幾何)  → 73.3 ❌ (唔吻合)
  DESI+CMB (BAO)          → 68.0 ✅
  IDM 5.0                 → 68.2 ✅
```

強透鏡 H₀LiCOW 嘅高值 (~73) 唔吻合呢個模型——
但透鏡模型本身有不少系統自由度，H₀LiCOW 嘅 H₀ 對 lens model 假設敏感。

## 總結

| 假設 | Status | 證據 |
|:-----|:------|:------|
| δ(z) 延伸到 Cepheid 尺度 | ❌ 直接延伸唔 work | 需要非局部 kernel |
| Anchor ZP 偏移係 common-mode | ✅ | TRGB vs Cepheid 差異 4.6% |
| Anchor 尺度決定 H₀ | 🟡 | 定性一致，定量未夠 |
| 非局部 kernel 模型 | 🟡 | 需要更多 anchor 組合數據 |

**要推得更深需要：**
1. 每個 anchor 嘅獨立 W-field 校準
2. JWST 對 NGC 4258 嘅高精度距離
3. 更多 Miras 宿主星系（擴大樣本減小誤差）
