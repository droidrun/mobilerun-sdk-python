# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppCreateSignedUploadURLParams", "File"]


class AppCreateSignedUploadURLParams(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]

    files: Required[Iterable[File]]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]

    size_bytes: Required[Annotated[float, PropertyInfo(alias="sizeBytes")]]

    target_sdk: Required[Annotated[float, PropertyInfo(alias="targetSdk")]]

    version_code: Required[Annotated[float, PropertyInfo(alias="versionCode")]]

    version_name: Required[Annotated[str, PropertyInfo(alias="versionName")]]

    category_name: Annotated[str, PropertyInfo(alias="categoryName")]

    country: str
    """Country code for Search Results"""

    description: str

    developer_name: Annotated[str, PropertyInfo(alias="developerName")]

    icon_url: Annotated[str, PropertyInfo(alias="iconURL")]

    rating_count: Annotated[float, PropertyInfo(alias="ratingCount")]

    rating_score: Annotated[float, PropertyInfo(alias="ratingScore")]


class File(TypedDict, total=False):
    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
