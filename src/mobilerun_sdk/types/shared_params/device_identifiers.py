# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeviceIdentifiers"]


class DeviceIdentifiers(TypedDict, total=False):
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
