# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .action_catalog_entry import ActionCatalogEntry

__all__ = ["ActionCatalogRetrieveResponse"]


class ActionCatalogRetrieveResponse(BaseModel):
    data: ActionCatalogEntry
