from enum import Enum


class STRATS_TYPE(Enum):
    GENERIC
    MAX_VANNA
    MAX_VOLGA
    OTC_REPLICA
    EXPIRY_FLY
    EXPIRY_SWITCH
    TAIL_FLY
    TAIL_SWITCH
    RISK_REVERSAL
    STRANGLE
    CALL_FLY
    PUT_FLY
    YCSO_SWO
    EXPIRY_COMBO
    TAIL_COMBO
    EXPIRY_TAIL_BOX
    EXPIRY_STRIKE_BOX
    TAIL_STRIKE_BOX


strats_type, neutral_metrics, anchor_metric, anchor_amount, anchor_leg

max_volga, [kappa, vanna], kappa, -1e3, 0
max_vanna, [kappa, volga], kappa, 1e3, 1
otc_replica, [kappa], kappa, 1e3, 0
expiry_fly, [gamma, vega], kappa, 1e3, 1
tail_fly, [kappa, gamma_pc12], kappa, 1e3, 1
expiry_switch, [gamma_pc11], kappa, 1e3, 1
tail_switch, [kappa], kappa, 1e3, 1
ycso_swo, [kappa], kappa, 1e3, 0
risk_reversal, [gamma, volga], kappa, 1e3, 1
strangle: [gamma, vanna], kappa, -1e3, 0
wedge, CAP_ST - SWO_ST
