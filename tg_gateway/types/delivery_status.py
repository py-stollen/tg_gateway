from .base import TelegramGatewayObject
from .custom import DateTime


class DeliveryStatus(TelegramGatewayObject):
    """
    Source: https://core.telegram.org/gateway/api#deliverystatus
    """

    status: str
    updated_at: DateTime
