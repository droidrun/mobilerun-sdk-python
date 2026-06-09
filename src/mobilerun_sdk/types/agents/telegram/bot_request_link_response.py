# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BotRequestLinkResponse"]


class BotRequestLinkResponse(BaseModel):
    id: str

    bot_username: str = FieldInfo(alias="botUsername")

    deep_link: str = FieldInfo(alias="deepLink")
