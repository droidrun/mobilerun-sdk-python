# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExecutionGetMetricsParams"]


class ExecutionGetMetricsParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    to: Optional[str]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
