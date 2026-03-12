# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DeviceCreateParams", "Carrier", "Identifiers", "Proxy"]


class DeviceCreateParams(TypedDict, total=False):
    device_type: Annotated[
        Literal["dedicated_physical_device", "dedicated_premium_device", "dedicated_emulated_device"],
        PropertyInfo(alias="deviceType"),
    ]

    apps: Optional[SequenceNotStr[str]]

    carrier: Carrier

    files: Optional[SequenceNotStr[str]]

    identifiers: Identifiers

    name: str

    proxy: Proxy

    smart_ip: Annotated[bool, PropertyInfo(alias="smartIp")]


class Carrier(TypedDict, total=False):
    gsm_operator_alpha: Required[Annotated[str, PropertyInfo(alias="GsmOperatorAlpha")]]

    gsm_operator_numeric: Required[Annotated[int, PropertyInfo(alias="GsmOperatorNumeric")]]

    gsm_sim_operator_alpha: Required[Annotated[str, PropertyInfo(alias="GsmSimOperatorAlpha")]]

    gsm_sim_operator_iso_country: Required[Annotated[str, PropertyInfo(alias="GsmSimOperatorIsoCountry")]]

    gsm_sim_operator_numeric: Required[Annotated[int, PropertyInfo(alias="GsmSimOperatorNumeric")]]

    persist_sys_timezone: Required[Annotated[str, PropertyInfo(alias="PersistSysTimezone")]]


class Identifiers(TypedDict, total=False):
    bootloader_serial_number: Required[Annotated[str, PropertyInfo(alias="BootloaderSerialNumber")]]

    identifier_android_id: Required[Annotated[str, PropertyInfo(alias="IdentifierAndroidID")]]

    identifier_app_set_id: Required[Annotated[str, PropertyInfo(alias="IdentifierAppSetID")]]

    identifier_bluetooth_mac: Required[Annotated[str, PropertyInfo(alias="IdentifierBluetoothMAC")]]

    identifier_gaid: Required[Annotated[str, PropertyInfo(alias="IdentifierGAID")]]

    identifier_gsfid: Required[Annotated[str, PropertyInfo(alias="IdentifierGSFID")]]

    identifier_iccid: Required[Annotated[str, PropertyInfo(alias="IdentifierICCID")]]

    identifier_imei: Required[Annotated[str, PropertyInfo(alias="IdentifierIMEI")]]

    identifier_imsi: Required[Annotated[str, PropertyInfo(alias="IdentifierIMSI")]]

    identifier_media_drmid: Required[Annotated[str, PropertyInfo(alias="IdentifierMediaDRMID")]]

    identifier_meid: Required[Annotated[str, PropertyInfo(alias="IdentifierMEID")]]

    identifier_phone_number: Required[Annotated[str, PropertyInfo(alias="IdentifierPhoneNumber")]]

    identifier_serial: Required[Annotated[str, PropertyInfo(alias="IdentifierSerial")]]

    identifier_wifi_mac: Required[Annotated[str, PropertyInfo(alias="IdentifierWifiMAC")]]

    serial_number: Required[Annotated[str, PropertyInfo(alias="SerialNumber")]]


class Proxy(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]
