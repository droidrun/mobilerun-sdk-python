# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .proxy_config_param import ProxyConfigParam
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    device_type: Annotated[
        Literal["dedicated_physical_device", "dedicated_premium_device", "dedicated_emulated_device"],
        PropertyInfo(alias="deviceType"),
    ]

    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    name: str

    proxy: ProxyConfigParam
