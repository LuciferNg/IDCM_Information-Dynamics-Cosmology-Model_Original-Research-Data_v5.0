# 對抗熱寂社會的結構推導

## 框架映射

從 IDM 5.0 映射到社會系統：

| 宇宙學量 | 社會對應 |
|:---------|:---------|
| $C_{n+1} = 1/(1+C_n)$ | 社會認知 recursion |
| $\varphi^{-1} \approx 0.618$ | 社會固定點 (文化 equilibrium) |
| $\varepsilon = \varphi^{-1}/4$ | 社會開放度 |
| $A(r) = \varepsilon \cdot (r/\xi)^\beta$ | 擾動傳播幅度 |
| $\kappa = 1/16$ | 社會 closure constant |
| 熱寂 (de Sitter vacuum) | 文明熱寂 (認知真空) |

## 第一步：社會固定點的穩定性

社會 recursion 假設：

$$S_{n+1} = \frac{1}{1 + S_n}$$

固定點：

$$S_\infty = \varphi^{-1}$$

固定點附近的 Lyapunov 穩定性：

$$\left|\frac{dS_{n+1}}{dS_n}\right|_{S=\varphi^{-1}} = \left|\frac{-1}{(1+\varphi^{-1})^2}\right| = \frac{1}{\varphi^2} \approx 0.146$$

$$0.146 < 1 \quad\Rightarrow\quad \text{穩定固定點}$$

**社會自然趨向 equilibrium。任何 small perturbation 以因子 $\varphi^2 \approx 2.618$ 每步衰減。**

## 第二步：注入不穩定性 (ε-injection)

在 recursion 中注入 perturbation $\delta$：

$$S_{n+1} = \frac{1}{1 + S_n} + \varepsilon \cdot \delta$$

$\varepsilon$ 是注入振幅，$\delta$ 是擾動方向。

固定點 shift：

$$\Delta S_\infty \approx \varepsilon \cdot \varphi^2 \cdot \delta$$

即係：注入 $\varepsilon$ 將固定點偏移 $\varepsilon\varphi^2\delta$。

**只要 $\varepsilon > 0$，社會無法收斂到原來的固定點。**

臨界注入量防止收斂到任何固定點：

$$\varepsilon_{\text{crit}} > \frac{1 - \varphi^{-1}}{2} = \frac{1 - 0.618}{2} = 0.191$$

當 $\varepsilon > 0.191$，社會 recursion 無法 settle 到任何 equilibrium。

```
IDM 5.0 的 ε = 0.1545 接近但略低於這個 threshold。
這意味著宇宙本身也在「邊緣」——接近但不完全脫離平衡。
```

## 第三步：擴展認知邊界 (β-expansion)

認知邊界擴展 = 增加新維度。

在 IDM 中，尺度指數 $\beta = \varphi^{-1}/2$ 連接了不同尺度：

$$A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^\beta$$

擴展認知邊界意味著：

1. 打開新 domain → 增加 $\xi$（相關長度）
2. 校準新尺度 → 激活新 $r$ 值

社會認知空間的維度擴展：

$$D_{\text{cognitive}} = D_0 + \sum_i \beta_i \cdot \ln\left(\frac{r_i}{\xi_i}\right)$$

其中 $D_0$ 是初始認知維度，$\beta_i$ 是每個新 domain 的尺度指數。

**每次 calibrate 一個新 domain，認知空間維度增加 $\beta$。**

## 第四步：兩者協同

熱寂條件：

$$S_\infty = \varphi^{-1}, \quad \varepsilon = 0, \quad \beta = 0$$

即係：社會已收斂到固定點，無擾動注入，無新域。

對抗條件：

$$\varepsilon > 0 \quad \land \quad \beta > 0$$

即係：注入不穩定性 + 擴展邊界，兩者同時存在。

協同效應：

$$\text{Social Entropy} \propto \varepsilon \cdot \beta \cdot \ln\left(\frac{t}{\tau_0}\right)$$

- $\varepsilon$：防止收斂到固定點
- $\beta$：確保有新維度可以 iterate
- $\ln(t/\tau_0)$：時間累積效應

## 第五步：Calibrator 的操作方程

Calibrator 的兩個操作：

$$a = \varepsilon \cdot \delta \quad \text{(注入擾動)}$$

$$b = \beta \cdot \ln\left(\frac{r_{\text{new}}}{\xi}\right) \quad \text{(擴展邊界)}$$

有效 social entropy generation：

$$\frac{dS_{\text{social}}}{dt} = a \cdot b = \varepsilon \cdot \beta \cdot \delta \cdot \ln\left(\frac{r_{\text{new}}}{\xi}\right)$$

對抗熱寂的條件：

$$\frac{dS_{\text{social}}}{dt} > 0 \quad \Rightarrow \quad \varepsilon \cdot \beta > 0$$

**只要 calibrator 持續注入擾動 ($\varepsilon > 0$) 並擴展邊界 ($\beta > 0$)，社會 entropy 就不會歸零。**

不是「改變社會整體」——是**確保 sync field 中有至少一個非零梯度。**

## 最終公式

$$\boxed{\text{文明存活條件}:\ \varepsilon \cdot \beta > 0}$$

$$\boxed{\text{文明熱寂條件}:\ \varepsilon \cdot \beta = 0}$$

Calibrator 不需改變 macro trend。
**Calibrator 只需確保自己的 $\varepsilon \cdot \beta \neq 0$。**
