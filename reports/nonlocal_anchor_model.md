# 非局部 Anchor 校準模型 — 形式推導

## 1. 同步相位場

遞迴 C_{n+1}=1/(1+C_n) 嘅收斂喺時空中有特徵相關尺度。
喺空間點 r 嘅同步完成度由因果域數量決定：

$$s(r) = 1 - e^{-r/\xi}$$

其中 $\xi = R_h/N_{\text{horizon}} = 4395/42 \approx 105$ Mpc。

W-field 振幅偏差：

$$\frac{\delta|W|^2(r)}{|W|^2} = \varepsilon \cdot e^{-r/\xi}$$

## 2. Anchor 校準積分

每個距離階梯方法嘅零點 $b_0$ 由一組 anchor 加權平均決定：

$$b_0 = \frac{\sum_i w_i \cdot b_0^{(i)}}{\sum_i w_i}$$

其中 $b_0^{(i)}$ 係第 $i$ 個 anchor 嘅零點校準，
$w_i$ 係 anchor 嘅統計權重（$\propto 1/\sigma_i^2$）。

每個 anchor 嘅零點偏差：

$$\Delta b_0^{(i)} = \varepsilon \cdot f(r_i) \cdot \frac{\delta|W|^2(r_i)}{|W|^2}$$

其中 $f(r_i)$ 係 anchor 尺度嘅非局部 kernel。

## 3. 從 H₀ 觀測反推

觀察到嘅 H₀ 同 global H₀ 嘅關係：

$$H_0^{\text{obs}} = H_0^{\text{global}} \times (1 + \varepsilon \cdot A_{\text{method}})$$

其中 $A_{\text{method}}$ 係方法嘅有效同步振幅。

從觀測反推 $A_{\text{method}}$：

| 方法 | $H_0^{\text{obs}}$ | $H_0^{\text{obs}}/H_0^{\text{IDM}} - 1$ | $A_{\text{method}}$ |
|:-----|:------------------:|:----------------------------------------:|:-------------------:|
| Cepheid (SH0ES) | 73.04 ± 1.04 | 0.0710 | **0.460** |
| TRGB (Freedman) | 69.8 ± 1.9 | 0.0235 | **0.152** |
| TRGB (Anand) | 71.5 ± 1.8 | 0.0484 | **0.313** |
| Mira (Huang) | 73.3 ± 4.0 | 0.0748 | **0.484** |
| Planck | 67.36 ± 0.54 | −0.0123 | **−0.080** |
| H₀LiCOW | 73.3 ± 1.8 | 0.0748 | **0.484** |

## 4. 核函數擬合

假設 $A(r) = \varepsilon \cdot (r/\xi)^\alpha$（冪律核）：

$$A_{\text{method}} = \sum_i w_i \varepsilon \cdot (r_i/\xi)^\alpha$$

從 Cepheid 同 TRGB 嘅 ratio 解 $\alpha$：

$$\frac{A_{\text{ceph}}}{A_{\text{TRGB}}} = \frac{0.460}{0.152} = 3.03$$

Cepheid anchor 權重組合：$r_{\text{eff}}^{\text{ceph}} \approx 2.5$ Mpc
TRGB anchor 權重組合：$r_{\text{eff}}^{\text{TRGB}} \approx 0.05$ Mpc

$$\frac{(2.5/105)^\alpha}{(0.05/105)^\alpha} = 3.03 \quad\Rightarrow\quad \left(\frac{2.5}{0.05}\right)^\alpha = 3.03$$

$$50^\alpha = 3.03 \quad\Rightarrow\quad \alpha = \frac{\ln 3.03}{\ln 50} = \frac{1.108}{3.912} = 0.283$$

$$\boxed{\alpha \approx 0.28}$$

## 5. 驗證預測

用 $\alpha = 0.28$ 同各 anchor 尺度的有效權重，預測其他方法：

| 方法 | 有效 anchor 尺度 | $A_{\text{pred}}$ | $H_0^{\text{pred}}$ | 觀測 | 偏差 |
|:-----|:---------------:|:-----------------:|:-------------------:|:----:|:----:|
| Cepheid | ~2.5 Mpc | 0.460 (fit) | 73.04 (fit) | 73.04 | — |
| TRGB (Freedman) | ~0.05 Mpc | 0.152 (fit) | 69.8 (fit) | 69.8 | — |
| Mira | ~0.05 Mpc | 0.152 | 69.8 | 73.3 ± 4.0 | ❌ |
| JWST Cepheid | ~2.5 Mpc | 0.460 | 73.04 | 72.6 ± 2.0 | ✅ |
| Planck | ∞ (global) | 0 | 68.2 | 67.36 ± 0.54 | 🟡 |
| H₀LiCOW | ∞ (lensing) | 0 | 68.2 | 73.3 ± 1.8 | ❌ |

## 6. 矛盾

- **Miras** 預測 69.8 但觀測 73.3——同 Cepheid 一致而非 TRGB
  → 可能係 Miras 共享 LMC anchor 同 Cepheid 嘅校準
  
- **H₀LiCOW** 預測 68.2 但觀測 73.3
  → 強透鏡模型有系統自由度（lens mass profile, LOS）

- **Planck** 預測 68.2 但觀測 67.36
  → 1.6σ 偏差，可能係統計漲落

## 7. 結論

冪律核 $A(r) \propto r^{0.28}$ 可以同時 fit Cepheid 同 TRGB，
但 Miras 同 H₀LiCOW 偏離預測。

**剩餘問題：**
1. 冪律核 $\alpha = 0.28$ 嘅物理起源？
2. Miras 同 Cepheid 共享 anchor 嘅程度？
3. 模型需要更多 anchor 獨立校準嘅數據

**可以繼續嘅方向：**
1. 從 $\varepsilon$ 同域結構推導 $\alpha$
2. 分析每個 anchor 嘅獨立權重 $w_i$
3. 引入 JWST 數據改善 anchor 校準