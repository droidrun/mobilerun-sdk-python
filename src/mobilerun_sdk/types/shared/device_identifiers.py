# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeviceIdentifiers"]


class DeviceIdentifiers(BaseModel):
    bootloader_serial_number: str = FieldInfo(alias="BootloaderSerialNumber")

    identifier_android_id: str = FieldInfo(alias="IdentifierAndroidID")

    identifier_app_set_id: str = FieldInfo(alias="IdentifierAppSetID")

    identifier_bluetooth_mac: str = FieldInfo(alias="IdentifierBluetoothMAC")

    identifier_gaid: str = FieldInfo(alias="IdentifierGAID")

    identifier_gsfid: str = FieldInfo(alias="IdentifierGSFID")

    identifier_iccid: str = FieldInfo(alias="IdentifierICCID")

    identifier_imei: str = FieldInfo(alias="IdentifierIMEI")

    identifier_imsi: str = FieldInfo(alias="IdentifierIMSI")

    identifier_media_drmid: str = FieldInfo(alias="IdentifierMediaDRMID")

    identifier_meid: str = FieldInfo(alias="IdentifierMEID")

    identifier_phone_number: str = FieldInfo(alias="IdentifierPhoneNumber")

    identifier_serial: str = FieldInfo(alias="IdentifierSerial")

    identifier_wifi_mac: str = FieldInfo(alias="IdentifierWifiMAC")

    serial_number: str = FieldInfo(alias="SerialNumber")
