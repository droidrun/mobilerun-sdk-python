# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from .._utils import PropertyInfo

from typing import Union

from datetime import datetime

__all__ = ["DeviceTerminateParams"]

class DeviceTerminateParams(TypedDict, total=False):
    previous_device_id: Annotated[str, PropertyInfo(alias="previousDeviceId")]

    terminate_at: Annotated[Union[str, datetime], PropertyInfo(alias="terminateAt", format = "iso8601")]