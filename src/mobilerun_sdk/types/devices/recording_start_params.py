# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["RecordingStartParams"]


class RecordingStartParams(TypedDict, total=False):
    name: str

    retention_days: Annotated[int, PropertyInfo(alias="retentionDays")]

    types: Optional[SequenceNotStr[str]]
