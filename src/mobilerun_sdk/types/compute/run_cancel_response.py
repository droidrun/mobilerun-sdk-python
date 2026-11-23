# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .function_run import FunctionRun

__all__ = ["RunCancelResponse"]


class RunCancelResponse(BaseModel):
    data: FunctionRun
