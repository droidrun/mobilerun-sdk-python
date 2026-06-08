# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Flow"]


class Flow(BaseModel):
    id: str

    cooldown_scope: Literal["flow", "device"] = FieldInfo(alias="cooldownScope")

    cooldown_seconds: Optional[int] = FieldInfo(alias="cooldownSeconds", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    enabled: bool

    last_triggered_at: Optional[str] = FieldInfo(alias="lastTriggeredAt", default=None)

    name: str

    trigger_id: str = FieldInfo(alias="triggerId")

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
