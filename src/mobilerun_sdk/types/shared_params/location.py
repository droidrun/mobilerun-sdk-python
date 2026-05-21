# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Location"]


class Location(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]
