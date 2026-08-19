# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

__all__ = ["PackageCreateParams"]

class PackageCreateParams(TypedDict, total=False):
    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]