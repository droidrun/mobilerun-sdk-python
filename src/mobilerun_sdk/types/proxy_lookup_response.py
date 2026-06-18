# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProxyLookupResponse", "Carrier"]


class Carrier(BaseModel):
    """Mobile carrier information."""

    mcc: Optional[str] = None
    """Mobile Country Code."""

    mnc: Optional[str] = None
    """Mobile Network Code."""

    name: Optional[str] = None
    """Carrier name."""


class ProxyLookupResponse(BaseModel):
    ip: str
    """IP address of the proxy."""

    is_mobile: bool = FieldInfo(alias="isMobile")
    """Whether the IP is a mobile connection."""

    latitude: float
    """Latitude of the proxy."""

    longitude: float
    """Longitude of the proxy."""

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    carrier: Optional[Carrier] = None
    """Mobile carrier information."""

    city: Optional[str] = None
    """City of the proxy."""

    country: Optional[str] = None
    """Country of the proxy."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """ISO country code."""

    region: Optional[str] = None
    """Region of the proxy."""

    timezone: Optional[str] = None
    """Timezone of the proxy."""
