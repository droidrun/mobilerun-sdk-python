# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyCheckoutResponse"]


class ProxyCheckoutResponse(BaseModel):
    status: Literal["checking", "pending_payment", "provisioning", "active", "cancelling", "ended", "error"]
    """Lifecycle of a proxy.

    A freshly created proxy is `checking` while its billing identity is being
    resolved — clients should poll until a `paymentUrl` or a later status appears —
    then `provisioning` — or `pending_payment` until the customer completes checkout
    — and becomes `active` once its upstream is assigned. `cancelling` retains full
    access through the paid period; when the subscription expires the proxy is
    `ended`. `error` marks a failed provisioning attempt.
    """

    payment_url: Optional[str] = FieldInfo(alias="paymentUrl", default=None)
    """Payable checkout URL; omitted after payment."""
