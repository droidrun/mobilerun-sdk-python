# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..compute.function_run import FunctionRun

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    data: FunctionRun
