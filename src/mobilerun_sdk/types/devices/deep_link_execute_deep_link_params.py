# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeepLinkExecuteDeepLinkParams"]


class DeepLinkExecuteDeepLinkParams(TypedDict, total=False):
    deep_link: Required[Annotated[str, PropertyInfo(alias="deepLink")]]
    """Deep link to open (e.g. myapp://path or https://example.com/path)"""

    action: str
    """Android only: intent action to dispatch.

    Defaults to android.intent.action.VIEW.
    """

    bundle_id: Annotated[str, PropertyInfo(alias="bundleId")]
    """Reserved for targeting a specific iOS app; currently rejected as unsupported."""

    package_name: Annotated[str, PropertyInfo(alias="packageName")]
    """Android only: package to receive the intent (e.g.

    com.example.app). Omit to let the system pick the handler.
    """

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
