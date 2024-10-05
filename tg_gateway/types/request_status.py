from typing import Optional

from .base import TelegramGatewayObject
from .delivery_status import DeliveryStatus
from .verification_status import VerificationStatus


class RequestStatus(TelegramGatewayObject):
    """
    Source: https://core.telegram.org/gateway/api#requeststatus
    """

    request_id: str
    phone_number: str
    request_cost: float
    remaining_balance: Optional[float] = None
    delivery_status: Optional[DeliveryStatus] = None
    verification_status: Optional[VerificationStatus] = None
    payload: Optional[str] = None
