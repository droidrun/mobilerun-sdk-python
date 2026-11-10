# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionCatalogRetrieveParams"]


class ActionCatalogRetrieveParams(TypedDict, total=False):
    profile: Literal["agent_routine"]
    """Restrict reads to the agent routine step surface."""
