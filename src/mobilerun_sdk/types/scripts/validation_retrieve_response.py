# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .validation import Validation

__all__ = ["ValidationRetrieveResponse"]


class ValidationRetrieveResponse(BaseModel):
    data: Validation
