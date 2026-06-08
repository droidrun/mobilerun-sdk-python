# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["A11YNode", "BoundsInScreen"]


class BoundsInScreen(BaseModel):
    bottom: int

    left: int

    right: int

    top: int


class A11YNode(BaseModel):
    bounds_in_screen: BoundsInScreen = FieldInfo(alias="boundsInScreen")

    children: Optional[List["A11YNode"]] = None

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
