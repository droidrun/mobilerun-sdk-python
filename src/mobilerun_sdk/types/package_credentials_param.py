# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PackageCredentialsParam"]


class PackageCredentialsParam(TypedDict, total=False):
    credential_names: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="credentialNames")]]

    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]
