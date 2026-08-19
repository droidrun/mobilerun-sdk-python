# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from pydantic import Field as FieldInfo

from typing_extensions import Literal

__all__ = ["WebhookRotateSecretResponse", "Data"]

class Data(BaseModel):
    id: str

    blocked_at: Optional[str] = FieldInfo(alias = "blockedAt", default = None)

    blocked_reason: Optional[str] = FieldInfo(alias = "blockedReason", default = None)

    created_at: str = FieldInfo(alias = "createdAt")

    created_by: Optional[str] = FieldInfo(alias = "createdBy", default = None)
    """Id of the actor who created this endpoint. Null when no creator was recorded."""

    description: Optional[str] = None

    event_types: List[str] = FieldInfo(alias = "eventTypes")

    health: Literal["healthy", "failing", "blocked"]
    """System-observed delivery health.

    `blocked` endpoints are auto-disabled after sustained failure; PATCH
    state=ACTIVE to re-enable.
    """

    secret: str
    """Signing secret — shown only once. Store it now."""

    signing_enabled: bool = FieldInfo(alias = "signingEnabled")

    state: Literal["ACTIVE", "DISABLED", "DELETED"]

    updated_at: str = FieldInfo(alias = "updatedAt")

    url: str

class WebhookRotateSecretResponse(BaseModel):
    data: Data