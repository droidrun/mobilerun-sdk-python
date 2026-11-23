# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .function_version import FunctionVersion

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    data: Optional[FunctionVersion] = None
