# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrowserExecuteScriptParams"]


class BrowserExecuteScriptParams(TypedDict, total=False):
    script: Required[str]
    """
    JavaScript expression to evaluate in the device's foreground Chrome tab (CDP
    Runtime.evaluate). It is an expression, not a function body — the expression's
    value is returned (no top-level 'return'). Must evaluate to a JSON-serializable
    value; wrap multi-statement logic in an IIFE, e.g. (() => { ... ; return x })().
    """

    x_device_display_id: Annotated[int, PropertyInfo(alias="X-Device-Display-ID")]
