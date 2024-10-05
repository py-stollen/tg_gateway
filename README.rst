
##########
tg_gateway
##########

**tg_gateway** is a Python library for interacting with the
`Telegram Gateway API <https://core.telegram.org/gateway>`_

Installation
------------

..  code-block:: bash

    pip install -U tg_gateway

Usage example
--------------

.. code-block:: python

    import asyncio
    import logging
    from typing import Final

    from tg_gateway import TelegramGateway

    API_TOKEN: Final[str] = "YOUR_TOKEN_HERE"


    async def main() -> None:
        logging.basicConfig(level=logging.DEBUG)
        gateway: TelegramGateway = TelegramGateway(api_token=API_TOKEN, force_detailed_errors=True)
        result = await gateway.send_verification_message(
            phone_number="+88812956932",
            code_length=8,
            callback_url="https://example.com",
        )
        logging.info(result)
        await gateway.session.close()


    if __name__ == "__main__":
        asyncio.run(main())


Contact
-------
For any questions or feedback, feel free to reach out to me on my `Telegram <https://t.me/wakaree>`_
