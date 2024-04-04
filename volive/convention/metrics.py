MAJOR_GREEKS = ['vega', 'kappa', 'gamma', 'vanna', 'volga', 'dskew', 'dsmile', 'theta']
PCA_GREEKS = ['gamma_pc11', 'gamma_pc12', 'gamma_pc22']
THETAS = ['theta_gamma', 'theta_vanna', 'theta_volga', 'theta_unpred', 'theta_vol_theta']


RATES_HIST_VALUES = {
    'df_2': 'df ** 2',
    'dv_star': 'dv - bb_slope_hedge * df',
    'dv_start_2': 'dv_star ** 2',
    'dv_star_df': 'dv_start * df',
    'f_diff': 'f - (inst_f - interp_basis_f) * 1',
    'vol_diff': 'vol - (inst_vol - interp_basis_vol) * 1',
    'skew_diff': '',

    'vol_rc': 'vega * vol_diff',
    'skew_rc': 'dskew * skew_diff',
    'asset': 'rol_rc + skew_rc + smile_rc',

    'gamma_perf': '.5 * gamma * df_2 + theta_gamma / 251',
    'vanna_perf': 'vanna * dv_start_df + theta_vanna / 251',
    'volga_perf': '.5 * volga * dv_star_2 + theta_volga / 251',
    'unpred_theta_perf': '(theta_unpred + vol_theta) * 1 / 251',

    'gvv_perf': 'gamma_perf + vanna_perf + volga_perf + unpred_theta_perf',
    'vol_asset_perf': 'vega * dv',
    'skew_asset_perf': 'skew * skew_risk',
    'vol_roll_hist': 'vega * vol_roll',
    'skew_roll_hist': 'skew * skew_roll',

    'atm_perform': 'gamma_perf + unpred_theta_perf + vol_roll_hist',
    'skew_perf': 'vanna_perf + skew_roll_hist',
    'smile_perf': 'volga_perf + smile_roll_hist',

    'ev': 'gvv_perf + vol_roll_hist + skew_roll_hist + smile_roll_hist',
    'hedged_ev': 'ev + vol_asset_perf + skew_asset_perf + smile_asset_perf',
}