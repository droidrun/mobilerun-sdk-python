# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrafficSessionCreateParams"]


class TrafficSessionCreateParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    expires_in_seconds: Annotated[int, PropertyInfo(alias="expiresInSeconds")]

    max_body_bytes: Annotated[int, PropertyInfo(alias="maxBodyBytes")]
