# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

__all__ = ["UiStateListResponse"]

class UiStateListResponse(BaseModel):
    urls: List[str]
    """The list of media URLs"""