# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    title: Required[str]

    agent: str

    description: str

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Optional client key.

    Reusing the same key with the same request body by the same authenticated caller
    within 24 hours returns the already-created session instead of a second one.
    """
