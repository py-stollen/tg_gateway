import logging
from typing import Final

import uvicorn
from fastapi import FastAPI

from examples.fastapi_webhook_handler import router
from tg_gateway import TelegramGateway

API_TOKEN: Final[str] = "YOUR_TOKEN_HERE"


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    gateway: TelegramGateway = TelegramGateway(api_token=API_TOKEN, force_detailed_errors=True)

    app: FastAPI = FastAPI()
    app.state.gateway = gateway
    app.include_router(router)

    return uvicorn.run(app=app, host="127.0.0.1", port=8081)


if __name__ == "__main__":
    main()
