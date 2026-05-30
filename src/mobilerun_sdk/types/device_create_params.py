# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .proxy_config_param import ProxyConfigParam
from .shared_params.location import Location
from .shared_params.device_carrier import DeviceCarrier
from .shared_params.device_identifiers import DeviceIdentifiers

__all__ = ["DeviceCreateParams"]


class DeviceCreateParams(TypedDict, total=False):
    query_country: Annotated[str, PropertyInfo(alias="country")]
    """ISO 3166-1 alpha-2 country code.

    If omitted the system picks the country with the most availability.
    """

    device_type: Annotated[
        Literal["dedicated_physical_device", "dedicated_premium_device", "dedicated_ios_device"],
        PropertyInfo(alias="deviceType"),
    ]

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """Profile ID to use as device spec"""

    android_version: Annotated[int, PropertyInfo(alias="androidVersion")]

    apps: Optional[SequenceNotStr[str]]

    carrier: DeviceCarrier

    body_country: Annotated[str, PropertyInfo(alias="country")]

    files: Optional[SequenceNotStr[str]]

    identifiers: DeviceIdentifiers

    locale: str

    location: Location

    name: str

    proxy: ProxyConfigParam

    timezone: str
