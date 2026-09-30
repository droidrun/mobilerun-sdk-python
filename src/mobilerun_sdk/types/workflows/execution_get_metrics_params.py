# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExecutionGetMetricsParams"]


class ExecutionGetMetricsParams(TypedDict, total=False):
    flow_id: Annotated[str, PropertyInfo(alias="flowId")]

    from_: Annotated[Union[str, datetime, None], PropertyInfo(alias="from", format="iso8601")]

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    trigger_id: Annotated[str, PropertyInfo(alias="triggerId")]
