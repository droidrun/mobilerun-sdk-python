# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["WebhookListResponse", "Counts", "Item", "ItemIntegration", "ItemIntegrationCapability"]


class Counts(BaseModel):
    active: float

    blocked: float

    disabled: float

    failing: float

    total: float


class ItemIntegrationCapability(BaseModel):
    id: str

    revision: int


class ItemIntegration(BaseModel):
    """Integration target; null for `http` webhooks."""

    args: Dict[str, object]

    capability: ItemIntegrationCapability

    label: str
    """Target name at creation time, e.g. `#ops`."""


class Item(BaseModel):
    id: str

    blocked_at: Optional[str] = FieldInfo(alias="blockedAt", default=None)

    blocked_reason: Optional[str] = FieldInfo(alias="blockedReason", default=None)
    """Why the webhook was blocked, e.g.

    `integration_disconnected` (reconnect the integration) or
    `integration_target_invalid` (the channel is gone or not allowed).
    """

    created_at: str = FieldInfo(alias="createdAt")

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Id of the actor who created this endpoint. Null when no creator was recorded."""

    description: Optional[str] = None

    event_types: List[str] = FieldInfo(alias="eventTypes")

    health: Literal["healthy", "failing", "blocked"]
    """System-observed delivery health.

    `blocked` endpoints are auto-disabled after sustained failure; PATCH
    state=ACTIVE to re-enable.
    """

    integration: Optional[ItemIntegration] = None
    """Integration target; null for `http` webhooks."""

    kind: Literal["http", "integration"]
    """
    `http` posts signed JSON to `url`; `integration` posts a message through a
    connected integration (e.g. a Slack channel).
    """

    signing_enabled: bool = FieldInfo(alias="signingEnabled")
    """Always false for `integration` webhooks."""

    state: Literal["ACTIVE", "DISABLED", "DELETED"]

    updated_at: str = FieldInfo(alias="updatedAt")

    url: Optional[str] = None
    """Delivery URL; null for `integration` webhooks."""


class WebhookListResponse(BaseModel):
    counts: Counts

    items: List[Item]

    pagination: Pagination
