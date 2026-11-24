# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    input: Required[Dict[str, object]]

    timeout_s: Annotated[int, PropertyInfo(alias="timeoutS")]
    """Omitted: 300 s."""

    version: Union[Literal["latest"], int]
    """
    Latest selects the newest ready version of the function; a number pins a
    version.
    """

    wait_s: Annotated[int, PropertyInfo(alias="waitS")]
    """Seconds the reply waits for the run to end; 202 when it is still running."""
