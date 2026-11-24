# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .function_source import FunctionSource

__all__ = ["FunctionSourceResponse"]


class FunctionSourceResponse(BaseModel):
    data: FunctionSource
