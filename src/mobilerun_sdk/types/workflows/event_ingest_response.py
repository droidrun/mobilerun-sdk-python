# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

__all__ = ["EventIngestResponse"]

class EventIngestResponse(BaseModel):
    event_id: str = FieldInfo(alias = "eventId")