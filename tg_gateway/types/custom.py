import sys
from datetime import datetime, timezone
from typing import Annotated

from pydantic import PlainSerializer

# Serializer source: https://github.com/aiogram/aiogram
if sys.platform == "win32":

    def _datetime_serializer(value: datetime) -> int:
        tz: timezone = timezone.utc if value.tzinfo else None
        return round((value - datetime(1970, 1, 1, tzinfo=tz)).total_seconds())

else:

    def _datetime_serializer(value: datetime) -> int:
        return round(value.timestamp())


# Make datetime compatible with Telegram Bot API (unixtime)
DateTime = Annotated[
    datetime,
    PlainSerializer(
        func=_datetime_serializer,
        return_type=int,
        when_used="unless-none",
    ),
]
