# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AppListResponse", "AppListResponseItem", "AppListResponseItemAvailableUpdate"]


class AppListResponseItemAvailableUpdate(BaseModel):
    country: str

    version_code: int = FieldInfo(alias="versionCode")

    version_name: str = FieldInfo(alias="versionName")


class AppListResponseItem(BaseModel):
    is_system_app: bool = FieldInfo(alias="isSystemApp")

    label: str

    package_name: str = FieldInfo(alias="packageName")

    version_code: int = FieldInfo(alias="versionCode")

    version_name: str = FieldInfo(alias="versionName")

    available_update: Optional[AppListResponseItemAvailableUpdate] = FieldInfo(alias="availableUpdate", default=None)


AppListResponse: TypeAlias = List[AppListResponseItem]
