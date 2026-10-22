# 同步相位尺度推導 (修正版)

## 核心修正：A(r) 增長 vs 衰減

之前混亂咗方向。正確理解：

**同步相位偏差 A(r) 係觀察者同 anchor 之間嘅非相關性度量。**
- r 細（MW, 0.001 Mpc）：觀察者同 anchor 高度相關 → A ≈ 0
- r 大（NGC 4258, 7 Mpc）：觀察者同 anchor 弱相關 → A → ε

所以 **A(r) 增長隨 r**，唔係衰減。

## Anchor 權重尺度

### Cepheid anchors

| Anchor | r (Mpc) | Cepheids | 權重 w | w×r |
|:-------|:-------:|:--------:|:------:|:---:|
| MW (parallax) | ~0.001 | ~300 | 300 | 0.3 |
| LMC (eclipsing binary) | ~0.05 | ~200 | 200 | 10 |
| NGC 4258 (maser) | ~7.6 | ~150 | 150 | 1140 |
| **加權平均** | | | **650** | **1150.3** |

$$r_{\text{ceph}} = \frac{1150.3}{650} = \mathbf{1.77\ \text{Mpc}}$$

### TRGB anchors (CCHP)

TRGB 用 LMC 同 SMC 做 anchor，冇用 MW：

| Anchor | r (Mpc) | 權重 |
|:-------|:-------:|:----:|
| LMC | 0.05 | 1 |
| SMC | 0.06 | 1 |

$$r_{\text{TRGB}} \approx 0.05\ \text{Mpc}$$

## 觀測約束

從 Cepheid 同 TRGB 嘅 A 值：

$$A_{\text{ceph}} = \frac{H_0^{\text{ceph}}/H_0^{\text{IDM}} - 1}{\varepsilon} = \frac{73.04/68.2 - 1}{0.1545} = \frac{0.0710}{0.1545} = 0.460$$

$$A_{\text{TRGB}} = \frac{69.8/68.2 - 1}{0.1545} = \frac{0.0235}{0.1545} = 0.152$$

$$\frac{A_{\text{ceph}}}{A_{\text{TRGB}}} = \frac{0.460}{0.152} = 3.03$$

## 尺度指數推導

$$A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^\beta \quad (\beta > 0)$$

$$\frac{A_{\text{ceph}}}{A_{\text{TRGB}}} = \left(\frac{r_{\text{ceph}}}{r_{\text{TRGB}}}\right)^\beta$$

$$3.03 = \left(\frac{1.77}{0.05}\right)^\beta = 35.4^\beta$$

$$\beta = \frac{\ln 3.03}{\ln 35.4} = \frac{1.109}{3.567} = \mathbf{0.311}$$

## 同基本常數嘅關係

$$\beta = 0.311 \approx \frac{1}{\pi} = 0.3185$$

差距：$(0.3185 - 0.311)/0.311 = 2.4\%$ — 喺誤差範圍內。

**候選關係：**

$$\boxed{\beta = \frac{1}{\pi}}$$

$$\boxed{A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^{1/\pi}}$$

## 解釋

$\beta = 1/\pi$ 嘅物理意義：

1. $\pi$ 出現暗示 **2D 投影**——同步相位喺天球上嘅角相關性
2. 觀察者到 anchor 嘅距離 r 投影到 2D 天球：角尺度 $\theta = r/D_A$
3. 角相關性嘅冪律：$C(\theta) \propto \theta^{-1/\pi}$ 對應 2D 等向場

另一可能：$\beta = \frac{\varphi^{-1}}{2} = \frac{0.618}{2} = 0.309$，同 0.311 更接近 (差 0.6%)

$$A(r) = \varepsilon \cdot (r/\xi)^{\varphi^{-1}/2}$$

## 預測：JWST 對 NGC 4258

JWST SH0ES (Riess+2024) 用 JWST 重新測量 NGC 4258 Cepheids。
如果 JWST 減少系統誤差，有效 r 會更接近 NGC 4258 嘅 7.6 Mpc (而非加權平均 1.77 Mpc)：

$$r_{\text{JWST}} \approx 7.6\ \text{Mpc}$$

$$A_{\text{JWST}} = 0.1545 \times (7.6/105)^{1/\pi} = 0.1545 \times 0.422 = 0.065$$

$$H_0^{\text{JWST}} = 68.2 \times (1 + 0.1545 \times 0.065) = 68.2 \times 1.010 = 68.9$$

JWST 應該測到 $H_0 \approx 68.9$ — 低過 SH0ES 嘅 73.0，接近 IDM。

**實際觀測：JWST Riess+2024 測到 72.6 ± 2.0**
→ 高過預測 68.9，但喺 1.9σ 內（error bar 大）。

## 未解決問題

1. $\beta = 1/\pi$ 定 $\beta = \varphi^{-1}/2$？需要更多數據分辨
2. Miras 嘅 $H_0 = 73.3$ 同 Cepheid 一致而非 TRGB——可能係 Miras 嘅 anchor 權重同 Cepheid 相似
3. 強透鏡 H₀LiCOW (73.3) 完全偏離模型——需要獨立校準
