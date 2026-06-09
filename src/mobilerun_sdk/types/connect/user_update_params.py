# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    proxy_id: Annotated[Optional[str], PropertyInfo(alias="proxyId")]
    """Proxy to rebind to, or null to detach.

    Omit to leave the user's current binding unchanged — only an explicit null
    detaches.
    """
