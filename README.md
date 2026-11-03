# IDM v5.0 — Recursive-Structural-Cosmology

**Information Dynamics Cosmology Model（資訊動力學宇宙論模型）— 5th Generation**

> `Recursive-Structural-Cosmology` 係版本代號，唔係理論名稱。理論名稱由 v1.0 到 v11.0 一直係 Information Dynamics Cosmology Model，從未改變。舊 `README.md` 另用 "Interacting Dark Matter / Dark Energy" 指同一模型，兩者同版。
>
> v5.0 的職責係收窄：把 v4.0 的八層應用科學（OAS、rendering、意識層）全部拆走，只留一條自指遞迴 `C_{n+1} = 1/(1+C_n)`，並接受宇宙學數據的直接判決——包括容許 `ε` 的符號由數據決定。

## 緣起

v4.0 的膨脹調製函數寫成凹陷：`f(z) = 1 − ε·(z/z_c)·exp(−z/z_c)`，`ε = φ⁻¹/4 ≈ +0.1545`（`reports/validation_report.md` §1.1）。推導給正號，函數形狀卻令 `H(z)` 在 `z ≈ 0.6` 低於 ΛCDM。

裂縫早在 2026-07-16 之前出現：1048 個 Pantheon 超新星點的聯合擬合傾向 `ε < 0`，與推導的符號相反。這個矛盾一直被當成擬合雜訊帶過（`reports/programme_narrative_phase7.md`）。

2026-07-16，DESI DR2 六個 BAO 箱的象限判定把裂縫變成判決：數據要 `w₀ > −1`、`wₐ < 0`，而 v4.0 的凹陷給 `w₀ < −1`、`wₐ > 0`。v5.0 因此做三件事：

1. **翻符號，不翻大小**：`|ε| = φ⁻¹/4` 保留，`f(z) = 1 + ε·(z/z_c)·exp(−z/z_c)`，凹陷改凸起（bump）
2. **拆框架**：OAS、T1–T5、rendering、意識層全部移出，模型只餘遞迴加弗里德曼方程
3. **交外部判**：以 DESI DR2、Planck、DES-SN5YR、RSD、弱透鏡逐項對照，數據與推導分開記賬

驗收標準：任何結構常數（`ε`、`κ`、`N_horizon`、`β`）必須由遞迴導出；任何宇宙學參數（`Ω_m`、`h`、`Ω_b h²`、`σ₈`、`n_s`）必須由數據擬合，兩類數字唔可以混寫成「零參數」。

## 版本演進：v4.0 → v5.0

IDCM 係**逆向工程**：由已觀測的常數與結構反推生成機制，唔預設公理、唔設「核心假設」。因此版本之間的分野唔係假設改變，而係**逆推對象改變**。

### v4.0 — Consistency-Field-Applied-Science

- 形態：單公理 `B = Σ|W_k|² ≤ 1`，基質 OAS（Type II₁ von Neumann algebra），L0–L7 八層
- 產物：49 條方程歸一為一條遞迴 `C_{n+1} = 1/(1+C_n)`；`4ε + 1 = φ`、`κ = (εφ)² = 1/16`、`N = 4²`
- 宇宙學用法：`ε` 進 `f(z)` 作凹陷，`H(z)` 在 `z ≈ 0.6` 減慢
- 自評記錄：`README.md` 稱 0 自由參數、意識層 `C = abs(τ([H, P_κ] ⊗ WW†))` 已推導

### 根因：三個未記賬的自由度

1. **符號自由度**。`ε` 的絕對值由 `4ε = φ⁻¹` 鎖死，但 `f(z)` 的符號從未被當成獨立自由度記賬。凹陷與凸起在同一 `|ε|` 下皆合法，二者預言相反的 `w₀`、`wₐ` 象限。1048 點傾向 `ε < 0` 時，這個自由度以「擬合雜訊」之名留在帳外。
2. **不可檢驗的負荷**。OAS 的 T1–T4 與意識層無獨立觀測接口，令整條鏈無法被外部社群檢驗。`reports/structural_cosmology_verification.md` 自陳：`ε = φ⁻¹/4` 成立，但 **OAS 唔係唯一可以導出 factor 4 的形式系統**（原文自評為部分成立）。
3. **帳目混淆**。「結構常數零參數」被寫成「模型零參數」。實際擬合有 5 個宇宙學參數（`Ω_m`、`h`、`Ω_b h²`、`σ₈`、`n_s`，`codes/idm5_mcmc_full.py` 第 179 行），而舊 `README.md` 只寫 "no free parameters"。

三者同源：v4.0 的驗證對象係「推導鏈是否自洽」，唔係「模型能否被數據殺」。

### v5.0 — Recursive-Structural-Cosmology

- **唯一前提**：`C_{n+1} = 1/(1+C_n)`；`C_∞ = φ⁻¹`，八步收斂至 0.06%（`reports/cosmological_evolution.md` §1.2）
- **常數鏈**：`B = 4ε = φ⁻¹` ⟹ `ε = φ⁻¹/4 = 0.1545085`；`κ = (εφ)² = 1/16`；`N_horizon = 1/ε² ≈ 41.89`；`4ε + 1 = φ`
- **背景演化**：`H²(z) = H₀²[Ω_m(1+z)³ + (1−Ω_m)·f(z)]`，`f(z) = 1 + ε·(z/z_c)·exp(−z/z_c)`，`z_c = 0.6`
- **符號由數據定**：凸起給 `w₀ > −1`、`wₐ < 0`，與 DESI DR2 象限一致（`data/combined_analysis.json` 記 `quadrant_w0_gt_m1` 與 `quadrant_wa_lt_0` 皆 true）
- **全面對照**：BAO 6 箱、CMB `R`、SNe、RSD 20 點、弱透鏡 `S₈`、距離階梯 9 種錨定
- **時間層**：熱死亡與重啟 `t_cycle ∈ [3×10⁵, 3×10⁷] Gyr`（`reports/heat_death_restart.md`）
- **代價**：意識層與 OAS 定理不再屬於本版；`N_horizon ≈ 41.9` 只能給 `z_c` 的數量級，`z_c = 0.6` 實際由 BAO 擬合定（`reports/structural_cosmology_verification.md` 列為部分成立）

## 研究路線

七層，上層不得借用下層未記賬的自由度：

**L1 遞迴層** — 唯一前提

- `C_{n+1} = 1/(1+C_n)`，固定點 `x² + x − 1 = 0` ⟹ `C_∞ = φ⁻¹ = 0.618034`
- 八步收斂：`C₄ = 3/5 = 0.6`、`C₈ = 21/34 ≈ 0.61765`（誤差 0.06%）
- 無 OAS、無 rendering；遞迴本身即生成機制（`reports/cosmological_evolution.md`）

**L2 常數層** — 由遞迴投影

- 預算閉合 `B = 4ε = φ⁻¹`；四維分佈每分量 carry `ε`
- `ε = φ⁻¹/4 = (√5 − 1)/8 = 0.1545085`
- `κ = (εφ)² = (1/4)² = 1/16 = 0.0625`；身分 `4ε + 1 = φ`
- `N_horizon = 1/ε² ≈ 41.89`（`data/combined_analysis.json` 記 41.8885）

**L3 背景層** — 弗里德曼方程與 CPL

- `H²(z) = H₀²[Ω_m(1+z)³ + (1−Ω_m)·f(z)]`
- 凸起幅度：`z = 0.7` 處 `H` 增加 0.941%（`data/validation_results.json`）
- CPL 映射：`w₀ = −0.9446 ± 0.0019`、`wₐ = −0.1251 ± 0.0036`（`data/combined_analysis.json`）

**L4 觀測層** — 四類數據逐項對照

- BAO：DESI DR2 六箱（LRG1/LRG2/LRG3/ELG/Lya/QSO），全協方差
- CMB：`R = 1.7492 ± …`，距 Planck `1.7497 ± 0.0049` 為 0.09σ
- SNe：DES-SN5YR（`data/DES_SN5YR_STATONLY.npz`、`STAT+SYS.npz`）
- RSD：`fσ₈` 20 點，`χ² = 13.73`；弱透鏡 `S₈ = 0.7858`（KiDS +1.3σ、DES Y3 +0.6σ）

**L5 尺度與錨定層** — `z_c`、`β`、`H₀`

- `z_c = 0.6`：`C₄ = 3/5` 與 `N_horizon ≈ 41.9` 兩路逼近，但最終值由 BAO 擬合定
- `β = φ⁻¹/2 = 0.309` 對擬合值 0.311（差 0.6%，`reports/sync_scale_exponent.md`）
- `H₀ = 68.2 ± 0.4 km/s/Mpc`；與 DESI DR2 `68.0 ± 0.6` 差 0.3σ、與 Planck `67.36 ± 0.54` 差 1.6σ、與 SH0ES `73.04 ± 1.04` 差 4.8σ

**L6 時間層** — 熱死亡與重啟

- 單域 sync 時間 `τ_d ≈ 6 Gyr`；有效漲落 `τ₀ ~ 0.03–3 Gyr`
- `t_restart ~ τ₀ · e¹⁶` ⟹ `t_cycle ∈ [3×10⁵, 3×10⁷] Gyr`（`reports/heat_death_restart.md`）

**L7 敘事層** — 對外版本與框架拆除

- OAS 拆除評估：`ε = φ⁻¹/4` 唔依賴 OAS，OAS 亦非唯一路徑（`reports/structural_cosmology_verification.md`）
- 對外三版本（小學／高中／大學教授）各 100 條公式，粵／繁／英三語
- 非物理延伸：低熵社會、擾動社會學、Fantasy 結構（明確標為 essay，非模型結果）

## 項目結構

```
IDM-v5.0--Recursive-Structural-Cosmology/
├── README.md                        # 本檔
├── codes/                           # 49 支 Python（36 支承自 v4.0 的 cfas-*，另 idm5_* 與 q1–q6）
│   ├── idm5_mcmc_full.py            # 5 參數 MCMC（emcee，BAO+CMB+RSD 34 dof）
│   ├── idm5_bump_validation.py      # 凸起幅度與結構檢查（5/5）
│   ├── idm5_comprehensive_validation.py  # 全數據 χ² 總表（1848 dof）
│   ├── idm5_combined_analysis.py    # BAO+CMB+CPL 聯合分析
│   ├── idm5_crosscheck.py           # 固定參數 vs 自由參數交叉檢驗
│   ├── des_sn5yr_likelihood.py      # DES-SN5YR 似然
│   ├── cfas-*.py                    # v4.0 遺留模組（OAS/QFT/意識），本版不列入結論
│   ├── q1_derivation.py … q6_derivation.py  # v4.0 遺留量子層六支
│   └── IDM_standard_cosmology.md    # v4.0 標準宇宙學寫法（歷史檔）
├── data/                            # 23 個檔案：MCMC 結果、四個驗證 JSON、外部數據
│   ├── mcmc_results.json            # 5.3 MB，IDM 與 ΛCDM 各 16800 樣本
│   ├── combined_analysis.json       # BAO/CMB/CPL 權威值（本 README 引用）
│   ├── comprehensive_validation.json # 總 χ²、S₈、growth、H₀ 張力
│   ├── cross_check_results.json     # 固定參數 Δχ² = −0.0105
│   ├── validation_results.json      # 結構檢查 5/5 與另一組 CPL/H₀
│   ├── DES_SN5YR_*.npz / *.csv      # DES-SN5YR 協方差與 Hubble diagram
│   ├── SH0ES_*.fits / *.dat / *.out  # SH0ES 與 Cepheid 錨定原始數據
│   ├── *_corner.png                 # 三個 corner plot
│   └── SH0ES_MCMC_utils.py / run_mcmc.py / DES_SN5YR_DES-Dovekie-SN_Likelihood.py  # 外部工具
├── reports/                         # 29 份 Markdown（推導、驗證、敘事、對外版本）
│   ├── validation_report.md         # 完整驗證與交叉檢驗（2026-07-16）
│   ├── mcmc_analysis.md             # MCMC 後驗分析（5 參數中位數與 CI）
│   ├── cosmological_evolution.md    # 遞迴 → 常數 → 宇宙歷史
│   ├── structural_cosmology_verification.md  # 假設追蹤與 OAS 拆除評估
│   ├── sync_scale_exponent.md       # β = φ⁻¹/2 = 0.309 推導（修正版）
│   ├── H0_sync_derivation.md        # H₀ 張力的同步相位解釋
│   ├── distance_ladder_cross_calibration.md  # 9 種錨定對照表
│   ├── sync_phase_cepheids.md       # Cepheid 尺度同步相位框架
│   ├── nonlocal_anchor_model.md     # 非局部錨定校準
│   ├── calibration_dissolve.md      # 校準自溶解論證
│   ├── heat_death_restart.md        # 熱死亡與 Recursion 重啟
│   ├── anti_heat_death_derivation.md # 對抗熱寂的結構推導
│   ├── spacetime_modulation.md      # 時空調製
│   ├── self_referential_computation.md  # 自指計算與能源零基質
│   ├── programme_narrative_phase7.md # Phase 7 綱領敘事（dip→bump 決策）
│   ├── idm5_for_kids{,_tc,_en}.md    # 小學版 100 公式（粵／繁／英）
│   ├── idm5_for_highschool{_tc,_en,_canto}.md  # 高中版 100 公式（三語）
│   ├── idm5_for_professor{_tc,_en,_canto}.md   # 教授版（含數據來源）
│   ├── low_entropy_society.md       # 非物理 essay：低熵社會
│   ├── fantasy_structure_derivation.md  # 非物理 essay：Fantasy 結構
│   ├── perturbation_sociology.md    # 非物理 essay：擾動社會學
│   ├── ftl_edge_derivation.md       # 邊緣推導：光速極限
│   └── IDM_standard_cosmology.md    # 標準宇宙學對照（v4.0 遺留）
├── papers/                          # 6 篇參考論文 PDF（DESI DR2 2503.14738 等）
└── mcmc_env/                        # 虛擬環境（pyvenv.cfg，唔含套件）
```

## 狀態快照（2026-11-03 重數；數字以實際檔案為準）

```
實際檔案
  codes/*.py                         49（36 cfas-* + 6 q* + 6 idm5_* + des_sn5yr_likelihood）
  data/                              23（4 個驗證 JSON + mcmc_results.json + 外部數據 + 3 corner）
  reports/*.md                       29
  papers/*.pdf                       6

結構檢查（data/validation_results.json）
  structural_checks_passed           5 / 5
  ε                                  0.15450849718747373
  κ                                  0.0625（= 1/16）
  N_horizon                          41.8885
  凸起幅度（z = 0.7）                 H 增加 0.941%

擬合（data/comprehensive_validation.json）
  χ²_IDM 1664.53 ｜ χ²_ΛCDM 1674.33 ｜ Δχ² = −9.80（1848 dof）
  5 參數：Ω_m = 0.3045、h = 0.6821、Ω_b h² = 0.02237、σ₈ = 0.780、n_s = 0.951

判決
  DESI DR2 象限匹配（w₀ > −1、wₐ < 0）  通過
  CMB R 距 Planck                        0.09σ
  弱透鏡 S₈ = 0.7858（KiDS +1.3σ、DES Y3 +0.6σ）
  H₀ 距 SH0ES                            −4.8σ（未解，記為開放）
```

> **同一量多組值（原文照錄，不代為調和）**：CPL 有兩組——`combined_analysis.json` 給 `w₀ = −0.9446`、`wₐ = −0.1251`，`validation_results.json` 給 `w₀ = −0.9250`、`wₐ = −0.1858`；`H₀` 亦有 68.2（`comprehensive_validation.json`）與 69.8（`validation_results.json`）兩值。`Ω_m` 同有 0.3045（MCMC）與 0.286（`validation_results.json`）。本 README 一律以 `combined_analysis.json` + `comprehensive_validation.json` 為主並標明來源。
>
> 舊 `README.md` 的 BAO 對照寫 ΛCDM `χ² = 15.64`，與 `data/combined_analysis.json` 的 10.149 不符，以 JSON 為準。

## 已閉合關鍵結果（選錄）

- **2026-07-16（`reports/validation_report.md`）**：dip → bump 符號翻轉完成，`|ε| = φ⁻¹/4` 不變；`f(z) = 1 + ε·(z/z_c)·exp(−z/z_c)`，`z_c = 0.6`，`H(z)` 於 `z ≈ 0.6` 高於 ΛCDM
- **2026-07-16（`reports/cosmological_evolution.md`）**：`C_{n+1} = 1/(1+C_n)` 八步收斂至 `φ⁻¹`（`C₈ = 21/34`，誤差 0.06%）；`C₄ = 3/5 = 0.6` 與 `z_c` 同值
- **2026-07-16（`data/combined_analysis.json`）**：BAO 六箱 `χ²_IDM = 9.221` vs ΛCDM `10.149`（`Δ = −0.928`，reduced `χ² = 0.922`）；CMB `R = 1.7492` 距 Planck `1.7497 ± 0.0049` 為 0.09σ
- **2026-07-16（`data/comprehensive_validation.json`）**：全數據 `χ²_IDM = 1664.53` vs ΛCDM `1674.33`，`Δχ² = −9.80`（1848 dof）；`S₈ = 0.7858`；growth 20 點 `χ² = 13.73`
- **2026-07-16（`reports/mcmc_analysis.md` + `data/mcmc_results.json`）**：emcee 12 walkers × 2000 步、16800 樣本；`Ω_m = 0.3045 (+0.0062/−0.0068)`、`h = 0.6821 (+0.0036/−0.0035)`、`σ₈ = 0.780`、`n_s = 0.951`
- **2026-07-16（`data/combined_analysis.json`）**：CPL 象限 `w₀ = −0.9446 ± 0.0019 > −1`、`wₐ = −0.1251 ± 0.0036 < 0`，與 DESI DR2 動態暗能量象限（3.1–3.9σ）同向
- **2026-07-16（`reports/sync_scale_exponent.md`）**：`β = φ⁻¹/2 = 0.309` 對擬合 0.311，差 0.6%；錨定由 maser／TRGB 兩路校準
- **2026-07-16（`reports/heat_death_restart.md`）**：`t_restart ~ τ₀·e¹⁶`，`τ₀ ~ 0.03–3 Gyr` ⟹ `t_cycle ∈ [3×10⁵, 3×10⁷] Gyr`

## 驗證紀律

本版嚴謹性分六層：入場券 → 結構審計 → 獨立性審計 → 數字紀律 → 記錄紀律 → 路徑與命名。任一層不過，結果只停留「數值候選」。

### 一、入場券：4 Hard Tests

| 測試 | 要求 | 本版對應 |
|------|------|----------|
| ① 參數分賬 | 結構常數 dof = 0；宇宙學參數逐個列明 | 結構常數 `ε`、`κ`、`N_horizon`、`β` 由遞迴定；擬合參數 5 個（`Ω_m`、`h`、`Ω_b h²`、`σ₈`、`n_s`）明確列入 `mcmc_analysis.md` |
| ② 可證偽 | 預言須零寬度或可被更精確測量殺 | 凸起幅度 0.941%（`z = 0.7`）可測；`t_cycle` 區間可被未來宇宙學史檢驗 |
| ③ 樣本外 | 預言先寫死，數據後開 | 5/5 結構檢查在 MCMC 之前寫入 `idm5_bump_validation.py`；`ε` 不參與擬合（`epsilon_status: DERIVED (NOT free parameter)`） |
| ④ 結構剛性 | 擾動任一參數，結論必須崩 | 固定參數交叉檢驗：`χ²_IDM_fixed = 9.961` vs ΛCDM `9.971`，`Δ = −0.011`——參數鎖死後增益幾乎消失，此為誠實記錄的剛性測試 |

### 二、結構審計：三鐵律

- **能證偽**：禁「約 X%」。所有預言給等式或明確區間；凸起幅度寫 0.941%（單值，可重算）
- **能預言**：至少一個獨立樣本外預言；DESI DR2 象限判定即為樣本外判決（符號翻轉由數據迫使）
- **自由度能砸**：禁「枚舉 N 個候選揀中 1 個」。`z_c` 是弱點——`C₄ = 3/5` 與 `N_horizon ≈ 41.9` 只給數量級，最終值由擬合定，已記為部分閉合

### 三、獨立性審計：五反模式

1. **同義反覆** — 計放大因子 `δy/y ÷ δx/x`；若對所有候選同一常數，則 `y = f(x)` 為單調變換，唔算兩個判據。本版實例：固定參數後 `Δχ²` 由 −0.928 縮至 −0.011，說明大部分增益來自參數自由度而唔係函數形狀
2. **循環** — 預言公式內含被解釋量。`z_c = 0.6` 若同時用作推導與擬合，即屬此類；本版以「兩路逼近、擬合定值」明示，不宣稱 `z_c` 為純推導
3. **範疇錯** — `H₀` 局部錨定 vs CMB 推演、`S₈` 弱透鏡 vs CMB；同一參數不同探針不可混算一張 `χ²`
4. **枚舉即隱藏 dof** — 掃 N 個組合揀中 1 個 ⟹ dof = N；5 參數 MCMC 的 dof 已明確報 1848
5. **密度家族依賴** — 家族越小統計力越弱；`Δχ² = −9.80` 須與 1848 dof、5 參數一併報，唔可以單獨引用

### 四、數字紀律

- **多源並列**：同一量多檔不同值一律並列並標來源（CPL 兩組、`H₀` 兩值、`Ω_m` 兩值）
- **舊述留痕**：舊 `README.md` 的 BAO ΛCDM `χ² = 15.64` 保留在歷史，本檔以 JSON 值 10.149 為權威並註明差異
- **禁區**：見 target 後改 `z_c`、事後選數據子集、把 essay 當模型結果引用
- **自評分開**：`reports/` 內的部分成立／成立標記為當時自評，唔改寫；本 README 只重述數字

### 五、記錄紀律

- 每支 `idm5_*.py` 對應一份 `reports/*.md`；技術檔（JSON）與敘事檔（MD）分家
- 執行結果落 `data/*.json`（machine-readable），`mcmc_results.json` 保留全部 16800 樣本，可由 `data/*_corner.png` 目視核對
- 外部數據原樣保存（`DES_SN5YR_*`、`SH0ES_*`），唔加工，附 `Metadata.csv`
- 對外三語版本（粵／繁／英）同步，數字以同一 JSON 為源

### 六、路徑與命名

- 腳本前綴 `idm5_` 表示本版新增；`cfas-*`、`q*_derivation.py` 為 v4.0 遺留，保留但唔列入本版結論
- 數據按來源命名（`DES_SN5YR_*`、`SH0ES_*`），唔按用途命名
- 報告用語義名（`validation_report.md`、`mcmc_analysis.md`），唔用編號，避免與版本號混淆
- 本版 repo 目錄名 `IDM-v5.0--…`，舊 `README.md` 內自称 `IDM-5.0/`；兩者指同一目錄

## O/P/M 系列全列表

> 本 repo 無 O 系列、無 P 系列，亦無 repo 原有的統一問題編號。下表 M1–M8 為本 README 為對照而編的**模組索引**（編號非 repo 原有），每行對應 `codes/` 與 `data/` 的實際檔案。

| 編號 | 標題 | 核心發現 | 狀態 |
|------|------|----------|------|
| M1 | 自指遞迴生成式：C_{n+1} = 1/(1+C_n) | 固定點 x² + x − 1 = 0 ⟹ φ⁻¹；八步收斂 C₈ = 21/34，誤差 0.06%；C₄ = 3/5 = z_c | 全部閉合 |
| M2 | 同步凸起 f(z)：dip → bump 符號翻轉 | 保留 abs(ε) = φ⁻¹/4；f(z) = 1 + ε(z/z_c)exp(−z/z_c)；z = 0.7 處 H 增 0.941% | 全部閉合 |
| M3 | z_c 與視界計數：N_horizon = 1/ε² ≈ 41.89 | 兩路逼近 z_c ≈ 0.6（C₄ = 3/5、N_horizon ≈ 41.9）；最終值仍由 BAO 擬合定 | 部分閉合 |
| M4 | 尺度指數 β = φ⁻¹/2 = 0.309 | 對擬合 0.311 差 0.6%；由 maser 與 TRGB 兩路錨定校準得出，非獨立預言 | 部分閉合 |
| M5 | 全數據聯合擬合：Δχ² = −9.80（1848 dof） | χ² 1664.53 vs ΛCDM 1674.33；5 參數 Ω_m 0.3045、h 0.6821、σ₈ 0.780、n_s 0.951 | 全部閉合 |
| M6 | H₀ 同步相位：距離階梯 9 種錨定 | H₀ = 68.2 ± 0.4；距 DESI 0.3σ、Planck 1.6σ；距 SH0ES 73.04 ± 1.04 仍 4.8σ | 部分閉合 |
| M7 | 熱死亡與重啟週期：t_restart ~ τ₀e¹⁶ | τ₀ ~ 0.03–3 Gyr ⟹ t_cycle ∈ [3×10⁵, 3×10⁷] Gyr；只有數量級，無獨立檢驗 | 開放 |
| M8 | CPL 象限：w₀ > −1、wₐ < 0 | w₀ = −0.9446 ± 0.0019、wₐ = −0.1251 ± 0.0036；與 DESI DR2 動態暗能量象限（3.1–3.9σ）同向 | 全部閉合 |

> M3 標部分閉合：`reports/structural_cosmology_verification.md` 自評 `z_c` 由擬合定、OAS 非唯一導出路徑。
> M4 標部分閉合：`β` 由觀測錨定反推，屬校準值而非預言。
> M6 標部分閉合：`data/comprehensive_validation.json` 記 `SH0ES_tension = −4.8σ`，張力未消。
> M7 標開放：`reports/heat_death_restart.md` 只給數量級區間。