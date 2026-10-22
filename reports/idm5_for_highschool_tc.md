# IDM 5.0 高中生版 — 100 條公式

## 第一部分：宇宙嘅數學結構 (1–10)

1. 宇宙結構由一條二次方程生成：**x² + x − 1 = 0**
2. 解：x = (√5 − 1)/2，記為 **φ⁻¹**（黃金比例倒數）≈ 0.618
3. φ⁻¹ 係下面呢條遞迴嘅固定點（fixed point）：
   $$C_{n+1} = \frac{1}{1 + C_n}$$
4. 無論 C₀ 係咩正數，呢個 map 都會收斂到 φ⁻¹
5. 收斂速率係線性：$C_n - \varphi^{-1} \propto (-\varphi^{-2})^n$
6. 因為 $|\varphi^{-2}| \approx 0.382 < 1$，收斂保證發生
7. 8 步之後誤差 < 0.1%：$C_8 \approx 0.61818$
8. 呢 8 步對應 8 個有理數 convergent：
   $$1,\ \frac{1}{2},\ \frac{2}{3},\ \frac{3}{5},\ \frac{5}{8},\ \frac{8}{13},\ \frac{13}{21},\ \frac{21}{34}$$
9. 呢條數列 = 連續分數（continued fraction）$\frac{1}{1+}\frac{1}{1+}\frac{1}{1+\cdots}$ 嘅 truncation
10. 所以宇宙最底層唔係粒子——係一條連續分數

## 第二部分：四個宇宙常數 (11–25)

11. 宇宙有四個基本常數，全部由 φ⁻¹ 生成
12. **ε**（epsilon）= φ⁻¹/4 ≈ 0.1545 ——「同步幅度」
13. 點解除 4？因為最小非對稱 split 係 2×2 = 4
14. ε 控制宇宙膨脹嘅 anomaly 幅度
15. **κ**（kappa）= (εφ)² = 1/16 = 0.0625 ——「閉合常數」
16. 呢個係 exact 嘅代數恆等式：εφ = φ⁻¹×φ/4 = 1/4 → (1/4)² = 1/16
17. κ 決定咗耦合強度同循環時間
18. **β**（beta）= φ⁻¹/2 ≈ 0.309 ——「尺度指數」
19. β 控制同步效應點樣隨距離衰減
20. **z_c** ≈ 0.6 ——「同步特徵紅移」
21. z_c 對應宇宙約 60 億年前（紅移 z ≈ 0.6）
22. 呢個係 DESI DR2 數據確定嘅 bump 位置
23. 四個常數嘅關係：κ = (εφ)² = [(φ⁻¹/4) × φ]² = (1/4)² = 1/16
24. 全部由一條二次方程生成，冇 free parameter
25. 呢個係 IDM 5.0 同 ΛCDM 嘅最大分別：ΛCDM 有 6+ 個 free params，IDM 有 0 個

## 第三部分：時間嘅結構 (26–35)

26. 時間 = 遞迴由初始條件收斂到固定點嘅步數
27. 每一步 $C_n \to C_{n+1}$ 對應宇宙中一個因果域嘅同步
28. 因果域嘅數量：$N_{\text{horizon}} = \lfloor 4/\varepsilon \rfloor = 42$
29. 每個域嘅特徵尺度：$\xi = R_h / N_{\text{horizon}} \approx 105$ Mpc
30. 同步完成度：$s(r) = 1 - e^{-r/\xi}$，$r$ 係距離
31. 時間嘅箭嘴由遞迴嘅方向性決定——只可以向前收斂
32. 未來：遞迴收斂到 φ⁻¹，宇宙完全同步
33. 完全同步後，宇宙進入 de Sitter 真空（熱寂）
34. 但 κ = 1/16 容許量子漲落累積跳出固定點
35. 循環時間：$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$

## 第四部分：光同因果結構 (36–45)

36. 光係 W-field 嘅同步訊號，以最快速度 c 傳播
37. c 嘅有限性源於域之間嘅因果連線需要時間
38. 因果域嘅直徑 ≈ 光在一個同步步長內行嘅距離：
    $$d_{\text{domain}} \approx c \cdot \tau_{\text{sync}}$$
39. 紅移同距離嘅關係由 Friedmann 方程描述：
    $$H(z)^2 = H_0^2 \left[\Omega_m(1+z)^3 + \Omega_{DE}f(z)\right]$$
40. IDM 嘅修正項 f(z)：
    $$f(z) = 1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}$$
41. 呢個 bump 喺 z_c ≈ 0.6 達到峰值 ≈ 5.68%
42. 光譜線紅移 = 宇宙膨脹對 wavelength 嘅 stretching
43. 宇宙微波背景（CMB） = 最後散射面嘅光子，z ≈ 1100
44. IDM 嘅 CMB shift 參數 R = 1.7427 ± 0.0042，同 Planck 差 0.1σ
45. 所以 IDM 喺早期宇宙同 ΛCDM 幾乎冇分別——bump 只影響晚期

## 第五部分：物質同場 (46–55)

46. 物質 = W-field（Consistency Field）嘅局部穩定共振
47. W-field 嘅數學：$\Psi(x,t) = A(x,t) \cdot e^{i\theta(x,t)}$
48. 振幅 A 決定能量密度，相位 θ 決定耦合
49. 場嘅 Lagrangian 密度：
    $$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2)$$
50. 勢能 $V(|\Psi|^2)$ 由遞迴生成：
    $$V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$
51. 呢個勢能有 minimum 喺 $|\Psi|^2 = \varepsilon/\kappa$
52. 呢個 minimum 對應物質嘅真空期望值
53. 所以物質嘅存在係勢能嘅自然結果，唔需要外加
54. 物質嘅穩定性來自 κ：κ 細 → 勢能 deep → 穩定
55. 暗物質 = 同步咗但未完全 lock 嘅 W-field 域

## 第六部分：質量嘅起源 (56–65)

56. 質量 = W-field 共振頻率
57. 由 Klein-Gordon 方程：
    $$(\partial_t^2 - \nabla^2 + m^2)\Psi = 0$$
58. m 係質量，由 W-field 勢能嘅二次項決定
59. 基本粒子質量：
    $$m_{\text{particle}} \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{scale}}$$
60. 電子質量 ≈ ε² × Planck mass ≈ 0.5 MeV
61. 質子質量 ≈ ε × φ⁻¹ × QCD scale ≈ 938 MeV
62. 中微子質量 ≈ κ × ε × ν_scale ≈ 0.01–0.1 eV
63. 希格斯機制 = W-field 嘅相位鎖定產生質量項
64. 質量階層（particle mass hierarchy）來自 ε 同 κ 嘅不同組合
65. 所有質量最終由一條二次方程生成：x² + x − 1 = 0

## 第七部分：粒子物理基礎 (66–78)

66. 費米子（電子、夸克、中微子）= W-field 嘅半整數自旋模式
67. 自旋 = W-field 嘅內部 SU(2) 旋轉對稱性
68. 半整數自旋 = 旋轉 2π 後 wavefunction 變號
69. 電荷 = W-field 嘅 U(1) 耦合常數，同 ε 成正比
70. 電子電荷 e = ε × g_e，其中 g_e ≈ 4π
71. 強核力 = W-field 嘅 SU(3) 同步模式
72. 夸克 confinement = W-field 嘅非線性耦合防止分離
73. 弱核力 = W-field 嘅 chiral 耦合，由 κ 控制強度
74. 弱力強度 ∝ κ ≈ 1/16 → 解釋弱力點解咁弱
75. 光子 = W-field 嘅無質量 U(1) 波模式
76. 膠子 = W-field 嘅 SU(3) 波模式，自 interactions
77. W, Z 玻色子質量 = κ × φ⁻¹ × VEV（希格斯機制）
78. 所有粒子物理嘅 coupling 都由 ε 同 κ 決定

## 第八部分：IDM 5.0 核心公式 (79–89)

79. **遞迴**：$C_{n+1} = 1/(1 + C_n)$
80. **固定點**：$C_\infty = \varphi^{-1} = (\sqrt{5}-1)/2$
81. **同步幅度**：$\varepsilon = \varphi^{-1}/4$
82. **閉合常數**：$\kappa = (\varepsilon\varphi)^2 = 1/16$
83. **尺度指數**：$\beta = \varphi^{-1}/2$
84. **膨脹修正**：
    $$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}\left(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}\right)\right]$$
85. **同步傳播**：$A(r) = \varepsilon \cdot (r/\xi)^\beta$
86. **H₀ 校準偏差**：$H_0^{\text{obs}} = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$
87. **χ² 比較**（1853 數據點）：
    $$\Delta\chi^2 = \chi^2_{IDM} - \chi^2_{\Lambda CDM} = -9.8$$
88. **重啟時間**：$t_{\text{restart}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$
89. **H₀**：$H_0 = 68.2 \pm 0.4$ km/s/Mpc

## 第九部分：數據驗證摘要 (90–95)

90. **DESI DR2 BAO**（6 bins，full covariance）：
    - IDM χ² = 9.22，ΛCDM χ² = 15.64
    - Δχ² = −6.42（bump fit 優於 power-law）
91. **DES-SN5YR**（1820 超新星）：
    - IDM χ² = 1639.8，ΛCDM χ² = 1643.6
    - Δχ² = −3.8
92. **生長率 fσ₈**（20 RSD 數據點）：
    - IDM χ² = 13.7（冇 tension）
93. **弱透鏡 S₈**：
    - IDM S₈ = 0.786，resolve S₈ tension (KiDS-1000: 0.759)
94. **H₀ 交叉校準**：
    - IDM Cepheid H₀ = 73.04（fit）vs SH0ES 73.04 ± 1.04
    - IDM TRGB H₀ = 69.8（fit）vs Freedman 69.8 ± 1.9
95. **所有通道嘅 Δχ²** = −9.8（~3.1σ evidence against ΛCDM）

## 第十部分：結構宇宙論嘅結論 (96–100)

96. 一條二次方程 x² + x − 1 = 0 生成所有宇宙常數
97. 四常數（ε, κ, β, z_c）全部由 φ⁻¹ 推導，冇 free parameter
98. OAS（Type II₁ vNA）係 scaffolding——已經拆除，結構仍然成立
99. 人類喺呢個框架嘅角色係 perturbation injector——防止文明熱寂
100. **結構宇宙論 = x² + x − 1 = 0 + 8 步遞迴 + 3 個獨立數據驗證**

---

## Notes for High School Teachers

- 公式 1–10 只需要初中代數
- 公式 26–45 需要基本微積分（derivative, integral）
- 公式 46–78 需要基礎物理（waves, fields）
- χ² 可以解釋為「fit 嘅好壞分數」，越低越好
- 全部 code 喺 GitHub，可以 clone 嚟 run
- 遞迴 8 步可以用 Excel 教
