# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from .._utils import PropertyInfo

from typing import Optional

__all__ = ["EsimImportParams"]

class EsimImportParams(TypedDict, total=False):
    auto_install: Annotated[bool, PropertyInfo(alias="autoInstall")]
    """Rent OFF only: dispatch install-on-device immediately after a successful import.

    No-op when ESIM_BYO_RENT_ENABLED=true.
    """

    carrier_name: Annotated[str, PropertyInfo(alias="carrierName")]

    confirmation_code: Annotated[str, PropertyInfo(alias="confirmationCode")]

    country_code: Annotated[str, PropertyInfo(alias="countryCode")]

    device_id: Annotated[str, PropertyInfo(alias="deviceId")]
    """physedge device id to auto-install onto; requires autoInstall:true and rent OFF.

    Omit for a random pool device.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotencyKey")]
    """
    Client-supplied key; replaying the same key+request returns the original import
    instead of importing again
    """

    lpa_code: Annotated[str, PropertyInfo(alias="lpaCode")]
    """Full LPA activation code"""

    matching_id: Annotated[str, PropertyInfo(alias="matchingId")]

    msisdn: str
    """
    Self-reported E.164 MSISDN for this eSIM's line — an unverified label, never
    used for routing
    """

    name: Optional[str]
    """
    User-defined display label — NFC-normalized, up to 15 GRAPHEMES (not UTF-16 code
    units; an emoji/flag may span several). Omit/null/empty/whitespace-only leaves
    it unset.
    """

    notes: str

    smdp_address: Annotated[str, PropertyInfo(alias="smdpAddress")]
    """SM-DP+ activation host — bare hostname ONLY, no port/scheme/path."""