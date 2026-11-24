# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .function_validation import FunctionValidation

__all__ = ["ValidationCreateResponse"]


class ValidationCreateResponse(BaseModel):
    data: FunctionValidation
