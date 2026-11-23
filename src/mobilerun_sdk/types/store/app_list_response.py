# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_store_app import PublicStoreApp
from ..shared.pagination import Pagination

__all__ = ["AppListResponse"]


class AppListResponse(BaseModel):
    items: List[PublicStoreApp]

    pagination: Pagination
