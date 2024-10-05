from typing import Optional

from ..types import RequestStatus
from .base import TelegramGatewayMethod


class CheckVerificationStatus(
    TelegramGatewayMethod[RequestStatus],
    api_method="checkVerificationStatus",
    returning=RequestStatus,
):
    """
    Source: https://core.telegram.org/gateway/api#checkverificationstatus
    """

    request_id: str
    code: Optional[str] = None
