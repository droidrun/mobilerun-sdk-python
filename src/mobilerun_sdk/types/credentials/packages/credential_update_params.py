# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    package_name: Required[Annotated[str, PropertyInfo(alias="packageName")]]

    label: Required[Optional[str]]
