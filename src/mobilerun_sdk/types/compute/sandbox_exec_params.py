# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SandboxExecParams"]


class SandboxExecParams(TypedDict, total=False):
    command: Required[str]

    cwd: str

    env: Dict[str, str]

    timeout_s: Annotated[int, PropertyInfo(alias="timeoutS")]

    wait_s: Annotated[int, PropertyInfo(alias="waitS")]
