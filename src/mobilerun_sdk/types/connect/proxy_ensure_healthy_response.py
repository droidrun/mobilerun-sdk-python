# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyEnsureHealthyResponse"]


class ProxyEnsureHealthyResponse(BaseModel):
    """The outcome of an ensure-healthy check."""

    proxy_id: str = FieldInfo(alias="proxyId")

    status: Literal["healthy", "rotated", "refused", "unreachable"]
    """`healthy`: the upstream accepted the current session.

    `rotated`: the session was refused and the proxy now uses a fresh, checked
    session; retry through the proxy. `refused`: the session was refused and could
    not be replaced. `unreachable`: the upstream could not be reached; the session
    was left unchanged.
    """
