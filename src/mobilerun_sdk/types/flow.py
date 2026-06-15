# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Flow"]


class Flow(BaseModel):
    id: str

    blocked_at: Optional[str] = FieldInfo(alias="blockedAt", default=None)

    consecutive_failures: int = FieldInfo(alias="consecutiveFailures")

    cooldown_scope: Literal["flow", "device"] = FieldInfo(alias="cooldownScope")

    cooldown_seconds: Optional[int] = FieldInfo(alias="cooldownSeconds", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    enabled: bool

    last_failure_at: Optional[str] = FieldInfo(alias="lastFailureAt", default=None)

    last_failure_code: Optional[
        Literal["device_not_found", "permission_denied", "client_error", "transient", "logic"]
    ] = FieldInfo(alias="lastFailureCode", default=None)

    last_triggered_at: Optional[str] = FieldInfo(alias="lastTriggeredAt", default=None)

    name: str

    status: Literal["healthy", "failing", "blocked"]

    trigger_id: str = FieldInfo(alias="triggerId")

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")
