# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionCatalogRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    device_free: bool = FieldInfo(alias="deviceFree")
    """
    True when this step itself runs without a device; only such steps may appear in
    a device-free flow. Not the same as cloudRoutine: a device-free step can still
    be device-routine-only (see cloudRoutineReason).
    """

    method: str

    name: str

    provider: Literal["mobilerun", "oneDrive", "googleDrive"]

    service: Literal["tasks_api", "devices_api", "agents_api", "webhooks", "integrations_api", "triggers_api"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    cloud_routine: Optional[bool] = FieldInfo(alias="cloudRoutine", default=None)
    """True when this step is allowed in a cloud agent routine.

    Present only for profile=agent_routine. False does not mean the step needs a
    device; read cloudRoutineReason.
    """

    cloud_routine_reason: Optional[Literal["needs_device", "device_routine_only"]] = FieldInfo(
        alias="cloudRoutineReason", default=None
    )
    """
    Why cloudRoutine is false: needs_device (the step needs a device),
    device_routine_only (allowed only in device routines; the step itself does not
    need a device). Present only when cloudRoutine is false.
    """

    output_schema: Optional[object] = FieldInfo(alias="outputSchema", default=None)

    params_schema: Optional[object] = FieldInfo(alias="paramsSchema", default=None)


class ActionCatalogRetrieveResponse(BaseModel):
    data: Data
