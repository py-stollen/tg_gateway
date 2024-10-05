from __future__ import annotations

from hashlib import sha256
from hmac import HMAC
from typing import TYPE_CHECKING, Any, Optional

from stollen import Stollen
from stollen.requests.fields import Header

from .const import TELEGRAM_GATEWAY_PRODUCTION
from .exceptions import TelegramGatewayAPIError

if TYPE_CHECKING:
    from .types import RequestStatus


class TelegramGateway(Stollen):
    def __init__(
        self,
        api_token: str,
        api_url: str = TELEGRAM_GATEWAY_PRODUCTION,
        **stollen_kwargs: Any,
    ) -> None:
        if not isinstance(api_token, str):
            raise TypeError("api_token must be a string!")
        self._api_token = api_token
        super().__init__(
            base_url=api_url,
            global_request_fields=[
                Header(name="Authorization", value=f"Bearer {api_token}"),
            ],
            response_data_key=["result"],
            error_message_key=["error"],
            general_error_class=TelegramGatewayAPIError,
            **stollen_kwargs,
        )

    @property
    def api_token(self) -> str:
        return self._api_token

    def check_signature(self, timestamp: int, signature: str, body_text: str) -> bool:
        data_string: str = f"{timestamp}\n{body_text}"
        generated_signature: HMAC = HMAC(
            key=sha256(string=self.api_token.encode()).digest(),
            msg=data_string.encode(),
            digestmod=sha256,
        )
        return generated_signature.hexdigest() == signature

    async def check_send_ability(self, *, phone_number: str) -> RequestStatus:
        from .methods import CheckSendAbility

        call: CheckSendAbility = CheckSendAbility(phone_number=phone_number)

        return await self(call)

    async def check_verification_status(
        self,
        *,
        request_id: str,
        code: Optional[str] = None,
    ) -> RequestStatus:
        from .methods import CheckVerificationStatus

        call: CheckVerificationStatus = CheckVerificationStatus(
            request_id=request_id,
            code=code,
        )

        return await self(call)

    async def revoke_verification_message(self, *, request_id: str) -> bool:
        from .methods import RevokeVerificationMessage

        call: RevokeVerificationMessage = RevokeVerificationMessage(request_id=request_id)

        return await self(call)

    async def send_verification_message(
        self,
        *,
        phone_number: str,
        request_id: Optional[str] = None,
        sender_username: Optional[str] = None,
        code: Optional[str] = None,
        code_length: Optional[int] = None,
        callback_url: Optional[str] = None,
        payload: Optional[str] = None,
        ttl: Optional[int] = None,
    ) -> RequestStatus:
        from .methods import SendVerificationMessage

        call: SendVerificationMessage = SendVerificationMessage(
            phone_number=phone_number,
            request_id=request_id,
            sender_username=sender_username,
            code=code,
            code_length=code_length,
            callback_url=callback_url,
            payload=payload,
            ttl=ttl,
        )

        return await self(call)
