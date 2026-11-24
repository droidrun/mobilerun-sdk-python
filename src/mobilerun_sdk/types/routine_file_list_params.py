# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutineFileListParams"]


class RoutineFileListParams(TypedDict, total=False):
    execution_id: Annotated[str, PropertyInfo(alias="executionId")]

    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    folder: str
    """Exact folder (canonicalized: "//" collapsed, trailing "/" stripped)."""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
