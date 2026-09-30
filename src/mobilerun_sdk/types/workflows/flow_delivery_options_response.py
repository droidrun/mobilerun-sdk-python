# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowDeliveryOptionsResponse", "Data", "DataDestination", "DataDirectUploadStep"]


class DataDestination(BaseModel):
    connection: Literal["connected", "not_connected", "expired", "unknown"]

    connect_key: str = FieldInfo(alias="connectKey")

    icon_url: Optional[str] = FieldInfo(alias="iconUrl", default=None)

    key: Literal["one_drive", "google_drive"]

    label: str


class DataDirectUploadStep(BaseModel):
    flow_action_id: str = FieldInfo(alias="flowActionId")

    name: str


class Data(BaseModel):
    can_deliver_recording: bool = FieldInfo(alias="canDeliverRecording")

    destinations: List[DataDestination]
    """Delivery destinations in registry order."""

    direct_upload_step: Optional[DataDirectUploadStep] = FieldInfo(alias="directUploadStep", default=None)

    has_files_upload: bool = FieldInfo(alias="hasFilesUpload")

    recording_mode: Literal["off", "flow", "selected_steps"] = FieldInfo(alias="recordingMode")


class FlowDeliveryOptionsResponse(BaseModel):
    data: Data
