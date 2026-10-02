# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConnectionCreateParams"]


class ConnectionCreateParams(TypedDict, total=False):
    provider: Required[Literal["gmail"]]

    binding_hash: Annotated[str, PropertyInfo(alias="bindingHash")]
    """sha256 hex of the browser-held connect binding secret."""

    client_request_id: Annotated[str, PropertyInfo(alias="clientRequestId")]
    """Use the Idempotency-Key header."""

    label: str
