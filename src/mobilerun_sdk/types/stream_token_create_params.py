# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StreamTokenCreateParams"]


class StreamTokenCreateParams(TypedDict, total=False):
    device_id: Required[Annotated[str, PropertyInfo(alias="deviceId")]]

    allowed_origins: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedOrigins")]
    """
    Exact `https://host[:port]` origins (and `http://localhost[:port]`) allowed to
    connect.
    """

    ttl_seconds: Annotated[int, PropertyInfo(alias="ttlSeconds")]
