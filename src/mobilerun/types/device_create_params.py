# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DeviceCreateParams", "Proxy"]


class DeviceCreateParams(TypedDict, total=False):
    device_type: Annotated[
        Literal["device_slot", "dedicated_emulated_device", "dedicated_physical_device"],
        PropertyInfo(alias="deviceType"),
    ]

    provider: Literal["limrun", "remote", "roidrun"]

    apps: Optional[SequenceNotStr[str]]

    country: str

    files: Optional[SequenceNotStr[str]]

    name: str

    proxy: Proxy


class Proxy(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]
