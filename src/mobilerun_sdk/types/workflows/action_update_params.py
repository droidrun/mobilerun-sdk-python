# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Dict

__all__ = ["ActionUpdateParams"]

class ActionUpdateParams(TypedDict, total=False):
    description: str

    name: str

    params: Dict[str, object]