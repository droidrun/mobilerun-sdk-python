# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing_extensions import Literal

__all__ = ["AppDeleteResponse"]

class AppDeleteResponse(BaseModel):
    message: str

    success: Literal[True]