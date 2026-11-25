# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IdentityMeResponse"]


class IdentityMeResponse(BaseModel):
    auth_method: Literal["api_key", "session"] = FieldInfo(alias="authMethod")

    owner_id: str = FieldInfo(alias="ownerId")

    user_id: str = FieldInfo(alias="userId")

    api_key_id: Optional[str] = FieldInfo(alias="apiKeyId", default=None)
