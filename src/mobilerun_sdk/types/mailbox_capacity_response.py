# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailboxCapacityResponse", "Data"]


class Data(BaseModel):
    included_remaining: int = FieldInfo(alias="includedRemaining")


class MailboxCapacityResponse(BaseModel):
    data: Data
