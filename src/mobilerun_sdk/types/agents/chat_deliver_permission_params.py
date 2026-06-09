# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChatDeliverPermissionParams"]


class ChatDeliverPermissionParams(TypedDict, total=False):
    permission_id: Required[Annotated[str, PropertyInfo(alias="permissionId")]]

    response: Required[Literal["once", "always", "reject"]]
