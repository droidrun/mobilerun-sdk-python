# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FlowCapacityResponse", "Data"]


class Data(BaseModel):
    included: int

    remaining: int

    status: Literal["available", "exhausted", "not_included"]


class FlowCapacityResponse(BaseModel):
    data: Data
