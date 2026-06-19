# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .flow_execution import FlowExecution

__all__ = ["ExecutionRetrieveResponse"]


class ExecutionRetrieveResponse(BaseModel):
    data: FlowExecution
