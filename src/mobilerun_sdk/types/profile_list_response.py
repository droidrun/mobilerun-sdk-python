# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .shared.meta import Meta

__all__ = ["ProfileListResponse"]


class ProfileListResponse(BaseModel):
    items: Optional[List[Profile]] = None

    pagination: Meta

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
