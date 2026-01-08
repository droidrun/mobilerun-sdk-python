# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "StateUiResponse",
    "DeviceContext",
    "DeviceContextDisplayMetrics",
    "DeviceContextFilteringParams",
    "DeviceContextScreenBounds",
    "DeviceContextScreenSize",
    "PhoneState",
    "PhoneStateFocusedElement",
]


class DeviceContextDisplayMetrics(BaseModel):
    density: float

    density_dpi: int = FieldInfo(alias="densityDpi")

    height_pixels: int = FieldInfo(alias="heightPixels")

    scaled_density: float = FieldInfo(alias="scaledDensity")

    width_pixels: int = FieldInfo(alias="widthPixels")


class DeviceContextFilteringParams(BaseModel):
    min_element_size: int

    overlay_offset: int


class DeviceContextScreenBounds(BaseModel):
    height: int

    width: int


class DeviceContextScreenSize(BaseModel):
    height: int

    width: int


class DeviceContext(BaseModel):
    display_metrics: DeviceContextDisplayMetrics

    filtering_params: DeviceContextFilteringParams

    screen_bounds: DeviceContextScreenBounds

    screen_size: DeviceContextScreenSize = FieldInfo(alias="screenSize")


class PhoneStateFocusedElement(BaseModel):
    class_name: Optional[str] = FieldInfo(alias="className", default=None)

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)

    text: Optional[str] = None


class PhoneState(BaseModel):
    is_editable: bool = FieldInfo(alias="isEditable")

    keyboard_visible: bool = FieldInfo(alias="keyboardVisible")

    activity_name: Optional[str] = FieldInfo(alias="activityName", default=None)

    current_app: Optional[str] = FieldInfo(alias="currentApp", default=None)

    focused_element: Optional[PhoneStateFocusedElement] = FieldInfo(alias="focusedElement", default=None)

    package_name: Optional[str] = FieldInfo(alias="packageName", default=None)


class StateUiResponse(BaseModel):
    a11y_tree: "ElementNode"

    device_context: DeviceContext

    phone_state: PhoneState

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""


from ..element_node import ElementNode
