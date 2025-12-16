# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    x_user_id: Required[Annotated[str, PropertyInfo(alias="X-User-ID")]]

    include_system_apps: Annotated[bool, PropertyInfo(alias="includeSystemApps")]
