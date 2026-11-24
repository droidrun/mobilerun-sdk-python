# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RunLogsResponse", "Data"]


class Data(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    url: str


class RunLogsResponse(BaseModel):
    data: Data
