# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from ..._utils import PropertyInfo

__all__ = ["ActionCatalogListParams"]

class ActionCatalogListParams(TypedDict, total=False):
    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks"]