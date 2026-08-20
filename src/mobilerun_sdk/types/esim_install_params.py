# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EsimInstallParams"]


class EsimInstallParams(TypedDict, total=False):
    device_id: Annotated[str, PropertyInfo(alias="deviceId")]
    """physedge device id to install the eSIM onto; omit for a random pool device"""
