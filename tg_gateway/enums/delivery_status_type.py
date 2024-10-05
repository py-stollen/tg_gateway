from enum import StrEnum, auto


class DeliveryStatusType(StrEnum):
    SENT = auto()
    READ = auto()
    REVOKED = auto()
