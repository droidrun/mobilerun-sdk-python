# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .flow_action import FlowAction

__all__ = ["ActionAddResponse"]


class ActionAddResponse(BaseModel):
    data: FlowAction
