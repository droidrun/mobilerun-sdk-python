# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionCreateParams"]


class ActionCreateParams(TypedDict, total=False):
    catalog_entry_id: Required[Annotated[str, PropertyInfo(alias="catalogEntryId")]]

    name: Required[str]

    description: str

    params: Dict[str, Optional[object]]
