# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from pydantic import Field as FieldInfo

__all__ = ["DeviceCarrier"]

class DeviceCarrier(BaseModel):
    gsm_operator_alpha: str = FieldInfo(alias = "GsmOperatorAlpha")

    gsm_operator_numeric: int = FieldInfo(alias = "GsmOperatorNumeric")

    gsm_sim_operator_alpha: str = FieldInfo(alias = "GsmSimOperatorAlpha")

    gsm_sim_operator_iso_country: str = FieldInfo(alias = "GsmSimOperatorIsoCountry")

    gsm_sim_operator_numeric: int = FieldInfo(alias = "GsmSimOperatorNumeric")

    persist_sys_timezone: str = FieldInfo(alias = "PersistSysTimezone")