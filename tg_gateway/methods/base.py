from stollen import StollenMethod
from stollen.enums import HTTPMethod
from stollen.types import StollenT

from ..client import TelegramGateway


class TelegramGatewayMethod(
    StollenMethod[StollenT, TelegramGateway],
    http_method=HTTPMethod.POST,
    abstract=True,
):
    pass
