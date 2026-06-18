# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["HookTestResponse"]


class HookTestResponse(BaseModel):
    """Response after attempting test delivery."""

    id: str
    """The hook ID"""

    success: bool
    """Whether delivery succeeded (2xx)"""

    error: Optional[str] = None
    """Error message if delivery failed"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP status from target"""
