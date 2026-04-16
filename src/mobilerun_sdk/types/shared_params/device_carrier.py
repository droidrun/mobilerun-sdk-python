# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeviceCarrier"]


class DeviceCarrier(TypedDict, total=False):
    gsm_operator_alpha: Required[Annotated[str, PropertyInfo(alias="GsmOperatorAlpha")]]

    gsm_operator_numeric: Required[Annotated[int, PropertyInfo(alias="GsmOperatorNumeric")]]

    gsm_sim_operator_alpha: Required[Annotated[str, PropertyInfo(alias="GsmSimOperatorAlpha")]]

    gsm_sim_operator_iso_country: Required[Annotated[str, PropertyInfo(alias="GsmSimOperatorIsoCountry")]]

    gsm_sim_operator_numeric: Required[Annotated[int, PropertyInfo(alias="GsmSimOperatorNumeric")]]

    persist_sys_timezone: Required[Annotated[str, PropertyInfo(alias="PersistSysTimezone")]]
