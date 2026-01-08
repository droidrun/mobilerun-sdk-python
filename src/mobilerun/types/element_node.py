# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ElementNode", "BoundsInParent", "BoundsInScreen", "CollectionInfo", "CollectionItemInfo", "RangeInfo"]


class BoundsInParent(BaseModel):
    bottom: int

    left: int

    right: int

    top: int


class BoundsInScreen(BaseModel):
    bottom: int

    left: int

    right: int

    top: int


class CollectionInfo(BaseModel):
    column_count: int = FieldInfo(alias="columnCount")

    is_hierarchical: bool = FieldInfo(alias="isHierarchical")

    row_count: int = FieldInfo(alias="rowCount")

    selection_mode: int = FieldInfo(alias="selectionMode")


class CollectionItemInfo(BaseModel):
    column_index: int = FieldInfo(alias="columnIndex")

    column_span: int = FieldInfo(alias="columnSpan")

    is_heading: bool = FieldInfo(alias="isHeading")

    is_selected: bool = FieldInfo(alias="isSelected")

    row_index: int = FieldInfo(alias="rowIndex")

    row_span: int = FieldInfo(alias="rowSpan")


class RangeInfo(BaseModel):
    current: int

    max: int

    min: int

    type: int


class ElementNode(BaseModel):
    action_count: int = FieldInfo(alias="actionCount")

    action_list: Optional[List[str]] = FieldInfo(alias="actionList", default=None)

    bounds_in_parent: BoundsInParent = FieldInfo(alias="boundsInParent")

    bounds_in_screen: BoundsInScreen = FieldInfo(alias="boundsInScreen")

    child_count: int = FieldInfo(alias="childCount")

    children: Optional[List["ElementNode"]] = None

    class_name: str = FieldInfo(alias="className")

    collection_info: CollectionInfo = FieldInfo(alias="collectionInfo")

    collection_item_info: CollectionItemInfo = FieldInfo(alias="collectionItemInfo")

    container_title: str = FieldInfo(alias="containerTitle")

    content_description: str = FieldInfo(alias="contentDescription")

    drawing_order: int = FieldInfo(alias="drawingOrder")

    error: str

    extras: Dict[str, object]

    has_labeled_by: bool = FieldInfo(alias="hasLabeledBy")

    has_label_for: bool = FieldInfo(alias="hasLabelFor")

    has_touch_delegate: bool = FieldInfo(alias="hasTouchDelegate")

    has_traversal_after: bool = FieldInfo(alias="hasTraversalAfter")

    has_traversal_before: bool = FieldInfo(alias="hasTraversalBefore")

    hint: str

    input_type: int = FieldInfo(alias="inputType")

    is_accessibility_focused: bool = FieldInfo(alias="isAccessibilityFocused")

    is_checkable: bool = FieldInfo(alias="isCheckable")

    is_checked: bool = FieldInfo(alias="isChecked")

    is_clickable: bool = FieldInfo(alias="isClickable")

    is_context_clickable: bool = FieldInfo(alias="isContextClickable")

    is_dismissable: bool = FieldInfo(alias="isDismissable")

    is_editable: bool = FieldInfo(alias="isEditable")

    is_enabled: bool = FieldInfo(alias="isEnabled")

    is_focusable: bool = FieldInfo(alias="isFocusable")

    is_focused: bool = FieldInfo(alias="isFocused")

    is_heading: bool = FieldInfo(alias="isHeading")

    is_important_for_accessibility: bool = FieldInfo(alias="isImportantForAccessibility")

    is_long_clickable: bool = FieldInfo(alias="isLongClickable")

    is_multi_line: bool = FieldInfo(alias="isMultiLine")

    is_password: bool = FieldInfo(alias="isPassword")

    is_screen_reader_focusable: bool = FieldInfo(alias="isScreenReaderFocusable")

    is_scrollable: bool = FieldInfo(alias="isScrollable")

    is_selected: bool = FieldInfo(alias="isSelected")

    is_showing_hint_text: bool = FieldInfo(alias="isShowingHintText")

    is_text_selectable: bool = FieldInfo(alias="isTextSelectable")

    is_visible_to_user: bool = FieldInfo(alias="isVisibleToUser")

    live_region: bool = FieldInfo(alias="liveRegion")

    max_text_length: int = FieldInfo(alias="maxTextLength")

    movement_granularities: int = FieldInfo(alias="movementGranularities")

    pane_title: str = FieldInfo(alias="paneTitle")

    range_info: RangeInfo = FieldInfo(alias="rangeInfo")

    resource_id: str = FieldInfo(alias="resourceId")

    state_description: str = FieldInfo(alias="stateDescription")

    text: str

    text_selection_end: int = FieldInfo(alias="textSelectionEnd")

    text_selection_start: int = FieldInfo(alias="textSelectionStart")

    tooltip_text: str = FieldInfo(alias="tooltipText")

    touch_delegate_region_count: int = FieldInfo(alias="touchDelegateRegionCount")

    unique_id: str = FieldInfo(alias="uniqueId")

    window_id: int = FieldInfo(alias="windowId")
