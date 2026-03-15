# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.device_spec import DeviceSpec

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Profile name"""

    spec: Required[DeviceSpec]
    """Device specification"""
