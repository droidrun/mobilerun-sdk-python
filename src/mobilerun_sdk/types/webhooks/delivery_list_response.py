# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["DeliveryListResponse", "Item"]


class Item(BaseModel):
    id: str

    attempts: float

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)

    created_at: str = FieldInfo(alias="createdAt")

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Id of the parent endpoint's creator.

    Null when the endpoint row is gone or its creator was never recorded.
    """

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    endpoint_id: str = FieldInfo(alias="endpointId")

    endpoint_url: str = FieldInfo(alias="endpointUrl")

    event_id: str = FieldInfo(alias="eventId")

    event_type: str = FieldInfo(alias="eventType")

    is_test: bool = FieldInfo(alias="isTest")

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    last_status_code: Optional[float] = FieldInfo(alias="lastStatusCode", default=None)

    occurred_at: str = FieldInfo(alias="occurredAt")

    source: str

    status: Literal["pending", "success", "skipped", "dead"]


class DeliveryListResponse(BaseModel):
    items: List[Item]

    pagination: Pagination
