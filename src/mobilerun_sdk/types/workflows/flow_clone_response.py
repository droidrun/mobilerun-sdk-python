# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..flow import Flow
from ..._models import BaseModel

__all__ = ["FlowCloneResponse"]


class FlowCloneResponse(BaseModel):
    data: Flow
