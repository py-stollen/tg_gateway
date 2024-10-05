from typing import Optional

from ..types import RequestStatus
from .base import TelegramGatewayMethod


class SendVerificationMessage(
    TelegramGatewayMethod[RequestStatus],
    api_method="sendVerificationMessage",
    returning=RequestStatus,
):
    """
    Source: https://core.telegram.org/gateway/api#sendverificationmessage
    """

    phone_number: str
    request_id: Optional[str] = None
    sender_username: Optional[str] = None
    code: Optional[str] = None
    code_length: Optional[int] = None
    callback_url: Optional[str] = None
    payload: Optional[str] = None
    ttl: Optional[int] = None
