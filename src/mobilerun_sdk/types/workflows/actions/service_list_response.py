# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import List

__all__ = ["ServiceListResponse"]

class ServiceListResponse(BaseModel):
    data: List[str]