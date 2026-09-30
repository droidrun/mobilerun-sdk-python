# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeviceSummaryResponse"]


class DeviceSummaryResponse(BaseModel):
    by_state: Dict[str, int] = FieldInfo(alias="byState")

    by_type: Dict[str, int] = FieldInfo(alias="byType")

    total: int

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
