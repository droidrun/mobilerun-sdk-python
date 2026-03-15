# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .device_spec_param import DeviceSpecParam

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    name: Required[str]
    """Profile name"""

    spec: Required[DeviceSpecParam]
    """Device specification"""
