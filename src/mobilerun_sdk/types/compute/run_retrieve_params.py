# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RunRetrieveParams"]


class RunRetrieveParams(TypedDict, total=False):
    wait_s: Annotated[Optional[int], PropertyInfo(alias="waitS")]
    """Seconds the reply waits for the run to end; 202 when it is still running."""
