# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ScriptCreateParams", "Manifest", "ManifestCredential"]


class ScriptCreateParams(TypedDict, total=False):
    name: Required[str]

    source: Required[str]

    description: str

    manifest: Manifest


class ManifestCredential(TypedDict, total=False):
    name: Required[str]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]


class Manifest(TypedDict, total=False):
    credentials: Iterable[ManifestCredential]

    hosts: SequenceNotStr[str]

    scopes: SequenceNotStr[str]
