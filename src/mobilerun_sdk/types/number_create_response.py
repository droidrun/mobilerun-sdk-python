# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NumberCreateResponse", "Data"]


class Data(BaseModel):
    checkout_url: Optional[str] = FieldInfo(alias="checkoutUrl", default=None)

    number_id: str = FieldInfo(alias="numberId")

    state: Literal["awaiting_payment", "provisioning"]


class NumberCreateResponse(BaseModel):
    data: Data
