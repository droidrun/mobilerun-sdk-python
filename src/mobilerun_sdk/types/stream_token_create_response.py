# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StreamTokenCreateResponse"]


class StreamTokenCreateResponse(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    key: str

    key_id: str = FieldInfo(alias="keyId")
