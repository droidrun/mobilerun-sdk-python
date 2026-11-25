# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ScheduledRunCreateParams"]


class ScheduledRunCreateParams(TypedDict, total=False):
    run_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="runAt", format="iso8601")]]
    """RFC 3339 time with an offset; between one minute and 365 days from now."""

    payload: Dict[str, object]
