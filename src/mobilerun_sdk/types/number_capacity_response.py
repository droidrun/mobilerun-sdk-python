# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NumberCapacityResponse", "Data"]


class Data(BaseModel):
    included: int

    included_remaining: int = FieldInfo(alias="includedRemaining")
    """Deprecated — always equal to `remaining`.

    Migrate to `remaining`; this field will be removed in a future revision.
    """

    remaining: int

    status: Literal["available", "exhausted", "not_included"]


class NumberCapacityResponse(BaseModel):
    data: Data
