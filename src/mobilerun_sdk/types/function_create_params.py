# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["FunctionCreateParams", "APIKey", "APIKeyPermissions", "APIKeyFull", "Manifest", "ManifestCredential"]


class FunctionCreateParams(TypedDict, total=False):
    name: Required[str]

    source: Required[str]

    api_key: Annotated[APIKey, PropertyInfo(alias="apiKey")]

    description: str

    manifest: Manifest


class APIKeyPermissions(TypedDict, total=False):
    permissions: Required[Dict[str, SequenceNotStr[str]]]


class APIKeyFull(TypedDict, total=False):
    full: Required[Literal[True]]


APIKey: TypeAlias = Union[APIKeyPermissions, APIKeyFull]


class ManifestCredential(TypedDict, total=False):
    name: Required[str]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]


class Manifest(TypedDict, total=False):
    credentials: Iterable[ManifestCredential]

    hosts: SequenceNotStr[str]

    scopes: SequenceNotStr[str]
