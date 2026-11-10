# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumberBindingListCandidatesResponse", "Item"]


class Item(BaseModel):
    id: str

    name: str

    state: Literal["ready"]


class NumberBindingListCandidatesResponse(BaseModel):
    items: Optional[List[Item]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
