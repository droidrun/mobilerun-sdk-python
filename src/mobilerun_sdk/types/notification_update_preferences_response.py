# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from pydantic import Field as FieldInfo

__all__ = ["NotificationUpdatePreferencesResponse", "Data"]

class Data(BaseModel):
    muted_types: List[str] = FieldInfo(alias = "mutedTypes")

class NotificationUpdatePreferencesResponse(BaseModel):
    data: Data