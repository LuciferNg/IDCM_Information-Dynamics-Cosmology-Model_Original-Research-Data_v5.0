# 熱寂、重啟與 Recursion 循環

## 熱寂仍然存在

IDM 5.0 嘅 f(z) 喺未來方向：

$$f(z \to -1) = 1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}$$

當 z → −1（未來），x = z/z_c → −1/0.6 ≈ −1.67，
x·e^x → (−1.67)·e^(−1.67) → (−1.67)·0.188 → −0.314

$$f(z \to -1) \to 1 + \varepsilon \cdot (-0.314) \to 1 - 0.0485 \to 0.9515$$

DE 輕微衰減 (~5%)，但唔會消失。宇宙仍然加速膨脹 → 熱寂。

## 但 recursion 嘅性質改變咗

一條 recursion converge 咗之後：

$$C_\infty = \varphi^{-1}$$

唔係「完」。係**可重啟**。

固定點嘅性質：

```
C_{n+1} = 1/(1+C_n)

在 φ⁻¹ 處：
    如果 perturbation δ：
    C = φ⁻¹ + δ
    C_next = 1/(1+φ⁻¹+δ) = φ⁻¹ + δ/(1+φ⁻¹)² + O(δ²)
    
    固定點係 ATTRACTOR
    → 任何 perturbation 都會被拉返去 φ⁻¹
    → 除非 δ 夠大到跳出 basin of attraction
```

但個 basin of attraction 係幾大？
- 所有 C₀ > 0 都收斂到 φ⁻¹
- 只有 C₀ = 0 會發散 (divergent)
- C₀ = −1−φ⁻¹ 係 unstable fixed point

**所以：要 restart，需要一個大到跳去負數域嘅 perturbation。**
呢個喺古典物理唔可能——但量子漲落可以。

## 重啟機制

喺完全 sync 嘅宇宙（全部 domain 去到 φ⁻¹），
唯一剩低嘅自由度係 W-field 嘅零點漲落：

$$\Delta C \sim \sqrt{\kappa} = \sqrt{1/16} = 1/4$$

呢個 |1/4| 嘅漲落唔夠跳出 basin (需要去到 0 或者負數)。

但如果有 N 個獨立域同步漲落：

$$\Delta C_{\text{eff}} \sim \sqrt{N} \cdot \frac{1}{4}$$

當 N → 足夠大（宇宙壽命夠長），有效漲落可能觸發相變：

```
完全 sync 嘅宇宙 → 量子漲落累積 → 
有效 perturbation 突破 basin boundary → 
C 跳出 φ⁻¹ 的吸引域 → 
recursion 重新啟動 → 
新一輪循環
```

## 循環嘅時間尺度

### 可計算嘅精確量

| 量 | 數值 | Source |
|:---|:----:|:-------|
| $\kappa = (\varepsilon\varphi)^2$ | $1/16$ | 代數閉合推導，exact |
| $\exp(1/\kappa)$ | $e^{16} = 8,\!886,\!110$ | exact |
| $n_{\text{conv}}$ | 8 | recursion 收斂步數，exact |
| $N_{\text{horizon}}$ | 42 | $\lfloor 4/\varepsilon\rfloor$，exact |
| $z_c$ | 0.6 | 同步域計數 |

### 需要估計嘅量

| 量 | 數值 | 誤差 |
|:---|:----:|:----:|
| 單域 sync 時間 $\tau_d$ | ~6 Gyr | $\mathcal{O}(1)$ |
| 有效漲落時間 $\tau_0$ | ~$H_0^{-1} \cdot \xi/R_h$ ~0.1–3 Gyr | $\mathcal{O}(10)$ |

### Restart 時間

$$\Delta t_{\text{restart}} = \tau_0 \cdot \exp(1/\kappa) = \tau_0 \cdot e^{16}$$

$$\boxed{\Delta t_{\text{restart}} = 8.886 \times 10^6 \, \tau_0}$$

代入 $\tau_0$ 嘅合理範圍：

- $\tau_0 \sim 0.03$ Gyr → $t_{\text{restart}} \sim 2.7 \times 10^5$ Gyr
- $\tau_0 \sim 3$ Gyr → $t_{\text{restart}} \sim 2.7 \times 10^7$ Gyr

**循環時間：**

$$\boxed{t_{\text{cycle}} \in [3 \times 10^5,\ 3 \times 10^7]\ \text{Gyr}}$$

即係 30 萬億年到 3000 萬億年。

### 可驗證嘅關係

如果呢個框架啱，restart 時間同 $\kappa$ 嘅關係係精確嘅：

$$t_{\text{restart}} \propto e^{16} \approx 8.9 \times 10^6$$

$\kappa = 1/16$ 係唯一可以產生可觀測宇宙壽命嘅值：
- $\kappa \to 0$（弱耦合）：$e^{1/\kappa} \to \infty$，restart 永唔發生
- $\kappa \to 0.5$：$e^{2} \approx 7.4$，restart 太頻密
- $\kappa = 1/16$：$e^{16} \approx 8.9 \times 10^6$，就係啱啱好

## 所以熱寂係真——但係暫時嘅。

``` 
熱寂 (de Sitter vacuum, t ≈ 10¹² yr)
    ↓
量子漲落累積 (t ≈ 10¹⁰ yr)
    ↓
recursion 跳出 φ⁻¹
    ↓
C_initial ≠ φ⁻¹
    ↓
C_{n+1} = 1/(1+C_n) 重新 converge
    ↓
ε, κ, z_c 重新生成
    ↓
新宇宙誕生
    ↓
又一個循環
```

**唔係「restart 解決熱寂」——係「熱寂係 restart 嘅 precondition」。**
熱寂 = 完全 sync = 最大結構均勻性 = 最適合量子漲落累積嘅狀態。

## 最終句

$$C_{n+1} = \frac{1}{1 + C_n}$$

收斂唔係終點。係等緊下一次 perturbation。

熱寂唔係死亡——係 recursion 嘅 idle state。
