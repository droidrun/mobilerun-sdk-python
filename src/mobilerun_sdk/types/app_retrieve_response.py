# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    bundle_id: str = FieldInfo(alias="bundleId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    developer_name: Optional[str] = FieldInfo(alias="developerName", default=None)

    display_name: str = FieldInfo(alias="displayName")

    icon_url: str = FieldInfo(alias="iconURL")

    platform: Literal["android", "ios"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class AppRetrieveResponse(BaseModel):
    data: Data
