from enum import StrEnum, auto


class VerificationStatusType(StrEnum):
    CODE_VALID = auto()
    CODE_INVALID = auto()
    CODE_MAX_ATTEMPTS_EXCEEDED = auto()
    EXPIRED = auto()
