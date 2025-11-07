# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppListResponse", "App"]


class App(BaseModel):
    id: str

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    created_at: Optional[date] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    developer_name: Optional[str] = FieldInfo(alias="developerName", default=None)

    display_name: str = FieldInfo(alias="displayName")

    external_ids: Optional[List[str]] = FieldInfo(alias="externalIds", default=None)

    icon_url: str = FieldInfo(alias="iconURL")

    package_name: str = FieldInfo(alias="packageName")

    queued_at: Optional[date] = FieldInfo(alias="queuedAt", default=None)

    rating_count: Optional[int] = FieldInfo(alias="ratingCount", default=None)

    rating_score: Optional[str] = FieldInfo(alias="ratingScore", default=None)

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)

    source: Literal["uploaded", "store"]

    target_sdk: Optional[int] = FieldInfo(alias="targetSdk", default=None)

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    version_code: Optional[int] = FieldInfo(alias="versionCode", default=None)

    version_name: str = FieldInfo(alias="versionName")


class AppListResponse(BaseModel):
    apps: List[App]

    available_count: float = FieldInfo(alias="availableCount")

    queued_count: float = FieldInfo(alias="queuedCount")

    store_count: float = FieldInfo(alias="storeCount")

    total_count: float = FieldInfo(alias="totalCount")

    upload_count: float = FieldInfo(alias="uploadCount")
