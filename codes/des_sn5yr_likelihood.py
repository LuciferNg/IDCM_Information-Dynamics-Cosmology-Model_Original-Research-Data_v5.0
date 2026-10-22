"""
DES-SN5YR 完整似然模組
1820 SNe 距離模數 + 全協方差矩陣
邊際化絕對星等 M (analytical marginalization)
"""

import numpy as np
import os, csv

DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data"

def load_des_sn5yr(use_sys=True):
    """Load DES-SN5YR data: redshifts, distance moduli, full covariance"""
    # DES-SN5YR HD file has header lines then 'VARNAMES: ...' then data
    with open(f"{DATA_DIR}/DES_SN5YR_DES-Dovekie_HD.csv", 'r') as f:
        lines = f.readlines()
    
    # Find VARNAMES line
    varnames_line = None
    for i, line in enumerate(lines):
        if 'VARNAMES:' in line:
            varnames_line = i
            break
    
    if varnames_line is None:
        raise ValueError("Could not find VARNAMES line")
    
    # Parse headers
    headers = lines[varnames_line].replace('VARNAMES:', '').strip().split()
    print(f"Headers: {headers}")
    
    # Parse data lines (after VARNAMES)
    # Format: SN: <name> <survey_int> <zHD> <zHEL> <MU> <MUERR> ...
    # So zHD is col 3, MU is col 5
    z_list, mu_list = [], []
    for line in lines[varnames_line+1:]:
        parts = line.strip().split()
        if len(parts) >= 8:  # SN: + NAME + SURVEY + zHD + zHEL + MU + MUERR + ...
            try:
                z = float(parts[3])  # zHD is column index 3
                mu = float(parts[5])  # MU is column index 5
                if z > 0.005:
                    z_list.append(z)
                    mu_list.append(mu)
            except (ValueError, IndexError):
                continue
    
    z = np.array(z_list)
    mu_obs = np.array(mu_list)
    n = len(z)
    
    # 載入協方差矩陣 (from original npz file - it's an inverse cov in upper triangular)
    fname = "STAT+SYS.npz" if use_sys else "STATONLY.npz"
    d = np.load(f"{DATA_DIR}/DES_SN5YR_{fname}", allow_pickle=True)
    
    n_cov = int(d['nsn'].item()) if hasattr(d['nsn'], 'item') else int(d['nsn'][0])
    cov_data = d['cov']
    
    # Build full inverse covariance matrix from upper triangular
    # Note: npz stores INVERSE covariance (not the covariance itself) in upper triangular
    inv_cov = np.zeros((n, n))
    idx = np.triu_indices(n, 0)
    m = min(len(cov_data), len(idx[0]))
    upper_vals = cov_data[:m]
    inv_cov[idx[0][:m], idx[1][:m]] = upper_vals
    # Fill lower triangle
    i_lo = np.tril_indices(n, -1)
    inv_cov[i_lo] = inv_cov.T[i_lo]
    
    print(f"DES-SN5YR: {n} SNe loaded (from {n_cov} in npz), z∈[{z.min():.3f},{z.max():.3f}]")
    return z, mu_obs, inv_cov

def chi2_sn5yr(model, Om, h):
    """DES-SN5YR χ² with M marginalization
    使用 Goliath et al. (2001) eq. A9-A12 的解析邊際化
    """
    z, mu_obs, inv_cov = load_des_sn5yr(use_sys=True)
    
    # 模型距離模數
    mu_pred = np.array([5*np.log10((1+zi) * (299792.458/(h*100)) * model.DM(zi, Om) * 1e5) 
                        for zi in z])
    
    # 殘差
    delta = mu_pred - mu_obs
    
    # Full χ²
    chi2_full = delta @ inv_cov @ delta
    
    # M 邊際化 (Goliath+2001)
    B = np.sum(inv_cov @ delta)  # Σ Cov⁻¹ Δμ
    C = np.sum(inv_cov)          # Σ Cov⁻¹
    chi2 = chi2_full - B*B / C + np.log(C / (2*np.pi))
    
    return float(chi2)
