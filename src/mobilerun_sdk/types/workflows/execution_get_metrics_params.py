# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

from typing import Optional

__all__ = ["ExecutionGetMetricsParams"]

class ExecutionGetMetricsParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]

    to: Optional[str]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]