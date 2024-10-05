from __future__ import annotations

import logging
from typing import Annotated, Any, Final

from fastapi import APIRouter, Body, Header, HTTPException, Request, status

from tg_gateway import TelegramGateway
from tg_gateway.types import RequestStatus

router: Final[APIRouter] = APIRouter()
logger: Final[logging.Logger] = logging.getLogger(name=__name__)


@router.post("/webhook/gateway")
async def accept_report_delivery(
    request: Request,
    x_request_timestamp: Annotated[int, Header()],
    x_request_signature: Annotated[str, Header()],
    data: Annotated[RequestStatus, Body()],
) -> Any:
    gateway: TelegramGateway = request.app.state.gateway
    if not gateway.check_signature(
        timestamp=x_request_timestamp,
        signature=x_request_signature,
        body_text=(await request.body()).decode(),
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid signature provided!",
        )
    logger.info("Received report delivery: %s", data)
