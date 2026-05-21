# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LanguageSetParams"]


class LanguageSetParams(TypedDict, total=False):
    locale: Required[str]
    """
    BCP-47 locale: a 2–3 letter language tag, optionally followed by a 4-letter
    script and/or a 2-letter region (e.g. en-US, de-DE, ja-JP, zh-Hans-CN).
    """

    restart: bool
    """Restart zygote so the locale change takes full effect immediately.

    Without it, the locale is written but won't fully apply until the next reboot.
    """

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
