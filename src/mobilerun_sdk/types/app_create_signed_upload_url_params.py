# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from .._utils import PropertyInfo

from typing import Iterable

__all__ = ["AppCreateSignedUploadURLParams", "File"]

class AppCreateSignedUploadURLParams(TypedDict, total=False):
    bundle_id: Required[Annotated[str, PropertyInfo(alias="bundleId")]]

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]

    files: Required[Iterable[File]]

    version_code: Required[Annotated[float, PropertyInfo(alias="versionCode")]]

    version_name: Required[Annotated[str, PropertyInfo(alias="versionName")]]

    country: str
    """Country code for Search Results"""

    description: str

    developer_name: Annotated[str, PropertyInfo(alias="developerName")]

    icon_url: Annotated[str, PropertyInfo(alias="iconURL")]

    platform: Literal["android", "ios"]

    target_sdk: Annotated[float, PropertyInfo(alias="targetSdk")]

class File(TypedDict, total=False):
    content_type: Required[Annotated[Literal["application/vnd.android.package-archive", "application/octet-stream", "application/zip"], PropertyInfo(alias="contentType")]]

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]

    sha256: str