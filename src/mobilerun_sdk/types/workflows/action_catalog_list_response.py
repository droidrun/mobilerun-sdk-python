# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.pagination import Pagination
from .action_catalog_entry import ActionCatalogEntry

__all__ = ["ActionCatalogListResponse"]


class ActionCatalogListResponse(BaseModel):
    items: List[ActionCatalogEntry]

    pagination: Pagination
