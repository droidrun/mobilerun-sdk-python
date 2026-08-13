# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeliveryRetrieveAttemptsResponse", "Data", "DataAttempt"]


class DataAttempt(BaseModel):
    attempt_no: float = FieldInfo(alias="attemptNo")

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    error: Optional[str] = None

    request_body: Optional[str] = FieldInfo(alias="requestBody", default=None)

    request_headers: Optional[Dict[str, str]] = FieldInfo(alias="requestHeaders", default=None)

    request_method: str = FieldInfo(alias="requestMethod")

    request_url: str = FieldInfo(alias="requestUrl")

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)

    response_snippet: Optional[str] = FieldInfo(alias="responseSnippet", default=None)

    response_status: Optional[float] = FieldInfo(alias="responseStatus", default=None)

    sent_at: str = FieldInfo(alias="sentAt")

    signed: bool


class Data(BaseModel):
    id: str

    attempts: List[DataAttempt]

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)

    created_at: str = FieldInfo(alias="createdAt")

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """Id of the parent endpoint's creator.

    Null when the endpoint row is gone or its creator was never recorded.
    """

    duration_ms: Optional[float] = FieldInfo(alias="durationMs", default=None)

    endpoint_id: str = FieldInfo(alias="endpointId")

    event_id: str = FieldInfo(alias="eventId")

    event_type: str = FieldInfo(alias="eventType")

    is_test: bool = FieldInfo(alias="isTest")

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    last_status_code: Optional[float] = FieldInfo(alias="lastStatusCode", default=None)

    occurred_at: str = FieldInfo(alias="occurredAt")

    source: str

    status: Literal["pending", "success", "skipped", "dead"]


class DeliveryRetrieveAttemptsResponse(BaseModel):
    data: Data
