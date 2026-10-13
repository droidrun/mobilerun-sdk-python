# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowRunParams"]


class FlowRunParams(TypedDict, total=False):
    capture_screenshots: Annotated[bool, PropertyInfo(alias="captureScreenshots")]
    """
    Record and keep this run's scripts.run screenshots
    (device.screenshot(save=True)) even without flow delivery. Used for a one-off
    proof run.
    """

    payload: Dict[str, object]
