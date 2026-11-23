# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ValidationCreateParams", "Manifest", "ManifestCredential"]


class ValidationCreateParams(TypedDict, total=False):
    source: Required[str]

    wait_s: Annotated[Optional[int], PropertyInfo(alias="waitS")]
    """Wait up to 25 seconds for validation to finish.

    Excess waiters return immediately.
    """

    manifest: Manifest


class ManifestCredential(TypedDict, total=False):
    name: Required[str]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]


class Manifest(TypedDict, total=False):
    credentials: Iterable[ManifestCredential]

    hosts: SequenceNotStr[str]

    scopes: SequenceNotStr[str]
