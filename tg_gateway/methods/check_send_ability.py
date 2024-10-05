from ..types import RequestStatus
from .base import TelegramGatewayMethod


class CheckSendAbility(
    TelegramGatewayMethod[RequestStatus],
    api_method="checkSendAbility",
    returning=RequestStatus,
):
    """
    Source: https://core.telegram.org/gateway/api#checksendability
    """

    phone_number: str
