# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AppInstallParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    bundle_id: Required[Annotated[str, PropertyInfo(alias="bundleId")]]
    """iOS bundle identifier (e.g. com.example.app)"""

    package_name: Annotated[str, PropertyInfo(alias="packageName")]
    """Android package name (e.g. com.example.app)"""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]


class Variant1(TypedDict, total=False):
    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]
    """Android package name (e.g. com.example.app)"""

    bundle_id: Annotated[str, PropertyInfo(alias="bundleId")]
    """iOS bundle identifier (e.g. com.example.app)"""

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]


AppInstallParams: TypeAlias = Union[Variant0, Variant1]
