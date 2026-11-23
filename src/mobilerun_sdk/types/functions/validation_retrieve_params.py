# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ValidationRetrieveParams"]


class ValidationRetrieveParams(TypedDict, total=False):
    wait_s: Annotated[Optional[int], PropertyInfo(alias="waitS")]
    """Wait up to 25 seconds for validation to finish.

    Excess waiters return immediately.
    """
