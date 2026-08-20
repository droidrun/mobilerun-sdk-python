# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProxyBuyResponse"]


class ProxyBuyResponse(BaseModel):
    """A proxy including its password. Returned only on create and single-proxy reads."""

    id: str

    country: str
    """ISO 3166-1 alpha-2 country code (lowercase)."""

    created_at: datetime = FieldInfo(alias="createdAt")

    host: str

    password: str

    port: int

    status: Literal["pending_payment", "provisioning", "active", "cancelling", "ended", "error"]
    """Lifecycle of a proxy.

    A freshly created proxy is `provisioning` — or `pending_payment` until the
    customer completes checkout — and becomes `active` once its upstream is
    assigned. `cancelling` retains full access through the paid period; when the
    subscription expires the proxy is `ended`. `error` marks a failed provisioning
    attempt.
    """

    type: Literal["dedicated_residential", "residential", "mobile"]

    username: str

    payment_url: Optional[str] = FieldInfo(alias="paymentUrl", default=None)
    """Checkout URL to complete payment while status is `pending_payment`.

    Null once paid or when no payment was required.
    """
