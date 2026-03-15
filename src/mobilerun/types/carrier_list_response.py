# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .carrier import Carrier
from .._models import BaseModel
from .shared.meta import Meta

__all__ = ["CarrierListResponse"]


class CarrierListResponse(BaseModel):
    items: Optional[List[Carrier]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
