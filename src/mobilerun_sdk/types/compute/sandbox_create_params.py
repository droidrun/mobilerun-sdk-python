# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SandboxCreateParams", "APIKey", "APIKeyPermissions", "APIKeyFull", "APIKeyKey"]


class SandboxCreateParams(TypedDict, total=False):
    allowed_hosts: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedHosts")]

    api_key: Annotated[APIKey, PropertyInfo(alias="apiKey")]

    env: Dict[str, str]

    idle_timeout_s: Annotated[int, PropertyInfo(alias="idleTimeoutS")]

    name: str

    timeout_s: Annotated[int, PropertyInfo(alias="timeoutS")]


class APIKeyPermissions(TypedDict, total=False):
    permissions: Required[Dict[str, SequenceNotStr[str]]]


class APIKeyFull(TypedDict, total=False):
    full: Required[Literal[True]]


class APIKeyKey(TypedDict, total=False):
    key: Required[str]


APIKey: TypeAlias = Union[APIKeyPermissions, APIKeyFull, APIKeyKey]
