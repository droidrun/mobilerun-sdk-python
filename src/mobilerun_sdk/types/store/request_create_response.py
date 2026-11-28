# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RequestCreateResponse"]


class RequestCreateResponse(BaseModel):
    delivered: Literal["ticket", "event"]

    ticket_number: Optional[int] = FieldInfo(alias="ticketNumber", default=None)
