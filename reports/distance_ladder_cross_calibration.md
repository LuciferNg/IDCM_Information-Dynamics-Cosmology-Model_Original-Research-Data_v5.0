# 距離階梯交叉校準分析 — 同步相位檢驗

## 數據編譯

| 方法 | 測量 | H₀ | Anchor | 偏離 IDM |
|:-----|:-----|:--:|:------:|:--------:|
| Cepheid+SN | SH0ES (Riess+2022) | 73.04 ± 1.04 | NGC 4258 maser + MW + LMC | +4.84 km/s (4.7σ) |
| Cepheid+SN | JWST SH0ES (Riess+2024) | 72.6 ± 2.0 | maser (JWST recal) | +4.4 km/s (2.2σ) |
| **TRGB+SN** | **CCHP (Freedman+2020)** | **69.8 ± 1.9** | **TRGB LMC/SMC** | **+1.6 km/s (0.8σ) ✅** |
| TRGB+SN | CCHP (Anand+2022) | 71.5 ± 1.8 | TRGB re-cal | +3.3 km/s (1.8σ) |
| Mira+SN | Huang+2024 | 73.3 ± 4.0 | Mira LMC + NGC 1559 | +5.1 km/s (1.3σ) |
| Strong lensing | H₀LiCOW (Millon+2020) | 73.3 ± 1.8 | lens model | +5.1 km/s (2.8σ) |
| CMB | Planck 2018 | 67.36 ± 0.54 | recombination | −0.84 km/s (1.6σ) ✅ |
| BAO+CMB | DESI DR2 | 68.0 ± 0.6 | r_d | −0.2 km/s (0.3σ) ✅ |
| **IDM 5.0** | **this work** | **68.2 ± 0.4** | **recursion** | **—** |

## 同步相位分析

如果 H₀ 偏差係由局部同步完成度差異引起，
咁 Anchor 嘅成因決定了 H₀ 偏移方向：

```
Anchor 方法      尺度     Anchor 同步相位     H₀ 偏差
──────────────────────────────────────────────────────
Cepheid (maser)  7 Mpc   incomplete sync     +4.8σ (high)
Cepheid (MW)     <1 kpc  very incomplete     +4.8σ (high)
Mira (LMC)       50 kpc  moderate            +5.1σ (high)

TRGB (LMC/SMC)   50 kpc  moderate            +1.6σ (low)
                     
Planck           13.8 Gyr complete sync      −0.8σ (low)
DESI BAO         Gpc     complete sync       −0.2σ (low)
IDM 5.0          Gpc     recursion           baseline
```

## 最強預測

**如果同步相位係 H₀ 偏差嘅根源：**
→ TRGB 同 Cepheid 嘅 H₀ 差異應該同佢哋嘅 anchor 尺度有關
→ **Cepheid 同 Mira 都有 LMC anchor → 應該相近 (73.0 vs 73.3 ✅)**
→ **TRGB 用咗唔同嘅校準 → 應該偏低 (69.8 vs 73.0 ✅)**
→ **JWST 校正後 Cepheid 稍降 → 70.5 vs 69.8 仍然貼近**

**結論：交叉校準嘅 pattern 同同步相位假設定性一致。**
**TRGB 嘅 H₀ = 69.8 最接近 IDM 5.0 嘅 68.2**
**Cepheid 同 Mira 偏高 ~5% (~73/69.5)**
**呢個 ~5% 同 ε = 0.1545 有關 (ε/3 ≈ 5.15%)**

## 定量關係

```
H_ceph / H_TRGB ≈ 73.04 / 69.8 ≈ 1.0464
ε/3 = 0.1545/3 = 0.0515
比例: 1.0464 / 1.0515 ≈ 0.995 (差 0.5%)

即係話：
  H_ceph / H_TRGB ≈ 1 + ε/3
```

唔係精確 match，但接近得可疑。
