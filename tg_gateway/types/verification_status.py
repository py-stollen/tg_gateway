from typing import Optional

from .base import TelegramGatewayObject
from .custom import DateTime


class VerificationStatus(TelegramGatewayObject):
    """
    Source: https://core.telegram.org/gateway/api#verificationstatus
    """

    status: str
    updated_at: DateTime
    code_entered: Optional[str] = None
