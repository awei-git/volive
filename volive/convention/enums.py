from enum import Enum


class INST_TYPE(Enum):
    SWAPTION
    SRFO


class SAVE_LOCATION(Enum):
    FILE
    S3
    REDIS


class VAL_REQ(Enum):
    STATUS
    META
    BASE
    RESOLVE
    PARAMS
    METRICS_BASE
    METRICS_F_AND_VOL
    METRICS
    METRICS_SCENARIOS
    SETTLE_BASIS
    MTM
    DELTA_HEDGE


