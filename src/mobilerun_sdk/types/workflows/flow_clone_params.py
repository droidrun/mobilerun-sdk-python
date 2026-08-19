# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["FlowCloneParams"]

class FlowCloneParams(TypedDict, total=False):
    device_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceIds")]

    name: str