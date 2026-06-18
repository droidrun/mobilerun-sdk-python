# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["HookTestParams"]


class HookTestParams(TypedDict, total=False):
    event: Optional[str]
    """Event type to simulate (default: completed)"""
