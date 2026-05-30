# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .rect import Rect
from ..._models import BaseModel

__all__ = [
    "StateUiResponse",
    "A11yTree",
    "A11yTreeBoundsInScreen",
    "DeviceContext",
    "DeviceContextDisplayMetrics",
    "DeviceContextFilteringParams",
    "ImeTree",
    "ImeTreeBoundsInScreen",
    "PhoneState",
    "PhoneStateFocusedElement",
]


class A11yTreeBoundsInScreen(BaseModel):
    bottom: int

    left: int

    right: int

    top: int


class A11yTree(BaseModel):
    bounds_in_screen: A11yTreeBoundsInScreen = FieldInfo(alias="boundsInScreen")

    children: Optional[List[object]] = None

    class_name: str = FieldInfo(alias="className")

    content_description: str = FieldInfo(alias="contentDescription")

    is_checkable: bool = FieldInfo(alias="isCheckable")

    is_checked: bool = FieldInfo(alias="isChecked")

    is_clickable: bool = FieldInfo(alias="isClickable")

    is_enabled: bool = FieldInfo(alias="isEnabled")

    is_focusable: bool = FieldInfo(alias="isFocusable")

    is_focused: bool = FieldInfo(alias="isFocused")

    is_long_clickable: bool = FieldInfo(alias="isLongClickable")

    is_password: bool = FieldInfo(alias="isPassword")

    is_scrollable: bool = FieldInfo(alias="isScrollable")

    is_selected: bool = FieldInfo(alias="isSelected")

    package_name: str = FieldInfo(alias="packageName")

    resource_id: str = FieldInfo(alias="resourceId")

    text: str


class DeviceContextDisplayMetrics(BaseModel):
    density: float

    density_dpi: int = FieldInfo(alias="densityDpi")

    height_pixels: int = FieldInfo(alias="heightPixels")

    scaled_density: float = FieldInfo(alias="scaledDensity")

    width_pixels: int = FieldInfo(alias="widthPixels")


class DeviceContextFilteringParams(BaseModel):
    min_element_size: int

    overlay_offset: int


class DeviceContext(BaseModel):
    display_metrics: DeviceContextDisplayMetrics

    filtering_params: DeviceContextFilteringParams

    screen_bounds: Rect


class ImeTreeBoundsInScreen(BaseModel):
    bottom: int

    left: int

    right: int

    top: int


class ImeTree(BaseModel):
    bounds_in_screen: ImeTreeBoundsInScreen = FieldInfo(alias="boundsInScreen")

    children: Optional[List[object]] = None

    class_name: str = FieldInfo(alias="className")

    content_description: str = FieldInfo(alias="contentDescription")

    is_checkable: bool = FieldInfo(alias="isCheckable")

    is_checked: bool = FieldInfo(alias="isChecked")

    is_clickable: bool = FieldInfo(alias="isClickable")

    is_enabled: bool = FieldInfo(alias="isEnabled")

    is_focusable: bool = FieldInfo(alias="isFocusable")

    is_focused: bool = FieldInfo(alias="isFocused")

    is_long_clickable: bool = FieldInfo(alias="isLongClickable")

    is_password: bool = FieldInfo(alias="isPassword")

    is_scrollable: bool = FieldInfo(alias="isScrollable")

    is_selected: bool = FieldInfo(alias="isSelected")

    package_name: str = FieldInfo(alias="packageName")

    resource_id: str = FieldInfo(alias="resourceId")

    text: str


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
    a11y_tree: A11yTree

    device_context: DeviceContext

    ime_tree: ImeTree

    phone_state: PhoneState

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
