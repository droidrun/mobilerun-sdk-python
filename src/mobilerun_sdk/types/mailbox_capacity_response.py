# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailboxCapacityResponse", "Data"]


class Data(BaseModel):
    included: int

    included_remaining: int = FieldInfo(alias="includedRemaining")

    remaining: int

    status: Literal["available", "exhausted", "not_included"]


class MailboxCapacityResponse(BaseModel):
    data: Data
