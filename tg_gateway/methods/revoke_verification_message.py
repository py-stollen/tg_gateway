from .base import TelegramGatewayMethod


class RevokeVerificationMessage(
    TelegramGatewayMethod[bool],
    api_method="revokeVerificationMessage",
    returning=bool,
):
    """
    Source: https://core.telegram.org/gateway/api#revokeverificationmessage
    """

    request_id: str
