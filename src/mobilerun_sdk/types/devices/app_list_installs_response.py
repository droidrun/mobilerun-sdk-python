# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, List

__all__ = ["AppListInstallsResponse", "Install"]

class Install(BaseModel):
    app_id: str = FieldInfo(alias = "appId")
    """Android package name or iOS bundle id"""

    platform: str
    """android or ios"""

    started_at: datetime = FieldInfo(alias = "startedAt")

    status: Literal["running", "succeeded", "failed"]
    """
    On iOS MDM devices, succeeded means the install command was accepted by the
    device's MDM channel, not that the install finished on-device.
    """

    updated_at: datetime = FieldInfo(alias = "updatedAt")

    error_class: Optional[str] = FieldInfo(alias = "errorClass", default = None)
    """Closed set: download_failed, adb_install_failed, panic, timeout, failed.

    Only present when status is failed.
    """

class AppListInstallsResponse(BaseModel):
    installs: Optional[List[Install]] = None

    schema_: Optional[str] = FieldInfo(alias = "$schema", default = None)
    """A URL to the JSON Schema for this object."""