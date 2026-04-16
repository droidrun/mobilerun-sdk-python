# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CarrierUpdateParams"]


class CarrierUpdateParams(TypedDict, total=False):
    company: str
    """Company name"""

    country: str
    """Country name"""

    country_code: str
    """Country dialing code"""

    country_iso: str
    """ISO country code"""

    detail_url: str
    """URL to carrier details"""

    gsm_bands: str
    """Supported GSM bands"""

    lte_bands: str
    """Supported LTE bands"""

    mobile_prefix: str
    """Mobile number prefix"""

    nsn_size: str
    """NSN size"""

    number_format: str
    """Phone number format"""

    operator: str
    """Operator name"""

    protocols: str
    """Supported protocols"""

    umts_bands: str
    """Supported UMTS bands"""

    website: str
    """Company website"""
