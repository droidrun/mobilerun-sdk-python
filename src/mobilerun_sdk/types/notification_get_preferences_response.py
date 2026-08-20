# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NotificationGetPreferencesResponse", "Data"]


class Data(BaseModel):
    muted_types: List[str] = FieldInfo(alias="mutedTypes")


class NotificationGetPreferencesResponse(BaseModel):
    data: Data
