# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailboxCapacityResponse", "Data"]


class Data(BaseModel):
    included: Optional[int] = None
    """null with status unlimited"""

    included_remaining: Optional[int] = FieldInfo(alias="includedRemaining", default=None)
    """null with status unlimited"""

    remaining: Optional[int] = None
    """null with status unlimited"""

    status: Literal["available", "exhausted", "not_included", "unlimited"]


class MailboxCapacityResponse(BaseModel):
    data: Data
