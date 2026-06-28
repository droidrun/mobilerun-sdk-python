# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .flow_action import FlowAction

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    data: List[FlowAction]
