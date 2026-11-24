# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .serverless_function import ServerlessFunction

__all__ = ["FunctionRetrieveResponse"]


class FunctionRetrieveResponse(BaseModel):
    data: ServerlessFunction
