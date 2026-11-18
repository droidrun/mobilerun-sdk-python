# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.pagination import Pagination
from .serverless_function import ServerlessFunction

__all__ = ["FunctionListResponse", "Data"]


class Data(BaseModel):
    items: List[ServerlessFunction]

    pagination: Pagination


class FunctionListResponse(BaseModel):
    data: Data
