PNL_MARKET_MOVE = {
    'on_df': 'f_open - f_base',
    'on_dv': 'vol_atm_event_open - vol_atm_event_base',
    'on_dskew': '',
    'on_dsmile': '',
    'int_df': 'f_end - f_open',
}


PNL_POSITIONAL_EXPLAINED = {
    'explained': 'pv_end - pv_base',
    'explained__on': 'pv_open - pv_base',
    'explained__on__time': 'pv_time - pv_base',
    'explained__on__rates_roll': 'pv_rates_roll - pv_time',
    'explained__on__vol_roll': 'pv_vol_roll - pv_rates_roll',
    'explained__on__skew_smile_roll': 'pv_open - pv_vol_roll',
    'explained__int': 'pv_end - pv_open',
    'explained__int__rates': 'pv_rates - pv_open',
    'explained__int__vol': 'pv_vol - pv_rates',
    'explained__int__skew': 'pv_skew - pv_vol',
    'explained__int__event': 'pv_end - pv_skew'
}


PNL_POSITIONAL_PREDICTED = {
    'predicted__on__time': 'dt * theta_base',
    'predicted__on__time__theta_gamma': 'dt * theta_gamma_base',
    'predicted__on__time__theta_vanna': 'dt * theta_vanna_base',
    'predicted__on__time__theta_volga': 'dt * theta_volga_base',
    'predicted__on__time__theta_vol_theta': 'dt * theta_vol_theta_base',
    'predicted__on__time__theta_unpred': 'dt * theta_unpred_base',
    'predicted__on__rates_roll__rates_roll': 'df * delta_base',
    'predicted__on__vol_roll__vol_roll': 'dv * vega_base',
    'predicted__on__skew_vol__skew_roll': 'dskew * skew_risk_base',
    'predicted__on__skew_vol__smile_roll': 'dsmile * smile_risk_base',
    'predicted__int__rates__delta': 'df * delta_open',
    'predicted__int__rates__gamma': 'df ** 2 * .5 * gamma_open',
    'predicted__int__vol__vega': 'dv_star * vega_open',
    'predicted__int__vol__vanna': 'dv_star * df * vanna_open',
    'predicted__int__vol__volga': '.5 * dv_star ** 2 * volga_open',
    'predicted__int__vol__skew': 'dskew * skew_risk_open + dsmiel * smile_risk_open',
    'predicted__int__vol_no_bb': 'int__vol_no_bb__vega + volga + vanna'
}