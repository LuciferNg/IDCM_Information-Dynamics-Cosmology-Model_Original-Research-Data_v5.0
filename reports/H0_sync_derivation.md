# H₀ Tension 的同步起源 — 推導筆記

## 背景

IDM 5.0 已確認：**同步遞迴** $C_{n+1}=1/(1+C_n)$ 支配暗能量行為，
產生特徵 bump $f(z)=1+\varepsilon\cdot (z/z_c)\cdot e^{-z/z_c}$ 於 $z_c\approx 0.6$。
但 H₀ tension（SH0ES 73.0 vs IDM 68.2）不能由 $f(z)$ 直接解釋——兩者尺度差 100 倍。

## 多尺度同步假設

同步遞迴嘅收斂率取決於因果域數量 $N$：

```math
s(N) = 1 - e^{-N/N_0}, \quad N_0=42
```

| 尺度 | 物理系統 | $N$ | $s(N)$ | 可觀測效應 |
|:-----|:---------|:---:|:------:|:----------|
| ~3000 Mpc ($z\approx 0.6$) | DE sector | 42 | 63% | $f(z)$ bump, $\Delta H/H \approx 5.7\%$ |
| ~34 Mpc ($z\approx 0.008$) | Cepheid 宿主 | 0.2 | 0.5% | 可忽略 (< 0.1%) |
| ~1 pc | Cepheid 本身 | $10^{-7}$ | $\sim 10^{-7}$ | 完全可忽略 |

**→ 同步完成度 $s(N)$ 模型不能解釋 Cepheid 尺度嘅 7% H₀ 偏差。**

## 替代通道：距離階梯校準嘅非交換性效應

Type II₁ von Neumann 代數嘅非交換性：$\tau(AB) \neq \tau(A)\tau(B)$。
喺距離階梯中：

```math
\mu_{\text{ceph}} = \tau(\text{Cepheid PL}) \cdot \tau(\text{geometric anchor})
```

如果 $\tau(AB) \neq \tau(A)\tau(B)$，校準會引入系統偏移。

**Anchor 效應**：
- NGC 4258 (maser, 7.6 Mpc)
- Milky Way (parallax, < 1 kpc)  
- LMC (eclipsing binaries, 50 kpc)

呢啲 anchor 嘅 $\tau(\text{anchor})$ 本身就係喺局部 W-field 中測量，
非交換性會令 anchor 距離同 global expansion 距離之間有固定 offset：

```math
\mu_{\text{obs}} = \mu_{\text{true}} + \Delta_{\text{anchor}}
\quad\text{其中}\quad \Delta_{\text{anchor}} = \tau([\text{anchor}, \text{global}]) \neq 0
```

呢個 $\Delta_{\text{anchor}}$ 係 **common-mode**——影響所有 Cepheid 宿主，
解釋點解 mean($\mu_{\text{obs}} - \mu_{\text{model}}$) $\neq 0$。

## 經驗性預測

如果 $\Delta_{\text{anchor}}$ 係同步嘅 signature：
1. **TRGB 距離階梯**應有唔同嘅 $\Delta_{\text{anchor}}$（因 anchor 方法唔同）
2. **Miras** 應有獨立嘅偏移
3. **所有 local distance ladder** 應有系統性偏差，幅度 $\propto$ anchor 尺度

目前嘅觀測：
- TRGB H₀ ≈ 69.8 (Anand+2022) — 低過 SH0ES 3.2 km/s (4.6%)
- Miras H₀ ≈ 73.3 (Huang+2024) — 接近 SH0ES
- Cepheids H₀ = 73.0 (Riess+2022)

TRGB 嘅較低 H₀ 可能反映唔同 anchor 方法有唔同嘅非交換性偏差。
Cepheid 同 Miras 嘅一致性可能表明兩者 share 類似嘅 SMC/LMC anchor。

## 下一步

要驗證呢個需要：
1. JWST Cepheid 數據（anchor 校準獨立性檢驗）
2. 將 $\Delta_{\text{anchor}}$ 參數化加入 SH0ES MCMC
3. fit: $H_0^{\text{local}} = H_0^{\text{global}} \times (1 + \delta_{\text{sync}})$
