# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CarrierCreateParams"]


class CarrierCreateParams(TypedDict, total=False):
    country: Required[str]
    """Country name"""

    mcc: Required[str]
    """Mobile Country Code"""

    mnc: Required[str]
    """Mobile Network Code"""

    operator: Required[str]
    """Operator name"""

    company: str
    """Company name"""

    country_code: str
    """Country dialing code (e.g., +1)"""

    country_iso: str
    """ISO country code"""

    detail_url: str
    """URL to carrier details page"""

    gsm_bands: str
    """Supported GSM bands"""

    lte_bands: str
    """Supported LTE bands"""

    mobile_prefix: str
    """Mobile number prefix"""

    nsn_size: str
    """National Significant Number size"""

    number_format: str
    """Phone number format"""

    protocols: str
    """Supported protocols (comma-separated)"""

    umts_bands: str
    """Supported UMTS bands"""

    website: str
    """Company website"""
